import json
import os
import sys
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.calc_engine import run_ensemble, load_model_config
from scripts.selection import select_portfolio
from scripts.render_artifact import render

BASE = Path(__file__).resolve().parent
SCRATCH = BASE

matches = [
    {
        "id": "bundesliga_stuttgart_glad",
        "league": "Bundesliga",
        "home_team": "VfB Stuttgart",
        "away_team": "Borussia Mönchengladbach",
        "kickoff": "2026-10-23T18:30:00Z",
        "elo_home": 1820,
        "elo_away": 1667,
        "xg_home_for": 2.15,
        "xg_home_against": 1.25,
        "xg_away_for": 1.15,
        "xg_away_against": 1.85,
        "corners_home_for": 6.8,
        "corners_home_against": 3.7,
        "corners_away_for": 4.1,
        "corners_away_against": 6.2,
        "cards_home_for": 1.8,
        "cards_home_against": 2.6,
        "cards_away_for": 2.5,
        "cards_away_against": 1.9,
        "odds": {
            "1": 1.53, "X": 4.75, "2": 5.80,
            "1x": 1.16, "x2": 2.60, "12": 1.20,
            "dnb_home": 1.20, "dnb_away": 4.50,
            "over_1_5": 1.15, "under_1_5": 5.50,
            "over_2_5": 1.50, "under_2_5": 2.60,
            "over_3_5": 2.25, "under_3_5": 1.65,
            "btts_yes": 1.62, "btts_no": 2.25,
            "over_corners_8_5": 1.45, "under_corners_8_5": 2.65,
            "over_corners_9_5": 1.75, "under_corners_9_5": 2.05,
            "over_corners_10_5": 2.20, "under_corners_10_5": 1.65,
            "over_cards_3_5": 1.55, "under_cards_3_5": 2.35,
            "over_cards_4_5": 2.05, "under_cards_4_5": 1.75
        }
    },
    {
        "id": "premier_ipswich_forest",
        "league": "Premier League",
        "home_team": "Ipswich Town",
        "away_team": "Nottingham Forest",
        "kickoff": "2026-10-23T19:00:00Z",
        "elo_home": 1701,
        "elo_away": 1799,
        "xg_home_for": 1.38,
        "xg_home_against": 1.75,
        "xg_away_for": 1.45,
        "xg_away_against": 1.32,
        "corners_home_for": 5.2,
        "corners_home_against": 5.8,
        "corners_away_for": 4.6,
        "corners_away_against": 4.9,
        "cards_home_for": 2.1,
        "cards_home_against": 2.3,
        "cards_away_for": 2.4,
        "cards_away_against": 2.0,
        "odds": {
            "1": 3.25, "X": 3.45, "2": 2.23,
            "1x": 1.68, "x2": 1.36, "12": 1.32,
            "dnb_home": 2.35, "dnb_away": 1.60,
            "over_1_5": 1.28, "under_1_5": 3.75,
            "over_2_5": 1.88, "under_2_5": 1.95,
            "over_3_5": 3.10, "under_3_5": 1.38,
            "btts_yes": 1.70, "btts_no": 2.10,
            "over_corners_8_5": 1.50, "under_corners_8_5": 2.50,
            "over_corners_9_5": 1.85, "under_corners_9_5": 1.95,
            "over_corners_10_5": 2.35, "under_corners_10_5": 1.60,
            "over_cards_3_5": 1.60, "under_cards_3_5": 2.25,
            "over_cards_4_5": 2.15, "under_cards_4_5": 1.68
        }
    },
    {
        "id": "laliga_alaves_malaga",
        "league": "LaLiga",
        "home_team": "Deportivo Alavés",
        "away_team": "Málaga",
        "kickoff": "2026-10-23T19:00:00Z",
        "elo_home": 1721,
        "elo_away": 1666,
        "xg_home_for": 1.48,
        "xg_home_against": 1.15,
        "xg_away_for": 0.95,
        "xg_away_against": 1.80,
        "corners_home_for": 4.2,
        "corners_home_against": 4.5,
        "corners_away_for": 3.8,
        "corners_away_against": 5.4,
        "cards_home_for": 2.6,
        "cards_home_against": 2.8,
        "cards_away_for": 3.1,
        "cards_away_against": 2.4,
        "odds": {
            "1": 1.78, "X": 3.60, "2": 4.60,
            "1x": 1.20, "x2": 2.05, "12": 1.28,
            "dnb_home": 1.30, "dnb_away": 3.40,
            "over_1_5": 1.35, "under_1_5": 3.25,
            "over_2_5": 2.05, "under_2_5": 1.78,
            "over_3_5": 3.60, "under_3_5": 1.30,
            "btts_yes": 1.95, "btts_no": 1.82,
            "over_corners_8_5": 1.65, "under_corners_8_5": 2.20,
            "over_corners_9_5": 2.05, "under_corners_9_5": 1.75,
            "over_corners_10_5": 2.65, "under_corners_10_5": 1.48,
            "over_cards_3_5": 1.42, "under_cards_3_5": 2.75,
            "over_cards_4_5": 1.82, "under_cards_4_5": 1.95,
            "over_cards_5_5": 2.50, "under_cards_5_5": 1.52
        }
    },
    {
        "id": "seriea_torino_monza",
        "league": "Serie A",
        "home_team": "Torino",
        "away_team": "Monza",
        "kickoff": "2026-10-23T18:45:00Z",
        "elo_home": 1686,
        "elo_away": 1638,
        "xg_home_for": 1.35,
        "xg_home_against": 1.30,
        "xg_away_for": 1.05,
        "xg_away_against": 1.85,
        "corners_home_for": 4.8,
        "corners_home_against": 4.3,
        "corners_away_for": 4.2,
        "corners_away_against": 5.3,
        "cards_home_for": 2.2,
        "cards_home_against": 2.3,
        "cards_away_for": 2.7,
        "cards_away_against": 2.1,
        "odds": {
            "1": 1.98, "X": 3.45, "2": 3.90,
            "1x": 1.26, "x2": 1.82, "12": 1.31,
            "dnb_home": 1.42, "dnb_away": 2.80,
            "over_1_5": 1.32, "under_1_5": 3.40,
            "over_2_5": 1.98, "under_2_5": 1.85,
            "over_3_5": 3.45, "under_3_5": 1.32,
            "btts_yes": 1.85, "btts_no": 1.95,
            "over_corners_8_5": 1.60, "under_corners_8_5": 2.30,
            "over_corners_9_5": 1.98, "under_corners_9_5": 1.82,
            "over_corners_10_5": 2.55, "under_corners_10_5": 1.52,
            "over_cards_3_5": 1.50, "under_cards_3_5": 2.50,
            "over_cards_4_5": 1.95, "under_cards_4_5": 1.82
        }
    },
    {
        "id": "ligue1_brest_nice",
        "league": "Ligue 1",
        "home_team": "Brest",
        "away_team": "Nice",
        "kickoff": "2026-10-23T18:45:00Z",
        "elo_home": 1684,
        "elo_away": 1674,
        "xg_home_for": 1.52,
        "xg_home_against": 1.38,
        "xg_away_for": 1.40,
        "xg_away_against": 1.35,
        "corners_home_for": 5.1,
        "corners_home_against": 4.6,
        "corners_away_for": 4.7,
        "corners_away_against": 4.5,
        "cards_home_for": 2.0,
        "cards_home_against": 2.2,
        "cards_away_for": 2.3,
        "cards_away_against": 2.1,
        "odds": {
            "1": 2.45, "X": 3.35, "2": 2.95,
            "1x": 1.40, "x2": 1.56, "12": 1.33,
            "dnb_home": 1.75, "dnb_away": 2.05,
            "over_1_5": 1.30, "under_1_5": 3.55,
            "over_2_5": 1.92, "under_2_5": 1.90,
            "over_3_5": 3.30, "under_3_5": 1.34,
            "btts_yes": 1.75, "btts_no": 2.05,
            "over_corners_8_5": 1.55, "under_corners_8_5": 2.40,
            "over_corners_9_5": 1.92, "under_corners_9_5": 1.88,
            "over_corners_10_5": 2.45, "under_corners_10_5": 1.55,
            "over_cards_3_5": 1.55, "under_cards_3_5": 2.40,
            "over_cards_4_5": 2.05, "under_cards_4_5": 1.75
        }
    },
    {
        "id": "eredivisie_gae_telstar",
        "league": "Eredivisie",
        "home_team": "Go Ahead Eagles",
        "away_team": "Telstar",
        "kickoff": "2026-10-23T18:00:00Z",
        "elo_home": 1551,
        "elo_away": 1445,
        "xg_home_for": 1.65,
        "xg_home_against": 1.35,
        "xg_away_for": 1.05,
        "xg_away_against": 1.95,
        "corners_home_for": 5.8,
        "corners_home_against": 4.5,
        "corners_away_for": 3.9,
        "corners_away_against": 5.9,
        "cards_home_for": 1.6,
        "cards_home_against": 2.3,
        "cards_away_for": 2.5,
        "cards_away_against": 1.8,
        "odds": {
            "1": 1.66, "X": 3.95, "2": 4.80,
            "1x": 1.18, "x2": 2.20, "12": 1.25,
            "dnb_home": 1.25, "dnb_away": 3.80,
            "over_1_5": 1.20, "under_1_5": 4.60,
            "over_2_5": 1.68, "under_2_5": 2.20,
            "over_3_5": 2.70, "under_3_5": 1.48,
            "btts_yes": 1.70, "btts_no": 2.10,
            "over_corners_8_5": 1.50, "under_corners_8_5": 2.55,
            "over_corners_9_5": 1.85, "under_corners_9_5": 1.95,
            "over_corners_10_5": 2.35, "under_corners_10_5": 1.60,
            "over_cards_3_5": 1.65, "under_cards_3_5": 2.20,
            "over_cards_4_5": 2.20, "under_cards_4_5": 1.65
        }
    },
    {
        "id": "portugal_vitoria_maritimo",
        "league": "Liga Portugal",
        "home_team": "Vitória Guimarães",
        "away_team": "Marítimo",
        "kickoff": "2026-10-23T19:45:00Z",
        "elo_home": 1568,
        "elo_away": 1493,
        "xg_home_for": 1.42,
        "xg_home_against": 0.95,
        "xg_away_for": 0.85,
        "xg_away_against": 1.60,
        "corners_home_for": 5.6,
        "corners_home_against": 3.8,
        "corners_away_for": 3.7,
        "corners_away_against": 5.4,
        "cards_home_for": 2.5,
        "cards_home_against": 2.9,
        "cards_away_for": 3.0,
        "cards_away_against": 2.5,
        "odds": {
            "1": 1.60, "X": 3.90, "2": 5.60,
            "1x": 1.15, "x2": 2.30, "12": 1.25,
            "dnb_home": 1.22, "dnb_away": 4.10,
            "over_1_5": 1.30, "under_1_5": 3.50,
            "over_2_5": 2.05, "under_2_5": 1.75,
            "over_3_5": 3.65, "under_3_5": 1.28,
            "btts_yes": 2.00, "btts_no": 1.78,
            "over_corners_8_5": 1.55, "under_corners_8_5": 2.40,
            "over_corners_9_5": 1.95, "under_corners_9_5": 1.85,
            "over_corners_10_5": 2.50, "under_corners_10_5": 1.52,
            "over_cards_3_5": 1.45, "under_cards_3_5": 2.65,
            "over_cards_4_5": 1.85, "under_cards_4_5": 1.92,
            "over_cards_5_5": 2.55, "under_cards_5_5": 1.50
        }
    },
    {
        "id": "argentina_gimnasia_sarmiento",
        "league": "Liga Profesional Argentina",
        "home_team": "Gimnasia La Plata",
        "away_team": "Sarmiento de Junín",
        "kickoff": "2026-10-23T21:00:00Z",
        "elo_home": 1687,
        "elo_away": 1624,
        "xg_home_for": 1.30,
        "xg_home_against": 0.88,
        "xg_away_for": 0.75,
        "xg_away_against": 1.45,
        "corners_home_for": 4.9,
        "corners_home_against": 3.9,
        "corners_away_for": 3.4,
        "corners_away_against": 5.2,
        "cards_home_for": 2.7,
        "cards_home_against": 2.8,
        "cards_away_for": 3.2,
        "cards_away_against": 2.6,
        "odds": {
            "1": 1.71, "X": 3.80, "2": 6.00,
            "1x": 1.15, "x2": 2.15, "12": 1.26,
            "dnb_home": 1.25, "dnb_away": 4.30,
            "over_1_5": 1.42, "under_1_5": 2.85,
            "over_2_5": 2.30, "under_2_5": 1.62,
            "over_3_5": 4.30, "under_3_5": 1.22,
            "btts_yes": 2.25, "btts_no": 1.62,
            "over_corners_8_5": 1.65, "under_corners_8_5": 2.20,
            "over_corners_9_5": 2.10, "under_corners_9_5": 1.72,
            "over_corners_10_5": 2.75, "under_corners_10_5": 1.45,
            "over_cards_3_5": 1.38, "under_cards_3_5": 2.95,
            "over_cards_4_5": 1.75, "under_cards_4_5": 2.05,
            "over_cards_5_5": 2.40, "under_cards_5_5": 1.55
        }
    },
    {
        "id": "argentina_mendoza_platense",
        "league": "Liga Profesional Argentina",
        "home_team": "Gimnasia de Mendoza",
        "away_team": "Platense",
        "kickoff": "2026-10-23T21:30:00Z",
        "elo_home": 1646,
        "elo_away": 1633,
        "xg_home_for": 1.18,
        "xg_home_against": 1.10,
        "xg_away_for": 0.95,
        "xg_away_against": 1.25,
        "corners_home_for": 4.5,
        "corners_home_against": 4.2,
        "corners_away_for": 3.8,
        "corners_away_against": 4.8,
        "cards_home_for": 2.8,
        "cards_home_against": 2.9,
        "cards_away_for": 2.9,
        "cards_away_against": 2.7,
        "odds": {
            "1": 2.20, "X": 3.15, "2": 3.50,
            "1x": 1.30, "x2": 1.65, "12": 1.35,
            "dnb_home": 1.55, "dnb_away": 2.45,
            "over_1_5": 1.48, "under_1_5": 2.60,
            "over_2_5": 2.45, "under_2_5": 1.55,
            "over_3_5": 4.80, "under_3_5": 1.18,
            "btts_yes": 2.05, "btts_no": 1.75,
            "over_corners_8_5": 1.68, "under_corners_8_5": 2.15,
            "over_corners_9_5": 2.15, "under_corners_9_5": 1.68,
            "over_corners_10_5": 2.85, "under_corners_10_5": 1.42,
            "over_cards_3_5": 1.36, "under_cards_3_5": 3.05,
            "over_cards_4_5": 1.70, "under_cards_4_5": 2.12,
            "over_cards_5_5": 2.35, "under_cards_5_5": 1.60
        }
    },
    {
        "id": "argentina_tigre_tucuman",
        "league": "Liga Profesional Argentina",
        "home_team": "Tigre",
        "away_team": "Atlético Tucumán",
        "kickoff": "2026-10-24T00:15:00Z",
        "elo_home": 1643,
        "elo_away": 1579,
        "xg_home_for": 1.35,
        "xg_home_against": 0.95,
        "xg_away_for": 0.85,
        "xg_away_against": 1.55,
        "corners_home_for": 4.7,
        "corners_home_against": 4.0,
        "corners_away_for": 3.6,
        "corners_away_against": 5.1,
        "cards_home_for": 2.6,
        "cards_home_against": 2.7,
        "cards_away_for": 3.1,
        "cards_away_against": 2.5,
        "odds": {
            "1": 1.72, "X": 3.60, "2": 6.10,
            "1x": 1.15, "x2": 2.15, "12": 1.28,
            "dnb_home": 1.25, "dnb_away": 4.40,
            "over_1_5": 1.40, "under_1_5": 2.90,
            "over_2_5": 2.25, "under_2_5": 1.65,
            "over_3_5": 4.20, "under_3_5": 1.23,
            "btts_yes": 2.20, "btts_no": 1.65,
            "over_corners_8_5": 1.62, "under_corners_8_5": 2.25,
            "over_corners_9_5": 2.05, "under_corners_9_5": 1.75,
            "over_corners_10_5": 2.70, "under_corners_10_5": 1.46,
            "over_cards_3_5": 1.40, "under_cards_3_5": 2.85,
            "over_cards_4_5": 1.78, "under_cards_4_5": 2.02,
            "over_cards_5_5": 2.45, "under_cards_5_5": 1.55
        }
    },
    {
        "id": "colombia_chico_bucaramanga",
        "league": "Liga BetPlay Dimayor",
        "home_team": "Boyacá Chicó",
        "away_team": "Atlético Bucaramanga",
        "kickoff": "2026-10-23T23:00:00Z",
        "elo_home": 1420,
        "elo_away": 1640,
        "xg_home_for": 0.90,
        "xg_home_against": 1.55,
        "xg_away_for": 1.35,
        "xg_away_against": 0.95,
        "corners_home_for": 4.1,
        "corners_home_against": 5.2,
        "corners_away_for": 4.8,
        "corners_away_against": 3.9,
        "cards_home_for": 3.0,
        "cards_home_against": 2.5,
        "cards_away_for": 2.6,
        "cards_away_against": 2.9,
        "odds": {
            "1": 3.60, "X": 3.30, "2": 2.02,
            "1x": 1.75, "x2": 1.28, "12": 1.32,
            "dnb_home": 2.55, "dnb_away": 1.50,
            "over_1_5": 1.45, "under_1_5": 2.70,
            "over_2_5": 2.35, "under_2_5": 1.60,
            "over_3_5": 4.50, "under_3_5": 1.20,
            "btts_yes": 2.05, "btts_no": 1.75,
            "over_corners_8_5": 1.65, "under_corners_8_5": 2.20,
            "over_corners_9_5": 2.10, "under_corners_9_5": 1.72,
            "over_corners_10_5": 2.80, "under_corners_10_5": 1.44,
            "over_cards_3_5": 1.38, "under_cards_3_5": 2.95,
            "over_cards_4_5": 1.75, "under_cards_4_5": 2.05,
            "over_cards_5_5": 2.40, "under_cards_5_5": 1.55
        }
    },
    {
        "id": "colombia_junior_aguilas",
        "league": "Liga BetPlay Dimayor",
        "home_team": "Junior",
        "away_team": "Águilas Doradas",
        "kickoff": "2026-10-24T01:10:00Z",
        "elo_home": 1617,
        "elo_away": 1540,
        "xg_home_for": 1.45,
        "xg_home_against": 0.95,
        "xg_away_for": 0.92,
        "xg_away_against": 1.38,
        "corners_home_for": 5.4,
        "corners_home_against": 3.8,
        "corners_away_for": 3.9,
        "corners_away_against": 5.1,
        "cards_home_for": 2.5,
        "cards_home_against": 2.8,
        "cards_away_for": 3.1,
        "cards_away_against": 2.4,
        "odds": {
            "1": 1.80, "X": 3.50, "2": 4.10,
            "1x": 1.22, "x2": 1.95, "12": 1.29,
            "dnb_home": 1.32, "dnb_away": 3.15,
            "over_1_5": 1.38, "under_1_5": 3.05,
            "over_2_5": 2.15, "under_2_5": 1.70,
            "over_3_5": 3.90, "under_3_5": 1.26,
            "btts_yes": 2.02, "btts_no": 1.78,
            "over_corners_8_5": 1.58, "under_corners_8_5": 2.35,
            "over_corners_9_5": 1.98, "under_corners_9_5": 1.82,
            "over_corners_10_5": 2.60, "under_corners_10_5": 1.50,
            "over_cards_3_5": 1.40, "under_cards_3_5": 2.85,
            "over_cards_4_5": 1.80, "under_cards_4_5": 2.00,
            "over_cards_5_5": 2.48, "under_cards_5_5": 1.52
        }
    }
]

config_path = Path("models/model-v1.4.json")
config = load_model_config(str(config_path))

all_results = []
all_candidates = []
all_evaluations = []

for m in matches:
    res = run_ensemble(m, config)
    res['league'] = m['league']
    all_results.append(res)
    for m_key, evl in res['evaluations'].items():
        full = dict(evl)
        full['match'] = res['match']
        full['league'] = m['league']
        full['home_team'] = m['home_team']
        full['away_team'] = m['away_team']
        all_evaluations.append(full)
        if evl.get('has_value'):
            all_candidates.append(full)

print(f"Total value candidates: {len(all_candidates)}")

selected, excluded = select_portfolio(all_candidates, max_picks=6)

print(f"Selected: {len(selected)}")
print(f"Excluded: {len(excluded)}")

results_payload = {
    "all_results": all_results,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded
}

results_file = SCRATCH / "oct23_results.json"
with open(results_file, "w") as f:
    json.dump(results_payload, f, indent=2)

meta_payload = {
    "analysis_date_iso": "2026-10-23T09:00:00Z",
    "match_dates_text": "23 de octubre de 2026",
    "information_cutoff": "2026-10-23T08:55:00Z",
    "model_ia": "gemini3.8flash",
    "engine_version": "model-v1.4",
    "leagues_display": "Bundesliga, Liga Profesional Argentina, Liga BetPlay Dimayor, LaLiga, Ligue 1, Premier League, Serie A, Eredivisie, Liga Portugal",
    "requested_range": "2026-10-23 (todos los partidos de las 9 ligas solicitadas)",
    "universe_preamble": "Universo = 12 partidos programados para el viernes 23 de octubre de 2026 en las 9 ligas solicitadas (Bundesliga: 1, Premier League: 1, LaLiga: 1, Serie A: 1, Ligue 1: 1, Eredivisie: 1, Liga Portugal: 1, Liga Profesional Argentina: 3, Liga BetPlay Dimayor: 2). Recolección de cuotas Capa 1 y Capa 2 (1X2, totales de goles O/U 1.5, 2.5, 3.5, BTTS, DNB, córners y tarjetas). Se garantizaron los 8 campos obligatorios de córners y tarjetas (tasas for/against para ambos equipos basadas en los últimos 5-10 partidos). Evaluación cuantitativa determinista con scripts/calc_engine.py y calibración Platt de model-v1.4.",
    "universe_matches": [
        "- **Bundesliga (1 partido):** VfB Stuttgart vs. Borussia Mönchengladbach (MHP Arena, Stuttgart)",
        "- **Premier League (1 partido):** Ipswich Town vs. Nottingham Forest (Portman Road, Ipswich)",
        "- **LaLiga (1 partido):** Deportivo Alavés vs. Málaga (Estadio de Mendizorroza, Vitoria-Gasteiz)",
        "- **Serie A (1 partido):** Torino vs. Monza (Stadio Olimpico Grande Torino, Turín)",
        "- **Ligue 1 (1 partido):** Brest vs. Nice (Stade Francis-Le Blé, Brest)",
        "- **Eredivisie (1 partido):** Go Ahead Eagles vs. Telstar (De Adelaarshorst, Deventer)",
        "- **Liga Portugal (1 partido):** Vitória Guimarães vs. Marítimo (Estádio D. Afonso Henriques, Guimarães)",
        "- **Liga Argentina (3 partidos):** Gimnasia La Plata vs. Sarmiento de Junín, Gimnasia de Mendoza vs. Platense, Tigre vs. Atlético Tucumán",
        "- **Liga Colombiana (2 partidos):** Boyacá Chicó vs. Atlético Bucaramanga (La Independencia, Tunja), Junior vs. Águilas Doradas (Estadio Romelio Martínez / Metropolitano, Barranquilla)"
    ]
}

meta_file = SCRATCH / "oct23_meta.json"
with open(meta_file, "w") as f:
    json.dump(meta_payload, f, indent=2)

artifact_content = render(results_payload, meta_payload)
temp_artifact = SCRATCH / "temp_artifact_20261023.md"
with open(temp_artifact, "w", encoding="utf-8") as f:
    f.write(artifact_content)

print(f"Artifact successfully written to {temp_artifact}")
