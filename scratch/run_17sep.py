"""Run the model-v1.2 engine + portfolio selection for the 3 UEL matches on 2026-09-17.

Odds source: scratch/odds_17sep/normalized_odds.json (The Odds API, layer 1), captured
2026-09-17T01:38Z. Only markets actually captured are fed to the engine; lines without
captured odds are left out (the artifact reports them as n/d). Corners/cards rates are
required by the contract and are present for both teams, but no verified corners/cards
odds exist, so those markets are unavailable (never invented).
"""

import json
import subprocess
import sys
import os

sys.path.append(os.getcwd())

from scripts.selection import select_portfolio

MATCHES = [
    {
        "home_team": "Real Sociedad",
        "away_team": "Bournemouth",
        "league": "UEFA Europa League - Jornada 1",
        "xg_home_for": 0.93,
        "xg_home_against": 1.66,
        "xg_away_for": 1.50,
        "xg_away_against": 1.60,
        "elo_home": 1768,
        "elo_away": 1859,
        "corners_home_for": 7.7,
        "corners_home_against": 3.8,
        "corners_away_for": 4.5,
        "corners_away_against": 5.0,
        "cards_home_for": 2.3,
        "cards_home_against": 3.0,
        "cards_away_for": 3.2,
        "cards_away_against": 1.5,
        "odds": {
            "1": 2.90, "X": 3.55, "2": 2.30,
            "over_2_5": 1.72, "under_2_5": 2.10,
        },
    },
    {
        "home_team": "Celtic",
        "away_team": "Ferencvaros TC",
        "league": "UEFA Europa League - Jornada 1",
        "xg_home_for": 1.28,
        "xg_home_against": 0.25,
        "xg_away_for": 1.46,
        "xg_away_against": 1.59,
        "elo_home": 1692,
        "elo_away": 1657,
        "corners_home_for": 9.7,
        "corners_home_against": 4.2,
        "corners_away_for": 4.4,
        "corners_away_against": 3.2,
        "cards_home_for": 1.0,
        "cards_home_against": 2.2,
        "cards_away_for": 1.8,
        "cards_away_against": 2.2,
        "odds": {
            "1": 1.73, "X": 4.00, "2": 4.36,
            "over_2_5": 1.56, "under_2_5": 2.40,
            "over_3_5": 2.35, "under_3_5": 1.59,
        },
    },
    {
        "home_team": "Crystal Palace",
        "away_team": "Lech Poznan",
        "league": "UEFA Europa League - Jornada 1",
        "xg_home_for": 1.63,
        "xg_home_against": 1.93,
        "xg_away_for": 2.11,
        "xg_away_against": 0.84,
        "elo_home": 1818,
        "elo_away": 1676,
        "corners_home_for": 1.0,
        "corners_home_against": 5.67,
        "corners_away_for": 7.33,
        "corners_away_against": 4.00,
        "cards_home_for": 0.67,
        "cards_home_against": 0.67,
        "cards_away_for": 1.50,
        "cards_away_against": 2.17,
        "odds": {
            "1": 1.38, "X": 5.00, "2": 7.27,
            "over_2_5": 1.62, "under_2_5": 2.25,
        },
    },
]

all_results = []
all_candidates = []
all_evaluations = []

for match in MATCHES:
    inp_file = "scratch/temp_match_17sep.json"
    out_file = "scratch/temp_out_17sep.json"
    with open(inp_file, "w", encoding="utf-8") as f:
        json.dump(match, f, indent=2, ensure_ascii=False)
    res = subprocess.run(
        ["python3", "scripts/calc_engine.py", "--input", inp_file, "--output", out_file],
        capture_output=True, text=True,
    )
    if res.returncode != 0:
        print(f"Error calc_engine {match['home_team']}: {res.stderr}")
        sys.exit(1)
    with open(out_file, "r", encoding="utf-8") as f:
        out_data = json.load(f)
    all_results.append(out_data)
    for m_key, ev_data in out_data.get("evaluations", {}).items():
        ev_data["match"] = out_data["match"]
        ev_data["home_team"] = match["home_team"]
        ev_data["away_team"] = match["away_team"]
        all_evaluations.append(ev_data)
        if ev_data.get("has_value"):
            all_candidates.append(ev_data)

all_candidates = list(all_candidates)

# Robustness filter (same policy as the 2026-09-15 artifact): the engine has no
# league-level adjustment, so cross-league 1X2 probabilities are unreliable when
# model probability diverges sharply from the implied probability. Those stay in
# the ranking (documented) but are removed from the candidate pool for selection.
ROBUST_MAX_PROB_MISMATCH = 0.20
robust_candidates = []
robustness_excluded = []
for candidate in all_candidates:
    mismatch = abs(candidate["model_prob"] - candidate["implied_prob"])
    if candidate["market"] in {"1", "X", "2"} and mismatch > ROBUST_MAX_PROB_MISMATCH:
        candidate["selection_profile"] = "excluido"
        candidate["selection_reason"] = (
            "Excluido por robustez: probabilidad-mismatch entre ligas distintas (el motor no "
            "ajusta nivel de liga); el xG de la liga de origen genera una probabilidad 1X2 no fiable."
        )
        robustness_excluded.append(candidate)
    else:
        robust_candidates.append(candidate)

selected, excluded = select_portfolio(robust_candidates, max_picks=6)
excluded.extend(robustness_excluded)

results_obj = {
    "all_results": all_results,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded,
}

with open("scratch/results_17sep.json", "w", encoding="utf-8") as f:
    json.dump(results_obj, f, indent=2, ensure_ascii=False)

print(f"Partidos: {len(all_results)} | candidatos con value: {len(all_candidates)} | seleccionados: {len(selected)} | excluidos: {len(excluded)}")
for c in all_candidates:
    print(f"  CAND {c['match']} {c['market']}: cuota {c['odds']} prob {c['model_prob']:.3f} EV {c['ev_percent']:+.2f}% rEV {c['robust_ev_percent']:+.2f}% -> {c.get('selection_profile')}")
