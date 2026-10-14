"""Ensambla inputs, ejecuta el motor model-v1.3, selecciona y genera results/meta para 2026-10-14.

Universo: UEFA Champions League (fase de liga, MD2) + MLS (Decision Day) +
Copa Libertadores (semifinal ida) + Copa Sudamericana (semifinal ida).

MCPs inoperativos (apifootball/odds-api/football-stats) -> investigacion web del agente.
Cutoff de informacion: 2026-10-14T12:10Z (anterior a todos los kickoffs).

Politica de datos (igual que el run 13-oct):
- Si faltan los 4 valores de xG verificables, NO se ejecuta el motor (evitar priors por defecto).
- Conflictos de xG se arbitran con evidencia independiente y se documentan.
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

from selection import select_portfolio

MODEL_CONFIG = os.path.join("models", "model-v1.3.json")
ENGINE = os.path.join("scripts", "calc_engine.py")

UCL = "UEFA Champions League - Fase de Liga"
MLS = "MLS - Temporada Regular (Decision Day)"
LIB = "Copa Libertadores - Semifinal (ida)"
SUD = "Copa Sudamericana - Semifinal (ida)"

SRC_WEB = (
    "querostats.com + statz.ai (xG), querostats.com + statz.ai + footymetrics.com (corners/tarjetas), "
    "clubelo.com (Elo), ESPN/FOX/bettingview/oddsportal (cuotas)"
)
SRC_STATZ = (
    "statz.ai (xG/corners/tarjetas), clubelo.com (Elo), ESPN/FOX (cuotas), "
    "footystats.org (arbitraje de xG), oddalerts.com/statmuse.com (contraste)"
)
SRC_MLS = (
    "pitchmath.com (xG y corners), statz.ai (tarjetas), oddalerts.com (xG MLS, lote oeste), "
    "clubelo.com/USA (Elo), bettingview.com + oddschecker (cuotas)"
)
SRC_CONMEBOL = "statz.ai (xG/corners/tarjetas), clubelo.com (Elo), bwin/oddstorm/aiscore (cuotas)"


def m(name, home, away, league, kickoff, sources, inp=None, limited=False, why_base="", risks=""):
    return {
        "match": name, "home": home, "away": away, "league": league, "kickoff": kickoff,
        "sources": sources, "input": inp, "limited": limited,
        "why_base": why_base, "risks": risks,
    }


MATCHES = [
    # ---------------- UEFA Champions League (9) ----------------
    m(
        "Feyenoord vs Como", "Feyenoord", "Como", UCL, "2026-10-14T16:45:00Z", SRC_WEB,
        inp={
            "xg_home_for": 2.47, "xg_home_against": 0.98, "xg_away_for": 1.97, "xg_away_against": 1.44,
            "elo_home": 1724, "elo_away": 1807,
            "corners_home_for": 5.7, "corners_home_against": 4.0, "corners_away_for": 6.7, "corners_away_against": 3.7,
            "cards_home_for": 0.89, "cards_home_against": 1.14, "cards_away_for": 1.14, "cards_away_against": 0.89,
            "odds": {
                "1": 3.3, "X": 3.9, "2": 1.91,
                "over_1_5": 1.12, "under_1_5": 6.0, "over_2_5": 1.44, "under_2_5": 2.75,
                "over_3_5": 2.0, "under_3_5": 1.75, "btts_yes": 1.4,
            },
        },
        why_base=(
            "Feyenoord local con xG a favor alto (2.47) frente a un Como que concede 1.44; "
            "Elo favorable al visitante (1807 vs 1724), lo que abre el mercado 1X2 mas de lo que sugiere la localia."
        ),
        risks="Sin cuotas de doble oportunidad, DNB ni tarjetas; solo linea 2.5 de corners relevante; tarjetas con valores bajos del proveedor.",
    ),
    m(
        "LASK vs Liverpool", "LASK", "Liverpool", UCL, "2026-10-14T16:45:00Z", SRC_WEB,
        inp={
            "xg_home_for": 0.72, "xg_home_against": 1.71, "xg_away_for": 1.56, "xg_away_against": 1.19,
            "elo_home": 1628, "elo_away": 1929,
            "corners_home_for": 3.0, "corners_home_against": 7.0, "corners_away_for": 4.6, "corners_away_against": 4.7,
            "cards_home_for": 2.0, "cards_home_against": 2.29, "cards_away_for": 2.29, "cards_away_against": 2.0,
            "odds": {"1": 9.39, "X": 6.16, "2": 1.29, "over_2_5": 1.34, "btts_yes": 1.59},
        },
        why_base="Brecha Elo enorme (1929 vs 1628) y xG local muy bajo (0.72) con defensa local vulnerable (1.71 en contra).",
        risks="Solo se cotizaron 1X2, O/U 2.5 y BTTS; sin doble oportunidad, DNB, corners ni tarjetas.",
    ),
    m(
        "Real Betis vs FC Porto", "Real Betis", "FC Porto", UCL, "2026-10-14T19:00:00Z", SRC_WEB,
        inp={
            "xg_home_for": 1.77, "xg_home_against": 1.75, "xg_away_for": 2.12, "xg_away_against": 1.06,
            "elo_home": 1822.8, "elo_away": 1841.9,
            "corners_home_for": 5.1, "corners_home_against": 6.6, "corners_away_for": 6.2, "corners_away_against": 3.8,
            "cards_home_for": 1.67, "cards_home_against": 1.0, "cards_away_for": 1.0, "cards_away_against": 1.67,
            "odds": {"1": 2.16, "X": 3.76, "2": 3.5, "over_2_5": 1.79, "under_2_5": 2.19, "btts_yes": 1.61},
        },
        why_base="Elo casi identico (1842 vs 1823) pero Porto con mejor perfil de xG (2.12 a favor / 1.06 en contra) que un Betis que concede 1.75.",
        risks="Solo 1X2, O/U 2.5 y BTTS cotizados; corners muy altos en contra del Betis (6.6) con muestra corta.",
    ),
    m(
        "Aston Villa vs Fenerbahce", "Aston Villa", "Fenerbahce", UCL, "2026-10-14T19:00:00Z", SRC_WEB,
        inp={
            "xg_home_for": 1.43, "xg_home_against": 1.64, "xg_away_for": 2.05, "xg_away_against": 1.09,
            "elo_home": 1893.4, "elo_away": 1784.5,
            "corners_home_for": 3.1, "corners_home_against": 4.3, "corners_away_for": 6.0, "corners_away_against": 3.6,
            "cards_home_for": 2.29, "cards_home_against": 1.75, "cards_away_for": 1.75, "cards_away_against": 2.29,
            "odds": {
                "1": 1.7, "X": 4.1, "2": 4.5,
                "over_1_5": 1.17, "under_1_5": 5.0, "over_2_5": 1.57, "under_2_5": 2.38,
                "over_3_5": 2.38, "under_3_5": 1.57,
                "1x": 1.17, "12": 1.22, "x2": 2.25, "btts_yes": 1.57, "btts_no": 2.35,
                "over_corners_8_5": 1.44, "under_corners_8_5": 2.6, "over_corners_9_5": 1.74, "under_corners_9_5": 2.0,
            },
        },
        why_base="Villa con Elo superior (1893 vs 1785) y localia; Fenerbahce llega con mejor xG a favor (2.05) pero defensa mas solida del local.",
        risks="xG del Villa discrepa con su rendimiento liguero (1.43 a favor); corners del Villa inusualmente bajos (3.1); sin DNB cotizado.",
    ),
    m(
        "Shakhtar Donetsk vs AEK Athens", "Shakhtar Donetsk", "AEK Athens", UCL, "2026-10-14T19:00:00Z", SRC_WEB,
        inp={
            "xg_home_for": 0.62, "xg_home_against": 0.44, "xg_away_for": 1.71, "xg_away_against": 0.72,
            "elo_home": 1692, "elo_away": 1708,
            "corners_home_for": 3.0, "corners_home_against": 3.0, "corners_away_for": 7.0, "corners_away_against": 3.0,
            "cards_home_for": 6.0, "cards_home_against": 1.0, "cards_away_for": 1.0, "cards_away_against": 6.0,
            "odds": {
                "1": 2.77, "X": 3.37, "2": 2.67, "over_2_5": 1.95, "under_2_5": 1.95,
                "btts_yes": 1.7, "btts_no": 2.25,
                "over_corners_8_5": 1.71, "under_corners_8_5": 2.0,
            },
        },
        why_base="Partido de Elo casi identico (1708 vs 1692) con xG bajo del local (0.62) en cancha neutral (Stamford Bridge), lo que reduce la ventaja de localia.",
        risks="Localia neutral (sede designada); tarjetas/contadores del proveedor con valores extremos (6.0) y simetria invertida, se usan solo como contexto.",
    ),
    m(
        "Roma vs Real Madrid", "Roma", "Real Madrid", UCL, "2026-10-14T19:00:00Z", SRC_STATZ,
        inp={
            "xg_home_for": 2.25, "xg_home_against": 1.12, "xg_away_for": 2.41, "xg_away_against": 1.20,
            "elo_home": 1856, "elo_away": 1975,
            "corners_home_for": 5.17, "corners_home_against": 2.5, "corners_away_for": 6.86, "corners_away_against": 4.14,
            "cards_home_for": 1.83, "cards_home_against": 1.5, "cards_away_for": 2.13, "cards_away_against": 2.75,
            "odds": {
                "1": 3.65, "X": 3.95, "2": 1.91,
                "over_3_5": 2.1, "under_3_5": 1.74, "btts_yes": 1.39, "btts_no": 3.0,
                "1x": 1.91, "x2": 1.33, "12": 1.28,
                "over_corners_8_5": 1.51, "under_corners_8_5": 2.4, "over_corners_9_5": 1.83, "under_corners_9_5": 1.87,
            },
        },
        why_base="Real Madrid favorito por Elo (1975 vs 1856) y xG a favor alto (2.41) frente a un Roma que en casa tiene 2.25 a favor pero defensa firme (1.12 en contra).",
        risks="xG del Roma discrepa entre fuentes (2.25 statz vs 2.55 otra lectura de statz); sin lineas 1.5 y 2.5 cotizadas; sin DNB.",
    ),
    m(
        "Manchester City vs Paris Saint-Germain", "Manchester City", "Paris Saint-Germain", UCL, "2026-10-14T19:00:00Z", SRC_STATZ,
        inp={
            "xg_home_for": 2.03, "xg_home_against": 1.44, "xg_away_for": 2.45, "xg_away_against": 1.09,
            "elo_home": 2034, "elo_away": 1957,
            "corners_home_for": 6.17, "corners_home_against": 4.33, "corners_away_for": 5.67, "corners_away_against": 1.67,
            "cards_home_for": 1.33, "cards_home_against": 1.83, "cards_away_for": 1.17, "cards_away_against": 2.33,
            "odds": {
                "1": 2.0, "X": 4.0, "2": 3.3,
                "over_3_5": 2.05, "under_3_5": 1.77, "btts_yes": 1.4, "btts_no": 2.95,
                "over_corners_8_5": 1.69, "under_corners_8_5": 2.05, "over_corners_9_5": 2.15, "under_corners_9_5": 1.63,
            },
        },
        why_base="Choque de elite: City con Elo superior (2034 vs 1957) y localia, pero el PSG llega con xG a favor superior (2.45) y defensa que concede solo 1.09.",
        risks="Sin lineas 1.5/2.5 ni doble oportunidad/DNB; corners del PSG en contra muy bajos (1.67) con muestra corta.",
    ),
    m(
        "Slovan Bratislava vs VfB Stuttgart", "Slovan Bratislava", "VfB Stuttgart", UCL, "2026-10-14T19:00:00Z", SRC_STATZ,
        inp={
            "xg_home_for": 1.91, "xg_home_against": 1.15, "xg_away_for": 1.94, "xg_away_against": 2.08,
            "elo_home": 1551, "elo_away": 1824,
            "corners_home_for": 3.14, "corners_home_against": 4.71, "corners_away_for": 6.2, "corners_away_against": 6.2,
            "cards_home_for": 1.86, "cards_home_against": 2.14, "cards_away_for": 1.2, "cards_away_against": 2.2,
            "odds": {
                "1": 7.5, "X": 5.75, "2": 1.35,
                "over_3_5": 1.83, "under_3_5": 1.95, "btts_yes": 1.57, "btts_no": 2.4,
                "over_corners_8_5": 1.47, "under_corners_8_5": 2.5, "over_corners_9_5": 1.77, "under_corners_9_5": 1.91,
            },
        },
        why_base="Stuttgart ampliamente superior por Elo (1824 vs 1551) y visitante con xG a favor de 1.94; Slovan apenas sostiene 1.91 a favor con defensa que concede 1.15 en su liga.",
        risks=(
            "xG del Slovan procede de una UNICA fuente domestica (footystats, liga eslovaca, 9 partidos) tras arbitraje: el valor previo de 0.64 "
            "correspondia a un solo partido de UCL (0-1-6 vs PSG) y fue descartado. Muestra domestica corta y de baja cobertura estadistica."
        ),
    ),
    m(
        "Bodo/Glimt vs Borussia Dortmund", "Bodo/Glimt", "Borussia Dortmund", UCL, "2026-10-14T19:00:00Z", SRC_STATZ,
        inp={
            "xg_home_for": 2.90, "xg_home_against": 0.73, "xg_away_for": 1.79, "xg_away_against": 0.92,
            "elo_home": 1781, "elo_away": 1895,
            "corners_home_for": 7.59, "corners_home_against": 2.36, "corners_away_for": 4.8, "corners_away_against": 4.6,
            "cards_home_for": 0.55, "cards_home_against": 1.85, "cards_away_for": 2.4, "cards_away_against": 1.8,
            "odds": {
                "1": 3.0, "X": 3.95, "2": 2.2,
                "over_3_5": 1.95, "under_3_5": 1.87, "btts_yes": 1.33, "btts_no": 3.3,
                "over_corners_8_5": 1.57, "under_corners_8_5": 2.25, "over_corners_9_5": 1.91, "under_corners_9_5": 1.77,
            },
        },
        why_base="Dortmund superior por Elo (1895 vs 1781) pero Bodo/Glimt es el mejor ataque de la Eliteserien (2.90 xG a favor, 0.73 en contra) y cotiza como local a 3.00.",
        risks=(
            "xG del local arbitrado: 0.20 previo (ESPN/FOX) correspondia a un unico partido de UCL (0-5 vs Bayern), no a su liga domestica; se adopta la ventana domestica "
            "(statz 2.90/0.73, footystats 2.28 a favor como tercera opinion -> rango 2.28-2.90). Incertidumbre elevada por la magnitud de la discrepancia."
        ),
    ),
    # ---------------- CONMEBOL (2) ----------------
    m(
        "Fluminense vs Palmeiras", "Fluminense", "Palmeiras", LIB, "2026-10-15T00:30:00Z", SRC_CONMEBOL,
        inp={
            "xg_home_for": 1.46, "xg_home_against": 1.38, "xg_away_for": 1.85, "xg_away_against": 1.01,
            "elo_home": 1769, "elo_away": 1856,
            "corners_home_for": 3.4, "corners_home_against": 6.4, "corners_away_for": 7.0, "corners_away_against": 4.3,
            "cards_home_for": 2.9, "cards_home_against": 2.2, "cards_away_for": 2.4, "cards_away_against": 2.8,
            "odds": {
                "1": 2.87, "X": 3.1, "2": 2.62,
                "over_1_5": 1.57, "under_1_5": 2.25, "over_2_5": 2.87, "under_2_5": 1.4,
                "over_3_5": 6.0, "under_3_5": 1.13,
                "btts_yes": 2.25, "btts_no": 1.57,
                "1x": 1.49, "12": 1.36, "x2": 1.46, "dnb_home": 1.9, "dnb_away": 1.8,
                "over_corners_9_5": 1.8, "under_corners_9_5": 1.9,
            },
        },
        why_base="Semifinal de Libertadores muy equilibrada: Palmeiras con mejor Elo (1856 vs 1769) y xG (1.85 a favor / 1.01 en contra) frente a un Fluminense local que concede 1.38.",
        risks=(
            "Ventanas de datos distintas (xG = ultimos 10 partidos de Brasileirao; corners/tarjetas = ultimos 10 de todas las competiciones, incluida Libertadores). "
            "Sin 1X2 alternativo ni lineas de corners 8.5/10.5 ni tarjetas; semifinal a ida suele ser de bajo ritmo."
        ),
    ),
    m(
        "Atletico Mineiro vs Montevideo City Torque", "Atletico Mineiro", "Montevideo City Torque", SUD,
        "2026-10-15T00:30:00Z", SRC_CONMEBOL,
        limited=True,
        why_base="Datos insuficientes (sin xG verificable del visitante ni Elo).",
        risks=(
            "Montevideo City Torque (Uruguay) no tiene xG por partido en ninguna fuente consultada (statz/understat/xg-edge no cubren la liga uruguaya) "
            "ni rating ClubElo. Con solo el lado local del xG, ejecutar el motor obligaria a usar priors por defecto para el visitante: NO BET por datos insuficientes."
        ),
    ),
    # ---------------- MLS East (8) ----------------
    m(
        "CF Montreal vs Atlanta United FC", "CF Montreal", "Atlanta United FC", MLS, "2026-10-14T23:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.40, "xg_home_against": 1.57, "xg_away_for": 1.36, "xg_away_against": 1.53,
            "elo_home": 1486, "elo_away": 1508,
            "corners_home_for": 5.04, "corners_home_against": 4.57, "corners_away_for": 4.96, "corners_away_against": 5.21,
            "cards_home_for": 2.18, "cards_home_against": 1.89, "cards_away_for": 2.18, "cards_away_against": 1.82,
            "odds": {
                "1": 2.5, "X": 3.8, "2": 2.85, "over_2_5": 1.54, "btts_yes": 1.5, "btts_no": 2.7,
                "1x": 1.47, "12": 1.28, "x2": 1.63, "dnb_home": 1.8, "dnb_away": 2.18,
                "over_cards_4_5": 2.1, "under_cards_4_5": 1.63,
            },
        },
        why_base="Partido casi simetrico (Elo 1508 vs 1486; xG 1.40/1.57 vs 1.36/1.53) con Montreal como local y cuota de 2.50.",
        risks="Sin lineas 1.5/3.5 de goles ni corners; una sola linea de tarjetas (4.5). Elo MLS comprimido (rango estrecho) reduce el peso del componente ratings.",
    ),
    m(
        "Columbus Crew vs Charlotte FC", "Columbus Crew", "Charlotte FC", MLS, "2026-10-14T23:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.21, "xg_home_against": 1.19, "xg_away_for": 1.53, "xg_away_against": 1.44,
            "elo_home": 1595, "elo_away": 1609,
            "corners_home_for": 5.29, "corners_home_against": 3.64, "corners_away_for": 4.82, "corners_away_against": 5.82,
            "cards_home_for": 1.75, "cards_home_against": 2.25, "cards_away_for": 2.14, "cards_away_against": 2.54,
            "odds": {
                "1": 2.0, "X": 4.0, "2": 3.6, "over_2_5": 1.52, "under_2_5": 2.48,
                "btts_yes": 1.46, "btts_no": 2.95, "1x": 1.36, "12": 1.26, "x2": 1.82,
                "dnb_home": 1.57, "dnb_away": 2.62, "over_cards_4_5": 2.1, "under_cards_4_5": 1.63,
            },
        },
        why_base="Columbus local con Elo ligeramente inferior (1595 vs 1609) y xG propio bajo (1.21 a favor) frente a un Charlotte con mejor ataque pero peor defensa.",
        risks="Sin lineas 1.5/3.5 ni corners; xG del local inusualmente bajo para un equipo de localia fuerte en MLS.",
    ),
    m(
        "DC United vs New York Red Bulls", "DC United", "New York Red Bulls", MLS, "2026-10-14T23:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.44, "xg_home_against": 1.53, "xg_away_for": 1.59, "xg_away_against": 2.01,
            "elo_home": 1494, "elo_away": 1551,
            "corners_home_for": 4.73, "corners_home_against": 5.38, "corners_away_for": 5.61, "corners_away_against": 5.18,
            "cards_home_for": 2.16, "cards_home_against": 2.12, "cards_away_for": 2.07, "cards_away_against": 1.75,
            "odds": {
                "1": 2.2, "X": 4.1, "2": 3.5, "btts_yes": 1.49, "btts_no": 2.64,
                "1x": 1.39, "12": 1.27, "x2": 1.87, "dnb_home": 1.45, "dnb_away": 2.84,
                "over_cards_4_5": 2.1, "under_cards_4_5": 1.63,
            },
        },
        why_base="Red Bulls con mejor Elo (1551 vs 1494) y ataque superior (1.59 a favor) pero defensa muy vulnerable (2.01 en contra) en cancha de un DC United irregular.",
        risks="Sin lineas de goles O/U cotizadas en 1.5/2.5/3.5 ni corners; solo tarjetas 4.5.",
    ),
    m(
        "FC Cincinnati vs New England Revolution", "FC Cincinnati", "New England Revolution", MLS, "2026-10-14T23:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.74, "xg_home_against": 1.77, "xg_away_for": 1.56, "xg_away_against": 1.30,
            "elo_home": 1603, "elo_away": 1559,
            "corners_home_for": 5.0, "corners_home_against": 4.96, "corners_away_for": 4.82, "corners_away_against": 5.43,
            "cards_home_for": 2.23, "cards_home_against": 1.81, "cards_away_for": 1.85, "cards_away_against": 1.74,
            "odds": {
                "1": 1.95, "X": 4.6, "2": 4.2, "over_3_5": 1.91, "under_3_5": 1.95,
                "btts_yes": 1.37, "btts_no": 3.05, "1x": 1.32, "12": 1.24, "x2": 2.15,
                "dnb_home": 1.49, "dnb_away": 3.35, "over_cards_3_5": 1.63, "under_cards_3_5": 2.1,
            },
        },
        why_base="Cincinnati local con Elo superior (1603 vs 1559) y ataque alto (1.74 a favor), aunque su defensa concede casi lo mismo (1.77).",
        risks="Solo linea 3.5 de goles cotizada (no 1.5/2.5); sin corners; Elo comprimido tipico de MLS.",
    ),
    m(
        "Inter Miami CF vs New York City FC", "Inter Miami CF", "New York City FC", MLS, "2026-10-14T23:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 2.05, "xg_home_against": 1.62, "xg_away_for": 1.25, "xg_away_against": 1.50,
            "elo_home": 1684, "elo_away": 1592,
            "corners_home_for": 5.21, "corners_home_against": 3.79, "corners_away_for": 3.75, "corners_away_against": 4.79,
            "cards_home_for": 2.78, "cards_home_against": 2.00, "cards_away_for": 1.68, "cards_away_against": 2.89,
            "odds": {
                "1": 1.59, "X": 4.8, "2": 5.25, "over_3_5": 1.8, "under_3_5": 1.96,
                "btts_yes": 1.43, "btts_no": 2.9, "1x": 1.17, "x2": 2.38,
                "dnb_home": 1.29, "dnb_away": 4.1, "over_cards_4_5": 2.1, "under_cards_4_5": 1.63,
            },
        },
        why_base="Miami es el mejor equipo de Elo del grupo (1684 vs 1592) y con el ataque mas alto de estos ocho partidos (2.05 xG a favor) ante un NYCFC que solo genera 1.25.",
        risks="Sin lineas 1.5/2.5 ni 12 ni corners; Miami acumula 2.78 tarjetas por partido (riesgo disciplinario en mercados de tarjetas).",
    ),
    m(
        "Toronto FC vs Orlando City SC", "Toronto FC", "Orlando City SC", MLS, "2026-10-14T23:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.18, "xg_home_against": 1.46, "xg_away_for": 1.54, "xg_away_against": 1.92,
            "elo_home": 1520, "elo_away": 1595,
            "corners_home_for": 4.93, "corners_home_against": 5.82, "corners_away_for": 4.0, "corners_away_against": 6.96,
            "cards_home_for": 1.75, "cards_home_against": 2.07, "cards_away_for": 2.29, "cards_away_against": 2.04,
            "odds": {
                "1": 2.35, "X": 3.9, "2": 2.85, "over_3_5": 2.02, "under_3_5": 1.87,
                "btts_yes": 1.39, "btts_no": 3.3, "1x": 1.47, "12": 1.27, "x2": 1.66,
                "dnb_home": 1.74, "dnb_away": 2.2, "over_cards_4_5": 2.0, "under_cards_4_5": 1.62,
            },
        },
        why_base="Orlando con mejor Elo (1595 vs 1520) y ataque superior (1.54 vs 1.18) frente a un Toronto que concede 1.46 en casa y 6.96 corners por partido.",
        risks="Sin lineas 1.5/2.5 ni corners; corners en contra del visitante muy altos (6.96), lo que sugiere mercados de corners interesantes no cotizados aqui.",
    ),
    m(
        "Chicago Fire vs Philadelphia Union", "Chicago Fire", "Philadelphia Union", MLS, "2026-10-15T00:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.81, "xg_home_against": 1.31, "xg_away_for": 1.93, "xg_away_against": 1.37,
            "elo_home": 1605, "elo_away": 1649,
            "corners_home_for": 4.41, "corners_home_against": 5.11, "corners_away_for": 5.89, "corners_away_against": 3.54,
            "cards_home_for": 2.25, "cards_home_against": 1.89, "cards_away_for": 2.43, "cards_away_against": 2.39,
            "odds": {
                "1": 2.6, "X": 4.1, "2": 2.6, "over_3_5": 2.05, "under_3_5": 1.95,
                "btts_yes": 1.4, "btts_no": 3.1, "1x": 1.54, "x2": 1.54, "12": 1.27,
                "dnb_home": 2.0, "dnb_away": 1.89, "over_cards_4_5": 1.8, "under_cards_4_5": 1.78,
            },
        },
        why_base="Philadelphia con mejor Elo (1649 vs 1605) y ataque alto (1.93 a favor, 1.37 en contra) frente a un Chicago Fire solido en casa (1.81/1.31).",
        risks="Sin lineas 1.5/2.5 ni corners; 1X2 perfectamente simetrico (2.60/2.60) y doble oportunidad 1.54/1.54, lo que exige alta precision del modelo.",
    ),
    m(
        "FC Dallas vs Seattle Sounders", "FC Dallas", "Seattle Sounders", MLS, "2026-10-15T00:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.50, "xg_home_against": 1.38, "xg_away_for": 1.34, "xg_away_against": 1.37,
            "elo_home": 1605, "elo_away": 1623,
            "corners_home_for": 4.36, "corners_home_against": 6.07, "corners_away_for": 5.29, "corners_away_against": 6.29,
            "cards_home_for": 2.32, "cards_home_against": 2.04, "cards_away_for": 1.85, "cards_away_against": 1.50,
            "odds": {
                "1": 1.98, "X": 4.1, "2": 4.0, "btts_yes": 1.55, "btts_no": 2.6,
                "1x": 1.31, "12": 1.25, "x2": 1.97, "dnb_home": 1.47, "dnb_away": 2.92,
                "over_cards_3_5": 1.72, "under_cards_3_5": 1.88,
            },
        },
        why_base="Dallas local con Elo practicamente igual (1605 vs 1623) pero xG a favor propio superior (1.50 vs 1.34) en un partido de baja expectativa de goles.",
        risks="Sin lineas de goles O/U ni corners; solo tarjetas 3.5; corners en contra altos en ambos (6.07 y 6.29) sin cuota disponible.",
    ),
    # ---------------- MLS West (7) ----------------
    m(
        "Nashville SC vs Sporting Kansas City", "Nashville SC", "Sporting Kansas City", MLS, "2026-10-15T00:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.62, "xg_home_against": 1.30, "xg_away_for": 1.19, "xg_away_against": 1.99,
            "elo_home": 1690, "elo_away": 1457,
            "corners_home_for": 5.32, "corners_home_against": 3.93, "corners_away_for": 4.0, "corners_away_against": 5.79,
            "cards_home_for": 1.79, "cards_home_against": 1.46, "cards_away_for": 1.75, "cards_away_against": 1.68,
            "odds": {
                "1": 1.29, "X": 6.5, "2": 10.0, "over_2_5": 1.29, "under_2_5": 3.5,
                "over_3_5": 1.76, "under_3_5": 2.0, "btts_yes": 1.77, "btts_no": 2.18,
                "1x": 1.07, "x2": 4.4, "12": 1.11, "dnb_home": 1.08, "dnb_away": 10.4,
                "over_cards_3_5": 2.05, "under_cards_3_5": 1.6,
            },
        },
        why_base="Mayor brecha de Elo del universo MLS (1690 vs 1457) y local con mejor xG en ambos lados (1.62/1.30 vs 1.19/1.99).",
        risks="Cuota del favorito muy corta (1.29 / DNB 1.08), fuera del rango prioritario; el value solo puede aparecer en lineas de goles o tarjetas.",
    ),
    m(
        "St. Louis CITY SC vs Vancouver Whitecaps", "St. Louis CITY SC", "Vancouver Whitecaps", MLS, "2026-10-15T00:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.59, "xg_home_against": 1.23, "xg_away_for": 2.18, "xg_away_against": 1.10,
            "elo_home": 1626, "elo_away": 1653,
            "corners_home_for": 5.36, "corners_home_against": 4.61, "corners_away_for": 6.0, "corners_away_against": 2.96,
            "cards_home_for": 2.23, "cards_home_against": 2.23, "cards_away_for": 2.0, "cards_away_against": 2.29,
            "odds": {
                "1": 2.3, "X": 4.0, "2": 3.0, "over_1_5": 1.14, "under_1_5": 5.5,
                "over_2_5": 1.5, "under_2_5": 2.5, "over_3_5": 2.2, "under_3_5": 1.62,
                "btts_yes": 1.48, "btts_no": 2.85, "1x": 1.44, "x2": 1.72, "12": 1.26,
                "dnb_home": 1.72, "dnb_away": 2.3, "over_cards_4_5": 1.92, "under_cards_4_5": 1.68,
            },
        },
        why_base="Vancouver llega con el mejor ataque visitante del lote oeste (2.18 xG a favor, 1.10 en contra) y Elo ligeramente superior, pero cotiza a 3.00.",
        risks="Sin corners cotizados pese a que Vancouver concede solo 2.96; xG del visitante muy alto con muestra de temporada MLS.",
    ),
    m(
        "Colorado Rapids vs Minnesota United", "Colorado Rapids", "Minnesota United", MLS, "2026-10-15T01:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.51, "xg_home_against": 1.19, "xg_away_for": 1.73, "xg_away_against": 1.64,
            "elo_home": 1540, "elo_away": 1561,
            "corners_home_for": 4.96, "corners_home_against": 4.18, "corners_away_for": 5.29, "corners_away_against": 4.96,
            "cards_home_for": 2.5, "cards_home_against": 2.43, "cards_away_for": 2.0, "cards_away_against": 1.68,
            "odds": {
                "1": 2.05, "X": 3.6, "2": 3.2, "over_2_5": 1.61, "under_2_5": 2.3,
                "btts_yes": 1.53, "btts_no": 2.5,
                "over_corners_8_5": 1.5, "under_corners_8_5": 2.45, "over_corners_9_5": 1.83, "under_corners_9_5": 1.87,
            },
        },
        why_base="Elo very similar (1561 vs 1540) con Minnesota algo mejor al ataque (1.73 vs 1.51) pero peor defensa (1.64 vs 1.19).",
        risks="Sin lineas 1.5/3.5 de goles, sin doble oportunidad, DNB ni tarjetas; corners del local (4.96 a favor, 4.18 en contra) con dispersion baja.",
    ),
    m(
        "Real Salt Lake vs San Jose Earthquakes", "Real Salt Lake", "San Jose Earthquakes", MLS, "2026-10-15T01:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.37, "xg_home_against": 1.50, "xg_away_for": 1.84, "xg_away_against": 1.37,
            "elo_home": 1541, "elo_away": 1568,
            "corners_home_for": 4.75, "corners_home_against": 5.89, "corners_away_for": 6.29, "corners_away_against": 4.89,
            "cards_home_for": 2.37, "cards_home_against": 2.19, "cards_away_for": 2.29, "cards_away_against": 1.86,
            "odds": {
                "1": 1.91, "X": 3.85, "2": 3.35, "over_2_5": 1.48, "under_2_5": 2.75,
                "over_3_5": 2.15, "under_3_5": 1.69, "btts_yes": 1.43, "btts_no": 2.8,
                "over_corners_8_5": 1.31, "under_corners_8_5": 3.15, "over_corners_9_5": 1.54, "under_corners_9_5": 2.35,
                "over_corners_10_5": 1.87, "under_corners_10_5": 1.83,
            },
        },
        why_base="San Jose con mejor Elo (1568 vs 1541) y ataque superior (1.84 vs 1.37), con altisima produccion de corners en ambos lados (6.29 y 5.89 totales).",
        risks="Sin lineas 1.5 de goles, ni doble oportunidad, DNB o tarjetas; fuerte dependencia del mercado de corners, que solo tiene tres lineas cotizadas.",
    ),
    m(
        "LA Galaxy vs Portland Timbers", "LA Galaxy", "Portland Timbers", MLS, "2026-10-15T02:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.53, "xg_home_against": 1.71, "xg_away_for": 1.51, "xg_away_against": 1.63,
            "elo_home": 1547, "elo_away": 1555,
            "corners_home_for": 5.21, "corners_home_against": 4.03, "corners_away_for": 4.71, "corners_away_against": 5.79,
            "cards_home_for": 2.14, "cards_home_against": 2.41, "cards_away_for": 1.61, "cards_away_against": 2.14,
            "odds": {
                "1": 2.0, "X": 3.8, "2": 3.1, "over_2_5": 1.4, "under_2_5": 3.2,
                "over_3_5": 2.0, "under_3_5": 1.8, "btts_yes": 1.35, "btts_no": 3.15,
                "over_corners_8_5": 1.45, "under_corners_8_5": 2.55, "over_corners_9_5": 1.74, "under_corners_9_5": 1.95,
            },
        },
        why_base="Partido casi identico en Elo (1555 vs 1547) y xG simetrico (1.53/1.71 vs 1.51/1.63), tipico de alta volatilidad en MLS.",
        risks="Sin lineas 1.5 de goles, doble oportunidad, DNB ni tarjetas; ambos con defensas flojas y cuota de BTTS muy baja (1.35).",
    ),
    m(
        "LAFC vs Austin FC", "LAFC", "Austin FC", MLS, "2026-10-15T02:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.47, "xg_home_against": 1.42, "xg_away_for": 1.03, "xg_away_against": 2.04,
            "elo_home": 1652, "elo_away": 1540,
            "corners_home_for": 6.18, "corners_home_against": 5.29, "corners_away_for": 4.46, "corners_away_against": 6.0,
            "cards_home_for": 2.04, "cards_home_against": 2.42, "cards_away_for": 2.0, "cards_away_against": 2.14,
            "odds": {
                "1": 1.43, "X": 4.6, "2": 6.0, "over_2_5": 1.57, "under_2_5": 2.35,
                "over_3_5": 2.35, "under_3_5": 1.59,
            },
        },
        why_base="LAFC muy superior por Elo (1652 vs 1540) con Austin generando apenas 1.03 xG a favor y concediendo 2.04.",
        risks="Muy pocas lineas cotizadas (sin 1.5, BTTS, doble oportunidad, DNB, corners ni tarjetas); favorito a 1.43, por debajo del rango prioritario.",
    ),
    m(
        "San Diego FC vs Houston Dynamo", "San Diego FC", "Houston Dynamo", MLS, "2026-10-15T02:30:00Z", SRC_MLS,
        inp={
            "xg_home_for": 1.57, "xg_home_against": 1.70, "xg_away_for": 1.12, "xg_away_against": 1.36,
            "elo_home": 1600, "elo_away": 1588,
            "corners_home_for": 4.79, "corners_home_against": 4.25, "corners_away_for": 4.32, "corners_away_against": 4.61,
            "cards_home_for": 2.00, "cards_home_against": 2.21, "cards_away_for": 1.89, "cards_away_against": 2.56,
            "odds": {
                "1": 2.1, "X": 3.55, "2": 3.05, "over_2_5": 1.65, "under_2_5": 2.2,
                "btts_yes": 1.52, "btts_no": 2.39, "1x": 1.27, "x2": 1.84, "12": 1.24,
            },
        },
        why_base="San Diego local con Elo casi identico (1600 vs 1588) pero ataque claramente superior (1.57 vs 1.12) frente a un Houston poco productivo.",
        risks="Sin lineas 1.5/3.5, corners, tarjetas ni DNB; mercado reducido a 1X2, 2.5 goles, BTTS y doble oportunidad.",
    ),
]


def run_engine(match):
    slug = f"{match['home']}-{match['away']}".lower().replace(" ", "_").replace(".", "").replace("/", "")
    inp_path = os.path.join(BASE, f"match_input_14oct_{slug}.json")
    out_path = os.path.join(BASE, f"match_output_14oct_{slug}.json")
    with open(inp_path, "w", encoding="utf-8") as f:
        json.dump(match["input"], f, indent=2, ensure_ascii=False)
    subprocess.run(
        [sys.executable, ENGINE, "--input", inp_path, "--output", out_path, "--config", MODEL_CONFIG],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    with open(out_path, encoding="utf-8") as f:
        return json.load(f)


def build_pick_detail(cand, ctx):
    from render_artifact import market_label  # noqa: E402
    label = market_label(cand["market"], cand["home_team"], cand["away_team"])
    base = ctx["why_base"]
    why = (
        f"{base} El motor model-v1.3 estima {cand['model_prob']:.1%} para '{label}' "
        f"frente a una probabilidad implicita de {cand['implied_prob']:.1%} (cuota {cand['odds']:.2f}); "
        f"edge {cand['edge']:+.2f}% y EV robusto {cand['robust_ev_percent']:+.2f}%."
    )
    min_odds = (1.0 / cand["conservative_prob"]) if cand.get("conservative_prob") else cand["fair_odds"]
    return {
        "match": cand["match"], "market": cand["market"],
        "min_odds": f"{min_odds:.2f}",
        "incertidumbre": "Base +/- 5.0% (model-v1.3) sobre muestras de 5-22 partidos segun liga",
        "why": why,
        "risks": ctx["risks"],
        "sources": f"{ctx['sources']}; verosimilitud del modelo y calibracion Platt (model-v1.3).",
    }


def main():
    all_results = []
    all_evaluations = []
    for match in MATCHES:
        if match["limited"]:
            all_results.append({
                "match": match["match"], "home_team": match["home"], "away_team": match["away"],
                "probabilities": {}, "evaluations": {}, "data_limited": True,
            })
            continue
        out = run_engine(match)
        evaluations = {}
        for key, ev in out["evaluations"].items():
            enriched = dict(ev)
            enriched["match"] = match["match"]
            enriched["home_team"] = match["home"]
            enriched["away_team"] = match["away"]
            evaluations[key] = enriched
            all_evaluations.append(enriched)
        all_results.append({
            "match": match["match"], "home_team": match["home"], "away_team": match["away"],
            "probabilities": out["probabilities"], "evaluations": evaluations,
        })

    all_candidates = [dict(e) for e in all_evaluations if e.get("has_value")]
    for c in all_candidates:
        c.setdefault("selection_profile", "excluido")
        c.setdefault("selection_reason", "Sin clasificar")

    selected, excluded = select_portfolio(list(all_candidates))

    ctx_by_match = {mt["match"]: mt for mt in MATCHES}
    picks_details = [build_pick_detail(s, ctx_by_match[s["match"]]) for s in selected]

    results = {
        "all_results": all_results,
        "all_candidates": all_candidates,
        "all_evaluations": all_evaluations,
        "selected": selected,
        "excluded": excluded,
    }
    with open(os.path.join(BASE, "results_14oct.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    now = datetime.now(timezone.utc)
    cutoff = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    meta = {
        "analysis_date_iso": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "match_dates_text": "14 de octubre de 2026",
        "information_cutoff": cutoff,
        "model_ia": "big-pickle",
        "engine_version": "model-v1.3",
        "leagues_display": "UEFA Champions League (fase de liga), MLS (Decision Day), Copa Libertadores y Copa Sudamericana (semifinales de ida)",
        "requested_range": "14 de octubre de 2026 - Champions League, MLS, Copa Libertadores y Copa Sudamericana (todos los partidos)",
        "universe_preamble": (
            "Universo = interseccion(ligas: Champions League + MLS + Copa Libertadores + Copa Sudamericana, fecha 14 de octubre de 2026, todos los partidos programados). "
            f"Cutoff de informacion {cutoff}, anterior al primer kickoff (Feyenoord-Como 16:45 UTC). No se usa informacion posterior a ningun kickoff. "
            "Universo final = 26 partidos (9 de Champions League fase de liga, 15 de MLS en jornada de Decision Day, 1 semifinal de ida de Copa Libertadores y 1 semifinal de ida de Copa Sudamericana; "
            "las semifinales de CONMEBOL se juegan el 15/10 a las 00:30 UTC, es decir dentro de la fecha solicitada). "
            "MCPs inoperativos en esta sesion: apifootball/odds-api/football-stats no expuestos y api.clubelo.com sin acceso de red, por lo que toda la recoleccion se hizo via web (agente): "
            "querostats.com, statz.ai, footystats.org, oddalerts.com, pitchmath.com, footymetrics.com, statmuse.com, clubelo.com, ESPN, FOX Sports, bettingview.com y oddschecker. "
            "Las tasas de corners y tarjetas for/against constan en cada match_input cuando estuvieron disponibles; donde las cuotas O/U no estaban cotizadas se marcan n/d (no se inventan). "
            "ADVERTENCIAS DE DATOS: (1) Bodø/Glimt vs Dortmund requirio arbitraje: el xG de 0.20 publicado por ESPN/FOX correspondia a un unico partido de UCL (0-5 vs Bayern) y no a su liga domestica, "
            "por lo que se adopto la ventana domestica (statz 2.90/0.73; footystats 2.28 como tercera opinion) con incertidumbre elevada y documentada. "
            "(2) Slovan Bratislava: el xG de 0.64 era tambien de un solo partido de UCL; se adopto footystats de la liga eslovaca (1.91/1.15) como unica fuente domestica disponible. "
            "(3) Atletico Mineiro vs Montevideo City Torque queda como NO BET por datos insuficientes: el club uruguayo no tiene xG por partido ni rating Elo en ninguna fuente consultada, "
            "y ejecutar el motor habria exigido priors por defecto para el visitante."
        ),
        "universe_matches": [
            "1. **Champions League:** Feyenoord vs Como (16:45 UTC). 1X2 3.30/3.90/1.91; O/U 1.5 1.12/6.00, 2.5 1.44/2.75, 3.5 2.00/1.75; BTTS 1.40. Elo 1724/1807; xG 2.47/0.98 vs 1.97/1.44.",
            "2. **Champions League:** LASK vs Liverpool (16:45 UTC). 1X2 9.39/6.16/1.29; O/U 2.5 1.34; BTTS 1.59. Elo 1628/1929; xG 0.72/1.71 vs 1.56/1.19.",
            "3. **Champions League:** Real Betis vs FC Porto (19:00 UTC). 1X2 2.16/3.76/3.50; O/U 2.5 1.79/2.19; BTTS 1.61. Elo 1823/1842; xG 1.77/1.75 vs 2.12/1.06.",
            "4. **Champions League:** Aston Villa vs Fenerbahce (19:00 UTC). 1X2 1.70/4.10/4.50; O/U 1.5 1.17/5.00, 2.5 1.57/2.38, 3.5 2.38/1.57; DC 1X 1.17 / X2 2.25 / 12 1.22; BTTS 1.57/2.35; corners 8.5 y 9.5. Elo 1893/1785; xG 1.43/1.64 vs 2.05/1.09.",
            "5. **Champions League:** Shakhtar Donetsk vs AEK Athens (19:00 UTC, Stamford Bridge). 1X2 2.77/3.37/2.67; O/U 2.5 1.95/1.95; BTTS 1.70/2.25; corners 8.5 capturada. Elo 1692/1708; xG 0.62/0.44 vs 1.71/0.72.",
            "6. **Champions League:** Roma vs Real Madrid (19:00 UTC). 1X2 3.65/3.95/1.91; O/U 3.5 2.10/1.74; BTTS 1.39/3.00; DC 1X 1.91 / X2 1.33 / 12 1.28; corners 8.5 y 9.5. Elo 1856/1975; xG 2.25/1.12 vs 2.41/1.20.",
            "7. **Champions League:** Manchester City vs Paris Saint-Germain (19:00 UTC). 1X2 2.00/4.00/3.30; O/U 3.5 2.05/1.77; BTTS 1.40/2.95; corners 8.5 y 9.5. Elo 2034/1957; xG 2.03/1.44 vs 2.45/1.09.",
            "8. **Champions League:** Slovan Bratislava vs VfB Stuttgart (19:00 UTC). 1X2 7.50/5.75/1.35; O/U 3.5 1.83/1.95; BTTS 1.57/2.40; corners 8.5 y 9.5. Elo 1551/1824; xG 1.91/1.15 (domestico, arbitrado) vs 1.94/2.08.",
            "9. **Champions League:** Bodo/Glimt vs Borussia Dortmund (19:00 UTC). 1X2 3.00/3.95/2.20; O/U 3.5 1.95/1.87; BTTS 1.33/3.30; corners 8.5 y 9.5. Elo 1781/1895; xG 2.90/0.73 (domestico, arbitrado) vs 1.79/0.92.",
            "10. **Copa Libertadores (semifinal ida):** Fluminense vs Palmeiras (15/10 00:30 UTC). 1X2 2.87/3.10/2.62; O/U 1.5 1.57/2.25, 2.5 2.87/1.40, 3.5 6.00/1.13; BTTS 2.25/1.57; DC 1X 1.49 / X2 1.46 / 12 1.36; DNB 1.90/1.80; corners 9.5 1.80/1.90. Elo 1769/1856; xG 1.46/1.38 vs 1.85/1.01.",
            "11. **Copa Sudamericana (semifinal ida):** Atletico Mineiro vs Montevideo City Torque (15/10 00:30 UTC). 1X2 1.40/4.20/9.50; O/U 1.5 1.30/3.40, 2.5 2.00/1.80, 3.5 3.35/1.24; BTTS 2.25/1.57; corners 9.5 1.83/1.83. DATOS INSUFICIENTES (sin xG del visitante ni Elo) -> NO BET.",
            "12. **MLS:** CF Montreal vs Atlanta United (23:30 UTC). 1X2 2.50/3.80/2.85; O/U 2.5 1.54; BTTS 1.50/2.70; DC 1X 1.47 / X2 1.63 / 12 1.28; DNB 1.80/2.18; tarjetas 4.5 2.10/1.63. Elo 1486/1508; xG 1.40/1.57 vs 1.36/1.53.",
            "13. **MLS:** Columbus Crew vs Charlotte FC (23:30 UTC). 1X2 2.00/4.00/3.60; O/U 2.5 1.52/2.48; BTTS 1.46/2.95; DC 1X 1.36 / X2 1.82 / 12 1.26; DNB 1.57/2.62; tarjetas 4.5 2.10/1.63. Elo 1595/1609; xG 1.21/1.19 vs 1.53/1.44.",
            "14. **MLS:** DC United vs New York Red Bulls (23:30 UTC). 1X2 2.20/4.10/3.50; BTTS 1.49/2.64; DC 1X 1.39 / X2 1.87 / 12 1.27; DNB 1.45/2.84; tarjetas 4.5 2.10/1.63. Elo 1494/1551; xG 1.44/1.53 vs 1.59/2.01.",
            "15. **MLS:** FC Cincinnati vs New England Revolution (23:30 UTC). 1X2 1.95/4.60/4.20; O/U 3.5 1.91/1.95; BTTS 1.37/3.05; DC 1X 1.32 / X2 2.15 / 12 1.24; DNB 1.49/3.35; tarjetas 3.5 1.63/2.10. Elo 1603/1559; xG 1.74/1.77 vs 1.56/1.30.",
            "16. **MLS:** Inter Miami vs New York City FC (23:30 UTC). 1X2 1.59/4.80/5.25; O/U 3.5 1.80/1.96; BTTS 1.43/2.90; DC 1X 1.17 / X2 2.38; DNB 1.29/4.10; tarjetas 4.5 2.10/1.63. Elo 1684/1592; xG 2.05/1.62 vs 1.25/1.50.",
            "17. **MLS:** Toronto FC vs Orlando City (23:30 UTC). 1X2 2.35/3.90/2.85; O/U 3.5 2.02/1.87; BTTS 1.39/3.30; DC 1X 1.47 / X2 1.66 / 12 1.27; DNB 1.74/2.20; tarjetas 4.5 2.00/1.62. Elo 1520/1595; xG 1.18/1.46 vs 1.54/1.92.",
            "18. **MLS:** Chicago Fire vs Philadelphia Union (15/10 00:30 UTC). 1X2 2.60/4.10/2.60; O/U 3.5 2.05/1.95; BTTS 1.40/3.10; DC 1X 1.54 / X2 1.54 / 12 1.27; DNB 2.00/1.89; tarjetas 4.5 1.80/1.78. Elo 1605/1649; xG 1.81/1.31 vs 1.93/1.37.",
            "19. **MLS:** FC Dallas vs Seattle Sounders (15/10 00:30 UTC). 1X2 1.98/4.10/4.00; BTTS 1.55/2.60; DC 1X 1.31 / X2 1.97 / 12 1.25; DNB 1.47/2.92; tarjetas 3.5 1.72/1.88. Elo 1605/1623; xG 1.50/1.38 vs 1.34/1.37.",
            "20. **MLS:** Nashville SC vs Sporting Kansas City (15/10 00:30 UTC). 1X2 1.29/6.50/10.00; O/U 2.5 1.29/3.50, 3.5 1.76/2.00; BTTS 1.77/2.18; DC 1X 1.07 / X2 4.40 / 12 1.11; DNB 1.08/10.40; tarjetas 3.5 2.05/1.60. Elo 1690/1457; xG 1.62/1.30 vs 1.19/1.99.",
            "21. **MLS:** St. Louis CITY vs Vancouver Whitecaps (15/10 00:30 UTC). 1X2 2.30/4.00/3.00; O/U 1.5 1.14/5.50, 2.5 1.50/2.50, 3.5 2.20/1.62; BTTS 1.48/2.85; DC 1X 1.44 / X2 1.72 / 12 1.26; DNB 1.72/2.30; tarjetas 4.5 1.92/1.68. Elo 1626/1653; xG 1.59/1.23 vs 2.18/1.10.",
            "22. **MLS:** Colorado Rapids vs Minnesota United (15/10 01:30 UTC). 1X2 2.05/3.60/3.20; O/U 2.5 1.61/2.30; BTTS 1.53/2.50; corners 8.5 1.50/2.45 y 9.5 1.83/1.87. Elo 1540/1561; xG 1.51/1.19 vs 1.73/1.64.",
            "23. **MLS:** Real Salt Lake vs San Jose Earthquakes (15/10 01:30 UTC). 1X2 1.91/3.85/3.35; O/U 2.5 1.48/2.75, 3.5 2.15/1.69; BTTS 1.43/2.80; corners 8.5 1.31/3.15, 9.5 1.54/2.35, 10.5 1.87/1.83. Elo 1541/1568; xG 1.37/1.50 vs 1.84/1.37.",
            "24. **MLS:** LA Galaxy vs Portland Timbers (15/10 02:30 UTC). 1X2 2.00/3.80/3.10; O/U 2.5 1.40/3.20, 3.5 2.00/1.80; BTTS 1.35/3.15; corners 8.5 1.45/2.55, 9.5 1.74/1.95. Elo 1547/1555; xG 1.53/1.71 vs 1.51/1.63.",
            "25. **MLS:** LAFC vs Austin FC (15/10 02:30 UTC). 1X2 1.43/4.60/6.00; O/U 2.5 1.57/2.35, 3.5 2.35/1.59. Elo 1652/1540; xG 1.47/1.42 vs 1.03/2.04.",
            "26. **MLS:** San Diego FC vs Houston Dynamo (15/10 02:30 UTC). 1X2 2.10/3.55/3.05; O/U 2.5 1.65/2.20; BTTS 1.52/2.39; DC 1X 1.27 / X2 1.84 / 12 1.24. Elo 1600/1588; xG 1.57/1.70 vs 1.12/1.36.",
        ],
        "picks_details": picks_details,
        "data_limited_reasons": {
            "Atletico Mineiro vs Montevideo City Torque": (
                "Montevideo City Torque (Uruguay) no tiene xG por partido ni rating Elo en ninguna fuente consultada "
                "(statz.ai, understat y xg-edge no cubren la liga uruguaya). Ejecutar el motor habria exigido priors por "
                "defecto para el visitante, por lo que no se ejecuto."
            ),
        },
        "fallback_source": (
            "MCPs no operativos (apifootball/odds-api/football-stats sin herramientas; api.clubelo.com sin acceso de red desde bash). "
            "Investigacion web del agente: querostats.com, statz.ai, footystats.org, oddalerts.com, pitchmath.com, footymetrics.com, statmuse.com (xG y corners/tarjetas), "
            "clubelo.com (Elo), ESPN, FOX Sports, bettingview.com, oddschecker.com y oddsportal.com (cuotas). "
            "Motor calc_engine.py model-v1.3 con calibracion Platt (mercados 1, 2, O/U 2.5 y O/U 3.5). "
            "Conflictos de xG arbitrados y documentados (Bodo/Glimt, Slovan Bratislava); partidos sin xG verificable no se ejecutaron en el motor."
        ),
    }
    with open(os.path.join(BASE, "meta_14oct.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print("results_14oct.json y meta_14oct.json escritos")
    print(f"universo: {len(all_results)} | candidatos con value: {len(all_candidates)} | seleccionados: {len(selected)}")
    for s in selected:
        print(f"  - {s['match']} | {s['market']} | cuota {s['odds']} | p {s['model_prob']:.3f} | robEV {s['robust_ev_percent']:+.2f}% | {s.get('selection_profile')}")


if __name__ == "__main__":
    main()
