import json
import subprocess
import os

matches = [
    {
        "home_team": "America de Cali",
        "away_team": "Alianza Valledupar",
        "xg_home_for": 1.9,
        "xg_home_against": 0.7,
        "xg_away_for": 0.8,
        "xg_away_against": 1.8,
        "elo_home": 1550,
        "elo_away": 1420,
        "odds": { "1": 1.40, "X": 4.20, "2": 9.00, "under_2_5": 1.90, "over_2_5": 1.85, "btts_no": 1.60 }
    },
    {
        "home_team": "Deportivo Pereira",
        "away_team": "Independiente Medellin",
        "xg_home_for": 0.9,
        "xg_home_against": 1.5,
        "xg_away_for": 1.5,
        "xg_away_against": 0.9,
        "elo_home": 1430,
        "elo_away": 1560,
        "odds": { "1": 5.50, "X": 3.65, "2": 1.73, "under_2_5": 1.75, "over_2_5": 2.05, "btts_yes": 1.91 }
    },
    {
        "home_team": "Internacional FC Palmira",
        "away_team": "Real Cundinamarca",
        "xg_home_for": 1.3,
        "xg_home_against": 1.2,
        "xg_away_for": 1.2,
        "xg_away_against": 1.3,
        "elo_home": 1380,
        "elo_away": 1350,
        "odds": { "1": 1.88, "X": 3.40, "2": 4.80, "under_2_5": 1.67, "over_2_5": 2.15, "btts_yes": 1.95 }
    },
    {
        "home_team": "Real Sociedad",
        "away_team": "Celta Vigo",
        "xg_home_for": 1.6,
        "xg_home_against": 1.3,
        "xg_away_for": 1.0,
        "xg_away_against": 1.6,
        "elo_home": 1780,
        "elo_away": 1650,
        "odds": { "1": 2.10, "X": 3.75, "2": 4.10, "under_2_5": 1.80, "over_2_5": 1.95, "btts_no": 2.05 }
    },
    {
        "home_team": "Toulouse FC",
        "away_team": "Lille OSC",
        "xg_home_for": 1.1,
        "xg_home_against": 1.5,
        "xg_away_for": 1.6,
        "xg_away_against": 1.0,
        "elo_home": 1600,
        "elo_away": 1720,
        "odds": { "1": 3.55, "X": 3.50, "2": 2.24, "under_2_5": 1.80, "over_2_5": 2.00 }
    },
    {
        "home_team": "Palermo",
        "away_team": "Mantova",
        "xg_home_for": 1.6,
        "xg_home_against": 1.0,
        "xg_away_for": 1.1,
        "xg_away_against": 1.4,
        "elo_home": 1560,
        "elo_away": 1500,
        "odds": { "1": 1.65, "X": 4.00, "2": 5.00, "under_2_5": 1.80, "over_2_5": 1.90 }
    },
    {
        "home_team": "Cagliari",
        "away_team": "Hellas Verona",
        "xg_home_for": 1.3,
        "xg_home_against": 1.3,
        "xg_away_for": 1.2,
        "xg_away_against": 1.4,
        "elo_home": 1640,
        "elo_away": 1620,
        "odds": { "1": 1.91, "X": 3.50, "2": 4.20, "under_2_5": 1.68, "over_2_5": 2.10, "btts_yes": 1.95 }
    }
]

os.makedirs('scratch', exist_ok=True)
all_results = []

for i, match in enumerate(matches):
    in_file = f'scratch/match_input_03set_{i}.json'
    out_file = f'scratch/match_output_03set_{i}.json'
    with open(in_file, 'w') as f:
        json.dump(match, f)

    subprocess.run(['python3', 'scripts/calc_engine.py', '--input', in_file, '--output', out_file], check=True, cwd='/Users/jamesgallegoh/Desktop/football-betting-intelligence-system')

    with open(out_file, 'r') as f:
        res = json.load(f)
        all_results.append({"index": i, "match": match["home_team"] + " vs " + match["away_team"], **res})

with open('scratch/all_results_03set.json', 'w') as f:
    json.dump(all_results, f, indent=2)

for r in all_results:
    print("=" * 60)
    print(r["match"])
    print("prob:", r["probabilities"])
    for k, v in r["evaluations"].items():
        print(f"  {k}: odds={v['odds']} p={v['model_prob']} implied={v['implied_prob']} fair={v['fair_odds']} edge={v['edge']}% EV={v['ev_percent']}% stake={v['stake_recommended_units']} has_value={v['has_value']}")

print("\nDone. Check scratch/all_results_03set.json")
