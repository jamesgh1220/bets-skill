import json
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from scripts.selection import select_portfolio, classify_candidate

with open("scratch/all_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

# Sort candidates by model_prob, robust_ev_percent, ev_percent
candidates.sort(key=lambda x: (x["model_prob"], x["robust_ev_percent"], x["ev_percent"]), reverse=True)

selected, excluded = select_portfolio(candidates, max_picks=6)

print(f"Total Candidates: {len(candidates)}")
print(f"Selected ({len(selected)}):")
for s in selected:
    print(f"  {s['match']} | Mercado: {s['market']} | Cuota: {s['odds']} | Prob: {s['model_prob']*100:.1f}% | EV rob: {s['robust_ev_percent']}% | Stake: {s['stake_recommended_units']}u | Perfil: {s['selection_profile']}")

print(f"\nExcluded ({len(excluded)}):")
for e in excluded[:10]:
    print(f"  {e['match']} | Mercado: {e['market']} | Cuota: {e['odds']} | Prob: {e['model_prob']*100:.1f}% | EV rob: {e['robust_ev_percent']}% | Razón: {e['selection_reason']}")

with open("scratch/selected_picks.json", "w", encoding="utf-8") as f:
    json.dump(selected, f, indent=2, ensure_ascii=False)

with open("scratch/excluded_picks.json", "w", encoding="utf-8") as f:
    json.dump(excluded, f, indent=2, ensure_ascii=False)
