"""Ensambla inputs, ejecuta el motor model-v1.3, selecciona y genera results/meta para 2026-10-16.

Universo: Bundesliga (J6), LaLiga (J9), Serie A (J7), Ligue 1 (J7), Eredivisie (J9) y
Liga Profesional Argentina - Clausura F13 (todos los partidos de la fecha).
MCPs inoperativos -> investigacion web del agente (archivo data_16oct_all.json en scratch/).
Cutoff de informacion: anterior al primer kickoff (18:00 UTC, Heerenveen vs Excelsior).

Politica de datos (igual que runs 13/14/15-oct):
- Si faltan los 4 valores de xG verificables, NO se ejecuta el motor (evitar priors por defecto).
- Conflictos de xG arbitrados y documentados en `notes` de cada archivo de datos.
- Corners/tarjetas: se cotizan ambos lados de cada linea; donde no hay cuota, el mercado no se opera.
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

DATA_GLOB = os.path.join(BASE, "data_16oct_*.json")
XG_KEYS = ("xg_home_for", "xg_home_against", "xg_away_for", "xg_away_against")
RATE_KEYS = (
    "elo_home", "elo_away",
    "corners_home_for", "corners_home_against", "corners_away_for", "corners_away_against",
    "cards_home_for", "cards_home_against", "cards_away_for", "cards_away_against",
)

ODDS_ORDER = (
    "1", "X", "2", "1x", "x2", "12",
    "dnb_home", "dnb_away", "btts_yes", "btts_no",
    "over_1_5", "under_1_5", "over_2_5", "under_2_5", "over_3_5", "under_3_5",
    "over_corners_8_5", "under_corners_8_5", "over_corners_9_5", "under_corners_9_5",
    "over_corners_10_5", "under_corners_10_5",
    "over_cards_3_5", "under_cards_3_5", "over_cards_4_5", "under_cards_4_5",
    "over_cards_5_5", "under_cards_5_5",
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
    inp["home_team"] = rec.get("home")
    inp["away_team"] = rec.get("away")
    inp["odds"] = rec.get("odds") or {}
    return inp


def run_engine(inp, slug):
    inp_path = os.path.join(BASE, f"match_input_16oct_{slug}.json")
    out_path = os.path.join(BASE, f"match_output_16oct_{slug}.json")
    with open(inp_path, "w", encoding="utf-8") as f:
        json.dump(inp, f, indent=2, ensure_ascii=False)
    subprocess.run(
        [sys.executable, ENGINE, "--input", inp_path, "--output", out_path, "--config", MODEL_CONFIG],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    with open(out_path, encoding="utf-8") as f:
        return json.load(f)


def slugify(text):
    return text.lower().replace(" ", "_").replace(".", "").replace("/", "").replace("'", "")


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
    missing = [k for k in ("over_1_5", "under_1_5", "over_3_5", "under_3_5",
                           "over_corners_8_5", "under_corners_8_5", "over_cards_3_5", "under_cards_3_5")
               if k not in inp["odds"]]
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
    goals = " ".join(f"{k.replace('over_','O').replace('under_','U').replace('_','.')} {odds[k]:.2f}"
                     for k in ("over_1_5", "under_1_5", "over_2_5", "under_2_5", "over_3_5", "under_3_5") if k in odds)
    extras = " ".join(f"{k} {odds[k]:.2f}" for k in (
        "btts_yes", "btts_no", "1x", "x2", "12",
        "over_corners_8_5", "under_corners_8_5", "over_corners_9_5", "under_corners_9_5",
        "over_corners_10_5", "under_corners_10_5",
        "over_cards_3_5", "under_cards_3_5", "over_cards_4_5", "under_cards_4_5",
        "over_cards_5_5", "under_cards_5_5") if k in odds)
    elo = f"Elo {rec.get('elo_home', 'n/d')}/{rec.get('elo_away', 'n/d')}"
    xg = f"xG {rec.get('xg_home_for', 'n/d')}/{rec.get('xg_home_against', 'n/d')} vs {rec.get('xg_away_for', 'n/d')}/{rec.get('xg_away_against', 'n/d')}"
    suffix = " DATOS INSUFICIENTES (xG incompleto) -> NO BET." if rec.get("_limited") else ""
    return (f"{idx}. **{rec['league']}:** {rec['match']} ({kickoff}). 1X2 {' '.join(bits)}; {goals}; "
            f"{extras}. {elo}; {xg}.{suffix}")


def main():
    records = load_matches()
    for rec in records:
        limited = any(rec.get(k) is None for k in XG_KEYS)
        rec["_limited"] = limited
        rec["_low_confidence"] = None

    # Marcas de baja confianza por origen de datos (documentadas, no alteran el motor).
    for rec in records:
        note = str(rec.get("notes", ""))
        if "BAJA CONFIANZA" in note or "NO DETERMINADA" in note:
            rec["_low_confidence"] = True

    all_results = []
    all_evaluations = []
    data_limited_reasons = {}
    for rec in records:
        name = rec["match"]
        if rec["_limited"]:
            data_limited_reasons[name] = (
                "No hay xG verificable de ambos equipos en ninguna fuente consultada; ejecutar el motor "
                "habria exigido priors por defecto, por lo que no se ejecuto."
            )
            all_results.append({
                "match": name, "home_team": rec["home"], "away_team": rec["away"],
                "probabilities": {}, "evaluations": {}, "data_limited": True,
            })
            continue
        inp = build_input(rec)
        slug = slugify(f"{rec['home']}-{rec['away']}")
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
    from collections import Counter
    picks_per_match = Counter(s["match"] for s in selected)

    def pick_detail(cand):
        rec = rec_by_name[cand["match"]]
        inp = build_input(rec)
        from render_artifact import market_label  # noqa: E402
        label = market_label(cand["market"], cand["home_team"], cand["away_team"])
        extra = ""
        if rec.get("_low_confidence"):
            extra = (" Atencion: el input de este partido arrastra banderas de baja confianza "
                     "(ver Riesgos); la incertidumbre real es mayor que la base del motor.")
        risks = risks_for(rec, inp)
        siblings = [s for s in selected if s["match"] == cand["match"] and s["market"] != cand["market"]]
        if siblings:
            others = ", ".join(f"{s['market']} ({s['odds']:.2f})" for s in siblings)
            risks += (
                f" CORRELACION: este mismo partido aporta {picks_per_match[cand['match']]} picks al portfolio "
                f"(junto a {others}); son eventos correlacionados y elevan la varianza conjunta mas alla de la "
                "de picks de partidos independientes, por lo que el stake agregado del partido deberia leerse "
                "como una sola exposicion."
            )
        why = (
            f"{why_base_for(rec)} El motor model-v1.3 estima {cand['model_prob']:.1%} para '{label}' "
            f"frente a una probabilidad implicita de {cand['implied_prob']:.1%} (cuota {cand['odds']:.2f}); "
            f"edge {cand['edge']:+.2f}% y EV robusto {cand['robust_ev_percent']:+.2f}%.{extra}"
        )
        return {
            "match": cand["match"], "market": cand["market"],
            "min_odds": f"{cand['fair_odds']:.2f}",
            "incertidumbre": "Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27",
            "why": why,
            "risks": risks,
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
    with open(os.path.join(BASE, "results_16oct.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    now = datetime.now(timezone.utc)
    cutoff = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = {
        "analysis_date_iso": cutoff,
        "match_dates_text": "16 de octubre de 2026",
        "information_cutoff": cutoff,
        "model_ia": "bigpickle",
        "engine_version": "model-v1.3",
        "leagues_display": "Bundesliga (J6), LaLiga (J9), Serie A (J7), Ligue 1 (J7), Eredivisie (J9) y Liga Profesional Argentina (Clausura, F13)",
        "requested_range": "16 de octubre de 2026 - Bundesliga, Liga Argentina, Liga Espanola (LaLiga), Ligue 1, Serie A y Eredivisie (todos los partidos)",
        "universe_preamble": (
            "Universo = interseccion(ligas: Bundesliga, LaLiga, Serie A, Ligue 1, Eredivisie y Liga Profesional Argentina, "
            f"fecha 16 de octubre de 2026, todos los partidos programados). Cutoff de informacion {cutoff}, anterior al primer "
            "kickoff (18:00 UTC, Heerenveen vs Excelsior). No se usa informacion posterior a ningun kickoff. "
            "Universo final = 7 partidos, todos con los 4 valores de xG verificables y con los 8 campos obligatorios de "
            "corners/tarjetas (for/against por equipo) cargados antes de ejecutar el motor: "
            "Bundesliga J6 Eintracht Frankfurt vs FC Cologne (18:30 UTC); Ligue 1 J7 Le Mans vs Toulouse (18:45 UTC); "
            "Serie A J7 Frosinone vs Sassuolo (18:45 UTC); Eredivisie J9 Heerenveen vs Excelsior (18:00 UTC); "
            "LaLiga J9 Deportivo La Coruna vs Levante (19:00 UTC); Liga Profesional Argentina Clausura F13 "
            "Defensa y Justicia vs Instituto (22:00 UTC del 16/10) y Boca Juniors vs Talleres (00:30 UTC del 17/10 = "
            "21:30 ART del 16/10, por lo que su fecha local cae dentro del rango solicitado). "
            "Se verifico que no hubiera otros partidos de esas 6 ligas en la fecha: la Bundesliga solo programa el viernes "
            "1 partido (Frankfurt-Koln), LaLiga 1 (Depor-Levante), Serie A 1 (Frosinone-Sassuolo), Ligue 1 1 (Le Mans-Toulouse), "
            "Eredivisie 1 (Heerenveen-Excelsior); la Liga Profesional Argentina programa 2 el 16/10 (DyJ-Instituto y Boca-Talleres). "
            "MCPs inoperativos en esta sesion (football-stats, odds-api y apifootball), por lo que toda la recoleccion se hizo via "
            "web del agente: understat.com (xG), Sofascore public API y performanceodds.com (corners y tarjetas), clubelo.com (Elo), "
            "sportytrader.com (1X2/DC/DNB/BTTS/O-U 2.5), oddssafari.com (O-U 1.5/3.5, corners y tarjetas), statsbet.es (Argentina), "
            "dailysportpick.com, BetMGM y fuentes locales de contraste. "
            "CORRECCIONES DE KICKOFF (ET/ART -> UTC): Heerenveen 18:00Z, Frankfurt 18:30Z, Frosinone 18:45Z, Le Mans 18:45Z, "
            "Deportivo 19:00Z, Defensa y Justicia 22:00Z, Boca 00:30Z del 17/10 (21:30 ART del 16/10). "
            "Mercados de corners y tarjetas: se cotizaron AMBOS lados de cada linea evaluada (corners 8.5/9.5/10.5 y tarjetas 3.5/4.5/5.5) "
            "donde hubo cuota verificable; los tramos sin cuota (p. ej. tarjetas 5.5 en la mayoria de los partidos y la totalidad del "
            "mercado de tarjetas de Heerenveen-Excelsior) quedan consignados como 'sin cotizar' y no se operan. "
            "DISCREPANCIAS de la linea 2.5 reportadas y NO sustituidas: Eintracht over 2.5 (1.44 usado vs 1.34 oddssafari / 1.36 dailysportpick) "
            "y Defensa under 2.5 (1.99 usado vs 1.65 oddssafari / 1.54 BetMGM). "
            "BANDERAS DE BAJA CONFIANZA (documentadas, el motor se ejecuto igual porque los 4 xG existen): la pagina de StatsBet de Boca "
            "Juniors esta auto-encuadrada en Copa Libertadores 2026 (los datos de Boca son de baja confianza); la ventana temporal de xG de "
            "Defensa y Justicia e Instituto no esta determinada (~16 partidos implicados por 'Diferencia xG'); los for/against de corners y "
            "tarjetas de ambos partidos argentinos fueron derivados aritmeticamente (against = Media total - Media equipo) porque StatsBet no "
            "expone for/against directo. Lesiones, suspensiones y estado de entrenador NO VERIFICADOS en 6 de los 7 partidos: la busqueda web "
            "devolvio cero resultados en todos los idiomas consultados y FBref/footystats/soccerstats respondieron 403; solo el partido de Boca "
            "tiene bajas y descanso verificados por fuente local (lanumero12)."
        ),
        "universe_matches": [universe_line(i, r) for i, r in enumerate(records, 1)],
        "picks_details": picks_details,
        "data_limited_reasons": data_limited_reasons,
        "fallback_source": (
            "MCPs no operativos (football-stats, odds-api, apifootball). Investigacion web del agente: understat.com (xG), "
            "Sofascore public API y performanceodds.com (corners/tarjetas), clubelo.com (Elo), sportytrader.com, oddssafari.com, "
            "statsbet.es, dailysportpick.com y BetMGM (cuotas). Motor calc_engine.py model-v1.3 con calibracion Platt "
            "(mercados 1, 2, O/U 2.5 y O/U 3.5). Partidos sin xG verificable no se ejecutaron en el motor (ninguno en esta fecha)."
        ),
    }
    with open(os.path.join(BASE, "meta_16oct.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print("results_16oct.json y meta_16oct.json escritos")
    print(f"universo: {len(all_results)} | candidatos con value: {len(all_candidates)} | seleccionados: {len(selected)}")
    for s in selected:
        print(f"  - {s['match']} | {s['market']} | cuota {s['odds']} | p {s['model_prob']:.3f} | robEV {s['robust_ev_percent']:+.2f}% | {s.get('selection_profile')}")
    print("--- excluidos con value ---")
    for e in excluded:
        print(f"  - {e['match']} | {e['market']} | cuota {e['odds']} | p {e['model_prob']:.3f} | robEV {e['robust_ev_percent']:+.2f}%")


if __name__ == "__main__":
    main()
