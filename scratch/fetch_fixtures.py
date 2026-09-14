import urllib.request
import json
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def fetch_espn_scoreboard(date_str, league_code):
    url = f"https://site.api.espn.com/apis/site/v2/sports/soccer/{league_code}/scoreboard?dates={date_str}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            events = data.get('events', [])
            print(f"--- League: {league_code} on {date_str} (Count: {len(events)}) ---")
            for ev in events:
                name = ev.get('name')
                date = ev.get('date')
                status = ev.get('status', {}).get('type', {}).get('detail')
                print(f"  Event: {name} | Date: {date} | Status: {status}")
                comp = ev.get('competitions', [{}])[0]
                competitors = comp.get('competitors', [])
                for c in competitors:
                    team = c.get('team', {}).get('displayName')
                    home_away = c.get('homeAway')
                    print(f"    {home_away}: {team}")
    except Exception as e:
        print(f"Error fetching {league_code}: {e}")

leagues = [
    'eng.1', # Premier League
    'esp.1', # La Liga
    'ita.1', # Serie A
    'por.1', # Liga Portugal
    'arg.1', # Liga Argentina
    'col.1', # Liga Colombiana
]

date_str = '20260914'
for l in leagues:
    fetch_espn_scoreboard(date_str, l)
