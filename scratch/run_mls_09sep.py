import json, os, subprocess, sys

XG = {
    "Toronto FC":         (1.33, 1.48),
    "Nashville SC":       (1.36, 1.22),
    "CF Montreal":        (1.54, 1.37),
    "Charlotte FC":       (1.40, 1.64),
    "D.C. United":        (1.39, 1.61),
    "Columbus Crew":      (1.43, 1.24),
    "Atlanta United":     (1.36, 1.44),
    "Orlando City":       (1.41, 1.87),
    "Philadelphia Union": (1.78, 1.11),
    "FC Cincinnati":      (1.59, 1.78),
    "New York City FC":   (1.39, 1.43),
    "New England Revolution": (1.41, 1.56),
    "Minnesota United":   (1.50, 1.43),
    "FC Dallas":          (1.34, 1.46),
    "Houston Dynamo":     (1.46, 1.44),
    "Real Salt Lake":     (1.61, 1.47),
    "Chicago Fire":       (1.53, 1.40),
    "Inter Miami":        (1.72, 1.44),
    "Austin FC":          (1.26, 1.91),
    "Colorado Rapids":    (1.35, 1.28),
    "Vancouver Whitecaps":(2.02, 0.93),
    "LA Galaxy":          (1.48, 1.54),
    "San Diego FC":       (1.40, 1.42),
    "San Jose Earthquakes": (1.56, 1.46),
    "Portland Timbers":   (1.49, 1.95),
    "St. Louis City":     (1.57, 1.30),
    "LAFC":               (1.57, 1.43),
    "New York Red Bulls": (1.60, 1.52),
}

ELO = {
    "Toronto FC": 1490, "Nashville SC": 1680,
    "CF Montreal": 1470, "Charlotte FC": 1540,
    "D.C. United": 1480, "Columbus Crew": 1450,
    "Atlanta United": 1460, "Orlando City": 1490,
    "Philadelphia Union": 1500, "FC Cincinnati": 1530,
    "New York City FC": 1520, "New England Revolution": 1560,
    "Minnesota United": 1540, "FC Dallas": 1570,
    "Houston Dynamo": 1630, "Real Salt Lake": 1530,
    "Chicago Fire": 1570, "Inter Miami": 1650,
    "Austin FC": 1470, "Colorado Rapids": 1560,
    "Vancouver Whitecaps": 1690, "LA Galaxy": 1500,
    "San Diego FC": 1540, "San Jose Earthquakes": 1580,
    "Portland Timbers": 1510, "St. Louis City": 1580,
    "LAFC": 1610, "New York Red Bulls": 1490,
}

MATCHES = [
    ("Toronto FC", "Nashville SC", {"1": 2.90, "X": 3.60, "2": 2.30, "over_2_5": 1.67, "under_2_5": 2.16, "btts_yes": 1.54}),
    ("CF Montreal", "Charlotte FC", {"1": 2.30, "X": 3.90, "2": 2.80, "over_2_5": 1.55, "under_2_5": 2.40, "btts_yes": 1.47}),
    ("D.C. United", "Columbus Crew", {"1": 2.55, "X": 3.50, "2": 2.60, "over_2_5": 1.66, "under_2_5": 2.17, "btts_yes": 1.53}),
    ("Atlanta United", "Orlando City", {"1": 2.15, "X": 3.90, "2": 3.00}),
    ("Philadelphia Union", "FC Cincinnati", {"1": 1.69, "X": 4.33, "2": 4.20, "over_2_5": 1.36, "under_2_5": 3.05, "btts_yes": 1.40}),
    ("New York City FC", "New England Revolution", {"1": 2.25, "X": 3.60, "2": 3.00, "over_2_5": 1.85, "under_2_5": 1.86, "btts_yes": 1.57}),
    ("Minnesota United", "FC Dallas", {"1": 2.10, "X": 3.75, "2": 3.20, "over_2_5": 1.54, "under_2_5": 2.43, "btts_yes": 1.49}),
    ("Houston Dynamo", "Real Salt Lake", {"1": 1.74, "X": 4.09, "2": 4.20, "over_2_5": 1.60, "under_2_5": 2.30, "btts_yes": 1.56}),
    ("Chicago Fire", "Inter Miami", {"1": 2.15, "X": 4.20, "2": 2.80, "over_2_5": 1.26, "under_2_5": 3.70, "btts_yes": 1.26}),
    ("Austin FC", "Colorado Rapids", {"1": 2.50, "X": 3.50, "2": 2.70, "over_2_5": 1.74, "under_2_5": 2.05, "btts_yes": 1.58}),
    ("Vancouver Whitecaps", "LA Galaxy", {"1": 1.38, "X": 5.75, "2": 6.50, "over_2_5": 1.34, "under_2_5": 3.15, "btts_yes": 1.58}),
    ("San Diego FC", "San Jose Earthquakes", {"1": 1.77, "X": 4.20, "2": 3.80, "over_2_5": 1.33, "under_2_5": 3.40, "btts_yes": 1.36}),
    ("Portland Timbers", "St. Louis City", {"1": 2.30, "X": 4.20, "2": 2.80}),
    ("LAFC", "New York Red Bulls", {"1": 1.42, "X": 5.60, "2": 6.00, "over_2_5": 1.32, "under_2_5": 3.30, "btts_yes": 1.44}),
]

os.makedirs("scratch/mls_09sep", exist_ok=True)
match_details = []
for idx, (home, away, odds) in enumerate(MATCHES, 1):
    hxg = XG[home]; axg = XG[away]
    match_data = {
        "home_team": home, "away_team": away,
        "xg_home_for": hxg[0], "xg_home_against": hxg[1],
        "xg_away_for": axg[0], "xg_away_against": axg[1],
        "elo_home": ELO[home], "elo_away": ELO[away],
        "odds": odds,
    }
    in_path = f"scratch/mls_09sep/match_input_{idx:02d}.json"
    out_path = f"scratch/mls_09sep/match_output_{idx:02d}.json"
    with open(in_path, "w", encoding="utf-8") as f:
        json.dump(match_data, f, ensure_ascii=False)
    subprocess.run(["python3", "scripts/calc_engine.py", "--input", in_path, "--output", out_path], check=True)
    with open(out_path, encoding="utf-8") as f:
        out = json.load(f)
    match_details.append({"idx": idx, "match": f"{home} vs {away}", "home": home, "away": away, **out})

with open("scratch/mls_09sep/all_outputs.json", "w", encoding="utf-8") as f:
    json.dump(match_details, f, ensure_ascii=False, indent=2)

print(f"Completados {len(match_details)} partidos")

candidates = []
for md in match_details:
    for market, evd in md["evaluations"].items():
        if evd["has_value"]:
            cand = {k: evd[k] for k in ("market", "odds", "model_prob", "conservative_prob", "implied_prob", "fair_odds", "edge", "ev_percent", "robust_ev_percent", "stake_recommended_units")}
            cand["match"] = md["match"]
            cand["home"] = md["home"]; cand["away"] = md["away"]
            candidates.append(cand)

with open("scratch/mls_09sep/candidates.json", "w", encoding="utf-8") as f:
    json.dump(candidates, f, ensure_ascii=False, indent=2)

sys.path.insert(0, "scripts")
from selection import select_portfolio
selected, excluded = select_portfolio(candidates)
print(f"Candidatos con value: {len(candidates)}")
print(f"Seleccionados: {len(selected)}")
for s in selected:
    print(f"  - {s['match']} | {s['market']} | odds {s['odds']} | prob {s['model_prob']:.2%} | EVr {s['robust_ev_percent']:.1f}% | stake {s['stake_recommended_units']}u | {s['selection_profile']}")
for e in excluded:
    print(f"  X {e['match']} | {e['market']} | odds {e['odds']} | EVr {e['robust_ev_percent']:.1f}%")