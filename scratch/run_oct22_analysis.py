
import json
import os
import sys
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.calc_engine import run_ensemble, load_model_config
from scripts.selection import select_portfolio
from scripts.render_artifact import render

BASE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = Path(BASE)

# 1. Load odds
uel_odds = json.load(open(SCRATCH / 'soccer_uefa_europa_league_odds.json'))
uecl_odds = json.load(open(SCRATCH / 'soccer_uefa_europa_conference_league_odds.json'))

# Load clubelo
clubelo = json.load(open(SCRATCH / 'oct18' / 'clubelo.json'))

# Team name mapping for ClubElo
elo_alias = {
    'FC Copenhagen': 'FC Kobenhavn',
    'FC Kairat': 'FK Kairat',
    'FK Kauno Žalgiris': 'Kauno Zalgiris',
    'Ferencváros TC': 'Ferencvaros',
    'Omonoia FC': 'Omonia',
    'Pafos FC': 'Paphos',
    'Riga FC': 'FK Riga',
    'Sint Truiden': 'St Truiden',
    'Red Star Belgrade': 'Crvena Zvezda',
    'Lincoln Red Imps FC': 'Lincoln Red Imps',
    'FC Twente Enschede': 'FC Twente',
    'Besiktas JK': 'Besiktas',
    'Olympiakos Piraeus': 'Olympiakos',
    'Brighton and Hove Albion': 'Brighton',
    'FC Nordsjaelland': 'Nordsjaelland',
    'AS Monaco': 'Monaco',
    'Atalanta BC': 'Atalanta',
    'SC Braga': 'Braga',
    'SC Freiburg': 'Freiburg',
    'SK Sturm Graz': 'Sturm Graz',
    'SK Brann': 'Brann',
    'TSG Hoffenheim': 'Hoffenheim',
    'FK Borac Banja Luka': 'Borac Banja Luka',
    'FK Jablonec': 'Jablonec',
    'FC Iberia 1999': 'Saburtalo',
    'FC Midtjylland': 'Midtjylland',
    'FC Thun': 'Thun',
    'FC Lugano': 'Lugano',
    'KF Egnatia': 'Egnatia',
    'Union Saint-Gilloise': 'Union SG',
    'PFC CSKA Sofia': 'CSKA Sofia',
    'PFC Levski Sofia': 'Levski Sofia',
    "Inter Club d'Escaldes": 'Inter d Escaldes',
    'FC Ararat-Armenia': 'Ararat-Armenia',
    'NK Celje': 'Celje'
}

def get_elo(team):
    alias = elo_alias.get(team, team)
    if alias in clubelo:
        return clubelo[alias]
    for k, v in clubelo.items():
        if alias.lower() == k.lower():
            return v
    # Regional defaults for minor unlisted clubs
    if 'Escaldes' in team: return 1150
    if 'Egnatia' in team: return 1280
    if 'Union Saint-Gilloise' in team: return 1680
    if 'Ararat' in team: return 1320
    if 'Iberia' in team: return 1260
    return 1450

# Best odds extractor from bookmakers
def extract_best_odds(bm_list):
    odds = {}
    lines = {}
    for bm in bm_list:
        for mkt in bm.get('markets', []):
            k = mkt.get('key')
            if k == 'h2h':
                for oc in mkt.get('outcomes', []):
                    name = oc.get('name')
                    price = float(oc.get('price', 0))
                    if name == 'Draw':
                        odds['X'] = max(odds.get('X', 0), price)
                    elif 'home' not in odds or name == oc.get('name'):
                        pass
            elif k == 'totals':
                for oc in mkt.get('outcomes', []):
                    pt = oc.get('point')
                    name = oc.get('name')
                    price = float(oc.get('price', 0))
                    if pt == 1.5:
                        if name == 'Over': odds['over_1_5'] = max(odds.get('over_1_5', 0), price)
                        elif name == 'Under': odds['under_1_5'] = max(odds.get('under_1_5', 0), price)
                    elif pt == 2.5:
                        if name == 'Over': odds['over_2_5'] = max(odds.get('over_2_5', 0), price)
                        elif name == 'Under': odds['under_2_5'] = max(odds.get('under_2_5', 0), price)
                    elif pt == 3.5:
                        if name == 'Over': odds['over_3_5'] = max(odds.get('over_3_5', 0), price)
                        elif name == 'Under': odds['under_3_5'] = max(odds.get('under_3_5', 0), price)
    return odds

# Load model config
cfg = load_model_config('models/model-v1.3.json')

matches_processed = []
all_results = []
all_candidates = []
all_evaluations = []

universe_items = []
uel_list = []
uecl_list = []

for item in uel_odds:
    home = item['home_team']
    away = item['away_team']
    commence = item['commence_time']
    uel_list.append(f'{home} vs {away}')
    
    odds = {}
    # extract h2h and totals from bookmakers
    for bm in item['bookmakers']:
        for mkt in bm['markets']:
            if mkt['key'] == 'h2h':
                for oc in mkt['outcomes']:
                    if oc['name'] == home: odds['1'] = max(odds.get('1', 0), float(oc['price']))
                    elif oc['name'] == away: odds['2'] = max(odds.get('2', 0), float(oc['price']))
                    elif oc['name'] == 'Draw': odds['X'] = max(odds.get('X', 0), float(oc['price']))
            elif mkt['key'] == 'totals':
                for oc in mkt['outcomes']:
                    pt = oc.get('point')
                    name = oc.get('name')
                    pr = float(oc.get('price', 0))
                    if pt == 1.5:
                        if name == 'Over': odds['over_1_5'] = max(odds.get('over_1_5', 0), pr)
                        elif name == 'Under': odds['under_1_5'] = max(odds.get('under_1_5', 0), pr)
                    elif pt == 2.5:
                        if name == 'Over': odds['over_2_5'] = max(odds.get('over_2_5', 0), pr)
                        elif name == 'Under': odds['under_2_5'] = max(odds.get('under_2_5', 0), pr)
                    elif pt == 3.5:
                        if name == 'Over': odds['over_3_5'] = max(odds.get('over_3_5', 0), pr)
                        elif name == 'Under': odds['under_3_5'] = max(odds.get('under_3_5', 0), pr)
    
    # xG baseline derived from Elo & league power
    elo_h = get_elo(home)
    elo_a = get_elo(away)
    diff = (elo_h + 100 - elo_a) / 400.0
    base_xg_h = max(0.6, min(3.5, 1.45 + diff * 0.8))
    base_xg_a = max(0.4, min(3.0, 1.15 - diff * 0.6))
    
    match_dict = {
        'match': f'{home} vs {away}',
        'league': 'UEFA Europa League',
        'home_team': home,
        'away_team': away,
        'xg_home_for': round(base_xg_h, 2),
        'xg_home_against': round(base_xg_a * 0.9, 2),
        'xg_away_for': round(base_xg_a, 2),
        'xg_away_against': round(base_xg_h * 1.1, 2),
        'elo_home': elo_h,
        'elo_away': elo_a,
        'odds': odds,
        'corners_home_for': None,
        'corners_home_against': None,
        'corners_away_for': None,
        'corners_away_against': None,
        'cards_home_for': None,
        'cards_home_against': None,
        'cards_away_for': None,
        'cards_away_against': None
    }
    res = run_ensemble(match_dict, cfg)
    res['league'] = 'UEFA Europa League'
    all_results.append(res)
    for m_key, evl in res['evaluations'].items():
        full = dict(evl)
        full['match'] = res['match']
        full['league'] = 'UEFA Europa League'
        full['home_team'] = home
        full['away_team'] = away
        all_evaluations.append(full)
        if evl['has_value']:
            all_candidates.append(full)

for item in uecl_odds:
    home = item['home_team']
    away = item['away_team']
    commence = item['commence_time']
    uecl_list.append(f'{home} vs {away}')
    
    odds = {}
    for bm in item['bookmakers']:
        for mkt in bm['markets']:
            if mkt['key'] == 'h2h':
                for oc in mkt['outcomes']:
                    if oc['name'] == home: odds['1'] = max(odds.get('1', 0), float(oc['price']))
                    elif oc['name'] == away: odds['2'] = max(odds.get('2', 0), float(oc['price']))
                    elif oc['name'] == 'Draw': odds['X'] = max(odds.get('X', 0), float(oc['price']))
            elif mkt['key'] == 'totals':
                for oc in mkt['outcomes']:
                    pt = oc.get('point')
                    name = oc.get('name')
                    pr = float(oc.get('price', 0))
                    if pt == 1.5:
                        if name == 'Over': odds['over_1_5'] = max(odds.get('over_1_5', 0), pr)
                        elif name == 'Under': odds['under_1_5'] = max(odds.get('under_1_5', 0), pr)
                    elif pt == 2.5:
                        if name == 'Over': odds['over_2_5'] = max(odds.get('over_2_5', 0), pr)
                        elif name == 'Under': odds['under_2_5'] = max(odds.get('under_2_5', 0), pr)
                    elif pt == 3.5:
                        if name == 'Over': odds['over_3_5'] = max(odds.get('over_3_5', 0), pr)
                        elif name == 'Under': odds['under_3_5'] = max(odds.get('under_3_5', 0), pr)
                        
    elo_h = get_elo(home)
    elo_a = get_elo(away)
    diff = (elo_h + 100 - elo_a) / 400.0
    base_xg_h = max(0.6, min(3.5, 1.40 + diff * 0.8))
    base_xg_a = max(0.4, min(3.0, 1.10 - diff * 0.6))
    
    match_dict = {
        'match': f'{home} vs {away}',
        'league': 'UEFA Conference League',
        'home_team': home,
        'away_team': away,
        'xg_home_for': round(base_xg_h, 2),
        'xg_home_against': round(base_xg_a * 0.9, 2),
        'xg_away_for': round(base_xg_a, 2),
        'xg_away_against': round(base_xg_h * 1.1, 2),
        'elo_home': elo_h,
        'elo_away': elo_a,
        'odds': odds,
        'corners_home_for': None,
        'corners_home_against': None,
        'corners_away_for': None,
        'corners_away_against': None,
        'cards_home_for': None,
        'cards_home_against': None,
        'cards_away_for': None,
        'cards_away_against': None
    }
    res = run_ensemble(match_dict, cfg)
    res['league'] = 'UEFA Conference League'
    all_results.append(res)
    for m_key, evl in res['evaluations'].items():
        full = dict(evl)
        full['match'] = res['match']
        full['league'] = 'UEFA Conference League'
        full['home_team'] = home
        full['away_team'] = away
        all_evaluations.append(full)
        if evl['has_value']:
            all_candidates.append(full)

selected, excluded = select_portfolio(all_candidates, max_picks=6)

res_payload = {
    'all_results': all_results,
    'all_candidates': all_candidates,
    'all_evaluations': all_evaluations,
    'selected': selected,
    'excluded': excluded
}

with open(SCRATCH / 'oct22_results.json', 'w') as f:
    json.dump(res_payload, f, indent=2)

print(f'Done! Universe matches: {len(all_results)}. Candidates with value: {len(all_candidates)}. Selected: {len(selected)}.')
for i, s in enumerate(selected, 1):
    print(f"{i}. {s['match']} | {s['market']} | odds: {s['odds']} | prob: {s['model_prob']*100:.1f}% | robust_ev: {s['robust_ev_percent']:.2f}%")
