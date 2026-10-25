import json
from scripts.selection import select_portfolio

with open("scratch/oct24/all_results.json") as f:
    all_results = json.load(f)

# Flatten candidates
candidates = []
for res in all_results:
    m_name = res["match"]
    league = res.get("league", "")
    commence_time = res.get("commence_time", "")
    for m_key, ev_data in res.get("evaluations", {}).items():
        if not ev_data.get("has_value"):
            continue
        c = dict(ev_data)
        c["match"] = m_name
        c["league"] = league
        c["commence_time"] = commence_time
        # selection string
        if m_key == "1":
            sel = m_name.split(" vs ")[0]
        elif m_key == "2":
            sel = m_name.split(" vs ")[1]
        elif m_key == "X":
            sel = "Empate (X)"
        elif m_key.startswith("over_"):
            sel = f"Más de {m_key.replace('over_', '').replace('_', '.')} goles"
        elif m_key.startswith("under_"):
            sel = f"Menos de {m_key.replace('under_', '').replace('_', '.')} goles"
        else:
            sel = m_key
        c["selection"] = sel
        candidates.append(c)

selected, excluded = select_portfolio(candidates, max_picks=6)

print(f"Total candidates: {len(candidates)}")
print(f"Selected: {len(selected)}")
for idx, s in enumerate(selected, 1):
    print(f"{idx}. {s['match']} ({s['league']}) | Mercado: {s['market']} | Selección: {s['selection']} | Cuota: {s['odds']} | Prob: {s['model_prob']:.1%} | Robust EV: {s['robust_ev_percent']:.1f}% | Stake: {s['stake_recommended_units']}u | Perfil: {s['selection_profile']}")

print(f"\nExcluded sample (top 5 by robust EV):")
excluded_sorted = sorted(excluded, key=lambda x: x['robust_ev_percent'], reverse=True)
for e in excluded_sorted[:5]:
    print(f" - {e['match']} | {e['market']} | Cuota: {e['odds']} | Prob: {e['model_prob']:.1%} | Robust EV: {e['robust_ev_percent']:.1f}% | Razón: {e['selection_reason']}")

