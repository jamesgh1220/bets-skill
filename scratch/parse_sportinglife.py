import urllib.request
import re
import json

url = 'https://www.sportinglife.com/football/fixtures-results/2026-09-14'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Let's inspect __NEXT_DATA__ or json embedded in HTML if available
next_data = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
if next_data:
    data = json.loads(next_data.group(1))
    print("Found NEXT_DATA JSON!")
    with open('scratch/sportinglife_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    # Parse competitions and matches
    # Let's search inside json structure
    page_props = data.get('props', {}).get('pageProps', {})
    print("Keys in pageProps:", page_props.keys())
    
    matches_data = page_props.get('matches', [])
    print(f"Total matches in pageProps: {len(matches_data)}")
    
    for m in matches_data:
        comp_name = m.get('competitionName') or m.get('competition', {}).get('name') or m.get('homeComp')
        home = m.get('homeTeam', {}).get('name') or m.get('homeTeamName')
        away = m.get('awayTeam', {}).get('name') or m.get('awayTeamName')
        time = m.get('time') or m.get('date') or m.get('matchTime')
        print(f"Comp: {comp_name} | {home} vs {away} | Time: {time}")

else:
    print("NEXT_DATA not found, doing regex search...")

