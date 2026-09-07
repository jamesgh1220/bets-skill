#!/usr/bin/env python3
"""Validate and atomically publish an analysis artifact without overwriting runs."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from validate_analysis_artifact import slugify_model, validate_artifact


def publish(input_path: Path, artifacts_dir: Path, analysis_date: str, model: str) -> Path:
    content = input_path.read_text(encoding="utf-8")
    errors = validate_artifact(content, expected_date=analysis_date, expected_model=model)
    if errors:
        raise ValueError("\n".join(errors))

    artifacts_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify_model(model)
    for revision in range(1, 10000):
        destination = artifacts_dir / f"analisis-{analysis_date}--{slug}--v{revision:02d}.md"
        try:
            with destination.open("x", encoding="utf-8") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
        except FileExistsError:
            continue
        input_path.unlink()
        return destination
    raise RuntimeError("No fue posible asignar una revisión disponible.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--analysis-date", required=True, help="Fecha ISO YYYY-MM-DD")
    parser.add_argument("--model", required=True, help="Identificador de la IA ejecutora")
    parser.add_argument("--artifacts-dir", type=Path, default=Path("artifacts"))
    args = parser.parse_args()
    try:
        destination = publish(args.input, args.artifacts_dir, args.analysis_date, args.model)
    except (OSError, ValueError) as error:
        print(f"PUBLICACIÓN RECHAZADA: {error}", file=sys.stderr)
        return 1
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
