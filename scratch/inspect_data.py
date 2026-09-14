import json

with open('scratch/sportinglife_data.json') as f:
    data = json.load(f)

matches = data.get('props', {}).get('pageProps', {}).get('matches', [])
print(f"Loaded {len(matches)} matches from json.")

for idx, m in enumerate(matches):
    print(f"\n--- Match {idx+1} ---")
    print("Keys:", m.keys())
    # find team names
    print("homeTeam:", m.get('homeTeam'))
    print("awayTeam:", m.get('awayTeam'))
    print("homeComp:", m.get('homeComp'))
    print("date:", m.get('date'))
    print("matchDate:", m.get('matchDate'))
    print("time:", m.get('time'))
    print("status:", m.get('status'))
