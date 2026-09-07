import json
import subprocess
import os

matches = [
    {
        "home_team": "Barracas Central",
        "away_team": "Argentinos Juniors",
        "xg_home_for": 0.9,
        "xg_home_against": 1.1,
        "xg_away_for": 1.4,
        "xg_away_against": 0.8,
        "elo_home": 1450,
        "elo_away": 1620,
        "odds": { "1": 3.80, "X": 3.00, "2": 2.13, "under_2_5": 1.75, "btts_no": 1.65 }
    },
    {
        "home_team": "Llaneros",
        "away_team": "Deportes Tolima",
        "xg_home_for": 1.1,
        "xg_home_against": 1.0,
        "xg_away_for": 1.3,
        "xg_away_against": 1.1,
        "elo_home": 1480,
        "elo_away": 1550,
        "odds": { "1": 2.88, "X": 3.20, "2": 2.50, "under_2_5": 1.62, "btts_no": 1.83 }
    },
    {
        "home_team": "Getafe",
        "away_team": "Celta Vigo",
        "xg_home_for": 0.72,
        "xg_home_against": 1.0,
        "xg_away_for": 0.8,
        "xg_away_against": 1.3,
        "elo_home": 1650,
        "elo_away": 1600,
        "odds": { "1": 2.55, "X": 2.95, "2": 3.40, "under_2_5": 1.42, "btts_no": 1.60 }
    },
    {
        "home_team": "Elche",
        "away_team": "Real Sociedad",
        "xg_home_for": 1.2,
        "xg_home_against": 1.5,
        "xg_away_for": 1.3,
        "xg_away_against": 1.1,
        "elo_home": 1520,
        "elo_away": 1680,
        "odds": { "1": 3.10, "X": 3.30, "2": 2.37, "under_2_5": 2.08, "over_2_5": 1.80, "btts_yes": 1.62 }
    },
    {
        "home_team": "Cagliari",
        "away_team": "Lecce",
        "xg_home_for": 1.19,
        "xg_home_against": 1.0,
        "xg_away_for": 0.83,
        "xg_away_against": 1.2,
        "elo_home": 1580,
        "elo_away": 1540,
        "odds": { "1": 2.05, "X": 3.40, "2": 4.30, "under_2_5": 1.75, "btts_no": 1.71 }
    },
    {
        "home_team": "Udinese",
        "away_team": "Lazio",
        "xg_home_for": 1.45,
        "xg_home_against": 1.2,
        "xg_away_for": 1.24,
        "xg_away_against": 0.8,
        "elo_home": 1580,
        "elo_away": 1700,
        "odds": { "1": 2.65, "X": 3.13, "2": 2.85, "under_2_5": 1.63, "btts_no": 1.80 }
    },
    {
        "home_team": "Estoril",
        "away_team": "Arouca",
        "xg_home_for": 1.10,
        "xg_home_against": 1.40,
        "xg_away_for": 1.20,
        "xg_away_against": 1.10,
        "elo_home": 1480,
        "elo_away": 1520,
        "odds": { "1": 2.20, "X": 3.40, "2": 3.35, "under_2_5": 1.80, "btts_yes": 1.68 }
    },
    {
        "home_team": "Gil Vicente",
        "away_team": "Academico de Viseu",
        "xg_home_for": 1.45,
        "xg_home_against": 0.85,
        "xg_away_for": 0.85,
        "xg_away_against": 1.45,
        "elo_home": 1550,
        "elo_away": 1420,
        "odds": { "1": 1.95, "X": 3.50, "2": 4.30, "under_2_5": 1.69, "btts_no": 1.75 }
    }
]

os.makedirs('scratch', exist_ok=True)
all_results = []

for i, match in enumerate(matches):
    in_file = f'scratch/match_07sep_{i}.json'
    out_file = f'scratch/match_output_07sep_{i}.json'
    with open(in_file, 'w') as f:
        json.dump(match, f, indent=2)
    
    subprocess.run(['python3', 'scripts/calc_engine.py', '--input', in_file, '--output', out_file], check=True)
    
    with open(out_file, 'r') as f:
        res = json.load(f)
        all_results.append(res)

with open('scratch/all_results_07sep.json', 'w') as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)

print("Done. Check scratch/all_results_07sep.json")
for r in all_results:
    print(f"\n{r['match']}:")
    for market, ev in r['evaluations'].items():
        if ev['has_value']:
            print(f"  {market}: Prob={ev['model_prob']:.3f}, Fair={ev['fair_odds']}, Odds={ev['odds']}, Edge={ev['edge']}%, EV={ev['ev_percent']}%, Stake={ev['stake_recommended_units']}")
