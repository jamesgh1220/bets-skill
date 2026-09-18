import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.calc_engine import run_ensemble, load_model_config
from scripts.selection import select_portfolio

matches = [
    {
        "league": "Europa League",
        "home_team": "Omonia Nicosia",
        "away_team": "Celta de Vigo",
        "elo_home": 1490,
        "elo_away": 1660,
        "xg_home_for": 1.40,
        "xg_home_against": 1.00,
        "xg_away_for": 1.00,
        "xg_away_against": 1.20,
        "odds": {
            "1": 4.50, "X": 3.55, "2": 1.86,
            "over_1_5": 1.33, "under_1_5": 3.40, "over_2_5": 2.00,
            "btts_yes": 1.85, "1x": 1.85, "x2": 1.22, "12": 1.30,
            "dnb_home": 2.30, "dnb_away": 1.50
        }
    },
    {
        "league": "Europa League",
        "home_team": "Sunderland",
        "away_team": "AZ Alkmaar",
        "elo_home": 1600,
        "elo_away": 1610,
        "xg_home_for": 1.30,
        "xg_home_against": 1.10,
        "xg_away_for": 1.70,
        "xg_away_against": 1.10,
        "odds": {
            "1": 1.67, "X": 3.90, "2": 4.33,
            "over_2_5": 1.93, "under_2_5": 1.93,
            "btts_yes": 1.70, "btts_no": 2.05
        }
    },
    {
        "league": "Europa League",
        "home_team": "FC Ararat-Armenia",
        "away_team": "Sparta Prague",
        "elo_home": 1440,
        "elo_away": 1620,
        "xg_home_for": 1.10,
        "xg_home_against": 1.30,
        "xg_away_for": 1.60,
        "xg_away_against": 1.00,
        "odds": {
            "1": 5.25, "X": 4.00, "2": 1.65,
            "over_2_5": 1.88, "under_2_5": 1.98,
            "btts_yes": 1.70, "btts_no": 2.05
        }
    },
    {
        "league": "Europa League",
        "home_team": "AC Milan",
        "away_team": "Benfica",
        "elo_home": 1715,
        "elo_away": 1740,
        "xg_home_for": 1.90,
        "xg_home_against": 1.20,
        "xg_away_for": 2.10,
        "xg_away_against": 0.90,
        "odds": {
            "1": 2.15, "X": 3.50, "2": 3.40,
            "over_2_5": 1.75, "under_2_5": 2.15,
            "btts_yes": 1.60, "btts_no": 2.35
        }
    },
    {
        "league": "Europa League",
        "home_team": "Sturm Graz",
        "away_team": "Stade Rennais",
        "elo_home": 1540,
        "elo_away": 1640,
        "xg_home_for": 1.30,
        "xg_home_against": 1.20,
        "xg_away_for": 1.60,
        "xg_away_against": 1.00,
        "odds": {
            "1": 3.70, "X": 3.80, "2": 1.91,
            "over_2_5": 1.62, "under_2_5": 2.30,
            "btts_yes": 1.57, "btts_no": 2.25
        }
    },
    {
        "league": "Europa League",
        "home_team": "Bayer Leverkusen",
        "away_team": "NK Celje",
        "elo_home": 1750,
        "elo_away": 1380,
        "xg_home_for": 2.00,
        "xg_home_against": 0.90,
        "xg_away_for": 0.90,
        "xg_away_against": 1.70,
        "odds": {
            "1": 1.08, "X": 12.00, "2": 26.00,
            "over_2_5": 1.30, "over_3_5": 1.70, "btts_yes": 1.80
        }
    },
    {
        "league": "Europa League",
        "home_team": "Anderlecht",
        "away_team": "Olympique Lyonnais",
        "elo_home": 1590,
        "elo_away": 1700,
        "xg_home_for": 1.50,
        "xg_home_against": 1.20,
        "xg_away_for": 1.60,
        "xg_away_against": 1.30,
        "odds": {
            "1": 3.10, "X": 3.50, "2": 2.25,
            "over_2_5": 1.62, "under_2_5": 2.30,
            "btts_yes": 1.56, "btts_no": 2.40, "1x": 1.62, "x2": 1.40
        }
    },
    {
        "league": "Europa League",
        "home_team": "Hapoel Be'er Sheva",
        "away_team": "Dinamo Zagreb",
        "elo_home": 1500,
        "elo_away": 1610,
        "xg_home_for": 1.40,
        "xg_home_against": 1.70,
        "xg_away_for": 2.00,
        "xg_away_against": 1.40,
        "odds": {
            "1": 3.60, "X": 3.70, "2": 1.95,
            "over_2_5": 1.66, "under_2_5": 2.20,
            "btts_yes": 1.57, "btts_no": 2.25, "1x": 1.80, "x2": 1.25
        }
    },
    {
        "league": "Europa League",
        "home_team": "Olympiacos",
        "away_team": "Jagiellonia Białystok",
        "elo_home": 1620,
        "elo_away": 1530,
        "xg_home_for": 1.80,
        "xg_home_against": 1.00,
        "xg_away_for": 1.20,
        "xg_away_against": 1.50,
        "odds": {
            "1": 1.36, "X": 4.60, "2": 8.50,
            "over_2_5": 1.90, "under_2_5": 2.20, "btts_yes": 1.95
        }
    },
    {
        "league": "LaLiga",
        "home_team": "Atlético de Madrid",
        "away_team": "Osasuna",
        "elo_home": 1790,
        "elo_away": 1560,
        "xg_home_for": 1.80,
        "xg_home_against": 1.10,
        "xg_away_for": 1.00,
        "xg_away_against": 1.40,
        "odds": {
            "1": 1.50, "X": 4.30, "2": 6.50,
            "over_1_5": 1.25, "under_1_5": 3.80,
            "over_2_5": 1.78, "under_2_5": 2.10,
            "over_3_5": 2.60, "under_3_5": 1.50,
            "btts_yes": 1.91, "btts_no": 1.91, "1x": 1.12, "x2": 2.65,
            "dnb_home": 1.12, "dnb_away": 6.50
        }
    },
    {
        "league": "LaLiga",
        "home_team": "Deportivo de La Coruña",
        "away_team": "Sevilla FC",
        "elo_home": 1490,
        "elo_away": 1610,
        "xg_home_for": 1.30,
        "xg_home_against": 1.35,
        "xg_away_for": 1.60,
        "xg_away_against": 1.40,
        "odds": {
            "1": 2.45, "X": 3.30, "2": 2.90,
            "over_1_5": 1.25, "under_1_5": 3.75,
            "over_2_5": 1.70, "under_2_5": 2.20,
            "over_3_5": 2.60, "under_3_5": 1.50,
            "btts_yes": 1.85, "btts_no": 1.95, "1x": 1.38, "x2": 1.60,
            "dnb_home": 1.62, "dnb_away": 2.20
        }
    },
    {
        "league": "LaLiga",
        "home_team": "Barcelona",
        "away_team": "Racing de Santander",
        "elo_home": 1870,
        "elo_away": 1420,
        "xg_home_for": 2.60,
        "xg_home_against": 0.90,
        "xg_away_for": 1.30,
        "xg_away_against": 1.70,
        "odds": {
            "1": 1.06, "X": 13.00, "2": 23.00,
            "over_1_5": 1.03, "under_1_5": 12.00,
            "over_2_5": 1.12, "under_2_5": 6.00,
            "over_3_5": 1.33, "under_3_5": 3.40,
            "btts_yes": 1.80, "btts_no": 1.95, "1x": 1.01, "x2": 10.00,
            "dnb_home": 1.01, "dnb_away": 23.00
        }
    },
    {
        "league": "LaLiga",
        "home_team": "Levante UD",
        "away_team": "Athletic Club",
        "elo_home": 1470,
        "elo_away": 1680,
        "xg_home_for": 1.20,
        "xg_home_against": 1.50,
        "xg_away_for": 1.40,
        "xg_away_against": 1.10,
        "odds": {
            "1": 3.15, "X": 3.40, "2": 2.25,
            "over_1_5": 1.22, "under_1_5": 4.00,
            "over_2_5": 1.83, "under_2_5": 2.00,
            "over_3_5": 2.75, "under_3_5": 1.44,
            "btts_yes": 1.70, "btts_no": 2.15, "1x": 1.68, "x2": 1.30,
            "dnb_home": 2.40, "dnb_away": 1.53
        }
    },
    {
        "league": "EFL Cup",
        "home_team": "Manchester United",
        "away_team": "Brighton & Hove Albion",
        "elo_home": 1740,
        "elo_away": 1730,
        "xg_home_for": 1.70,
        "xg_home_against": 1.30,
        "xg_away_for": 1.70,
        "xg_away_against": 1.20,
        "odds": {
            "1": 1.75, "X": 3.75, "2": 3.50,
            "over_1_5": 1.18, "under_1_5": 4.50,
            "over_2_5": 1.50, "under_2_5": 2.50,
            "over_3_5": 2.20, "under_3_5": 1.60,
            "btts_yes": 1.60, "btts_no": 2.30, "1x": 1.25, "x2": 1.83,
            "dnb_home": 1.30, "dnb_away": 3.50
        }
    },
    {
        "league": "EFL Cup",
        "home_team": "Coventry City",
        "away_team": "Aston Villa",
        "elo_home": 1520,
        "elo_away": 1720,
        "xg_home_for": 0.90,
        "xg_home_against": 1.60,
        "xg_away_for": 1.20,
        "xg_away_against": 1.20,
        "odds": {
            "1": 2.88, "X": 3.50, "2": 2.25,
            "over_1_5": 1.30, "under_1_5": 3.40,
            "over_2_5": 1.80, "under_2_5": 2.00,
            "over_3_5": 2.60, "under_3_5": 1.48,
            "btts_yes": 1.75, "btts_no": 2.05, "1x": 1.53, "x2": 1.29,
            "dnb_home": 1.95, "dnb_away": 1.80
        }
    },
    {
        "league": "EFL Cup",
        "home_team": "Fleetwood Town",
        "away_team": "Sheffield United",
        "elo_home": 1380,
        "elo_away": 1620,
        "xg_home_for": 0.80,
        "xg_home_against": 1.50,
        "xg_away_for": 1.60,
        "xg_away_against": 1.00,
        "odds": {
            "1": 5.00, "X": 4.00, "2": 1.60,
            "over_1_5": 1.28, "under_1_5": 3.50,
            "over_2_5": 1.91, "under_2_5": 1.85,
            "over_3_5": 3.10, "under_3_5": 1.33,
            "btts_yes": 1.91, "btts_no": 1.85, "1x": 2.30, "x2": 1.22,
            "dnb_home": 5.00, "dnb_away": 1.17
        }
    },
    {
        "league": "EFL Cup",
        "home_team": "Everton",
        "away_team": "Wolverhampton Wanderers",
        "elo_home": 1650,
        "elo_away": 1500,
        "xg_home_for": 1.40,
        "xg_home_against": 1.10,
        "xg_away_for": 1.10,
        "xg_away_against": 1.50,
        "odds": {
            "1": 1.65, "X": 4.20, "2": 3.39,
            "over_2_5": 1.70, "under_2_5": 2.05, "btts_yes": 1.83
        }
    },
    {
        "league": "Copa Libertadores",
        "home_team": "LDU Quito",
        "away_team": "Palmeiras",
        "elo_home": 1520,
        "elo_away": 1710,
        "xg_home_for": 1.10,
        "xg_home_against": 0.90,
        "xg_away_for": 1.30,
        "xg_away_against": 0.80,
        "odds": {
            "1": 2.55, "X": 2.95, "2": 2.50,
            "over_1_5": 1.50, "under_1_5": 2.48,
            "over_2_5": 2.45, "under_2_5": 1.51,
            "btts_yes": 2.05, "btts_no": 1.70
        }
    },
    {
        "league": "Copa Libertadores",
        "home_team": "Corinthians",
        "away_team": "Estudiantes de La Plata",
        "elo_home": 1650,
        "elo_away": 1590,
        "xg_home_for": 1.25,
        "xg_home_against": 0.85,
        "xg_away_for": 0.95,
        "xg_away_against": 1.15,
        "odds": {
            "1": 1.97, "X": 3.00, "2": 4.43,
            "over_1_5": 1.57, "under_1_5": 2.25,
            "over_2_5": 2.88, "under_2_5": 1.43,
            "btts_yes": 2.63, "btts_no": 1.44
        }
    },
    {
        "league": "Copa Sudamericana",
        "home_team": "Atlético Mineiro",
        "away_team": "Santos",
        "elo_home": 1620,
        "elo_away": 1615,
        "xg_home_for": 1.50,
        "xg_home_against": 1.00,
        "xg_away_for": 1.10,
        "xg_away_against": 1.40,
        "odds": {
            "1": 1.77, "X": 3.54, "2": 4.56,
            "over_1_5": 1.36, "under_1_5": 3.00,
            "over_2_5": 2.16, "under_2_5": 1.83,
            "over_3_5": 4.00, "under_3_5": 1.22,
            "btts_yes": 2.02
        }
    },
    {
        "league": "Liga BetPlay",
        "home_team": "Once Caldas",
        "away_team": "Deportes Tolima",
        "elo_home": 1550,
        "elo_away": 1560,
        "xg_home_for": 1.15,
        "xg_home_against": 0.95,
        "xg_away_for": 0.95,
        "xg_away_against": 1.10,
        "odds": {
            "1": 2.14, "X": 3.15, "2": 3.38,
            "over_2_5": 2.22, "under_2_5": 1.79
        }
    },
    {
        "league": "Liga BetPlay",
        "home_team": "Internacional de Bogotá",
        "away_team": "Atlético Nacional",
        "elo_home": 1400,
        "elo_away": 1640,
        "xg_home_for": 0.90,
        "xg_home_against": 1.40,
        "xg_away_for": 1.60,
        "xg_away_against": 0.90,
        "odds": {
            "1": 4.20, "X": 3.42, "2": 1.82,
            "over_2_5": 2.00, "under_2_5": 1.97
        }
    },
]

model_config = load_model_config("models/model-v1.2.json")

all_candidates = []
all_evaluations = []
all_results = []

for m in matches:
    res = run_ensemble(m, model_config)
    res["league"] = m["league"]
    all_results.append(res)
    for m_key, ev in res["evaluations"].items():
        full = dict(ev)
        full["match"] = res["match"]
        full["league"] = m["league"]
        full["home_team"] = m["home_team"]
        full["away_team"] = m["away_team"]
        all_evaluations.append(full)
        if ev["has_value"]:
            all_candidates.append(full)

selected, excluded = select_portfolio(all_candidates, max_picks=6)

output_data = {
    "all_results": all_results,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded
}

with open("scratch/results_16sep.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"Total partidos procesados: {len(all_results)}")
print(f"Total evaluaciones de mercado (todos los lados): {len(all_evaluations)}")
print(f"Total candidatos con value (bruto): {len(all_candidates)}")
print(f"Picks seleccionados (prioritario/excepcional): {len(selected)}")
print(f"Picks excluidos: {len(excluded)}")

print("\n--- PICKS SELECCIONADOS ---")
for i, s in enumerate(selected, 1):
    print(f"{i}. {s['match']} | Mercado: {s['market']} | Cuota: {s['odds']} | Prob: {s['model_prob']*100:.1f}% | EV: {s['ev_percent']}% | EV rob: {s['robust_ev_percent']}% | Stake: {s['stake_recommended_units']:.2f}u | Perfil: {s['selection_profile']}")

print("\n--- TODOS LOS CANDIDATOS ---")
for c in sorted(all_candidates, key=lambda x: (x["model_prob"], x["robust_ev_percent"]), reverse=True):
    print(f"{c['match']} ({c['league']}) - {c['market']} | Odds: {c['odds']} | Prob: {c['model_prob']*100:.1f}% | EV: {c['ev_percent']}% | EV rob: {c['robust_ev_percent']}% | Stake: {c['stake_recommended_units']}u | Profile: {c['selection_profile']}")