import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path("scripts").resolve()))
from selection import select_portfolio

out = json.loads(Path("scratch/rc_envigado_output.json").read_text(encoding="utf-8"))

match = out["match"]
home = "Real Cartagena"
away = "Envigado FC"

def enrich(market, ev):
    return {"match": match, "home_team": home, "away_team": away, "market": market, **ev}

all_evaluations = [enrich(k, v) for k, v in out["evaluations"].items()]
all_candidates = [e for e in all_evaluations if e.get("has_value")]
selected, excluded = select_portfolio(all_candidates, max_picks=6)

results = {
    "all_results": [out],
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded,
}
Path("scratch/rc_envigado_results.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print("CANDIDATES:", len(all_candidates))
for c in all_candidates:
    print(f"- {c['market']} odds={c['odds']} prob={c['model_prob']:.1%} rEV={c['robust_ev_percent']:.1f}% -> {c['selection_profile']}")
print("SELECTED:")
for s in selected:
    print(f"- {s['market']} odds={s['odds']} prob={s['model_prob']:.1%} stake={s['stake_recommended_units']}u profile={s['selection_profile']}")
print("EXCLUDED:")
for e in excluded:
    print(f"- {e['market']} odds={e['odds']} prob={e['model_prob']:.1%} rEV={e['robust_ev_percent']:.1f}% reason={e['selection_reason']}")