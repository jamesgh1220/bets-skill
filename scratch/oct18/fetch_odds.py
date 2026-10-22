"""Fetch 2026-10-17 odds from The Odds API (8 leagues).

Strategy (credit-aware):
  1. Bulk /odds with markets=h2h, regions=eu -> discover event ids  (1 credit/league)
  2. Per-event /events/{id}/odds with the full market set, regions=eu (6 credits/event)
"""
import json, os, re, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
KEY = None
with open(os.path.join(ROOT, ".env")) as f:
    for line in f:
        m = re.match(r"\s*ODDS_API_KEY\s*=\s*(\S+)", line)
        if m:
            KEY = m.group(1)
assert KEY

LEAGUES = {
    "soccer_epl": "Premier League",
    "soccer_spain_la_liga": "La Liga",
    "soccer_italy_serie_a": "Serie A",
    "soccer_germany_bundesliga": "Bundesliga",
    "soccer_france_ligue_one": "Ligue 1",
    "soccer_netherlands_eredivisie": "Eredivisie",
    "soccer_usa_mls": "MLS",
    "soccer_argentina_primera_division": "Liga Profesional Argentina",
}
EVENT_MARKETS = "h2h,totals,btts,double_chance,draw_no_bet,alternate_totals"
TARGET_DAY = "2026-10-17"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
    return json.loads(urllib.request.urlopen(req, timeout=60).read().decode())


out = os.path.join(HERE, "odds_raw")
os.makedirs(out, exist_ok=True)
index = {}
for sport, label in LEAGUES.items():
    evs = get(f"https://api.the-odds-api.com/v4/sports/{sport}/odds/"
              f"?apiKey={KEY}&regions=eu&markets=h2h&oddsFormat=decimal")
    if not isinstance(evs, list):
        print("ERR", sport, evs)
        continue
    day = [e for e in evs if e["commence_time"].startswith(TARGET_DAY)]
    print(f"{label:32s} discovered={len(day)}")
    for e in day:
        full = get(f"https://api.the-odds-api.com/v4/sports/{sport}/events/{e['id']}/odds/"
                   f"?apiKey={KEY}&regions=eu&markets={EVENT_MARKETS}&oddsFormat=decimal")
        rec = {"league": label, "sport": sport, "event_id": e["id"],
               "home": e["home_team"], "away": e["away_team"],
               "commence_time": e["commence_time"],
               "bookmakers": full.get("bookmakers", [])}
        index[e["id"]] = rec
        print(f"   {e['home_team']} vs {e['away_team']}  books={len(rec['bookmakers'])}")

with open(os.path.join(HERE, "odds_full.json"), "w") as f:
    json.dump(index, f, ensure_ascii=False, indent=1)
print("TOTAL EVENTS:", len(index))
