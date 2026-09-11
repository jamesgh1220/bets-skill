import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

MATCHES = {
    "01_union_schalke": {
        "home_team": "Union Berlin",
        "away_team": "Schalke 04",
        "xg_home_for": 1.65,
        "xg_home_against": 1.45,
        "xg_away_for": 1.05,
        "xg_away_against": 1.55,
        "elo_home": 1540,
        "elo_away": 1450,
        "odds": {
            "1": 2.11, "X": 3.73, "2": 3.23, "over_2_5": 1.60
        }
    },
    "02_sevilla_valencia": {
        "home_team": "Sevilla",
        "away_team": "Valencia",
        "xg_home_for": 1.55,
        "xg_home_against": 1.35,
        "xg_away_for": 0.95,
        "xg_away_against": 1.90,
        "elo_home": 1610,
        "elo_away": 1560,
        "odds": {
            "1": 2.35, "X": 3.09, "2": 3.32,
            "over_2_5": 2.35, "under_2_5": 1.65,
            "btts_yes": 2.00, "btts_no": 1.75,
            "1x": 1.29, "x2": 1.67
        }
    },
    "03_venezia_fiorentina": {
        "home_team": "Venezia",
        "away_team": "Fiorentina",
        "xg_home_for": 1.20,
        "xg_home_against": 1.55,
        "xg_away_for": 1.35,
        "xg_away_against": 1.75,
        "elo_home": 1430,
        "elo_away": 1550,
        "odds": {
            "1": 2.74, "X": 3.41, "2": 2.56,
            "over_2_5": 1.90,
            "over_1_5": 1.27,
            "btts_yes": 1.66
        }
    },
    "04_rennes_marseille": {
        "home_team": "Rennes",
        "away_team": "Marseille",
        "xg_home_for": 1.80,
        "xg_home_against": 1.20,
        "xg_away_for": 1.55,
        "xg_away_against": 1.30,
        "elo_home": 1605,
        "elo_away": 1640,
        "odds": {
            "1": 2.29, "X": 4.01, "2": 2.74,
            "over_2_5": 1.57, "over_3_5": 2.35,
            "btts_yes": 1.50
        }
    },
    "05_az_willem": {
        "home_team": "AZ Alkmaar",
        "away_team": "Willem II",
        "xg_home_for": 2.30,
        "xg_home_against": 1.00,
        "xg_away_for": 1.05,
        "xg_away_against": 1.80,
        "elo_home": 1730,
        "elo_away": 1440,
        "odds": {
            "1": 1.13, "X": 9.55, "2": 20.00,
            "over_2_5": 1.26, "under_2_5": 3.30,
            "btts_yes": 1.90, "btts_no": 1.80
        }
    },
    "06_newells_velez": {
        "home_team": "Newell's Old Boys",
        "away_team": "Vélez Sarsfield",
        "xg_home_for": 1.05,
        "xg_home_against": 1.20,
        "xg_away_for": 1.10,
        "xg_away_against": 1.00,
        "elo_home": 1520,
        "elo_away": 1580,
        "odds": {
            "1": 2.70, "X": 2.90, "2": 2.80,
            "over_2_5": 2.60
        }
    },
    "07_defensa_gimnasiamza": {
        "home_team": "Defensa y Justicia",
        "away_team": "Gimnasia (Mendoza)",
        "xg_home_for": 1.20,
        "xg_home_against": 1.15,
        "xg_away_for": 1.35,
        "xg_away_against": 1.25,
        "elo_home": 1510,
        "elo_away": 1450,
        "odds": {
            "1": 2.05, "X": 3.30, "2": 3.60,
            "over_1_5": 1.44, "over_2_5": 2.35, "under_2_5": 1.57,
            "btts_yes": 2.00, "btts_no": 1.75,
            "1x": 1.29, "x2": 1.70
        }
    },
    "08_boca_ccordoba": {
        "home_team": "Boca Juniors",
        "away_team": "Central Córdoba (SdE)",
        "xg_home_for": 1.75,
        "xg_home_against": 0.95,
        "xg_away_for": 0.90,
        "xg_away_against": 2.00,
        "elo_home": 1700,
        "elo_away": 1410,
        "odds": {
            "1": 1.35, "X": 4.58, "2": 10.40,
            "under_2_5": 1.73
        }
    },
    "09_jaguares_fortaleza": {
        "home_team": "Jaguares",
        "away_team": "Fortaleza",
        "xg_home_for": 1.10,
        "xg_home_against": 1.60,
        "xg_away_for": 1.20,
        "xg_away_against": 1.40,
        "elo_home": 1380,
        "elo_away": 1450,
        "odds": {
            "1": 2.33, "X": 2.83, "2": 3.25
        }
    },
    "10_santafe_tolima": {
        "home_team": "Independiente Santa Fe",
        "away_team": "Deportes Tolima",
        "xg_home_for": 1.45,
        "xg_home_against": 1.10,
        "xg_away_for": 1.50,
        "xg_away_against": 1.20,
        "elo_home": 1570,
        "elo_away": 1550,
        "odds": {
            "1": 2.32, "X": 3.03, "2": 3.32
        }
    }
}

for name, data in MATCHES.items():
    with open(os.path.join(BASE, f"input_{name}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"generated {len(MATCHES)} inputs")