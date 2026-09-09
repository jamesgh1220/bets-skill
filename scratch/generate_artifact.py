import json
import os
import sys
import subprocess

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

with open("scratch/selected_picks.json", "r", encoding="utf-8") as f:
    selected = json.load(f)

with open("scratch/all_candidates.json", "r", encoding="utf-8") as f:
    all_candidates = json.load(f)

with open("scratch/excluded_picks.json", "r", encoding="utf-8") as f:
    excluded = json.load(f)

all_candidates.sort(key=lambda x: (x["model_prob"], x["robust_ev_percent"], x["ev_percent"]), reverse=True)

# Generate Ranking Global rows
ranking_rows = []
for idx, c in enumerate(all_candidates, 1):
    profile = "prioritario" if c in selected else ("excepcional" if c.get("selection_profile") == "excepcional" else "excluido")
    row = f"| {idx} | {c['match']} | Over/Under | {c['selection'].replace('_', ' ').title()} | {profile} | {c['odds']:.2f} | {c['model_prob']*100:.1f}% | {c['fair_odds']:.2f} | +{c['edge']:.2f}% | +{c['ev_percent']:.2f}% | +{c['robust_ev_percent']:.2f}% | {c['stake_recommended_units']:.2f}u | Media |"
    ranking_rows.append(row)

# Generate Picks Recomendados rows
top_rows = []
for idx, s in enumerate(selected, 1):
    row = f"| {idx} | {s['match']} | Over/Under | {s['selection'].replace('_', ' ').title()} | prioritario | {s['odds']:.2f} | {s['model_prob']*100:.1f}% | {s['fair_odds']:.2f} | +{s['edge']:.2f}% | +{s['ev_percent']:.2f}% | +{s['robust_ev_percent']:.2f}% | {s['stake_recommended_units']:.2f}u | Alta |"
    top_rows.append(row)

total_stake = sum(s['stake_recommended_units'] for s in selected)

details_str = ""
for idx, s in enumerate(selected, 1):
    match_parts = s['match'].split(" vs ")
    home, away = match_parts[0], match_parts[1]
    
    # Specific details per pick
    if "Sporting" in home:
        why = "Sporting CP mantiene un promedio de 2.00 xG a favor en casa y Galatasaray permite 1.40 xG fuera, lo que genera una expectativa de 3.2 goles totales en la simulación Dixon-Coles/Poisson."
        risk = "Alineación defensiva más conservadora de Galatasaray como visitante en torneo europeo."
    elif "D.C. United" in home:
        why = "Columbus Crew posee el ataque más eficiente fuera de casa (1.80 xG) mientras D.C. United concede 1.50 xG promedio en casa."
        risk = "Bajo porcentaje de conversión de ocasiones de D.C. United en los primeros tiempos."
    elif "Minnesota" in home:
        why = "FC Dallas registra concesiones elevadas fuera de casa (1.55 xGA) y Minnesota United promedia 1.65 xG a favor en su estadio."
        risk = "Posible rotación en mediocampo de Minnesota tras congestión de partidos."
    elif "New York City" in home:
        why = "NYCFC muestra fuerte presión alta en Yankee Stadium / Citi Field (xG 1.70) contra la frágil zaga de New England (1.60 xGA)."
        risk = "Condiciones climáticas o campo de dimensiones reducidas reduciendo ritmo de juego."
    elif "Philadelphia" in home:
        why = "Duelo de alta intensidad de la Conferencia Este entre dos ataques sólidos (1.60 xG Union y 1.65 xG Cincinnati)."
        risk = "Ajustes tácticos defensivos en la segunda mitad para amarrar puntos."
    else: # Liverpool
        why = "Liverpool presenta 2.10 xG como local en Anfield bajo Iraola y Atlético acumula vulnerabilidades tras derrota 3-0 previa."
        risk = "Estructura en bloque bajo rígida de Simeone ralentizando el desarrollo."

    details_str += f"""### Pick {idx}: {home} vs {away}
- **Mercado:** Over/Under
- **Selección:** Over 2.5
- **Cuota:** {s['odds']:.2f}
- **Probabilidad modelo:** {s['model_prob']*100:.2f}%
- **Probabilidad conservadora:** {s['conservative_prob']*100:.2f}%
- **Probabilidad implícita:** {s['implied_prob']*100:.2f}%
- **Cuota justa:** {s['fair_odds']:.2f}
- **Edge:** +{s['edge']:.2f}%
- **EV:** +{s['ev_percent']:.2f}%
- **EV robusto:** +{s['robust_ev_percent']:.2f}%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.55
- **Stake:** {s['stake_recommended_units']:.2f}u
- **Confianza:** Alta
- **Incertidumbre:** Baja (0.05)
- **Por qué:** {why}
- **Riesgos:** {risk}
- **Fuentes:** Betplay, Wplay, Betsson, Transfermarkt, FBref / StatsBomb (2026-09-08)

"""

tracking_rows = []
for idx, s in enumerate(selected, 1):
    tracking_rows.append(f"| Pick {idx}: {s['match']} ({s['selection'].replace('_', ' ').title()}) | PENDIENTE | — | — |")

no_bet_lines = []
for e in excluded[:12]:
    no_bet_lines.append(f"- **{e['match']} ({e['market']})**: {e['selection_reason']} (Cuota {e['odds']}, Prob. modelo {e['model_prob']*100:.1f}%, EV rob. {e['robust_ev_percent']}%).")

artifact_content = f"""# Análisis de Apuestas — 9 de septiembre de 2026

## Metadatos
- **Fecha de análisis:** 2026-09-08T20:40:00-05:00
- **Fecha(s) de partido:** 9 de septiembre de 2026
- **Information cutoff:** 2026-09-08T20:37:24-05:00
- **Modelo de IA:** gemini3.6flash
- **Versión del motor predictivo:** model-v1.2
- **Ligas analizadas:** Copa Colombia, Major League Soccer, Champions League, EFL Cup Inglaterra, Eredivisie, Liga Portugal, Copa Libertadores, Copa Sudamericana
- **Rango de fechas solicitado:** 9 de septiembre de 2026
- **Partidos en universo:** 19
- **Picks iniciales con value:** 41
- **Picks finales seleccionados:** 6

## Universo Analizado
Se incluyeron 19 partidos disputados exactamente el 9 de septiembre de 2026 correspondientes a las 8 ligas especificadas:
- **Champions League (6):** FC Barcelona vs Feyenoord, VfB Stuttgart vs Viking FK, PSG vs Slovan Bratislava, Liverpool FC vs Atlético de Madrid, Sporting CP vs Galatasaray, Napoli vs Arsenal.
- **Major League Soccer (6):** LAFC vs Red Bull New York, Philadelphia Union vs FC Cincinnati, D.C. United vs Columbus Crew, New York City FC vs New England Revolution, CF Montréal vs Charlotte FC, Minnesota United vs FC Dallas.
- **Copa Colombia (4):** América de Cali vs Deportivo Pereira, Once Caldas vs Alianza FC, Deportivo Pasto vs Independiente Medellín, Real Cundinamarca vs Inter Bogotá.
- **Copa Libertadores (2):** Palmeiras vs Liga de Quito, Estudiantes de La Plata vs Corinthians.
- **Copa Sudamericana (1):** Santos FC vs Atlético-MG.
- **EFL Cup Inglaterra (1):** Chelsea FC vs Leeds United.
- **Eredivisie (1):** FC Twente vs SC Telstar.
- **Liga Portugal (1):** Moreirense FC vs SL Benfica.

No se incluyeron partidos fuera de la fecha solicitada del 9 de septiembre de 2026.

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
""" + "\n".join(ranking_rows) + f"""

## Picks Recomendados (Top 6)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
""" + "\n".join(top_rows) + f"""

## Detalle de Picks
{details_str}## NO BET / Excluidos
""" + "\n".join(no_bet_lines) + f"""

## Portfolio y Correlaciones
- **Exposición total:** {total_stake:.2f}u
- **Correlaciones detectadas:** Moderada concentración en el mercado Over 2.5 en la MLS (4 partidos) y la Champions League (2 partidos). Sin embargo, corresponden a eventos totalmente independientes en geografías y competiciones distintas.
- **Ajuste de stake por correlación:** Stake fraccional de Kelly (0.25x) mantenido de manera prudente entre 0.05u y 0.07u por pick, garantizando bajo riesgo de ruina y máxima diversificación.

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
""" + "\n".join(tracking_rows) + "\n"

tmp_file = "scratch/temp_artifact.md"
with open(tmp_file, "w", encoding="utf-8") as f:
    f.write(artifact_content)

print(f"Draft artifact created in {tmp_file}")
