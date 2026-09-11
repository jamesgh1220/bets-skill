import json

RANKINGS = [
    # (partido, mercado, seleccion, perfil, cuota, prob%, fair, edge%, ev%, evrob%, stake, conf, reason)
    ("Sevilla vs Valencia (LaLiga)", "over_2_5", "Más de 2.5 goles", "excluido", "2.35", "67.9", "1.47", "59.61", "59.61", "47.86", "0.11", "—", "Cuota 2.35 fuera del rango prioritario (1.50–2.20) y <3.00; no admite perfil prioritario ni excepcional."),
    ("AZ Alkmaar vs Willem II (Eredivisie)", "X", "Empate", "excluido", "9.55", "19.0", "5.27", "81.35", "81.35", "33.60", "0.02", "—", "Cuota alta con probabilidad 19.0% < 30% mínimo reforzado."),
    ("Jaguares vs Fortaleza (Liga BetPlay)", "2", "Victoria Fortaleza", "excepcional", "3.25", "42.7", "2.34", "38.71", "38.71", "22.46", "0.04", "Media", "Cumple cuota ≥3.00, probabilidad ≥30% y EV robusto ≥10%."),
    ("Venezia vs Fiorentina (Serie A)", "over_2_5", "Más de 2.5 goles", "prioritario", "1.90", "69.3", "1.44", "31.67", "31.67", "22.17", "0.09", "Media", "Cumple cuota media, probabilidad ≥55% y EV robusto ≥5%."),
    ("Sevilla vs Valencia (LaLiga)", "1", "Victoria Sevilla", "excluido", "2.35", "56.1", "1.78", "31.81", "31.81", "20.06", "0.06", "—", "Cuota 2.35 fuera del rango prioritario y <3.00."),
    ("Defensa y Justicia vs Gimnasia (Mza) (LPF Argentina)", "over_2_5", "Más de 2.5 goles", "excluido", "2.35", "55.4", "1.81", "30.17", "30.17", "18.42", "0.06", "—", "Cuota 2.35 fuera del rango prioritario y <3.00."),
    ("Defensa y Justicia vs Gimnasia (Mza) (LPF Argentina)", "2", "Victoria Gimnasia (Mza)", "excluido", "3.60", "34.1", "2.93", "22.80", "22.80", "4.80", "0.02", "—", "Cuota ≥3.00 pero EV robusto 4.8% < 10% mínimo reforzado."),
    ("Newell's Old Boys vs Vélez (LPF Argentina)", "over_2_5", "Más de 2.5 goles", "excluido", "2.60", "44.4", "2.25", "15.36", "15.36", "2.36", "0.02", "—", "Cuota fuera de rango prioritario; EV robusto < 5%."),
    ("Rennes vs Marseille (Ligue 1)", "over_2_5", "Más de 2.5 goles", "excluido", "1.57", "69.3", "1.44", "8.79", "8.79", "0.94", "0.04", "—", "EV robusto 0.94% < 5% mínimo."),
    ("Union Berlin vs Schalke 04 (Bundesliga)", "over_2_5", "Más de 2.5 goles", "excluido", "1.60", "67.2", "1.49", "7.57", "7.57", "-0.43", "0.03", "—", "EV robusto negativo."),
    ("Sevilla vs Valencia (LaLiga)", "btts_yes", "Ambos marcan (Sí)", "excluido", "2.00", "54.7", "1.83", "9.34", "9.34", "-0.66", "0.02", "—", "EV robusto negativo."),
    ("Union Berlin vs Schalke 04 (Bundesliga)", "1", "Victoria Union Berlin", "excluido", "2.11", "51.0", "1.96", "7.57", "7.57", "-2.98", "0.02", "—", "Probabilidad 51.0% < 55% y EV robusto negativo."),
    ("Santa Fe vs Tolima (Liga BetPlay)", "2", "Victoria Tolima", "excluido", "3.32", "34.6", "2.89", "14.71", "14.71", "-1.89", "0.02", "—", "Cuota ≥3.00 pero EV robusto -1.89% < 10%."),
    ("Sevilla vs Valencia (LaLiga)", "1x", "Doble oportunidad local/empate", "excluido", "1.29", "80.0", "1.25", "3.17", "3.17", "-3.28", "0.03", "—", "Cuota 1.29 < 1.50 mínimo y EV robusto negativo."),
    ("Newell's Old Boys vs Vélez (LPF Argentina)", "2", "Victoria Vélez", "excluido", "2.80", "39.5", "2.53", "10.57", "10.57", "-3.43", "0.01", "—", "EV robusto negativo y probabilidad < 55%."),
    ("Defensa y Justicia vs Gimnasia (Mza) (LPF Argentina)", "x2", "Doble oportunidad empate/visitante", "excluido", "1.70", "61.8", "1.62", "5.01", "5.01", "-3.49", "0.02", "—", "EV robusto negativo."),
    ("Venezia vs Fiorentina (Serie A)", "2", "Victoria Fiorentina", "excluido", "2.56", "40.4", "2.47", "3.50", "3.50", "-9.30", "0.01", "—", "EV robusto negativo y probabilidad < 55%."),
    ("AZ Alkmaar vs Willem II (Eredivisie)", "2", "Victoria Willem II", "excluido", "20.00", "8.4", "11.90", "68.00", "68.00", "-32.00", "0.01", "—", "Cuota alta con probabilidad 8.4% < 30% y EV robusto negativo."),
]

PICKS = {
    "1": {
        "partido": "Venezia vs Fiorentina",
        "mercado": "Over/Under 2.5 goles",
        "seleccion": "Más de 2.5 goles",
        "cuota": "1.90",
        "prob": "69.3%",
        "prob_cons": "64.3%",
        "prob_impl": "52.63%",
        "fair": "1.44",
        "edge": "31.67%",
        "ev": "31.67%",
        "evrob": "22.17%",
        "perfil": "prioritario",
        "cuota_min": "1.44",
        "stake": "0.09u",
        "confianza": "Media",
        "incertidumbre": "Media. Ambas escuadras iniciaron la temporada sin victorias (0-0-3). Fiorentina cambió de entrenador en las últimas fechas y Venezia registra bajas importantes; la muestra 2026/27 es pequeña (3 partidos) y los xG de entrada incorporan mayor incertidumbre. En el escenario pesimista (xG −15% en los cuatro insumos) el EV robusto cae a −3.2%, por lo que el valor es moderadamente sensible a los supuestos de entrada.",
        "porque": "El modelo estima goles esperados de 1.60 y 1.33 (total 2.93) y asigna 69.3% a Más de 2.5 goles frente a 52.6% implícito en la cuota 1.90 (edge 31.7%). La defensa de Fiorentina ya acumula 9 goles en contra en 3 partidos y el over 1.5 está a cuota 1.27 (prob. modelo 79.6%), coherente con una línea de gol elevada. El EV robusto (22.2%) supera el mínimo del 5% para perfil prioritario.",
        "riesgos": "Partido entre dos equipos sin triunfos puede volverse cauteloso y de ritmo bajo; el cambio de entrenador de Fiorentina añade incertidumbre táctica; si el partido se cierra temprano el over puede no llegar. La sensibilidad xG negativa erosiona el valor, por lo que el stake se mantiene en 0.09u.",
        "fuentes": "Lega Serie A (fixture oficial, viernes 11 sep 19:45), OddStorm (cuotas 1X2), Extratips (over 2.5 @ 1.90, BTTS), NerdyTips (over 1.5 @ 1.27; Fiorentina 9 goles concedidos, cambio de entrenador; Venezia con bajas). Cálculo propio vía calc_engine.py con model-v1.2.",
    },
    "2": {
        "partido": "Jaguares vs Fortaleza",
        "mercado": "1X2",
        "seleccion": "Victoria Fortaleza",
        "cuota": "3.25",
        "prob": "42.7%",
        "prob_cons": "37.7%",
        "prob_impl": "30.77%",
        "fair": "2.34",
        "edge": "38.71%",
        "ev": "38.71%",
        "evrob": "22.46%",
        "perfil": "excepcional",
        "cuota_min": "2.34",
        "stake": "0.04u",
        "confianza": "Media",
        "incertidumbre": "Alta-media. La Liga BetPlay II tiene muestra de temporada limitada y cuotas verificables con dispersión entre operadores; los xG de entrada son estimaciones basadas en forma reciente y H2H. Pese a ello, el EV robusto permanece positivo en todos los escenarios de sensibilidad (xG −15%/+15% y Elo: 14.4%–36.8%).",
        "porque": "El modelo asigna 42.7% a la victoria de Fortaleza frente a 30.8% implícito en cuota 3.25 (edge 38.7%). Los últimos 3 enfrentamientos directos los ganó Fortaleza y Jaguares no gana en 7 de sus últimos 8 partidos (4 derrotas, 3 empates). El EV robusto del 22.5% cumple el umbral reforzado del 10% para cuotas ≥3.00.",
        "riesgos": "Cuota alta (≥3.00): el mercado local en Montería y la volatilidad de la liga colombiana pueden sesgar el resultado; la muestra es pequeña y las cuotas de BetPlay varían entre operadores. Regla: máximo 1 pick excepcional, stake tope 0.25u; aquí Kelly fraccional da 0.04u.",
        "fuentes": "Dimayor (programación oficial fecha 10, 11 sep 6:15 p.m.), miCasino (cuotas 2.33/2.83/3.25 y pronóstico Fortaleza), Vanguardia (programación fecha 10), pronosticosfutbol.ai (Fortaleza 45%, doble oportunidad X2). Cálculo propio vía calc_engine.py con model-v1.2.",
    },
}

def pct(x):
    return x

header = "| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |\n|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|"

rank_rows = []
for i, r in enumerate(RANKINGS, start=1):
    rank_rows.append(f"| {i} | {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | {r[8]} | {r[9]} | {r[10]} | {r[11]} |")

pick_rows = []
for num in ("1", "2"):
    p = PICKS[num]
    pick_rows.append(f"| {num} | {p['partido']} | {p['mercado']} | {p['seleccion']} | {p['perfil']} | {p['cuota']} | {p['prob']} | {p['fair']} | {p['edge']} | {p['ev']} | {p['evrob']} | {p['stake']} | {p['confianza']} |")

lines = []
lines.append("# Análisis de Apuestas — 11 de septiembre de 2026")
lines.append("")
lines.append("## Metadatos")
lines.append("- **Fecha de análisis:** 2026-09-11T00:00:00-05:00")
lines.append("- **Fecha(s) de partido:** 2026-09-11")
lines.append("- **Information cutoff:** 2026-09-10T20:30:00-05:00")
lines.append("- **Modelo de IA:** bigpickle")
lines.append("- **Versión del motor predictivo:** model-v1.2")
lines.append("- **Ligas analizadas:** Bundesliga, Ligue 1, Serie A, LaLiga, Eredivisie, Liga Profesional Argentina, Liga BetPlay (Colombia)")
lines.append("- **Rango de fechas solicitado:** 11 de septiembre de 2026")
lines.append("- **Partidos en universo:** 10")
lines.append("- **Picks iniciales con value:** 18")
lines.append("- **Picks finales seleccionados:** 2")
lines.append("")
lines.append("## Universo Analizado")
lines.append("")
lines.append("Universo = intersección(ligas, fecha, partidos=todos). Partidos de las 7 ligas solicitadas disputados el 11 de septiembre de 2026.")
lines.append("")
lines.append("### Incluidos (10 partidos)")
lines.append("| # | Competición | Partido | Fecha/Hora |")
lines.append("|---|---|---|---|")
uni = [
    ("1", "Eredivisie", "AZ Alkmaar vs Willem II", "11 sep, 19:00 CEST"),
    ("2", "Serie A", "Venezia vs Fiorentina", "11 sep, 19:45 CEST"),
    ("3", "Ligue 1", "Rennes vs Marseille", "11 sep, 20:45 CEST"),
    ("4", "Bundesliga", "Union Berlin vs Schalke 04", "11 sep, 20:30 CET (18:30 UTC)"),
    ("5", "LaLiga", "Sevilla vs Valencia", "11 sep, 18:00 UTC"),
    ("6", "Liga Profesional Argentina", "Newell's Old Boys vs Vélez", "11 sep, 17:00 ART"),
    ("7", "Liga Profesional Argentina", "Defensa y Justicia vs Gimnasia (Mza)", "11 sep, 19:15 ART"),
    ("8", "Liga Profesional Argentina", "Boca Juniors vs Central Córdoba (SdE)", "11 sep, 21:30 ART"),
    ("9", "Liga BetPlay (Colombia)", "Jaguares vs Fortaleza", "11 sep, 18:15 COT"),
    ("10", "Liga BetPlay (Colombia)", "Independiente Santa Fe vs Deportes Tolima", "11 sep, 20:30 COT"),
]
for u in uni:
    lines.append("| " + " | ".join(u) + " |")
lines.append("")
lines.append("### Excluidos")
lines.append("")
lines.append("- **Por fecha:** Ningún partido de las ligas solicitadas fuera del 11 de septiembre de 2026 fue incluido (se descartaron partidos del 12 al 14 de septiembre de las mismas competiciones).")
lines.append("- **Por mercado:** Propuestas de esquinas/tarjetas sin disponibilidad de tasas for/against verificables de ambos equipos y cuota contrastable quedaron no disponibles; props de tiros/jugadores fuera del alcance de v1.1.")
lines.append("")
lines.append("## Ranking Global")
lines.append("")
lines.append(header)
for row in rank_rows:
    lines.append(row)
lines.append("")
lines.append("## Picks Recomendados (Top 2)")
lines.append("")
lines.append(header)
for row in pick_rows:
    lines.append(row)
lines.append("")
lines.append("## Detalle de Picks")
lines.append("")

def detail(num):
    p = PICKS[num]
    return [
        f"### Pick {num}: {p['partido']}",
        f"- **Mercado:** {p['mercado']}",
        f"- **Selección:** {p['seleccion']}",
        f"- **Cuota:** {p['cuota']}",
        f"- **Probabilidad modelo:** {p['prob']}",
        f"- **Probabilidad conservadora:** {p['prob_cons']}",
        f"- **Probabilidad implícita:** {p['prob_impl']}",
        f"- **Cuota justa:** {p['fair']}",
        f"- **Edge:** {p['edge']}",
        f"- **EV:** {p['ev']}",
        f"- **EV robusto:** {p['evrob']}",
        f"- **Perfil de selección:** {p['perfil']}",
        f"- **Cuota mínima:** {p['cuota_min']}",
        f"- **Stake:** {p['stake']}",
        f"- **Confianza:** {p['confianza']}",
        f"- **Incertidumbre:** {p['incertidumbre']}",
        f"- **Por qué:** {p['porque']}",
        f"- **Riesgos:** {p['riesgos']}",
        f"- **Fuentes:** {p['fuentes']}",
        "",
    ]

lines.extend(detail("1"))
lines.extend(detail("2"))
lines.append("## NO BET / Excluidos")
lines.append("")
for r in RANKINGS:
    if r[3] == "excluido":
        lines.append(f"- **{r[0]} · {r[1]} ({r[2]}):** {r[12]}")
lines.append("")
lines.append("## Portfolio y Correlaciones")
lines.append("")
lines.append("- **Exposición total:** 0.13u (Pick 1: 0.09u + Pick 2: 0.04u)")
lines.append("- **Correlaciones detectadas:** Ninguna relevante. Pick 1 es total de goles en Serie A (Venezia-Fiorentina) y Pick 2 es 1X2 en Liga BetPlay (Jaguares-Fortaleza): competiciones y mercados distintos, sin solapamiento de equipos.")
lines.append("- **Ajuste de stake por correlación:** No aplica; no se redujo exposición conjunta por correlación.")
lines.append("")
lines.append("## Tracking")
lines.append("")
lines.append("| Pick | Estado | Resultado | Profit/Loss |")
lines.append("|---|---|---|---|")
lines.append("| Venezia vs Fiorentina over_2_5 | PENDIENTE | — | — |")
lines.append("| Jaguares vs Fortaleza 2 | PENDIENTE | — | — |")
lines.append("")

content = "\n".join(lines)
with open("temp_artifact_11sep.md", "w", encoding="utf-8") as f:
    f.write(content)
print(content)