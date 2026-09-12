import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.calc_engine import run_ensemble, load_model_config
from scripts.selection import select_portfolio, classify_candidate

matches = [
    {
        "league": "LaLiga",
        "home_team": "Sevilla FC",
        "away_team": "Valencia CF",
        "elo_home": 1680,
        "elo_away": 1590,
        "xg_home_for": 1.55,
        "xg_home_against": 1.10,
        "xg_away_for": 1.05,
        "xg_away_against": 1.45,
        "odds": {
            "1": 2.12, "X": 3.35, "2": 3.60,
            "over_1_5": 1.34, "under_2_5": 1.78, "over_2_5": 2.08, "over_3_5": 3.75,
            "btts_yes": 1.95, "btts_no": 1.85, "1x": 1.30, "x2": 1.72,
            "dnb_home": 1.52, "dnb_away": 2.50
        }
    },
    {
        "league": "Ligue 1",
        "home_team": "Stade Rennais",
        "away_team": "Olympique de Marseille",
        "elo_home": 1660,
        "elo_away": 1675,
        "xg_home_for": 1.45,
        "xg_home_against": 1.25,
        "xg_away_for": 1.40,
        "xg_away_against": 1.30,
        "odds": {
            "1": 2.18, "X": 3.70, "2": 3.25,
            "over_1_5": 1.28, "under_2_5": 1.98, "over_2_5": 1.85, "over_3_5": 3.20,
            "btts_yes": 1.70, "btts_no": 2.15, "1x": 1.35, "x2": 1.68,
            "dnb_home": 1.57, "dnb_away": 2.35
        }
    },
    {
        "league": "Serie A",
        "home_team": "Venezia FC",
        "away_team": "ACF Fiorentina",
        "elo_home": 1490,
        "elo_away": 1655,
        "xg_home_for": 1.05,
        "xg_home_against": 1.55,
        "xg_away_for": 1.45,
        "xg_away_against": 1.15,
        "odds": {
            "1": 3.10, "X": 3.40, "2": 2.35,
            "over_1_5": 1.30, "under_2_5": 1.85, "over_2_5": 1.98, "over_3_5": 3.50,
            "btts_yes": 1.80, "btts_no": 2.00, "1x": 1.60, "x2": 1.38,
            "dnb_home": 2.20, "dnb_away": 1.67
        }
    },
    {
        "league": "Bundesliga",
        "home_team": "1. FC Union Berlin",
        "away_team": "FC Schalke 04",
        "elo_home": 1620,
        "elo_away": 1530,
        "xg_home_for": 1.40,
        "xg_home_against": 1.15,
        "xg_away_for": 1.10,
        "xg_away_against": 1.50,
        "odds": {
            "1": 2.15, "X": 3.60, "2": 3.25,
            "over_1_5": 1.32, "under_2_5": 1.82, "over_2_5": 2.00, "over_3_5": 3.60,
            "btts_yes": 1.85, "btts_no": 1.95, "1x": 1.33, "x2": 1.70,
            "dnb_home": 1.53, "dnb_away": 2.40
        }
    },
    {
        "league": "Eredivisie",
        "home_team": "AZ Alkmaar",
        "away_team": "Willem II",
        "elo_home": 1690,
        "elo_away": 1420,
        "xg_home_for": 2.25,
        "xg_home_against": 0.85,
        "xg_away_for": 0.80,
        "xg_away_against": 2.10,
        "odds": {
            "1": 1.12, "X": 8.50, "2": 17.00,
            "over_1_5": 1.12, "under_2_5": 3.10, "over_2_5": 1.36, "over_3_5": 1.95,
            "btts_yes": 2.10, "btts_no": 1.72, "1x": 1.02, "x2": 6.00,
            "dnb_home": 1.03, "dnb_away": 12.00
        }
    },
    {
        "league": "Liga BetPlay",
        "home_team": "Jaguares de Córdoba",
        "away_team": "Fortaleza FC",
        "elo_home": 1410,
        "elo_away": 1425,
        "xg_home_for": 1.15,
        "xg_home_against": 1.10,
        "xg_away_for": 1.00,
        "xg_away_against": 1.20,
        "odds": {
            "1": 2.35, "X": 3.10, "2": 3.35,
            "over_1_5": 1.45, "under_2_5": 1.55, "over_2_5": 2.45, "over_3_5": 4.80,
            "btts_yes": 2.05, "btts_no": 1.75, "1x": 1.34, "x2": 1.60,
            "dnb_home": 1.65, "dnb_away": 2.35
        }
    },
    {
        "league": "Liga BetPlay",
        "home_team": "Independiente Santa Fe",
        "away_team": "Deportes Tolima",
        "elo_home": 1525,
        "elo_away": 1535,
        "xg_home_for": 1.30,
        "xg_home_against": 1.00,
        "xg_away_for": 1.15,
        "xg_away_against": 1.05,
        "odds": {
            "1": 2.35, "X": 3.10, "2": 3.30,
            "over_1_5": 1.42, "under_2_5": 1.58, "over_2_5": 2.38, "over_3_5": 4.60,
            "btts_yes": 2.00, "btts_no": 1.80, "1x": 1.33, "x2": 1.60,
            "dnb_home": 1.63, "dnb_away": 2.30
        }
    },
    {
        "league": "Liga Argentina",
        "home_team": "Newell's Old Boys",
        "away_team": "Vélez Sarsfield",
        "elo_home": 1540,
        "elo_away": 1570,
        "xg_home_for": 1.10,
        "xg_home_against": 1.05,
        "xg_away_for": 1.15,
        "xg_away_against": 0.95,
        "odds": {
            "1": 3.00, "X": 2.95, "2": 2.65,
            "over_1_5": 1.48, "under_2_5": 1.50, "over_2_5": 2.60, "over_3_5": 5.00,
            "btts_yes": 2.10, "btts_no": 1.70, "1x": 1.48, "x2": 1.40,
            "dnb_home": 2.05, "dnb_away": 1.80
        }
    },
    {
        "league": "Liga Argentina",
        "home_team": "Defensa y Justicia",
        "away_team": "Gimnasia y Esgrima Mendoza",
        "elo_home": 1520,
        "elo_away": 1440,
        "xg_home_for": 1.40,
        "xg_home_against": 1.10,
        "xg_away_for": 1.00,
        "xg_away_against": 1.45,
        "odds": {
            "1": 2.12, "X": 3.15, "2": 3.75,
            "over_1_5": 1.38, "under_2_5": 1.68, "over_2_5": 2.20, "over_3_5": 4.10,
            "btts_yes": 1.95, "btts_no": 1.85, "1x": 1.28, "x2": 1.72,
            "dnb_home": 1.50, "dnb_away": 2.65
        }
    },
    {
        "league": "Liga Argentina",
        "home_team": "Boca Juniors",
        "away_team": "Central Córdoba",
        "elo_home": 1650,
        "elo_away": 1410,
        "xg_home_for": 1.70,
        "xg_home_against": 0.85,
        "xg_away_for": 0.75,
        "xg_away_against": 1.65,
        "odds": {
            "1": 1.38, "X": 4.40, "2": 8.50,
            "over_1_5": 1.25, "under_2_5": 1.90, "over_2_5": 1.90, "over_3_5": 3.30,
            "btts_yes": 2.15, "btts_no": 1.70, "1x": 1.08, "x2": 3.00,
            "dnb_home": 1.12, "dnb_away": 6.00
        }
    }
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

with open("scratch/results_11sep.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"Total partidos procesados: {len(all_results)}")
print(f"Total evaluaciones de mercado (todos los lados): {len(all_evaluations)}")
over_fn = lambda m: m.split("_")[0]
import collections
ou = collections.Counter(("over" if e["market"].startswith("over_2_5") else "under" if e["market"].startswith("under_2_5") else "other") for e in all_evaluations)
print(f"O/U 2.5 evaluados -> over: {ou['over']} | under: {ou['under']}")
print(f"Total candidatos con value (bruto): {len(all_candidates)}")
print(f"Picks seleccionados (prioritario/excepcional): {len(selected)}")
print(f"Picks excluidos: {len(excluded)}")

print("\n--- PICKS SELECCIONADOS ---")
for i, s in enumerate(selected, 1):
    print(f"{i}. {s['match']} | Mercado: {s['market']} | Cuota: {s['odds']} | Prob: {s['model_prob']*100:.1f}% | EV rob: {s['robust_ev_percent']}% | Stake: {s['stake_recommended_units']}u | Perfil: {s['selection_profile']}")

print("\n--- TODOS LOS CANDIDATOS ---")
for c in sorted(all_candidates, key=lambda x: (x["model_prob"], x["robust_ev_percent"]), reverse=True):
    profile, reason = classify_candidate(c)
    print(f"{c['match']} ({c['league']}) - {c['market']} | Odds: {c['odds']} | Prob: {c['model_prob']*100:.1f}% | EV: {c['ev_percent']}% | EV rob: {c['robust_ev_percent']}% | Stake: {c['stake_recommended_units']}u | Profile: {profile}")
