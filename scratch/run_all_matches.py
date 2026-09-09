import json
import os
import subprocess

matches = [
    # Champions League
    {
        "home_team": "FC Barcelona",
        "away_team": "Feyenoord",
        "league": "Champions League",
        "xg_home_for": 2.30, "xg_home_against": 0.90,
        "xg_away_for": 1.40, "xg_away_against": 1.30,
        "elo_home": 1920, "elo_away": 1720,
        "odds": {
            "1": 1.18, "X": 7.00, "2": 13.00,
            "over_1_5": 1.12, "over_2_5": 1.38, "under_2_5": 2.95, "over_3_5": 2.00,
            "btts_yes": 1.95, "btts_no": 1.80, "1x": 1.03, "dnb_home": 1.04
        }
    },
    {
        "home_team": "Liverpool FC",
        "away_team": "Atlético de Madrid",
        "league": "Champions League",
        "xg_home_for": 2.10, "xg_home_against": 1.00,
        "xg_away_for": 1.35, "xg_away_against": 1.15,
        "elo_home": 1910, "elo_away": 1840,
        "odds": {
            "1": 1.90, "X": 3.50, "2": 4.00,
            "over_1_5": 1.28, "over_2_5": 1.90, "under_2_5": 1.90, "over_3_5": 3.20,
            "btts_yes": 1.80, "btts_no": 1.95, "1x": 1.25, "x2": 1.85, "dnb_home": 1.38, "dnb_away": 2.80
        }
    },
    {
        "home_team": "Napoli",
        "away_team": "Arsenal",
        "league": "Champions League",
        "xg_home_for": 1.70, "xg_home_against": 1.05,
        "xg_away_for": 1.80, "xg_away_against": 0.95,
        "elo_home": 1830, "elo_away": 1900,
        "odds": {
            "1": 2.90, "X": 3.30, "2": 2.45,
            "over_1_5": 1.30, "over_2_5": 1.95, "under_2_5": 1.85, "over_3_5": 3.30,
            "btts_yes": 1.75, "btts_no": 2.00, "1x": 1.53, "x2": 1.40, "dnb_away": 1.75
        }
    },
    {
        "home_team": "Sporting CP",
        "away_team": "Galatasaray",
        "league": "Champions League",
        "xg_home_for": 2.00, "xg_home_against": 1.10,
        "xg_away_for": 1.50, "xg_away_against": 1.40,
        "elo_home": 1810, "elo_away": 1730,
        "odds": {
            "1": 1.70, "X": 3.90, "2": 4.60,
            "over_1_5": 1.22, "over_2_5": 1.65, "under_2_5": 2.20,
            "btts_yes": 1.68, "btts_no": 2.10, "1x": 1.20, "dnb_home": 1.28
        }
    },
    {
        "home_team": "Paris Saint-Germain",
        "away_team": "Slovan Bratislava",
        "league": "Champions League",
        "xg_home_for": 2.50, "xg_home_against": 0.85,
        "xg_away_for": 0.90, "xg_away_against": 2.10,
        "elo_home": 1930, "elo_away": 1560,
        "odds": {
            "1": 1.10, "X": 9.50, "2": 21.00,
            "over_2_5": 1.25, "under_2_5": 3.80, "over_3_5": 1.70,
            "btts_yes": 2.20, "btts_no": 1.60
        }
    },
    {
        "home_team": "VfB Stuttgart",
        "away_team": "Viking FK",
        "league": "Champions League",
        "xg_home_for": 1.90, "xg_home_against": 1.15,
        "xg_away_for": 1.10, "xg_away_against": 1.80,
        "elo_home": 1780, "elo_away": 1580,
        "odds": {
            "1": 1.35, "X": 5.20, "2": 8.00,
            "over_2_5": 1.50, "under_2_5": 2.50,
            "btts_yes": 1.75, "btts_no": 2.00, "1x": 1.08, "dnb_home": 1.11
        }
    },
    # MLS
    {
        "home_team": "LAFC",
        "away_team": "Red Bull New York",
        "league": "Major League Soccer",
        "xg_home_for": 1.85, "xg_home_against": 1.10,
        "xg_away_for": 1.20, "xg_away_against": 1.35,
        "elo_home": 1640, "elo_away": 1570,
        "odds": {
            "1": 1.85, "X": 3.60, "2": 4.10,
            "over_2_5": 1.75, "under_2_5": 2.05,
            "btts_yes": 1.70, "1x": 1.24, "dnb_home": 1.36
        }
    },
    {
        "home_team": "Philadelphia Union",
        "away_team": "FC Cincinnati",
        "league": "Major League Soccer",
        "xg_home_for": 1.60, "xg_home_against": 1.25,
        "xg_away_for": 1.65, "xg_away_against": 1.20,
        "elo_home": 1580, "elo_away": 1630,
        "odds": {
            "1": 2.40, "X": 3.40, "2": 2.85,
            "over_2_5": 1.72, "under_2_5": 2.10,
            "btts_yes": 1.60, "x2": 1.55, "dnb_away": 2.05
        }
    },
    {
        "home_team": "D.C. United",
        "away_team": "Columbus Crew",
        "league": "Major League Soccer",
        "xg_home_for": 1.40, "xg_home_against": 1.50,
        "xg_away_for": 1.80, "xg_away_against": 1.15,
        "elo_home": 1520, "elo_away": 1650,
        "odds": {
            "1": 3.30, "X": 3.60, "2": 2.05,
            "over_2_5": 1.65, "under_2_5": 2.20,
            "btts_yes": 1.58, "x2": 1.33, "dnb_away": 1.50
        }
    },
    {
        "home_team": "New York City FC",
        "away_team": "New England Revolution",
        "league": "Major League Soccer",
        "xg_home_for": 1.70, "xg_home_against": 1.20,
        "xg_away_for": 1.25, "xg_away_against": 1.60,
        "elo_home": 1590, "elo_away": 1510,
        "odds": {
            "1": 1.75, "X": 3.75, "2": 4.40,
            "over_2_5": 1.70, "under_2_5": 2.10,
            "btts_yes": 1.68, "1x": 1.20, "dnb_home": 1.30
        }
    },
    {
        "home_team": "CF Montréal",
        "away_team": "Charlotte FC",
        "league": "Major League Soccer",
        "xg_home_for": 1.35, "xg_home_against": 1.45,
        "xg_away_for": 1.40, "xg_away_against": 1.30,
        "elo_home": 1500, "elo_away": 1550,
        "odds": {
            "1": 2.50, "X": 3.30, "2": 2.80,
            "over_2_5": 1.85, "under_2_5": 1.95,
            "btts_yes": 1.68, "x2": 1.52, "dnb_away": 2.00
        }
    },
    {
        "home_team": "Minnesota United",
        "away_team": "FC Dallas",
        "league": "Major League Soccer",
        "xg_home_for": 1.65, "xg_home_against": 1.30,
        "xg_away_for": 1.25, "xg_away_against": 1.55,
        "elo_home": 1560, "elo_away": 1520,
        "odds": {
            "1": 1.95, "X": 3.50, "2": 3.70,
            "over_2_5": 1.75, "under_2_5": 2.05,
            "btts_yes": 1.65, "1x": 1.27, "dnb_home": 1.42
        }
    },
    # Copa Colombia
    {
        "home_team": "América de Cali",
        "away_team": "Deportivo Pereira",
        "league": "Copa Colombia",
        "xg_home_for": 1.55, "xg_home_against": 0.95,
        "xg_away_for": 1.05, "xg_away_against": 1.35,
        "elo_home": 1540, "elo_away": 1460,
        "odds": {
            "1": 1.80, "X": 3.30, "2": 4.60,
            "over_2_5": 2.15, "under_2_5": 1.68,
            "btts_yes": 2.00, "1x": 1.18, "dnb_home": 1.30
        }
    },
    {
        "home_team": "Once Caldas",
        "away_team": "Alianza FC",
        "league": "Copa Colombia",
        "xg_home_for": 1.45, "xg_home_against": 1.00,
        "xg_away_for": 0.95, "xg_away_against": 1.40,
        "elo_home": 1510, "elo_away": 1430,
        "odds": {
            "1": 1.85, "X": 3.25, "2": 4.40,
            "over_2_5": 2.20, "under_2_5": 1.65,
            "btts_yes": 2.05, "1x": 1.20, "dnb_home": 1.33
        }
    },
    {
        "home_team": "Deportivo Pasto",
        "away_team": "Independiente Medellín",
        "league": "Copa Colombia",
        "xg_home_for": 1.25, "xg_home_against": 1.10,
        "xg_away_for": 1.35, "xg_away_against": 1.15,
        "elo_home": 1450, "elo_away": 1530,
        "odds": {
            "1": 2.65, "X": 3.05, "2": 2.75,
            "over_2_5": 2.30, "under_2_5": 1.60,
            "btts_yes": 1.95, "x2": 1.45, "dnb_away": 1.90
        }
    },
    {
        "home_team": "Real Cundinamarca",
        "away_team": "Inter Bogotá",
        "league": "Copa Colombia",
        "xg_home_for": 1.20, "xg_home_against": 1.20,
        "xg_away_for": 1.10, "xg_away_against": 1.30,
        "elo_home": 1350, "elo_away": 1330,
        "odds": {
            "1": 2.20, "X": 3.10, "2": 3.40,
            "over_2_5": 2.10, "under_2_5": 1.70,
            "btts_yes": 1.90, "1x": 1.30, "dnb_home": 1.55
        }
    },
    # Copa Libertadores
    {
        "home_team": "Palmeiras",
        "away_team": "Liga de Quito",
        "league": "Copa Libertadores",
        "xg_home_for": 2.05, "xg_home_against": 0.85,
        "xg_away_for": 1.05, "xg_away_against": 1.60,
        "elo_home": 1820, "elo_away": 1640,
        "odds": {
            "1": 1.45, "X": 4.20, "2": 7.25,
            "over_2_5": 1.80, "under_2_5": 2.00,
            "btts_yes": 2.05, "1x": 1.10, "dnb_home": 1.15
        }
    },
    {
        "home_team": "Estudiantes de La Plata",
        "away_team": "Corinthians",
        "league": "Copa Libertadores",
        "xg_home_for": 1.45, "xg_home_against": 1.00,
        "xg_away_for": 1.25, "xg_away_against": 1.20,
        "elo_home": 1670, "elo_away": 1680,
        "odds": {
            "1": 2.25, "X": 3.10, "2": 3.40,
            "over_2_5": 2.25, "under_2_5": 1.62,
            "btts_yes": 1.95, "1x": 1.30, "dnb_home": 1.58
        }
    },
    # Copa Sudamericana
    {
        "home_team": "Santos FC",
        "away_team": "Atlético-MG",
        "league": "Copa Sudamericana",
        "xg_home_for": 1.40, "xg_home_against": 1.15,
        "xg_away_for": 1.45, "xg_away_against": 1.10,
        "elo_home": 1650, "elo_away": 1720,
        "odds": {
            "1": 2.70, "X": 3.10, "2": 2.65,
            "over_2_5": 2.15, "under_2_5": 1.68,
            "btts_yes": 1.88, "x2": 1.44, "dnb_away": 1.85
        }
    },
    # EFL Cup
    {
        "home_team": "Chelsea FC",
        "away_team": "Leeds United",
        "league": "EFL Cup Inglaterra",
        "xg_home_for": 2.00, "xg_home_against": 1.10,
        "xg_away_for": 1.30, "xg_away_against": 1.50,
        "elo_home": 1850, "elo_away": 1660,
        "odds": {
            "1": 1.55, "X": 4.20, "2": 5.50,
            "over_2_5": 1.60, "under_2_5": 2.30,
            "btts_yes": 1.70, "1x": 1.14, "dnb_home": 1.22
        }
    },
    # Eredivisie
    {
        "home_team": "FC Twente",
        "away_team": "SC Telstar",
        "league": "Eredivisie",
        "xg_home_for": 2.10, "xg_home_against": 1.05,
        "xg_away_for": 0.95, "xg_away_against": 2.00,
        "elo_home": 1700, "elo_away": 1450,
        "odds": {
            "1": 1.30, "X": 5.50, "2": 9.00,
            "over_2_5": 1.45, "under_2_5": 2.65,
            "btts_yes": 1.80, "1x": 1.06, "dnb_home": 1.08
        }
    },
    # Liga Portugal
    {
        "home_team": "Moreirense FC",
        "away_team": "SL Benfica",
        "league": "Liga Portugal",
        "xg_home_for": 1.15, "xg_home_against": 1.45,
        "xg_away_for": 2.10, "xg_away_against": 0.90,
        "elo_home": 1560, "elo_away": 1830,
        "odds": {
            "1": 6.50, "X": 4.30, "2": 1.48,
            "over_2_5": 1.70, "under_2_5": 2.10,
            "btts_yes": 1.85, "x2": 1.10, "dnb_away": 1.18
        }
    }
]

all_candidates = []
match_results = []

os.makedirs("scratch", exist_ok=True)

for idx, m in enumerate(matches):
    in_file = f"scratch/input_{idx}.json"
    out_file = f"scratch/output_{idx}.json"
    with open(in_file, "w", encoding="utf-8") as f:
        json.dump(m, f, indent=2)
    
    subprocess.run(["python3", "scripts/calc_engine.py", "--input", in_file, "--output", out_file], check=True)
    
    with open(out_file, "r", encoding="utf-8") as f:
        res = json.load(f)
    
    match_results.append({
        "match_info": m,
        "results": res
    })
    
    for market_key, ev_data in res.get("evaluations", {}).items():
        if ev_data.get("has_value"):
            all_candidates.append({
                "match": res["match"],
                "league": m["league"],
                "market": market_key,
                "selection": market_key,
                "odds": ev_data["odds"],
                "model_prob": ev_data["model_prob"],
                "fair_odds": ev_data["fair_odds"],
                "edge": ev_data["edge"],
                "ev_percent": ev_data["ev_percent"],
                "robust_ev_percent": ev_data["robust_ev_percent"],
                "stake_recommended_units": ev_data["stake_recommended_units"],
                "conservative_prob": ev_data["conservative_prob"],
                "implied_prob": ev_data["implied_prob"],
            })

print(f"Total candidates with value (EV >= min_edge): {len(all_candidates)}")
with open("scratch/all_candidates.json", "w", encoding="utf-8") as f:
    json.dump(all_candidates, f, indent=2, ensure_ascii=False)

with open("scratch/all_matches_out.json", "w", encoding="utf-8") as f:
    json.dump(match_results, f, indent=2, ensure_ascii=False)
