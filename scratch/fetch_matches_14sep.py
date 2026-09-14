import urllib.request
import json

leagues = {
    'Premier League': 'eng.1',
    'LaLiga': 'esp.1',
    'Serie A': 'ita.1',
    'Liga Portugal': 'por.1',
    'Liga Argentina': 'arg.1',
    'Liga Colombiana': 'col.1'
}

date_str = '20260914'
all_matches = []

for name, code in leagues.items():
    url = f'https://site.api.espn.com/apis/site/v2/sports/soccer/{code}/scoreboard?dates={date_str}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.88.1'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            events = data.get('events', [])
            print(f"=== {name}: {len(events)} partidos el 2026-09-14 ===")
            for ev in events:
                competition = ev.get('competitions', [{}])[0]
                competitors = competition.get('competitors', [])
                home_team = away_team = None
                for c in competitors:
                    if c.get('homeAway') == 'home':
                        home_team = c.get('team', {}).get('displayName')
                    else:
                        away_team = c.get('team', {}).get('displayName')
                status = competition.get('status', {}).get('type', {}).get('name')
                date_iso = ev.get('date')
                odds_list = competition.get('odds', [])
                odds_data = {}
                if odds_list:
                    od = odds_list[0]
                    ml = od.get('moneyline', {})
                    odds_data = {
                        'overUnder': od.get('overUnder'),
                        'ml_home': ml.get('home', {}).get('close', {}).get('odds'),
                        'ml_away': ml.get('away', {}).get('close', {}).get('odds'),
                        'ml_draw': ml.get('draw', {}).get('close', {}).get('odds')
                    }
                print(f"   * {home_team} vs {away_team} | {date_iso} | status={status} | odds={odds_data}")
                all_matches.append({
                    'league': name,
                    'name': ev.get('name'),
                    'home_team': home_team,
                    'away_team': away_team,
                    'date': date_iso,
                    'status': status,
                    'odds_data': odds_data,
                    'event_id': ev.get('id')
                })
    except Exception as e:
        print(f"Error {name}: {e}")

with open('scratch/fetched_matches_14sep.json', 'w', encoding='utf-8') as f:
    json.dump(all_matches, f, indent=2, ensure_ascii=False)

print(f"\nTotal partidos encontrados el 2026-09-14: {len(all_matches)}")
