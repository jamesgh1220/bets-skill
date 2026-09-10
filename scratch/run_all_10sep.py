import json
import sys
import os

sys.path.append(os.path.abspath('.'))
from scripts.calc_engine import run_ensemble, load_model_config
from scripts.selection import select_portfolio

matches_data = [
    {
        "league": "Liga BetPlay (Colombia)",
        "home_team": "Millonarios",
        "away_team": "Deportivo Cali",
        "xg_home_for": 1.35,
        "xg_home_against": 0.90,
        "xg_away_for": 1.10,
        "xg_away_against": 1.25,
        "elo_home": 1540,
        "elo_away": 1470,
        "odds": {
            "1": 1.70, "X": 3.60, "2": 5.25,
            "over_1_5": 1.38, "under_2_5": 1.70, "over_2_5": 2.15,
            "btts_yes": 2.05, "btts_no": 1.75, "1x": 1.16, "x2": 2.15, "dnb_home": 1.25
        }
    },
    {
        "league": "Copa Libertadores",
        "home_team": "Independiente del Valle",
        "away_team": "Flamengo",
        "xg_home_for": 1.65,
        "xg_home_against": 1.10,
        "xg_away_for": 1.50,
        "xg_away_against": 1.15,
        "elo_home": 1610,
        "elo_away": 1690,
        "odds": {
            "1": 2.70, "X": 3.25, "2": 2.65,
            "over_1_5": 1.33, "under_2_5": 1.78, "over_2_5": 2.05,
            "btts_yes": 1.82, "btts_no": 1.95, "1x": 1.48, "x2": 1.45, "dnb_home": 1.88
        }
    },
    {
        "league": "Copa Sudamericana",
        "home_team": "Cienciano",
        "away_team": "Montevideo City Torque",
        "xg_home_for": 1.55,
        "xg_home_against": 1.15,
        "xg_away_for": 1.20,
        "xg_away_against": 1.40,
        "elo_home": 1520,
        "elo_away": 1440,
        "odds": {
            "1": 1.62, "X": 3.75, "2": 5.50,
            "over_1_5": 1.30, "under_2_5": 1.95, "over_2_5": 1.85,
            "btts_yes": 1.87, "btts_no": 1.90, "1x": 1.14, "x2": 2.30, "dnb_home": 1.22
        }
    },
    {
        "league": "Champions League",
        "home_team": "Fenerbahçe",
        "away_team": "AS Roma",
        "xg_home_for": 1.45,
        "xg_home_against": 1.35,
        "xg_away_for": 1.55,
        "xg_away_against": 1.15,
        "elo_home": 1650,
        "elo_away": 1720,
        "odds": {
            "1": 3.10, "X": 3.50, "2": 2.20,
            "over_1_5": 1.26, "under_2_5": 2.10, "over_2_5": 1.73,
            "btts_yes": 1.65, "btts_no": 2.20, "1x": 1.65, "x2": 1.36, "dnb_home": 2.15, "dnb_away": 1.60
        }
    },
    {
        "league": "Champions League",
        "home_team": "Como",
        "away_team": "RB Leipzig",
        "xg_home_for": 1.25,
        "xg_home_against": 1.40,
        "xg_away_for": 1.70,
        "xg_away_against": 1.20,
        "elo_home": 1510,
        "elo_away": 1680,
        "odds": {
            "1": 3.80, "X": 3.60, "2": 1.95,
            "over_1_5": 1.27, "under_2_5": 2.05, "over_2_5": 1.75,
            "btts_yes": 1.62, "btts_no": 2.25, "1x": 1.85, "x2": 1.28, "dnb_away": 1.42
        }
    },
    {
        "league": "Champions League",
        "home_team": "Bayern Múnich",
        "away_team": "Bodø/Glimt",
        "xg_home_for": 2.80,
        "xg_home_against": 0.70,
        "xg_away_for": 0.85,
        "xg_away_against": 2.10,
        "elo_home": 1950,
        "elo_away": 1530,
        "odds": {
            "1": 1.14, "X": 8.50, "2": 17.00,
            "over_1_5": 1.08, "under_2_5": 3.40, "over_2_5": 1.30, "over_3_5": 1.80, "under_3_5": 2.00,
            "btts_yes": 1.95, "btts_no": 1.80, "1x": 1.02, "x2": 5.50
        }
    },
    {
        "league": "Champions League",
        "home_team": "PSV Eindhoven",
        "away_team": "Shakhtar Donetsk",
        "xg_home_for": 2.10,
        "xg_home_against": 1.05,
        "xg_away_for": 1.15,
        "xg_away_against": 1.75,
        "elo_home": 1740,
        "elo_away": 1580,
        "odds": {
            "1": 1.42, "X": 4.80, "2": 7.00,
            "over_1_5": 1.16, "under_2_5": 2.70, "over_2_5": 1.45,
            "btts_yes": 1.70, "btts_no": 2.10, "1x": 1.10, "dnb_home": 1.14
        }
    },
    {
        "league": "Champions League",
        "home_team": "Slavia Praga",
        "away_team": "RC Lens",
        "xg_home_for": 1.35,
        "xg_home_against": 1.25,
        "xg_away_for": 1.45,
        "xg_away_against": 1.20,
        "elo_home": 1620,
        "elo_away": 1660,
        "odds": {
            "1": 2.75, "X": 3.40, "2": 2.50,
            "over_1_5": 1.30, "under_2_5": 1.90, "over_2_5": 1.90,
            "btts_yes": 1.72, "btts_no": 2.08, "1x": 1.52, "x2": 1.44
        }
    },
    {
        "league": "Champions League",
        "home_team": "Manchester United",
        "away_team": "Sabah FK",
        "xg_home_for": 2.60,
        "xg_home_against": 0.65,
        "xg_away_for": 0.60,
        "xg_away_against": 2.40,
        "elo_home": 1820,
        "elo_away": 1390,
        "odds": {
            "1": 1.12, "X": 9.50, "2": 21.00,
            "over_1_5": 1.09, "under_2_5": 3.10, "over_2_5": 1.35, "over_3_5": 1.95,
            "btts_yes": 2.20, "btts_no": 1.65
        }
    },
    {
        "league": "Liga Portugal",
        "home_team": "Estrela Amadora",
        "away_team": "Braga",
        "xg_home_for": 0.95,
        "xg_home_against": 1.65,
        "xg_away_for": 1.60,
        "xg_away_against": 1.05,
        "elo_home": 1420,
        "elo_away": 1630,
        "odds": {
            "1": 4.60, "X": 3.65, "2": 1.78,
            "over_1_5": 1.28, "under_2_5": 1.95, "over_2_5": 1.85,
            "btts_yes": 1.80, "btts_no": 1.95, "1x": 2.05, "x2": 1.20, "dnb_away": 1.30
        }
    }
]

model_config = load_model_config("models/model-v1.2.json")
all_candidates = []
all_matches_output = []

for m in matches_data:
    res = run_ensemble(m, model_config)
    match_str = res["match"]
    league = m["league"]
    all_matches_output.append({"league": league, "result": res})
    for market, eval_data in res["evaluations"].items():
        if eval_data.get("has_value"):
            cand = {
                "match": match_str,
                "league": league,
                "market": market,
                "odds": eval_data["odds"],
                "model_prob": eval_data["model_prob"],
                "implied_prob": eval_data["implied_prob"],
                "fair_odds": eval_data["fair_odds"],
                "edge": eval_data["edge"],
                "ev_percent": eval_data["ev_percent"],
                "robust_ev_percent": eval_data["robust_ev_percent"],
                "stake_recommended_units": eval_data["stake_recommended_units"]
            }
            all_candidates.append(cand)

selected, excluded = select_portfolio(all_candidates, max_picks=6)

output = {
    "all_matches": all_matches_output,
    "all_candidates": all_candidates,
    "selected": selected,
    "excluded": excluded
}

os.makedirs("scratch", exist_ok=True)
with open("scratch/analysis_10sep_results.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Total candidates with value: {len(all_candidates)}")
print(f"Selected picks: {len(selected)}")
print(f"Excluded: {len(excluded)}")
