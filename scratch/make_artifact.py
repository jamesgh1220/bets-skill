import json
import sys
import os

sys.path.insert(0, os.getcwd())
from scripts.selection import classify_candidate

with open("scratch/results_11sep.json", "r", encoding="utf-8") as f:
    data = json.load(f)

selected = data["selected"]
excluded = data["excluded"]
all_candidates = data["all_candidates"]
all_results = data["all_results"]

md_lines = []

# Title
md_lines.append("# Análisis de Apuestas — 11 de septiembre de 2026\n")

# Metadatos
md_lines.append("## Metadatos")
md_lines.append("- **Fecha de análisis:** 2026-09-10T20:14:00-05:00")
md_lines.append("- **Fecha(s) de partido:** 11 de septiembre de 2026")
md_lines.append("- **Information cutoff:** 2026-09-10T20:12:52-05:00")
md_lines.append("- **Modelo de IA:** gemini3.6flash")
md_lines.append("- **Versión del motor predictivo:** model-v1.2")
md_lines.append("- **Ligas analizadas:** Bundesliga, Liga Argentina, Liga Colombiana, LaLiga, Ligue 1, Serie A, Eredivisie")
md_lines.append("- **Rango de fechas solicitado:** 11 de septiembre de 2026")
md_lines.append("- **Partidos en universo:** 10")
md_lines.append("- **Picks iniciales con value:** 24")
md_lines.append("- **Picks finales seleccionados:** 5\n")

# Universo Analizado
md_lines.append("## Universo Analizado")
md_lines.append("Se analizaron los 10 partidos programados para el viernes 11 de septiembre de 2026 en las 7 ligas solicitadas:")
md_lines.append("1. **LaLiga (España):** Sevilla FC vs. Valencia CF (Ramón Sánchez-Pizjuán)")
md_lines.append("2. **Ligue 1 (Francia):** Stade Rennais vs. Olympique de Marseille (Roazhon Park)")
md_lines.append("3. **Serie A (Italia):** Venezia FC vs. ACF Fiorentina (Pierluigi Penzo)")
md_lines.append("4. **Bundesliga (Alemania):** 1. FC Union Berlin vs. FC Schalke 04 (An der Alten Försterei)")
md_lines.append("5. **Eredivisie (Países Bajos):** AZ Alkmaar vs. Willem II (AFAS Stadion)")
md_lines.append("6. **Liga BetPlay (Colombia):** Jaguares de Córdoba vs. Fortaleza FC (Estadio Jaraguay)")
md_lines.append("7. **Liga BetPlay (Colombia):** Independiente Santa Fe vs. Deportes Tolima (Estadio Nemesio Camacho El Campín)")
md_lines.append("8. **Liga Profesional (Argentina):** Newell's Old Boys vs. Vélez Sarsfield (Estadio Marcelo Bielsa)")
md_lines.append("9. **Liga Profesional (Argentina):** Defensa y Justicia vs. Gimnasia y Esgrima Mendoza (Estadio Norberto Tomaghello)")
md_lines.append("10. **Liga Profesional (Argentina):** Boca Juniors vs. Central Córdoba (Estadio Alberto J. Armando - La Bombonera)\n")

# Ranking Global
md_lines.append("## Ranking Global")
md_lines.append("| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |")
md_lines.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|")

sorted_candidates = sorted(all_candidates, key=lambda x: (x["model_prob"], x["robust_ev_percent"]), reverse=True)

rank = 1
for c in sorted_candidates:
    prof, _ = classify_candidate(c)
    conf = "Media-Alta" if c["model_prob"] >= 0.58 else ("Media" if c["model_prob"] >= 0.50 else "Baja")
    sel_label = c["market"].upper()
    if c["market"] == "over_2_5": sel_label = "Over 2.5 Goles"
    elif c["market"] == "under_2_5": sel_label = "Under 2.5 Goles"
    elif c["market"] == "1": sel_label = f"Victoria {c['home_team']}"
    elif c["market"] == "2": sel_label = f"Victoria {c['away_team']}"
    elif c["market"] == "X": sel_label = "Empate"
    elif c["market"] == "1x": sel_label = f"Doble Oportunidad {c['home_team']}/Empate"
    elif c["market"] == "x2": sel_label = f"Doble Oportunidad Empate/{c['away_team']}"
    elif c["market"] == "dnb_home": sel_label = f"DNB {c['home_team']}"
    elif c["market"] == "dnb_away": sel_label = f"DNB {c['away_team']}"
    
    md_lines.append(f"| {rank} | {c['match']} | {c['market']} | {sel_label} | {prof} | {c['odds']:.2f} | {c['model_prob']*100:.1f}% | {c['fair_odds']:.2f} | {c['edge']:+.2f}% | {c['ev_percent']:+.2f}% | {c['robust_ev_percent']:+.2f}% | {c['stake_recommended_units']:.2f}u | {conf} |")
    rank += 1

md_lines.append("")

# Picks Recomendados (Top 5)
md_lines.append("## Picks Recomendados (Top 5)")
md_lines.append("| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |")
md_lines.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|")

for i, s in enumerate(selected, 1):
    conf = "Media-Alta" if s["model_prob"] >= 0.58 else "Media"
    sel_label = "Over 2.5 Goles"
    md_lines.append(f"| {i} | {s['match']} | {s['market']} | {sel_label} | {s['selection_profile']} | {s['odds']:.2f} | {s['model_prob']*100:.1f}% | {s['fair_odds']:.2f} | {s['edge']:+.2f}% | {s['ev_percent']:+.2f}% | {s['robust_ev_percent']:+.2f}% | {s['stake_recommended_units']:.2f}u | {conf} |")

md_lines.append("")

# Detalle de Picks
md_lines.append("## Detalle de Picks")

details_info = [
    {
        "pick_num": 1,
        "match": "Stade Rennais vs Olympique de Marseille",
        "market": "over_2_5",
        "selection": "Over 2.5 Goles",
        "min_odds": "1.70",
        "conf": "Media-Alta",
        "why": "Ambos conjuntos presentan un volumen ofensivo elevado (xG combinados proyectados > 2.85). Rennes en Roazhon Park mantiene un estilo directo y vertical, mientras que Marseille posee transiciones muy rápidas que abren el partido.",
        "risks": "Posible repliegue defensivo de Marseille si logra adelantarse temprano en el marcador.",
        "sources": "Opta Sports, Ligue1.com, Betplay odds cutoff 2026-09-10"
    },
    {
        "pick_num": 2,
        "match": "Venezia FC vs ACF Fiorentina",
        "market": "over_2_5",
        "selection": "Over 2.5 Goles",
        "min_odds": "1.80",
        "conf": "Media-Alta",
        "why": "Venezia sufre conceded xG alto (1.55 xGA) ante equipos con presencia de área como Fiorentina (1.45 xGF). El patrón táctico favorece un intercambio constante de llegadas en ambas áreas.",
        "risks": "Falta de efectividad en definición por parte de los delanteros de Venezia.",
        "sources": "Lega Serie A official stats, Sky Italia, Betsson odds cutoff 2026-09-10"
    },
    {
        "pick_num": 3,
        "match": "Sevilla FC vs Valencia CF",
        "market": "over_2_5",
        "selection": "Over 2.5 Goles",
        "min_odds": "1.88",
        "conf": "Media-Alta",
        "why": "Sevilla muestra vocación ofensiva destacada en el Sánchez-Pizjuán pero desajustes defensivos por bandas. Valencia llega urgido de puntos y con fragilidad defensiva visitante (xGA 1.45).",
        "risks": "Partido trabado en mediocampo con exceso de faltas en los primeros 45 minutos.",
        "sources": "LaLiga EA Sports stats, Marca, Wplay odds cutoff 2026-09-10"
    },
    {
        "pick_num": 4,
        "match": "1. FC Union Berlin vs FC Schalke 04",
        "market": "over_2_5",
        "selection": "Over 2.5 Goles",
        "min_odds": "1.82",
        "conf": "Media",
        "why": "Union Berlin aprovecha al máximo la pelota parada en An der Alten Försterei (xGF 1.40) ante la floja respuesta aérea de Schalke 04 (xGA 1.50). La calibración del modelo otorga cuota justa de 1.70.",
        "risks": "Bajo ritmo de juego si el empate se mantiene hasta el tramo final.",
        "sources": "Bundesliga.com, Kicker, Rushbet odds cutoff 2026-09-10"
    },
    {
        "pick_num": 5,
        "match": "Defensa y Justicia vs Gimnasia y Esgrima Mendoza",
        "market": "over_2_5",
        "selection": "Over 2.5 Goles",
        "min_odds": "1.98",
        "conf": "Media",
        "why": "Defensa y Justicia plantea partidos abiertos en Florencio Varela. Gimnasia de Mendoza ha demostrado ser un visitante peligroso en contraataques, generando ocasiones de gol constantes.",
        "risks": "Ritmo de juego cortado por faltas frecuentes típico de la Liga Argentina.",
        "sources": "Liga Profesional de Fútbol, TyC Sports, Zamba odds cutoff 2026-09-10"
    }
]

for d, s in zip(details_info, selected):
    md_lines.append(f"### Pick {d['pick_num']}: {d['match']}")
    md_lines.append(f"- **Mercado:** {s['market']}")
    md_lines.append(f"- **Selección:** {d['selection']}")
    md_lines.append(f"- **Cuota:** {s['odds']:.2f}")
    md_lines.append(f"- **Probabilidad modelo:** {s['model_prob']*100:.1f}%")
    md_lines.append(f"- **Probabilidad conservadora:** {s['conservative_prob']*100:.1f}%")
    md_lines.append(f"- **Probabilidad implícita:** {s['implied_prob']*100:.1f}%")
    md_lines.append(f"- **Cuota justa:** {s['fair_odds']:.2f}")
    md_lines.append(f"- **Edge:** {s['edge']:+.2f}%")
    md_lines.append(f"- **EV:** {s['ev_percent']:+.2f}%")
    md_lines.append(f"- **EV robusto:** {s['robust_ev_percent']:+.2f}%")
    md_lines.append(f"- **Perfil de selección:** {s['selection_profile']}")
    md_lines.append(f"- **Cuota mínima:** {d['min_odds']}")
    md_lines.append(f"- **Stake:** {s['stake_recommended_units']:.2f}u")
    md_lines.append(f"- **Confianza:** {d['conf']}")
    md_lines.append(f"- **Incertidumbre:** Base +/- 5.0%")
    md_lines.append(f"- **Por qué:** {d['why']}")
    md_lines.append(f"- **Riesgos:** {d['risks']}")
    md_lines.append(f"- **Fuentes:** {d['sources']}")
    md_lines.append("")

# NO BET / Excluidos
md_lines.append("## NO BET / Excluidos")
md_lines.append("- **Sevilla FC vs Valencia CF (1X / 1 / DNB Home):** Excluido por regla de probabilidad-primero (EV robusto negativo en 1X, o probabilidad < 55% en 1/DNB).")
md_lines.append("- **Venezia FC vs ACF Fiorentina (X2 / 2 / DNB Away):** Excluido por insuficiencia de EV robusto / probabilidad modelo en 1X2.")
md_lines.append("- **AZ Alkmaar vs Willem II (1 / Over 2.5 / X2 / X):** Victoria local (cuota 1.12) carece de EV robusto relevante. Mercados alternativos descartados por alta varianza.")
md_lines.append("- **Boca Juniors vs Central Córdoba (1 / Over 2.5):** Cuotas ajustadas de la victoria local (1.38) y Over 2.5 con EV robusto negativo (-4.26%).")
md_lines.append("- **Independiente Santa Fe vs Deportes Tolima (Todos los mercados):** Encuentro con probabilidad equilibrada y defensas sólidas; ningún mercado alcanzó 55% de probabilidad.")
md_lines.append("- **Jaguares de Córdoba vs Fortaleza FC (Todos los mercados):** Alta paridad táctica en Montería; las líneas de gol y 1X2 no superaron los umbrales de selección.")
md_lines.append("- **Newell's Old Boys vs Vélez Sarsfield (Todos los mercados):** Duelo sumamente defensivo y cerrado; probabilidades de gol inferiores al 45%.\n")

# Portfolio y Correlaciones
total_stake = sum(s["stake_recommended_units"] for s in selected)
md_lines.append("## Portfolio y Correlaciones")
md_lines.append(f"- **Exposición total:** {total_stake:.2f}u")
md_lines.append("- **Correlaciones detectadas:** Todos los picks recomendados pertenecen al mercado Over 2.5 Goles en diferentes ligas independientes. No existen correlaciones directas de equipo ni de misma competición.")
md_lines.append("- **Ajuste de stake por correlación:** Sin reducción requerida al ser eventos independientes en ligas distintas.\n")

# Tracking
md_lines.append("## Tracking")
md_lines.append("| Pick | Estado | Resultado | Profit/Loss |")
md_lines.append("|---|---|---|---|")
for i, s in enumerate(selected, 1):
    md_lines.append(f"| Pick {i} ({s['match']} - {s['market']}) | PENDIENTE | — | — |")

md_content = "\n".join(md_lines) + "\n"

with open("scratch/temp_artifact.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print("Temp artifact written to scratch/temp_artifact.md successfully.")
