import json, subprocess, os

ODDS = json.load(open("scratch/odds_17sep/odds_clean.json"))

# event_id -> (home_team, away_team)
EVENT = {
    "cff5815d2f10c40b034716e082023a84": ("OFI Crete", "TSG Hoffenheim"),
    "7293d131a4072c4123dde03fb3e50b3e": ("PFC Levski Sofia", "Salzburg"),
    "72b83b12135b1fcb72f4c154804a5e3f": ("Besiktas JK", "Marseille"),
    "802837ee46675cf2e15f0492a56d269a": ("Real Sociedad", "Bournemouth"),
    "f2d062505296c5434be2d3b7345807ae": ("Celtic", "Ferencváros TC"),
    "e21f5417eecd4ef4cb1581eee499b80a": ("Crystal Palace", "Lech Poznań"),
    "8e42b05b63dfa24c0f5785aac3835fe5": ("Juventus", "NEC Nijmegen"),
    "01678a3de0b0537624fbc64304d90710": ("Lillestrom", "Torreense"),
    "9fdd372c461b22bca9a6306427583499": ("Viktoria Plzeň", "Union Saint-Gilloise"),
    "7f644eca099054612d9a7e7e5d8787da": ("Real Betis", "Getafe"),
    "56c5e4d30fc27dedb3ae48a80b81346d": ("Málaga", "Villarreal"),
    "e521d4165ecf78c3b58864293e866030": ("Manchester City", "Norwich City"),
    "9f51bed6dc9cb798333ea483c49ec233": ("Flamengo-RJ", "Independiente del Valle"),
    "10d8075d3ece90f2ada6650e988c69d9": ("Montevideo City Torque", "Club Cienciano"),
}

MAR = {
    "OFI Crete vs TSG Hoffenheim": (1.67,1.59,1.87,1.85,1473,1754,3.0,5.5,6.7,4.0,0.5,2.5,2.33,0.67),
    "PFC Levski Sofia vs Salzburg": (2.20,0.76,2.85,1.37,1583,1646,4.9,4.1,8.3,3.4,2.0,2.11,1.0,2.4),
    "Besiktas JK vs Marseille": (1.74,0.46,1.65,1.51,1693,1775,6.3,4.0,5.3,4.3,2.11,2.33,1.25,2.25),
    "Real Sociedad vs Bournemouth": (0.93,1.66,1.50,1.60,1768,1859,7.7,3.8,4.5,5.0,2.3,3.0,3.2,1.5),
    "Celtic vs Ferencváros TC": (1.28,0.25,1.46,1.59,1692,1657,9.7,4.2,4.4,3.2,1.0,2.2,1.8,2.2),
    "Crystal Palace vs Lech Poznań": (1.63,1.93,2.11,0.84,1818,1676,1.0,5.67,7.33,4.0,0.67,0.67,1.5,2.17),
    "Juventus vs NEC Nijmegen": (1.95,0.95,1.90,1.30,1833,1591,9.8,2.1,4.4,3.4,1.8,2.1,1.8,1.8),
    "Lillestrom vs Torreense": (1.68,1.55,0.95,1.30,1530,1449,5.4,6.7,4.1,4.2,1.7,2.4,None,None),
    "Viktoria Plzeň vs Union Saint-Gilloise": (1.65,1.50,2.0,1.2,1638,1803,5.0,4.8,4.7,4.1,2.5,3.5,2.3,1.7),
    "Real Betis vs Getafe": (1.20,2.10,0.75,1.40,1817,1699,4.1,5.0,4.7,4.0,2.0,3.0,3.0,2.0),
    "Málaga vs Villarreal": (1.00,1.40,1.75,1.30,1677,1788,5.0,4.8,6.6,4.25,2.3,2.0,2.0,2.3),
    "Manchester City vs Norwich City": (2.20,0.70,1.90,1.55,2032,1620,5.4,2.8,4.9,4.8,1.8,2.0,3.0,2.0),
    "Flamengo-RJ vs Independiente del Valle": (1.64,1.31,1.93,1.03,1828,1758,5.37,4.33,6.4,3.4,2.65,None,1.75,2.38),
    "Montevideo City Torque vs Club Cienciano": (1.43,1.08,1.46,1.35,1550,1593,4.3,5.0,5.13,3.87,2.9,None,1.36,None),
}

def odds_for(evid, home, away):
    ev = ODDS[evid]
    h2h = ev["markets"].get("h2h", {})
    o = {}
    for k, v in h2h.items():
        if k == home: o["1"] = v["median"]
        elif k == away: o["2"] = v["median"]
        elif k == "Draw": o["X"] = v["median"]
    tot = ev["markets"].get("totals", {})
    for line in ("1.5","2.5","3.5"):
        ok, uk = f"Over@{line}", f"Under@{line}"
        if ok in tot: o[f"over_{line.replace('.','_')}"] = tot[ok]["median"]
        if uk in tot: o[f"under_{line.replace('.','_')}"] = tot[uk]["median"]
    return o

os.makedirs("scratch/inputs_17sep", exist_ok=True)
os.makedirs("scratch/outputs_17sep", exist_ok=True)

inputs = {}
for evid, (home, away) in EVENT.items():
    (cf, ca, af, aa, eh, ea,
     chf, cha, cof, coa, cahf, caha, cao_away_for, cao_away_against) = MAR[f"{home} vs {away}"]
    inp = {
        "home_team": home, "away_team": away,
        "xg_home_for": cf, "xg_home_against": ca,
        "xg_away_for": af, "xg_away_against": aa,
        "elo_home": eh, "elo_away": ea,
        "corners_home_for": chf, "corners_home_against": cha,
        "corners_away_for": cof, "corners_away_against": coa,
        "cards_home_for": cahf, "cards_home_against": caha,
        "cards_away_for": cao_away_for, "cards_away_against": cao_away_against,
        "odds": odds_for(evid, home, away),
    }
    inp = {k: (v if v is not None else None) for k, v in inp.items()}
    inputs[evid] = inp
    path = f"scratch/inputs_17sep/{evid[:8]}.json"
    with open(path, "w") as fh:
        json.dump(inp, fh, ensure_ascii=False, indent=1)

results = {}
for evid in EVENT:
    ip = f"scratch/inputs_17sep/{evid[:8]}.json"
    op = f"scratch/outputs_17sep/{evid[:8]}.json"
    r = subprocess.run(["python3", "scripts/calc_engine.py", "--input", ip, "--output", op],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR", evid[:8], r.stderr[-400:]); continue
    results[evid] = json.load(open(op))
print("engine runs done:", len(results), "/", len(EVENT))
# summary of evaluations with value
for evid, res in results.items():
    m = res["match"]
    for k, ev in res["evaluations"].items():
        if ev["has_value"]:
            print(f"{m:45s} {k:12s} odds={ev['odds']:.2f} prob={ev['model_prob']:.3f} fair={ev['fair_odds']:.2f} "
                  f"EV={ev['ev_percent']:+.1f}% rEV={ev['robust_ev_percent']:+.1f}% stake={ev['stake_recommended_units']:.2f}")
json.dump(results, open("scratch/outputs_17sep/all_results_raw.json","w"), ensure_ascii=False, indent=1)
print("saved all_results_raw.json")