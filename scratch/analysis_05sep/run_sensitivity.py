import json
import subprocess

base_matches = {
  "gimnasia_boca": {
    "home_team": "Gimnasia Mendoza", "away_team": "Boca Juniors",
    "xg_home_for": 1.05, "xg_home_against": 1.25,
    "xg_away_for": 1.20, "xg_away_against": 1.00,
    "elo_home": 1500, "elo_away": 1630,
    "odds": { "1": 4.05, "X": 3.04, "2": 2.02 }
  },
  "ajax_psv": {
    "home_team": "Ajax", "away_team": "PSV Eindhoven",
    "xg_home_for": 1.80, "xg_home_against": 1.20,
    "xg_away_for": 2.00, "xg_away_against": 1.30,
    "elo_home": 1660, "elo_away": 1690,
    "odds": { "1": 2.60, "X": 3.75, "2": 2.40 }
  },
  "athletic_atletico": {
    "home_team": "Athletic Club", "away_team": "Atletico Madrid",
    "xg_home_for": 1.40, "xg_home_against": 1.30,
    "xg_away_for": 1.50, "xg_away_against": 1.20,
    "elo_home": 1640, "elo_away": 1690,
    "odds": { "1": 3.15, "X": 3.45, "2": 2.25 }
  }
}

scenarios = {
  "base": lambda m: m,
  "home_up": lambda m: {**m, "xg_home_for": m["xg_home_for"] + 0.15, "xg_home_against": m["xg_home_against"] - 0.10},
  "home_down": lambda m: {**m, "xg_home_for": m["xg_home_for"] - 0.15, "xg_home_against": m["xg_home_against"] + 0.10},
  "away_up": lambda m: {**m, "xg_away_for": m["xg_away_for"] + 0.15, "xg_away_against": m["xg_away_against"] - 0.10},
  "away_down": lambda m: {**m, "xg_away_for": m["xg_away_for"] - 0.15, "xg_away_against": m["xg_away_against"] + 0.10}
}

output = {}
for mid, m in base_matches.items():
    output[mid] = {}
    for sname, sfunc in scenarios.items():
        mi = sfunc({**m, "id": mid, "league": "sens"})
        with open('scratch/analysis_05sep/sens_in.json', 'w') as f:
            json.dump(mi, f)
        subprocess.run(["python3", "scripts/calc_engine.py", "--input", "scratch/analysis_05sep/sens_in.json", "--output", "scratch/analysis_05sep/sens_out.json"], check=True)
        with open('scratch/analysis_05sep/sens_out.json') as f:
            r = json.load(f)
        output[mid][sname] = r["probabilities"]

with open('scratch/analysis_05sep/sens_results.json', 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print("Sensitivity complete.")