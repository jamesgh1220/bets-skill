"""Ensambla results/meta JSON para el 21/09 y renderiza el artefacto."""
import json
import os
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(BASE, "..", "scripts")
sys.path.insert(0, SCRIPTS)

from selection import select_portfolio

TEAMS = {
    "Lanús vs Estudiantes de La Plata": ("Lanús", "Estudiantes de La Plata"),
    "Barracas Central vs Independiente Rivadavia": ("Barracas Central", "Independiente Rivadavia"),
    "Bogotá F.C. vs Barranquilla F.C.": ("Bogotá F.C.", "Barranquilla F.C."),
    "Real Cundinamarca vs Deportes Quindío": ("Real Cundinamarca", "Deportes Quindío"),
    "Real Cartagena vs Envigado FC": ("Real Cartagena", "Envigado FC"),
}

OUTPUTS = [
    "match_output_lanus_estudiantes.json",
    "match_output_barracas_rivadavia.json",
    "match_output_bogota_barranquilla.json",
    "match_output_cundinamarca_quindio.json",
    "match_output_cartagena_envigado.json",
]

all_results = []
all_evaluations = []
for fn in OUTPUTS:
    with open(os.path.join(BASE, fn), encoding="utf-8") as f:
        out = json.load(f)
    match_name = out["match"]
    home, away = TEAMS[match_name]
    evaluations = {}
    for key, ev in out["evaluations"].items():
        enriched = dict(ev)
        enriched["match"] = match_name
        enriched["home_team"] = home
        enriched["away_team"] = away
        evaluations[key] = enriched
        enriched_flat = dict(enriched)
        enriched_flat.pop("market", None) if enriched_flat.get("market") else None
        all_evaluations.append(enriched)
    all_results.append({
        "match": match_name,
        "home_team": home,
        "away_team": away,
        "probabilities": out["probabilities"],
        "evaluations": evaluations,
    })

all_candidates = [dict(e) for e in all_evaluations if e.get("has_value")]

for c in all_candidates:
    if c.get("market") and "match" in c and c["market"] not in {}:
        pass
    c.setdefault("selection_profile", "excluido")
    c.setdefault("selection_reason", "Sin clasificar")

selected, excluded = select_portfolio(list(all_candidates))

results = {
    "all_results": all_results,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded,
}

with open(os.path.join(BASE, "results_21sep.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

now = datetime.now(timezone.utc)
cutoff = now.strftime("%Y-%m-%dT%H:%M:%SZ")

meta = {
    "analysis_date_iso": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "match_dates_text": "21 de septiembre de 2026",
    "information_cutoff": cutoff,
    "model_ia": "bigpickle",
    "engine_version": "model-v1.3",
    "leagues_display": "Liga Profesional Argentina (Zonas A y B) y Primera B de Colombia",
    "requested_range": "21 de septiembre de 2026 — Liga Argentina y Primera B Colombia (todos los partidos)",
    "universe_preamble": (
        "Universo = interseccion(ligas liga argentina + primera B colombia, fecha 21 de septiembre de 2026, todos los partidos programados). "
        f"Cutoff de informacion {cutoff} (anterior a todos los kickoffs: Bogota-Barranquilla 20:30 UTC, Barracas-IRivadavia y Real Cundinamarca-Quindio 22:00 UTC, "
        "Lanus-Estudiantes 00:15 UTC 22/09, Real Cartagena-Envigado 00:30 UTC 22/09). Aldosivi vs Atletico Tucuman se EXCLUYE por kickoff 17:30 UTC "
        "(partido en curso al cierre; no se usa informacion posterior al kickoff). MCPs inoperativos: apifootball devolvio 'Authentification failed!', "
        "football-stats sin datos 2026 (no corners/cards via MCP) y odds-api null, por lo que la investigacion se realizo via web (agente): "
        "APWin, FootyStats, OddStorm, PrimaTips, FootyBets, sitios de clubes, Soccerstats. Las tasas de corners/tarjetas for/against constan en cada match_input "
        "(campo obligatorio); las cuotas O/U de corners/tarjetas NO estan disponibles en las fuentes, por lo que esos mercados quedan NO DISPONIBLES (no se inventan cuotas). "
        "Nota Primera B: kickoff Bogota-Barranquilla con discrepancia 15:30 vs 16:30 COT en fuentes (APWin/OddStorm: 15:30 COT = 20:30 UTC); se consigna 20:30 UTC."
    ),
    "universe_matches": [
        "1. **Liga Argentina, Zona A:** Lanus vs Estudiantes de La Plata (21 septiembre, 21:15 ART / 00:15 UTC; 1X2 Betsson 2.24 / bwin 2.14 / luckia 2.30; Est. 2 3.24-3.77; U2.5 mejor 1.37 bwin; BTTS mejor 2.27).",
        "2. **Liga Argentina, Zona B:** Barracas Central vs Independiente Rivadavia (19:00 ART / 22:00 UTC; 1X2 PrimaTips 3.40/3.05/2.30-2.41; O1.5 1.50/U1.5 2.50; O2.5 2.60/U2.5 1.48; O3.5 5.50/U3.5 1.14; BTTS 2.10/1.67).",
        "3. **Primera B Colombia:** Bogota FC vs Barranquilla FC (15:30 COT / 20:30 UTC, Estadio Olaya Herrera; 1X2 OddStorm 1.73/3.70/4.50; O/U 2.5 1.99/1.92; O/U 3.5 3.60/1.35).",
        "4. **Primera B Colombia:** Real Cundinamarca (Real Soacha) vs Deportes Quindio (17:00 COT / 22:00 UTC; 1X2 OddStorm 2.20/3.15/3.90; O/U 2.5 2.44/1.64; O/U 3.5 4.80/1.24).",
        "5. **Primera B Colombia:** Real Cartagena vs Envigado FC (19:30 COT / 00:30 UTC; 1X2 Gainblers 1.75/3.50/5.10; O/U 2.5 1.97/1.77; O/U 3.5 3.10/1.33).",
        "EXCLUIDO: **Liga Argentina, Zona B:** Aldosivi vs Atletico Tucuman (kickoff 17:30 UTC 21/09; en curso al cierre -> NO BET pos-kickoff, sin analisis).",
    ],
    "picks_details": [],
    "fallback_source": (
        "MCPs no operativos (apifootball 'Authentification failed!', football-stats sin datos 2026/27, odds-api null). "
        "Investigacion del agente via web: APWin.com (xG, forma, corners, tarjetas, cuotas), FootyStats (xG n=22/12), "
        "OddStorm/PrimaTips (odds Colombia/Argentina), FootyBets (tarjetas), Soccerstats, Wikipedia/Fotmob (kicks/times), "
        "sportsgambler/TyC (Argentina). Elo: clubelo (Argentina), estimates a partir de footywow/render para Primera B (sin clubelo). "
        "Motor calc_engine.py model-v1.3 con calibracion Platt (1/2, O/U 2.5 y O/U 3.5). xG Lanus-Estudiantes con discrepancia proveedores "
        "(APWin 1.47/1.50 y 1.61/1.29 vs statz 1.32/1.02 y 1.24/1.03); se uso APWin (n=26 liga, directo). Tarjetas Envigado APWin 1.47 vs "
        "input agente 2.55; se uso APWin. Primera B sin Elo clubelo: estimaciones documentadas en match_input."
    ),
}

with open(os.path.join(BASE, "meta_21sep.json"), "w", encoding="utf-8") as f:
    json.dump(meta, f, indent=2, ensure_ascii=False)

print("results_21sep.json y meta_21sep.json escritos")
print(f"candidatos con value: {len(all_candidates)}, seleccionados: {len(selected)}")