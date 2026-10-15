"""Ensambla inputs, ejecuta el motor model-v1.3, selecciona y genera results/meta para 2026-10-15.

Universo: UEFA Europa League (MD2) + UEFA Conference League (MD1) + Copa Libertadores (semifinal ida).
MCPs inoperativos -> investigacion web del agente (archivos data_15oct_*.json en scratch/).
Cutoff de informacion: 2026-10-15T13:30Z (anterior a todos los kickoffs).

Politica de datos (igual que runs 13/14-oct):
- Si faltan los 4 valores de xG verificables, NO se ejecuta el motor (evitar priors por defecto).
- Conflictos de xG arbitrados y documentados en `notes` de cada archivo de datos.
"""
import glob
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

from selection import select_portfolio

MODEL_CONFIG = os.path.join("models", "model-v1.3.json")
ENGINE = os.path.join("scripts", "calc_engine.py")

DATA_GLOB = os.path.join(BASE, "data_15oct_*.json")
XG_KEYS = ("xg_home_for", "xg_home_against", "xg_away_for", "xg_away_against")
RATE_KEYS = (
    "elo_home", "elo_away",
    "corners_home_for", "corners_home_against", "corners_away_for", "corners_away_against",
    "cards_home_for", "cards_home_against", "cards_away_for", "cards_away_against",
)


def load_matches():
    matches = []
    for path in sorted(glob.glob(DATA_GLOB)):
        with open(path, encoding="utf-8") as f:
            matches.extend(json.load(f))
    return matches


def build_input(rec):
    inp = {}
    for key in XG_KEYS + RATE_KEYS:
        inp[key] = rec.get(key)
    inp["odds"] = rec.get("odds") or {}
    return inp


def run_engine(inp, slug):
    inp_path = os.path.join(BASE, f"match_input_15oct_{slug}.json")
    out_path = os.path.join(BASE, f"match_output_15oct_{slug}.json")
    with open(inp_path, "w", encoding="utf-8") as f:
        json.dump(inp, f, indent=2, ensure_ascii=False)
    subprocess.run(
        [sys.executable, ENGINE, "--input", inp_path, "--output", out_path, "--config", MODEL_CONFIG],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    with open(out_path, encoding="utf-8") as f:
        return json.load(f)


def why_base_for(rec):
    elo_h, elo_a = rec.get("elo_home"), rec.get("elo_away")
    xg_hf, xg_ha = rec.get("xg_home_for"), rec.get("xg_home_against")
    xg_af, xg_aa = rec.get("xg_away_for"), rec.get("xg_away_against")
    parts = []
    if elo_h and elo_a:
        diff = abs(elo_h - elo_a)
        fav = "local" if elo_h >= elo_a else "visitante"
        parts.append(f"Elo favorece al {fav} ({max(elo_h, elo_a):.0f} vs {min(elo_h, elo_a):.0f}, brecha {diff:.0f})")
    if all(v is not None for v in (xg_hf, xg_ha, xg_af, xg_aa)):
        parts.append(
            f"perfil xG {xg_hf:.2f}/{xg_ha:.2f} (local) vs {xg_af:.2f}/{xg_aa:.2f} (visitante)"
        )
    return " | ".join(parts) + "."


def risks_for(rec, inp):
    missing = [k for k in ("over_1_5", "under_1_5", "over_3_5", "under_3_5", "btts_yes") if k not in inp["odds"]]
    parts = []
    if missing:
        parts.append("Cuotas no cotizadas: " + ", ".join(missing))
    null_rates = [k for k in RATE_KEYS if inp.get(k) is None]
    if null_rates:
        parts.append("Tasas sin publicar: " + ", ".join(null_rates))
    if rec.get("notes"):
        parts.append(str(rec["notes"]))
    return "; ".join(parts) if parts else "Sin riesgos de datos adicionales."


def universe_line(idx, rec):
    odds = rec.get("odds") or {}
    kickoff = rec.get("kickoff_utc", "?").replace("2026-10-", "").replace(":00Z", "Z")
    bits = [f"{odds[k]:.2f}" for k in ("1", "X", "2") if k in odds]
    ou = " ".join(f"{k.replace('over_','O').replace('under_','U').replace('_','.')} {odds[k]:.2f}"
                  for k in ("over_1_5", "under_1_5", "over_2_5", "under_2_5", "over_3_5", "under_3_5") if k in odds)
    extras = " ".join(f"{k} {odds[k]:.2f}" for k in ("btts_yes", "btts_no", "1x", "x2", "12",
                      "over_corners_8_5", "under_corners_8_5", "over_cards_5_5", "under_cards_5_5") if k in odds)
    elo = f"Elo {rec.get('elo_home', 'n/d')}/{rec.get('elo_away', 'n/d')}"
    xg = f"xG {rec.get('xg_home_for', 'n/d')}/{rec.get('xg_home_against', 'n/d')} vs {rec.get('xg_away_for', 'n/d')}/{rec.get('xg_away_against', 'n/d')}"
    l1x2 = " ".join(bits)
    suffix = " DATOS INSUFICIENTES (xG visitante no verificable) -> NO BET." if rec.get("_limited") else ""
    return f"{idx}. **{rec['league'].split(' - ')[0]}:** {rec['match']} ({kickoff}). 1X2 {l1x2}; {ou}; {extras}. {elo}; {xg}.{suffix}"


def main():
    records = load_matches()
    for rec in records:
        limited = any(rec.get(k) is None for k in XG_KEYS)
        rec["_limited"] = limited

    all_results = []
    all_evaluations = []
    data_limited_reasons = {}
    for rec in records:
        name = rec["match"]
        if rec["_limited"]:
            data_limited_reasons[name] = (
                "No hay xG verificable del visitante en ninguna fuente consultada; ejecutar el motor "
                "habria exigido priors por defecto, por lo que no se ejecuto."
            )
            all_results.append({
                "match": name, "home_team": rec["home"], "away_team": rec["away"],
                "probabilities": {}, "evaluations": {}, "data_limited": True,
            })
            continue
        inp = build_input(rec)
        slug = f"{rec['home']}-{rec['away']}".lower().replace(" ", "_").replace(".", "").replace("/", "").replace("'", "")
        out = run_engine(inp, slug)
        evaluations = {}
        for key, ev in out["evaluations"].items():
            enriched = dict(ev)
            enriched["match"] = name
            enriched["home_team"] = rec["home"]
            enriched["away_team"] = rec["away"]
            evaluations[key] = enriched
            all_evaluations.append(enriched)
        all_results.append({
            "match": name, "home_team": rec["home"], "away_team": rec["away"],
            "probabilities": out["probabilities"], "evaluations": evaluations,
        })

    all_candidates = [dict(e) for e in all_evaluations if e.get("has_value")]
    for c in all_candidates:
        c.setdefault("selection_profile", "excluido")
        c.setdefault("selection_reason", "Sin clasificar")

    selected, excluded = select_portfolio(list(all_candidates))

    rec_by_name = {r["match"]: r for r in records}

    def pick_detail(cand):
        rec = rec_by_name[cand["match"]]
        inp = build_input(rec)
        from render_artifact import market_label  # noqa: E402
        label = market_label(cand["market"], cand["home_team"], cand["away_team"])
        why = (
            f"{why_base_for(rec)} El motor model-v1.3 estima {cand['model_prob']:.1%} para '{label}' "
            f"frente a una probabilidad implicita de {cand['implied_prob']:.1%} (cuota {cand['odds']:.2f}); "
            f"edge {cand['edge']:+.2f}% y EV robusto {cand['robust_ev_percent']:+.2f}%."
        )
        return {
            "match": cand["match"], "market": cand["market"],
            "min_odds": f"{cand['fair_odds']:.2f}",
            "incertidumbre": "Base +/- 5.0% (model-v1.3); muestras 3-27 partidos segun liga/club",
            "why": why,
            "risks": risks_for(rec, inp),
            "sources": f"{rec.get('sources', 'web del agente')}; verosimilitud del modelo y calibracion Platt (model-v1.3).",
        }

    picks_details = [pick_detail(s) for s in selected]

    results = {
        "all_results": all_results,
        "all_candidates": all_candidates,
        "all_evaluations": all_evaluations,
        "selected": selected,
        "excluded": excluded,
    }
    with open(os.path.join(BASE, "results_15oct.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    now = datetime.now(timezone.utc)
    cutoff = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = {
        "analysis_date_iso": cutoff,
        "match_dates_text": "15 de octubre de 2026",
        "information_cutoff": cutoff,
        "model_ia": "big-pickle",
        "engine_version": "model-v1.3",
        "leagues_display": "UEFA Europa League (fase de liga, MD2), UEFA Conference League (MD1) y Copa Libertadores (semifinal de ida)",
        "requested_range": "15 de octubre de 2026 - Europa League, Conference League y Copa Libertadores (todos los partidos)",
        "universe_preamble": (
            "Universo = interseccion(ligas: Europa League + Conference League + Copa Libertadores, fecha 15 de octubre de 2026, todos los partidos programados). "
            f"Cutoff de informacion {cutoff}, anterior al primer kickoff (16:45 UTC). No se usa informacion posterior a ningun kickoff. "
            "Universo final = 37 partidos (18 de Europa League fase de liga MD2: 8 a las 16:45 UTC y 10 a las 19:00 UTC; "
            "18 de Conference League MD1: 10 a las 16:45 UTC y 8 a las 19:00 UTC; 1 semifinal de ida de Copa Libertadores a las 00:30 UTC del 16/10). "
            "MCPs inoperativos en esta sesion (apifootball/odds-api/football-stats), por lo que toda la recoleccion se hizo via web del agente: "
            "statz.ai, xg-edge.com, footystats.org, futbor.com, makeyourstats.com, matchscan, performanceodds, totalcorner, clubelo.com/beta.clubelo, "
            "dailysportpick.com, sportytrader, fox sports, betfred, bettingstats, xpect y fuentes de contraste. "
            "Conflictos de xG arbitrados con la muestra domestica mas grande y documentados en las notas de cada partido. "
            "Jagiellonia vs Ararat-Armenia queda como NO BET por falta de xG verificable del visitante (liga armenia sin cobertura xG). "
            "Los mercados de corners y tarjetas quedan sin cotizar en casi todo el universo (solo la semifinal de Libertadores tiene lineas verificables 8.5 corners y 5.5 tarjetas); "
            "donde no hay cuota no se opera el mercado."
        ),
        "universe_matches": [universe_line(i, r) for i, r in enumerate(records, 1)],
        "picks_details": picks_details,
        "data_limited_reasons": data_limited_reasons,
        "fallback_source": (
            "MCPs no operativos. Investigacion web del agente: statz.ai, xg-edge.com, footystats.org, futbor.com, makeyourstats.com, "
            "clubelo.com (Elo), dailysportpick.com/sportytrader/fox/betfred (cuotas). "
            "Motor calc_engine.py model-v1.3 con calibracion Platt (mercados 1, 2, O/U 2.5 y O/U 3.5). "
            "Partidos sin xG verificable no se ejecutaron en el motor."
        ),
    }
    with open(os.path.join(BASE, "meta_15oct.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print("results_15oct.json y meta_15oct.json escritos")
    print(f"universo: {len(all_results)} | candidatos con value: {len(all_candidates)} | seleccionados: {len(selected)}")
    for s in selected:
        print(f"  - {s['match']} | {s['market']} | cuota {s['odds']} | p {s['model_prob']:.3f} | robEV {s['robust_ev_percent']:+.2f}% | {s.get('selection_profile')}")


if __name__ == "__main__":
    main()
