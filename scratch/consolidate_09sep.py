"""Consolida salidas de calc_engine para el universo 2026-09-09 y aplica selección."""
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
sys.path.insert(0, os.path.join(REPO, "scripts"))

from selection import select_portfolio, classify_candidate


def _sel(mk, ev):
    if mk == "1":
        return "Local (1)"
    if mk == "X":
        return "Empate (X)"
    if mk == "2":
        return "Visitante (2)"
    if mk.startswith("over_"):
        line = mk.replace("over_", "").replace("_", ".")
        return f"Over {line}"
    if mk.startswith("under_"):
        line = mk.replace("under_", "").replace("_", ".")
        return f"Under {line}"
    if mk == "btts_yes":
        return "BTTS Sí"
    if mk == "btts_no":
        return "BTTS No"
    if mk == "1x":
        return "1X"
    if mk == "x2":
        return "X2"
    if mk == "12":
        return "12"
    return mk


RES = os.path.join(BASE, "outputs_09sep")
files = sorted(f for f in os.listdir(RES) if f.endswith(".json"))

candidates = []
for f in files:
    with open(os.path.join(RES, f), encoding="utf-8") as fh:
        data = json.load(fh)
    match = data["match"]
    for mk, ev in data["evaluations"].items():
        if ev["has_value"] or ev["ev_percent"] > 0:
            cand = {
                "match": match,
                "market": ev["market"],
                "selection": _sel(mk, ev),
                "odds": ev["odds"],
                "model_prob": ev["model_prob"],
                "conservative_prob": ev["conservative_prob"],
                "implied_prob": ev["implied_prob"],
                "fair_odds": ev["fair_odds"],
                "edge": ev["edge"],
                "ev_percent": ev["ev_percent"],
                "robust_ev_percent": ev["robust_ev_percent"],
                "stake_recommended_units": ev["stake_recommended_units"],
            }
            candidates.append(cand)

candidates.sort(key=lambda c: (c["robust_ev_percent"], c["ev_percent"], c["model_prob"]), reverse=True)

selected, excluded = select_portfolio([dict(c) for c in candidates])

print("=" * 120)
print(f"{'R':<3}{'Partido':<34}{'Merc':<11}{'Sel':<18}{'Cuota':>6}{'Prob':>7}{'Justa':>7}{'Edge':>8}{'EV':>8}{'EVrob':>8}{'Stake':>6}")
print("=" * 120)
for i, c in enumerate(candidates, 1):
    sel = "-"
    profile = classify_candidate(c)[0]
    if c in selected:
        sel = "SEL"
    print(f"{i:<3}{c['match']:<34}{c['market']:<11}{c['selection']:<18}{c['odds']:>6.2f}"
          f"{c['model_prob']*100:>6.1f}%{c['fair_odds']:>7.2f}{c['edge']:>8.1f}{c['ev_percent']:>8.1f}"
          f"{c['robust_ev_percent']:>8.1f}{c['stake_recommended_units']:>5.2f}u {sel:<4}{profile}")

print("\nSELECCIONADOS:")
for c in selected:
    print(f"  {c['match']} | {c['market']} | {c['selection']} | {c['odds']} | "
          f"prob {c['model_prob']*100:.1f}% | fair {c['fair_odds']} | EV {c['ev_percent']:.1f}% | "
          f"EVr {c['robust_ev_percent']:.1f}% | stake {c['stake_recommended_units']:.2f}u")

print(f"\nTotal candidatos con value: {len(candidates)}")
print(f"Seleccionados: {len(selected)} | Excluidos: {len(excluded)}")

with open(os.path.join(BASE, "candidates_09sep.json"), "w", encoding="utf-8") as fh:
    json.dump({"candidates": candidates, "selected": selected, "excluded": excluded}, fh,
              ensure_ascii=False, indent=2)