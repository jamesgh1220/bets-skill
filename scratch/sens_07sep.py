import json
import subprocess
import os
import copy

BASE = '/Users/jamesgallegoh/Desktop/football-betting-intelligence-system'

def run(input_data):
    in_file = f'{BASE}/scratch/sens_in.json'
    out_file = f'{BASE}/scratch/sens_out.json'
    with open(in_file, 'w') as f:
        json.dump(input_data, f)
    subprocess.run(['python3', 'scripts/calc_engine.py', '--input', in_file, '--output', out_file], check=True, cwd=BASE)
    with open(out_file, 'r') as f:
        return json.load(f)

def sensitivity(match, label, market_key):
    print(f"===== {label} =====")
    base = run(match)
    ev_base = base["evaluations"][market_key]["ev_percent"]
    p_base = base["evaluations"][market_key]["model_prob"]
    print(f"  Base: p={p_base} EV={ev_base}% odds={match['odds'][market_key]}")
    variations = {
        "home_for+0.3": ("xg_home_for", +0.3),
        "home_for-0.3": ("xg_home_for", -0.3),
        "home_against+0.3": ("xg_home_against", +0.3),
        "home_against-0.3": ("xg_home_against", -0.3),
        "away_for+0.3": ("xg_away_for", +0.3),
        "away_for-0.3": ("xg_away_for", -0.3),
        "away_against+0.3": ("xg_away_against", +0.3),
        "away_against-0.3": ("xg_away_against", -0.3),
        "elo_home+50": ("elo_home", +50),
        "elo_home-50": ("elo_home", -50),
        "elo_away+50": ("elo_away", +50),
        "elo_away-50": ("elo_away", -50),
    }
    evs = []
    ps = []
    for name, (key, delta) in variations.items():
        m2 = copy.deepcopy(match)
        m2[key] = m2.get(key, 0) + delta
        res = run(m2)
        ev = res["evaluations"][market_key]["ev_percent"]
        p = res["evaluations"][market_key]["model_prob"]
        evs.append(ev)
        ps.append(p)
        print(f"  {name}: p={p} EV={ev}%")
    print(f"  Min EV={min(evs)} Max EV={max(evs)} Min p={min(ps)} Max p={max(ps)}")
    print()

sensitivity({
    "home_team": "Getafe", "away_team": "Celta Vigo",
    "xg_home_for": 0.72, "xg_home_against": 1.0, "xg_away_for": 0.8, "xg_away_against": 1.3,
    "elo_home": 1650, "elo_away": 1600,
    "odds": { "1": 2.55, "X": 2.95, "2": 3.40 }
}, "Getafe home (1) @2.55", "1")

sensitivity({
    "home_team": "Barracas Central", "away_team": "Argentinos Juniors",
    "xg_home_for": 0.9, "xg_home_against": 1.1, "xg_away_for": 1.4, "xg_away_against": 0.8,
    "elo_home": 1450, "elo_away": 1620,
    "odds": { "1": 3.80, "X": 3.00, "2": 2.13 }
}, "Barracas home (1) @3.80", "1")

sensitivity({
    "home_team": "Llaneros", "away_team": "Deportes Tolima",
    "xg_home_for": 1.1, "xg_home_against": 1.0, "xg_away_for": 1.3, "xg_away_against": 1.1,
    "elo_home": 1480, "elo_away": 1550,
    "odds": { "1": 2.88, "X": 3.20, "2": 2.50 }
}, "Llaneros home (1) @2.88", "1")

sensitivity({
    "home_team": "Gil Vicente", "away_team": "Academico de Viseu",
    "xg_home_for": 1.45, "xg_home_against": 0.85, "xg_away_for": 0.85, "xg_away_against": 1.45,
    "elo_home": 1550, "elo_away": 1420,
    "odds": { "1": 1.95, "X": 3.50, "2": 4.30 }
}, "Gil Vicente home (1) @1.95", "1")

sensitivity({
    "home_team": "Barracas Central", "away_team": "Argentinos Juniors",
    "xg_home_for": 0.9, "xg_home_against": 1.1, "xg_away_for": 1.4, "xg_away_against": 0.8,
    "elo_home": 1450, "elo_away": 1620,
    "odds": { "under_2_5": 1.75 }
}, "Barracas Under 2.5 @1.75", "under_2_5")

sensitivity({
    "home_team": "Cagliari", "away_team": "Lecce",
    "xg_home_for": 1.19, "xg_home_against": 1.0, "xg_away_for": 0.83, "xg_away_against": 1.2,
    "elo_home": 1580, "elo_away": 1540,
    "odds": { "under_2_5": 1.75 }
}, "Cagliari Under 2.5 @1.75", "under_2_5")

sensitivity({
    "home_team": "Estoril", "away_team": "Arouca",
    "xg_home_for": 1.10, "xg_home_against": 1.40, "xg_away_for": 1.20, "xg_away_against": 1.10,
    "elo_home": 1480, "elo_away": 1520,
    "odds": { "2": 3.35 }
}, "Arouca away (2) @3.35", "2")

sensitivity({
    "home_team": "Elche", "away_team": "Real Sociedad",
    "xg_home_for": 1.2, "xg_home_against": 1.5, "xg_away_for": 1.3, "xg_away_against": 1.1,
    "elo_home": 1520, "elo_away": 1680,
    "odds": { "under_2_5": 2.08 }
}, "Elche Under 2.5 @2.08", "under_2_5")