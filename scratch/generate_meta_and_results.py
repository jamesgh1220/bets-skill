import json

match_keys = [
    'barca_madrid', 'freiburg_bayern', 'inter_fiorentina', 'liverpool_brighton',
    'psv_feyenoord', 'sporting_viseu', 'monaco_lille', 'nacional_dim',
    'river_racing', 'lafc_galaxy'
]

all_results = []
all_evaluations = []

# Map to store home_team and away_team
team_map = {
    "Barcelona vs Real Madrid": ("Barcelona", "Real Madrid"),
    "SC Freiburg vs Bayern Munich": ("SC Freiburg", "Bayern Munich"),
    "Inter Milan vs Fiorentina": ("Inter Milan", "Fiorentina"),
    "Liverpool vs Brighton": ("Liverpool", "Brighton"),
    "PSV Eindhoven vs Feyenoord": ("PSV Eindhoven", "Feyenoord"),
    "Sporting CP vs Academico de Viseu": ("Sporting CP", "Academico de Viseu"),
    "AS Monaco vs LOSC Lille": ("AS Monaco", "LOSC Lille"),
    "Atletico Nacional vs Independiente Medellin": ("Atletico Nacional", "Independiente Medellin"),
    "River Plate vs Racing Club": ("River Plate", "Racing Club"),
    "LAFC vs LA Galaxy": ("LAFC", "LA Galaxy")
}

for k in match_keys:
    with open(f"scratch/output_{k}.json") as f:
        data = json.load(f)
        all_results.append(data)
        mname = data['match']
        ht, at = team_map[mname]
        for mkt, ev in data.get('evaluations', {}).items():
            item = dict(ev)
            item['match'] = mname
            item['home_team'] = ht
            item['away_team'] = at
            all_evaluations.append(item)

def get_eval(mid_sub, mkt):
    for item in all_evaluations:
        if mid_sub.lower() in item['match'].lower() and item['market'] == mkt:
            return dict(item)
    return None

picks_info = [
    ("Liverpool", "over_2_5", 0.75, "Media-Alta", "Fuerte volumen ofensivo de ambos equipos (Liverpool xG 1.95 y Brighton xG 1.65). Ritmo abierto esperado en Anfield.", "Rotaciones imprevistas o falta de puntería temprana."),
    ("Monaco", "over_2_5", 0.50, "Media-Alta", "Monaco y Lille llegan empatados con alta producción ofensiva en Ligue 1. Probabilidad modelo 66.5% supera holgadamente cuota 1.75.", "Planteamiento especulativo de Lille jugando de visitante."),
    ("River", "over_2_5", 0.50, "Media-Alta", "El Monumental favorece transiciones rápidas ante una defensa de Racing permeable. Edge de +17.84% y prob 60.4%.", "Clásico cerrado con excesiva fricción en mediocampo."),
    ("Nacional", "over_2_5", 0.50, "Media", "Clásico Paisa con ambos equipos necesitados de consolidar puesto en cuadrangulares; historial reciente directo con 3+ goles.", "Condiciones climáticas adversas o interrupciones por faltas."),
    ("Barcelona", "over_2_5", 0.50, "Media-Alta", "El Clásico presenta los dos ataques más letales de España (xG conjunto superior a 3.90). Cuota 1.50 con prob 75.4%.", "Estrategia de repliegue bajo y bloque bajo de Real Madrid."),
    ("PSV", "over_2_5", 0.50, "Media-Alta", "De Kraker enfrenta a las dos ofensivas más goleadoras de los Países Bajos; modelo proyecta 79.5% de probabilidad de 3+ goles.", "Feyenoord priorizando bloque defensivo para cuidar el liderato.")
]

selected = []
all_candidates = []
picks_details = []

for mid, mkt, stake, conf, reasons, risks in picks_info:
    c = get_eval(mid, mkt)
    c['stake_recommended_units'] = stake
    c['selection_profile'] = 'prioritario'
    c['confidence'] = conf
    selected.append(c)
    all_candidates.append(c)
    picks_details.append({
        "match": c['match'],
        "market": c['market'],
        "conf": conf,
        "why": reasons,
        "risks": risks,
        "sources": "Odds-API (Pinnacle / Betsson), SofaScore, FlashScore",
        "incertidumbre": "Base +/- 5.0%"
    })

excluded = []

# Exclude LAFC over 2.5
lafc_ov = get_eval("LAFC", "over_2_5")
if lafc_ov:
    c = dict(lafc_ov)
    c['selection_profile'] = 'excluido'
    c['selection_reason'] = 'Excluido por límite de 6 picks de máxima calidad en portfolio y balance de ligas.'
    all_candidates.append(c)
    excluded.append(c)

# Exclude Barcelona X
barca_x = get_eval("Barcelona", "X")
if barca_x:
    c = dict(barca_x)
    c['selection_profile'] = 'excluido'
    c['selection_reason'] = 'EV robusto negativo (-1.67%) tras penalización por incertidumbre.'
    all_candidates.append(c)
    excluded.append(c)

# Exclude LAFC 2
lafc_2 = get_eval("LAFC", "2")
if lafc_2:
    c = dict(lafc_2)
    c['selection_profile'] = 'excluido'
    c['selection_reason'] = 'Probabilidad modelo (26.0%) inferior al umbral mínimo del 30% requerido para longshots.'
    all_candidates.append(c)
    excluded.append(c)

results_data = {
    "all_results": all_results,
    "all_candidates": all_candidates,
    "all_evaluations": all_evaluations,
    "selected": selected,
    "excluded": excluded
}

meta_data = {
    "analysis_date_iso": "2026-10-25",
    "match_dates_text": "25 de octubre de 2026",
    "information_cutoff": "2026-10-25 07:24 UTC",
    "model_ia": "gemini3.8flash",
    "engine_version": "v1.2",
    "leagues_display": "Bundesliga, Liga Argentina, Liga Colombiana, Liga Española, MLS, Ligue 1, Premier League, Serie A, Eredivisie, Liga Portugal",
    "requested_range": "2026-10-25",
    "universe_preamble": "Universo construido por intersección estricta de las 10 ligas solicitadas en la fecha 25 de octubre de 2026:",
    "universe_matches": [
        "- **La Liga**: Barcelona vs Real Madrid (Camp Nou)",
        "- **Bundesliga**: SC Freiburg vs Bayern Munich (Europa-Park Stadion)",
        "- **Serie A**: Inter Milan vs Fiorentina (San Siro)",
        "- **Premier League**: Liverpool vs Brighton (Anfield)",
        "- **Eredivisie**: PSV Eindhoven vs Feyenoord (Philips Stadion)",
        "- **Liga Portugal**: Sporting CP vs Academico de Viseu (Estadio Jose Alvalade)",
        "- **Ligue 1**: AS Monaco vs LOSC Lille (Stade Louis II)",
        "- **Liga Colombiana**: Atletico Nacional vs Independiente Medellin (Atanasio Girardot)",
        "- **Liga Argentina**: River Plate vs Racing Club (Mas Monumental)",
        "- **MLS**: LAFC vs LA Galaxy (BMO Stadium)"
    ],
    "picks_details": picks_details
}

with open("scratch/results_25oct.json", "w") as f:
    json.dump(results_data, f, indent=2)

with open("scratch/meta_25oct.json", "w") as f:
    json.dump(meta_data, f, indent=2)

print("Generated complete meta and results JSON.")
