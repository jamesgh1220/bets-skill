import json

with open('scratch/sportinglife_data.json') as f:
    data = json.load(f)

matches = data.get('props', {}).get('pageProps', {}).get('matches', [])

print(f"Total matches found in file: {len(matches)}\n")

parsed_matches = []

for idx, m in enumerate(matches):
    comp = m.get('competition', {}).get('name') or m.get('homeComp')
    date = m.get('match_date')
    time = m.get('match_time')
    
    home_team = m.get('team_score_a', {}).get('team', {}).get('name')
    away_team = m.get('team_score_b', {}).get('team', {}).get('name')
    
    # Extract odds
    mbm = m.get('match_betting_market') or {}
    markets = mbm.get('match_betting_v2') or []
    home_odds = []
    draw_odds = []
    away_odds = []
    for b in markets:
        if not isinstance(b, dict): continue
        b_for = b.get('for')
        val = b.get('odds_decimal')
        if val is not None:
            if b_for == 'HOME': home_odds.append(val)
            elif b_for == 'DRAW': draw_odds.append(val)
            elif b_for == 'AWAY': away_odds.append(val)
    
    h_odd = max(home_odds) if home_odds else None
    d_odd = max(draw_odds) if draw_odds else None
    a_odd = max(away_odds) if away_odds else None
    
    print(f"Match {idx+1}: [{comp}] {home_team} vs {away_team} | Date: {date} {time} | Odds: 1={h_odd}, X={d_odd}, 2={a_odd}")
    
    parsed_matches.append({
        "comp": comp,
        "home": home_team,
        "away": away_team,
        "date": date,
        "time": time,
        "odds_1": h_odd,
        "odds_X": d_odd,
        "odds_2": a_odd
    })

with open('scratch/all_fixtures_sep14.json', 'w') as f:
    json.dump(parsed_matches, f, indent=2)
