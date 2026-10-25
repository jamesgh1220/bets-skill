import urllib.request
import json
import time

api_key = "e8e5ad6f4f934114dfe7e5a153af80d7"

with open("scratch/today_events.json") as f:
    events_by_league = json.load(f)

sports_map = {
    "Premier League": "soccer_epl",
    "LaLiga": "soccer_spain_la_liga",
    "Bundesliga": "soccer_germany_bundesliga",
    "Serie A": "soccer_italy_serie_a",
    "Ligue 1": "soccer_france_ligue_one",
    "Eredivisie": "soccer_netherlands_eredivisie",
    "Liga Portugal": "soccer_portugal_primeira_liga",
    "MLS": "soccer_usa_mls",
    "Liga Argentina": "soccer_argentina_primera_division"
}

# Instead of fetching 32 events individually (which would blow our 22 remaining calls),
# we can call the league odds endpoint with markets=h2h,totals!
# Each league call costs 1 request and returns odds for ALL games in that league!
all_odds = {}

for league_name, sport_key in sports_map.items():
    if not events_by_league.get(league_name):
        continue
    url = f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds/?apiKey={api_key}&regions=eu,us&markets=h2h,totals&oddsFormat=decimal"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            rem = resp.headers.get("x-requests-remaining")
            print(f"Fetched odds for {league_name}. Remaining requests: {rem}")
            data = json.loads(resp.read().decode('utf-8'))
            all_odds[league_name] = data
        time.sleep(0.5)
    except Exception as e:
        print(f"Error fetching odds for {league_name}: {e}")

with open("scratch/oct24/all_league_odds.json", "w") as f:
    json.dump(all_odds, f, indent=2)

