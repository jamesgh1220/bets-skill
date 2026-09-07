#!/usr/bin/env python3
"""Validate the Markdown contract for football betting analysis artifacts."""

from __future__ import annotations

import argparse
from datetime import datetime
import re
import sys
import unicodedata
from pathlib import Path


FILENAME_RE = re.compile(
    r"^analisis-(?P<date>\d{4}-\d{2}-\d{2})--(?P<model>[a-z0-9]+(?:-[a-z0-9]+)*)--v(?P<revision>\d{2,})\.md$"
)
REQUIRED_SECTIONS = (
    "## Metadatos",
    "## Universo Analizado",
    "## Ranking Global",
    "## Detalle de Picks",
    "## NO BET / Excluidos",
    "## Portfolio y Correlaciones",
    "## Tracking",
)
REQUIRED_METADATA = (
    "Fecha de análisis",
    "Fecha(s) de partido",
    "Information cutoff",
    "Modelo de IA",
    "Versión del motor predictivo",
    "Ligas analizadas",
    "Rango de fechas solicitado",
    "Partidos en universo",
    "Picks iniciales con value",
    "Picks finales seleccionados",
)
PICK_COLUMNS = (
    "Rank", "Partido", "Mercado", "Selección", "Cuota", "Prob.", "Justa",
    "Edge", "EV", "Stake", "Confianza",
)
DETAIL_FIELDS = (
    "Mercado", "Selección", "Cuota", "Probabilidad modelo",
    "Probabilidad implícita", "Cuota justa", "Edge", "EV", "Cuota mínima",
    "Stake", "Confianza", "Incertidumbre", "Por qué", "Riesgos", "Fuentes",
)


def slugify_model(model: str) -> str:
    normalized = unicodedata.normalize("NFKD", model).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    if not slug:
        raise ValueError("El identificador de modelo no contiene caracteres válidos.")
    return slug


def _section_body(lines: list[str], heading: str) -> list[str]:
    start = lines.index(heading) + 1
    end = next((i for i in range(start, len(lines)) if lines[i].startswith("## ")), len(lines))
    return lines[start:end]


def _detail_body(lines: list[str], heading: str) -> list[str]:
    start = lines.index(heading) + 1
    end = next(
        (i for i in range(start, len(lines)) if lines[i].startswith("### ") or lines[i].startswith("## ")),
        len(lines),
    )
    return lines[start:end]


def _table_rows(body: list[str]) -> list[list[str]]:
    table_lines = [line for line in body if line.startswith("|")]
    if len(table_lines) < 2:
        return []
    return [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in table_lines]


def validate_artifact(
    content: str,
    filename: str | None = None,
    expected_date: str | None = None,
    expected_model: str | None = None,
) -> list[str]:
    """Return a list of contract violations; an empty list means valid."""
    errors: list[str] = []
    lines = content.splitlines()
    if not lines or not re.fullmatch(r"# Análisis de Apuestas — .+", lines[0]):
        errors.append("El título debe ser '# Análisis de Apuestas — {fecha_en_texto}'.")

    for section in REQUIRED_SECTIONS:
        if section not in lines:
            errors.append(f"Falta la sección obligatoria '{section}'.")

    picks_heading = next((line for line in lines if re.fullmatch(r"## Picks Recomendados \(Top \d+\)", line)), None)
    if not picks_heading:
        errors.append("Falta la sección '## Picks Recomendados (Top {N})'.")

    metadata: dict[str, str] = {}
    if "## Metadatos" in lines:
        for line in _section_body(lines, "## Metadatos"):
            match = re.fullmatch(r"- \*\*(.+?):\*\*\s*(.+)", line)
            if match:
                metadata[match.group(1)] = match.group(2).strip()
        for field in REQUIRED_METADATA:
            if not metadata.get(field):
                errors.append(f"Falta el metadato obligatorio '{field}'.")

    analysis_value = metadata.get("Fecha de análisis", "")
    analysis_date = analysis_value[:10]
    if analysis_value:
        try:
            datetime.fromisoformat(analysis_value.replace("Z", "+00:00"))
        except ValueError:
            errors.append("'Fecha de análisis' debe ser ISO 8601 con fecha y hora.")
    cutoff = metadata.get("Information cutoff", "")
    if cutoff:
        try:
            datetime.fromisoformat(cutoff.replace("Z", "+00:00"))
        except ValueError:
            errors.append("'Information cutoff' debe ser ISO 8601 con fecha y hora.")
    if expected_date and analysis_date != expected_date:
        errors.append("La fecha de análisis no coincide con --analysis-date.")
    if expected_model and metadata.get("Modelo de IA"):
        if slugify_model(metadata["Modelo de IA"]) != slugify_model(expected_model):
            errors.append("'Modelo de IA' no coincide con --model.")

    selected = None
    for field in ("Partidos en universo", "Picks iniciales con value"):
        if metadata.get(field) and not re.fullmatch(r"\d+", metadata[field]):
            errors.append(f"'{field}' debe ser un entero no negativo.")
    if metadata.get("Picks finales seleccionados"):
        match = re.fullmatch(r"(\d+)", metadata["Picks finales seleccionados"])
        if not match:
            errors.append("'Picks finales seleccionados' debe ser un entero entre 0 y 6.")
        else:
            selected = int(match.group(1))
            if selected > 6:
                errors.append("No se permiten más de 6 picks finales.")

    if picks_heading:
        heading_count = int(re.search(r"\d+", picks_heading).group())
        if selected is not None and heading_count != selected:
            errors.append("El Top del encabezado no coincide con los picks finales seleccionados.")
        body = _section_body(lines, picks_heading)
        rows = _table_rows(body)
        if not rows or tuple(rows[0]) != PICK_COLUMNS:
            errors.append("La tabla de Picks Recomendados no tiene las columnas obligatorias.")
        elif selected is not None and len(rows) - 2 != selected:
            errors.append("La cantidad de filas en Picks Recomendados no coincide con los metadatos.")

    detail_count = len([line for line in lines if re.fullmatch(r"### Pick \d+: .+", line)])
    if selected is not None and detail_count != selected:
        errors.append("La cantidad de detalles de pick no coincide con los metadatos.")
    for heading in [line for line in lines if re.fullmatch(r"### Pick \d+: .+", line)]:
        body = _detail_body(lines, heading)
        found = {match.group(1) for line in body if (match := re.fullmatch(r"- \*\*(.+?):\*\*\s*.+", line))}
        for field in DETAIL_FIELDS:
            if field not in found:
                errors.append(f"{heading}: falta el campo '{field}'.")

    if "## Tracking" in lines:
        rows = _table_rows(_section_body(lines, "## Tracking"))
        tracking_header = ("Pick", "Estado", "Resultado", "Profit/Loss")
        if not rows or tuple(rows[0]) != tracking_header:
            errors.append("Tracking debe incluir la tabla Pick/Estado/Resultado/Profit/Loss.")
        elif selected is not None and len(rows) - 2 != selected:
            errors.append("La cantidad de filas de Tracking no coincide con los picks finales.")
        elif rows and any(row[1] not in {"PENDIENTE", "GANADA", "PERDIDA", "PUSH", "VOID"} for row in rows[2:]):
            errors.append("Tracking contiene un estado no permitido.")

    if filename:
        match = FILENAME_RE.fullmatch(Path(filename).name)
        if not match:
            errors.append("El nombre debe ser analisis-YYYY-MM-DD--{modelo}--vNN.md.")
        else:
            if analysis_date and match.group("date") != analysis_date:
                errors.append("La fecha del nombre no coincide con Fecha de análisis.")
            if metadata.get("Modelo de IA") and match.group("model") != slugify_model(metadata["Modelo de IA"]):
                errors.append("El modelo del nombre no coincide con Modelo de IA.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--analysis-date")
    parser.add_argument("--model")
    args = parser.parse_args()
    errors = validate_artifact(
        args.artifact.read_text(encoding="utf-8"),
        filename=args.artifact.name,
        expected_date=args.analysis_date,
        expected_model=args.model,
    )
    if errors:
        print("ARTEFACTO INVÁLIDO:", file=sys.stderr)
        print(*[f"- {error}" for error in errors], sep="\n", file=sys.stderr)
        return 1
    print(f"ARTEFACTO VÁLIDO: {args.artifact}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
