# Análisis de Apuestas — 13 de octubre de 2026

## Metadatos
- **Fecha de análisis:** 2026-10-13T14:51:45Z
- **Fecha(s) de partido:** 13 de octubre de 2026
- **Information cutoff:** 2026-10-13T14:51:45Z
- **Modelo de IA:** big-pickle
- **Versión del motor predictivo:** model-v1.3
- **Ligas analizadas:** UEFA Champions League (fase de liga) y Primera A de Colombia (Clausura)
- **Rango de fechas solicitado:** 13 de octubre de 2026 - Liga Colombiana, Champions League y Copa Sudamericana (todos los partidos)
- **Partidos en universo:** 10
- **Picks iniciales con value:** 45
- **Picks finales seleccionados:** 6

## Universo Analizado
Universo = interseccion(ligas: liga colombiana + champions league + copa sudamericana, fecha 13 de octubre de 2026, todos los partidos programados). Cutoff de informacion 2026-10-13T14:51:45Z, anterior al primer kickoff (Lens-Sporting 16:45 UTC). No se usa informacion posterior a ningun kickoff. Copa Sudamericana NO tiene partidos el 13/10/2026 (verificado en calendario): 0 partidos. Universo final = 10 partidos (9 de Champions League fase de liga + 1 de Primera A Colombia). MCPs inoperativos en esta sesion: apifootball/odds-api/football-stats no expuestos, soccer-mcp ausente, the-odds-api HTTP 401 y api.clubelo.com inaccesible; por ello la investigacion se realizo via web (agente): xg-edge, footymetrics, querostats, statz.ai, sportsgambler, 1x2.expert, 24score, wincomparator, foxsports, clubelo.com. Las tasas de corners/tarjetas for/against constan en cada match_input cuando estuvieron disponibles; donde las cuotas O/U de corners/tarjetas no estaban cotizadas, se marcan n/d (no se inventan). ADVERTENCIA DE DATOS: 3 partidos (Lens-Sporting, Sabah-Slavia, Viking-Bayern) NO tienen xG/goals verificables; para evitar publicar probabilidades basadas en priors por defecto del motor, NO se ejecuto el motor en ellos: figuran como NO BET por datos insuficientes (probabilidades n/d en la tabla O/U).
1. **Champions League:** Lens vs Sporting CP (16:45 UTC). 1X2 2.36/3.50/2.70; O/U 2.5 1.56/2.35 (foxsports). Elo Lens 1817 / Sporting 1876. DATOS INSUFICIENTES (sin xG/goals ni corners/tarjetas) -> NO BET.
2. **Champions League:** Sabah FK vs Slavia Prague (16:45 UTC). 1X2 3.50/3.75/1.92; O/U 2.5 1.62/2.15; BTTS 1.54/2.25 (wincomparator). Sin Elo ni xG -> NO BET por datos insuficientes.
3. **Champions League:** Arsenal vs Lille (19:00 UTC). 1X2 1.22/7.00/13.00; O/U 1.5 1.17/5.00, 2.5 1.53/2.50, 3.5 2.30/1.62; BTTS 2.10/1.67; corners y tarjetas O/U capturadas. Elo 2043/1782; xG 1.84/0.79 vs 1.36/1.68.
4. **Champions League:** Atletico Madrid vs Manchester United (19:00 UTC). 1X2 1.925/3.96/3.54; O/U 1.5 1.12/4.70, 2.5 1.50/2.70, 3.5 2.39/1.68; BTTS 1.47/2.53; DNB 1.42/3.00. Elo 1907/1876; xG 1.76/1.05 vs 1.74/1.43.
5. **Champions League:** Villarreal vs Napoli (19:00 UTC). 1X2 2.20/3.65/3.10; O/U 1.5 1.20/4.50, 2.5 1.63/2.25, 3.5 2.50/1.50; BTTS 1.61/2.65; DC 1X 1.32 / X2 1.74; DNB 1.56/2.54. Elo 1797/1839; xG 2.16/1.22 vs 1.66/1.34.
6. **Champions League:** Galatasaray vs Barcelona (19:00 UTC). 1X2 8.25/6.21/1.26; O/U 1.5 1.05/11.0, 2.5 1.20/5.0, 3.5 1.51/2.63; BTTS 1.39/2.82; DNB 5.79/1.11; DC 1X 3.48 / X2 1.05 / 12 1.10. Elo 1798/2026; xG 2.37/1.03 vs 3.81/0.97.
7. **Champions League:** Inter Milan vs Club Brugge (19:00 UTC). 1X2 1.25/6.00/10.00; O/U 1.5 1.10/7.0, 2.5 1.37/3.10, 3.5 2.34/1.64; BTTS 1.73/2.05; DC 1X 1.04 / X2 3.80 / 12 1.12; DNB 1.06/7.00. Elo 1949/1812; xG 2.42/1.23 vs 2.40/1.01.
8. **Champions League:** RB Leipzig vs PSV Eindhoven (19:00 UTC). 1X2 1.60/4.90/4.50; O/U 2.5 1.27/3.75; BTTS 1.34/3.15; DC 1X 1.20 / X2 2.32 / 12 1.17; DNB 1.27/3.30. Elo 1825/1787; xG 2.27/1.40 vs 2.60/1.25.
9. **Champions League:** Viking FK vs Bayern Munich (19:00 UTC). 1X2 17.63/n-d/1.10 (foxsports; linea cotizada 4.5). Sin xG ni Elo local -> NO BET por datos insuficientes.
10. **Primera A Colombia (Clausura):** Atletico Bucaramanga vs Aguilas Doradas Rionegro (23:30 UTC). 1X2 1.95/3.25/3.80; O/U 1.5 1.33/3.10, 2.5 2.10/1.70, 3.5 3.80/1.23; BTTS 1.84/1.85; DC 1X 1.25 / X2 1.77 / 12 1.29; DNB 1.43/2.65; corners O/U 8.5 y 9.5 capturadas. Elo 1637/1548; xG 0.96/1.05 vs 1.29/1.00.

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Galatasaray vs Barcelona | over_2_5 | Over 2.5 Goles | excluido | 1.20 | 89.6% | 1.12 | +7.53% | +7.53% | +1.53% | 0.09u | Media-Alta |
| 2 | RB Leipzig vs PSV Eindhoven | over_2_5 | Over 2.5 Goles | excluido | 1.27 | 85.8% | 1.17 | +8.92% | +8.92% | +2.57% | 0.08u | Media-Alta |
| 3 | Galatasaray vs Barcelona | over_3_5 | Over 3.5 Goles | prioritario | 1.51 | 82.8% | 1.21 | +25.09% | +25.09% | +17.54% | 0.12u | Media-Alta |
| 4 | Inter Milan vs Club Brugge | over_2_5 | Over 2.5 Goles | excluido | 1.37 | 82.3% | 1.22 | +12.74% | +12.74% | +5.89% | 0.09u | Media-Alta |
| 5 | Arsenal vs Lille | under_corners_10_5 | Under 10.5 Córners | excluido | 1.46 | 76.5% | 1.31 | +11.67% | +11.67% | +4.37% | 0.06u | Media-Alta |
| 6 | Villarreal vs Napoli | over_2_5 | Over 2.5 Goles | prioritario | 1.63 | 75.8% | 1.32 | +23.47% | +23.47% | +15.32% | 0.09u | Media-Alta |
| 7 | Atletico Madrid vs Manchester United | over_2_5 | Over 2.5 Goles | excluido | 1.50 | 71.0% | 1.41 | +6.48% | +6.48% | -1.02% | 0.03u | Media-Alta |
| 8 | Galatasaray vs Barcelona | under_corners_10_5 | Under 10.5 Córners | prioritario | 1.74 | 70.4% | 1.42 | +22.42% | +22.42% | +13.72% | 0.08u | Media-Alta |
| 9 | Inter Milan vs Club Brugge | over_3_5 | Over 3.5 Goles | excluido | 2.34 | 70.3% | 1.42 | +64.55% | +64.55% | +52.85% | 0.12u | Media-Alta |
| 10 | Inter Milan vs Club Brugge | btts_yes | Ambos marcan (BTTS) | prioritario | 1.73 | 69.1% | 1.45 | +19.59% | +19.59% | +10.94% | 0.07u | Media-Alta |
| 11 | Arsenal vs Lille | under_corners_9_5 | Under 9.5 Córners | prioritario | 1.80 | 68.3% | 1.46 | +23.01% | +23.01% | +14.01% | 0.07u | Media-Alta |
| 12 | Atletico Bucaramanga vs Aguilas Doradas Rionegro | x2 | Doble Oportunidad Empate/Aguilas Doradas Rionegro | prioritario | 1.77 | 66.7% | 1.50 | +18.11% | +18.11% | +9.26% | 0.06u | Media-Alta |
| 13 | RB Leipzig vs PSV Eindhoven | x2 | Doble Oportunidad Empate/PSV Eindhoven | excluido | 2.32 | 66.5% | 1.50 | +54.37% | +54.37% | +42.77% | 0.10u | Media-Alta |
| 14 | Inter Milan vs Club Brugge | x2 | Doble Oportunidad Empate/Club Brugge | excepcional | 3.80 | 60.1% | 1.66 | +128.38% | +128.38% | +109.38% | 0.11u | Media-Alta |
| 15 | Villarreal vs Napoli | over_3_5 | Over 3.5 Goles | excluido | 2.50 | 59.6% | 1.68 | +49.02% | +49.02% | +36.52% | 0.08u | Media-Alta |
| 16 | Arsenal vs Lille | under_corners_8_5 | Under 8.5 Córners | excluido | 2.30 | 58.7% | 1.70 | +35.01% | +35.01% | +23.51% | 0.07u | Media-Alta |
| 17 | Villarreal vs Napoli | over_corners_9_5 | Over 9.5 Córners | excluido | 1.95 | 57.7% | 1.73 | +12.51% | +12.51% | +2.76% | 0.03u | Media |
| 18 | Atletico Madrid vs Manchester United | over_cards_3_5 | Over 3.5 Tarjetas | excluido | 1.87 | 56.6% | 1.77 | +5.91% | +5.91% | -3.44% | 0.02u | Media |
| 19 | Arsenal vs Lille | over_cards_3_5 | Over 3.5 Tarjetas | excluido | 2.16 | 53.5% | 1.87 | +15.62% | +15.62% | +4.82% | 0.03u | Media |
| 20 | Arsenal vs Lille | btts_yes | Ambos marcan (BTTS) | excluido | 2.10 | 52.6% | 1.90 | +10.54% | +10.54% | +0.04% | 0.02u | Media |
| 21 | Atletico Bucaramanga vs Aguilas Doradas Rionegro | under_corners_8_5 | Under 8.5 Córners | excluido | 2.02 | 52.4% | 1.91 | +5.93% | +5.93% | -4.17% | 0.01u | Media |
| 22 | Atletico Madrid vs Manchester United | over_3_5 | Over 3.5 Goles | excluido | 2.39 | 52.3% | 1.91 | +25.02% | +25.02% | +13.07% | 0.05u | Media |
| 23 | Arsenal vs Lille | over_3_5 | Over 3.5 Goles | excluido | 2.30 | 46.2% | 2.16 | +6.31% | +6.31% | -5.19% | 0.01u | Baja |
| 24 | RB Leipzig vs PSV Eindhoven | 2 | Victoria PSV Eindhoven | excepcional | 4.50 | 44.8% | 2.23 | +101.73% | +101.73% | +79.23% | 0.07u | Baja |
| 25 | RB Leipzig vs PSV Eindhoven | dnb_away | DNB PSV Eindhoven | excepcional | 3.30 | 44.8% | 1.75 | +69.66% | +69.66% | +53.16% | 0.08u | Baja |
| 26 | Inter Milan vs Club Brugge | 2 | Victoria Club Brugge | excepcional | 10.00 | 38.0% | 2.63 | +280.20% | +280.20% | +230.20% | 0.08u | Baja |
| 27 | Inter Milan vs Club Brugge | dnb_away | DNB Club Brugge | excepcional | 7.00 | 38.0% | 2.05 | +188.22% | +188.22% | +153.22% | 0.08u | Baja |
| 28 | Arsenal vs Lille | over_cards_4_5 | Over 4.5 Tarjetas | excepcional | 3.50 | 38.0% | 2.63 | +33.07% | +33.07% | +15.57% | 0.03u | Baja |
| 29 | Atletico Bucaramanga vs Aguilas Doradas Rionegro | 2 | Victoria Aguilas Doradas Rionegro | excepcional | 3.80 | 37.0% | 2.70 | +40.64% | +40.64% | +21.64% | 0.04u | Baja |
| 30 | Atletico Bucaramanga vs Aguilas Doradas Rionegro | dnb_away | DNB Aguilas Doradas Rionegro | excluido | 2.65 | 37.0% | 1.90 | +27.80% | +27.80% | +14.55% | 0.04u | Baja |
| 31 | Galatasaray vs Barcelona | 1x | Doble Oportunidad Galatasaray/Empate | excluido | 3.48 | 36.2% | 2.76 | +25.94% | +25.94% | +8.54% | 0.03u | Baja |
| 32 | Atletico Bucaramanga vs Aguilas Doradas Rionegro | under_1_5 | Under 1.5 Goles | excluido | 3.10 | 35.9% | 2.79 | +11.26% | +11.26% | -4.24% | 0.01u | Baja |
| 33 | Arsenal vs Lille | x2 | Doble Oportunidad Empate/Lille | excepcional | 4.00 | 35.1% | 2.85 | +40.52% | +40.52% | +20.52% | 0.03u | Baja |
| 34 | Villarreal vs Napoli | dnb_away | DNB Napoli | excluido | 2.54 | 31.2% | 2.43 | +3.44% | +3.44% | -9.26% | 0.01u | Baja |
| 35 | Atletico Madrid vs Manchester United | dnb_away | DNB Manchester United | excluido | 3.00 | 30.9% | 2.44 | +17.43% | +17.43% | +2.43% | 0.02u | Baja |
| 36 | Atletico Madrid vs Manchester United | 2 | Victoria Manchester United | excluido | 3.54 | 30.9% | 3.24 | +9.32% | +9.32% | -8.38% | 0.01u | Baja |
| 37 | Arsenal vs Lille | over_cards_5_5 | Over 5.5 Tarjetas | excluido | 6.05 | 25.4% | 3.93 | +54.00% | +54.00% | +23.75% | 0.03u | Baja |
| 38 | Inter Milan vs Club Brugge | X | Empate | excluido | 6.00 | 22.1% | 4.53 | +32.48% | +32.48% | +2.48% | 0.02u | Baja |
| 39 | Arsenal vs Lille | X | Empate | excluido | 7.00 | 22.0% | 4.54 | +54.28% | +54.28% | +19.28% | 0.02u | Baja |
| 40 | Arsenal vs Lille | under_1_5 | Under 1.5 Goles | excluido | 5.00 | 21.9% | 4.57 | +9.50% | +9.50% | -15.50% | 0.01u | Baja |
| 41 | RB Leipzig vs PSV Eindhoven | X | Empate | excluido | 4.90 | 21.7% | 4.60 | +6.43% | +6.43% | -18.07% | 0.00u | Baja |
| 42 | Galatasaray vs Barcelona | X | Empate | excluido | 6.21 | 19.4% | 5.15 | +20.66% | +20.66% | -10.39% | 0.01u | Baja |
| 43 | Galatasaray vs Barcelona | 1 | Victoria Galatasaray | excluido | 8.25 | 16.8% | 5.97 | +38.27% | +38.27% | -2.98% | 0.01u | Baja |
| 44 | Galatasaray vs Barcelona | dnb_home | DNB Galatasaray | excluido | 5.79 | 16.8% | 4.81 | +16.47% | +16.47% | -12.48% | 0.01u | Baja |
| 45 | Arsenal vs Lille | 2 | Victoria Lille | excluido | 13.00 | 13.1% | 7.64 | +70.17% | +70.17% | +5.17% | 0.01u | Baja |

## Evaluación Over/Under por Partido
Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada (n/d = cuota no disponible en la corrida).
| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |
|---|---|---|---:|---:|---:|---:|---:|---|
| Arsenal vs Lille | 1.5 | 78.1% | 1.17 | -8.62% | 21.9% | 5.00 | +9.50% | Value Under |
| Arsenal vs Lille | 2.5 | 66.8% | 1.53 | +2.20% | 33.2% | 2.50 | -17.00% | Sin value |
| Arsenal vs Lille | 3.5 | 46.2% | 2.30 | +6.31% | 53.8% | 1.62 | -12.88% | Value Over |
| Atletico Madrid vs Manchester United | 1.5 | 80.6% | 1.12 | -9.74% | 19.4% | 4.70 | -8.77% | Sin value |
| Atletico Madrid vs Manchester United | 2.5 | 71.0% | 1.50 | +6.48% | 29.0% | 2.70 | -21.67% | Value Over |
| Atletico Madrid vs Manchester United | 3.5 | 52.3% | 2.39 | +25.02% | 47.7% | 1.68 | -19.88% | Value Over |
| Villarreal vs Napoli | 1.5 | 83.4% | 1.20 | +0.02% | 16.7% | 4.50 | -25.07% | Sin value |
| Villarreal vs Napoli | 2.5 | 75.8% | 1.63 | +23.47% | 24.2% | 2.25 | -45.44% | Value Over |
| Villarreal vs Napoli | 3.5 | 59.6% | 2.50 | +49.02% | 40.4% | 1.50 | -39.41% | Value Over |
| Galatasaray vs Barcelona | 1.5 | 91.8% | 1.05 | -3.56% | 8.2% | 11.00 | -10.35% | Sin value |
| Galatasaray vs Barcelona | 2.5 | 89.6% | 1.20 | +7.53% | 10.4% | 5.00 | -48.05% | Value Over |
| Galatasaray vs Barcelona | 3.5 | 82.8% | 1.51 | +25.09% | 17.2% | 2.63 | -54.87% | Value Over |
| Inter Milan vs Club Brugge | 1.5 | 87.3% | 1.10 | -4.01% | 12.7% | 7.00 | -10.82% | Sin value |
| Inter Milan vs Club Brugge | 2.5 | 82.3% | 1.37 | +12.74% | 17.7% | 3.10 | -45.10% | Value Over |
| Inter Milan vs Club Brugge | 3.5 | 70.3% | 2.34 | +64.55% | 29.7% | 1.64 | -51.32% | Value Over |
| RB Leipzig vs PSV Eindhoven | 1.5 | 89.4% | n/d | n/d | 10.6% | n/d | n/d | Cuotas no capturadas |
| RB Leipzig vs PSV Eindhoven | 2.5 | 85.8% | 1.27 | +8.92% | 14.2% | 3.75 | -46.60% | Value Over |
| RB Leipzig vs PSV Eindhoven | 3.5 | 76.2% | n/d | n/d | 23.8% | n/d | n/d | Cuotas no capturadas |
| Atletico Bucaramanga vs Aguilas Doradas Rionegro | 1.5 | 64.1% | 1.33 | -14.73% | 35.9% | 3.10 | +11.26% | Value Under |
| Atletico Bucaramanga vs Aguilas Doradas Rionegro | 2.5 | 43.4% | 2.10 | -8.88% | 56.6% | 1.70 | -3.76% | Sin value |
| Atletico Bucaramanga vs Aguilas Doradas Rionegro | 3.5 | 19.7% | 3.80 | -25.03% | 80.3% | 1.23 | -1.27% | Sin value |
| Lens vs Sporting CP | 1.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Lens vs Sporting CP | 2.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Lens vs Sporting CP | 3.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Sabah FK vs Slavia Prague | 1.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Sabah FK vs Slavia Prague | 2.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Sabah FK vs Slavia Prague | 3.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Viking FK vs Bayern Munich | 1.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Viking FK vs Bayern Munich | 2.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Viking FK vs Bayern Munich | 3.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |

## Picks Recomendados (Top 6)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Galatasaray vs Barcelona | over_3_5 | Over 3.5 Goles | prioritario | 1.51 | 82.8% | 1.21 | +25.09% | +25.09% | +17.54% | 0.12u | Media-Alta |
| 2 | Villarreal vs Napoli | over_2_5 | Over 2.5 Goles | prioritario | 1.63 | 75.8% | 1.32 | +23.47% | +23.47% | +15.32% | 0.09u | Media-Alta |
| 3 | Galatasaray vs Barcelona | under_corners_10_5 | Under 10.5 Córners | prioritario | 1.74 | 70.4% | 1.42 | +22.42% | +22.42% | +13.72% | 0.08u | Media-Alta |
| 4 | Inter Milan vs Club Brugge | btts_yes | Ambos marcan (BTTS) | prioritario | 1.73 | 69.1% | 1.45 | +19.59% | +19.59% | +10.94% | 0.07u | Media-Alta |
| 5 | Arsenal vs Lille | under_corners_9_5 | Under 9.5 Córners | prioritario | 1.80 | 68.3% | 1.46 | +23.01% | +23.01% | +14.01% | 0.07u | Media-Alta |
| 6 | Atletico Bucaramanga vs Aguilas Doradas Rionegro | x2 | Doble Oportunidad Empate/Aguilas Doradas Rionegro | prioritario | 1.77 | 66.7% | 1.50 | +18.11% | +18.11% | +9.26% | 0.06u | Media-Alta |

## Detalle de Picks
### Pick 1: Galatasaray vs Barcelona
- **Mercado:** over_3_5
- **Selección:** Over 3.5 Goles
- **Cuota:** 1.51
- **Probabilidad modelo:** 82.8%
- **Probabilidad conservadora:** 77.8%
- **Probabilidad implícita:** 66.2%
- **Cuota justa:** 1.21
- **Edge:** +25.09%
- **EV:** +25.09%
- **EV robusto:** +17.54%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.28
- **Stake:** 0.12u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestra corta de xG (n aprox. 5-8)
- **Por qué:** Barcelona muy favorito (Elo 2026 vs 1798) y con xG a favor extremo (3.81) segun el proveedor consultado. El motor model-v1.3 estima 82.8% para 'Over 3.5 Goles' frente a una probabilidad implicita de 66.2% (cuota 1.51); edge +25.09% y EV robusto +17.54%.
- **Riesgos:** xG away de 3.81 inusualmente alto (posible muestra corta del proveedor); tarjetas incompletas (2 de 4 tasas); cuotas de un solo agregador.
- **Fuentes:** investigacion web del agente (agregadores de cuotas y xG), clubelo.com (Elo); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 2: Villarreal vs Napoli
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.63
- **Probabilidad modelo:** 75.8%
- **Probabilidad conservadora:** 70.8%
- **Probabilidad implícita:** 61.4%
- **Cuota justa:** 1.32
- **Edge:** +23.47%
- **EV:** +23.47%
- **EV robusto:** +15.32%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.41
- **Stake:** 0.09u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestra corta de xG (n aprox. 5-8)
- **Por qué:** Villarreal con alto xG a favor (2.16) y corners altos; Elo ligeramente favorable al Napoli (1839 vs 1797). El motor model-v1.3 estima 75.8% para 'Over 2.5 Goles' frente a una probabilidad implicita de 61.4% (cuota 1.63); edge +23.47% y EV robusto +15.32%.
- **Riesgos:** Cuotas de corners/tarjetas parciales; linea 12 y varias lineas O/U no cotizadas; bookmakers mezclados (novibet/betimate/ats.io).
- **Fuentes:** xg-edge.com (xG), footymetrics.com (corners/tarjetas/goals), novibet/betimate/ats.io (cuotas), clubelo.com (Elo); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 3: Galatasaray vs Barcelona
- **Mercado:** under_corners_10_5
- **Selección:** Under 10.5 Córners
- **Cuota:** 1.74
- **Probabilidad modelo:** 70.4%
- **Probabilidad conservadora:** 65.4%
- **Probabilidad implícita:** 57.5%
- **Cuota justa:** 1.42
- **Edge:** +22.42%
- **EV:** +22.42%
- **EV robusto:** +13.72%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.53
- **Stake:** 0.08u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestra corta de xG (n aprox. 5-8)
- **Por qué:** Barcelona muy favorito (Elo 2026 vs 1798) y con xG a favor extremo (3.81) segun el proveedor consultado. El motor model-v1.3 estima 70.4% para 'Under 10.5 Córners' frente a una probabilidad implicita de 57.5% (cuota 1.74); edge +22.42% y EV robusto +13.72%.
- **Riesgos:** xG away de 3.81 inusualmente alto (posible muestra corta del proveedor); tarjetas incompletas (2 de 4 tasas); cuotas de un solo agregador.
- **Fuentes:** investigacion web del agente (agregadores de cuotas y xG), clubelo.com (Elo); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 4: Inter Milan vs Club Brugge
- **Mercado:** btts_yes
- **Selección:** Ambos marcan (BTTS)
- **Cuota:** 1.73
- **Probabilidad modelo:** 69.1%
- **Probabilidad conservadora:** 64.1%
- **Probabilidad implícita:** 57.8%
- **Cuota justa:** 1.45
- **Edge:** +19.59%
- **EV:** +19.59%
- **EV robusto:** +10.94%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.56
- **Stake:** 0.07u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestra corta de xG (n aprox. 5-8)
- **Por qué:** Inter favorito claro (Elo 1949 vs 1812) con xG alto (2.42) y Brugge concediendo poco pero de liga menor. El motor model-v1.3 estima 69.1% para 'Ambos marcan (BTTS)' frente a una probabilidad implicita de 57.8% (cuota 1.73); edge +19.59% y EV robusto +10.94%.
- **Riesgos:** Fuentes de xG con conflicto (footystats vs statz); tarjetas de Brugge incompletas; solo linea 9.5 de corners cotizada.
- **Fuentes:** footystats.org + statz.ai (xG Inter), oddalerts.com (xG Brugge), sportsgambler.com (corners/goals/cuotas), thesoccerodds.com + pinnacle.com (cuotas), clubelo.com (Elo); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 5: Arsenal vs Lille
- **Mercado:** under_corners_9_5
- **Selección:** Under 9.5 Córners
- **Cuota:** 1.80
- **Probabilidad modelo:** 68.3%
- **Probabilidad conservadora:** 63.3%
- **Probabilidad implícita:** 55.6%
- **Cuota justa:** 1.46
- **Edge:** +23.01%
- **EV:** +23.01%
- **EV robusto:** +14.01%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.58
- **Stake:** 0.07u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestra corta de xG (n aprox. 5-8)
- **Por qué:** Arsenal muy superior en Elo (2043 vs 1782) y con xG a favor alto (1.84) frente a defensa de Lille vulnerable (xG contra 1.68). El motor model-v1.3 estima 68.3% para 'Under 9.5 Córners' frente a una probabilidad implicita de 55.6% (cuota 1.80); edge +23.01% y EV robusto +14.01%.
- **Riesgos:** Rotaciones de Champions; DNB no ofrecido (no cotizado); Lille con mejor rendimiento defensivo reciente en Ligue 1.
- **Fuentes:** xg-edge.com (xG), footymetrics.com (corners/tarjetas/goals), 1x2.expert + 24score.com (cuotas Bet365/MarathonBet), clubelo.com (Elo); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 6: Atletico Bucaramanga vs Aguilas Doradas Rionegro
- **Mercado:** x2
- **Selección:** Doble Oportunidad Empate/Aguilas Doradas Rionegro
- **Cuota:** 1.77
- **Probabilidad modelo:** 66.7%
- **Probabilidad conservadora:** 61.7%
- **Probabilidad implícita:** 56.5%
- **Cuota justa:** 1.50
- **Edge:** +18.11%
- **EV:** +18.11%
- **EV robusto:** +9.26%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.62
- **Stake:** 0.06u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestra corta de xG (n aprox. 5-8)
- **Por qué:** Bucaramanga local con mejor Elo (1637 vs 1548); partido de expectativa de goles baja (xG total ~2.25). El motor model-v1.3 estima 66.7% para 'Doble Oportunidad Empate/Aguilas Doradas Rionegro' frente a una probabilidad implicita de 56.5% (cuota 1.77); edge +18.11% y EV robusto +9.26%.
- **Riesgos:** Liga con menor cobertura estadistica; xG de proveedor unico; contextos de rotacion por calendario Clausura.
- **Fuentes:** statof.com, bzzoiro, clubelo.com (Elo y datos de temporada); verosimilitud del modelo y calibracion Platt (model-v1.3).

## NO BET / Excluidos
- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**
  - Arsenal vs Lille — Over 1.5 Goles (over_1_5): Prob modelo 78.1%, EV -8.62%, EV robusto -14.47% → sin value.
  - Arsenal vs Lille — Over 2.5 Goles (over_2_5): Prob modelo 66.8%, EV +2.20%, EV robusto -5.45% → sin value.
  - Arsenal vs Lille — Under 2.5 Goles (under_2_5): Prob modelo 33.2%, EV -17.00%, EV robusto -29.50% → sin value.
  - Arsenal vs Lille — Under 3.5 Goles (under_3_5): Prob modelo 53.8%, EV -12.88%, EV robusto -20.98% → sin value.
  - Arsenal vs Lille — Over 8.5 Córners (over_corners_8_5): Prob modelo 41.3%, EV -37.22%, EV robusto -44.82% → sin value.
  - Arsenal vs Lille — Over 9.5 Córners (over_corners_9_5): Prob modelo 31.7%, EV -39.84%, EV robusto -49.34% → sin value.
  - Arsenal vs Lille — Over 10.5 Córners (over_corners_10_5): Prob modelo 23.5%, EV -42.39%, EV robusto -54.64% → sin value.
  - Arsenal vs Lille — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 46.5%, EV -24.95%, EV robusto -33.02% → sin value.
  - Arsenal vs Lille — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 62.0%, EV -23.76%, EV robusto -29.91% → sin value.
  - Arsenal vs Lille — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 74.6%, EV -20.76%, EV robusto -26.07% → sin value.
  - Atletico Madrid vs Manchester United — Over 1.5 Goles (over_1_5): Prob modelo 80.6%, EV -9.74%, EV robusto -15.34% → sin value.
  - Atletico Madrid vs Manchester United — Under 1.5 Goles (under_1_5): Prob modelo 19.4%, EV -8.77%, EV robusto -32.27% → sin value.
  - Atletico Madrid vs Manchester United — Under 2.5 Goles (under_2_5): Prob modelo 29.0%, EV -21.67%, EV robusto -35.17% → sin value.
  - Atletico Madrid vs Manchester United — Under 3.5 Goles (under_3_5): Prob modelo 47.7%, EV -19.88%, EV robusto -28.28% → sin value.
  - Atletico Madrid vs Manchester United — Over 9.5 Córners (over_corners_9_5): Prob modelo 43.4%, EV -19.75%, EV robusto -29.00% → sin value.
  - Atletico Madrid vs Manchester United — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 43.4%, EV -20.64%, EV robusto -29.79% → sin value.
  - Villarreal vs Napoli — Over 1.5 Goles (over_1_5): Prob modelo 83.4%, EV +0.02%, EV robusto -5.98% → sin value.
  - Villarreal vs Napoli — Under 1.5 Goles (under_1_5): Prob modelo 16.7%, EV -25.07%, EV robusto -47.58% → sin value.
  - Villarreal vs Napoli — Under 2.5 Goles (under_2_5): Prob modelo 24.2%, EV -45.44%, EV robusto -56.69% → sin value.
  - Villarreal vs Napoli — Under 3.5 Goles (under_3_5): Prob modelo 40.4%, EV -39.41%, EV robusto -46.91% → sin value.
  - Villarreal vs Napoli — Under 9.5 Córners (under_corners_9_5): Prob modelo 42.3%, EV -21.74%, EV robusto -30.99% → sin value.
  - Villarreal vs Napoli — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 27.3%, EV -45.38%, EV robusto -55.38% → sin value.
  - Galatasaray vs Barcelona — Over 1.5 Goles (over_1_5): Prob modelo 91.8%, EV -3.56%, EV robusto -8.81% → sin value.
  - Galatasaray vs Barcelona — Under 1.5 Goles (under_1_5): Prob modelo 8.2%, EV -10.35%, EV robusto -65.35% → sin value.
  - Galatasaray vs Barcelona — Under 2.5 Goles (under_2_5): Prob modelo 10.4%, EV -48.05%, EV robusto -73.05% → sin value.
  - Galatasaray vs Barcelona — Under 3.5 Goles (under_3_5): Prob modelo 17.2%, EV -54.87%, EV robusto -68.02% → sin value.
  - Galatasaray vs Barcelona — Over 10.5 Córners (over_corners_10_5): Prob modelo 29.6%, EV -40.72%, EV robusto -50.72% → sin value.
  - Inter Milan vs Club Brugge — Over 1.5 Goles (over_1_5): Prob modelo 87.3%, EV -4.01%, EV robusto -9.51% → sin value.
  - Inter Milan vs Club Brugge — Under 1.5 Goles (under_1_5): Prob modelo 12.7%, EV -10.82%, EV robusto -45.82% → sin value.
  - Inter Milan vs Club Brugge — Under 2.5 Goles (under_2_5): Prob modelo 17.7%, EV -45.10%, EV robusto -60.60% → sin value.
  - Inter Milan vs Club Brugge — Under 3.5 Goles (under_3_5): Prob modelo 29.7%, EV -51.32%, EV robusto -59.52% → sin value.
  - Inter Milan vs Club Brugge — Over 9.5 Córners (over_corners_9_5): Prob modelo 53.7%, EV -1.22%, EV robusto -10.42% → sin value.
  - Inter Milan vs Club Brugge — Under 9.5 Córners (under_corners_9_5): Prob modelo 46.3%, EV -8.76%, EV robusto -18.61% → sin value.
  - RB Leipzig vs PSV Eindhoven — Under 2.5 Goles (under_2_5): Prob modelo 14.2%, EV -46.60%, EV robusto -65.35% → sin value.
  - RB Leipzig vs PSV Eindhoven — Over 9.5 Córners (over_corners_9_5): Prob modelo 54.1%, EV -9.06%, EV robusto -17.46% → sin value.
  - RB Leipzig vs PSV Eindhoven — Under 9.5 Córners (under_corners_9_5): Prob modelo 45.9%, EV -6.42%, EV robusto -16.62% → sin value.
  - Atletico Bucaramanga vs Aguilas Doradas Rionegro — Over 1.5 Goles (over_1_5): Prob modelo 64.1%, EV -14.73%, EV robusto -21.38% → sin value.
  - Atletico Bucaramanga vs Aguilas Doradas Rionegro — Over 2.5 Goles (over_2_5): Prob modelo 43.4%, EV -8.88%, EV robusto -19.38% → sin value.
  - Atletico Bucaramanga vs Aguilas Doradas Rionegro — Under 2.5 Goles (under_2_5): Prob modelo 56.6%, EV -3.76%, EV robusto -12.26% → sin value.
  - Atletico Bucaramanga vs Aguilas Doradas Rionegro — Over 3.5 Goles (over_3_5): Prob modelo 19.7%, EV -25.03%, EV robusto -44.03% → sin value.
  - Atletico Bucaramanga vs Aguilas Doradas Rionegro — Under 3.5 Goles (under_3_5): Prob modelo 80.3%, EV -1.27%, EV robusto -7.42% → sin value.
  - Atletico Bucaramanga vs Aguilas Doradas Rionegro — Over 8.5 Córners (over_corners_8_5): Prob modelo 47.6%, EV -18.67%, EV robusto -27.22% → sin value.
  - Atletico Bucaramanga vs Aguilas Doradas Rionegro — Over 9.5 Córners (over_corners_9_5): Prob modelo 37.7%, EV -21.28%, EV robusto -31.73% → sin value.
  - Atletico Bucaramanga vs Aguilas Doradas Rionegro — Under 9.5 Córners (under_corners_9_5): Prob modelo 62.3%, EV +3.48%, EV robusto -4.82% → sin value.
- **Candidatos con value excluidos por probabilidad-primero:**
  - Arsenal vs Lille: Empate (X) EV +54.28% / EV rob +19.28%, Victoria Lille (2) EV +70.17% / EV rob +5.17%, Under 1.5 Goles (under_1_5) EV +9.50% / EV rob -15.50%, Over 3.5 Goles (over_3_5) EV +6.31% / EV rob -5.19%, Ambos marcan (BTTS) (btts_yes) EV +10.54% / EV rob +0.04%, Under 8.5 Córners (under_corners_8_5) EV +35.01% / EV rob +23.51%, Under 10.5 Córners (under_corners_10_5) EV +11.67% / EV rob +4.37%, Over 3.5 Tarjetas (over_cards_3_5) EV +15.62% / EV rob +4.82%, Over 5.5 Tarjetas (over_cards_5_5) EV +54.00% / EV rob +23.75%, Doble Oportunidad Empate/Lille (x2) EV +40.52% / EV rob +20.52%, Over 4.5 Tarjetas (over_cards_4_5) EV +33.07% / EV rob +15.57% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Atletico Madrid vs Manchester United: Victoria Manchester United (2) EV +9.32% / EV rob -8.38%, Over 2.5 Goles (over_2_5) EV +6.48% / EV rob -1.02%, Over 3.5 Goles (over_3_5) EV +25.02% / EV rob +13.07%, DNB Manchester United (dnb_away) EV +17.43% / EV rob +2.43%, Over 3.5 Tarjetas (over_cards_3_5) EV +5.91% / EV rob -3.44% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Villarreal vs Napoli: Over 3.5 Goles (over_3_5) EV +49.02% / EV rob +36.52%, DNB Napoli (dnb_away) EV +3.44% / EV rob -9.26%, Over 9.5 Córners (over_corners_9_5) EV +12.51% / EV rob +2.76% — No cumple los mínimos de selección probabilidad-primero.
  - Galatasaray vs Barcelona: Victoria Galatasaray (1) EV +38.27% / EV rob -2.98%, Empate (X) EV +20.66% / EV rob -10.39%, Over 2.5 Goles (over_2_5) EV +7.53% / EV rob +1.53%, Doble Oportunidad Galatasaray/Empate (1x) EV +25.94% / EV rob +8.54%, DNB Galatasaray (dnb_home) EV +16.47% / EV rob -12.48% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Inter Milan vs Club Brugge: Empate (X) EV +32.48% / EV rob +2.48%, Over 2.5 Goles (over_2_5) EV +12.74% / EV rob +5.89%, Over 3.5 Goles (over_3_5) EV +64.55% / EV rob +52.85%, Victoria Club Brugge (2) EV +280.20% / EV rob +230.20%, Doble Oportunidad Empate/Club Brugge (x2) EV +128.38% / EV rob +109.38%, DNB Club Brugge (dnb_away) EV +188.22% / EV rob +153.22% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - RB Leipzig vs PSV Eindhoven: Empate (X) EV +6.43% / EV rob -18.07%, Over 2.5 Goles (over_2_5) EV +8.92% / EV rob +2.57%, Doble Oportunidad Empate/PSV Eindhoven (x2) EV +54.37% / EV rob +42.77%, Victoria PSV Eindhoven (2) EV +101.73% / EV rob +79.23%, DNB PSV Eindhoven (dnb_away) EV +69.66% / EV rob +53.16% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Atletico Bucaramanga vs Aguilas Doradas Rionegro: Under 1.5 Goles (under_1_5) EV +11.26% / EV rob -4.24%, DNB Aguilas Doradas Rionegro (dnb_away) EV +27.80% / EV rob +14.55%, Under 8.5 Córners (under_corners_8_5) EV +5.93% / EV rob -4.17%, Victoria Aguilas Doradas Rionegro (2) EV +40.64% / EV rob +21.64% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.

## Portfolio y Correlaciones
- **Exposición total:** 0.49u
- **Correlaciones detectadas:** Mercados presentes: btts_yes, over_2_5, over_3_5, under_corners_10_5, under_corners_9_5, x2. Verificar solapamiento de mercado mismo partido.
- **Ajuste de stake por correlación:** Los picks pertenecen a partidos distintos; no se aplica reducción adicional por eventos dependientes.

## Tracking
_Fuente: resultados vía websearch (MCP apifootball no operativo — fallback activo). Actualizado 2026-10-23._
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1 (Galatasaray vs Barcelona - over_3_5) | GANADA | 1 - 4 | +0.06u |
| Pick 2 (Villarreal vs Napoli - over_2_5) | GANADA | 3 - 1 | +0.06u |
| Pick 3 (Galatasaray vs Barcelona - under_corners_10_5) | GANADA | 7 córners | +0.06u |
| Pick 4 (Inter Milan vs Club Brugge - btts_yes) | GANADA | 3 - 4 | +0.05u |
| Pick 5 (Arsenal vs Lille - under_corners_9_5) | GANADA | 7 córners | +0.06u |
| Pick 6 (Atletico Bucaramanga vs Aguilas Doradas Rionegro - x2) | GANADA | 1 - 1 | +0.05u |
| **Total** | | | **+0.34u (6 G / 0 P)** |
