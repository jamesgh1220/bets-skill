import json
import glob
import os

BASE = os.path.dirname(os.path.abspath(__file__))
MATCH_LABELS = {
    "input_01_union_schalke.json": "Union Berlin vs Schalke 04 (Bundesliga)",
    "input_02_sevilla_valencia.json": "Sevilla vs Valencia (LaLiga)",
    "input_03_venezia_fiorentina.json": "Venezia vs Fiorentina (Serie A)",
    "input_04_rennes_marseille.json": "Rennes vs Marseille (Ligue 1)",
    "input_05_az_willem.json": "AZ Alkmaar vs Willem II (Eredivisie)",
    "input_06_newells_velez.json": "Newell's vs Vélez (LPF Argentina)",
    "input_07_defensa_gimnasiamza.json": "Defensa y Justicia vs Gimnasia (Mza) (LPF Argentina)",
    "input_08_boca_ccordoba.json": "Boca Juniors vs Central Córdoba (LPF Argentina)",
    "input_09_jaguares_fortaleza.json": "Jaguares vs Fortaleza (Liga BetPlay)",
    "input_10_santafe_tolima.json": "Santa Fe vs Tolima (Liga BetPlay)",
}
SELECTION_TXT = {
    "1": "Victoria local",
    "X": "Empate",
    "2": "Victoria visitante",
    "over_1_5": "Más de 1.5 goles",
    "under_1_5": "Menos de 1.5 goles",
    "over_2_5": "Más de 2.5 goles",
    "under_2_5": "Menos de 2.5 goles",
    "over_3_5": "Más de 3.5 goles",
    "btts_yes": "Ambos marcan (Sí)",
    "btts_no": "Ambos marcan (No)",
    "1x": "Doble oportunidad local/empate",
    "x2": "Doble oportunidad empate/visitante",
    "12": "Doble oportunidad sin empate",
    "dnb_home": "Sin empate local",
    "dnb_away": "Sin empate visitante",
}

candidates = []
for path in sorted(glob.glob(os.path.join(BASE, "output_*.json"))):
    d = json.load(open(path))
    match = d["match"]
    input_file = os.path.basename(path).replace("output_", "input_")
    label = MATCH_LABELS.get(input_file, match)
    for market, ev in d["evaluations"].items():
        if not ev["has_value"]:
            continue
        candidates.append({
            "match": label,
            "market": market,
            "selection": SELECTION_TXT.get(market, market),
            "odds": ev["odds"],
            "model_prob": ev["model_prob"],
            "conservative_prob": ev["conservative_prob"],
            "implied_prob": ev["implied_prob"],
            "fair_odds": ev["fair_odds"],
            "edge": ev["edge"],
            "ev_percent": ev["ev_percent"],
            "robust_ev_percent": ev["robust_ev_percent"],
            "stake_recommended_units": ev["stake_recommended_units"],
            "has_value": ev["has_value"],
        })

with open(os.path.join(BASE, "all_candidates.json"), "w", encoding="utf-8") as f:
    json.dump(candidates, f, ensure_ascii=False, indent=2)
print(f"candidates with value: {len(candidates)}")
for c in candidates:
    print(f"  {c['match'][:45]:45s} {c['market']:12s} odds={c['odds']:6.2f} p={c['model_prob']:.3f} robust={c['robust_ev_percent']:6.2f}%")