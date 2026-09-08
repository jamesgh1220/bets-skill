"""Sensibilidad de candidatos 2026-09-08: perturba xG y Elo y reevalúa el motor."""
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
from calc_engine import run_ensemble, load_model_config

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = load_model_config("models/model-v1.2.json")

CASES = [
    ("match_03_Borussia_Dortmund_vs_Villarreal", "over_2_5"),
    ("match_04_Lille_vs_Real_Betis", "over_2_5"),
    ("match_12_NEC_Nijmegen_vs_Excelsior", "2"),
    ("match_09_Crystal_Palace_vs_Middlesbrough", "2"),
    ("match_11_Sunderland_vs_Hull_City", "2"),
    ("match_15_Boca_Juniors_vs_Sao_Paulo", "2"),
]

def variant(base, dxg, delo):
    m = dict(base)
    m["xg_home_for"] += dxg; m["xg_home_against"] += dxg
    m["xg_away_for"] += dxg; m["xg_away_against"] += dxg
    m["elo_home"] += delo; m["elo_away"] -= delo
    return m

for name, market in CASES:
    path = os.path.join(HERE, "inputs_08sep", f"{name}.json")
    base = json.load(open(path))
    res_base = run_ensemble(base, CFG)
    ev0 = res_base["evaluations"][market]
    print("=" * 78)
    print(f"{name}  [{market}]  cuota {ev0['odds']}  base: p={ev0['model_prob']:.3f} EV={ev0['ev_percent']:+.1f}% EVrob={ev0['robust_ev_percent']:+.1f}%")
    for label, dxg, delo in [
        ("baja xG -0.15", -0.15, 0), ("sube xG +0.15", 0.15, 0),
        ("Elo -50 local", 0, -50), ("Elo +50 local", 0, 50),
        ("extremo -0.30 xG", -0.30, -75), ("extremo +0.30 xG", 0.30, 75),
    ]:
        m = variant(base, dxg, delo)
        r = run_ensemble(m, CFG)
        ev = r["evaluations"][market]
        flag = "OK" if ev["robust_ev_percent"] >= 5.0 or market != "over_2_5" and ev["robust_ev_percent"] >= 10.0 else "FRAGIL"
        print(f"   {label:>18s}: p={ev['model_prob']:.3f} EV={ev['ev_percent']:+.1f}% EVrob={ev['robust_ev_percent']:+.1f}%  [{flag}]")