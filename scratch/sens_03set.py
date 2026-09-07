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
    # Vary xG inputs by +/- 0.3
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
    "home_team": "Real Sociedad", "away_team": "Celta Vigo",
    "xg_home_for": 1.6, "xg_home_against": 1.3, "xg_away_for": 1.0, "xg_away_against": 1.6,
    "elo_home": 1780, "elo_away": 1650,
    "odds": { "1": 2.10, "X": 3.75, "2": 4.10 }
}, "Real Sociedad home (1) @2.10", "1")

sensitivity({
    "home_team": "Deportivo Pereira", "away_team": "Independiente Medellin",
    "xg_home_for": 0.9, "xg_home_against": 1.5, "xg_away_for": 1.5, "xg_away_against": 0.9,
    "elo_home": 1430, "elo_away": 1560,
    "odds": { "1": 5.50, "X": 3.65, "2": 1.73 }
}, "Pereira home (1) @5.50", "1")

sensitivity({
    "home_team": "Cagliari", "away_team": "Hellas Verona",
    "xg_home_for": 1.3, "xg_home_against": 1.3, "xg_away_for": 1.2, "xg_away_against": 1.4,
    "elo_home": 1640, "elo_away": 1620,
    "odds": { "1": 1.91, "X": 3.50, "2": 4.20 }
}, "Cagliari away/Verona win (2) @4.20", "2")

sensitivity({
    "home_team": "Internacional FC Palmira", "away_team": "Real Cundinamarca",
    "xg_home_for": 1.3, "xg_home_against": 1.2, "xg_away_for": 1.2, "xg_away_against": 1.3,
    "elo_home": 1380, "elo_away": 1350,
    "odds": { "1": 1.88, "X": 3.40, "2": 4.80 }
}, "Cundinamarca away (2) @4.80", "2")

sensitivity({
    "home_team": "Toulouse FC", "away_team": "Lille OSC",
    "xg_home_for": 1.1, "xg_home_against": 1.5, "xg_away_for": 1.6, "xg_away_against": 1.0,
    "elo_home": 1600, "elo_away": 1720,
    "odds": { "1": 3.55, "X": 3.50, "2": 2.24 }
}, "Toulouse home (1) @3.55", "1")

sensitivity({
    "home_team": "Cagliari", "away_team": "Hellas Verona",
    "xg_home_for": 1.3, "xg_home_against": 1.3, "xg_away_for": 1.2, "xg_away_against": 1.4,
    "elo_home": 1640, "elo_away": 1620,
    "odds": { "btts_yes": 1.95 }
}, "Cagliari-Verona BTTS yes @1.95", "btts_yes")
