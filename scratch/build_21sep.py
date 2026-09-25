import json, os, subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(BASE, "..", "models", "model-v1.3.json")

def build(filename, data):
    path = os.path.join(BASE, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    out = path.replace("_input_", "_output_")
    subprocess.run(["python3", "calc_engine.py", "--config", CONFIG,
                    "--input", path, "--output", out], cwd=os.path.join(BASE, "..", "scripts"), check=True)
    print("OK", filename)

# Match 1: Lanús vs Estudiantes de La Plata (Zona A, 21.09 21:15 ART / 00:15 UTC)
lan = {
  "home_team": "Lanús", "away_team": "Estudiantes de La Plata",
  "league": "Liga Profesional Argentina (Clausura Zona A, J10)",
  "match_date": "2026-09-21",
  "xg_home_for": 1.47, "xg_home_against": 1.50,
  "xg_away_for": 1.61, "xg_away_against": 1.29,
  "elo_home": 1695, "elo_away": 1729,
  "corners_home_for": 7.4, "corners_home_against": 4.0,
  "corners_away_for": 2.9, "corners_away_against": 4.7,
  "cards_home_for": 2.2, "cards_home_against": 2.0,
  "cards_away_for": 2.85, "cards_away_against": 2.69,
  "odds": {
    "1": 2.30, "X": 3.24, "2": 3.77,
    "over_1_5": 1.80, "under_1_5": 2.00,
    "over_2_5": 2.87, "under_2_5": 1.37,
    "over_3_5": 6.00, "under_3_5": 1.10,
    "btts_yes": 2.25, "btts_no": 1.57,
    "1x": 1.29, "x2": 1.62, "12": 1.40,
    "dnb_home": 1.50, "dnb_away": 2.50
  }
}

# Match 2: Barracas Central vs Independiente Rivadavia (Zona B, 19:00 ART / 22:00 UTC)
bar = {
  "home_team": "Barracas Central", "away_team": "Independiente Rivadavia",
  "league": "Liga Profesional Argentina (Clausura Zona B, J10)",
  "match_date": "2026-09-21",
  "xg_home_for": 1.27, "xg_home_against": 1.68,
  "xg_away_for": 1.64, "xg_away_against": 1.35,
  "elo_home": 1624, "elo_away": 1735,
  "corners_home_for": 3.08, "corners_home_against": 5.20,
  "corners_away_for": 4.57, "corners_away_against": 3.81,
  "cards_home_for": 2.38, "cards_home_against": 1.67,
  "cards_away_for": 1.67, "cards_away_against": 2.38,
  "odds": {
    "1": 3.40, "X": 3.05, "2": 2.41,
    "over_1_5": 1.50, "under_1_5": 2.50,
    "over_2_5": 2.60, "under_2_5": 1.48,
    "over_3_5": 5.50, "under_3_5": 1.14,
    "btts_yes": 2.10, "btts_no": 1.67
  }
}

# Match 3: Bogotá FC vs Barranquilla FC (Primera B COL, 15:30 COT / 20:30 UTC)
bog = {
  "home_team": "Bogotá F.C.", "away_team": "Barranquilla F.C.",
  "league": "Primera B Colombia (Torneo BetPlay Finalización, J10)",
  "match_date": "2026-09-21",
  "xg_home_for": 1.45, "xg_home_against": 1.46,
  "xg_away_for": 1.47, "xg_away_against": 1.57,
  "elo_home": 1460, "elo_away": 1480,
  "corners_home_for": 4.68, "corners_home_against": 3.86,
  "corners_away_for": 3.96, "corners_away_against": 4.63,
  "cards_home_for": 1.21, "cards_home_against": 1.10,
  "cards_away_for": 1.10, "cards_away_against": 1.21,
  "odds": {
    "1": 1.73, "X": 3.70, "2": 4.50,
    "over_2_5": 1.99, "under_2_5": 1.92,
    "over_3_5": 3.60, "under_3_5": 1.35
  }
}

# Match 4: Real Cundinamarca (Real Soacha) vs Deportes Quindío (17:00 COT / 22:00 UTC)
soa = {
  "home_team": "Real Cundinamarca", "away_team": "Deportes Quindío",
  "league": "Primera B Colombia (Torneo BetPlay Finalización, J10)",
  "match_date": "2026-09-21",
  "xg_home_for": 1.52, "xg_home_against": 1.46,
  "xg_away_for": 1.35, "xg_away_against": 1.33,
  "elo_home": 1455, "elo_away": 1510,
  "corners_home_for": 4.2, "corners_home_against": 4.2,
  "corners_away_for": 5.0, "corners_away_against": 5.1,
  "cards_home_for": 1.30, "cards_home_against": 1.97,
  "cards_away_for": 1.97, "cards_away_against": 1.30,
  "odds": {
    "1": 2.20, "X": 3.15, "2": 3.90,
    "over_2_5": 2.44, "under_2_5": 1.64,
    "over_3_5": 4.80, "under_3_5": 1.24
  }
}

# Match 5: Real Cartagena vs Envigado (19:30 COT / 00:30 UTC)
car = {
  "home_team": "Real Cartagena", "away_team": "Envigado FC",
  "league": "Primera B Colombia (Torneo BetPlay Finalización, J10)",
  "match_date": "2026-09-21",
  "xg_home_for": 1.70, "xg_home_against": 1.38,
  "xg_away_for": 1.45, "xg_away_against": 1.53,
  "elo_home": 1520, "elo_away": 1505,
  "corners_home_for": 5.4, "corners_home_against": 4.45,
  "corners_away_for": 3.91, "corners_away_against": 6.3,
  "cards_home_for": 2.0, "cards_home_against": 2.75,
  "cards_away_for": 2.55, "cards_away_against": 2.2,
  "odds": {
    "1": 1.75, "X": 3.50, "2": 5.10,
    "over_2_5": 1.97, "under_2_5": 1.77,
    "over_3_5": 3.10, "under_3_5": 1.33,
    "x2": 1.95
  }
}

for name, data in [("match_input_lanus_estudiantes.json", lan),
                   ("match_input_barracas_rivadavia.json", bar),
                   ("match_input_bogota_barranquilla.json", bog),
                   ("match_input_cundinamarca_quindio.json", soa),
                   ("match_input_cartagena_envigado.json", car)]:
    build(name, data)