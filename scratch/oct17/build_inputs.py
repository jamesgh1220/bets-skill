#!/usr/bin/env python3
"""Build match_input_*.json files for the 2026-10-17 universe and run the engine.

Data sources (with documented fallbacks where a source is unavailable):
- xG/xGA  : Understat (EPL, La Liga, Bundesliga, Serie A, Ligue 1) -> true xG.
            Wikipedia GF/GA per game used ONLY as a goals-derived xG proxy for
            Eredivisie, MLS and Liga Profesional Argentina (no Understat coverage).
- Elo     : ClubElo. Teams absent from ClubElo receive the median Elo of the
            other event teams in the same league (documented fallback).
- Odds    : The Odds API, best (max) price per outcome across bookmakers.
- corners/cards: NOT AVAILABLE (apifootball auth failed; SofaScore/FlashScore
            403; The Odds API exposes no corners/cards markets). Documented, not
            silently omitted.
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
    "Hull City": "Hull", "Ipswich Town": "Ipswich",
    # La Liga
    "Atlético Madrid": "Atletico Madrid", "Elche CF": "Elche",
    "Athletic Bilbao": "Athletic Club",
    # Serie A
    "Inter Milan": "Inter", "AS Roma": "Roma",
    # Bundesliga
    "FC Schalke 04": "Schalke 04", "FSV Mainz 05": "Mainz 05",
    "SC Paderborn": "Paderborn", "RB Leipzig": "RasenBallsport Leipzig",
    # Ligue 1
    "RC Lens": "Lens",
}

# Odds API team name -> ClubElo club name.
ELO_ALIAS = {
    "Manchester City": "Man City", "Ipswich Town": "Ipswich",
    "Newcastle United": "Newcastle",
    "Atlético Madrid": "Atlético", "Elche CF": "Elche", "Real Betis": "Betis",
    "Athletic Bilbao": "Athletic Club",
    "Inter Milan": "Internazionale", "AS Roma": "Roma",
    "Borussia Dortmund": "Dortmund", "FC Schalke 04": "Schalke",
    "FSV Mainz 05": "Mainz", "Hamburger SV": "Hamburg",
    "VfB Stuttgart": "Stuttgart", "Werder Bremen": "Werder",
    "SC Paderborn": "Paderborn", "Bayern Munich": "Bayern München",
    "RB Leipzig": "RB Leipzig",
    "Paris Saint Germain": "Paris SG", "RC Lens": "Lens",
    # Eredivisie
    "ADO Den Haag": "Den Haag", "PSV Eindhoven": "PSV", "SC Telstar": "Telstar",
    "Sparta Rotterdam": "Sparta",
    # MLS
    "Philadelphia Union": "Philadelphia", "Charlotte FC": "Charlotte",
    "Minnesota United FC": "Minnesota Utd", "St. Louis City SC": "St. Louis City",
    "Inter Miami CF": "Inter Miami", "New England Revolution": "NE Revolution",
    "Orlando City SC": "Orlando City", "New York City FC": "NYC FC",
    "Los Angeles FC": "LAFC", "New York Red Bulls": "New York RB",
    # ARG
    "CA Tigre BA": "Tigre", "Lanus": "Lanús", "Atlético Tucuman": "Atlético Tucumán",
    "Velez Sarsfield BA": "Vélez Sarsfield", "Gimnasia Mendoza": "GyE Mendoza",
    "Independiente Rivadavia": "Ind Rivadavia",
}

# Wikipedia GF/GA (aggregate table) team name per league.
WIKI_TABLE = {"Eredivisie": 0, "MLS": 2, "ARG": 4}
WIKI_ALIAS = {
    "Eredivisie": {"SC Telstar": "Telstar"},
    "MLS": {"Chicago Fire": "Chicago Fire FC"},
    "ARG": {"CA Tigre BA": "Tigre", "Lanus": "Lanús",
            "Atlético Tucuman": "Atlético Tucumán", "Platense": "Platense",
            "Velez Sarsfield BA": "Vélez Sarsfield"},
}

# Link-verified override: the ARG aggregate table collapses two distinct clubs
# ("Gimnasia y Esgrima (LP)" and "Gimnasia y Esgrima (M)") to the same label.
WIKI_OVERRIDE = {("ARG", "Gimnasia Mendoza"): {"pld": 28, "gf": 29, "ga": 34}}

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
    key = WIKI_OVERRIDE.get((league, team))
    if key:
        return key
    name = WIKI_ALIAS.get(league, {}).get(team, team)
    table = WIKI[league][WIKI_TABLE[league]]
    for row in table["rows"]:
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
    # wiki goals-derived proxy
    row = wiki_lookup(code, team)
    if not row:
        raise KeyError(f"wiki missing: {league}/{team}")
    return (row["gf"] / row["pld"], row["ga"] / row["pld"],
            f"Wikipedia {code} 2026 (proxy GF/GA por partido, sin xG)")


def elo_for(team: str, league: str, league_elos: dict):
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
        mk = "totals" if point == 2.5 else "alternate_totals"
        p = best_price(event, mk, name=name, point=point)
        if p:
            odds[key] = p
    for key, name in (("btts_yes", "Yes"), ("btts_no", "No")):
        p = best_price(event, "btts", name=name)
        if p:
            odds[key] = p
    for dc_name, price in _dc_outcomes(event):
        odds[dc_name] = price
    for key, name in (("dnb_home", home), ("dnb_away", away)):
        p = best_price(event, "draw_no_bet", name=name)
        if p:
            odds[key] = p
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

    report = []
    results = []
    for i, (eid, e) in enumerate(sorted(ODDS.items(), key=lambda kv: kv[1]["commence_time"])):
        lg = e["league"]
        home, away = e["home"], e["away"]
        hf, ha, hsrc = team_rates(lg, home)
        af, aa, asrc = team_rates(lg, away)
        elo_h, miss_h = elo_for(home, lg, league_elos)
        elo_a, miss_a = elo_for(away, lg, league_elos)
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
        report.append(f"{i:02d} {home} vs {away} [{lg}] xg={hsrc} flags={flags} odds={len(odds)}")

    json.dump(results, open(os.path.join(HERE, "all_results.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\n".join(report))
    print(f"\n{len(results)} matches processed. league medians: {league_elos}")


if __name__ == "__main__":
    main()
