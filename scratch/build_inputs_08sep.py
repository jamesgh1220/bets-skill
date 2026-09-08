"""Genera los match_input JSON del universo 2026-09-08 para calc_engine.py.

Fuentes de cuotas (agregadores/respaldo cuando las casas colombianas no son
extraíbles directamente): OddsSafari, ESPN Odds, 20Bet, BetMGM, 1xBet, Betsson,
Betway, Stake, FanDuel, DraftKings. xG/Elo estimados desde consenso de modelos
externos (Sports Mole, Extratips, that'sagoal, DRatings) y forma verificada.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs_08sep")
os.makedirs(OUT, exist_ok=True)

MATCHES = [
    {
        "home_team": "Real Madrid",
        "away_team": "Inter Milan",
        "xg_home_for": 2.30, "xg_home_against": 1.05,
        "xg_away_for": 1.80, "xg_away_against": 1.15,
        "elo_home": 2080, "elo_away": 1950,
        "odds": {"1": 1.65, "X": 4.40, "2": 4.85, "btts_yes": 1.53, "1x": 1.28},
    },
    {
        "home_team": "FC Porto",
        "away_team": "Manchester City",
        "xg_home_for": 1.50, "xg_home_against": 1.25,
        "xg_away_for": 2.05, "xg_away_against": 0.95,
        "elo_home": 1750, "elo_away": 2010,
        "odds": {"1": 4.40, "X": 4.09, "2": 1.74, "over_2_5": 1.64, "under_2_5": 2.20},
    },
    {
        "home_team": "Borussia Dortmund",
        "away_team": "Villarreal",
        "xg_home_for": 2.05, "xg_home_against": 1.20,
        "xg_away_for": 1.45, "xg_away_against": 1.25,
        "elo_home": 1870, "elo_away": 1690,
        "odds": {"1": 1.75, "X": 4.00, "2": 4.20, "over_2_5": 1.62, "under_2_5": 2.25},
    },
    {
        "home_team": "Lille",
        "away_team": "Real Betis",
        "xg_home_for": 1.75, "xg_home_against": 1.15,
        "xg_away_for": 1.50, "xg_away_against": 1.20,
        "elo_home": 1680, "elo_away": 1670,
        "odds": {"1": 2.35, "X": 3.60, "2": 3.16, "over_2_5": 1.83, "under_2_5": 2.00, "btts_yes": 1.70},
    },
    {
        "home_team": "Club Brugge",
        "away_team": "Aston Villa",
        "xg_home_for": 1.80, "xg_home_against": 1.25,
        "xg_away_for": 1.30, "xg_away_against": 1.20,
        "elo_home": 1620, "elo_away": 1760,
        "odds": {"1": 2.60, "X": 3.65, "2": 2.45, "over_2_5": 1.63},
    },
    {
        "home_team": "AEK Athens",
        "away_team": "LASK Linz",
        "xg_home_for": 1.90, "xg_home_against": 0.85,
        "xg_away_for": 1.55, "xg_away_against": 1.30,
        "elo_home": 1680, "elo_away": 1560,
        "odds": {"1": 1.75, "X": 4.10, "2": 4.40, "over_2_5": 1.63, "under_2_5": 2.32, "btts_yes": 1.67},
    },
    {
        "home_team": "Millwall",
        "away_team": "Newcastle United",
        "xg_home_for": 1.35, "xg_home_against": 1.30,
        "xg_away_for": 1.90, "xg_away_against": 1.10,
        "elo_home": 1500, "elo_away": 1860,
        "odds": {"1": 5.50, "X": 4.20, "2": 1.62, "over_2_5": 1.64, "under_2_5": 2.20},
    },
    {
        "home_team": "Bournemouth",
        "away_team": "Lincoln City",
        "xg_home_for": 1.85, "xg_home_against": 1.30,
        "xg_away_for": 1.15, "xg_away_against": 1.45,
        "elo_home": 1720, "elo_away": 1490,
        "odds": {"1": 1.30, "X": 5.40, "2": 8.20, "over_3_5": 2.10, "btts_yes": 1.75},
    },
    {
        "home_team": "Crystal Palace",
        "away_team": "Middlesbrough",
        "xg_home_for": 1.60, "xg_home_against": 1.45,
        "xg_away_for": 1.65, "xg_away_against": 1.10,
        "elo_home": 1680, "elo_away": 1560,
        "odds": {"1": 1.76, "X": 4.05, "2": 4.40},
    },
    {
        "home_team": "Leyton Orient",
        "away_team": "Bradford City",
        "xg_home_for": 1.35, "xg_home_against": 1.25,
        "xg_away_for": 1.20, "xg_away_against": 1.05,
        "elo_home": 1490, "elo_away": 1510,
        "odds": {"1": 3.05, "X": 3.35, "2": 2.20, "over_2_5": 2.00, "under_2_5": 1.80, "btts_yes": 1.80},
    },
    {
        "home_team": "Sunderland",
        "away_team": "Hull City",
        "xg_home_for": 1.30, "xg_home_against": 1.10,
        "xg_away_for": 1.05, "xg_away_against": 0.75,
        "elo_home": 1650, "elo_away": 1640,
        "odds": {"1": 1.70, "X": 3.70, "2": 4.70, "over_2_5": 1.95, "under_2_5": 1.85, "btts_yes": 1.95, "btts_no": 1.85},
    },
    {
        "home_team": "NEC Nijmegen",
        "away_team": "Excelsior",
        "xg_home_for": 1.42, "xg_home_against": 1.45,
        "xg_away_for": 1.70, "xg_away_against": 1.30,
        "elo_home": 1580, "elo_away": 1520,
        "odds": {"1": 1.47, "X": 4.33, "2": 5.60, "over_2_5": 1.35, "under_2_5": 3.20, "btts_yes": 1.44},
    },
    {
        "home_team": "Fluminense",
        "away_team": "Platense",
        "xg_home_for": 1.95, "xg_home_against": 0.95,
        "xg_away_for": 1.05, "xg_away_against": 1.20,
        "elo_home": 1820, "elo_away": 1590,
        "odds": {"1": 1.43, "X": 3.85, "2": 10.00},
    },
    {
        "home_team": "Independiente Santa Fe",
        "away_team": "Vasco da Gama",
        "xg_home_for": 1.25, "xg_home_against": 1.35,
        "xg_away_for": 1.50, "xg_away_against": 1.70,
        "elo_home": 1660, "elo_away": 1650,
        "odds": {"1": 2.28, "X": 3.35, "2": 3.25},
    },
    {
        "home_team": "Boca Juniors",
        "away_team": "Sao Paulo",
        "xg_home_for": 1.40, "xg_home_against": 0.85,
        "xg_away_for": 1.50, "xg_away_against": 1.05,
        "elo_home": 1750, "elo_away": 1720,
        "odds": {"1": 1.99, "X": 3.30, "2": 4.10},
    },
]

for idx, m in enumerate(MATCHES, start=1):
    slug = f"{m['home_team']}_vs_{m['away_team']}".replace(" ", "_").replace(",", "")
    path = os.path.join(OUT, f"match_{idx:02d}_{slug}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(m, fh, ensure_ascii=False, indent=2)
    print(path)