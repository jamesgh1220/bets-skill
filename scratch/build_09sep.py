"""Genera inputs y ejecuta calc_engine para el universo 2026-09-09 (model-v1.2).

Cuotas de referencia (cutoff 2026-09-08): TDP/1xBet/Betano/Unibet/bet365/Pinnacle
(Champions League), ESPN/DraftKings (EFL Cup), transfermarkt/flashscore (Eredivisie),
bet365/topfootytips (Liga Portugal), Betnacional/KTO/Betano (CONMEBOL),
OddsJet/sportsgambler/sportsline/Wincomparator (MLS), telefootball/betiball (Copa
Colombia). xG season per-90 y Elo aproximado desde forma/tabla.
"""
import json
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
OUT = os.path.join(BASE, "inputs_09sep")
RES = os.path.join(BASE, "outputs_09sep")
os.makedirs(OUT, exist_ok=True)
os.makedirs(RES, exist_ok=True)

MATCHES = [
    # ---------------- Champions League MD1 ----------------
    {
        "home_team": "Barcelona", "away_team": "Feyenoord",
        "xg_home_for": 2.30, "xg_home_against": 0.70,
        "xg_away_for": 1.25, "xg_away_against": 1.60,
        "elo_home": 1980, "elo_away": 1730,
        "odds": {"1": 1.11, "X": 13.78, "2": 27.00, "over_2_5": 1.19, "under_2_5": 5.50,
                 "btts_yes": 1.85, "12": 1.04, "x2": 8.30},
    },
    {
        "home_team": "VfB Stuttgart", "away_team": "Viking FK",
        "xg_home_for": 1.80, "xg_home_against": 1.80,
        "xg_away_for": 1.20, "xg_away_against": 1.50,
        "elo_home": 1720, "elo_away": 1500,
        "odds": {"1": 1.26, "X": 7.50, "2": 12.00, "over_2_5": 1.28, "under_2_5": 4.00,
                 "btts_yes": 1.61, "btts_no": 2.38, "1x": 1.05, "12": 1.12, "x2": 4.25},
    },
    {
        "home_team": "Liverpool", "away_team": "Atletico Madrid",
        "xg_home_for": 1.90, "xg_home_against": 1.05,
        "xg_away_for": 1.45, "xg_away_against": 1.35,
        "elo_home": 1905, "elo_away": 1876,
        "odds": {"1": 1.75, "X": 4.17, "2": 4.90, "over_2_5": 1.62, "under_2_5": 2.47,
                 "btts_yes": 1.62, "btts_no": 2.38, "1x": 1.22, "12": 1.26, "x2": 2.19},
    },
    {
        "home_team": "Napoli", "away_team": "Arsenal",
        "xg_home_for": 1.30, "xg_home_against": 1.40,
        "xg_away_for": 1.70, "xg_away_against": 0.80,
        "elo_home": 1760, "elo_away": 2020,
        "odds": {"1": 5.40, "X": 3.90, "2": 1.73, "over_2_5": 1.99, "under_2_5": 1.94,
                 "btts_yes": 1.91, "btts_no": 1.95, "1x": 2.22, "12": 1.29, "x2": 1.18},
    },
    {
        "home_team": "Paris Saint-Germain", "away_team": "Slovan Bratislava",
        "xg_home_for": 2.10, "xg_home_against": 1.30,
        "xg_away_for": 1.20, "xg_away_against": 1.90,
        "elo_home": 1950, "elo_away": 1450,
        "odds": {"1": 1.07, "X": 21.00, "2": 51.00, "over_2_5": 1.20, "under_2_5": 5.00,
                 "btts_yes": 2.70, "btts_no": 1.44},
    },
    {
        "home_team": "Sporting CP", "away_team": "Galatasaray",
        "xg_home_for": 2.10, "xg_home_against": 1.00,
        "xg_away_for": 1.80, "xg_away_against": 1.60,
        "elo_home": 1850, "elo_away": 1720,
        "odds": {"1": 1.87, "X": 4.00, "2": 4.30, "over_2_5": 1.66, "under_2_5": 2.38,
                 "btts_yes": 1.62, "btts_no": 2.38, "1x": 1.25, "12": 1.28, "x2": 2.06},
    },
    # ---------------- Copa Colombia (Octavos, partido único) ----------------
    {
        "home_team": "Once Caldas", "away_team": "Alianza Valledupar",
        "xg_home_for": 1.35, "xg_home_against": 1.10,
        "xg_away_for": 0.95, "xg_away_against": 1.30,
        "elo_home": 1650, "elo_away": 1580,
        "odds": {"1": 1.39, "X": 4.33, "2": 7.50},
    },
    {
        "home_team": "Deportivo Pasto", "away_team": "Independiente Medellin",
        "xg_home_for": 1.10, "xg_home_against": 1.30,
        "xg_away_for": 1.45, "xg_away_against": 1.20,
        "elo_home": 1560, "elo_away": 1680,
        "odds": {"1": 3.30, "X": 3.10, "2": 2.20},
    },
    # ---------------- EFL Cup (R3) ----------------
    {
        "home_team": "Chelsea", "away_team": "Leeds United",
        "xg_home_for": 2.00, "xg_home_against": 1.60,
        "xg_away_for": 1.50, "xg_away_against": 1.10,
        "elo_home": 1800, "elo_away": 1720,
        "odds": {"1": 1.65, "X": 3.95, "2": 4.70, "over_2_5": 1.67, "under_2_5": 2.20,
                 "btts_yes": 1.65},
    },
    # ---------------- Eredivisie (R3) ----------------
    {
        "home_team": "FC Twente", "away_team": "SC Telstar",
        "xg_home_for": 1.85, "xg_home_against": 1.00,
        "xg_away_for": 0.90, "xg_away_against": 1.75,
        "elo_home": 1750, "elo_away": 1480,
        "odds": {"1": 1.26, "X": 7.25, "2": 11.00, "over_2_5": 1.33, "under_2_5": 3.75,
                 "btts_yes": 1.66},
    },
    # ---------------- Liga Portugal ----------------
    {
        "home_team": "Moreirense", "away_team": "Benfica",
        "xg_home_for": 0.85, "xg_home_against": 1.55,
        "xg_away_for": 2.20, "xg_away_against": 0.70,
        "elo_home": 1520, "elo_away": 1900,
        "odds": {"1": 10.50, "X": 5.60, "2": 1.20, "over_2_5": 2.15, "under_2_5": 1.64,
                 "btts_yes": 2.25},
    },
    # ---------------- Copa Libertadores (QF ida) ----------------
    {
        "home_team": "Palmeiras", "away_team": "Liga de Quito",
        "xg_home_for": 1.60, "xg_home_against": 0.80,
        "xg_away_for": 1.10, "xg_away_against": 1.15,
        "elo_home": 1880, "elo_away": 1730,
        "odds": {"1": 1.25, "X": 5.50, "2": 14.00, "over_2_5": 1.87, "under_2_5": 1.87,
                 "btts_yes": 2.60, "btts_no": 1.43},
    },
    {
        "home_team": "Estudiantes de La Plata", "away_team": "Corinthians",
        "xg_home_for": 1.10, "xg_home_against": 0.80,
        "xg_away_for": 0.95, "xg_away_against": 1.35,
        "elo_home": 1770, "elo_away": 1780,
        "odds": {"1": 2.30, "X": 3.00, "2": 3.40, "over_2_5": 2.80, "under_2_5": 1.40,
                 "btts_yes": 2.17, "btts_no": 1.60},
    },
    # ---------------- Copa Sudamericana (QF ida) ----------------
    {
        "home_team": "Santos", "away_team": "Atletico Mineiro",
        "xg_home_for": 1.35, "xg_home_against": 1.10,
        "xg_away_for": 0.85, "xg_away_against": 0.95,
        "elo_home": 1800, "elo_away": 1820,
        "odds": {"1": 2.10, "X": 3.10, "2": 3.25, "over_2_5": 2.38, "under_2_5": 1.57,
                 "btts_yes": 1.91, "btts_no": 1.72},
    },
    # ---------------- MLS ----------------
    {
        "home_team": "Toronto FC", "away_team": "Nashville SC",
        "xg_home_for": 1.33, "xg_home_against": 1.48,
        "xg_away_for": 1.36, "xg_away_against": 1.22,
        "elo_home": 1490, "elo_away": 1680,
        "odds": {"1": 2.90, "X": 3.60, "2": 2.30, "over_2_5": 1.67, "under_2_5": 2.16,
                 "btts_yes": 1.54},
    },
    {
        "home_team": "CF Montreal", "away_team": "Charlotte FC",
        "xg_home_for": 1.54, "xg_home_against": 1.37,
        "xg_away_for": 1.40, "xg_away_against": 1.64,
        "elo_home": 1470, "elo_away": 1540,
        "odds": {"1": 2.30, "X": 3.90, "2": 2.80, "over_2_5": 1.55, "under_2_5": 2.40,
                 "btts_yes": 1.47},
    },
    {
        "home_team": "D.C. United", "away_team": "Columbus Crew",
        "xg_home_for": 1.39, "xg_home_against": 1.61,
        "xg_away_for": 1.43, "xg_away_against": 1.24,
        "elo_home": 1480, "elo_away": 1450,
        "odds": {"1": 2.55, "X": 3.50, "2": 2.60, "over_2_5": 1.66, "under_2_5": 2.17,
                 "btts_yes": 1.53},
    },
    {
        "home_team": "Atlanta United", "away_team": "Orlando City",
        "xg_home_for": 1.36, "xg_home_against": 1.44,
        "xg_away_for": 1.41, "xg_away_against": 1.87,
        "elo_home": 1460, "elo_away": 1490,
        "odds": {"1": 2.15, "X": 3.90, "2": 3.00},
    },
    {
        "home_team": "Philadelphia Union", "away_team": "FC Cincinnati",
        "xg_home_for": 1.78, "xg_home_against": 1.11,
        "xg_away_for": 1.59, "xg_away_against": 1.78,
        "elo_home": 1500, "elo_away": 1530,
        "odds": {"1": 1.69, "X": 4.33, "2": 4.20, "over_2_5": 1.36, "under_2_5": 3.05,
                 "btts_yes": 1.40},
    },
    {
        "home_team": "New York City FC", "away_team": "New England Revolution",
        "xg_home_for": 1.39, "xg_home_against": 1.43,
        "xg_away_for": 1.41, "xg_away_against": 1.56,
        "elo_home": 1520, "elo_away": 1560,
        "odds": {"1": 2.25, "X": 3.60, "2": 3.00, "over_2_5": 1.85, "under_2_5": 1.86,
                 "btts_yes": 1.57},
    },
    {
        "home_team": "Minnesota United", "away_team": "FC Dallas",
        "xg_home_for": 1.50, "xg_home_against": 1.43,
        "xg_away_for": 1.34, "xg_away_against": 1.46,
        "elo_home": 1540, "elo_away": 1570,
        "odds": {"1": 2.10, "X": 3.75, "2": 3.20, "over_2_5": 1.54, "under_2_5": 2.43,
                 "btts_yes": 1.49},
    },
    {
        "home_team": "Houston Dynamo", "away_team": "Real Salt Lake",
        "xg_home_for": 1.46, "xg_home_against": 1.44,
        "xg_away_for": 1.61, "xg_away_against": 1.47,
        "elo_home": 1630, "elo_away": 1530,
        "odds": {"1": 1.74, "X": 4.09, "2": 4.20, "over_2_5": 1.60, "under_2_5": 2.30,
                 "btts_yes": 1.56},
    },
    {
        "home_team": "Chicago Fire", "away_team": "Inter Miami",
        "xg_home_for": 1.53, "xg_home_against": 1.40,
        "xg_away_for": 1.72, "xg_away_against": 1.44,
        "elo_home": 1570, "elo_away": 1650,
        "odds": {"1": 2.15, "X": 4.20, "2": 2.80, "over_2_5": 1.26, "under_2_5": 3.70,
                 "btts_yes": 1.26},
    },
    {
        "home_team": "Austin FC", "away_team": "Colorado Rapids",
        "xg_home_for": 1.26, "xg_home_against": 1.91,
        "xg_away_for": 1.35, "xg_away_against": 1.28,
        "elo_home": 1470, "elo_away": 1560,
        "odds": {"1": 2.50, "X": 3.50, "2": 2.70, "over_2_5": 1.74, "under_2_5": 2.05,
                 "btts_yes": 1.58},
    },
    {
        "home_team": "Vancouver Whitecaps", "away_team": "LA Galaxy",
        "xg_home_for": 2.02, "xg_home_against": 0.93,
        "xg_away_for": 1.48, "xg_away_against": 1.54,
        "elo_home": 1690, "elo_away": 1500,
        "odds": {"1": 1.38, "X": 5.75, "2": 6.50, "over_2_5": 1.34, "under_2_5": 3.15,
                 "btts_yes": 1.58},
    },
    {
        "home_team": "San Diego FC", "away_team": "San Jose Earthquakes",
        "xg_home_for": 1.40, "xg_home_against": 1.42,
        "xg_away_for": 1.56, "xg_away_against": 1.46,
        "elo_home": 1540, "elo_away": 1580,
        "odds": {"1": 1.77, "X": 4.20, "2": 3.80, "over_2_5": 1.33, "under_2_5": 3.40,
                 "btts_yes": 1.36},
    },
    {
        "home_team": "Portland Timbers", "away_team": "St. Louis City",
        "xg_home_for": 1.49, "xg_home_against": 1.95,
        "xg_away_for": 1.57, "xg_away_against": 1.30,
        "elo_home": 1510, "elo_away": 1580,
        "odds": {"1": 2.30, "X": 4.20, "2": 2.80},
    },
    {
        "home_team": "Los Angeles FC", "away_team": "New York Red Bulls",
        "xg_home_for": 1.57, "xg_home_against": 1.43,
        "xg_away_for": 1.60, "xg_away_against": 1.52,
        "elo_home": 1610, "elo_away": 1490,
        "odds": {"1": 1.42, "X": 5.60, "2": 6.00, "over_2_5": 1.32, "under_2_5": 3.30,
                 "btts_yes": 1.44},
    },
]

for idx, m in enumerate(MATCHES, start=1):
    slug = f"{m['home_team']}_vs_{m['away_team']}".replace(" ", "_").replace(",", "")
    in_path = os.path.join(OUT, f"match_{idx:02d}_{slug}.json")
    out_path = os.path.join(RES, f"match_{idx:02d}_{slug}.json")
    with open(in_path, "w", encoding="utf-8") as fh:
        json.dump(m, fh, ensure_ascii=False, indent=2)
    result = subprocess.run(
        [sys.executable, os.path.join(REPO, "scripts", "calc_engine.py"),
         "--input", in_path, "--output", out_path],
        capture_output=True, text=True, cwd=REPO,
    )
    if result.returncode != 0:
        print(f"ERROR {idx}: {result.stderr}")
        continue
    print(f"OK {idx:02d}: {m['home_team']} vs {m['away_team']}")

print(f"\n{len(MATCHES)} partidos procesados. Salidas en {RES}")