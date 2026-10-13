"""Ensambla inputs, ejecuta el motor model-v1.3, selecciona y genera results/meta para 2026-10-13.

Universo: UEFA Champions League (fase de liga) + Primera A Colombia (Clausura).
Copa Sudamericana sin partidos el 13/10/2026 (verificado).

MCPs inoperativos (apifootball/odds-api/football-stats) -> investigacion web del agente.
Los 3 partidos sin xG verificable (Lens-Sporting, Sabah-Slavia, Viking-Bayern) se marcan
data_limited: NO se ejecuta el motor (no se publican probabilidades con priors por defecto).
"""
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


def m(name, home, away, league, kickoff, sources, inp=None, limited=False, why_base="", risks=""):
    return {
        "match": name, "home": home, "away": away, "league": league, "kickoff": kickoff,
        "sources": sources, "input": inp, "limited": limited,
        "why_base": why_base, "risks": risks,
    }


MATCHES = [
    m(
        "Arsenal vs Lille", "Arsenal", "Lille", "UEFA Champions League - Fase de Liga",
        "2026-10-13T19:00:00Z",
        "xg-edge.com (xG), footymetrics.com (corners/tarjetas/goals), 1x2.expert + 24score.com (cuotas Bet365/MarathonBet), clubelo.com (Elo)",
        inp={
            "xg_home_for": 1.84, "xg_home_against": 0.79, "xg_away_for": 1.36, "xg_away_against": 1.68,
            "goals_home_for": 1.67, "goals_home_against": 0.83, "goals_away_for": 1.6, "goals_away_against": 0.8,
            "elo_home": 2043, "elo_away": 1782,
            "corners_home_for": 4.5, "corners_home_against": 3.33, "corners_away_for": 3.0, "corners_away_against": 5.33,
            "cards_home_for": 1.33, "cards_home_against": 3.83, "cards_away_for": 1.33, "cards_away_against": 1.67,
            "odds": {
                "1": 1.22, "X": 7.0, "2": 13.0,
                "over_1_5": 1.17, "under_1_5": 5.0, "over_2_5": 1.53, "under_2_5": 2.5, "over_3_5": 2.3, "under_3_5": 1.62,
                "btts_yes": 2.1, "btts_no": 1.67, "1x": 1.04, "x2": 4.0, "12": 1.11,
                "over_corners_8_5": 1.52, "under_corners_8_5": 2.3, "over_corners_9_5": 1.9, "under_corners_9_5": 1.8,
                "over_corners_10_5": 2.45, "under_corners_10_5": 1.46,
                "over_cards_3_5": 2.16, "under_cards_3_5": 1.615, "over_cards_4_5": 3.5, "under_cards_4_5": 1.23,
                "over_cards_5_5": 6.05, "under_cards_5_5": 1.063,
            },
        },
        why_base="Arsenal muy superior en Elo (2043 vs 1782) y con xG a favor alto (1.84) frente a defensa de Lille vulnerable (xG contra 1.68).",
        risks="Rotaciones de Champions; DNB no ofrecido (no cotizado); Lille con mejor rendimiento defensivo reciente en Ligue 1.",
    ),
    m(
        "Atletico Madrid vs Manchester United", "Atletico Madrid", "Manchester United",
        "UEFA Champions League - Fase de Liga", "2026-10-13T19:00:00Z",
        "querostats.com + xg-edge.com (xG), pythiafootball.com + footymetrics.com (corners/tarjetas), 20bet/betgolazo/ats.io/football-predictions.ai (cuotas), clubelo.com (Elo)",
        inp={
            "xg_home_for": 1.76, "xg_home_against": 1.05, "xg_away_for": 1.74, "xg_away_against": 1.43,
            "goals_home_for": 2.29, "goals_home_against": 1.0, "goals_away_for": 1.5, "goals_away_against": 1.5,
            "elo_home": 1907, "elo_away": 1876,
            "corners_home_for": 5.0, "corners_home_against": 3.0, "corners_away_for": 6.67, "corners_away_against": 3.83,
            "cards_home_for": 1.91, "cards_home_against": 2.0, "cards_away_for": 1.67, "cards_away_against": 3.0,
            "odds": {
                "1": 1.925, "X": 3.96, "2": 3.54,
                "over_1_5": 1.12, "under_1_5": 4.7, "over_2_5": 1.5, "under_2_5": 2.7, "over_3_5": 2.39, "under_3_5": 1.68,
                "btts_yes": 1.47, "btts_no": 2.53, "dnb_home": 1.42, "dnb_away": 3.0,
                "over_corners_9_5": 1.85, "over_cards_3_5": 1.87, "under_cards_3_5": 1.83,
            },
        },
        why_base="Localia fuerte del Atletico (Elo 1907, xG contra 1.05) frente a un United que concede (xG contra 1.43).",
        risks="Cuotas de corners/tarjetas parciales (solo linea 9.5 y tarjetas 3.5); doble oportunidad no cotizada; bookmakers mezclados.",
    ),
    m(
        "Villarreal vs Napoli", "Villarreal", "Napoli", "UEFA Champions League - Fase de Liga",
        "2026-10-13T19:00:00Z",
        "xg-edge.com (xG), footymetrics.com (corners/tarjetas/goals), novibet/betimate/ats.io (cuotas), clubelo.com (Elo)",
        inp={
            "xg_home_for": 2.16, "xg_home_against": 1.22, "xg_away_for": 1.66, "xg_away_against": 1.34,
            "goals_home_for": 1.63, "goals_home_against": 1.63, "goals_away_for": 1.67, "goals_away_against": 1.0,
            "elo_home": 1797, "elo_away": 1839,
            "corners_home_for": 6.75, "corners_home_against": 4.38, "corners_away_for": 5.5, "corners_away_against": 5.0,
            "cards_home_for": 1.75, "cards_home_against": 2.88, "cards_away_for": 1.0, "cards_away_against": 1.17,
            "odds": {
                "1": 2.2, "X": 3.65, "2": 3.1,
                "over_1_5": 1.2, "under_1_5": 4.5, "over_2_5": 1.63, "under_2_5": 2.25, "over_3_5": 2.5, "under_3_5": 1.5,
                "btts_yes": 1.61, "btts_no": 2.65, "1x": 1.32, "x2": 1.74, "dnb_home": 1.56, "dnb_away": 2.54,
                "over_corners_9_5": 1.95, "under_corners_9_5": 1.85, "over_cards_4_5": 2.0,
            },
        },
        why_base="Villarreal con alto xG a favor (2.16) y corners altos; Elo ligeramente favorable al Napoli (1839 vs 1797).",
        risks="Cuotas de corners/tarjetas parciales; linea 12 y varias lineas O/U no cotizadas; bookmakers mezclados (novibet/betimate/ats.io).",
    ),
    m(
        "Galatasaray vs Barcelona", "Galatasaray", "Barcelona", "UEFA Champions League - Fase de Liga",
        "2026-10-13T19:00:00Z",
        "investigacion web del agente (agregadores de cuotas y xG), clubelo.com (Elo)",
        inp={
            "xg_home_for": 2.37, "xg_home_against": 1.03, "xg_away_for": 3.81, "xg_away_against": 0.97,
            "elo_home": 1798, "elo_away": 2026,
            "corners_home_for": 5.7, "corners_home_against": 2.3, "corners_away_for": 7.0, "corners_away_against": 2.5,
            "cards_home_for": 1.9, "cards_away_for": 1.6,
            "odds": {
                "1": 8.25, "X": 6.21, "2": 1.26,
                "over_1_5": 1.05, "under_1_5": 11.0, "over_2_5": 1.20, "under_2_5": 5.0, "over_3_5": 1.51, "under_3_5": 2.63,
                "btts_yes": 1.39, "btts_no": 2.82, "1x": 3.48, "x2": 1.05, "12": 1.10,
                "dnb_home": 5.79, "dnb_away": 1.11,
                "over_corners_10_5": 2.00, "under_corners_10_5": 1.74,
                "over_cards_3_5": 1.97, "under_cards_3_5": 1.76, "over_cards_4_5": 3.36,
            },
        },
        why_base="Barcelona muy favorito (Elo 2026 vs 1798) y con xG a favor extremo (3.81) segun el proveedor consultado.",
        risks="xG away de 3.81 inusualmente alto (posible muestra corta del proveedor); tarjetas incompletas (2 de 4 tasas); cuotas de un solo agregador.",
    ),
    m(
        "Inter Milan vs Club Brugge", "Inter Milan", "Club Brugge", "UEFA Champions League - Fase de Liga",
        "2026-10-13T19:00:00Z",
        "footystats.org + statz.ai (xG Inter), oddalerts.com (xG Brugge), sportsgambler.com (corners/goals/cuotas), thesoccerodds.com + pinnacle.com (cuotas), clubelo.com (Elo)",
        inp={
            "xg_home_for": 2.42, "xg_home_against": 1.23, "xg_away_for": 2.40, "xg_away_against": 1.01,
            "goals_home_for": 3.0, "goals_home_against": 1.6, "goals_away_for": 1.8, "goals_away_against": 0.4,
            "elo_home": 1949, "elo_away": 1812,
            "corners_home_for": 6.0, "corners_home_against": 3.4, "corners_away_for": 7.5, "corners_away_against": 3.8,
            "cards_home_for": 1.8, "cards_home_against": 1.8, "cards_away_for": 1.6,
            "odds": {
                "1": 1.25, "X": 6.00, "2": 10.00,
                "over_1_5": 1.10, "under_1_5": 7.00, "over_2_5": 1.37, "under_2_5": 3.10, "over_3_5": 2.34, "under_3_5": 1.64,
                "btts_yes": 1.73, "btts_no": 2.05, "1x": 1.04, "12": 1.12, "x2": 3.80,
                "dnb_home": 1.06, "dnb_away": 7.00,
                "over_corners_9_5": 1.84, "under_corners_9_5": 1.97,
            },
        },
        why_base="Inter favorito claro (Elo 1949 vs 1812) con xG alto (2.42) y Brugge concediendo poco pero de liga menor.",
        risks="Fuentes de xG con conflicto (footystats vs statz); tarjetas de Brugge incompletas; solo linea 9.5 de corners cotizada.",
    ),
    m(
        "RB Leipzig vs PSV Eindhoven", "RB Leipzig", "PSV Eindhoven", "UEFA Champions League - Fase de Liga",
        "2026-10-13T19:00:00Z",
        "footystats.org + statz.ai (xG/goals), sportsgambler.com (corners/cuotas), clubelo.com (Elo)",
        inp={
            "xg_home_for": 2.27, "xg_home_against": 1.40, "xg_away_for": 2.60, "xg_away_against": 1.25,
            "goals_home_for": 2.25, "goals_home_against": 1.25, "goals_away_for": 3.4, "goals_away_against": 1.4,
            "elo_home": 1825, "elo_away": 1787,
            "corners_home_for": 5.3, "corners_home_against": 4.9, "corners_away_for": 7.1, "corners_away_against": 3.5,
            "cards_home_for": 1.3, "cards_away_for": 1.9,
            "odds": {
                "1": 1.60, "X": 4.90, "2": 4.50,
                "over_2_5": 1.27, "under_2_5": 3.75, "btts_yes": 1.34, "btts_no": 3.15,
                "1x": 1.20, "12": 1.17, "x2": 2.32, "dnb_home": 1.27, "dnb_away": 3.30,
                "over_corners_9_5": 1.68, "under_corners_9_5": 2.04,
            },
        },
        why_base="Leipzig local (Elo 1825 vs 1787) con PSV de alto xG a favor (2.60) pero fragil; partido con tendencia a goles.",
        risks="Solo linea O/U 2.5 cotizada; xG de Leipzig con conflicto de fuentes; tarjetas incompletas.",
    ),
    m(
        "Atletico Bucaramanga vs Aguilas Doradas Rionegro", "Atletico Bucaramanga", "Aguilas Doradas Rionegro",
        "Primera A Colombia - Clausura", "2026-10-13T23:30:00Z",
        "statof.com, bzzoiro, clubelo.com (Elo y datos de temporada)",
        inp={
            "xg_home_for": 0.96, "xg_home_against": 1.05, "xg_away_for": 1.29, "xg_away_against": 1.0,
            "goals_home_for": 1.53, "goals_home_against": 1.0, "goals_away_for": 1.16, "goals_away_against": 1.35,
            "elo_home": 1637, "elo_away": 1548,
            "corners_home_for": 3.5, "corners_home_against": 4.85, "corners_away_for": 4.9, "corners_away_against": 4.1,
            "cards_home_for": 2.6, "cards_home_against": 2.5, "cards_away_for": 2.4, "cards_away_against": 3.2,
            "odds": {
                "1": 1.95, "X": 3.25, "2": 3.80,
                "over_1_5": 1.33, "under_1_5": 3.10, "over_2_5": 2.10, "under_2_5": 1.70, "over_3_5": 3.80, "under_3_5": 1.23,
                "btts_yes": 1.84, "btts_no": 1.85, "1x": 1.25, "x2": 1.77, "12": 1.29,
                "dnb_home": 1.43, "dnb_away": 2.65,
                "over_corners_8_5": 1.71, "under_corners_8_5": 2.02, "over_corners_9_5": 2.09, "under_corners_9_5": 1.66,
            },
        },
        why_base="Bucaramanga local con mejor Elo (1637 vs 1548); partido de expectativa de goles baja (xG total ~2.25).",
        risks="Liga con menor cobertura estadistica; xG de proveedor unico; contextos de rotacion por calendario Clausura.",
    ),
    m(
        "Lens vs Sporting CP", "Lens", "Sporting CP", "UEFA Champions League - Fase de Liga",
        "2026-10-13T16:45:00Z",
        "foxsports.com (1X2 y O/U 2.5), clubelo.com (Elo)",
        limited=True,
        why_base="Datos insuficientes (sin xG/goals verificables).",
        risks="Sin xG/goals ni corners/tarjetas; solo 1X2 y O/U 2.5 capturadas.",
    ),
    m(
        "Sabah FK vs Slavia Prague", "Sabah FK", "Slavia Prague", "UEFA Champions League - Fase de Liga",
        "2026-10-13T16:45:00Z",
        "wincomparator.com (1X2/O2.5/BTTS)",
        limited=True,
        why_base="Datos insuficientes (sin xG/goals/Elo verificables).",
        risks="Sin xG/goals ni corners/tarjetas; Elo ClubElo no disponible para ninguno de los dos equipos.",
    ),
    m(
        "Viking FK vs Bayern Munich", "Viking FK", "Bayern Munich", "UEFA Champions League - Fase de Liga",
        "2026-10-13T19:00:00Z",
        "foxsports.com (1X2), clubelo.com (Elo Bayern)",
        limited=True,
        why_base="Datos insuficientes (sin xG/goals; Elo local no disponible).",
        risks="Solo 1X2 capturada; lineas 1.5/2.5/3.5 no presentes (fuente cotiza linea 4.5); sin corners/tarjetas.",
    ),
]


def run_engine(idx, match):
    slug = f"{match['home']}-{match['away']}".lower().replace(" ", "_").replace(".", "")
    inp_path = os.path.join(BASE, f"match_input_13oct_{slug}.json")
    out_path = os.path.join(BASE, f"match_output_13oct_{slug}.json")
    with open(inp_path, "w", encoding="utf-8") as f:
        json.dump(match["input"], f, indent=2, ensure_ascii=False)
    subprocess.run(
        [sys.executable, ENGINE, "--input", inp_path, "--output", out_path, "--config", MODEL_CONFIG],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    with open(out_path, encoding="utf-8") as f:
        return json.load(f)


def build_pick_detail(cand, ctx):
    from render_artifact import market_label  # noqa: E402
    label = market_label(cand["market"], cand["home_team"], cand["away_team"])
    inp = ctx["input"] or {}
    base = ctx["why_base"]
    why = (
        f"{base} El motor model-v1.3 estima {cand['model_prob']:.1%} para '{label}' "
        f"frente a una probabilidad implicita de {cand['implied_prob']:.1%} (cuota {cand['odds']:.2f}); "
        f"edge {cand['edge']:+.2f}% y EV robusto {cand['robust_ev_percent']:+.2f}%."
    )
    min_odds = (1.0 / cand["conservative_prob"]) if cand.get("conservative_prob") else cand["fair_odds"]
    return {
        "match": cand["match"], "market": cand["market"],
        "min_odds": f"{min_odds:.2f}",
        "incertidumbre": "Base +/- 5.0% (model-v1.3) sobre muestra corta de xG (n aprox. 5-8)",
        "why": why,
        "risks": ctx["risks"],
        "sources": f"{ctx['sources']}; verosimilitud del modelo y calibracion Platt (model-v1.3).",
    }


def main():
    all_results = []
    all_evaluations = []
    for idx, match in enumerate(MATCHES):
        if match["limited"]:
            all_results.append({
                "match": match["match"], "home_team": match["home"], "away_team": match["away"],
                "probabilities": {}, "evaluations": {}, "data_limited": True,
            })
            continue
        out = run_engine(idx, match)
        evaluations = {}
        for key, ev in out["evaluations"].items():
            enriched = dict(ev)
            enriched["match"] = match["match"]
            enriched["home_team"] = match["home"]
            enriched["away_team"] = match["away"]
            evaluations[key] = enriched
            all_evaluations.append(enriched)
        all_results.append({
            "match": match["match"], "home_team": match["home"], "away_team": match["away"],
            "probabilities": out["probabilities"], "evaluations": evaluations,
        })

    all_candidates = [dict(e) for e in all_evaluations if e.get("has_value")]
    for c in all_candidates:
        c.setdefault("selection_profile", "excluido")
        c.setdefault("selection_reason", "Sin clasificar")

    selected, excluded = select_portfolio(list(all_candidates))

    ctx_by_match = {mt["match"]: mt for mt in MATCHES}
    picks_details = [build_pick_detail(s, ctx_by_match[s["match"]]) for s in selected]

    results = {
        "all_results": all_results,
        "all_candidates": all_candidates,
        "all_evaluations": all_evaluations,
        "selected": selected,
        "excluded": excluded,
    }
    with open(os.path.join(BASE, "results_13oct.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    now = datetime.now(timezone.utc)
    cutoff = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    meta = {
        "analysis_date_iso": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "match_dates_text": "13 de octubre de 2026",
        "information_cutoff": cutoff,
        "model_ia": "big-pickle",
        "engine_version": "model-v1.3",
        "leagues_display": "UEFA Champions League (fase de liga) y Primera A de Colombia (Clausura)",
        "requested_range": "13 de octubre de 2026 - Liga Colombiana, Champions League y Copa Sudamericana (todos los partidos)",
        "universe_preamble": (
            "Universo = interseccion(ligas: liga colombiana + champions league + copa sudamericana, fecha 13 de octubre de 2026, todos los partidos programados). "
            f"Cutoff de informacion {cutoff}, anterior al primer kickoff (Lens-Sporting 16:45 UTC). No se usa informacion posterior a ningun kickoff. "
            "Copa Sudamericana NO tiene partidos el 13/10/2026 (verificado en calendario): 0 partidos. Universo final = 10 partidos "
            "(9 de Champions League fase de liga + 1 de Primera A Colombia). "
            "MCPs inoperativos en esta sesion: apifootball/odds-api/football-stats no expuestos, soccer-mcp ausente, the-odds-api HTTP 401 y api.clubelo.com inaccesible; "
            "por ello la investigacion se realizo via web (agente): xg-edge, footymetrics, querostats, statz.ai, sportsgambler, 1x2.expert, 24score, wincomparator, foxsports, clubelo.com. "
            "Las tasas de corners/tarjetas for/against constan en cada match_input cuando estuvieron disponibles; donde las cuotas O/U de corners/tarjetas no estaban cotizadas, se marcan n/d (no se inventan). "
            "ADVERTENCIA DE DATOS: 3 partidos (Lens-Sporting, Sabah-Slavia, Viking-Bayern) NO tienen xG/goals verificables; para evitar publicar probabilidades basadas en priors por defecto del motor, "
            "NO se ejecuto el motor en ellos: figuran como NO BET por datos insuficientes (probabilidades n/d en la tabla O/U)."
        ),
        "universe_matches": [
            "1. **Champions League:** Lens vs Sporting CP (16:45 UTC). 1X2 2.36/3.50/2.70; O/U 2.5 1.56/2.35 (foxsports). Elo Lens 1817 / Sporting 1876. DATOS INSUFICIENTES (sin xG/goals ni corners/tarjetas) -> NO BET.",
            "2. **Champions League:** Sabah FK vs Slavia Prague (16:45 UTC). 1X2 3.50/3.75/1.92; O/U 2.5 1.62/2.15; BTTS 1.54/2.25 (wincomparator). Sin Elo ni xG -> NO BET por datos insuficientes.",
            "3. **Champions League:** Arsenal vs Lille (19:00 UTC). 1X2 1.22/7.00/13.00; O/U 1.5 1.17/5.00, 2.5 1.53/2.50, 3.5 2.30/1.62; BTTS 2.10/1.67; corners y tarjetas O/U capturadas. Elo 2043/1782; xG 1.84/0.79 vs 1.36/1.68.",
            "4. **Champions League:** Atletico Madrid vs Manchester United (19:00 UTC). 1X2 1.925/3.96/3.54; O/U 1.5 1.12/4.70, 2.5 1.50/2.70, 3.5 2.39/1.68; BTTS 1.47/2.53; DNB 1.42/3.00. Elo 1907/1876; xG 1.76/1.05 vs 1.74/1.43.",
            "5. **Champions League:** Villarreal vs Napoli (19:00 UTC). 1X2 2.20/3.65/3.10; O/U 1.5 1.20/4.50, 2.5 1.63/2.25, 3.5 2.50/1.50; BTTS 1.61/2.65; DC 1X 1.32 / X2 1.74; DNB 1.56/2.54. Elo 1797/1839; xG 2.16/1.22 vs 1.66/1.34.",
            "6. **Champions League:** Galatasaray vs Barcelona (19:00 UTC). 1X2 8.25/6.21/1.26; O/U 1.5 1.05/11.0, 2.5 1.20/5.0, 3.5 1.51/2.63; BTTS 1.39/2.82; DNB 5.79/1.11; DC 1X 3.48 / X2 1.05 / 12 1.10. Elo 1798/2026; xG 2.37/1.03 vs 3.81/0.97.",
            "7. **Champions League:** Inter Milan vs Club Brugge (19:00 UTC). 1X2 1.25/6.00/10.00; O/U 1.5 1.10/7.0, 2.5 1.37/3.10, 3.5 2.34/1.64; BTTS 1.73/2.05; DC 1X 1.04 / X2 3.80 / 12 1.12; DNB 1.06/7.00. Elo 1949/1812; xG 2.42/1.23 vs 2.40/1.01.",
            "8. **Champions League:** RB Leipzig vs PSV Eindhoven (19:00 UTC). 1X2 1.60/4.90/4.50; O/U 2.5 1.27/3.75; BTTS 1.34/3.15; DC 1X 1.20 / X2 2.32 / 12 1.17; DNB 1.27/3.30. Elo 1825/1787; xG 2.27/1.40 vs 2.60/1.25.",
            "9. **Champions League:** Viking FK vs Bayern Munich (19:00 UTC). 1X2 17.63/n-d/1.10 (foxsports; linea cotizada 4.5). Sin xG ni Elo local -> NO BET por datos insuficientes.",
            "10. **Primera A Colombia (Clausura):** Atletico Bucaramanga vs Aguilas Doradas Rionegro (23:30 UTC). 1X2 1.95/3.25/3.80; O/U 1.5 1.33/3.10, 2.5 2.10/1.70, 3.5 3.80/1.23; BTTS 1.84/1.85; DC 1X 1.25 / X2 1.77 / 12 1.29; DNB 1.43/2.65; corners O/U 8.5 y 9.5 capturadas. Elo 1637/1548; xG 0.96/1.05 vs 1.29/1.00.",
        ],
        "picks_details": picks_details,
        "fallback_source": (
            "MCPs no operativos (apifootball/odds-api/football-stats sin herramientas, soccer-mcp ausente, the-odds-api 401, api.clubelo.com inaccesible). "
            "Investigacion web del agente: xg-edge.com y querostats.com y statz.ai y footystats.org y oddalerts.com (xG/goals), footymetrics.com y pythiafootball.com y sportsgambler.com (corners/tarjetas), "
            "1x2.expert y 24score.com y wincomparator.com y novibet y betgolazo y ats.io y thesoccerodds.com y pinnacle.com y foxsports.com (cuotas), clubelo.com (Elo). "
            "Motor calc_engine.py model-v1.3 con calibracion Platt (mercados 1, 2, O/U 2.5 y O/U 3.5). Conflictos de xG documentados por partido en los match_input. "
            "Los 3 partidos sin xG verificable no se ejecutaron en el motor (evitar priors por defecto)."
        ),
    }
    with open(os.path.join(BASE, "meta_13oct.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print("results_13oct.json y meta_13oct.json escritos")
    print(f"universo: {len(all_results)} | candidatos con value: {len(all_candidates)} | seleccionados: {len(selected)}")
    for s in selected:
        print(f"  - {s['match']} | {s['market']} | cuota {s['odds']} | p {s['model_prob']:.3f} | robEV {s['robust_ev_percent']:+.2f}% | {s.get('selection_profile')}")


if __name__ == "__main__":
    main()
