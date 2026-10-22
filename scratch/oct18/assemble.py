#!/usr/bin/env python3
"""Assemble results.json and meta.json for scripts/render_artifact.py (2026-10-18)."""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from selection import select_portfolio  # noqa: E402

NOW_UTC = "2026-10-18T02:35:08+00:00"
MATCH_DATES_TEXT = "18 de octubre de 2026"

results_all = json.load(open(os.path.join(HERE, "all_results.json")))

# Per-match raw inputs (xG/Elo) for informative per-pick sourcing.
INPUTS = {}
for fn in sorted(os.listdir(os.path.join(HERE, "inputs"))):
    d = json.load(open(os.path.join(HERE, "inputs", fn)))
    INPUTS[f"{d['home_team']} vs {d['away_team']}"] = d

LEAGUE_ORDER = ["Premier League", "La Liga", "Serie A", "Bundesliga", "Ligue 1",
                "Eredivisie", "MLS", "Liga Profesional Argentina"]
LEAGUE_LABEL = {
    "Premier League": "Premier League", "La Liga": "La Liga", "Serie A": "Serie A",
    "Bundesliga": "Bundesliga", "Ligue 1": "Ligue 1", "Eredivisie": "Eredivisie",
    "MLS": "MLS", "Liga Profesional Argentina": "Liga Profesional Argentina",
}

all_candidates = []
all_evaluations = []
for r in results_all:
    match = r["match"]
    home, away = r["home_team"], r["away_team"]
    for market, ev in r["evaluations"].items():
        base = {
            "match": match, "market": market, "home_team": home, "away_team": away,
            "odds": ev["odds"], "model_prob": ev["model_prob"],
            "fair_odds": ev["fair_odds"], "edge": ev["edge"],
            "ev_percent": ev["ev_percent"], "robust_ev_percent": ev["robust_ev_percent"],
            "stake_recommended_units": ev["stake_recommended_units"],
            "conservative_prob": ev["conservative_prob"],
            "implied_prob": ev["implied_prob"], "has_value": ev["has_value"],
        }
        all_evaluations.append(base)
        if ev["has_value"]:
            all_candidates.append(dict(base))

selected, excluded = select_portfolio(all_candidates, max_picks=6)

# ------------------------------------------------------------------ metadata
universe_matches = []
for r in sorted(results_all, key=lambda x: x["commence_time"]):
    hhmm = r["commence_time"][11:16]
    universe_matches.append(
        f"- {r['home_team']} vs {r['away_team']} ({LEAGUE_LABEL[r['league']]}) — {hhmm} UTC"
    )

universe_preamble = (
    "Universo: 29 partidos del 2026-10-18 en 8 ligas, delimitados por FECHA LOCAL del "
    "partido (no por marca UTC): los 7 partidos de MLS con kickoff 00:40/02:30 UTC del "
    "2026-10-18 pertenecen al 2026-10-17 en local y quedan fuera; los eventos del "
    "2026-10-19 UTC que son 2026-10-19 en local también quedan fuera. Ligas: Premier "
    "League (4), La Liga (4), Bundesliga (2), Serie A (4), Ligue 1 (5), Eredivisie (5), "
    "Liga Profesional Argentina (4), MLS (1). EXCLUIDA la Liga BetPlay (Colombia): "
    "solicitada en el rango de ligas, no aparece en el proveedor de cuotas ni en ninguna "
    "fuente de datos disponible (The Odds API no la cubre; apifootball con autenticación "
    "fallida); sin fixtures, cuotas ni estadísticas verificables, por lo que no se analiza "
    "ningún partido de esa liga (no se inventan datos). xG real (Understat) en las 5 "
    "grandes ligas; para Eredivisie, MLS y Argentina se usa proxy GF/GA por partido de "
    "Wikipedia ante la ausencia de xG (documentado por partido). Córners/Tarjetas NO "
    "DISPONIBLES en ninguna fuente (apifootball sin autenticación, SofaScore 403, The "
    "Odds API sin esos mercados): consignado explícitamente, nunca omitido en silencio. "
    "El mercado draw_no_bet NO fue capturado en esta corrida (presupuesto de créditos de "
    "The Odds API casi agotado: los endpoints por evento se consultaron con h2h, totals, "
    "alternate_totals, btts y double_chance; DNB quedó fuera), por lo que se evalúan 1X2, "
    "doble oportunidad, BTTS y totales. Cuota = mejor precio disponible entre las casas de "
    "The Odds API al cutoff. ACTUALIDAD: identidad de clubes y pertenencia a torneos 2026 "
    "verificadas contra las tablas de Wikipedia y los rankings ClubElo/Understat vigentes; "
    "la verificación en vivo de lesiones, suspensiones y alineaciones probables NO pudo "
    "completarse (apifootball con autenticación fallida, SofaScore 403), por lo que esa "
    "incertidumbre se asume en el margen base del motor y se declara por pick."
)

LEAGUE_SRC = {
    "Premier League": "Understat EPL 2026 (xG real) + ClubElo + The Odds API",
    "La Liga": "Understat La Liga 2026 (xG real) + ClubElo + The Odds API",
    "Serie A": "Understat Serie A 2026 (xG real) + ClubElo + The Odds API",
    "Bundesliga": "Understat Bundesliga 2026 (xG real) + ClubElo + The Odds API",
    "Ligue 1": "Understat Ligue 1 2026 (xG real) + ClubElo + The Odds API",
    "Eredivisie": "Wikipedia Eredivisie 2026 (proxy GF/GA) + ClubElo + The Odds API",
    "MLS": "Wikipedia MLS 2026 (proxy GF/GA) + ClubElo + The Odds API",
    "Liga Profesional Argentina": "Wikipedia Primera 2026 (proxy GF/GA) + ClubElo + The Odds API",
}
PROXY_LEAGUES = {"Eredivisie", "MLS", "Liga Profesional Argentina"}
ELO_FALLBACK_TEAMS = {"Estudiantes de Río Cuarto"}


def market_phrase(market, home, away, prob):
    if market == "1":
        return f"P(victoria {home})={prob*100:.1f}%"
    if market == "2":
        return f"P(victoria {away})={prob*100:.1f}%"
    if market == "X":
        return f"P(empate)={prob*100:.1f}%"
    if market.startswith("over_"):
        line = market[5:].replace("_", ".")
        return f"P(Over {line} goles)={prob*100:.1f}%"
    if market.startswith("under_"):
        line = market[6:].replace("_", ".")
        return f"P(Under {line} goles)={prob*100:.1f}%"
    if market == "btts_yes":
        return f"P(ambos marcan)={prob*100:.1f}%"
    if market == "btts_no":
        return f"P(no marcan ambos)={prob*100:.1f}%"
    if market == "1x":
        return f"P({home} o empate)={prob*100:.1f}%"
    if market == "x2":
        return f"P(empate o {away})={prob*100:.1f}%"
    if market == "12":
        return f"P({home} o {away})={prob*100:.1f}%"
    if market == "dnb_home":
        return f"P({home} gana sin empate)={prob*100:.1f}%"
    if market == "dnb_away":
        return f"P({away} gana sin empate)={prob*100:.1f}%"
    return f"P(selección)={prob*100:.1f}%"


picks_details = []
for s in selected:
    league = next(r["league"] for r in results_all if r["match"] == s["match"])
    eg = next(r for r in results_all if r["match"] == s["match"])["probabilities"]
    notes = []
    if league in PROXY_LEAGUES:
        notes.append("xG por proxy GF/GA (sin Understat)")
    if s["home_team"] in ELO_FALLBACK_TEAMS or s["away_team"] in ELO_FALLBACK_TEAMS:
        notes.append("Elo de respaldo (mediana de liga)")
    incert = "Base +/- 5.0%" + (f"; {'; '.join(notes)}" if notes else "")
    why = (
        f"{market_phrase(s['market'], s['home_team'], s['away_team'], s['model_prob'])} "
        f"frente a la implícita {s['implied_prob']*100:.1f}%; cuota justa {s['fair_odds']:.2f} "
        f"vs cuota capturada {s['odds']:.2f}. Goles esperados del motor: "
        f"{eg['expected_goals_home']} - {eg['expected_goals_away']}. "
        f"EV robusto {s['robust_ev_percent']:+.2f}% con cuota en perfil "
        f"{s.get('selection_profile', 'prioritario')}."
    )
    risks = (
        "Varianza intrínseca del fútbol; el EV depende de cuotas de mejor precio entre casas "
        "(puede no estar disponible al mismo precio). "
    )
    if league in PROXY_LEAGUES:
        risks += "Datos de entrada por proxy GF/GA (sin xG real): mayor incertidumbre estructural. "
    if s["home_team"] in ELO_FALLBACK_TEAMS or s["away_team"] in ELO_FALLBACK_TEAMS:
        risks += "Elo estimado por mediana de liga para un equipo sin rating ClubElo. "
    risks += "Córners/tarjetas no disponibles: no se evalúan esos mercados. " \
        "Lesiones/suspensiones/alineaciones no verificables en vivo (fuentes no operativas) " \
        "y no modeladas: no se descarta un cambio de última hora."
    inp = INPUTS[s["match"]]
    src = LEAGUE_SRC[league]
    rates = (f"{s['home_team']} {inp['xg_home_for']:.2f}/{inp['xg_home_against']:.2f}, "
             f"{s['away_team']} {inp['xg_away_for']:.2f}/{inp['xg_away_against']:.2f}")
    fuentes = f"{src} ({rates}); Elo {inp['elo_home']:.0f}/{inp['elo_away']:.0f}; The Odds API cuota {s['odds']:.2f}"
    picks_details.append({
        "match": s["match"], "market": s["market"],
        "conf": "Media-Alta" if s["model_prob"] >= 0.58 else ("Media" if s["model_prob"] >= 0.50 else "Baja"),
        "incertidumbre": incert,
        "why": why,
        "risks": risks,
        "sources": fuentes,
        "min_odds": f"{1.0 / s['conservative_prob']:.2f}" if s["conservative_prob"] > 0 else "",
    })

results = {
    "all_results": results_all,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded,
}

meta = {
    "match_dates_text": MATCH_DATES_TEXT,
    "analysis_date_iso": NOW_UTC,
    "information_cutoff": NOW_UTC,
    "model_ia": "bigpickle",
    "engine_version": "model-v1.3",
    "leagues_display": "Premier League, La Liga, Serie A, Bundesliga, Ligue 1, Eredivisie, MLS, Liga Profesional Argentina (Liga BetPlay Colombia excluida: sin fuente de datos)",
    "requested_range": "2026-10-18",
    "universe_preamble": universe_preamble,
    "universe_matches": universe_matches,
    "picks_details": picks_details,
    "fallback_source": "Motor model-v1.3; xG Understat (proxy GF/GA en Eredivisie/MLS/Argentina); Elo ClubElo (respaldo por mediana de liga); cuotas The Odds API (mejor precio por resultado).",
}

json.dump(results, open(os.path.join(HERE, "results.json"), "w"), ensure_ascii=False, indent=1)
json.dump(meta, open(os.path.join(HERE, "meta.json"), "w"), ensure_ascii=False, indent=1)

print(f"candidates(initial value)={len(all_candidates)} selected={len(selected)} excluded={len(excluded)}")
for i, s in enumerate(selected, 1):
    print(f"  {i}. {s['match']:40s} {s['market']:12s} odds={s['odds']:.2f} p={s['model_prob']:.3f} "
          f"ev={s['ev_percent']:+.2f}% rob={s['robust_ev_percent']:+.2f}% prof={s['selection_profile']}")
