import urllib.request
import json

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://prod-public-api.livescore.com/v1/api/app/date/soccer/20260913/0?MD=1'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())

stages = data.get('Stages', [])

print("=== TODOS LOS PARTIDOS EN LIVESCORE PARA 2026-09-13 POR PAÍS Y LIGA ===")

leagues_requested = [
    'bundesliga', 'argentina', 'colombia', 'colombiana', 'spain', 'espanola', 'laliga',
    'mls', 'usa', 'france', 'ligue 1', 'england', 'premier league', 'italy', 'serie a',
    'holland', 'netherlands', 'eredivisie', 'portugal', 'primeira'
]

matches_by_requested_league = {}

for st in stages:
    cname = str(st.get('Cname', ''))
    sname = str(st.get('Snm', ''))
    ccode = str(st.get('Ccd', ''))
    league_full = f"{ccode} | {cname} - {sname}"
    events = st.get('Events', [])
    
    # Check match against requested list
    for lreq in leagues_requested:
        if lreq in ccode.lower() or lreq in cname.lower() or lreq in sname.lower():
            if league_full not in matches_by_requested_league:
                matches_by_requested_league[league_full] = []
            for ev in events:
                t1 = ev.get('T1', [{}])[0].get('Nm', 'Home')
                t2 = ev.get('T2', [{}])[0].get('Nm', 'Away')
                time_val = ev.get('Esd', '')
                status = ev.get('Eps', '')
                matches_by_requested_league[league_full].append((t1, t2, time_val, status))

for lg, matches in matches_by_requested_league.items():
    print(f"\n[{lg}] ({len(matches)} partidos):")
    for t1, t2, time_val, status in matches:
        print(f"   * {t1} vs {t2} (UTC: {time_val}, Status: {status})")
