import json
import subprocess
import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath('scripts'))

BASE = Path('scratch/analysis_13sep')
OUT_DIR = BASE / 'outputs'
IN_DIR = BASE / 'inputs'
OUT_DIR.mkdir(parents=True, exist_ok=True)
IN_DIR.mkdir(parents=True, exist_ok=True)

# Team stats: xG_for, xG_against (season pace), Elo.
TEAM_STATS = {
    # Premier League
    "Coventry City": {"xg_for": 0.90, "xg_against": 1.55, "elo": 1490},
    "Brighton & Hove Albion": {"xg_for": 1.65, "xg_against": 1.35, "elo": 1680},
    "Manchester United": {"xg_for": 1.90, "xg_against": 1.45, "elo": 1790},
    "Manchester City": {"xg_for": 2.05, "xg_against": 0.95, "elo": 1930},
    # LaLiga
    "Celta Vigo": {"xg_for": 1.15, "xg_against": 1.25, "elo": 1600},
    "Málaga": {"xg_for": 0.85, "xg_against": 1.60, "elo": 1500},
    "Levante": {"xg_for": 1.20, "xg_against": 1.30, "elo": 1550},
    "Barcelona": {"xg_for": 2.60, "xg_against": 0.55, "elo": 2010},
    "Getafe": {"xg_for": 0.95, "xg_against": 1.20, "elo": 1560},
    "Deportivo": {"xg_for": 1.55, "xg_against": 1.15, "elo": 1660},
    "Real Sociedad": {"xg_for": 1.20, "xg_against": 1.05, "elo": 1690},
    "Atlético Madrid": {"xg_for": 1.50, "xg_against": 0.95, "elo": 1780},
    # Bundesliga
    "RB Leipzig": {"xg_for": 1.65, "xg_against": 1.50, "elo": 1750},
    "Hamburg SV": {"xg_for": 0.75, "xg_against": 2.00, "elo": 1480},
    "SV Elversberg": {"xg_for": 1.30, "xg_against": 1.45, "elo": 1490},
    "Bayern Munich": {"xg_for": 2.30, "xg_against": 0.80, "elo": 1950},
    # Serie A
    "Lecce": {"xg_for": 0.95, "xg_against": 1.40, "elo": 1550},
    "Monza": {"xg_for": 1.10, "xg_against": 1.60, "elo": 1530},
    "Napoli": {"xg_for": 1.60, "xg_against": 1.35, "elo": 1750},
    "Bologna": {"xg_for": 1.05, "xg_against": 1.20, "elo": 1620},
    "Sassuolo": {"xg_for": 1.40, "xg_against": 1.30, "elo": 1620},
    "Juventus": {"xg_for": 1.70, "xg_against": 0.80, "elo": 1860},
    # Ligue 1
    "Lille": {"xg_for": 1.60, "xg_against": 0.95, "elo": 1700},
    "Troyes": {"xg_for": 1.00, "xg_against": 1.70, "elo": 1520},
    "Le Mans": {"xg_for": 1.15, "xg_against": 1.45, "elo": 1500},
    "Lens": {"xg_for": 1.35, "xg_against": 1.30, "elo": 1660},
    "Brest": {"xg_for": 1.45, "xg_against": 1.30, "elo": 1620},
    "Paris Saint-Germain": {"xg_for": 1.85, "xg_against": 1.10, "elo": 1900},
    # Eredivisie
    "Excelsior": {"xg_for": 1.80, "xg_against": 1.10, "elo": 1660},
    "FC Utrecht": {"xg_for": 1.35, "xg_against": 2.10, "elo": 1560},
    "Heerenveen": {"xg_for": 1.35, "xg_against": 1.70, "elo": 1590},
    "Telstar": {"xg_for": 1.05, "xg_against": 2.05, "elo": 1510},
    "PEC Zwolle": {"xg_for": 1.05, "xg_against": 1.80, "elo": 1550},
    "Feyenoord Rotterdam": {"xg_for": 1.90, "xg_against": 1.20, "elo": 1810},
    "PSV Eindhoven": {"xg_for": 2.15, "xg_against": 0.90, "elo": 1870},
    "Sparta Rotterdam": {"xg_for": 1.05, "xg_against": 1.65, "elo": 1560},
    # Liga Portugal
    "Arouca": {"xg_for": 1.40, "xg_against": 0.85, "elo": 1660},
    "Santa Clara": {"xg_for": 1.55, "xg_against": 0.70, "elo": 1690},
    "Benfica": {"xg_for": 2.20, "xg_against": 0.60, "elo": 1900},
    "Gil Vicente": {"xg_for": 1.10, "xg_against": 0.90, "elo": 1620},
    "FC Famalicao": {"xg_for": 0.95, "xg_against": 1.30, "elo": 1580},
    "Sporting CP": {"xg_for": 2.00, "xg_against": 0.80, "elo": 1870},
    # MLS
    "Chicago Fire FC": {"xg_for": 1.89, "xg_against": 1.43, "elo": 1620},
    "New England Revolution": {"xg_for": 1.61, "xg_against": 1.45, "elo": 1630},
    "Vancouver Whitecaps": {"xg_for": 2.21, "xg_against": 0.94, "elo": 1700},
    "Austin FC": {"xg_for": 1.06, "xg_against": 1.94, "elo": 1540},
    "San Diego FC": {"xg_for": 1.50, "xg_against": 1.40, "elo": 1600},
    "Philadelphia Union": {"xg_for": 1.60, "xg_against": 1.35, "elo": 1640},
    # Liga Argentina
    "Sarmiento (Junín)": {"xg_for": 1.60, "xg_against": 1.40, "elo": 1570},
    "Belgrano (Córdoba)": {"xg_for": 1.15, "xg_against": 0.80, "elo": 1680},
    "Tigre": {"xg_for": 1.05, "xg_against": 0.90, "elo": 1560},
    "Rosario Central": {"xg_for": 1.35, "xg_against": 1.15, "elo": 1590},
    "Argentinos Juniors": {"xg_for": 1.50, "xg_against": 0.95, "elo": 1700},
    "Gimnasia La Plata": {"xg_for": 1.30, "xg_against": 1.40, "elo": 1630},
    "Independiente": {"xg_for": 1.00, "xg_against": 0.80, "elo": 1670},
    "San Lorenzo": {"xg_for": 0.55, "xg_against": 0.85, "elo": 1580},
    "Huracán": {"xg_for": 1.10, "xg_against": 0.95, "elo": 1620},
    "Racing Club": {"xg_for": 1.25, "xg_against": 1.20, "elo": 1660},
    # Liga Colombiana
    "Deportivo Pereira": {"xg_for": 1.05, "xg_against": 1.50, "elo": 1530},
    "Atlético Bucaramanga": {"xg_for": 1.35, "xg_against": 0.95, "elo": 1620},
    "Atlético Nacional": {"xg_for": 1.70, "xg_against": 0.80, "elo": 1700},
    "Águilas Doradas": {"xg_for": 1.20, "xg_against": 1.25, "elo": 1550},
    "Once Caldas": {"xg_for": 1.30, "xg_against": 1.10, "elo": 1590},
    "Deportivo Cali": {"xg_for": 1.05, "xg_against": 1.10, "elo": 1560},
    "Cúcuta Deportivo": {"xg_for": 0.95, "xg_against": 1.70, "elo": 1520},
    "Millonarios": {"xg_for": 1.30, "xg_against": 0.90, "elo": 1650},
}

MATCHES_ORDER = [
    ("Coventry City", "Brighton & Hove Albion", "Premier League"),
    ("Manchester United", "Manchester City", "Premier League"),
    ("Celta Vigo", "Málaga", "LaLiga"),
    ("Levante", "Barcelona", "LaLiga"),
    ("Getafe", "Deportivo", "LaLiga"),
    ("Real Sociedad", "Atlético Madrid", "LaLiga"),
    ("RB Leipzig", "Hamburg SV", "Bundesliga"),
    ("SV Elversberg", "Bayern Munich", "Bundesliga"),
    ("Lecce", "Monza", "Serie A"),
    ("Napoli", "Bologna", "Serie A"),
    ("Sassuolo", "Juventus", "Serie A"),
    ("Lille", "Troyes", "Ligue 1"),
    ("Le Mans", "Lens", "Ligue 1"),
    ("Brest", "Paris Saint-Germain", "Ligue 1"),
    ("Excelsior", "FC Utrecht", "Eredivisie"),
    ("Heerenveen", "Telstar", "Eredivisie"),
    ("PEC Zwolle", "Feyenoord Rotterdam", "Eredivisie"),
    ("PSV Eindhoven", "Sparta Rotterdam", "Eredivisie"),
    ("Arouca", "Santa Clara", "Liga Portugal"),
    ("Benfica", "Gil Vicente", "Liga Portugal"),
    ("FC Famalicao", "Sporting CP", "Liga Portugal"),
    ("Chicago Fire FC", "New England Revolution", "MLS"),
    ("Vancouver Whitecaps", "Austin FC", "MLS"),
    ("San Diego FC", "Philadelphia Union", "MLS"),
    ("Sarmiento (Junín)", "Belgrano (Córdoba)", "Liga Argentina"),
    ("Tigre", "Rosario Central", "Liga Argentina"),
    ("Argentinos Juniors", "Gimnasia La Plata", "Liga Argentina"),
    ("Independiente", "San Lorenzo", "Liga Argentina"),
    ("Huracán", "Racing Club", "Liga Argentina"),
    ("Deportivo Pereira", "Atlético Bucaramanga", "Liga Colombiana"),
    ("Atlético Nacional", "Águilas Doradas", "Liga Colombiana"),
    ("Once Caldas", "Deportivo Cali", "Liga Colombiana"),
    ("Cúcuta Deportivo", "Millonarios", "Liga Colombiana"),
]

ODDS_MAP = {
    0: {"1": 4.00, "X": 3.75, "2": 1.85, "over_2_5": 1.83, "under_2_5": 2.10, "btts_yes": 1.70},
    1: {"1": 3.30, "X": 3.80, "2": 2.11, "under_3_5": 1.70},
    2: {"1": 1.80, "X": 3.80, "2": 5.38, "over_1_5": 1.37, "under_1_5": 3.25, "over_2_5": 2.07, "under_2_5": 1.78, "over_3_5": 3.60, "under_3_5": 1.29, "btts_yes": 2.03, "btts_no": 1.85},
    3: {"1": 15.00, "X": 9.00, "2": 1.14},
    4: {"1": 2.53, "X": 2.97, "2": 4.00, "over_1_5": 1.69, "under_1_5": 2.15, "over_2_5": 1.70, "under_2_5": 2.35, "btts_yes": 2.50, "btts_no": 1.51},
    5: {"1": 2.92, "X": 3.68, "2": 2.39, "under_2_5": 2.15},
    6: {"1": 1.43, "X": 5.00, "2": 7.31, "btts_yes": 1.62, "btts_no": 2.21},
    7: {"1": 12.00, "X": 8.00, "2": 1.14, "btts_yes": 1.52},
    8: {"1": 2.70, "X": 3.12, "2": 2.80, "under_2_5": 1.67, "btts_yes": 1.90, "btts_no": 1.82},
    9: {"1": 1.84, "X": 3.58, "2": 4.65, "over_2_5": 1.85, "under_2_5": 1.85},
    10: {"1": 5.20, "X": 3.90, "2": 1.60, "over_2_5": 1.78, "under_2_5": 1.95, "btts_yes": 1.82},
    11: {"1": 1.40, "X": 4.80, "2": 7.00, "over_2_5": 1.70, "btts_yes": 1.95},
    12: {"1": 5.64, "X": 4.41, "2": 1.64, "over_1_5": 1.20, "under_1_5": 4.40, "over_2_5": 1.66, "over_3_5": 2.64, "under_3_5": 1.48, "btts_yes": 1.78, "btts_no": 2.18},
    13: {"1": 9.25, "X": 6.10, "2": 1.24, "btts_yes": 1.71},
    14: {"1": 2.20, "X": 3.70, "2": 2.95, "over_2_5": 1.60},
    15: {"1": 1.63, "X": 4.50, "2": 4.60, "over_1_5": 1.11, "under_1_5": 6.50, "over_2_5": 1.40, "under_2_5": 2.88, "over_3_5": 1.91, "under_3_5": 1.80, "btts_yes": 1.50, "btts_no": 2.50},
    16: {"1": 6.00, "X": 5.00, "2": 1.42, "over_2_5": 1.38, "btts_yes": 1.51},
    17: {"1": 1.20, "X": 7.00, "2": 11.00},
    18: {"1": 2.65, "X": 3.00, "2": 2.90, "over_2_5": 2.07, "under_2_5": 1.44, "btts_yes": 1.89, "btts_no": 1.63},
    19: {"1": 1.15, "X": 7.20, "2": 15.00},
    20: {"1": 5.66, "X": 4.23, "2": 1.51, "over_2_5": 1.75, "btts_no": 1.92},
    21: {"1": 1.87, "X": 3.85, "2": 3.50, "over_3_5": 1.77, "under_3_5": 1.72, "btts_yes": 1.44, "btts_no": 2.63},
    22: {"1": 1.28, "X": 5.75, "2": 8.50, "over_3_5": 1.87, "under_3_5": 1.85, "btts_yes": 1.80, "btts_no": 1.95},
    23: {"1": 2.60, "X": 3.65, "2": 2.40, "over_3_5": 1.76, "under_3_5": 1.64, "btts_yes": 1.44, "btts_no": 2.70},
    24: {"1": 3.15, "X": 3.10, "2": 2.40, "over_2_5": 2.76, "under_2_5": 1.54, "btts_yes": 2.20, "btts_no": 1.79},
    25: {"1": 2.90, "X": 2.90, "2": 2.70, "over_2_5": 2.80, "under_2_5": 1.51, "btts_yes": 2.23, "btts_no": 1.66},
    26: {"1": 1.72, "X": 3.60, "2": 4.90, "over_1_5": 1.36, "under_1_5": 3.00, "over_2_5": 2.20, "under_2_5": 1.65, "over_3_5": 4.00, "under_3_5": 1.22, "btts_yes": 2.05, "btts_no": 1.70},
    27: {"1": 2.05, "X": 3.00, "2": 4.00, "over_1_5": 1.57, "under_1_5": 2.25, "over_2_5": 2.88, "under_2_5": 1.40, "over_3_5": 6.00, "under_3_5": 1.13, "btts_yes": 2.25, "btts_no": 1.57},
    28: {"1": 2.65, "X": 2.75, "2": 3.15},
    29: {"1": 4.20, "X": 3.50, "2": 1.74},
    30: {"1": 1.39, "X": 3.95, "2": 8.00},
    31: {"1": 2.00, "X": 3.20, "2": 3.55},
    32: {"1": 4.20, "X": 3.35, "2": 1.77, "over_1_5": 1.30, "over_2_5": 2.02, "under_2_5": 1.80, "over_3_5": 3.65, "btts_yes": 1.89},
}


def build_input(idx, home, away, league):
    hs = TEAM_STATS[home]
    as_ = TEAM_STATS[away]
    data = {
        "home_team": home,
        "away_team": away,
        "league": league,
        "xg_home_for": hs["xg_for"],
        "xg_home_against": hs["xg_against"],
        "xg_away_for": as_["xg_for"],
        "xg_away_against": as_["xg_against"],
        "elo_home": hs["elo"],
        "elo_away": as_["elo"],
        "odds": ODDS_MAP[idx],
        "match": f"{home} vs {away}",
    }
    return data


def main():
    all_results = []
    all_candidates = []
    all_evaluations = []

    for idx, (home, away, league) in enumerate(MATCHES_ORDER):
        data = build_input(idx, home, away, league)
        in_file = IN_DIR / f"input_{idx:02d}.json"
        out_file = OUT_DIR / f"output_{idx:02d}.json"
        in_file.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")

        subprocess.run(
            [sys.executable, "scripts/calc_engine.py",
             "--input", str(in_file), "--output", str(out_file)],
            check=True, capture_output=True, cwd=os.getcwd(),
        )
        res = json.loads(out_file.read_text(encoding="utf-8"))
        all_results.append(res)

        for market, ev in res["evaluations"].items():
            row = dict(ev)
            row.update({"match": res["match"], "home_team": home, "away_team": away})
            all_evaluations.append(row)
            if ev.get("has_value"):
                cand = dict(ev)
                cand.update({"match": res["match"], "home_team": home, "away_team": away})
                all_candidates.append(cand)

    import selection
    selected, excluded = selection.select_portfolio(all_candidates, max_picks=6)

    seen = set()
    deduped = []
    for s in selected:
        if s["match"] in seen:
            excluded.append(s)
            continue
        seen.add(s["match"])
        deduped.append(s)
    selected = deduped

    results = {
        "all_results": all_results,
        "all_candidates": all_candidates,
        "all_evaluations": all_evaluations,
        "selected": selected,
        "excluded": excluded,
    }
    with open("scratch/results_13sep.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Matches: {len(all_results)} | Candidates: {len(all_candidates)} | "
          f"Evaluations: {len(all_evaluations)} | Selected: {len(selected)} | Excluded: {len(excluded)}")
    for i, s in enumerate(selected, 1):
        print(f"  PICK {i}: {s['match']} | {s['market']} | odds {s['odds']:.2f} | "
              f"prob {s['model_prob']:.1%} | fair {s['fair_odds']:.2f} | edge {s['edge']:+.2f}% | "
              f"EV {s['ev_percent']:+.2f}% | EVrob {s['robust_ev_percent']:+.2f}% | stake {s['stake_recommended_units']:.2f}u")


if __name__ == "__main__":
    main()