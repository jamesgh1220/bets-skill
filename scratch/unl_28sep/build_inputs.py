"""Build 8 match_input JSONs for UEFA Nations League 2026-09-28 (MD2).

xG for national teams is NOT AVAILABLE (statz 2026/27 xG contaminated, mixes 2024-25
NL fixtures relabelled 2026/27). Per documented decision, xg_* fields carry
goals_for/goals_against averages as a GOALS-DERIVED PROXY — labelled, never true xG.
Corners/cards are real collected rates (statz 2026/27 logs).
Odds captured from The Odds API on 2026-09-28 ~14:02Z (pre-kickoff).
"""

import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ODDS = json.load(open(os.path.join(HERE, "odds_best.json")))

def odds_key(match):
    home = match["home"]
    away = match["away"]
    for k in ODDS:
        if ODDS[k]["home"] == home and ODDS[k]["away"] == away:
            return k
    raise KeyError(f"odds not found for {home} vs {away}")

MATCHES = [
    # (home, away, elo_h, elo_a, xg_proxy_h_for, against, away_for, against,
    #  corners_h_for, h_against, a_for, a_against, cards_h_for, h_against, a_for, a_against, kickoff)
    dict(home="Armenia", away="Montenegro", elo_home=1388, elo_away=1469,
         xg_home_for=0.8, xg_home_against=2.3, xg_away_for=1.5, xg_away_against=1.9,
         corners_home_for=5.7, corners_home_against=4.6, corners_away_for=5.3, corners_away_against=3.6,
         cards_home_for=1.1, cards_home_against=1.7, cards_away_for=1.6, cards_away_against=1.6,
         kickoff="2026-09-28T16:00:00Z"),
    dict(home="Latvia", away="Cyprus", elo_home=1273, elo_away=1306,
         xg_home_for=0.6, xg_home_against=1.4, xg_away_for=1.7, xg_away_against=1.6,
         corners_home_for=4.5, corners_home_against=5.7, corners_away_for=4.8, corners_away_against=4.2,
         cards_home_for=2.1, cards_home_against=1.5, cards_away_for=2.5, cards_away_against=1.7,
         kickoff="2026-09-28T16:00:00Z"),
    dict(home="Georgia", away="Ukraine", elo_home=1626, elo_away=1802,
         xg_home_for=1.2, xg_home_against=1.6, xg_away_for=1.6, xg_away_against=1.4,
         corners_home_for=5.0, corners_home_against=4.6, corners_away_for=4.56, corners_away_against=4.33,
         cards_home_for=1.1, cards_home_against=2.5, cards_away_for=2.5, cards_away_against=1.2,
         kickoff="2026-09-28T16:00:00Z"),
    dict(home="Belgium", away="France", elo_home=1979, elo_away=2083,
         xg_home_for=2.4, xg_home_against=0.8, xg_away_for=2.4, xg_away_against=1.1,
         corners_home_for=5.2, corners_home_against=3.4, corners_away_for=5.9, corners_away_against=2.9,
         cards_home_for=1.7, cards_home_against=1.7, cards_away_for=1.5, cards_away_against=1.0,
         kickoff="2026-09-28T18:45:00Z"),
    dict(home="Romania", away="Bosnia & Herzegovina", elo_home=1629, elo_away=1616,
         xg_home_for=1.7, xg_home_against=1.4, xg_away_for=0.9, xg_away_against=1.2,
         corners_home_for=4.2, corners_home_against=5.3, corners_away_for=4.5, corners_away_against=5.5,
         cards_home_for=1.7, cards_home_against=2.2, cards_away_for=2.1, cards_away_against=1.3,
         kickoff="2026-09-28T18:45:00Z"),
    dict(home="Northern Ireland", away="Hungary", elo_home=1633, elo_away=1688,
         xg_home_for=0.8, xg_home_against=1.1, xg_away_for=1.5, xg_away_against=1.1,
         corners_home_for=3.0, corners_home_against=5.7, corners_away_for=5.2, corners_away_against=4.0,
         cards_home_for=2.3, cards_home_against=1.4, cards_away_for=1.7, cards_away_against=2.9,
         kickoff="2026-09-28T18:45:00Z"),
    dict(home="Turkey", away="Italy", elo_home=1839, elo_away=1837,
         xg_home_for=1.5, xg_home_against=0.9, xg_away_for=1.9, xg_away_against=1.2,
         corners_home_for=7.5, corners_home_against=3.8, corners_away_for=6.5, corners_away_against=3.7,
         cards_home_for=2.1, cards_home_against=1.3, cards_away_for=1.8, cards_away_against=1.9,
         kickoff="2026-09-28T18:45:00Z"),
    dict(home="Sweden", away="Poland", elo_home=1741, elo_away=1699,
         xg_home_for=1.9, xg_home_against=2.0, xg_away_for=1.6, xg_away_against=1.2,
         corners_home_for=3.4, corners_home_against=5.0, corners_away_for=6.3, corners_away_against=3.2,
         cards_home_for=1.1, cards_home_against=1.5, cards_away_for=1.8, cards_away_against=2.2,
         kickoff="2026-09-28T18:45:00Z"),
]

for m in MATCHES:
    key = odds_key(m)
    odds_raw = ODDS[key]["odds"]
    # Only captured odds are included; corners/cards odds not captured -> n/d (omitted).
    inp = {
        "home_team": m["home"],
        "away_team": m["away"],
        "league": "UEFA Nations League",
        "match_date": "2026-09-28",
        "kickoff_utc": m["kickoff"],
        "info_note": (
            "xg_* are GOALS-DERIVED PROXY (statz 2026/27 national-team xG contaminated; "
            "goals_for/goals_against avgs, N=10 unless noted). elo from international-football.net "
            "2026-09-28 post-MD1. corners/cards from statz logs."
        ),
        "xg_home_for": m["xg_home_for"], "xg_home_against": m["xg_home_against"],
        "xg_away_for": m["xg_away_for"], "xg_away_against": m["xg_away_against"],
        "elo_home": m["elo_home"], "elo_away": m["elo_away"],
        "corners_home_for": m["corners_home_for"], "corners_home_against": m["corners_home_against"],
        "corners_away_for": m["corners_away_for"], "corners_away_against": m["corners_away_against"],
        "cards_home_for": m["cards_home_for"], "cards_home_against": m["cards_home_against"],
        "cards_away_for": m["cards_away_for"], "cards_away_against": m["cards_away_against"],
        "odds": odds_raw,
    }
    slug = "-".join(m["home"].lower().replace(" ", "_").replace("&", "and").split())
    path = os.path.join(HERE, f"match_input_{slug}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(inp, f, ensure_ascii=False, indent=2)
    print("wrote", os.path.basename(path))