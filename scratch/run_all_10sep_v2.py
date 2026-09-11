import json
import sys
import os

sys.path.append(os.path.abspath('.'))
from scripts.calc_engine import run_ensemble, load_model_config
from scripts.selection import select_portfolio

matches_data = [
    {
        "league": "Champions League",
        "home_team": "Fenerbahçe",
        "away_team": "AS Roma",
        "xg_home_for": 1.45,
        "xg_home_against": 1.30,
        "xg_away_for": 1.55,
        "xg_away_against": 1.10,
        "elo_home": 1650,
        "elo_away": 1720,
        "odds": {
            "1": 3.30, "X": 3.45, "2": 2.18,
            "over_1_5": 1.35, "under_2_5": 2.05, "over_2_5": 1.78,
            "btts_yes": 1.67, "btts_no": 2.15, "1x": 1.72, "x2": 1.32, "dnb_home": 2.10, "dnb_away": 1.62
        }
    },
    {
        "league": "Copa Libertadores",
        "home_team": "Independiente del Valle",
        "away_team": "Flamengo",
        "xg_home_for": 1.65,
        "xg_home_against": 1.05,
        "xg_away_for": 1.50,
        "xg_away_against": 1.15,
        "elo_home": 1610,
        "elo_away": 1690,
        "odds": {
            "1": 2.65, "X": 3.25, "2": 2.75,
            "over_1_5": 1.35, "under_2_5": 1.80, "over_2_5": 2.00,
            "btts_yes": 1.80, "btts_no": 1.98, "1x": 1.50, "x2": 1.48, "dnb_home": 1.85, "dnb_away": 1.92
        }
    },
    {
        "league": "Copa Sudamericana",
        "home_team": "Cienciano",
        "away_team": "Montevideo City Torque",
        "xg_home_for": 1.50,
        "xg_home_against": 1.15,
        "xg_away_for": 1.25,
        "xg_away_against": 1.40,
        "elo_home": 1520,
        "elo_away": 1440,
        "odds": {
            "1": 1.51, "X": 3.90, "2": 6.00,
            "over_1_5": 1.30, "under_2_5": 1.95, "over_2_5": 1.85,
            "btts_yes": 1.91, "btts_no": 1.85, "1x": 1.12, "x2": 2.55, "dnb_home": 1.20
        }
    },
    {
        "league": "Liga BetPlay (Colombia)",
        "home_team": "Millonarios",
        "away_team": "Deportivo Cali",
        "xg_home_for": 1.35,
        "xg_home_against": 0.95,
        "xg_away_for": 1.10,
        "xg_away_against": 1.30,
        "elo_home": 1540,
        "elo_away": 1470,
        "odds": {
            "1": 1.70, "X": 3.40, "2": 5.25,
            "over_1_5": 1.38, "under_2_5": 1.65, "over_2_5": 2.20,
            "btts_yes": 2.10, "btts_no": 1.67, "1x": 1.16, "x2": 2.15, "dnb_home": 1.25
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
with open("scratch/analysis_10sep_v2_results.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Total candidates with value: {len(all_candidates)}")
print(f"Selected picks: {len(selected)}")
print(f"Excluded: {len(excluded)}")

# Print summary
print("\n=== RANKING GLOBAL ===")
for i, cand in enumerate(all_candidates, 1):
    print(f"{i}. {cand['match']} | {cand['market']} | Odds: {cand['odds']} | P: {cand['model_prob']:.2%} | EV: {cand['ev_percent']:.1f}% | Robust EV: {cand['robust_ev_percent']:.1f}% | {cand['selection_profile']}")

print("\n=== SELECTED ===")
for pick in selected:
    print(f"  {pick['match']} | {pick['market']} | Odds: {pick['odds']} | P: {pick['model_prob']:.2%} | EV: {pick['ev_percent']:.1f}% | Robust EV: {pick['robust_ev_percent']:.1f}% | Stake: {pick['stake_recommended_units']}u")
