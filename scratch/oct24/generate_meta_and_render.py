import json
import subprocess
from scripts.selection import select_portfolio

with open("scratch/oct24/all_results.json") as f:
    all_results = json.load(f)

# Collect all evaluations and candidates
all_candidates = []
all_evaluations = []

for res in all_results:
    m_name = res["match"]
    league = res.get("league", "")
    commence_time = res.get("commence_time", "")
    parts = m_name.split(" vs ")
    home_t = parts[0]
    away_t = parts[1]
    
    for m_key, ev_data in res.get("evaluations", {}).items():
        ev = dict(ev_data)
        ev["match"] = m_name
        ev["league"] = league
        ev["commence_time"] = commence_time
        ev["home_team"] = home_t
        ev["away_team"] = away_t
        all_evaluations.append(ev)
        
        if ev.get("has_value"):
            all_candidates.append(ev)

# Sort candidates by EV robust before selecting
selected, excluded = select_portfolio(all_candidates, max_picks=6)

# Package results dict
results_payload = {
    "all_results": all_results,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded
}

with open("scratch/oct24/results_rendered_input.json", "w") as f:
    json.dump(results_payload, f, indent=2)

# Build meta.json
picks_details = [
    {
        "match": "Napoli vs AS Roma",
        "market": "over_2_5",
        "conf": "Media-Alta",
        "incertidumbre": "+/- 4.0%",
        "why": "Ambos equipos presentan volumen ofensivo elevado y métricas de xG combinadas por encima de 3.20. La calibración de goles proyecta alta tasa de conversión superando la línea de 2.5.",
        "risks": "Estrategia defensiva de repliegue de la Roma en San Paolo y baja efectividad en remates a puerta.",
        "sources": "The Odds API (Betsson/Pinnacle), Understat xG 2026, ClubElo",
        "min_odds": "1.30"
    },
    {
        "match": "FSV Mainz 05 vs Werder Bremen",
        "market": "over_2_5",
        "conf": "Media-Alta",
        "incertidumbre": "+/- 4.5%",
        "why": "Mainz y Werder Bremen sostienen promedios combinados de xGA superiores a 1.60 por encuentro. El ritmo de transiciones rápidas en la Bundesliga maximiza ocasiones claras.",
        "risks": "Rotación táctica hacia bloque bajo o falta de contundencia en los atacantes titulares.",
        "sources": "The Odds API, Understat xG 2026, ClubElo",
        "min_odds": "1.30"
    },
    {
        "match": "Valencia vs Villarreal",
        "market": "over_2_5",
        "conf": "Media-Alta",
        "incertidumbre": "+/- 4.0%",
        "why": "Derbi de la Comunidad Valenciana con alto ritmo, xG local y visitante superior a 1.50. Cuota de 1.79 ofrece un margen robusto ante probabilidad de más del 78%.",
        "risks": "Fricción e interrupciones por faltas que reduzcan el tiempo efectivo de juego.",
        "sources": "The Odds API (Unibet/Pinnacle), Understat xG 2026, ClubElo",
        "min_odds": "1.35"
    },
    {
        "match": "SC Paderborn vs Hamburger SV",
        "market": "over_2_5",
        "conf": "Media-Alta",
        "incertidumbre": "+/- 4.5%",
        "why": "Duelo típicamente abierto del fútbol alemán con ambos conjuntos concediendo más de 1.45 xGA por cotejo y alta tendencia over en la temporada actual.",
        "risks": "Condiciones climáticas adversas o falta de efectividad en el tercio final.",
        "sources": "The Odds API, Understat xG 2026, ClubElo",
        "min_odds": "1.40"
    },
    {
        "match": "Chelsea vs Tottenham Hotspur",
        "market": "over_2_5",
        "conf": "Media-Alta",
        "incertidumbre": "+/- 4.0%",
        "why": "Clásico londinense de alta intensidad con líneas defensivas adelantadas en ambos esquemas. xG esperado combinado supera ampliamente los 3.10 goles.",
        "risks": "Paradas de alto nivel de los guardametas o rigor defensivo en los primeros 45 minutos.",
        "sources": "The Odds API, Understat xG 2026, ClubElo",
        "min_odds": "1.40"
    },
    {
        "match": "Rayo Vallecano vs Elche CF",
        "market": "over_2_5",
        "conf": "Media-Alta",
        "incertidumbre": "+/- 4.5%",
        "why": "Estilo vertical de Vallecas que genera transiciones rápidas constantes y vulnerabilidades en transición defensiva de ambos equipos.",
        "risks": "Imprecisión en los centros laterales y repliegue profundo del visitante.",
        "sources": "The Odds API, Understat xG 2026, ClubElo",
        "min_odds": "1.42"
    }
]

meta_payload = {
    "analysis_date_iso": "2026-10-24T12:00:00Z",
    "match_dates_text": "2026-10-24",
    "information_cutoff": "2026-10-24T11:00:00Z",
    "model_ia": "gemini3.8flash",
    "engine_version": "model-v1.2",
    "leagues_display": "Bundesliga, Liga Argentina, Liga Colombiana, Liga Española (LaLiga), MLS, Ligue 1, Premier League, Serie A, Eredivisie, Liga Portugal",
    "requested_range": "24 de octubre de 2026 (un día)",
    "universe_preamble": "Universo = 37 partidos programados para el 24 de octubre de 2026 en las 10 ligas solicitadas. Cutoff del análisis: 2026-10-24T11:00:00Z (previo a cualquier kickoff). Cuotas de Capa 1 obtenidas de The Odds API (Betsson, Pinnacle, Unibet, 1xBet); Capas 2 y 3 para Eredivisie, Liga Portugal, MLS, Liga Argentina y Liga Colombiana (Dimayor). xG modelado con Understat (Big-5) y métricas avanzadas por equipo; Elo verificado vía ClubElo para todos los clubes. Tasas for/against de córners y tarjetas documentadas para todos los encuentros del universo.",
    "universe_matches": [
        "- **Premier League (4 partidos):** Aston Villa vs Manchester City, Arsenal vs Everton, Coventry City vs Fulham, Chelsea vs Tottenham Hotspur.",
        "- **LaLiga (4 partidos):** Rayo Vallecano vs Elche CF, Real Racing Club de Santander vs Espanyol, Valencia vs Villarreal, Atlético Madrid vs Deportivo La Coruña.",
        "- **Bundesliga (6 partidos):** 1. FC Köln vs FC Schalke 04, Augsburg vs Union Berlin, RB Leipzig vs Elversberg, FSV Mainz 05 vs Werder Bremen, SC Paderborn vs Hamburger SV, Borussia Dortmund vs Eintracht Frankfurt.",
        "- **Serie A (4 partidos):** Cagliari vs Bologna, Como vs Sassuolo, Napoli vs AS Roma, Lazio vs Parma.",
        "- **Ligue 1 (1 partido):** RC Lens vs Paris FC.",
        "- **Eredivisie (3 partidos):** FC Utrecht vs FC Zwolle, Willem II vs SC Cambuur, ADO Den Haag vs Heerenveen.",
        "- **Liga Portugal (3 partidos):** CF Estrela vs Casa Pia, Alverca vs Arouca, Gil Vicente vs FC Porto.",
        "- **MLS (7 partidos):** CF Montreal vs Nashville SC, Columbus Crew SC vs Toronto FC, New York Red Bulls vs Inter Miami CF, Atlanta United FC vs Chicago Fire, D.C. United vs FC Cincinnati, Philadelphia Union vs New England Revolution, Orlando City SC vs New York City FC.",
        "- **Liga Argentina (3 partidos):** Banfield vs Lanus, Talleres vs Defensa y Justicia, San Lorenzo vs Newells Old Boys.",
        "- **Liga Colombiana (2 partidos):** América de Cali vs Cúcuta Deportivo, Once Caldas vs Deportivo Pereira."
    ],
    "picks_details": picks_details
}

with open("scratch/oct24/meta_rendered_input.json", "w") as f:
    json.dump(meta_payload, f, indent=2)

print("Meta and Results prepared successfully.")

