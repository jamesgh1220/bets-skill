import json
import subprocess
import os

matches = [
    {
        "home_team": "America de Cali",
        "away_team": "Alianza FC",
        "xg_home_for": 1.6,
        "xg_home_against": 0.8,
        "xg_away_for": 1.0,
        "xg_away_against": 1.4,
        "elo_home": 1550,
        "elo_away": 1420,
        "odds": { "1": 1.36, "X": 4.40, "2": 8.50, "under_2_5": 1.95, "btts_no": 1.58 }
    },
    {
        "home_team": "Inter Palmira",
        "away_team": "Real Cundinamarca",
        "xg_home_for": 1.3,
        "xg_home_against": 1.1,
        "xg_away_for": 1.1,
        "xg_away_against": 1.3,
        "elo_home": 1380,
        "elo_away": 1350,
        "odds": { "1": 2.10, "X": 3.10, "2": 3.40, "under_2_5": 1.60 }
    },
    {
        "home_team": "Real Sociedad",
        "away_team": "Celta Vigo",
        "xg_home_for": 1.5,
        "xg_home_against": 1.2,
        "xg_away_for": 1.0,
        "xg_away_against": 1.6,
        "elo_home": 1780,
        "elo_away": 1650,
        "odds": { "1": 2.15, "X": 3.58, "2": 3.71, "under_2_5": 1.70 }
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
        "odds": { "1": 3.30, "X": 3.40, "2": 2.15, "under_2_5": 1.80, "over_2_5": 2.00 }
    },
    {
        "home_team": "Palermo",
        "away_team": "Mantova",
        "xg_home_for": 1.4,
        "xg_home_against": 1.1,
        "xg_away_for": 1.2,
        "xg_away_against": 1.3,
        "elo_home": 1520,
        "elo_away": 1480,
        "odds": { "1": 2.05, "X": 3.20, "2": 3.50, "under_2_5": 1.75 }
    },
    {
        "home_team": "Cagliari",
        "away_team": "Verona",
        "xg_home_for": 1.3,
        "xg_home_against": 1.3,
        "xg_away_for": 1.2,
        "xg_away_against": 1.4,
        "elo_home": 1620,
        "elo_away": 1600,
        "odds": { "1": 2.30, "X": 3.10, "2": 3.20, "under_2_5": 1.65 }
    }
]

os.makedirs('scratch', exist_ok=True)
all_results = []

for i, match in enumerate(matches):
    in_file = f'scratch/match_input_{i}.json'
    out_file = f'scratch/match_output_{i}.json'
    with open(in_file, 'w') as f:
        json.dump(match, f)
    
    subprocess.run(['python3', 'scripts/calc_engine.py', '--input', in_file, '--output', out_file], check=True)
    
    with open(out_file, 'r') as f:
        res = json.load(f)
        all_results.append(res)

with open('scratch/all_results.json', 'w') as f:
    json.dump(all_results, f, indent=2)

print("Done. Check scratch/all_results.json")
