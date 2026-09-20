import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.calc_engine import run_ensemble, load_model_config
from scripts.selection import select_portfolio

BASE = os.path.dirname(os.path.abspath(__file__))
ANALYSIS = os.path.join(BASE, "analysis_19sep")
os.makedirs(ANALYSIS, exist_ok=True)

elo = json.load(open(os.path.join(BASE, "analysis_19sep", "elo_19sep.json")))
us = json.load(open(os.path.join(BASE, "analysis_19sep", "us_xg.json")))
cons = json.load(open(os.path.join(BASE, "odds_19sep", "consolidated.json")))

LEAGUE_OF = {
    "Premier League": ["Tottenham Hotspur", "Aston Villa", "Brighton and Hove Albion", "Arsenal", "Everton", "Ipswich Town", "Newcastle United", "Hull City", "Nottingham Forest", "Coventry City"],
    "Bundesliga": ["Hamburger SV", "1. FC Köln", "Werder Bremen", "Augsburg", "Borussia Monchengladbach", "FSV Mainz 05", "Eintracht Frankfurt", "SC Freiburg", "VfB Stuttgart", "Borussia Dortmund"],
    "La Liga": ["CA Osasuna", "Rayo Vallecano", "Athletic Bilbao", "Alavés", "Celta Vigo", "Real Racing Club de Santander", "Sevilla", "Barcelona"],
    "Serie A": ["Bologna", "Torino", "Udinese", "Cagliari", "AS Roma", "Inter Milan", "Venezia", "Lazio"],
    "Ligue 1": ["Paris FC", "Strasbourg", "Angers", "Troyes", "Toulouse", "Le Havre", "Le Mans FC", "Lorient", "Lyon", "Rennes"],
    "Eredivisie": ["ADO Den Haag", "SC Cambuur", "Sparta Rotterdam", "Heerenveen", "Ajax", "Excelsior", "Willem II", "Fortuna Sittard"],
    "Liga Portugal": ["Gil Vicente", "CS Maritimo", "Nacional", "Famalicão", "Alverca", "Rio Ave FC", "Sporting Lisbon", "Arouca"],
    "Liga Argentina": ["Gimnasia La Plata", "Banfield", "Gimnasia Mendoza", "Deportivo Riestra", "Union Santa Fe", "Independiente", "River Plate", "Atlético Huracán", "Instituto de Córdoba", "Talleres"],
    "MLS": ["CF Montreal", "Columbus Crew SC", "D.C. United", "Charlotte FC", "San Jose Earthquakes", "Los Angeles FC", "New England Revolution", "Orlando City SC", "FC Dallas", "Austin FC", "Houston Dynamo", "FC Cincinnati", "Minnesota United FC", "LA Galaxy", "Sporting Kansas City", "Philadelphia Union", "St. Louis City SC", "Toronto FC", "Nashville SC", "Chicago Fire", "Colorado Rapids", "Seattle Sounders FC", "Real Salt Lake", "Vancouver Whitecaps FC", "Portland Timbers", "Atlanta United FC"],
    "Liga Colombiana": ["Millonarios", "Boyacá Chicó F.C.", "Alianza FC", "Independiente Santa Fe", "Deportivo Cali", "Cúcuta Deportivo", "Deportivo Pasto", "Once Caldas"],
}

def league_for(home, away):
    for lg, teams in LEAGUE_OF.items():
        if home in teams and away in teams:
            return lg
    return "MLS"

# xG per team: (for, against, home_split_for, home_split_against, away_split_for, away_split_against, source, proxy)
def build_xg_map():
    # Understat big-5
    us_map = {
        "Tottenham Hotspur": "Tottenham", "Brighton and Hove Albion": "Brighton", "Coventry City": "Coventry",
        "Hull City": "Hull", "Ipswich Town": "Ipswich", "Newcastle United": "Newcastle United",
        "Nottingham Forest": "Nottingham Forest", "Everton": "Everton", "Arsenal": "Arsenal", "Aston Villa": "Aston Villa",
        "Hamburger SV": "Hamburger SV", "1. FC Köln": "FC Cologne", "Werder Bremen": "Werder Bremen", "Augsburg": "Augsburg",
        "Borussia Monchengladbach": "Borussia M.Gladbach", "FSV Mainz 05": "Mainz 05", "Eintracht Frankfurt": "Eintracht Frankfurt",
        "SC Freiburg": "Freiburg", "VfB Stuttgart": "VfB Stuttgart", "Borussia Dortmund": "Borussia Dortmund",
        "CA Osasuna": "Osasuna", "Rayo Vallecano": "Rayo Vallecano", "Athletic Bilbao": "Athletic Club", "Alavés": "Alaves",
        "Celta Vigo": "Celta Vigo", "Real Racing Club de Santander": "Racing Santander", "Sevilla": "Sevilla", "Barcelona": "Barcelona",
        "Bologna": "Bologna", "Torino": "Torino", "Udinese": "Udinese", "Cagliari": "Cagliari", "AS Roma": "Roma",
        "Inter Milan": "Inter", "Venezia": "Venezia", "Lazio": "Lazio",
        "Paris FC": "Paris FC", "Strasbourg": "Strasbourg", "Angers": "Angers", "Troyes": "Troyes", "Toulouse": "Toulouse",
        "Le Havre": "Le Havre", "Le Mans FC": "Le Mans", "Lorient": "Lorient", "Lyon": "Lyon", "Rennes": "Rennes",
    }
    xg = {}
    for lg_name, lv in us.items():
        for us_team, v in lv.items():
            xg[us_team] = {
                "for": v["xg_for"], "against": v["xg_against"],
                "home_for": v.get("xg_for_home"), "home_against": v.get("xga_home"),
                "away_for": v.get("xg_for_away"), "away_against": v.get("xga_away"),
                "source": f"Understat {lg_name}", "proxy": False,
            }
    xg_out = {}
    for odds_name, us_team in us_map.items():
        if us_team in xg:
            xg_out[odds_name] = xg[us_team]
    # Non big-5: overall per-match averages
    rest = {
        "ADO Den Haag": (0.77, 2.02, "statz.ai Eredivisie", False), "SC Cambuur": (1.53, 2.00, "statz.ai Eredivisie", False),
        "Sparta Rotterdam": (1.80, 2.35, "statz.ai Eredivisie", False), "Heerenveen": (1.37, 1.70, "statz.ai Eredivisie", False),
        "Ajax": (2.62, 1.22, "statz.ai Eredivisie", False), "Excelsior": (1.57, 1.27, "statz.ai Eredivisie", False),
        "Willem II": (1.38, 2.40, "statz.ai Eredivisie", False), "Fortuna Sittard": (0.87, 2.68, "statz.ai Eredivisie", False),
        "Gil Vicente": (1.36, 1.00, "FotMob Opta Primeira Liga", False), "CS Maritimo": (1.08, 1.30, "FotMob Opta Primeira Liga", False),
        "Nacional": (1.15, 2.02, "FotMob Opta Primeira Liga", False), "Famalicão": (0.97, 1.25, "FotMob Opta Primeira Liga", False),
        "Alverca": (1.17, 2.08, "FotMob Opta Primeira Liga", False), "Rio Ave FC": (0.58, 1.72, "FotMob Opta Primeira Liga", False),
        "Sporting Lisbon": (2.18, 0.60, "FotMob Opta Primeira Liga", False), "Arouca": (1.13, 1.53, "FotMob Opta Primeira Liga", False),
        "Gimnasia La Plata": (1.20, 1.22, "Statz.ai Liga Prof", False), "Banfield": (1.14, 1.51, "Statz.ai Liga Prof", False),
        "Gimnasia Mendoza": (1.00, 1.38, "Statz.ai Liga Prof", False), "Deportivo Riestra": (0.90, 0.91, "Statz.ai Liga Prof", False),
        "Union Santa Fe": (1.36, 1.17, "Statz.ai Liga Prof", False), "Independiente": (1.09, 1.16, "Statz.ai Liga Prof", False),
        "River Plate": (1.62, 0.81, "Statz.ai Liga Prof", False), "Atlético Huracán": (1.12, 1.12, "Statz.ai Liga Prof", False),
        "Instituto de Córdoba": (1.42, 0.74, "Statz.ai Liga Prof", False), "Talleres": (1.19, 1.21, "Statz.ai Liga Prof", False),
        "CF Montreal": (1.57, 1.76, "ASA MLS 2026", False), "Columbus Crew SC": (1.30, 1.32, "ASA MLS 2026", False),
        "D.C. United": (1.50, 1.74, "ASA MLS 2026", False), "Charlotte FC": (1.69, 1.57, "ASA MLS 2026", False),
        "San Jose Earthquakes": (1.95, 1.65, "ASA MLS 2026", False), "Los Angeles FC": (1.73, 1.49, "ASA MLS 2026", False),
        "New England Revolution": (1.60, 1.56, "ASA MLS 2026", False), "Orlando City SC": (1.68, 2.03, "ASA MLS 2026", False),
        "FC Dallas": (1.73, 1.46, "ASA MLS 2026", False), "Austin FC": (1.16, 2.02, "ASA MLS 2026", False),
        "Houston Dynamo": (1.17, 1.26, "ASA MLS 2026", False), "FC Cincinnati": (1.81, 1.99, "ASA MLS 2026", False),
        "Minnesota United FC": (1.83, 1.64, "ASA MLS 2026", False), "LA Galaxy": (1.65, 1.84, "ASA MLS 2026", False),
        "Sporting Kansas City": (1.17, 2.19, "ASA MLS 2026", False), "Philadelphia Union": (2.01, 1.49, "ASA MLS 2026", False),
        "St. Louis City SC": (1.70, 1.37, "ASA MLS 2026", False), "Toronto FC": (1.37, 1.51, "ASA MLS 2026", False),
        "Nashville SC": (1.51, 1.48, "ASA MLS 2026", False), "Chicago Fire": (1.93, 1.45, "ASA MLS 2026", False),
        "Colorado Rapids": (1.55, 1.26, "ASA MLS 2026", False), "Seattle Sounders FC": (1.59, 1.70, "ASA MLS 2026", False),
        "Real Salt Lake": (1.54, 1.71, "ASA MLS 2026", False), "Vancouver Whitecaps FC": (2.40, 1.05, "ASA MLS 2026", False),
        "Portland Timbers": (1.57, 1.91, "ASA MLS 2026", False), "Atlanta United FC": (1.53, 1.70, "ASA MLS 2026", False),
        "Millonarios": (1.66, 1.11, "apwin.com Colombia 2026", False), "Boyacá Chicó F.C.": (1.00, 1.36, "apwin.com Colombia 2026", False),
        "Alianza FC": (0.89, 1.78, "GF/GA proxy Clausura (primatips)", True), "Independiente Santa Fe": (1.41, 1.36, "apwin.com Colombia 2026", False),
        "Deportivo Cali": (1.36, 1.09, "apwin.com Colombia 2026", False), "Cúcuta Deportivo": (1.00, 1.82, "apwin.com Colombia 2026", False),
        "Deportivo Pasto": (1.27, 1.31, "apwin.com Colombia 2026", False), "Once Caldas": (1.67, 1.39, "apwin.com Colombia 2026", False),
    }
    for t, (f, a, src, proxy) in rest.items():
        xg_out[t] = {"for": f, "against": a, "home_for": None, "home_against": None,
                     "away_for": None, "away_against": None, "source": src, "proxy": proxy}
    return xg_out


# Estimates Colombian Elo via regression fitted on teams with real Elo + xG diff
def estimate_colombia_elo():
    # elo = 70.3*xgd + 1664.7  (fitted across 93 teams w/ real elo and xG)
    col = {
        "Millonarios": (1.66, 1.11), "Boyacá Chicó F.C.": (1.00, 1.36), "Alianza FC": (0.89, 1.78),
        "Independiente Santa Fe": (1.41, 1.36), "Deportivo Cali": (1.36, 1.09), "Cúcuta Deportivo": (1.00, 1.82),
        "Deportivo Pasto": (1.27, 1.31), "Once Caldas": (1.67, 1.39),
    }
    return {t: round(70.3 * (f - a) + 1664.7) for t, (f, a) in col.items()}


xg_all = build_xg_map()
col_elo = estimate_colombia_elo()

# Colombia odds from research (Capa 3 aggregator, Pinnacle/best via football-predictions.ai)
col_odds = {
    ("Millonarios", "Boyacá Chicó F.C."): {"1": 1.27, "X": 5.45, "2": 11.54, "source": "football-predictions.ai best odds (Pinnacle 1X2, Capa 3)"},
    ("Alianza FC", "Independiente Santa Fe"): {"1": 2.81, "X": 3.27, "2": 2.55, "source": "football-predictions.ai best odds (Pinnacle, Capa 3)"},
    ("Deportivo Cali", "Cúcuta Deportivo"): {"1": 1.54, "X": 4.33, "2": 6.59, "source": "football-predictions.ai best odds (Pinnacle 1/2, Bet365 X, Capa 3)"},
    ("Deportivo Pasto", "Once Caldas"): {"1": 3.07, "X": 3.30, "2": 2.33, "source": "football-predictions.ai best odds (Pinnacle 1/2, Betfair X, Capa 3)"},
}
col_ou = {("Millonarios", "Boyacá Chicó F.C."): {"over_2_5": None, "under_2_5": None},
          ("Alianza FC", "Independiente Santa Fe"): {"over_2_5": None, "under_2_5": None},
          ("Deportivo Cali", "Cúcuta Deportivo"): {"over_2_5": None, "under_2_5": None},
          ("Deportivo Pasto", "Once Caldas"): {"over_2_5": None, "under_2_5": None}}

# corner/card library
MODEL_CONFIG = load_model_config("models/model-v1.3.json")

cc = {}
try:
    cc = json.load(open("/tmp/cc_library.json"))
except Exception:
    pass
# format: entries team -> list of [corners_for, corners_against, cards_for, cards_against]
def cc_rates(team):
    if team in cc:
        row = cc[team][-1]
        return {"corners_for": row[0], "corners_against": row[1], "cards_for": row[2], "cards_against": row[3]}
    return None

matches = json.load(open(os.path.join(BASE, "odds_19sep", "matches_19sep.txt")))
all_candidates = []
all_evaluations = []
all_results = []
match_files = []

for idx, m in enumerate(matches, 1):
    home, away = m.split(" vs ")
    league = league_for(home, away)
    # find odds event
    ev = None
    for e in cons.values():
        h = e.get("h2h", {})
        keyset = set(h.keys())
        if "Draw" in keyset:
            keyset.discard("Draw")
        if home in keyset and away in keyset:
            ev = e
            break
    odds = {}
    odds_source = "The Odds API (REST fallback, capa 1)"
    if ev:
        h = ev["h2h"]
        odds["1"] = h.get(home)
        odds["X"] = h.get("Draw")
        odds["2"] = h.get(away)
        t = ev.get("totals", {})
        if "2.5" in t:
            odds["over_2_5"] = t["2.5"].get("Over")
            odds["under_2_5"] = t["2.5"].get("Under")
        if "3.5" in t:
            odds["over_3_5"] = t["3.5"].get("Over")
            odds["under_3_5"] = t["3.5"].get("Under")
    else:
        # Colombia fallback
        key = (home, away)
        if key in col_odds:
            for k in ("1", "X", "2"):
                if col_odds[key][k]:
                    odds[k] = col_odds[key][k]
            ou = col_ou.get(key, {})
            for k, v in ou.items():
                if v:
                    odds[k] = v
            odds_source = col_odds[key]["source"]

    xh = xg_all.get(home); xa = xg_all.get(away)
    e_home = elo.get(home) or col_elo.get(home)
    e_away = elo.get(away) or col_elo.get(away)

    # home splits if available, else overall; blend by sample size to avoid
    # overconfidence on tiny home/away windows (n=1 splits are unstable).
    def blend(split_for, split_against, n_split, overall_for, overall_against, n_overall):
        if split_for is None or not n_split:
            return overall_for, overall_against
        w = min(1.0, n_split / 4.0)  # start trusting split at n=4
        f = w * split_for + (1 - w) * overall_for
        a = w * split_against + (1 - w) * overall_against
        return f, a

    if xh:
        hf, ha = blend(xh.get("home_for"), xh.get("home_against"), xh.get("nh") or 0,
                       xh["for"], xh["against"], xh.get("n") or 0)
    else:
        hf, ha = 1.3, 1.3
    if xa:
        af, aa = blend(xa.get("away_for"), xa.get("away_against"), xa.get("na") or 0,
                       xa["for"], xa["against"], xa.get("n") or 0)
    else:
        af, aa = 1.3, 1.3

    cr_h = cc_rates(home)
    cr_a = cc_rates(away)

    match_input = {
        "file": f"m{idx}_{home.lower().replace(' ','_')}_{away.lower().replace(' ','_')}.json",
        "home_team": home,
        "away_team": away,
        "league": league,
        "match_date": "2026-09-19",
        "xg_home_for": round(hf, 2), "xg_home_against": round(ha, 2),
        "xg_away_for": round(af, 2), "xg_away_against": round(aa, 2),
        "elo_home": e_home, "elo_away": e_away,
        "corners_home_for": cr_h["corners_for"] if cr_h else None,
        "corners_home_against": cr_h["corners_against"] if cr_h else None,
        "corners_away_for": cr_a["corners_for"] if cr_a else None,
        "corners_away_against": cr_a["corners_against"] if cr_a else None,
        "cards_home_for": cr_h["cards_for"] if cr_h else None,
        "cards_home_against": cr_h["cards_against"] if cr_h else None,
        "cards_away_for": cr_a["cards_for"] if cr_a else None,
        "cards_away_against": cr_a["cards_against"] if cr_a else None,
        "odds": {k: v for k, v in odds.items() if v},
        "_meta": {
            "league": league,
            "odds_source": odds_source,
            "xg_home_source": xh["source"] if xh else "n/d",
            "xg_away_source": xa["source"] if xa else "n/d",
            "xg_estimado": bool((xh and xh.get("proxy")) or (xa and xa.get("proxy")) or home in col_elo or away in col_elo),
            "elo_estimado": home in col_elo or away in col_elo,
        },
    }
    mfile = os.path.join(ANALYSIS, match_input["file"])
    with open(mfile, "w", encoding="utf-8") as f:
        json.dump(match_input, f, indent=2, ensure_ascii=False)
    match_files.append(mfile)

    res = run_ensemble(match_input, MODEL_CONFIG)
    res["league"] = league
    res["odds_source"] = odds_source
    all_results.append(res)
    for m_key, evl in res["evaluations"].items():
        full = dict(evl)
        full["match"] = res["match"]
        full["league"] = league
        full["home_team"] = home
        full["away_team"] = away
        all_evaluations.append(full)
        if evl["has_value"]:
            all_candidates.append(full)

# rerun with model loaded is wrong order; fix by moving above
selected, excluded = select_portfolio(all_candidates, max_picks=6)

output_data = {
    "all_results": all_results,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded,
}
out = os.path.join(BASE, "analysis_19sep", "results_19sep.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"Matches: {len(all_results)}")
print(f"Evaluations: {len(all_evaluations)}")
print(f"Candidates(has_value): {len(all_candidates)}")
print(f"Selected: {len(selected)}  Excluded: {len(excluded)}")
print()
print("--- CANDIDATOS (todos) ---")
for c in sorted(all_candidates, key=lambda x: (x["model_prob"], x["robust_ev_percent"]), reverse=True):
    print(f"{c['match']:42s} {c['market']:10s} cuota={c['odds']:6.2f} prob={c['model_prob']*100:5.1f}% EV={c['ev_percent']:6.2f}% rEV={c['robust_ev_percent']:6.2f}% stake={c['stake_recommended_units']:.2f}u")