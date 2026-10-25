import json

with open("scratch/oct18/understat_2026.json") as f:
    us = json.load(f)

with open("scratch/oct24/clubelo.json") as f:
    elo = json.load(f)

with open("scratch/today_events.json") as f:
    events = json.load(f)

for league, evs in events.items():
    print(f"\n--- {league} ---")
    for e in evs:
        h = e['home_team']
        a = e['away_team']
        h_us = us.get(h) or any(h.lower() in k.lower() for k in us.keys())
        a_us = us.get(a) or any(a.lower() in k.lower() for k in us.keys())
        h_elo = elo.get(h) or any(h.lower() in k.lower() for k in elo.keys())
        a_elo = elo.get(a) or any(a.lower() in k.lower() for k in elo.keys())
        print(f"{h} vs {a}: Understat=({bool(h_us)}, {bool(a_us)}) | Elo=({bool(h_elo)}, {bool(a_elo)})")

