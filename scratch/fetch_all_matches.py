import urllib.request
import json
import os

leagues = {
    'Premier League': 'eng.1',
    'LaLiga': 'esp.1',
    'Bundesliga': 'ger.1',
    'Serie A': 'ita.1',
    'Ligue 1': 'fra.1',
    'Eredivisie': 'ned.1',
    'Liga Portugal': 'por.1',
    'MLS': 'usa.1',
    'Liga Argentina': 'arg.1',
    'Liga Colombiana': 'col.1'
}

date_str = '20260912'

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'curl/7.88.1')]

all_matches = []

for name, code in leagues.items():
    url = f'https://site.api.espn.com/apis/site/v2/sports/soccer/{code}/scoreboard?dates={date_str}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.88.1'})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            events = data.get('events', [])
            print(f"=== {name}: {len(events)} partidos el 2026-09-12 ===")
            for ev in events:
                name_str = ev.get('name')
                date_iso = ev.get('date')
                competitions = ev.get('competitions', [{}])[0]
                competitors = competitions.get('competitors', [])
                home_team = None
                away_team = None
                for c in competitors:
                    if c.get('homeAway') == 'home':
                        home_team = c.get('team', {}).get('displayName')
                    else:
                        away_team = c.get('team', {}).get('displayName')
                
                # Odd extraction if present
                odds_list = competitions.get('odds', [])
                odds_data = {}
                if odds_list:
                    od = odds_list[0]
                    # Moneyline
                    ml = od.get('moneyline', {})
                    # Over Under
                    ou = od.get('overUnder')
                    odds_data = {
                        'overUnder': ou,
                        'details': od.get('details'),
                        'ml_home': ml.get('home', {}).get('close', {}).get('odds'),
                        'ml_away': ml.get('away', {}).get('close', {}).get('odds'),
                        'ml_draw': ml.get('draw', {}).get('close', {}).get('odds')
                    }

                match_info = {
                    'league': name,
                    'name': name_str,
                    'home_team': home_team,
                    'away_team': away_team,
                    'date': date_iso,
                    'odds_data': odds_data,
                    'event_id': ev.get('id')
                }
                all_matches.append(match_info)
                print(f"   * {home_team} vs {away_team} | {date_iso}")
    except Exception as e:
        print(f"Error {name}: {e}")

with open('scratch/fetched_matches.json', 'w', encoding='utf-8') as f:
    json.dump(all_matches, f, indent=2, ensure_ascii=False)

print(f"\nTotal partidos encontrados el 12-09-2026: {len(all_matches)}")
