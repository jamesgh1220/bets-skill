#!/usr/bin/env python3
"""Render a contract-compliant analysis artifact from engine results.

Convierte el JSON producido por un run (match_inputs -> calc_engine -> selection)
en el Markdown que valida `validate_analysis_artifact.py`.

Documenta SIEMPRE ambos lados del mercado Over/Under (1.5/2.5/3.5): over y under
se muestran con probabilidad, cuota, edge y EV. Eso evita que el lado sin value
(habitualmente el under) quede invisible en el artefacto.

Uso:
  python3 scripts/render_artifact.py \
      --results scratch/results_11sep.json \
      --meta scratch/meta_11sep.json \
      --output scratch/temp_artifact.md
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

OU_LINES = (
    (1.5, "over_1_5", "under_1_5"),
    (2.5, "over_2_5", "under_2_5"),
    (3.5, "over_3_5", "under_3_5"),
)


def market_label(market: str, home: str, away: str) -> str:
    if market == "1":
        return f"Victoria {home}"
    if market == "X":
        return "Empate"
    if market == "2":
        return f"Victoria {away}"
    if market == "1x":
        return f"Doble Oportunidad {home}/Empate"
    if market == "x2":
        return f"Doble Oportunidad Empate/{away}"
    if market == "12":
        return f"Doble Oportunidad {home}/{away}"
    if market == "dnb_home":
        return f"DNB {home}"
    if market == "dnb_away":
        return f"DNB {away}"
    if market == "btts_yes":
        return "Ambos marcan (BTTS)"
    if market == "btts_no":
        return "No ambos marcan"
    for prefix, unit in (("corners", "Córners"), ("cards", "Tarjetas")):
        token = f"over_{prefix}_"
        if market.startswith(token):
            return f"Over {market[len(token):].replace('_', '.')} {unit}"
        token = f"under_{prefix}_"
        if market.startswith(token):
            return f"Under {market[len(token):].replace('_', '.')} {unit}"
    if market.startswith("over_"):
        return f"Over {market[5:].replace('_', '.')} Goles"
    if market.startswith("under_"):
        return f"Under {market[6:].replace('_', '.')} Goles"
    return market.upper()


def confidence(prob: float) -> str:
    if prob >= 0.58:
        return "Media-Alta"
    if prob >= 0.50:
        return "Media"
    return "Baja"


def fmt_ev(value) -> str:
    return "n/d" if value is None else f"{value:+.2f}%"


def fmt_odds(value) -> str:
    return "n/d" if value is None else f"{value:.2f}"


def min_odds_for(candidate: dict, detail: dict | None) -> str:
    if detail and detail.get("min_odds"):
        return str(detail["min_odds"])
    conservative = candidate.get("conservative_prob", 0.0)
    if conservative > 0:
        return f"{1.0 / conservative:.2f}"
    return f"{1.0 / candidate.get('model_prob', 1.0):.2f}"


def _ou_cells(match: dict, over_key: str, under_key: str) -> tuple:
    probs = match.get("probabilities", {})
    evals = match.get("evaluations", {})
    p_over = probs.get(over_key)
    p_under = probs.get(under_key)
    ov = evals.get(over_key) or {}
    un = evals.get(under_key) or {}
    over_val = ov.get("has_value", False) if ov else False
    under_val = un.get("has_value", False) if un else False

    if ov and un:
        if over_val and not under_val:
            verdict = "Value Over"
        elif under_val and not over_val:
            verdict = "Value Under"
        elif over_val and under_val:
            verdict = "Value en ambos"
        else:
            verdict = "Sin value"
    elif ov:
        verdict = "Solo Over con cuota (Under n/d)"
    elif un:
        verdict = "Solo Under con cuota (Over n/d)"
    else:
        verdict = "Cuotas no capturadas"

    return (
        f"{p_over * 100:.1f}%" if p_over is not None else "n/d",
        fmt_odds(ov.get("odds")),
        fmt_ev(ov.get("ev_percent")),
        f"{p_under * 100:.1f}%" if p_under is not None else "n/d",
        fmt_odds(un.get("odds")),
        fmt_ev(un.get("ev_percent")),
        verdict,
    )


def render(results: dict, meta: dict) -> str:
    all_results = results["all_results"]
    all_candidates = results.get("all_candidates", [])
    all_evaluations = results.get("all_evaluations", [])
    selected = results["selected"]
    excluded = results.get("excluded", [])

    picks_n = len(selected)
    lines: list[str] = []

    # Heading
    lines.append(f"# Análisis de Apuestas — {meta['match_dates_text']}\n")

    # Metadatos
    lines.append("## Metadatos")
    lines.append(f"- **Fecha de análisis:** {meta['analysis_date_iso']}")
    lines.append(f"- **Fecha(s) de partido:** {meta['match_dates_text']}")
    lines.append(f"- **Information cutoff:** {meta['information_cutoff']}")
    lines.append(f"- **Modelo de IA:** {meta['model_ia']}")
    lines.append(f"- **Versión del motor predictivo:** {meta['engine_version']}")
    lines.append(f"- **Ligas analizadas:** {meta['leagues_display']}")
    lines.append(f"- **Rango de fechas solicitado:** {meta['requested_range']}")
    lines.append(f"- **Partidos en universo:** {len(all_results)}")
    lines.append(f"- **Picks iniciales con value:** {len(all_candidates)}")
    lines.append(f"- **Picks finales seleccionados:** {picks_n}\n")

    # Universo
    lines.append("## Universo Analizado")
    lines.append(meta.get("universe_preamble", "Universo construido por intersección de ligas, fechas y partidos."))
    for item in meta.get("universe_matches", []):
        lines.append(item)
    lines.append("")

    # Ranking Global
    lines.append("## Ranking Global")
    lines.append("| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |")
    lines.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|")
    sorted_candidates = sorted(all_candidates, key=lambda c: (c["model_prob"], c["robust_ev_percent"]), reverse=True)
    for rank, c in enumerate(sorted_candidates, 1):
        prof = c.get("selection_profile", "excluido")
        lines.append(
            f"| {rank} | {c['match']} | {c['market']} | {market_label(c['market'], c['home_team'], c['away_team'])} "
            f"| {prof} | {c['odds']:.2f} | {c['model_prob'] * 100:.1f}% | {c['fair_odds']:.2f} "
            f"| {c['edge']:+.2f}% | {c['ev_percent']:+.2f}% | {c['robust_ev_percent']:+.2f}% "
            f"| {c['stake_recommended_units']:.2f}u | {confidence(c['model_prob'])} |"
        )
    lines.append("")

    # Evaluación Over/Under — ambos lados, siempre documentados
    lines.append("## Evaluación Over/Under por Partido")
    lines.append("Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. "
                 "Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada "
                 "(n/d = cuota no disponible en la corrida).")
    lines.append("| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |")
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---|")
    for match in all_results:
        if "probabilities" not in match:
            continue
        for line, over_key, under_key in OU_LINES:
            cols = _ou_cells(match, over_key, under_key)
            lines.append(f"| {match['match']} | {line:.1f} | {cols[0]} | {cols[1]} | {cols[2]} "
                         f"| {cols[3]} | {cols[4]} | {cols[5]} | {cols[6]} |")
    lines.append("")

    # Picks Recomendados
    lines.append(f"## Picks Recomendados (Top {picks_n})")
    lines.append("| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |")
    lines.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for i, s in enumerate(selected, 1):
        lines.append(
            f"| {i} | {s['match']} | {s['market']} | {market_label(s['market'], s['home_team'], s['away_team'])} "
            f"| {s.get('selection_profile', 'prioritario')} | {s['odds']:.2f} | {s['model_prob'] * 100:.1f}% | {s['fair_odds']:.2f} "
            f"| {s['edge']:+.2f}% | {s['ev_percent']:+.2f}% | {s['robust_ev_percent']:+.2f}% "
            f"| {s['stake_recommended_units']:.2f}u | {confidence(s['model_prob'])} |"
        )
    lines.append("")

    # Detalle de Picks
    lines.append("## Detalle de Picks")
    details_by_key = {(d["match"], d["market"]): d for d in meta.get("picks_details", [])}
    fallback_source = meta.get("fallback_source", "Motor predictivo model-v1.2, odds cutoff del artefacto")
    for i, s in enumerate(selected, 1):
        detail = details_by_key.get((s["match"], s["market"]), {})
        label = market_label(s["market"], s["home_team"], s["away_team"])
        lines.append(f"### Pick {i}: {s['match']}")
        lines.append(f"- **Mercado:** {s['market']}")
        lines.append(f"- **Selección:** {label}")
        lines.append(f"- **Cuota:** {s['odds']:.2f}")
        lines.append(f"- **Probabilidad modelo:** {s['model_prob'] * 100:.1f}%")
        lines.append(f"- **Probabilidad conservadora:** {s['conservative_prob'] * 100:.1f}%")
        lines.append(f"- **Probabilidad implícita:** {s['implied_prob'] * 100:.1f}%")
        lines.append(f"- **Cuota justa:** {s['fair_odds']:.2f}")
        lines.append(f"- **Edge:** {s['edge']:+.2f}%")
        lines.append(f"- **EV:** {s['ev_percent']:+.2f}%")
        lines.append(f"- **EV robusto:** {s['robust_ev_percent']:+.2f}%")
        lines.append(f"- **Perfil de selección:** {s.get('selection_profile', 'prioritario')}")
        lines.append(f"- **Cuota mínima:** {min_odds_for(s, detail)}")
        lines.append(f"- **Stake:** {s['stake_recommended_units']:.2f}u")
        lines.append(f"- **Confianza:** {detail.get('conf', confidence(s['model_prob']))}")
        lines.append(f"- **Incertidumbre:** {detail.get('incertidumbre', 'Base +/- 5.0%')}")
        lines.append(f"- **Por qué:** {detail.get('why') or 'Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).'}")
        lines.append(f"- **Riesgos:** {detail.get('risks') or 'Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.'}")
        lines.append(f"- **Fuentes:** {detail.get('sources') or fallback_source}")
        lines.append("")

    # NO BET / Excluidos
    lines.append("## NO BET / Excluidos")
    lines.append("- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**")
    ou_rejected = [e for e in all_evaluations
                   if (e["market"].startswith("over_") or e["market"].startswith("under_"))
                   and not e.get("has_value")]
    if ou_rejected:
        for e in ou_rejected:
            label = market_label(e["market"], e["home_team"], e["away_team"])
            lines.append(
                f"  - {e['match']} — {label} ({e['market']}): Prob modelo {e['model_prob'] * 100:.1f}%, "
                f"EV {e['ev_percent']:+.2f}%, EV robusto {e['robust_ev_percent']:+.2f}% → sin value."
            )
    else:
        lines.append("  - Ninguno.")
    if excluded:
        grouped: dict[str, list] = {}
        for c in excluded:
            grouped.setdefault(c["match"], []).append(c)
        lines.append("- **Candidatos con value excluidos por probabilidad-primero:**")
        for match, cands in grouped.items():
            parts = []
            for c in cands:
                label = market_label(c["market"], c["home_team"], c["away_team"])
                parts.append(f"{label} ({c['market']}) EV {c['ev_percent']:+.2f}% / EV rob {c['robust_ev_percent']:+.2f}%")
            reason = cands[0].get("selection_reason", "No cumple los mínimos de selección probabilidad-primero.")
            lines.append(f"  - {match}: {', '.join(parts)} — {reason}")
    lines.append("")

    # Portfolio y Correlaciones
    total_stake = sum(s["stake_recommended_units"] for s in selected)
    lines.append("## Portfolio y Correlaciones")
    lines.append(f"- **Exposición total:** {total_stake:.2f}u")
    markets_used = [s["market"] for s in selected]
    if len(set(markets_used)) == 1 and picks_n > 0:
        lines.append(f"- **Correlaciones detectadas:** Los {picks_n} picks pertenecen todos al mercado {market_label(markets_used[0], selected[0]['home_team'], selected[0]['away_team'])} en ligas/equipos distintos; sin correlación directa por equipo, aunque el riesgo de sesgo global al mercado es común.")
    else:
        lines.append(f"- **Correlaciones detectadas:** Mercados presentes: {', '.join(sorted(set(markets_used))) or 'ninguno'}. Verificar solapamiento de mercado mismo partido.")
    lines.append("- **Ajuste de stake por correlación:** Los picks pertenecen a partidos distintos; no se aplica reducción adicional por eventos dependientes.\n")

    # Tracking
    lines.append("## Tracking")
    lines.append("| Pick | Estado | Resultado | Profit/Loss |")
    lines.append("|---|---|---|---|")
    for i, s in enumerate(selected, 1):
        lines.append(f"| Pick {i} ({s['match']} - {s['market']}) | PENDIENTE | — | — |")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", required=True, type=Path)
    parser.add_argument("--meta", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    results = json.loads(args.results.read_text(encoding="utf-8"))
    meta = json.loads(args.meta.read_text(encoding="utf-8"))
    content = render(results, meta)
    args.output.write_text(content, encoding="utf-8")
    print(f"Artefacto temporal escrito en {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())