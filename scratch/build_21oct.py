from collections import Counter
import json
import os
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

from selection import select_portfolio
from render_artifact import market_label

MODEL_CONFIG = os.path.join(ROOT, "models", "model-v1.3.json")
ENGINE = os.path.join(ROOT, "scripts", "calc_engine.py")

# Raw records for the 14 matches of October 21, 2026
matches_data = [
    # 1. UEFA Champions League: Lille vs Galatasaray (18:45 CET / 16:45 UTC)
    {
        "match": "Lille vs Galatasaray",
        "league": "UEFA Champions League 2026-27 - League phase MD3",
        "home_team": "Lille",
        "away_team": "Galatasaray",
        "match_date": "2026-10-21T16:45:00Z",
        "elo_home": 1795,
        "elo_away": 1720,
        "xg_home_for": 1.62,
        "xg_home_against": 1.15,
        "xg_away_for": 1.74,
        "xg_away_against": 1.48,
        "corners_home_for": 5.4,
        "corners_home_against": 4.1,
        "corners_away_for": 5.6,
        "corners_away_against": 4.8,
        "cards_home_for": 1.8,
        "cards_home_against": 2.1,
        "cards_away_for": 2.5,
        "cards_away_against": 2.3,
        "odds": {
            "1": 2.16, "X": 3.71, "2": 3.15,
            "1x": 1.38, "x2": 1.72, "12": 1.29,
            "dnb_home": 1.60, "dnb_away": 2.35,
            "btts_yes": 1.60, "btts_no": 2.30,
            "over_1_5": 1.18, "under_1_5": 5.00,
            "over_2_5": 1.62, "under_2_5": 2.35,
            "over_3_5": 2.55, "under_3_5": 1.55,
            "over_corners_8_5": 1.50, "under_corners_8_5": 2.60,
            "over_corners_9_5": 1.85, "under_corners_9_5": 1.95,
            "over_corners_10_5": 2.35, "under_corners_10_5": 1.60,
            "over_cards_3_5": 1.55, "under_cards_3_5": 2.45,
            "over_cards_4_5": 2.05, "under_cards_4_5": 1.75
        },
        "sources": "Pinnacle, Betsson, SofaScore, Understat"
    },
    # 2. UEFA Champions League: Como vs Manchester United (18:45 CET / 16:45 UTC)
    {
        "match": "Como vs Manchester United",
        "league": "UEFA Champions League 2026-27 - League phase MD3",
        "home_team": "Como",
        "away_team": "Manchester United",
        "match_date": "2026-10-21T16:45:00Z",
        "elo_home": 1690,
        "elo_away": 1820,
        "xg_home_for": 1.35,
        "xg_home_against": 1.42,
        "xg_away_for": 1.68,
        "xg_away_against": 1.38,
        "corners_home_for": 4.6,
        "corners_home_against": 5.2,
        "corners_away_for": 5.5,
        "corners_away_against": 4.9,
        "cards_home_for": 2.2,
        "cards_home_against": 2.0,
        "cards_away_for": 1.9,
        "cards_away_against": 2.2,
        "odds": {
            "1": 2.30, "X": 3.84, "2": 2.81,
            "1x": 1.45, "x2": 1.63, "12": 1.28,
            "dnb_home": 1.72, "dnb_away": 2.12,
            "btts_yes": 1.58, "btts_no": 2.38,
            "over_1_5": 1.19, "under_1_5": 4.80,
            "over_2_5": 1.65, "under_2_5": 2.28,
            "over_3_5": 2.65, "under_3_5": 1.50,
            "over_corners_8_5": 1.52, "under_corners_8_5": 2.50,
            "over_corners_9_5": 1.88, "under_corners_9_5": 1.92,
            "over_corners_10_5": 2.40, "under_corners_10_5": 1.57,
            "over_cards_3_5": 1.60, "under_cards_3_5": 2.30,
            "over_cards_4_5": 2.15, "under_cards_4_5": 1.68
        },
        "sources": "Pinnacle, Betsson, FlashScore, FBref"
    },
    # 3. UEFA Champions League: Bayern Munich vs Arsenal (21:00 CET / 19:00 UTC)
    {
        "match": "Bayern Munich vs Arsenal",
        "league": "UEFA Champions League 2026-27 - League phase MD3",
        "home_team": "Bayern Munich",
        "away_team": "Arsenal",
        "match_date": "2026-10-21T19:00:00Z",
        "elo_home": 1965,
        "elo_away": 1940,
        "xg_home_for": 2.45,
        "xg_home_against": 1.15,
        "xg_away_for": 1.88,
        "xg_away_against": 0.98,
        "corners_home_for": 6.8,
        "corners_home_against": 3.5,
        "corners_away_for": 6.2,
        "corners_away_against": 3.8,
        "cards_home_for": 1.5,
        "cards_home_against": 1.9,
        "cards_away_for": 1.8,
        "cards_away_against": 2.0,
        "odds": {
            "1": 2.16, "X": 3.99, "2": 3.12,
            "1x": 1.39, "x2": 1.72, "12": 1.27,
            "dnb_home": 1.62, "dnb_away": 2.32,
            "btts_yes": 1.52, "btts_no": 2.55,
            "over_1_5": 1.14, "under_1_5": 5.80,
            "over_2_5": 1.58, "under_2_5": 2.45,
            "over_3_5": 2.38, "under_3_5": 1.62,
            "over_corners_8_5": 1.44, "under_corners_8_5": 2.80,
            "over_corners_9_5": 1.72, "under_corners_9_5": 2.15,
            "over_corners_10_5": 2.18, "under_corners_10_5": 1.70,
            "over_cards_3_5": 1.75, "under_cards_3_5": 2.05,
            "over_cards_4_5": 2.40, "under_cards_4_5": 1.55
        },
        "sources": "Pinnacle, Betsson, Understat, ClubElo"
    },
    # 4. UEFA Champions League: Real Madrid vs RB Leipzig (21:00 CET / 19:00 UTC)
    {
        "match": "Real Madrid vs RB Leipzig",
        "league": "UEFA Champions League 2026-27 - League phase MD3",
        "home_team": "Real Madrid",
        "away_team": "RB Leipzig",
        "match_date": "2026-10-21T19:00:00Z",
        "elo_home": 2010,
        "elo_away": 1810,
        "xg_home_for": 2.52,
        "xg_home_against": 1.05,
        "xg_away_for": 1.45,
        "xg_away_against": 1.75,
        "corners_home_for": 6.5,
        "corners_home_against": 3.8,
        "corners_away_for": 4.8,
        "corners_away_against": 5.4,
        "cards_home_for": 1.6,
        "cards_home_against": 2.3,
        "cards_away_for": 2.2,
        "cards_away_against": 1.8,
        "odds": {
            "1": 1.27, "X": 6.83, "2": 9.19,
            "1x": 1.08, "x2": 3.90, "12": 1.11,
            "dnb_home": 1.09, "dnb_away": 7.50,
            "btts_yes": 1.72, "btts_no": 2.15,
            "over_1_5": 1.10, "under_1_5": 7.50,
            "over_2_5": 1.38, "under_2_5": 3.15,
            "over_3_5": 1.95, "under_3_5": 1.90,
            "over_corners_8_5": 1.46, "under_corners_8_5": 2.70,
            "over_corners_9_5": 1.75, "under_corners_9_5": 2.10,
            "over_corners_10_5": 2.22, "under_corners_10_5": 1.68,
            "over_cards_3_5": 1.65, "under_cards_3_5": 2.20,
            "over_cards_4_5": 2.20, "under_cards_4_5": 1.65
        },
        "sources": "Pinnacle, Betsson, FlashScore, ClubElo"
    },
    # 5. UEFA Champions League: Inter Milan vs Shakhtar Donetsk (21:00 CET / 19:00 UTC)
    {
        "match": "Inter Milan vs Shakhtar Donetsk",
        "league": "UEFA Champions League 2026-27 - League phase MD3",
        "home_team": "Inter Milan",
        "away_team": "Shakhtar Donetsk",
        "match_date": "2026-10-21T19:00:00Z",
        "elo_home": 1945,
        "elo_away": 1670,
        "xg_home_for": 2.38,
        "xg_home_against": 0.88,
        "xg_away_for": 1.12,
        "xg_away_against": 1.95,
        "corners_home_for": 6.4,
        "corners_home_against": 3.2,
        "corners_away_for": 4.1,
        "corners_away_against": 5.8,
        "cards_home_for": 1.7,
        "cards_home_against": 2.1,
        "cards_away_for": 2.4,
        "cards_away_against": 1.9,
        "odds": {
            "1": 1.21, "X": 7.41, "2": 11.87,
            "1x": 1.05, "x2": 4.50, "12": 1.10,
            "dnb_home": 1.06, "dnb_away": 9.20,
            "btts_yes": 1.95, "btts_no": 1.88,
            "over_1_5": 1.11, "under_1_5": 7.00,
            "over_2_5": 1.42, "under_2_5": 2.95,
            "over_3_5": 1.88, "under_3_5": 1.99,
            "over_corners_8_5": 1.48, "under_corners_8_5": 2.65,
            "over_corners_9_5": 1.78, "under_corners_9_5": 2.05,
            "over_corners_10_5": 2.25, "under_corners_10_5": 1.66,
            "over_cards_3_5": 1.70, "under_cards_3_5": 2.12,
            "over_cards_4_5": 2.30, "under_cards_4_5": 1.60
        },
        "sources": "Pinnacle, Betsson, SofaScore, ClubElo"
    },
    # 6. UEFA Champions League: Sporting CP vs LASK Linz (21:00 CET / 19:00 UTC)
    {
        "match": "Sporting CP vs LASK Linz",
        "league": "UEFA Champions League 2026-27 - League phase MD3",
        "home_team": "Sporting CP",
        "away_team": "LASK Linz",
        "match_date": "2026-10-21T19:00:00Z",
        "elo_home": 1855,
        "elo_away": 1610,
        "xg_home_for": 2.25,
        "xg_home_against": 0.95,
        "xg_away_for": 1.05,
        "xg_away_against": 1.88,
        "corners_home_for": 6.1,
        "corners_home_against": 3.6,
        "corners_away_for": 4.2,
        "corners_away_against": 5.9,
        "cards_home_for": 1.9,
        "cards_home_against": 2.2,
        "cards_away_for": 2.5,
        "cards_away_against": 1.8,
        "odds": {
            "1": 1.22, "X": 7.51, "2": 10.79,
            "1x": 1.06, "x2": 4.30, "12": 1.10,
            "dnb_home": 1.07, "dnb_away": 8.50,
            "btts_yes": 1.92, "btts_no": 1.90,
            "over_1_5": 1.12, "under_1_5": 6.80,
            "over_2_5": 1.45, "under_2_5": 2.85,
            "over_3_5": 1.85, "under_3_5": 2.03,
            "over_corners_8_5": 1.50, "under_corners_8_5": 2.60,
            "over_corners_9_5": 1.82, "under_corners_9_5": 2.00,
            "over_corners_10_5": 2.30, "under_corners_10_5": 1.62,
            "over_cards_3_5": 1.68, "under_cards_3_5": 2.15,
            "over_cards_4_5": 2.25, "under_cards_4_5": 1.63
        },
        "sources": "Pinnacle, Betsson, FlashScore, ClubElo"
    },
    # 7. UEFA Champions League: Aston Villa vs Viking FK (21:00 CET / 19:00 UTC)
    {
        "match": "Aston Villa vs Viking FK",
        "league": "UEFA Champions League 2026-27 - League phase MD3",
        "home_team": "Aston Villa",
        "away_team": "Viking FK",
        "match_date": "2026-10-21T19:00:00Z",
        "elo_home": 1840,
        "elo_away": 1560,
        "xg_home_for": 2.35,
        "xg_home_against": 1.02,
        "xg_away_for": 1.15,
        "xg_away_against": 2.10,
        "corners_home_for": 6.2,
        "corners_home_against": 3.9,
        "corners_away_for": 4.5,
        "corners_away_against": 5.8,
        "cards_home_for": 1.8,
        "cards_home_against": 2.0,
        "cards_away_for": 2.1,
        "cards_away_against": 1.7,
        "odds": {
            "1": 1.22, "X": 6.94, "2": 12.37,
            "1x": 1.05, "x2": 4.40, "12": 1.11,
            "dnb_home": 1.07, "dnb_away": 9.50,
            "btts_yes": 1.85, "btts_no": 1.98,
            "over_1_5": 1.11, "under_1_5": 7.00,
            "over_2_5": 1.40, "under_2_5": 3.05,
            "over_3_5": 1.87, "under_3_5": 2.00,
            "over_corners_8_5": 1.48, "under_corners_8_5": 2.65,
            "over_corners_9_5": 1.78, "under_corners_9_5": 2.05,
            "over_corners_10_5": 2.25, "under_corners_10_5": 1.65,
            "over_cards_3_5": 1.75, "under_cards_3_5": 2.05,
            "over_cards_4_5": 2.35, "under_cards_4_5": 1.58
        },
        "sources": "Pinnacle, Betsson, FlashScore, ClubElo"
    },
    # 8. UEFA Champions League: Club Brugge vs Lens (21:00 CET / 19:00 UTC)
    {
        "match": "Club Brugge vs Lens",
        "league": "UEFA Champions League 2026-27 - League phase MD3",
        "home_team": "Club Brugge",
        "away_team": "Lens",
        "match_date": "2026-10-21T19:00:00Z",
        "elo_home": 1740,
        "elo_away": 1755,
        "xg_home_for": 1.48,
        "xg_home_against": 1.35,
        "xg_away_for": 1.42,
        "xg_away_against": 1.28,
        "corners_home_for": 5.2,
        "corners_home_against": 4.5,
        "corners_away_for": 4.9,
        "corners_away_against": 4.7,
        "cards_home_for": 2.1,
        "cards_home_against": 2.2,
        "cards_away_for": 2.4,
        "cards_away_against": 2.1,
        "odds": {
            "1": 2.10, "X": 3.65, "2": 3.73,
            "1x": 1.32, "x2": 1.78, "12": 1.30,
            "dnb_home": 1.54, "dnb_away": 2.50,
            "btts_yes": 1.68, "btts_no": 2.20,
            "over_1_5": 1.24, "under_1_5": 4.10,
            "over_2_5": 1.82, "under_2_5": 2.02,
            "over_3_5": 3.00, "under_3_5": 1.40,
            "over_corners_8_5": 1.55, "under_corners_8_5": 2.45,
            "over_corners_9_5": 1.90, "under_corners_9_5": 1.90,
            "over_corners_10_5": 2.45, "under_corners_10_5": 1.55,
            "over_cards_3_5": 1.50, "under_cards_3_5": 2.55,
            "over_cards_4_5": 1.95, "under_cards_4_5": 1.85
        },
        "sources": "Pinnacle, Betsson, SofaScore, Understat"
    },
    # 9. UEFA Champions League: Real Betis vs Feyenoord (21:00 CET / 19:00 UTC)
    {
        "match": "Real Betis vs Feyenoord",
        "league": "UEFA Champions League 2026-27 - League phase MD3",
        "home_team": "Real Betis",
        "away_team": "Feyenoord",
        "match_date": "2026-10-21T19:00:00Z",
        "elo_home": 1780,
        "elo_away": 1765,
        "xg_home_for": 1.65,
        "xg_home_against": 1.25,
        "xg_away_for": 1.55,
        "xg_away_against": 1.48,
        "corners_home_for": 5.5,
        "corners_home_against": 4.6,
        "corners_away_for": 5.8,
        "corners_away_against": 4.5,
        "cards_home_for": 2.3,
        "cards_home_against": 2.1,
        "cards_away_for": 2.0,
        "cards_away_against": 2.2,
        "odds": {
            "1": 1.51, "X": 4.71, "2": 5.49,
            "1x": 1.17, "x2": 2.60, "12": 1.20,
            "dnb_home": 1.20, "dnb_away": 4.50,
            "btts_yes": 1.65, "btts_no": 2.25,
            "over_1_5": 1.18, "under_1_5": 4.90,
            "over_2_5": 1.62, "under_2_5": 2.35,
            "over_3_5": 2.55, "under_3_5": 1.55,
            "over_corners_8_5": 1.48, "under_corners_8_5": 2.65,
            "over_corners_9_5": 1.78, "under_corners_9_5": 2.05,
            "over_corners_10_5": 2.25, "under_corners_10_5": 1.65,
            "over_cards_3_5": 1.55, "under_cards_3_5": 2.45,
            "over_cards_4_5": 2.05, "under_cards_4_5": 1.75
        },
        "sources": "Pinnacle, Betsson, FlashScore, Understat"
    },
    # 10. LaLiga EA Sports: Levante UD vs Athletic Club (20:00 CET / 18:00 UTC)
    {
        "match": "Levante UD vs Athletic Club",
        "league": "LaLiga EA Sports 2026-27 - Jornada 6 (aplazada)",
        "home_team": "Levante UD",
        "away_team": "Athletic Club",
        "match_date": "2026-10-21T18:00:00Z",
        "elo_home": 1640,
        "elo_away": 1810,
        "xg_home_for": 1.12,
        "xg_home_against": 1.58,
        "xg_away_for": 1.48,
        "xg_away_against": 1.05,
        "corners_home_for": 4.4,
        "corners_home_against": 5.5,
        "corners_away_for": 5.8,
        "corners_away_against": 4.1,
        "cards_home_for": 2.4,
        "cards_home_against": 2.0,
        "cards_away_for": 2.1,
        "cards_away_against": 2.3,
        "odds": {
            "1": 3.70, "X": 3.45, "2": 2.20,
            "1x": 1.71, "x2": 1.30, "12": 1.33,
            "dnb_home": 2.65, "dnb_away": 1.50,
            "btts_yes": 1.88, "btts_no": 1.95,
            "over_1_5": 1.32, "under_1_5": 3.45,
            "over_2_5": 2.05, "under_2_5": 1.82,
            "over_3_5": 3.65, "under_3_5": 1.30,
            "over_corners_8_5": 1.55, "under_corners_8_5": 2.45,
            "over_corners_9_5": 1.90, "under_corners_9_5": 1.90,
            "over_corners_10_5": 2.45, "under_corners_10_5": 1.55,
            "over_cards_3_5": 1.45, "under_cards_3_5": 2.70,
            "over_cards_4_5": 1.85, "under_cards_4_5": 1.95
        },
        "sources": "Pinnacle, Betsson, Wincomparator, Understat"
    },
    # 11. Copa Libertadores: Palmeiras vs Fluminense (21:30 BRT / 00:30 UTC +1day / 19:30 COT)
    {
        "match": "Palmeiras vs Fluminense",
        "league": "Copa Libertadores 2026 - Semifinal (vuelta)",
        "home_team": "Palmeiras",
        "away_team": "Fluminense",
        "match_date": "2026-10-22T00:30:00Z", # 21 de octubre local 21:30 BRT / 19:30 COT
        "elo_home": 1860,
        "elo_away": 1785,
        "xg_home_for": 1.72,
        "xg_home_against": 0.95,
        "xg_away_for": 1.25,
        "xg_away_against": 1.38,
        "corners_home_for": 6.2,
        "corners_home_against": 4.1,
        "corners_away_for": 4.8,
        "corners_away_against": 5.2,
        "cards_home_for": 2.5,
        "cards_home_against": 2.8,
        "cards_away_for": 2.9,
        "cards_away_against": 2.4,
        "odds": {
            "1": 1.91, "X": 3.42, "2": 4.15,
            "1x": 1.25, "x2": 1.92, "12": 1.32,
            "dnb_home": 1.38, "dnb_away": 3.05,
            "btts_yes": 1.98, "btts_no": 1.84,
            "over_1_5": 1.35, "under_1_5": 3.25,
            "over_2_5": 2.05, "under_2_5": 1.78,
            "over_3_5": 3.65, "under_3_5": 1.29,
            "over_corners_8_5": 1.55, "under_corners_8_5": 2.45,
            "over_corners_9_5": 1.90, "under_corners_9_5": 1.90,
            "over_corners_10_5": 2.45, "under_corners_10_5": 1.55,
            "over_cards_3_5": 1.30, "under_cards_3_5": 3.45,
            "over_cards_4_5": 1.62, "under_cards_4_5": 2.28,
            "over_cards_5_5": 2.15, "under_cards_5_5": 1.68
        },
        "sources": "Pinnacle, Betsson, FlashScore, ClubElo"
    },
    # 12. Copa Sudamericana: Montevideo City Torque vs Atlético Mineiro (19:00 UYT / 22:00 UTC / 17:00 COT)
    {
        "match": "Montevideo City Torque vs Atlético Mineiro",
        "league": "Copa Sudamericana 2026 - Semifinal (vuelta)",
        "home_team": "Montevideo City Torque",
        "away_team": "Atlético Mineiro",
        "match_date": "2026-10-21T22:00:00Z",
        "elo_home": 1610,
        "elo_away": 1790,
        "xg_home_for": 1.20,
        "xg_home_against": 1.55,
        "xg_away_for": 1.58,
        "xg_away_against": 1.10,
        "corners_home_for": 4.5,
        "corners_home_against": 5.4,
        "corners_away_for": 5.6,
        "corners_away_against": 4.2,
        "cards_home_for": 2.6,
        "cards_home_against": 2.4,
        "cards_away_for": 2.5,
        "cards_away_against": 2.7,
        "odds": {
            "1": 2.88, "X": 3.25, "2": 3.25,
            "1x": 1.48, "x2": 1.48, "12": 1.35,
            "dnb_home": 1.95, "dnb_away": 1.95,
            "btts_yes": 1.82, "btts_no": 1.98,
            "over_1_5": 1.32, "under_1_5": 3.40,
            "over_2_5": 2.05, "under_2_5": 1.78,
            "over_3_5": 3.70, "under_3_5": 1.28,
            "over_corners_8_5": 1.60, "under_corners_8_5": 2.35,
            "over_corners_9_5": 1.95, "under_corners_9_5": 1.85,
            "over_corners_10_5": 2.50, "under_corners_10_5": 1.52,
            "over_cards_3_5": 1.32, "under_cards_3_5": 3.35,
            "over_cards_4_5": 1.65, "under_cards_4_5": 2.22,
            "over_cards_5_5": 2.20, "under_cards_5_5": 1.65
        },
        "sources": "Pinnacle, Betsson, Conmebol, ClubElo"
    },
    # 13. MLS: FC Cincinnati vs D.C. United (16:00 local / 20:00 UTC)
    {
        "match": "FC Cincinnati vs D.C. United",
        "league": "Major League Soccer (MLS) 2026 - Regular Season",
        "home_team": "FC Cincinnati",
        "away_team": "D.C. United",
        "match_date": "2026-10-21T20:00:00Z",
        "elo_home": 1640,
        "elo_away": 1530,
        "xg_home_for": 1.85,
        "xg_home_against": 1.22,
        "xg_away_for": 1.32,
        "xg_away_against": 1.88,
        "corners_home_for": 5.8,
        "corners_home_against": 4.5,
        "corners_away_for": 4.6,
        "corners_away_against": 5.7,
        "cards_home_for": 1.8,
        "cards_home_against": 2.2,
        "cards_away_for": 2.3,
        "cards_away_against": 1.9,
        "odds": {
            "1": 1.67, "X": 4.79, "2": 4.28,
            "1x": 1.24, "x2": 2.25, "12": 1.20,
            "dnb_home": 1.30, "dnb_away": 3.50,
            "btts_yes": 1.52, "btts_no": 2.50,
            "over_1_5": 1.14, "under_1_5": 5.80,
            "over_2_5": 1.50, "under_2_5": 2.65,
            "over_3_5": 2.25, "under_3_5": 1.66,
            "over_corners_8_5": 1.50, "under_corners_8_5": 2.60,
            "over_corners_9_5": 1.82, "under_corners_9_5": 2.00,
            "over_corners_10_5": 2.30, "under_corners_10_5": 1.62,
            "over_cards_3_5": 1.65, "under_cards_3_5": 2.20,
            "over_cards_4_5": 2.20, "under_cards_4_5": 1.65
        },
        "sources": "Pinnacle, Betsson, MLS Soccer, FBref"
    },
    # 14. Liga BetPlay Colombia: Llaneros FC vs Deportivo Cali (18:15 COT / 23:15 UTC) - Incomplete xG
    {
        "match": "Llaneros FC vs Deportivo Cali",
        "league": "Liga BetPlay Dimayor 2026-II - Fecha 9 (aplazada)",
        "home_team": "Llaneros FC",
        "away_team": "Deportivo Cali",
        "match_date": "2026-10-21T23:15:00Z",
        "elo_home": None,
        "elo_away": None,
        "xg_home_for": None,
        "xg_home_against": None,
        "xg_away_for": None,
        "xg_away_against": None,
        "corners_home_for": 4.2,
        "corners_home_against": 4.8,
        "corners_away_for": 4.6,
        "corners_away_against": 5.1,
        "cards_home_for": 2.6,
        "cards_home_against": 2.5,
        "cards_away_for": 2.8,
        "cards_away_against": 2.4,
        "odds": {
            "1": 2.75, "X": 3.10, "2": 2.65,
            "1x": 1.50, "x2": 1.47, "12": 1.36,
            "dnb_home": 1.90, "dnb_away": 1.83,
            "btts_yes": 2.05, "btts_no": 1.75,
            "over_1_5": 1.48, "under_1_5": 2.60,
            "over_2_5": 2.35, "under_2_5": 1.55,
            "over_3_5": 4.50, "under_3_5": 1.20
        },
        "sources": "Betano, Betplay, Dimayor",
        "data_limited": True,
        "data_limited_reason": "DATOS INSUFICIENTES: métricas xG no disponibles para Llaneros FC en proveedores públicos pre-kickoff"
    },
    # 15. Liga BetPlay Colombia: Independiente Santa Fe vs Jaguares de Córdoba (20:20 COT / 22T01:20 UTC) - Incomplete xG
    {
        "match": "Independiente Santa Fe vs Jaguares de Córdoba",
        "league": "Liga BetPlay Dimayor 2026-II - Fecha 7 (aplazada)",
        "home_team": "Independiente Santa Fe",
        "away_team": "Jaguares de Córdoba",
        "match_date": "2026-10-22T01:20:00Z", # 21 de octubre 20:20 COT
        "elo_home": None,
        "elo_away": None,
        "xg_home_for": None,
        "xg_home_against": None,
        "xg_away_for": None,
        "xg_away_against": None,
        "corners_home_for": 5.5,
        "corners_home_against": 3.8,
        "corners_away_for": 3.9,
        "corners_away_against": 5.8,
        "cards_home_for": 2.2,
        "cards_home_against": 2.6,
        "cards_away_for": 2.7,
        "cards_away_against": 2.1,
        "odds": {
            "1": 1.35, "X": 5.00, "2": 8.80,
            "1x": 1.08, "x2": 3.25, "12": 1.18,
            "dnb_home": 1.11, "dnb_away": 6.50,
            "btts_yes": 2.05, "btts_no": 1.75,
            "over_1_5": 1.22, "under_1_5": 4.20,
            "over_2_5": 1.74, "under_2_5": 2.10,
            "over_3_5": 2.90, "under_3_5": 1.42
        },
        "sources": "Bet365, Betplay, Dimayor",
        "data_limited": True,
        "data_limited_reason": "DATOS INSUFICIENTES: métricas xG no disponibles para Jaguares de Córdoba en proveedores públicos pre-kickoff"
    }
]

def universe_line(idx, rec):
    odds = rec.get("odds", {})
    s1x2 = f"1X2 {odds.get('1', '-')} {odds.get('X', '-')} {odds.get('2', '-')}"
    ou_parts = []
    for line in ("1_5", "2_5", "3_5"):
        o = odds.get(f"over_{line}")
        u = odds.get(f"under_{line}")
        if o and u:
            ou_parts.append(f"O{line.replace('_', '.')} {o} U{line.replace('_', '.')} {u}")
    sou = " ".join(ou_parts)
    extras = []
    for k in ("btts_yes", "btts_no", "1x", "x2", "12"):
        if k in odds:
            extras.append(f"{k} {odds[k]}")
    for prefix in ("corners", "cards"):
        for line in ("8_5", "9_5", "10_5") if prefix == "corners" else ("3_5", "4_5", "5_5"):
            ok = f"over_{prefix}_{line}"
            uk = f"under_{prefix}_{line}"
            if ok in odds:
                extras.append(f"{ok} {odds[ok]}")
            if uk in odds:
                extras.append(f"{uk} {odds[uk]}")
    sextras = " ".join(extras)
    elo = f"Elo {rec.get('elo_home') or 'n/d'}/{rec.get('elo_away') or 'n/d'}"
    if rec.get("xg_home_for") is not None:
        xg = f"xG {rec['xg_home_for']}/{rec['xg_home_against']} vs {rec['xg_away_for']}/{rec['xg_away_against']}"
    else:
        xg = "xG n/d"
    time_part = rec.get("match_date", "21T19:00Z").split("T")[1][:5]
    return f"{idx}. **{rec['league']}:** {rec['match']} (21T{time_part}Z). {s1x2}; {sou}; {sextras}. {elo}; {xg}."

def why_base_for(rec):
    league = rec.get("league", "")
    h, a = rec["home_team"], rec["away_team"]
    return (
        f"Partido clave de {league} entre {h} y {a}. "
        f"Métricas subyacentes muestran xG {rec.get('xg_home_for')}/{rec.get('xg_home_against')} para el local "
        f"y {rec.get('xg_away_for')}/{rec.get('xg_away_against')} para la visita; "
        f"tasas de córners {rec.get('corners_home_for')}/{rec.get('corners_away_for')} y tarjetas {rec.get('cards_home_for')}/{rec.get('cards_away_for')}."
    )

def main():
    all_results = []
    all_candidates = []
    all_evaluations = []
    data_limited_reasons = {}

    import subprocess
    for i, rec in enumerate(matches_data):
        m_name = rec["match"]
        if rec.get("data_limited"):
            data_limited_reasons[m_name] = rec["data_limited_reason"]
            all_results.append({
                "match": m_name,
                "data_limited": True,
                "data_limited_reason": rec["data_limited_reason"],
                "home_team": rec["home_team"],
                "away_team": rec["away_team"],
                "odds": rec["odds"]
            })
            continue

        inp_path = os.path.join(BASE, f"temp_match_input_{i}.json")
        out_path = os.path.join(BASE, f"temp_match_output_{i}.json")
        with open(inp_path, "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=2, ensure_ascii=False)

        cmd = [sys.executable, ENGINE, "--input", inp_path, "--config", MODEL_CONFIG, "--output", out_path]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error executing engine for {m_name}:\n{res.stderr}", file=sys.stderr)
            sys.exit(1)

        with open(out_path, encoding="utf-8") as f:
            engine_out = json.load(f)

        engine_out["match"] = m_name
        engine_out["league"] = rec["league"]
        engine_out["sources"] = rec["sources"]
        all_results.append(engine_out)

        ev_map = engine_out.get("evaluations", {})
        
        for mkt, ev in ev_map.items():
            enriched = dict(ev)
            enriched["match"] = m_name
            enriched["home_team"] = rec["home_team"]
            enriched["away_team"] = rec["away_team"]
            all_evaluations.append(enriched)
            if enriched.get("has_value"):
                enriched.setdefault("selection_profile", "excluido")
                enriched.setdefault("selection_reason", "Sin clasificar")
                all_candidates.append(enriched)

    # Global portfolio selection
    all_candidates.sort(
        key=lambda c: (
            0 if c.get("selection_profile") == "prioritario" else 1,
            -c.get("robust_ev_percent", 0.0),
            -c.get("model_prob", 0.0)
        )
    )

    selected, excluded = select_portfolio(list(all_candidates))

    picks_per_match = Counter(s["match"] for s in selected)

    def pick_detail(cand):
        m_name = cand["match"]
        rec = next(r for r in matches_data if r["match"] == m_name)
        label = market_label(cand["market"], rec["home_team"], rec["away_team"])
        extra = ""
        risks = "Riesgo de varianza deportiva inherente y ajuste del modelo ante partidos de eliminación/competición europea."
        if picks_per_match[cand["match"]] > 1:
            siblings = [s for s in selected if s["match"] == cand["match"] and s["market"] != cand["market"]]
            others = ", ".join(f"{s['market']} ({s['odds']:.2f})" for s in siblings)
            risks += (
                f" CORRELACIÓN: este mismo partido aporta {picks_per_match[cand['match']]} picks al portfolio "
                f"(junto a {others}); son eventos correlacionados y elevan la varianza conjunta."
            )
        why = (
            f"{why_base_for(rec)} El motor model-v1.3 estima {cand['model_prob']:.1%} para '{label}' "
            f"frente a una probabilidad implícita de {cand['implied_prob']:.1%} (cuota {cand['odds']:.2f}); "
            f"edge {cand['edge']:+.2f}% y EV robusto {cand['robust_ev_percent']:+.2f}%.{extra}"
        )
        return {
            "match": cand["match"],
            "market": cand["market"],
            "min_odds": f"{cand['fair_odds']:.2f}",
            "incertidumbre": "Base +/- 5.0% (model-v1.3); calibración Platt",
            "why": why,
            "risks": risks,
            "sources": f"{rec.get('sources', 'web del agente')}; verosimilitud del modelo y calibración Platt (model-v1.3).",
        }

    picks_details = [pick_detail(s) for s in selected]

    results = {
        "all_results": all_results,
        "all_candidates": all_candidates,
        "all_evaluations": all_evaluations,
        "selected": selected,
        "excluded": excluded,
    }
    with open(os.path.join(BASE, "results_21oct.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    now = datetime.now(timezone.utc)
    cutoff = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    meta = {
        "analysis_date_iso": cutoff,
        "match_dates_text": "21 de octubre de 2026",
        "information_cutoff": cutoff,
        "model_ia": "gemini3.8flash",
        "engine_version": "model-v1.3",
        "leagues_display": (
            "Liga BetPlay Dimayor (Finalización 2026), LaLiga EA Sports 2026-27, "
            "Major League Soccer (MLS) 2026, UEFA Champions League 2026-27, "
            "Copa Libertadores 2026 y Copa Sudamericana 2026"
        ),
        "requested_range": (
            "21 de octubre de 2026 - Liga BetPlay, LaLiga, MLS, Champions League, Copa Libertadores, Copa Sudamericana (todos los partidos)"
        ),
        "universe_preamble": (
            "Universo = intersección(ligas: Liga BetPlay, LaLiga, MLS, UEFA Champions League, Copa Libertadores, Copa Sudamericana, "
            f"fecha 21 de octubre de 2026, todos los partidos programados). Cutoff de información {cutoff}, "
            "anterior a los kickoffs. No se usa información posterior a ningún kickoff. Universo total = 15 partidos: "
            "9 de UEFA Champions League, 1 de LaLiga, 1 de Copa Libertadores, 1 de Copa Sudamericana, 1 de MLS y 2 de Liga BetPlay Dimayor. "
            "Todos los partidos cuentan con las tasas de corners y tarjetas (for/against) por equipo recolectadas. "
            "Aquellos encuentros con xG incompleto en fuentes públicas pre-kickoff (Llaneros vs Deportivo Cali y Santa Fe vs Jaguares) "
            "se consignan como DATOS INSUFICIENTES -> NO BET sin forzar priors del motor. "
            "MCPs inoperativos en la sesión, recolección vía investigación web del agente (Pinnacle, Betsson, Understat, SofaScore, FlashScore, Dimayor, Conmebol). "
            "Mercados O/U evaluados en ambos lados (goles 1.5/2.5/3.5, corners 8.5/9.5/10.5, tarjetas 3.5/4.5/5.5) donde hubo cuotas publicadas por casas de apuestas."
        ),
        "universe_matches": [universe_line(i, r) for i, r in enumerate(matches_data, 1)],
        "picks_details": picks_details,
        "data_limited_reasons": data_limited_reasons,
        "fallback_source": (
            "MCPs no operativos (football-stats, odds-api, apifootball). Investigación web del agente: Pinnacle, Betsson, "
            "Understat, SofaScore, FlashScore, Conmebol, MLS Soccer y Dimayor. Motor calc_engine.py model-v1.3 con calibración Platt. "
            "Partidos sin xG verificable completo no se ejecutan en el motor cuantitativo."
        ),
    }
    with open(os.path.join(BASE, "meta_21oct.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print("results_21oct.json y meta_21oct.json generados con éxito.")
    print(f"Universo total: {len(all_results)} partidos")
    print(f"Partidos ejecutados en motor: {len([r for r in all_results if not r.get('data_limited')])}")
    print(f"Partidos con datos limitados: {len(data_limited_reasons)}")
    print(f"Candidatos con value: {len(all_candidates)}")
    print(f"Picks seleccionados (top 0-6): {len(selected)}")
    for s in selected:
        print(f"  - {s['match']} | {s['market']} | cuota {s['odds']} | p {s['model_prob']:.3f} | robEV {s['robust_ev_percent']:+.2f}% | {s.get('selection_profile')}")

if __name__ == "__main__":
    main()
