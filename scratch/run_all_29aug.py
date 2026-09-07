import json
import subprocess
import sys
import os

# Todos los partidos del 29 de agosto de 2026 con datos recopilados
matches = [
    # === PREMIER LEAGUE ===
    {
        "home_team": "Liverpool", "away_team": "Nottingham Forest",
        "league": "Premier League",
        "xg_home_for": 1.61, "xg_home_against": 1.25,
        "xg_away_for": 1.21, "xg_away_against": 1.51,
        "elo_home": 1905, "elo_away": 1780,
        "odds": {"1": 1.45, "X": 4.25, "2": 5.50, "over_2_5": 1.57, "under_2_5": 2.35, "btts_yes": 1.70}
    },
    {
        "home_team": "AFC Bournemouth", "away_team": "Everton",
        "league": "Premier League",
        "xg_home_for": 1.63, "xg_home_against": 1.49,
        "xg_away_for": 1.23, "xg_away_against": 1.49,
        "elo_home": 1833, "elo_away": 1795,
        "odds": {"1": 2.10, "X": 3.50, "2": 3.40, "over_2_5": 1.85, "under_2_5": 1.95, "btts_yes": 1.72}
    },
    {
        "home_team": "Tottenham Hotspur", "away_team": "Newcastle United",
        "league": "Premier League",
        "xg_home_for": 1.05, "xg_home_against": 1.38,
        "xg_away_for": 1.50, "xg_away_against": 1.35,
        "elo_home": 1790, "elo_away": 1856,
        "odds": {"1": 2.25, "X": 3.60, "2": 2.95, "over_2_5": 1.65, "under_2_5": 2.20, "btts_yes": 1.57}
    },
    # === LALIGA ===
    {
        "home_team": "Levante", "away_team": "Real Betis",
        "league": "LaLiga",
        "xg_home_for": 1.38, "xg_home_against": 1.62,
        "xg_away_for": 1.46, "xg_away_against": 1.21,
        "elo_home": 1681, "elo_away": 1786,
        "odds": {"1": 3.25, "X": 3.35, "2": 2.23, "over_2_5": 1.91, "under_2_5": 1.90, "btts_yes": 1.75}
    },
    {
        "home_team": "Real Sociedad", "away_team": "Espanyol",
        "league": "LaLiga",
        "xg_home_for": 1.43, "xg_home_against": 1.48,
        "xg_away_for": 1.29, "xg_away_against": 1.63,
        "elo_home": 1747, "elo_away": 1684,
        "odds": {"1": 1.85, "X": 3.70, "2": 4.30, "over_2_5": 1.83, "under_2_5": 1.98, "btts_yes": 1.73}
    },
    {
        "home_team": "Sevilla", "away_team": "Atletico de Madrid",
        "league": "LaLiga",
        "xg_home_for": 1.03, "xg_home_against": 1.61,
        "xg_away_for": 1.55, "xg_away_against": 1.27,
        "elo_home": 1699, "elo_away": 1876,
        "odds": {"1": 3.60, "X": 3.40, "2": 2.05, "over_2_5": 2.00, "under_2_5": 1.80, "btts_yes": 1.80}
    },
    # === SERIE A ===
    {
        "home_team": "Fiorentina", "away_team": "Frosinone",
        "league": "Serie A",
        "xg_home_for": 1.40, "xg_home_against": 1.25,
        "xg_away_for": 0.95, "xg_away_against": 1.65,
        "elo_home": 1707, "elo_away": 1635,
        "odds": {"1": 1.62, "X": 3.90, "2": 5.50, "over_2_5": 1.80, "under_2_5": 1.95, "btts_yes": 1.80}
    },
    {
        "home_team": "Monza", "away_team": "Udinese",
        "league": "Serie A",
        "xg_home_for": 1.11, "xg_home_against": 1.75,
        "xg_away_for": 1.63, "xg_away_against": 1.15,
        "elo_home": 1616, "elo_away": 1683,
        "odds": {"1": 2.95, "X": 3.25, "2": 2.40, "over_2_5": 2.15, "under_2_5": 1.67, "btts_yes": 1.95}
    },
    {
        "home_team": "Sassuolo", "away_team": "Torino",
        "league": "Serie A",
        "xg_home_for": 1.45, "xg_home_against": 1.40,
        "xg_away_for": 1.18, "xg_away_against": 1.20,
        "elo_home": 1669, "elo_away": 1670,
        "odds": {"1": 2.22, "X": 3.30, "2": 3.25, "over_2_5": 1.90, "under_2_5": 1.90, "btts_yes": 1.73}
    },
    {
        "home_team": "Juventus", "away_team": "Parma",
        "league": "Serie A",
        "xg_home_for": 1.96, "xg_home_against": 0.65,
        "xg_away_for": 0.87, "xg_away_against": 1.85,
        "elo_home": 1818, "elo_away": 1638,
        "odds": {"1": 1.22, "X": 6.85, "2": 15.50, "over_2_5": 1.67, "under_2_5": 2.22, "btts_yes": 2.35}
    },
    # === LIGUE 1 ===
    {
        "home_team": "Strasbourg", "away_team": "Lens",
        "league": "Ligue 1",
        "xg_home_for": 1.15, "xg_home_against": 1.80,
        "xg_away_for": 2.10, "xg_away_against": 1.05,
        "elo_home": 1714, "elo_away": 1812,
        "odds": {"1": 3.65, "X": 3.70, "2": 2.10, "over_2_5": 1.78, "under_2_5": 2.02, "btts_yes": 1.70}
    },
    {
        "home_team": "Lyon", "away_team": "Le Havre",
        "league": "Ligue 1",
        "xg_home_for": 1.85, "xg_home_against": 0.95,
        "xg_away_for": 0.85, "xg_away_against": 1.70,
        "elo_home": 1769, "elo_away": 1591,
        "odds": {"1": 1.52, "X": 4.65, "2": 7.45, "over_2_5": 1.65, "under_2_5": 2.25, "btts_yes": 1.85}
    },
    {
        "home_team": "Lorient", "away_team": "Troyes",
        "league": "Ligue 1",
        "xg_home_for": 1.20, "xg_home_against": 1.10,
        "xg_away_for": 0.90, "xg_away_against": 1.45,
        "elo_home": 1675, "elo_away": 1592,
        "odds": {"1": 1.84, "X": 3.55, "2": 4.30, "over_2_5": 2.00, "under_2_5": 1.80, "btts_yes": 1.95}
    },
    {
        "home_team": "Brest", "away_team": "Toulouse",
        "league": "Ligue 1",
        "xg_home_for": 1.30, "xg_home_against": 1.35,
        "xg_away_for": 1.32, "xg_away_against": 1.30,
        "elo_home": 1655, "elo_away": 1667,
        "odds": {"1": 2.70, "X": 3.50, "2": 2.75, "over_2_5": 1.90, "under_2_5": 1.90, "btts_yes": 1.74}
    },
    {
        "home_team": "Auxerre", "away_team": "Angers",
        "league": "Ligue 1",
        "xg_home_for": 1.10, "xg_home_against": 1.50,
        "xg_away_for": 0.95, "xg_away_against": 1.60,
        "elo_home": 1634, "elo_away": 1590,
        "odds": {"1": 1.95, "X": 3.50, "2": 4.10, "over_2_5": 2.00, "under_2_5": 1.80, "btts_yes": 1.80}
    },
    # === LIGA ARGENTINA ===
    {
        "home_team": "Deportivo Riestra", "away_team": "Velez Sarsfield",
        "league": "Liga Argentina",
        "xg_home_for": 0.85, "xg_home_against": 1.20,
        "xg_away_for": 1.30, "xg_away_against": 1.10,
        "elo_home": 1550, "elo_away": 1697,
        "odds": {"1": 2.82, "X": 2.78, "2": 2.87, "under_2_5": 1.65}
    },
    {
        "home_team": "Rosario Central", "away_team": "Gimnasia La Plata",
        "league": "Liga Argentina",
        "xg_home_for": 1.35, "xg_home_against": 1.10,
        "xg_away_for": 1.05, "xg_away_against": 1.40,
        "elo_home": 1723, "elo_away": 1620,
        "odds": {"1": 1.94, "X": 3.30, "2": 4.60, "under_2_5": 1.70}
    },
    {
        "home_team": "Huracan", "away_team": "Estudiantes Rio Cuarto",
        "league": "Liga Argentina",
        "xg_home_for": 1.15, "xg_home_against": 0.95,
        "xg_away_for": 0.80, "xg_away_against": 1.30,
        "elo_home": 1680, "elo_away": 1530,
        "odds": {"1": 1.72, "X": 3.40, "2": 5.20, "under_2_5": 1.55}
    },
    {
        "home_team": "Talleres", "away_team": "Central Cordoba",
        "league": "Liga Argentina",
        "xg_home_for": 1.40, "xg_home_against": 1.00,
        "xg_away_for": 0.75, "xg_away_against": 1.55,
        "elo_home": 1700, "elo_away": 1520,
        "odds": {"1": 1.66, "X": 3.50, "2": 6.10, "under_2_5": 1.60}
    },
    {
        "home_team": "Atletico Tucuman", "away_team": "Belgrano",
        "league": "Liga Argentina",
        "xg_home_for": 1.10, "xg_home_against": 0.90,
        "xg_away_for": 1.20, "xg_away_against": 1.15,
        "elo_home": 1640, "elo_away": 1660,
        "odds": {"1": 2.88, "X": 2.92, "2": 2.90, "under_2_5": 1.55}
    },
    # === LIGA COLOMBIANA ===
    {
        "home_team": "Jaguares", "away_team": "America de Cali",
        "league": "Liga Colombiana",
        "xg_home_for": 0.75, "xg_home_against": 1.40,
        "xg_away_for": 1.45, "xg_away_against": 0.85,
        "elo_home": 1480, "elo_away": 1647,
        "odds": {"1": 4.45, "X": 3.40, "2": 1.79, "under_2_5": 1.65}
    },
    {
        "home_team": "Junior", "away_team": "Independiente Santa Fe",
        "league": "Liga Colombiana",
        "xg_home_for": 1.10, "xg_home_against": 1.30,
        "xg_away_for": 1.25, "xg_away_against": 0.95,
        "elo_home": 1600, "elo_away": 1640,
        "odds": {"1": 1.89, "X": 3.35, "2": 4.03, "under_2_5": 1.60}
    },
    {
        "home_team": "Alianza Valledupar", "away_team": "Atletico Nacional",
        "league": "Liga Colombiana",
        "xg_home_for": 0.70, "xg_home_against": 1.50,
        "xg_away_for": 1.55, "xg_away_against": 0.90,
        "elo_home": 1450, "elo_away": 1698,
        "odds": {"1": 3.90, "X": 3.25, "2": 1.97, "under_2_5": 1.60}
    },
    # === MLS ===
    {
        "home_team": "DC United", "away_team": "LAFC",
        "league": "MLS",
        "xg_home_for": 1.20, "xg_home_against": 1.55,
        "xg_away_for": 1.70, "xg_away_against": 1.25,
        "elo_home": 1530, "elo_away": 1651,
        "odds": {"1": 3.30, "X": 3.60, "2": 2.10, "over_2_5": 1.65}
    },
    {
        "home_team": "Seattle Sounders", "away_team": "Chicago Fire",
        "league": "MLS",
        "xg_home_for": 1.25, "xg_home_against": 1.40,
        "xg_away_for": 1.30, "xg_away_against": 1.35,
        "elo_home": 1570, "elo_away": 1540,
        "odds": {"1": 2.40, "X": 3.50, "2": 3.00, "over_2_5": 1.70}
    },
    {
        "home_team": "Atlanta United", "away_team": "Charlotte FC",
        "league": "MLS",
        "xg_home_for": 1.30, "xg_home_against": 1.50,
        "xg_away_for": 1.15, "xg_away_against": 1.35,
        "elo_home": 1540, "elo_away": 1560,
        "odds": {"1": 2.60, "X": 3.45, "2": 2.70, "over_2_5": 1.75}
    },
    {
        "home_team": "Inter Miami", "away_team": "CF Montreal",
        "league": "MLS",
        "xg_home_for": 1.85, "xg_home_against": 1.30,
        "xg_away_for": 1.10, "xg_away_against": 1.60,
        "elo_home": 1667, "elo_away": 1510,
        "odds": {"1": 1.40, "X": 4.50, "2": 7.00, "over_2_5": 1.55}
    },
    {
        "home_team": "NY Red Bulls", "away_team": "Philadelphia Union",
        "league": "MLS",
        "xg_home_for": 1.40, "xg_home_against": 1.30,
        "xg_away_for": 1.35, "xg_away_against": 1.40,
        "elo_home": 1580, "elo_away": 1575,
        "odds": {"1": 2.30, "X": 3.50, "2": 3.10, "over_2_5": 1.72}
    },
    {
        "home_team": "Toronto FC", "away_team": "NYCFC",
        "league": "MLS",
        "xg_home_for": 1.15, "xg_home_against": 1.50,
        "xg_away_for": 1.55, "xg_away_against": 1.20,
        "elo_home": 1530, "elo_away": 1590,
        "odds": {"1": 3.10, "X": 3.55, "2": 2.25, "over_2_5": 1.68}
    },
    {
        "home_team": "Columbus Crew", "away_team": "New England Revolution",
        "league": "MLS",
        "xg_home_for": 1.55, "xg_home_against": 1.10,
        "xg_away_for": 1.00, "xg_away_against": 1.50,
        "elo_home": 1610, "elo_away": 1490,
        "odds": {"1": 1.65, "X": 3.80, "2": 5.00, "over_2_5": 1.70}
    },
    {
        "home_team": "Houston Dynamo", "away_team": "San Jose Earthquakes",
        "league": "MLS",
        "xg_home_for": 1.45, "xg_home_against": 1.20,
        "xg_away_for": 0.95, "xg_away_against": 1.55,
        "elo_home": 1580, "elo_away": 1470,
        "odds": {"1": 1.70, "X": 3.75, "2": 4.80, "over_2_5": 1.72}
    },
    # === EREDIVISIE ===
    {
        "home_team": "Excelsior Rotterdam", "away_team": "Sparta Rotterdam",
        "league": "Eredivisie",
        "xg_home_for": 1.70, "xg_home_against": 1.65,
        "xg_away_for": 1.87, "xg_away_against": 1.80,
        "elo_home": 1473, "elo_away": 1498,
        "odds": {"1": 2.45, "X": 3.71, "2": 2.68, "over_2_5": 1.55, "under_2_5": 2.40, "btts_yes": 1.50}
    },
    {
        "home_team": "AZ Alkmaar", "away_team": "Go Ahead Eagles",
        "league": "Eredivisie",
        "xg_home_for": 2.97, "xg_home_against": 0.85,
        "xg_away_for": 1.77, "xg_away_against": 1.40,
        "elo_home": 1672, "elo_away": 1525,
        "odds": {"1": 1.48, "X": 4.60, "2": 6.20, "over_2_5": 1.58, "under_2_5": 2.35, "btts_yes": 1.67}
    },
    {
        "home_team": "PEC Zwolle", "away_team": "NEC Nijmegen",
        "league": "Eredivisie",
        "xg_home_for": 1.10, "xg_home_against": 1.95,
        "xg_away_for": 2.80, "xg_away_against": 1.25,
        "elo_home": 1464, "elo_away": 1587,
        "odds": {"1": 4.30, "X": 4.30, "2": 1.68, "over_2_5": 1.40, "under_2_5": 2.87, "btts_yes": 1.44}
    },
    # === LIGA PORTUGAL ===
    {
        "home_team": "Alverca", "away_team": "Santa Clara",
        "league": "Liga Portugal",
        "xg_home_for": 1.17, "xg_home_against": 1.45,
        "xg_away_for": 1.47, "xg_away_against": 0.90,
        "elo_home": 1504, "elo_away": 1532,
        "odds": {"1": 2.70, "X": 3.10, "2": 2.65, "over_2_5": 2.35, "under_2_5": 1.56, "btts_yes": 1.87}
    },
    {
        "home_team": "Arouca", "away_team": "Maritimo",
        "league": "Liga Portugal",
        "xg_home_for": 1.07, "xg_home_against": 1.15,
        "xg_away_for": 1.38, "xg_away_against": 1.35,
        "elo_home": 1546, "elo_away": 1480,
        "odds": {"1": 2.28, "X": 3.25, "2": 3.10, "over_2_5": 2.10, "under_2_5": 1.72, "btts_yes": 1.80}
    },
    {
        "home_team": "Academico de Viseu", "away_team": "FC Porto",
        "league": "Liga Portugal",
        "xg_home_for": 0.98, "xg_home_against": 1.85,
        "xg_away_for": 2.22, "xg_away_against": 0.55,
        "elo_home": 1458, "elo_away": 1807,
        "odds": {"1": 8.50, "X": 5.20, "2": 1.32, "over_2_5": 1.80, "under_2_5": 2.00, "btts_yes": 2.15}
    },
]

os.makedirs("scratch", exist_ok=True)

all_results = []

for idx, match in enumerate(matches):
    input_path = f"scratch/match_input_{idx}.json"
    output_path = f"scratch/match_output_{idx}.json"
    
    with open(input_path, "w", encoding="utf-8") as f:
        json.dump(match, f, ensure_ascii=False)
        
    result = subprocess.run(
        ["python3", "scripts/calc_engine.py", "--input", input_path, "--output", output_path],
        capture_output=True, text=True
    )
    
    if result.returncode != 0:
        print(f"ERROR en partido {idx}: {match['home_team']} vs {match['away_team']}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        continue
    
    with open(output_path, "r", encoding="utf-8") as f:
        res = json.load(f)
        res["league"] = match["league"]
        all_results.append(res)

# Guardar todos los resultados consolidados
with open("scratch/all_results_29aug.json", "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)

# Mostrar solo mercados con value
print("=" * 80)
print("MERCADOS CON VALUE DETECTADO (has_value = true)")
print("=" * 80)
for r in all_results:
    for mk, ev in r.get("evaluations", {}).items():
        if ev.get("has_value"):
            print(f"\n🎯 {r['league']} | {r['match']}")
            print(f"   Mercado: {ev['market']} @ {ev['odds']}")
            print(f"   Prob Modelo: {ev['model_prob']*100:.1f}% | Prob Implícita: {ev['implied_prob']*100:.1f}%")
            print(f"   Cuota Justa: {ev['fair_odds']} | Edge: {ev['edge']:.1f}% | EV: {ev['ev_percent']:.1f}%")
            print(f"   Stake Kelly Fraccional: {ev['stake_recommended_units']}u")

print(f"\nTotal partidos procesados: {len(all_results)}")
