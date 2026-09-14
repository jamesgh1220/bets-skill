import json
import subprocess
import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath('scripts'))

BASE = Path('scratch/analysis_14sep')
OUT_DIR = BASE / 'outputs'
IN_DIR = BASE / 'inputs'
OUT_DIR.mkdir(parents=True, exist_ok=True)
IN_DIR.mkdir(parents=True, exist_ok=True)

# Team stats: xG_for, xG_against (season pace), Elo.
TEAM_STATS = {
    # Premier League
    "Leeds United": {"xg_for": 1.15, "xg_against": 1.10, "elo": 1670},
    "Newcastle United": {"xg_for": 1.45, "xg_against": 1.30, "elo": 1710},
    # LaLiga
    "Villarreal": {"xg_for": 1.50, "xg_against": 1.10, "elo": 1730},
    "Real Betis": {"xg_for": 1.25, "xg_against": 1.30, "elo": 1690},
    # Serie A
    "Como": {"xg_for": 1.10, "xg_against": 1.15, "elo": 1610},
    "Parma": {"xg_for": 0.95, "xg_against": 1.40, "elo": 1560},
    "Torino": {"xg_for": 1.20, "xg_against": 1.00, "elo": 1630},
    "Roma": {"xg_for": 1.30, "xg_against": 1.20, "elo": 1680},
    "Inter": {"xg_for": 1.75, "xg_against": 0.95, "elo": 1840},
    "Udinese": {"xg_for": 1.05, "xg_against": 1.35, "elo": 1600},
    # Liga Portugal
    "Rio Ave": {"xg_for": 1.00, "xg_against": 1.35, "elo": 1580},
    "Estrela Amadora": {"xg_for": 1.15, "xg_against": 1.25, "elo": 1620},
    "Moreirense": {"xg_for": 1.00, "xg_against": 1.15, "elo": 1600},
    "Marítimo": {"xg_for": 1.05, "xg_against": 1.35, "elo": 1580},
    "Braga": {"xg_for": 1.60, "xg_against": 1.10, "elo": 1770},
    "Estoril": {"xg_for": 0.90, "xg_against": 1.50, "elo": 1590},
    # Liga Argentina
    "Banfield": {"xg_for": 1.05, "xg_against": 1.20, "elo": 1610},
    "Barracas Central": {"xg_for": 0.80, "xg_against": 1.00, "elo": 1580},
    "Deportivo Riestra": {"xg_for": 0.90, "xg_against": 1.00, "elo": 1580},
    "Lanús": {"xg_for": 1.10, "xg_against": 0.95, "elo": 1650},
    "Instituto": {"xg_for": 1.40, "xg_against": 0.90, "elo": 1680},
    "Estudiantes Río Cuarto": {"xg_for": 0.80, "xg_against": 1.40, "elo": 1550},
    # Liga Colombiana
    "América de Cali": {"xg_for": 1.60, "xg_against": 0.80, "elo": 1720},
    "Deportivo Pasto": {"xg_for": 0.90, "xg_against": 1.70, "elo": 1520},
}

MATCHES_ORDER = [
    ("Leeds United", "Newcastle United", "Premier League"),
    ("Villarreal", "Real Betis", "LaLiga"),
    ("Como", "Parma", "Serie A"),
    ("Torino", "Roma", "Serie A"),
    ("Inter", "Udinese", "Serie A"),
    ("Rio Ave", "Estrela Amadora", "Liga Portugal"),
    ("Moreirense", "Marítimo", "Liga Portugal"),
    ("Braga", "Estoril", "Liga Portugal"),
    ("Banfield", "Barracas Central", "Liga Argentina"),
    ("Deportivo Riestra", "Lanús", "Liga Argentina"),
    ("Instituto", "Estudiantes Río Cuarto", "Liga Argentina"),
    ("América de Cali", "Deportivo Pasto", "Liga Colombiana"),
]

ODDS_MAP = {
    0: {"1": 2.50, "X": 3.40, "2": 2.87, "over_2_5": 2.10, "under_2_5": 1.72, "btts_yes": 1.72, "btts_no": 2.00},
    1: {"1": 2.45, "X": 3.35, "2": 2.95, "over_2_5": 1.90, "under_2_5": 1.90, "btts_yes": 1.80, "btts_no": 1.95},
    2: {"1": 2.30, "X": 3.25, "2": 3.25, "over_1_5": 1.33, "under_1_5": 3.10, "over_2_5": 1.95, "under_2_5": 1.85, "btts_yes": 1.65, "btts_no": 2.15},
    3: {"1": 2.80, "X": 3.00, "2": 2.75, "over_1_5": 1.25, "under_1_5": 3.75, "over_2_5": 1.75, "under_2_5": 2.05, "btts_yes": 1.70, "btts_no": 2.05},
    4: {"1": 1.45, "X": 4.60, "2": 7.00, "over_2_5": 1.62, "under_2_5": 2.25, "btts_yes": 1.85, "btts_no": 1.85},
    5: {"1": 2.55, "X": 3.20, "2": 2.95, "over_1_5": 1.38, "under_1_5": 2.90, "over_2_5": 2.10, "under_2_5": 1.72, "btts_yes": 1.80, "btts_no": 1.95},
    6: {"1": 2.40, "X": 3.20, "2": 2.85, "over_1_5": 1.40, "under_1_5": 2.75, "over_2_5": 2.03, "under_2_5": 1.83, "over_3_5": 4.00, "under_3_5": 1.22, "btts_yes": 1.95, "btts_no": 1.80},
    7: {"1": 1.44, "X": 4.50, "2": 6.80, "btts_yes": 1.83},
    8: {"over_2_5": 3.10, "under_2_5": 1.36, "btts_yes": 2.25, "btts_no": 1.57},
    9: {"1": 3.25, "X": 2.57, "2": 2.65, "over_1_5": 1.67, "under_1_5": 2.10, "over_2_5": 3.40, "under_2_5": 1.33, "btts_yes": 2.38, "btts_no": 1.53},
    10: {"1": 1.43, "X": 4.10, "2": 8.50},
    11: {"1": 1.37, "X": 4.20, "2": 7.50, "btts_no": 1.65},
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
    with open("scratch/results_14sep.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Matches: {len(all_results)} | Candidates: {len(all_candidates)} | "
          f"Evaluations: {len(all_evaluations)} | Selected: {len(selected)} | Excluded: {len(excluded)}")
    for i, s in enumerate(selected, 1):
        print(f"  PICK {i}: {s['match']} | {s['market']} | odds {s['odds']:.2f} | "
              f"prob {s['model_prob']:.1%} | fair {s['fair_odds']:.2f} | edge {s['edge']:+.2f}% | "
              f"EV {s['ev_percent']:+.2f}% | EVrob {s['robust_ev_percent']:+.2f}% | stake {s['stake_recommended_units']:.2f}u")


if __name__ == "__main__":
    main()