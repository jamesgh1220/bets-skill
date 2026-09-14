import json

with open('scratch/sportinglife_data.json') as f:
    data = json.load(f)

matches = data.get('props', {}).get('pageProps', {}).get('matches', [])
for idx in [2, 3, 10, 11, 13, 14, 15, 16]:
    if idx < len(matches):
        print(f"--- MATCH {idx} ---")
        print(json.dumps(matches[idx], indent=2))
