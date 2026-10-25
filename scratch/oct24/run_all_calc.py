import json
import subprocess
import os
import sys

with open("scratch/oct24/full_universe_inputs.json") as f:
    matches = json.load(f)

all_results = []
all_candidates = []
all_evaluations = []

for idx, m in enumerate(matches):
    in_file = f"scratch/oct24/input_{idx}.json"
    out_file = f"scratch/oct24/output_{idx}.json"
    
    with open(in_file, "w") as f:
        json.dump(m, f, indent=2)
        
    cmd = ["python3", "scripts/calc_engine.py", "--input", in_file, "--output", out_file]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error on match {m['home_team']} vs {m['away_team']}: {res.stderr}")
        continue
        
    with open(out_file) as f:
        out_data = json.load(f)
        out_data["league"] = m["league"]
        out_data["commence_time"] = m["commence_time"]
        all_results.append(out_data)
        
        # Check value candidates in evaluations
        for mk, ev_data in out_data.get("evaluations", {}).items():
            all_evaluations.append(ev_data)
            ev = ev_data.get("ev_percent", -100)
            robust_ev = ev_data.get("robust_ev_percent", -100)
            prob = ev_data.get("model_prob", 0)
            edge = ev_data.get("edge", 0)
            odds = ev_data.get("odds", 0)
            fair_odds = ev_data.get("fair_odds", 0)
            has_val = ev_data.get("has_value", False)
            stake = ev_data.get("stake_recommended_units", 0)
            
            c = {
                "match": f"{m['home_team']} vs {m['away_team']}",
                "league": m["league"],
                "commence_time": m["commence_time"],
                "market": mk,
                "selection": f"{m['home_team'] if mk == '1' else (m['away_team'] if mk == '2' else mk)}",
                "odds": odds,
                "fair_odds": fair_odds,
                "prob": prob,
                "edge": edge,
                "ev": ev,
                "robust_ev": robust_ev,
                "stake": stake,
                "has_value": has_val
            }
            if has_val or robust_ev > 0:
                all_candidates.append(c)

print(f"Processed {len(all_results)} matches successfully.")
print(f"Total value candidates: {len(all_candidates)}")

all_candidates.sort(key=lambda x: (x.get("robust_ev", 0), x.get("ev", 0)), reverse=True)
for c in all_candidates[:25]:
    print(f"{c['match']} ({c['league']}) | {c['market']} | Odds: {c['odds']} | Fair: {c['fair_odds']:.2f} | Prob: {c['prob']:.1%} | Edge: {c['edge']:.1f}% | Robust EV: {c['robust_ev']:.1f}% | Stake: {c['stake']}")

with open("scratch/oct24/all_results.json", "w") as f:
    json.dump(all_results, f, indent=2)

with open("scratch/oct24/all_candidates.json", "w") as f:
    json.dump(all_candidates, f, indent=2)

