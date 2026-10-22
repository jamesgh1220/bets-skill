"""Ensambla inputs, ejecuta el motor model-v1.3, selecciona y genera results/meta para 2026-10-20.

Universo:
- Liga BetPlay Dimayor (Finalización 2026, fecha 15 y fecha 13 aplazada): 4 partidos
- Copa Sudamericana 2026 (semifinal, vuelta): 1 partido
- UEFA Champions League 2026-27 (League phase MD3): 9 partidos
Total = 14 partidos.
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

from selection import select_portfolio  # noqa: E402
from render_artifact import market_label  # noqa: E402

MODEL_CONFIG = os.path.join(ROOT, "models", "model-v1.3.json")
ENGINE = os.path.join(ROOT, "scripts", "calc_engine.py")

XG_KEYS = ("xg_home_for", "xg_home_against", "xg_away_for", "xg_away_against")
RATE_KEYS = (
    "elo_home", "elo_away",
    "corners_home_for", "corners_home_against", "corners_away_for", "corners_away_against",
    "cards_home_for", "cards_home_against", "cards_away_for", "cards_away_against",
)


def load_all_records():
    # 1. Cargar xG fills para UCL
    xg_fills = {}
    with open(os.path.join(BASE, "data_20oct_ucl_xgfill.json"), encoding="utf-8") as f:
        fills_list = json.load(f)
        for fill in fills_list:
            m_name = fill["match"].replace(" SK", "").replace("SK ", "")
            xg_fills[m_name] = fill
            # Map canonical names
            if "Fenerbahçe" in m_name:
                xg_fills["Fenerbahçe vs Slavia Praha"] = fill
            if "Sabah" in m_name:
                xg_fills["Sabah FK vs Borussia Dortmund"] = fill
            if "Liverpool" in m_name:
                xg_fills["Liverpool vs Villarreal"] = fill
            if "Manchester City" in m_name:
                xg_fills["Manchester City vs AEK Athens"] = fill
            if "Paris Saint-Germain" in m_name:
                xg_fills["Paris Saint-Germain vs FC Barcelona"] = fill
            if "FC Porto" in m_name:
                xg_fills["FC Porto vs PSV Eindhoven"] = fill
            if "VfB Stuttgart" in m_name:
                xg_fills["VfB Stuttgart vs Atlético Madrid"] = fill

    # 2. Cargar BetPlay (4 partidos)
    with open(os.path.join(BASE, "data_20oct_betplay.json"), encoding="utf-8") as f:
        bp_list = json.load(f)

    # 3. Cargar Sudamericana (1 partido)
    with open(os.path.join(BASE, "data_20oct_sudamericana.json"), encoding="utf-8") as f:
        cs_list = json.load(f)

    # 4. Cargar UCL A & B (4 + 5 = 9 partidos)
    with open(os.path.join(BASE, "data_20oct_ucl_a.json"), encoding="utf-8") as f:
        ucl_a_list = json.load(f)
    with open(os.path.join(BASE, "data_20oct_ucl_b.json"), encoding="utf-8") as f:
        ucl_b_list = json.load(f)

    # Normalizar campos de todos los records
    records = []
    for raw in bp_list + cs_list + ucl_a_list + ucl_b_list:
        rec = dict(raw)
        m_name = rec.get("match") or f"{rec.get('home')} vs {rec.get('away')}"
        rec["match"] = m_name

        # Normalizar claves xG si vienen como xg_for_home etc.
        if "xg_for_home" in rec:
            rec["xg_home_for"] = rec.pop("xg_for_home")
            rec["xg_home_against"] = rec.pop("xg_against_home")
            rec["xg_away_for"] = rec.pop("xg_for_away")
            rec["xg_away_against"] = rec.pop("xg_against_away")

        # Aplicar xg_fills si aplica y le falta algún xg
        if m_name in xg_fills:
            fill = xg_fills[m_name]
            for k in XG_KEYS:
                if rec.get(k) is None and fill.get(k) is not None:
                    rec[k] = fill[k]

        # Normalizar corners / cards keys
        for prefix in ("corners", "cards"):
            for side, std_side in (("home", "home"), ("away", "away")):
                for direction in ("for", "against"):
                    var1 = f"{prefix}_{direction}_{side}"
                    var2 = f"{prefix}_{side}_{direction}"
                    if var1 in rec and var2 not in rec:
                        rec[var2] = rec.pop(var1)

        # Normalizar cuotas jerárquicas a dict plano
        raw_odds = rec.get("odds", {})
        flat_odds = {}
        for k, v in raw_odds.items():
            if isinstance(v, dict):
                for sk, sv in v.items():
                    if k == "1x2":
                        flat_odds[sk] = sv
                    elif k == "dc":
                        flat_odds[sk] = sv
                    elif k == "dnb":
                        flat_odds[f"dnb_home" if sk in ("1", "home") else f"dnb_away"] = sv
                    elif k == "btts":
                        flat_odds[f"btts_{sk}"] = sv
                    elif k == "ou_goals":
                        flat_odds[sk] = sv
                    elif k == "ou_corners":
                        suffix = sk[5:] if sk.startswith("over_") else sk[6:]
                        prefix_c = "over_corners" if sk.startswith("over_") else "under_corners"
                        flat_odds[f"{prefix_c}_{suffix}"] = sv
                    elif k == "ou_cards":
                        suffix = sk[5:] if sk.startswith("over_") else sk[6:]
                        prefix_c = "over_cards" if sk.startswith("over_") else "under_cards"
                        flat_odds[f"{prefix_c}_{suffix}"] = sv
            else:
                flat_odds[k] = v
        rec["odds"] = flat_odds
        records.append(rec)

    return records


def build_input(rec):
    inp = {}
    for key in XG_KEYS + RATE_KEYS:
        val = rec.get(key)
        if val is None:
            continue
        inp[key] = val
    inp["home_team"] = rec.get("home")
    inp["away_team"] = rec.get("away")
    inp["odds"] = rec.get("odds") or {}
    return inp


def slugify(text):
    return text.lower().replace(" ", "_").replace(".", "").replace("/", "").replace("'", "")


def run_engine(inp, slug):
    inp_path = os.path.join(BASE, f"match_input_20oct_{slug}.json")
    out_path = os.path.join(BASE, f"match_output_20oct_{slug}.json")
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
    return " | ".join(parts) + "." if parts else "Análisis cuantitativo de perfil y ratings."


def risks_for(rec, inp):
    missing = [k for k in ("over_1_5", "under_1_5", "over_3_5", "under_3_5",
                           "over_corners_8_5", "under_corners_8_5", "over_cards_3_5", "under_cards_3_5")
               if k not in inp.get("odds", {})]
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
    xg = (f"xG {rec.get('xg_home_for', 'n/d')}/{rec.get('xg_home_against', 'n/d')} vs "
          f"{rec.get('xg_away_for', 'n/d')}/{rec.get('xg_away_against', 'n/d')}")
    suffix = " DATOS INSUFICIENTES (xG incompleto) -> NO BET." if rec.get("_limited") else ""
    return (f"{idx}. **{rec['league']}:** {rec['match']} ({kickoff}). 1X2 {' '.join(bits)}; {goals}; "
            f"{extras}. {elo}; {xg}.{suffix}")


def main():
    records = load_all_records()
    for rec in records:
        limited = any(rec.get(k) is None for k in XG_KEYS)
        rec["_limited"] = limited
        note = str(rec.get("notes", ""))
        rec["_low_confidence"] = True if ("BAJA CONFIANZA" in note or "NO DETERMINADA" in note) else False

    all_results = []
    all_evaluations = []
    data_limited_reasons = {}

    for rec in records:
        name = rec["match"]
        if rec["_limited"]:
            data_limited_reasons[name] = (
                "No hay xG verificable de ambos equipos en ninguna fuente consultada pre-kickoff; "
                "ejecutar el motor cuantitativo habría exigido priors por defecto, por lo que no se ejecutó."
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
    picks_per_match = Counter(s["match"] for s in selected)

    def pick_detail(cand):
        rec = rec_by_name[cand["match"]]
        inp = build_input(rec)
        label = market_label(cand["market"], cand["home_team"], cand["away_team"])
        extra = ""
        if rec.get("_low_confidence"):
            extra = (" Atención: el input de este partido arrastra banderas de baja confianza "
                     "(ver Riesgos); la incertidumbre real es mayor que la base del motor.")
        risks = risks_for(rec, inp)
        siblings = [s for s in selected if s["match"] == cand["match"] and s["market"] != cand["market"]]
        if siblings:
            others = ", ".join(f"{s['market']} ({s['odds']:.2f})" for s in siblings)
            risks += (
                f" CORRELACIÓN: este mismo partido aporta {picks_per_match[cand['match']]} picks al portfolio "
                f"(junto a {others}); son eventos correlacionados y elevan la varianza conjunta más allá de la "
                "de picks de partidos independientes, por lo que el stake agregado del partido debería leerse "
                "como una sola exposición."
            )
        why = (
            f"{why_base_for(rec)} El motor model-v1.3 estima {cand['model_prob']:.1%} para '{label}' "
            f"frente a una probabilidad implícita de {cand['implied_prob']:.1%} (cuota {cand['odds']:.2f}); "
            f"edge {cand['edge']:+.2f}% y EV robusto {cand['robust_ev_percent']:+.2f}%.{extra}"
        )
        return {
            "match": cand["match"],
            "market": cand["market"],
            "min_odds": f"{cand['fair_odds']:.2f}",
            "incertidumbre": "Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en temporada 26/27",
            "why": why,
            "risks": risks,
            "sources": f"{rec.get('sources', 'web del agente')}; verosimilitud del modelo y calibración Platt (model-v1.3).",
        }

    picks_details = [pick_detail(s) for s in selected]

    results = {
        "all_results": all_results,
        "all_candidates": all_candidates,
        "all_evaluations": all_evaluations,
        "selected": selected,
        "excluded": excluded,
    }
    with open(os.path.join(BASE, "results_20oct.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    now = datetime.now(timezone.utc)
    cutoff = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = {
        "analysis_date_iso": cutoff,
        "match_dates_text": "20 de octubre de 2026",
        "information_cutoff": cutoff,
        "model_ia": "bigpickle",
        "engine_version": "model-v1.3",
        "leagues_display": (
            "Liga BetPlay Dimayor (Finalización 2026, fecha 15 y fecha 13 aplazada), "
            "Copa Sudamericana 2026 (semifinal vuelta) y UEFA Champions League 2026-27 (League phase MD3)"
        ),
        "requested_range": (
            "20 de octubre de 2026 - Liga BetPlay Colombia, Copa Sudamericana y UEFA Champions League (todos los partidos)"
        ),
        "universe_preamble": (
            "Universo = intersección(ligas: Liga BetPlay Dimayor, Copa Sudamericana, UEFA Champions League, "
            f"fecha 20 de octubre de 2026, todos los partidos programados). Cutoff de información {cutoff}, "
            "anterior a los kickoffs. No se usa información posterior a ningún kickoff. Universo total = 14 partidos: "
            "4 de Liga BetPlay Dimayor, 1 de Copa Sudamericana y 9 de UEFA Champions League. "
            "Todos los partidos cuentan con las tasas de corners y tarjetas (for/against) por equipo recolectadas. "
            "Aquellos encuentros con xG incompleto en fuentes públicas pre-kickoff se consignan como DATOS INSUFICIENTES "
            "-> NO BET sin forzar priors del motor. MCPs inoperativos en la sesión, recolección vía investigación web del agente "
            "(oddssafari, statsbet, clubelo, fotmob, foxsports, espn). "
            "Mercados O/U evaluados en ambos lados (goles 1.5/2.5/3.5, corners 8.5/9.5/10.5, tarjetas 3.5/4.5/5.5) donde "
            "hubo cuotas publicadas por casas de apuestas."
        ),
        "universe_matches": [universe_line(i, r) for i, r in enumerate(records, 1)],
        "picks_details": picks_details,
        "data_limited_reasons": data_limited_reasons,
        "fallback_source": (
            "MCPs no operativos (football-stats, odds-api, apifootball). Investigación web del agente: statsbet.es, "
            "oddssafari.com, clubelo.com, fotmob, foxsports y espn. Motor calc_engine.py model-v1.3 con calibración Platt. "
            "Partidos sin xG verificable completo no se ejecutan en el motor cuantitativo."
        ),
    }
    with open(os.path.join(BASE, "meta_20oct.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print("results_20oct.json y meta_20oct.json generados con éxito.")
    print(f"Universo total: {len(all_results)} partidos")
    print(f"Partidos ejecutados en motor: {len([r for r in all_results if not r.get('data_limited')])}")
    print(f"Partidos con datos limitados: {len(data_limited_reasons)}")
    print(f"Candidatos con value: {len(all_candidates)}")
    print(f"Picks seleccionados (top 0-6): {len(selected)}")
    for s in selected:
        print(f"  - {s['match']} | {s['market']} | cuota {s['odds']} | p {s['model_prob']:.3f} | robEV {s['robust_ev_percent']:+.2f}% | {s.get('selection_profile')}")


if __name__ == "__main__":
    main()
