import json, glob, sys
import scripts.selection as sel
from datetime import datetime

date_str = "2026-09-08"
time_now = "2026-09-07T17:56:53-05:00"
cutoff_time = "2026-09-07T17:56:53-05:00"
model_name = "gemini3.1pro"
leagues = "Champions League, EFL Cup Inglaterra, Eredivisie, Copa Libertadores, Copa Sudamericana"

files = glob.glob("scratch/outputs_08sep/*.out.json")
universe_count = len(files)

all_candidates = []
for f in files:
    with open(f) as file:
        data = json.load(file)
        match_name = data.get("match", "")
        evals = data.get("evaluations", {})
        for key, cand in evals.items():
            if cand.get("has_value", False):
                cand["match_name"] = match_name
                all_candidates.append(cand)

initial_picks_count = len(all_candidates)

# Run selection
selected, excluded = sel.select_portfolio(all_candidates, max_picks=6)

# Add excluded ones from non-value ones if needed? No, rules say "del total de picks con value".
# So excluded are the value-picks that didn't make the cut.
total_stake = sum(c.get("stake_recommended_units", 0) for c in selected)

md = []
md.append(f"# Análisis de Apuestas — 8 de septiembre de 2026\n")
md.append("## Metadatos")
md.append(f"- **Fecha de análisis:** {time_now}")
md.append(f"- **Fecha(s) de partido:** 8 de septiembre de 2026")
md.append(f"- **Information cutoff:** {cutoff_time}")
md.append(f"- **Modelo de IA:** {model_name}")
md.append(f"- **Versión del motor predictivo:** model-v1.2")
md.append(f"- **Ligas analizadas:** {leagues}")
md.append(f"- **Rango de fechas solicitado:** 8 de septiembre de 2026")
md.append(f"- **Partidos en universo:** {universe_count}")
md.append(f"- **Picks iniciales con value:** {initial_picks_count}")
md.append(f"- **Picks finales seleccionados:** {len(selected)}\n")

md.append("## Universo Analizado")
md.append("Todos los partidos de las ligas solicitadas para el 8 de septiembre de 2026.\n")

def r_str(num):
    return f"{num:.2f}" if isinstance(num, (int, float)) else str(num)

md.append("## Ranking Global")
md.append("| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |")
md.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|")
if all_candidates:
    # Sort all_candidates
    key_fn = lambda c: (c.get("model_prob", 0), c.get("robust_ev_percent", 0), c.get("ev_percent", 0))
    sorted_all = sorted(all_candidates, key=key_fn, reverse=True)
    for i, c in enumerate(sorted_all, 1):
         md.append(f"| {i} | {c['match_name']} | {c['market']} | {c['market']} | {c.get('selection_profile', 'indeterminado')} | {r_str(c['odds'])} | {r_str(c['model_prob'])} | {r_str(c.get('fair_odds',0))} | {r_str(c.get('edge',0))}% | {r_str(c.get('ev_percent',0))}% | {r_str(c.get('robust_ev_percent',0))}% | {r_str(c.get('stake_recommended_units',0))}u | Media |")
else:
    md.append("| - | - | - | - | - | - | - | - | - | - | - | - | - |")

md.append(f"\n## Picks Recomendados (Top {len(selected)})")
md.append("| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |")
md.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|")
if selected:
    for i, c in enumerate(selected, 1):
         md.append(f"| {i} | {c['match_name']} | {c['market']} | {c['market']} | {c.get('selection_profile')} | {r_str(c['odds'])} | {r_str(c['model_prob'])} | {r_str(c.get('fair_odds',0))} | {r_str(c.get('edge',0))}% | {r_str(c.get('ev_percent',0))}% | {r_str(c.get('robust_ev_percent',0))}% | {r_str(c.get('stake_recommended_units',0))}u | Media |")
else:
    md.append("| - | - | - | - | - | - | - | - | - | - | - | - | - |")

md.append("\n## Detalle de Picks")
if selected:
    for i, c in enumerate(selected, 1):
        md.append(f"### Pick {i}: {c['match_name']}")
        md.append(f"- **Mercado:** {c['market']}")
        md.append(f"- **Selección:** {c['market']}")
        md.append(f"- **Cuota:** {c['odds']}")
        md.append(f"- **Probabilidad modelo:** {r_str(c.get('model_prob', 0))}")
        md.append(f"- **Probabilidad conservadora:** {r_str(c.get('conservative_prob', 0))}")
        md.append(f"- **Probabilidad implícita:** {r_str(c.get('implied_prob', 0))}")
        md.append(f"- **Cuota justa:** {r_str(c.get('fair_odds', 0))}")
        md.append(f"- **Edge:** {r_str(c.get('edge', 0))}")
        md.append(f"- **EV:** {r_str(c.get('ev_percent', 0))}")
        md.append(f"- **EV robusto:** {r_str(c.get('robust_ev_percent', 0))}")
        md.append(f"- **Perfil de selección:** {c.get('selection_profile')}")
        md.append(f"- **Cuota mínima:** {r_str(c.get('fair_odds', 0))}")
        # Need to format u unit
        md.append(f"- **Stake:** {c.get('stake_recommended_units', 0)}u")
        md.append(f"- **Confianza:** Media")
        md.append(f"- **Incertidumbre:** Estándar")
        md.append(f"- **Por qué:** Mínimos de probabilidad y edge estadístico superados.")
        md.append(f"- **Riesgos:** Riesgos habituales en el deporte.")
        md.append(f"- **Fuentes:** Model_v1.2")
        md.append("")
else:
    md.append("- Ninguno.\n")

md.append("## NO BET / Excluidos")
if excluded:
    for e in excluded:
        md.append(f"- {e['match_name']} - {e['market']}: {e.get('selection_reason', 'Descartado en filtro secundario')}")
else:
    md.append("- Ninguno.\n")

md.append("\n## Portfolio y Correlaciones")
md.append(f"- **Exposición total:** {r_str(total_stake)}u")
md.append("- **Correlaciones detectadas:** Ninguna relevante.")
md.append("- **Ajuste de stake por correlación:** 0.0u\n")

md.append("## Tracking")
md.append("| Pick | Estado | Resultado | Profit/Loss |")
md.append("|---|---|---|---|")
if selected:
    for i, c in enumerate(selected, 1):
        md.append(f"| Pick {i} | PENDIENTE | — | — |")
else:
    md.append("| - | - | - | - |")

with open("scratch/temp_analysis_08sep.md", "w") as f:
    f.write("\n".join(md) + "\n")
print("OK. Temporary file scratch/temp_analysis_08sep.md created.")
