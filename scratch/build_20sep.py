import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.calc_engine import run_ensemble, load_model_config
from scripts.selection import select_portfolio

BASE = os.path.dirname(os.path.abspath(__file__))
ANALYSIS = os.path.join(BASE, "analysis_20sep")
os.makedirs(ANALYSIS, exist_ok=True)

elo = json.load(open(os.path.join(BASE, "analysis_20sep", "elo_20sep.json")))
us = json.load(open(os.path.join(BASE, "analysis_20sep", "us_xg_20sep.json")))
cons = json.load(open(os.path.join(BASE, "odds_20sep", "consolidated.json")))

LEAGUE_OF = {
    "Premier League": ["Bournemouth", "Liverpool", "Leeds United", "Crystal Palace", "Manchester City", "Sunderland", "Fulham", "Manchester United"],
    "Bundesliga": ["Bayer Leverkusen", "RB Leipzig", "FC Schalke 04", "SV Elversberg", "SC Paderborn", "TSG Hoffenheim"],
    "La Liga": ["Getafe", "Malaga", "Atletico Madrid", "Real Madrid", "Deportivo La Coruna", "Real Betis", "Villarreal", "Levante", "Valencia", "Real Sociedad"],
    "Serie A": ["Fiorentina", "Napoli", "Frosinone", "Como", "Parma", "Genoa", "Juventus", "Atalanta", "AC Milan", "Lecce"],
    "Ligue 1": ["Auxerre", "Brest", "Nice", "Lille", "Marseille", "Paris Saint-Germain"],
    "Eredivisie": ["Feyenoord", "FC Utrecht", "AZ Alkmaar", "SC Telstar", "FC Twente", "PSV Eindhoven", "NEC Nijmegen", "Go Ahead Eagles"],
    "Liga Portugal": ["Estrela da Amadora", "Academico de Viseu", "Vitoria SC", "Moreirense", "Santa Clara", "Braga", "Estoril", "Casa Pia", "FC Porto", "Benfica"],
    "MLS": ["Inter Miami", "San Diego FC"],
    "Liga Argentina": ["San Lorenzo", "Boca Juniors", "Platense", "Newell's Old Boys", "Rosario Central", "Argentinos Juniors", "Belgrano de Cordoba", "Estudiantes de Rio Cuarto"],
    "Liga Colombiana": ["Fortaleza CEIF", "Atletico Junior"],
}

def league_for(home, away):
    for lg, teams in LEAGUE_OF.items():
        if home in teams and away in teams:
            return lg
    return "MLS"

# us_xg_20sep.json is already keyed by canonical team names
def build_xg_map():
    xg = {}
    for team, v in us.items():
        xg[team] = {
            "for": v.get("xg_for"), "against": v.get("xg_against"),
            "home_for": v.get("xg_for_home"), "home_against": v.get("xga_home"),
            "away_for": v.get("xg_for_away"), "away_against": v.get("xga_away"),
            "n": v.get("n"), "nh": v.get("nh"), "na": v.get("na"),
            "source": v.get("source", "n/d"), "proxy": False,
        }
    return xg

xg_all = build_xg_map()

MODEL_CONFIG = load_model_config("models/model-v1.3.json")

cc = {}
try:
    cc = json.load(open("/tmp/cc_library.json"))
except Exception:
    pass
def cc_rates(team):
    if team in cc:
        row = cc[team][-1]
        return {"corners_for": row[0], "corners_against": row[1], "cards_for": row[2], "cards_against": row[3]}
    return None

matches = json.load(open(os.path.join(BASE, "odds_20sep", "matches_20sep.txt")))
all_candidates = []
all_evaluations = []
all_results = []
match_files = []

for idx, m in enumerate(matches, 1):
    home, away = m.split(" vs ")
    league = league_for(home, away)
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
    odds_lines = {}
    odds_source = "The Odds API (REST, capa 1)"
    if ev:
        h = ev["h2h"]
        odds["1"] = h.get(home)
        odds["X"] = h.get("Draw")
        odds["2"] = h.get(away)
        t = ev.get("totals", {})
        for line, ou in t.items():
            odds_lines[line] = {"over": ou.get("Over"), "under": ou.get("Under")}
            if line in ("1.5", "2.5", "3.5") and ou.get("Over") and ou.get("Under"):
                odds[f"over_{line.replace('.', '_')}"] = ou.get("Over")
                odds[f"under_{line.replace('.', '_')}"] = ou.get("Under")
    else:
        odds_source = "n/d"

    xh = xg_all.get(home); xa = xg_all.get(away)
    e_home = elo.get(home)
    e_away = elo.get(away)

    def blend(split_for, split_against, n_split, overall_for, overall_against, n_overall):
        if split_for is None or not n_split:
            return overall_for, overall_against
        w = min(1.0, n_split / 4.0)
        f = w * split_for + (1 - w) * overall_for
        a = w * split_against + (1 - w) * overall_against
        return f, a

    if xh and xh.get("for") is not None:
        hf, ha = blend(xh.get("home_for"), xh.get("home_against"), xh.get("nh") or 0,
                       xh["for"], xh["against"], xh.get("n") or 0)
    else:
        hf, ha = 1.3, 1.3
    if xa and xa.get("for") is not None:
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
        "match_date": "2026-09-20",
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
        "odds_lines": odds_lines,
        "_meta": {
            "league": league,
            "odds_source": odds_source,
            "xg_home_source": xh["source"] if xh else "n/d",
            "xg_away_source": xa["source"] if xa else "n/d",
            "xg_estimado": bool((xh and xh.get("proxy")) or (xa and xa.get("proxy"))),
            "elo_estimado": False,
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

selected, excluded = select_portfolio(all_candidates, max_picks=6)

output_data = {
    "all_results": all_results,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded,
}
out = os.path.join(BASE, "analysis_20sep", "results_20sep.json")
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