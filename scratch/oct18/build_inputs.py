#!/usr/bin/env python3
"""Build match_input_*.json files for the 2026-10-18 universe and run the engine.

Data sources (with documented fallbacks where a source is unavailable):
- xG/xGA  : Understat (EPL, La Liga, Bundesliga, Serie A, Ligue 1) -> true xG.
            Wikipedia GF/GA per game used ONLY as a goals-derived xG proxy for
            Eredivisie, MLS and Liga Profesional Argentina (no Understat coverage).
- Elo     : ClubElo global ranking, overridden by the ClubElo ARG country page
            for Argentine clubs (the global page confuses homonyms, e.g. an
            Argentine "River Plate" at 1441 vs the real one at 1734). Teams
            absent from ClubElo receive the median Elo of the other event teams
            in the same league (documented fallback).
- Odds    : The Odds API per-event endpoint, best (max) price per outcome across
            EU bookmakers. draw_no_bet market NOT captured (credit budget):
            documented, not silently omitted.
- corners/cards: NOT AVAILABLE (apifootball auth failed; SofaScore 403; The
            Odds API exposes no corners/cards markets). Documented, not omitted.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from statistics import median

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

ODDS = json.load(open(os.path.join(HERE, "odds_full.json")))
UNDERSTAT = json.load(open(os.path.join(HERE, "understat_2026.json")))
CLUBELO = json.load(open(os.path.join(HERE, "clubelo.json")))
WIKI = json.load(open(os.path.join(HERE, "wiki_tables.json")))

# ---------------------------------------------------------------- alias maps
# Odds API team name -> Understat team name (only 5 leagues have Understat).
US_ALIAS = {
    # EPL
    "Brighton and Hove Albion": "Brighton", "Leeds United": "Leeds",
    # La Liga
    "CA Osasuna": "Osasuna", "Real Racing Club de Santander": "Racing Santander",
    "Alavés": "Alaves", "Málaga": "Malaga",
    # Serie A
    "Atalanta BC": "Atalanta",
    # Bundesliga
    "SC Freiburg": "Freiburg", "TSG Hoffenheim": "Hoffenheim",
    "Borussia Monchengladbach": "Borussia M.Gladbach",
    # Ligue 1
    "AS Monaco": "Monaco",
}

# Odds API team name -> ClubElo club name (verified against clubelo.com).
ELO_ALIAS = {
    # EPL
    "Brighton and Hove Albion": "Brighton", "Leeds United": "Leeds",
    "Manchester United": "Man United", "Nottingham Forest": "Forest",
    # La Liga
    "CA Osasuna": "Osasuna", "Real Racing Club de Santander": "Santander",
    "Alavés": "Alaves", "Málaga": "Malaga", "Celta Vigo": "Celta",
    # Serie A
    "AC Milan": "Milan", "Atalanta BC": "Atalanta",
    # Bundesliga
    "SC Freiburg": "Freiburg", "TSG Hoffenheim": "Hoffenheim",
    "Borussia Monchengladbach": "Gladbach", "Bayer Leverkusen": "Leverkusen",
    # Ligue 1
    "AS Monaco": "Monaco",
    # Eredivisie
    "FC Zwolle": "Zwolle", "SC Cambuur": "Cambuur", "AZ Alkmaar": "AZ",
    "FC Twente Enschede": "Twente", "FC Utrecht": "Utrecht",
    "NEC Nijmegen": "Nijmegen", "Fortuna Sittard": "Sittard",
    # MLS
    "FC Cincinnati": "Cincinnati", "Columbus Crew SC": "Columbus",
    # ARG
    "Belgrano de Cordoba": "Belgrano", "Aldosivi Mar del Plata": "Aldosivi",
}

# Wikipedia GF/GA table per league (ARG: search both zone tables of the
# in-progress tournament; the annual aggregate is stale for current form).
WIKI_TABLES = {"Eredivisie": [0], "MLS": [2], "ARG": [2, 3]}
WIKI_ALIAS = {
    "Eredivisie": {"FC Zwolle": "PEC Zwolle", "SC Cambuur": "Cambuur",
                   "AZ Alkmaar": "AZ", "FC Twente Enschede": "Twente",
                   "FC Utrecht": "Utrecht", "NEC Nijmegen": "NEC"},
    "MLS": {"Columbus Crew SC": "Columbus Crew"},
    "ARG": {"Racing Club": "Racing", "Belgrano de Cordoba": "Belgrano",
            "Estudiantes de Río Cuarto": "Estudiantes (RC)",
            "Aldosivi Mar del Plata": "Aldosivi"},
}

LEAGUE_SOURCE = {
    "Premier League": ("understat", "EPL"),
    "La Liga": ("understat", "La Liga"),
    "Serie A": ("understat", "Serie A"),
    "Bundesliga": ("understat", "Bundesliga"),
    "Ligue 1": ("understat", "Ligue 1"),
    "Eredivisie": ("wiki", "Eredivisie"),
    "MLS": ("wiki", "MLS"),
    "Liga Profesional Argentina": ("wiki", "ARG"),
}


def wiki_lookup(league: str, team: str):
    name = WIKI_ALIAS.get(league, {}).get(team, team)
    for ti in WIKI_TABLES[league]:
        for row in WIKI[league][ti]["rows"]:
            if row["team"] == name:
                return row
    return None


def team_rates(league: str, team: str):
    """Return (for_per_game, against_per_game, source_label)."""
    kind, code = LEAGUE_SOURCE[league]
    if kind == "understat":
        name = US_ALIAS.get(team, team)
        rec = UNDERSTAT.get(name)
        if not rec:
            raise KeyError(f"understat missing: {league}/{team} -> {name}")
        return rec["xg_for"], rec["xg_against"], f"Understat {code} 2026 (xG real)"
    row = wiki_lookup(code, team)
    if not row:
        raise KeyError(f"wiki missing: {league}/{team}")
    return (row["gf"] / row["pld"], row["ga"] / row["pld"],
            f"Wikipedia {code} 2026 (proxy GF/GA por partido, sin xG)")


def elo_for(team: str):
    name = ELO_ALIAS.get(team, team)
    if name in CLUBELO:
        return float(CLUBELO[name]), None
    return None, name


def best_price(event, market_key, name=None, point=None):
    best = None
    for b in event["bookmakers"]:
        for m in b["markets"]:
            if m["key"] != market_key:
                continue
            for o in m["outcomes"]:
                if name is not None and o["name"] != name:
                    continue
                if point is not None and o.get("point") != point:
                    continue
                p = o["price"]
                if best is None or p > best:
                    best = p
    return best


def extract_odds(event):
    home, away = event["home"], event["away"]
    odds = {}
    for key, name in (("1", home), ("2", away), ("X", "Draw")):
        p = best_price(event, "h2h", name=name)
        if p:
            odds[key] = p
    for key, name, point in (
        ("over_2_5", "Over", 2.5), ("under_2_5", "Under", 2.5),
        ("over_1_5", "Over", 1.5), ("under_1_5", "Under", 1.5),
        ("over_3_5", "Over", 3.5), ("under_3_5", "Under", 3.5),
    ):
        p = best_price(event, "totals", name=name, point=point)
        if p is None:
            p = best_price(event, "alternate_totals", name=name, point=point)
        if p:
            odds[key] = p
    for key, name in (("btts_yes", "Yes"), ("btts_no", "No")):
        p = best_price(event, "btts", name=name)
        if p:
            odds[key] = p
    for dc_name, price in _dc_outcomes(event):
        odds[dc_name] = price
    return odds


def _dc_outcomes(event):
    home, away = event["home"], event["away"]
    best = {"1x": None, "x2": None, "12": None}
    for b in event["bookmakers"]:
        for m in b["markets"]:
            if m["key"] != "double_chance":
                continue
            for o in m["outcomes"]:
                n = o["name"]
                has_home, has_away, has_draw = home in n, away in n, "Draw" in n
                key = None
                if has_home and has_draw:
                    key = "1x"
                elif has_away and has_draw:
                    key = "x2"
                elif has_home and has_away:
                    key = "12"
                if key and (best[key] is None or o["price"] > best[key]):
                    best[key] = o["price"]
    return [(k, v) for k, v in best.items() if v]


def main():
    # league medians for Elo fallback
    league_teams = {}
    for e in ODDS.values():
        lg = e["league"]
        for t in (e["home"], e["away"]):
            league_teams.setdefault(lg, set()).add(t)
    league_elos = {}
    for lg, teams in league_teams.items():
        vals = []
        for t in teams:
            n = ELO_ALIAS.get(t, t)
            if n in CLUBELO:
                vals.append(CLUBELO[n])
        league_elos[lg] = median(vals)

    inputs_dir = os.path.join(HERE, "inputs")
    results_dir = os.path.join(HERE, "engine")
    os.makedirs(inputs_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    results = []
    for i, (eid, e) in enumerate(sorted(ODDS.items(), key=lambda kv: kv[1]["commence_time"])):
        lg = e["league"]
        home, away = e["home"], e["away"]
        hf, ha, hsrc = team_rates(lg, home)
        af, aa, asrc = team_rates(lg, away)
        elo_h, miss_h = elo_for(home)
        elo_a, miss_a = elo_for(away)
        fallback_h = elo_h is None
        fallback_a = elo_a is None
        if fallback_h:
            elo_h = league_elos[lg]
        if fallback_a:
            elo_a = league_elos[lg]
        odds = extract_odds(e)
        match_input = {
            "home_team": home, "away_team": away, "league": lg,
            "match_date": e["commence_time"][:10], "kickoff_utc": e["commence_time"],
            "xg_home_for": round(hf, 3), "xg_home_against": round(ha, 3),
            "xg_away_for": round(af, 3), "xg_away_against": round(aa, 3),
            "elo_home": elo_h, "elo_away": elo_a,
            "corner_cards_available": False,
            "odds": odds,
            "sources": {"xg": hsrc if hsrc == asrc else f"{hsrc}; {asrc}"},
        }
        path = os.path.join(inputs_dir, f"match_{i:02d}.json")
        json.dump(match_input, open(path, "w"), ensure_ascii=False, indent=1)
        out = os.path.join(results_dir, f"engine_{i:02d}.json")
        subprocess.run(
            [sys.executable, os.path.join(ROOT, "scripts", "calc_engine.py"),
             "--input", path, "--config", os.path.join(ROOT, "models", "model-v1.3.json"),
             "--output", out],
            check=True, cwd=ROOT,
            stdout=subprocess.DEVNULL,
        )
        res = json.load(open(out))
        res["home_team"], res["away_team"] = home, away
        res["league"] = lg
        res["commence_time"] = e["commence_time"]
        results.append(res)
        flags = []
        if fallback_h:
            flags.append(f"elo_home_fallback({miss_h})")
        if fallback_a:
            flags.append(f"elo_away_fallback({miss_a})")
        print(f"{i:02d} {home} vs {away} [{lg}] xg={hsrc} flags={flags} odds={len(odds)}")

    json.dump(results, open(os.path.join(HERE, "all_results.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"\n{len(results)} matches processed. league medians: {league_elos}")


if __name__ == "__main__":
    main()
