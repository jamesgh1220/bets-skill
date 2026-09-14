import json
import subprocess
import sys
import os

sys.path.append(os.getcwd())

from scripts.selection import select_portfolio

# Match definitions
matches_input = [
    {
        "home_team": "Leeds United",
        "away_team": "Newcastle United",
        "league": "Premier League",
        "xg_home_for": 1.28,
        "xg_home_against": 1.45,
        "xg_away_for": 1.62,
        "xg_away_against": 1.25,
        "elo_home": 1655,
        "elo_away": 1770,
        "odds": {
            "1": 2.30, "X": 3.50, "2": 3.00,
            "over_1_5": 1.25, "under_1_5": 3.80,
            "over_2_5": 1.80, "under_2_5": 2.00,
            "over_3_5": 3.00, "under_3_5": 1.38,
            "btts_yes": 1.68, "btts_no": 2.15,
            "1x": 1.38, "x2": 1.60, "12": 1.30,
            "dnb_home": 1.65, "dnb_away": 2.15
        }
    },
    {
        "home_team": "Villarreal",
        "away_team": "Real Betis",
        "league": "La Liga",
        "xg_home_for": 1.55,
        "xg_home_against": 1.30,
        "xg_away_for": 1.35,
        "xg_away_against": 1.40,
        "elo_home": 1740,
        "elo_away": 1710,
        "odds": {
            "1": 1.95, "X": 3.90, "2": 3.60,
            "over_1_5": 1.24, "under_1_5": 4.00,
            "over_2_5": 1.78, "under_2_5": 2.05,
            "over_3_5": 2.95, "under_3_5": 1.40,
            "btts_yes": 1.68, "btts_no": 2.15,
            "1x": 1.28, "x2": 1.85, "12": 1.26,
            "dnb_home": 1.45, "dnb_away": 2.65
        }
    },
    {
        "home_team": "Torino",
        "away_team": "Roma",
        "league": "Serie A",
        "xg_home_for": 1.05,
        "xg_home_against": 1.45,
        "xg_away_for": 1.52,
        "xg_away_against": 1.10,
        "elo_home": 1610,
        "elo_away": 1755,
        "odds": {
            "1": 6.50, "X": 4.20, "2": 1.53,
            "over_1_5": 1.32, "under_1_5": 3.35,
            "over_2_5": 2.02, "under_2_5": 1.80,
            "over_3_5": 3.60, "under_3_5": 1.28,
            "btts_yes": 2.05, "btts_no": 1.75,
            "1x": 2.50, "x2": 1.12, "12": 1.22,
            "dnb_home": 4.40, "dnb_away": 1.20
        }
    },
    {
        "home_team": "Como",
        "away_team": "Parma",
        "league": "Serie A",
        "xg_home_for": 1.65,
        "xg_home_against": 1.05,
        "xg_away_for": 0.90,
        "xg_away_against": 1.75,
        "elo_home": 1680,
        "elo_away": 1520,
        "odds": {
            "1": 1.20, "X": 6.50, "2": 16.00,
            "over_1_5": 1.16, "under_1_5": 5.20,
            "over_2_5": 1.55, "under_2_5": 2.45,
            "over_3_5": 2.40, "under_3_5": 1.55,
            "btts_yes": 2.10, "btts_no": 1.72,
            "1x": 1.03, "x2": 4.50, "12": 1.11,
            "dnb_home": 1.06, "dnb_away": 10.00
        }
    },
    {
        "home_team": "Internazionale",
        "away_team": "Udinese",
        "league": "Serie A",
        "xg_home_for": 2.10,
        "xg_home_against": 0.85,
        "xg_away_for": 0.95,
        "xg_away_against": 1.65,
        "elo_home": 1880,
        "elo_away": 1560,
        "odds": {
            "1": 1.22, "X": 6.50, "2": 13.00,
            "over_1_5": 1.15, "under_1_5": 5.40,
            "over_2_5": 1.50, "under_2_5": 2.55,
            "over_3_5": 2.25, "under_3_5": 1.62,
            "btts_yes": 2.10, "btts_no": 1.72,
            "1x": 1.04, "x2": 4.20, "12": 1.11,
            "dnb_home": 1.07, "dnb_away": 8.50
        }
    },
    {
        "home_team": "Rio Ave",
        "away_team": "Estrela da Amadora",
        "league": "Liga Portugal",
        "xg_home_for": 1.15,
        "xg_home_against": 1.20,
        "xg_away_for": 1.05,
        "xg_away_against": 1.25,
        "elo_home": 1540,
        "elo_away": 1510,
        "odds": {
            "1": 2.63, "X": 3.60, "2": 2.63,
            "over_1_5": 1.38, "under_1_5": 3.00,
            "over_2_5": 2.15, "under_2_5": 1.70,
            "over_3_5": 4.00, "under_3_5": 1.24,
            "btts_yes": 1.90, "btts_no": 1.90,
            "1x": 1.48, "x2": 1.48, "12": 1.30,
            "dnb_home": 1.85, "dnb_away": 1.85
        }
    },
    {
        "home_team": "Moreirense",
        "away_team": "Marítimo",
        "league": "Liga Portugal",
        "xg_home_for": 1.20,
        "xg_home_against": 1.15,
        "xg_away_for": 1.10,
        "xg_away_against": 1.25,
        "elo_home": 1550,
        "elo_away": 1520,
        "odds": {
            "1": 2.50, "X": 3.40, "2": 2.80,
            "over_1_5": 1.35, "under_1_5": 3.20,
            "over_2_5": 2.10, "under_2_5": 1.72,
            "over_3_5": 3.80, "under_3_5": 1.26,
            "btts_yes": 1.85, "btts_no": 1.95,
            "1x": 1.42, "x2": 1.53, "12": 1.32,
            "dnb_home": 1.75, "dnb_away": 1.95
        }
    },
    {
        "home_team": "Sporting Braga",
        "away_team": "Estoril Praia",
        "league": "Liga Portugal",
        "xg_home_for": 1.90,
        "xg_home_against": 1.05,
        "xg_away_for": 1.05,
        "xg_away_against": 1.70,
        "elo_home": 1720,
        "elo_away": 1530,
        "odds": {
            "1": 1.44, "X": 4.75, "2": 7.00,
            "over_1_5": 1.20, "under_1_5": 4.40,
            "over_2_5": 1.65, "under_2_5": 2.25,
            "over_3_5": 2.60, "under_3_5": 1.48,
            "btts_yes": 1.80, "btts_no": 2.00,
            "1x": 1.10, "x2": 2.80, "12": 1.18,
            "dnb_home": 1.15, "dnb_away": 5.00
        }
    }
]

# Run calc_engine for each match
all_results = []
all_candidates = []
all_evaluations = []

for match in matches_input:
    inp_file = "scratch/temp_match.json"
    out_file = "scratch/temp_out.json"
    with open(inp_file, "w", encoding="utf-8") as f:
        json.dump(match, f, indent=2)
    
    res = subprocess.run(
        ["python3", "scripts/calc_engine.py", "--input", inp_file, "--output", out_file],
        capture_output=True, text=True
    )
    if res.returncode != 0:
        print(f"Error running calc_engine for {match['home_team']}: {res.stderr}")
        sys.exit(1)
        
    with open(out_file, "r", encoding="utf-8") as f:
        out_data = json.load(f)
        
    all_results.append(out_data)
    
    # Extract candidates with value
    evals = out_data.get("evaluations", {})
    for m_key, ev_data in evals.items():
        ev_data["match"] = out_data["match"]
        ev_data["home_team"] = match["home_team"]
        ev_data["away_team"] = match["away_team"]
        all_evaluations.append(ev_data)
        if ev_data.get("has_value"):
            all_candidates.append(ev_data)

selected, excluded = select_portfolio(all_candidates, max_picks=6)

results_obj = {
    "all_results": all_results,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded
}

with open("scratch/full_results.json", "w", encoding="utf-8") as f:
    json.dump(results_obj, f, indent=2, ensure_ascii=False)

print(f"Total partidos procesados: {len(all_results)}")
print(f"Total candidatos con value: {len(all_candidates)}")
print(f"Picks seleccionados: {len(selected)}")
print(f"Picks excluidos: {len(excluded)}")

# Generate meta.json
picks_details = []
for s in selected:
    picks_details.append({
        "match": s["match"],
        "market": s["market"],
        "min_odds": f"{1.0 / s['conservative_prob']:.2f}" if s.get('conservative_prob', 0) > 0 else f"{s['odds']:.2f}",
        "conf": "Media-Alta" if s['model_prob'] >= 0.58 else ("Media" if s['model_prob'] >= 0.50 else "Baja"),
        "incertidumbre": "Base +/- 5.0%",
        "why": f"Selección en {s['market']} con valor cuantitativo positivo (EV {s['ev_percent']:+.2f}%, EV robusto {s['robust_ev_percent']:+.2f}%).",
        "risks": "Varianza intrínseca en fútbol, rotaciones y fluctuación de cuotas antes del kickoff.",
        "sources": "Cuotas de casas de apuestas colombianas/internacionales (Betplay/Betsson/Wplay), datos xG y Elo model-v1.2"
    })

meta_obj = {
    "analysis_date_iso": "2026-09-13T20:00:00-05:00",
    "match_dates_text": "14 de septiembre de 2026",
    "information_cutoff": "2026-09-13T20:00:00-05:00",
    "model_ia": "gemini3.6flash",
    "engine_version": "model-v1.2",
    "leagues_display": "Liga Argentina, Liga Colombiana, LaLiga, Premier League, Serie A, Liga Portugal",
    "requested_range": "14 de septiembre de 2026",
    "universe_preamble": "Universo analizado correspondiente a los partidos programados el 14 de septiembre de 2026 en las ligas solicitadas.",
    "universe_matches": [
        "- **Premier League**: Leeds United vs Newcastle United (19:00 UTC)",
        "- **LaLiga**: Villarreal vs Real Betis (19:00 UTC)",
        "- **Serie A**: Torino vs Roma (16:30 UTC)",
        "- **Serie A**: Como vs Parma (16:30 UTC)",
        "- **Serie A**: Internazionale vs Udinese (18:45 UTC)",
        "- **Liga Portugal**: Rio Ave vs Estrela da Amadora (17:45 UTC)",
        "- **Liga Portugal**: Moreirense vs Marítimo (19:15 UTC)",
        "- **Liga Portugal**: Sporting Braga vs Estoril Praia (19:45 UTC)",
        "- **Liga Argentina**: Sin partidos programados el 14 de septiembre de 2026",
        "- **Liga Colombiana**: Sin partidos programados el 14 de septiembre de 2026"
    ],
    "picks_details": picks_details,
    "fallback_source": "Motor predictivo model-v1.2, datos xG/Elo y cuotas de mercado"
}

with open("scratch/full_meta.json", "w", encoding="utf-8") as f:
    json.dump(meta_obj, f, indent=2, ensure_ascii=False)

print("meta.json y results.json generados con éxito.")
