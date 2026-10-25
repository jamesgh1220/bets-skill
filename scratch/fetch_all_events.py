import urllib.request
import json
import datetime

api_key = "e8e5ad6f4f934114dfe7e5a153af80d7"

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

target_date_str = "2026-10-24"

all_events = {}

for league_name, sport_key in sports_map.items():
    url = f"https://api.the-odds-api.com/v4/sports/{sport_key}/events?apiKey={api_key}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            events = json.loads(resp.read().decode('utf-8'))
            filtered = []
            for ev in events:
                # check commence_time in UTC
                # format is usually 2026-10-24T...
                ctime = ev.get('commence_time', '')
                if ctime.startswith(target_date_str):
                    filtered.append(ev)
            all_events[league_name] = filtered
            print(f"{league_name}: {len(filtered)} partidos encontrados para {target_date_str}")
    except Exception as e:
        print(f"Error fetching {league_name}: {e}")

with open("scratch/today_events.json", "w") as f:
    json.dump(all_events, f, indent=2)

