# Análisis de Apuestas — 14 de octubre de 2026

## Metadatos
- **Fecha de análisis:** 2026-10-14T13:29:28Z
- **Fecha(s) de partido:** 14 de octubre de 2026
- **Information cutoff:** 2026-10-14T13:29:28Z
- **Modelo de IA:** big-pickle
- **Versión del motor predictivo:** model-v1.3
- **Ligas analizadas:** UEFA Champions League (fase de liga), MLS (Decision Day), Copa Libertadores y Copa Sudamericana (semifinales de ida)
- **Rango de fechas solicitado:** 14 de octubre de 2026 - Champions League, MLS, Copa Libertadores y Copa Sudamericana (todos los partidos)
- **Partidos en universo:** 26
- **Picks iniciales con value:** 105
- **Picks finales seleccionados:** 6

## Universo Analizado
Universo = interseccion(ligas: Champions League + MLS + Copa Libertadores + Copa Sudamericana, fecha 14 de octubre de 2026, todos los partidos programados). Cutoff de informacion 2026-10-14T13:29:28Z, anterior al primer kickoff (Feyenoord-Como 16:45 UTC). No se usa informacion posterior a ningun kickoff. Universo final = 26 partidos (9 de Champions League fase de liga, 15 de MLS en jornada de Decision Day, 1 semifinal de ida de Copa Libertadores y 1 semifinal de ida de Copa Sudamericana; las semifinales de CONMEBOL se juegan el 15/10 a las 00:30 UTC, es decir dentro de la fecha solicitada). MCPs inoperativos en esta sesion: apifootball/odds-api/football-stats no expuestos y api.clubelo.com sin acceso de red, por lo que toda la recoleccion se hizo via web (agente): querostats.com, statz.ai, footystats.org, oddalerts.com, pitchmath.com, footymetrics.com, statmuse.com, clubelo.com, ESPN, FOX Sports, bettingview.com y oddschecker. Las tasas de corners y tarjetas for/against constan en cada match_input cuando estuvieron disponibles; donde las cuotas O/U no estaban cotizadas se marcan n/d (no se inventan). ADVERTENCIAS DE DATOS: (1) Bodø/Glimt vs Dortmund requirio arbitraje: el xG de 0.20 publicado por ESPN/FOX correspondia a un unico partido de UCL (0-5 vs Bayern) y no a su liga domestica, por lo que se adopto la ventana domestica (statz 2.90/0.73; footystats 2.28 como tercera opinion) con incertidumbre elevada y documentada. (2) Slovan Bratislava: el xG de 0.64 era tambien de un solo partido de UCL; se adopto footystats de la liga eslovaca (1.91/1.15) como unica fuente domestica disponible. (3) Atletico Mineiro vs Montevideo City Torque queda como NO BET por datos insuficientes: el club uruguayo no tiene xG por partido ni rating Elo en ninguna fuente consultada, y ejecutar el motor habria exigido priors por defecto para el visitante.
1. **Champions League:** Feyenoord vs Como (16:45 UTC). 1X2 3.30/3.90/1.91; O/U 1.5 1.12/6.00, 2.5 1.44/2.75, 3.5 2.00/1.75; BTTS 1.40. Elo 1724/1807; xG 2.47/0.98 vs 1.97/1.44.
2. **Champions League:** LASK vs Liverpool (16:45 UTC). 1X2 9.39/6.16/1.29; O/U 2.5 1.34; BTTS 1.59. Elo 1628/1929; xG 0.72/1.71 vs 1.56/1.19.
3. **Champions League:** Real Betis vs FC Porto (19:00 UTC). 1X2 2.16/3.76/3.50; O/U 2.5 1.79/2.19; BTTS 1.61. Elo 1823/1842; xG 1.77/1.75 vs 2.12/1.06.
4. **Champions League:** Aston Villa vs Fenerbahce (19:00 UTC). 1X2 1.70/4.10/4.50; O/U 1.5 1.17/5.00, 2.5 1.57/2.38, 3.5 2.38/1.57; DC 1X 1.17 / X2 2.25 / 12 1.22; BTTS 1.57/2.35; corners 8.5 y 9.5. Elo 1893/1785; xG 1.43/1.64 vs 2.05/1.09.
5. **Champions League:** Shakhtar Donetsk vs AEK Athens (19:00 UTC, Stamford Bridge). 1X2 2.77/3.37/2.67; O/U 2.5 1.95/1.95; BTTS 1.70/2.25; corners 8.5 capturada. Elo 1692/1708; xG 0.62/0.44 vs 1.71/0.72.
6. **Champions League:** Roma vs Real Madrid (19:00 UTC). 1X2 3.65/3.95/1.91; O/U 3.5 2.10/1.74; BTTS 1.39/3.00; DC 1X 1.91 / X2 1.33 / 12 1.28; corners 8.5 y 9.5. Elo 1856/1975; xG 2.25/1.12 vs 2.41/1.20.
7. **Champions League:** Manchester City vs Paris Saint-Germain (19:00 UTC). 1X2 2.00/4.00/3.30; O/U 3.5 2.05/1.77; BTTS 1.40/2.95; corners 8.5 y 9.5. Elo 2034/1957; xG 2.03/1.44 vs 2.45/1.09.
8. **Champions League:** Slovan Bratislava vs VfB Stuttgart (19:00 UTC). 1X2 7.50/5.75/1.35; O/U 3.5 1.83/1.95; BTTS 1.57/2.40; corners 8.5 y 9.5. Elo 1551/1824; xG 1.91/1.15 (domestico, arbitrado) vs 1.94/2.08.
9. **Champions League:** Bodo/Glimt vs Borussia Dortmund (19:00 UTC). 1X2 3.00/3.95/2.20; O/U 3.5 1.95/1.87; BTTS 1.33/3.30; corners 8.5 y 9.5. Elo 1781/1895; xG 2.90/0.73 (domestico, arbitrado) vs 1.79/0.92.
10. **Copa Libertadores (semifinal ida):** Fluminense vs Palmeiras (15/10 00:30 UTC). 1X2 2.87/3.10/2.62; O/U 1.5 1.57/2.25, 2.5 2.87/1.40, 3.5 6.00/1.13; BTTS 2.25/1.57; DC 1X 1.49 / X2 1.46 / 12 1.36; DNB 1.90/1.80; corners 9.5 1.80/1.90. Elo 1769/1856; xG 1.46/1.38 vs 1.85/1.01.
11. **Copa Sudamericana (semifinal ida):** Atletico Mineiro vs Montevideo City Torque (15/10 00:30 UTC). 1X2 1.40/4.20/9.50; O/U 1.5 1.30/3.40, 2.5 2.00/1.80, 3.5 3.35/1.24; BTTS 2.25/1.57; corners 9.5 1.83/1.83. DATOS INSUFICIENTES (sin xG del visitante ni Elo) -> NO BET.
12. **MLS:** CF Montreal vs Atlanta United (23:30 UTC). 1X2 2.50/3.80/2.85; O/U 2.5 1.54; BTTS 1.50/2.70; DC 1X 1.47 / X2 1.63 / 12 1.28; DNB 1.80/2.18; tarjetas 4.5 2.10/1.63. Elo 1486/1508; xG 1.40/1.57 vs 1.36/1.53.
13. **MLS:** Columbus Crew vs Charlotte FC (23:30 UTC). 1X2 2.00/4.00/3.60; O/U 2.5 1.52/2.48; BTTS 1.46/2.95; DC 1X 1.36 / X2 1.82 / 12 1.26; DNB 1.57/2.62; tarjetas 4.5 2.10/1.63. Elo 1595/1609; xG 1.21/1.19 vs 1.53/1.44.
14. **MLS:** DC United vs New York Red Bulls (23:30 UTC). 1X2 2.20/4.10/3.50; BTTS 1.49/2.64; DC 1X 1.39 / X2 1.87 / 12 1.27; DNB 1.45/2.84; tarjetas 4.5 2.10/1.63. Elo 1494/1551; xG 1.44/1.53 vs 1.59/2.01.
15. **MLS:** FC Cincinnati vs New England Revolution (23:30 UTC). 1X2 1.95/4.60/4.20; O/U 3.5 1.91/1.95; BTTS 1.37/3.05; DC 1X 1.32 / X2 2.15 / 12 1.24; DNB 1.49/3.35; tarjetas 3.5 1.63/2.10. Elo 1603/1559; xG 1.74/1.77 vs 1.56/1.30.
16. **MLS:** Inter Miami vs New York City FC (23:30 UTC). 1X2 1.59/4.80/5.25; O/U 3.5 1.80/1.96; BTTS 1.43/2.90; DC 1X 1.17 / X2 2.38; DNB 1.29/4.10; tarjetas 4.5 2.10/1.63. Elo 1684/1592; xG 2.05/1.62 vs 1.25/1.50.
17. **MLS:** Toronto FC vs Orlando City (23:30 UTC). 1X2 2.35/3.90/2.85; O/U 3.5 2.02/1.87; BTTS 1.39/3.30; DC 1X 1.47 / X2 1.66 / 12 1.27; DNB 1.74/2.20; tarjetas 4.5 2.00/1.62. Elo 1520/1595; xG 1.18/1.46 vs 1.54/1.92.
18. **MLS:** Chicago Fire vs Philadelphia Union (15/10 00:30 UTC). 1X2 2.60/4.10/2.60; O/U 3.5 2.05/1.95; BTTS 1.40/3.10; DC 1X 1.54 / X2 1.54 / 12 1.27; DNB 2.00/1.89; tarjetas 4.5 1.80/1.78. Elo 1605/1649; xG 1.81/1.31 vs 1.93/1.37.
19. **MLS:** FC Dallas vs Seattle Sounders (15/10 00:30 UTC). 1X2 1.98/4.10/4.00; BTTS 1.55/2.60; DC 1X 1.31 / X2 1.97 / 12 1.25; DNB 1.47/2.92; tarjetas 3.5 1.72/1.88. Elo 1605/1623; xG 1.50/1.38 vs 1.34/1.37.
20. **MLS:** Nashville SC vs Sporting Kansas City (15/10 00:30 UTC). 1X2 1.29/6.50/10.00; O/U 2.5 1.29/3.50, 3.5 1.76/2.00; BTTS 1.77/2.18; DC 1X 1.07 / X2 4.40 / 12 1.11; DNB 1.08/10.40; tarjetas 3.5 2.05/1.60. Elo 1690/1457; xG 1.62/1.30 vs 1.19/1.99.
21. **MLS:** St. Louis CITY vs Vancouver Whitecaps (15/10 00:30 UTC). 1X2 2.30/4.00/3.00; O/U 1.5 1.14/5.50, 2.5 1.50/2.50, 3.5 2.20/1.62; BTTS 1.48/2.85; DC 1X 1.44 / X2 1.72 / 12 1.26; DNB 1.72/2.30; tarjetas 4.5 1.92/1.68. Elo 1626/1653; xG 1.59/1.23 vs 2.18/1.10.
22. **MLS:** Colorado Rapids vs Minnesota United (15/10 01:30 UTC). 1X2 2.05/3.60/3.20; O/U 2.5 1.61/2.30; BTTS 1.53/2.50; corners 8.5 1.50/2.45 y 9.5 1.83/1.87. Elo 1540/1561; xG 1.51/1.19 vs 1.73/1.64.
23. **MLS:** Real Salt Lake vs San Jose Earthquakes (15/10 01:30 UTC). 1X2 1.91/3.85/3.35; O/U 2.5 1.48/2.75, 3.5 2.15/1.69; BTTS 1.43/2.80; corners 8.5 1.31/3.15, 9.5 1.54/2.35, 10.5 1.87/1.83. Elo 1541/1568; xG 1.37/1.50 vs 1.84/1.37.
24. **MLS:** LA Galaxy vs Portland Timbers (15/10 02:30 UTC). 1X2 2.00/3.80/3.10; O/U 2.5 1.40/3.20, 3.5 2.00/1.80; BTTS 1.35/3.15; corners 8.5 1.45/2.55, 9.5 1.74/1.95. Elo 1547/1555; xG 1.53/1.71 vs 1.51/1.63.
25. **MLS:** LAFC vs Austin FC (15/10 02:30 UTC). 1X2 1.43/4.60/6.00; O/U 2.5 1.57/2.35, 3.5 2.35/1.59. Elo 1652/1540; xG 1.47/1.42 vs 1.03/2.04.
26. **MLS:** San Diego FC vs Houston Dynamo (15/10 02:30 UTC). 1X2 2.10/3.55/3.05; O/U 2.5 1.65/2.20; BTTS 1.52/2.39; DC 1X 1.27 / X2 1.84 / 12 1.24. Elo 1600/1588; xG 1.57/1.70 vs 1.12/1.36.

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Feyenoord vs Como | over_2_5 | Over 2.5 Goles | excluido | 1.44 | 80.5% | 1.24 | +15.99% | +15.99% | +8.79% | 0.09u | Media-Alta |
| 2 | Real Betis vs FC Porto | over_2_5 | Over 2.5 Goles | prioritario | 1.79 | 79.1% | 1.26 | +41.52% | +41.52% | +32.57% | 0.13u | Media-Alta |
| 3 | Fluminense vs Palmeiras | over_1_5 | Over 1.5 Goles | prioritario | 1.57 | 78.4% | 1.28 | +23.14% | +23.14% | +15.29% | 0.10u | Media-Alta |
| 4 | Fluminense vs Palmeiras | x2 | Doble Oportunidad Empate/Palmeiras | excluido | 1.46 | 76.0% | 1.32 | +10.99% | +10.99% | +3.69% | 0.06u | Media-Alta |
| 5 | LA Galaxy vs Portland Timbers | over_2_5 | Over 2.5 Goles | excluido | 1.40 | 75.8% | 1.32 | +6.05% | +6.05% | -0.95% | 0.04u | Media-Alta |
| 6 | Aston Villa vs Fenerbahce | over_2_5 | Over 2.5 Goles | prioritario | 1.57 | 73.8% | 1.35 | +15.90% | +15.90% | +8.05% | 0.07u | Media-Alta |
| 7 | Aston Villa vs Fenerbahce | x2 | Doble Oportunidad Empate/Fenerbahce | excluido | 2.25 | 73.8% | 1.36 | +65.96% | +65.96% | +54.71% | 0.13u | Media-Alta |
| 8 | St. Louis CITY SC vs Vancouver Whitecaps | x2 | Doble Oportunidad Empate/Vancouver Whitecaps | prioritario | 1.72 | 73.0% | 1.37 | +25.59% | +25.59% | +16.99% | 0.09u | Media-Alta |
| 9 | St. Louis CITY SC vs Vancouver Whitecaps | over_2_5 | Over 2.5 Goles | excluido | 1.50 | 72.5% | 1.38 | +8.75% | +8.75% | +1.25% | 0.04u | Media-Alta |
| 10 | Shakhtar Donetsk vs AEK Athens | under_2_5 | Under 2.5 Goles | prioritario | 1.95 | 72.3% | 1.38 | +41.06% | +41.06% | +31.31% | 0.11u | Media-Alta |
| 11 | Real Salt Lake vs San Jose Earthquakes | over_2_5 | Over 2.5 Goles | excluido | 1.48 | 72.3% | 1.38 | +6.94% | +6.94% | -0.46% | 0.04u | Media-Alta |
| 12 | Colorado Rapids vs Minnesota United | over_2_5 | Over 2.5 Goles | prioritario | 1.61 | 72.1% | 1.39 | +16.11% | +16.11% | +8.06% | 0.07u | Media-Alta |
| 13 | LAFC vs Austin FC | over_2_5 | Over 2.5 Goles | excluido | 1.57 | 70.7% | 1.41 | +11.05% | +11.05% | +3.20% | 0.05u | Media-Alta |
| 14 | Slovan Bratislava vs VfB Stuttgart | over_3_5 | Over 3.5 Goles | prioritario | 1.83 | 70.6% | 1.42 | +29.16% | +29.16% | +20.01% | 0.09u | Media-Alta |
| 15 | Manchester City vs Paris Saint-Germain | over_3_5 | Over 3.5 Goles | prioritario | 2.05 | 69.6% | 1.44 | +42.70% | +42.70% | +32.45% | 0.10u | Media-Alta |
| 16 | CF Montreal vs Atlanta United FC | over_2_5 | Over 2.5 Goles | excluido | 1.54 | 69.4% | 1.44 | +6.92% | +6.92% | -0.78% | 0.03u | Media-Alta |
| 17 | Roma vs Real Madrid | over_3_5 | Over 3.5 Goles | prioritario | 2.10 | 69.2% | 1.45 | +45.28% | +45.28% | +34.78% | 0.10u | Media-Alta |
| 18 | San Diego FC vs Houston Dynamo | over_2_5 | Over 2.5 Goles | excluido | 1.65 | 67.9% | 1.47 | +12.08% | +12.08% | +3.83% | 0.05u | Media-Alta |
| 19 | Feyenoord vs Como | over_3_5 | Over 3.5 Goles | prioritario | 2.00 | 67.4% | 1.48 | +34.78% | +34.78% | +24.78% | 0.09u | Media-Alta |
| 20 | Fluminense vs Palmeiras | over_2_5 | Over 2.5 Goles | excluido | 2.87 | 67.2% | 1.49 | +92.95% | +92.95% | +78.60% | 0.12u | Media-Alta |
| 21 | Slovan Bratislava vs VfB Stuttgart | btts_yes | Ambos marcan (BTTS) | excluido | 1.57 | 67.2% | 1.49 | +5.55% | +5.55% | -2.30% | 0.02u | Media-Alta |
| 22 | Real Betis vs FC Porto | btts_yes | Ambos marcan (BTTS) | excluido | 1.61 | 66.3% | 1.51 | +6.71% | +6.71% | -1.34% | 0.03u | Media-Alta |
| 23 | Shakhtar Donetsk vs AEK Athens | btts_no | No ambos marcan | excluido | 2.25 | 65.6% | 1.52 | +47.56% | +47.56% | +36.31% | 0.10u | Media-Alta |
| 24 | FC Cincinnati vs New England Revolution | x2 | Doble Oportunidad Empate/New England Revolution | prioritario | 2.15 | 64.8% | 1.54 | +39.26% | +39.26% | +28.51% | 0.09u | Media-Alta |
| 25 | Columbus Crew vs Charlotte FC | x2 | Doble Oportunidad Empate/Charlotte FC | prioritario | 1.82 | 64.5% | 1.55 | +17.46% | +17.46% | +8.36% | 0.05u | Media-Alta |
| 26 | Aston Villa vs Fenerbahce | under_corners_9_5 | Under 9.5 Córners | prioritario | 2.00 | 64.1% | 1.56 | +28.20% | +28.20% | +18.20% | 0.07u | Media-Alta |
| 27 | Toronto FC vs Orlando City SC | x2 | Doble Oportunidad Empate/Orlando City SC | excluido | 1.66 | 64.1% | 1.56 | +6.36% | +6.36% | -1.94% | 0.02u | Media-Alta |
| 28 | CF Montreal vs Atlanta United FC | x2 | Doble Oportunidad Empate/Atlanta United FC | excluido | 1.63 | 63.5% | 1.57 | +3.59% | +3.59% | -4.56% | 0.01u | Media-Alta |
| 29 | FC Dallas vs Seattle Sounders | x2 | Doble Oportunidad Empate/Seattle Sounders | prioritario | 1.97 | 61.3% | 1.63 | +20.80% | +20.80% | +10.95% | 0.05u | Media-Alta |
| 30 | San Diego FC vs Houston Dynamo | x2 | Doble Oportunidad Empate/Houston Dynamo | excluido | 1.84 | 60.7% | 1.65 | +11.69% | +11.69% | +2.49% | 0.03u | Media-Alta |
| 31 | Chicago Fire vs Philadelphia Union | over_3_5 | Over 3.5 Goles | prioritario | 2.05 | 60.3% | 1.66 | +23.64% | +23.64% | +13.39% | 0.06u | Media-Alta |
| 32 | Inter Miami CF vs New York City FC | over_3_5 | Over 3.5 Goles | excluido | 1.80 | 60.3% | 1.66 | +8.56% | +8.56% | -0.44% | 0.03u | Media-Alta |
| 33 | DC United vs New York Red Bulls | x2 | Doble Oportunidad Empate/New York Red Bulls | excluido | 1.87 | 60.1% | 1.66 | +12.37% | +12.37% | +3.02% | 0.04u | Media-Alta |
| 34 | LA Galaxy vs Portland Timbers | over_3_5 | Over 3.5 Goles | prioritario | 2.00 | 59.6% | 1.68 | +19.24% | +19.24% | +9.24% | 0.05u | Media-Alta |
| 35 | Shakhtar Donetsk vs AEK Athens | under_corners_8_5 | Under 8.5 Córners | prioritario | 2.00 | 59.6% | 1.68 | +19.12% | +19.12% | +9.12% | 0.05u | Media-Alta |
| 36 | FC Cincinnati vs New England Revolution | over_3_5 | Over 3.5 Goles | excluido | 1.91 | 59.5% | 1.68 | +13.55% | +13.55% | +4.00% | 0.04u | Media-Alta |
| 37 | Bodo/Glimt vs Borussia Dortmund | over_3_5 | Over 3.5 Goles | prioritario | 1.95 | 58.9% | 1.70 | +14.85% | +14.85% | +5.10% | 0.04u | Media-Alta |
| 38 | Fluminense vs Palmeiras | btts_yes | Ambos marcan (BTTS) | excluido | 2.25 | 58.3% | 1.72 | +31.13% | +31.13% | +19.88% | 0.06u | Media-Alta |
| 39 | Aston Villa vs Fenerbahce | over_3_5 | Over 3.5 Goles | excluido | 2.38 | 56.6% | 1.77 | +34.68% | +34.68% | +22.78% | 0.06u | Media |
| 40 | Roma vs Real Madrid | 1x | Doble Oportunidad Roma/Empate | excluido | 1.91 | 56.0% | 1.79 | +6.96% | +6.96% | -2.59% | 0.02u | Media |
| 41 | St. Louis CITY SC vs Vancouver Whitecaps | over_3_5 | Over 3.5 Goles | excluido | 2.20 | 54.6% | 1.83 | +20.03% | +20.03% | +9.03% | 0.04u | Media |
| 42 | Toronto FC vs Orlando City SC | over_3_5 | Over 3.5 Goles | excluido | 2.02 | 54.6% | 1.83 | +10.21% | +10.21% | +0.11% | 0.03u | Media |
| 43 | Aston Villa vs Fenerbahce | under_corners_8_5 | Under 8.5 Córners | excluido | 2.60 | 54.2% | 1.84 | +41.05% | +41.05% | +28.05% | 0.06u | Media |
| 44 | Real Salt Lake vs San Jose Earthquakes | over_3_5 | Over 3.5 Goles | excluido | 2.15 | 54.2% | 1.85 | +16.53% | +16.53% | +5.78% | 0.04u | Media |
| 45 | Real Betis vs FC Porto | 2 | Victoria FC Porto | excepcional | 3.50 | 52.7% | 1.90 | +84.45% | +84.45% | +66.95% | 0.08u | Media |
| 46 | LAFC vs Austin FC | over_3_5 | Over 3.5 Goles | excluido | 2.35 | 51.9% | 1.93 | +21.99% | +21.99% | +10.24% | 0.04u | Media |
| 47 | Bodo/Glimt vs Borussia Dortmund | 1 | Victoria Bodo/Glimt | excepcional | 3.00 | 51.4% | 1.94 | +54.26% | +54.26% | +39.26% | 0.07u | Media |
| 48 | Aston Villa vs Fenerbahce | 2 | Victoria Fenerbahce | excepcional | 4.50 | 50.8% | 1.97 | +128.69% | +128.69% | +106.19% | 0.09u | Media |
| 49 | FC Cincinnati vs New England Revolution | under_cards_3_5 | Under 3.5 Tarjetas | excluido | 2.10 | 50.6% | 1.97 | +6.34% | +6.34% | -4.16% | 0.01u | Media |
| 50 | Fluminense vs Palmeiras | 2 | Victoria Palmeiras | excluido | 2.62 | 50.2% | 1.99 | +31.47% | +31.47% | +18.37% | 0.05u | Media |
| 51 | Fluminense vs Palmeiras | dnb_away | DNB Palmeiras | excluido | 1.80 | 50.2% | 1.48 | +16.16% | +16.16% | +7.16% | 0.05u | Media |
| 52 | Inter Miami CF vs New York City FC | x2 | Doble Oportunidad Empate/New York City FC | excluido | 2.38 | 49.5% | 2.02 | +17.88% | +17.88% | +5.98% | 0.03u | Baja |
| 53 | St. Louis CITY SC vs Vancouver Whitecaps | 2 | Victoria Vancouver Whitecaps | excepcional | 3.00 | 48.4% | 2.06 | +45.29% | +45.29% | +30.29% | 0.06u | Baja |
| 54 | St. Louis CITY SC vs Vancouver Whitecaps | dnb_away | DNB Vancouver Whitecaps | excluido | 2.30 | 48.4% | 1.56 | +35.98% | +35.98% | +24.48% | 0.07u | Baja |
| 55 | Feyenoord vs Como | 1 | Victoria Feyenoord | excepcional | 3.30 | 47.5% | 2.11 | +56.62% | +56.62% | +40.12% | 0.06u | Baja |
| 56 | Manchester City vs Paris Saint-Germain | 2 | Victoria Paris Saint-Germain | excepcional | 3.30 | 47.0% | 2.13 | +55.03% | +55.03% | +38.53% | 0.06u | Baja |
| 57 | Fluminense vs Palmeiras | over_3_5 | Over 3.5 Goles | excepcional | 6.00 | 46.9% | 2.13 | +181.10% | +181.10% | +151.10% | 0.09u | Baja |
| 58 | Real Salt Lake vs San Jose Earthquakes | 2 | Victoria San Jose Earthquakes | excepcional | 3.35 | 46.8% | 2.14 | +56.78% | +56.78% | +40.03% | 0.06u | Baja |
| 59 | Roma vs Real Madrid | under_corners_8_5 | Under 8.5 Córners | excluido | 2.40 | 45.9% | 2.18 | +10.15% | +10.15% | -1.85% | 0.02u | Baja |
| 60 | Shakhtar Donetsk vs AEK Athens | 2 | Victoria AEK Athens | excluido | 2.67 | 45.4% | 2.20 | +21.24% | +21.24% | +7.89% | 0.03u | Baja |
| 61 | Columbus Crew vs Charlotte FC | btts_no | No ambos marcan | excluido | 2.95 | 45.0% | 2.22 | +32.72% | +32.72% | +17.97% | 0.04u | Baja |
| 62 | FC Dallas vs Seattle Sounders | btts_no | No ambos marcan | excluido | 2.60 | 43.3% | 2.31 | +12.53% | +12.53% | -0.47% | 0.02u | Baja |
| 63 | FC Cincinnati vs New England Revolution | 2 | Victoria New England Revolution | excepcional | 4.20 | 40.8% | 2.45 | +71.49% | +71.49% | +50.49% | 0.06u | Baja |
| 64 | FC Cincinnati vs New England Revolution | dnb_away | DNB New England Revolution | excepcional | 3.35 | 40.8% | 1.86 | +60.72% | +60.72% | +43.97% | 0.06u | Baja |
| 65 | CF Montreal vs Atlanta United FC | btts_no | No ambos marcan | excluido | 2.70 | 40.6% | 2.47 | +9.51% | +9.51% | -3.99% | 0.01u | Baja |
| 66 | Slovan Bratislava vs VfB Stuttgart | 1 | Victoria Slovan Bratislava | excepcional | 7.50 | 40.5% | 2.47 | +203.60% | +203.60% | +166.10% | 0.08u | Baja |
| 67 | Chicago Fire vs Philadelphia Union | 2 | Victoria Philadelphia Union | excluido | 2.60 | 40.5% | 2.47 | +5.20% | +5.20% | -7.80% | 0.01u | Baja |
| 68 | Bodo/Glimt vs Borussia Dortmund | btts_no | No ambos marcan | excepcional | 3.30 | 40.4% | 2.47 | +33.45% | +33.45% | +16.95% | 0.04u | Baja |
| 69 | Nashville SC vs Sporting Kansas City | x2 | Doble Oportunidad Empate/Sporting Kansas City | excepcional | 4.40 | 39.3% | 2.54 | +73.01% | +73.01% | +51.01% | 0.05u | Baja |
| 70 | LA Galaxy vs Portland Timbers | 2 | Victoria Portland Timbers | excluido | 3.10 | 39.3% | 2.55 | +21.74% | +21.74% | +6.24% | 0.03u | Baja |
| 71 | Toronto FC vs Orlando City SC | dnb_away | DNB Orlando City SC | excluido | 2.20 | 38.6% | 1.93 | +10.44% | +10.44% | -0.56% | 0.02u | Baja |
| 72 | Toronto FC vs Orlando City SC | 2 | Victoria Orlando City SC | excluido | 2.85 | 38.6% | 2.59 | +10.15% | +10.15% | -4.10% | 0.01u | Baja |
| 73 | Toronto FC vs Orlando City SC | btts_no | No ambos marcan | excepcional | 3.30 | 38.6% | 2.59 | +27.48% | +27.48% | +10.98% | 0.03u | Baja |
| 74 | Real Salt Lake vs San Jose Earthquakes | btts_no | No ambos marcan | excluido | 2.80 | 38.3% | 2.61 | +7.27% | +7.27% | -6.73% | 0.01u | Baja |
| 75 | St. Louis CITY SC vs Vancouver Whitecaps | btts_no | No ambos marcan | excluido | 2.85 | 38.2% | 2.62 | +8.87% | +8.87% | -5.38% | 0.01u | Baja |
| 76 | CF Montreal vs Atlanta United FC | dnb_away | DNB Atlanta United FC | excluido | 2.18 | 37.9% | 1.96 | +8.32% | +8.32% | -2.58% | 0.02u | Baja |
| 77 | CF Montreal vs Atlanta United FC | 2 | Victoria Atlanta United FC | excluido | 2.85 | 37.9% | 2.64 | +8.13% | +8.13% | -6.12% | 0.01u | Baja |
| 78 | Columbus Crew vs Charlotte FC | 2 | Victoria Charlotte FC | excepcional | 3.60 | 37.7% | 2.65 | +35.68% | +35.68% | +17.68% | 0.03u | Baja |
| 79 | Columbus Crew vs Charlotte FC | dnb_away | DNB Charlotte FC | excluido | 2.62 | 37.7% | 1.94 | +25.60% | +25.60% | +12.50% | 0.04u | Baja |
| 80 | Inter Miami CF vs New York City FC | btts_no | No ambos marcan | excluido | 2.90 | 37.3% | 2.68 | +8.20% | +8.20% | -6.30% | 0.01u | Baja |
| 81 | LA Galaxy vs Portland Timbers | btts_no | No ambos marcan | excluido | 3.15 | 36.1% | 2.77 | +13.68% | +13.68% | -2.07% | 0.02u | Baja |
| 82 | FC Cincinnati vs New England Revolution | btts_no | No ambos marcan | excluido | 3.05 | 36.0% | 2.78 | +9.74% | +9.74% | -5.51% | 0.01u | Baja |
| 83 | DC United vs New York Red Bulls | dnb_away | DNB New York Red Bulls | excluido | 2.84 | 35.9% | 2.11 | +26.15% | +26.15% | +11.95% | 0.04u | Baja |
| 84 | DC United vs New York Red Bulls | 2 | Victoria New York Red Bulls | excluido | 3.50 | 35.9% | 2.79 | +25.65% | +25.65% | +8.15% | 0.03u | Baja |
| 85 | Chicago Fire vs Philadelphia Union | btts_no | No ambos marcan | excluido | 3.10 | 35.8% | 2.80 | +10.89% | +10.89% | -4.61% | 0.01u | Baja |
| 86 | Colorado Rapids vs Minnesota United | 2 | Victoria Minnesota United | excluido | 3.20 | 35.1% | 2.85 | +12.29% | +12.29% | -3.71% | 0.01u | Baja |
| 87 | FC Dallas vs Seattle Sounders | 2 | Victoria Seattle Sounders | excepcional | 4.00 | 35.1% | 2.85 | +40.28% | +40.28% | +20.28% | 0.03u | Baja |
| 88 | FC Dallas vs Seattle Sounders | dnb_away | DNB Seattle Sounders | excluido | 2.92 | 35.1% | 2.10 | +28.65% | +28.65% | +14.05% | 0.04u | Baja |
| 89 | San Diego FC vs Houston Dynamo | 2 | Victoria Houston Dynamo | excluido | 3.05 | 35.1% | 2.85 | +6.93% | +6.93% | -8.32% | 0.01u | Baja |
| 90 | Shakhtar Donetsk vs AEK Athens | X | Empate | excluido | 3.37 | 33.1% | 3.02 | +11.51% | +11.51% | -5.34% | 0.01u | Baja |
| 91 | Roma vs Real Madrid | 1 | Victoria Roma | excluido | 3.65 | 32.5% | 3.08 | +18.44% | +18.44% | +0.19% | 0.02u | Baja |
| 92 | Columbus Crew vs Charlotte FC | X | Empate | excluido | 4.00 | 26.9% | 3.72 | +7.40% | +7.40% | -12.60% | 0.01u | Baja |
| 93 | Inter Miami CF vs New York City FC | 2 | Victoria New York City FC | excluido | 5.25 | 26.4% | 3.79 | +38.55% | +38.55% | +12.30% | 0.02u | Baja |
| 94 | Inter Miami CF vs New York City FC | dnb_away | DNB New York City FC | excluido | 4.10 | 26.4% | 2.91 | +31.33% | +31.33% | +10.83% | 0.03u | Baja |
| 95 | FC Dallas vs Seattle Sounders | X | Empate | excluido | 4.10 | 26.2% | 3.81 | +7.62% | +7.62% | -12.88% | 0.01u | Baja |
| 96 | FC Cincinnati vs New England Revolution | X | Empate | excluido | 4.60 | 23.9% | 4.18 | +10.12% | +10.12% | -12.88% | 0.01u | Baja |
| 97 | LASK vs Liverpool | X | Empate | excluido | 6.16 | 23.9% | 4.18 | +47.41% | +47.41% | +16.61% | 0.02u | Baja |
| 98 | LAFC vs Austin FC | X | Empate | excluido | 4.60 | 23.2% | 4.30 | +6.86% | +6.86% | -16.14% | 0.00u | Baja |
| 99 | Inter Miami CF vs New York City FC | X | Empate | excluido | 4.80 | 23.1% | 4.32 | +11.02% | +11.02% | -12.98% | 0.01u | Baja |
| 100 | Nashville SC vs Sporting Kansas City | X | Empate | excluido | 6.50 | 22.1% | 4.53 | +43.59% | +43.59% | +11.08% | 0.02u | Baja |
| 101 | Slovan Bratislava vs VfB Stuttgart | X | Empate | excluido | 5.75 | 21.4% | 4.68 | +22.88% | +22.88% | -5.87% | 0.01u | Baja |
| 102 | LAFC vs Austin FC | 2 | Victoria Austin FC | excluido | 6.00 | 20.0% | 4.99 | +20.18% | +20.18% | -9.82% | 0.01u | Baja |
| 103 | Nashville SC vs Sporting Kansas City | dnb_away | DNB Sporting Kansas City | excluido | 10.40 | 17.2% | 4.52 | +101.39% | +101.39% | +49.39% | 0.03u | Baja |
| 104 | Nashville SC vs Sporting Kansas City | 2 | Victoria Sporting Kansas City | excluido | 10.00 | 17.2% | 5.80 | +72.40% | +72.40% | +22.40% | 0.02u | Baja |
| 105 | LASK vs Liverpool | 1 | Victoria LASK | excluido | 9.39 | 12.7% | 7.87 | +19.35% | +19.35% | -27.60% | 0.01u | Baja |

## Evaluación Over/Under por Partido
Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada (n/d = cuota no disponible en la corrida).
| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |
|---|---|---|---:|---:|---:|---:|---:|---|
| Feyenoord vs Como | 1.5 | 86.2% | 1.12 | -3.48% | 13.8% | 6.00 | -17.08% | Sin value |
| Feyenoord vs Como | 2.5 | 80.5% | 1.44 | +15.99% | 19.4% | 2.75 | -46.51% | Value Over |
| Feyenoord vs Como | 3.5 | 67.4% | 2.00 | +34.78% | 32.6% | 1.75 | -42.93% | Value Over |
| LASK vs Liverpool | 1.5 | 73.8% | n/d | n/d | 26.2% | n/d | n/d | Cuotas no capturadas |
| LASK vs Liverpool | 2.5 | 59.3% | 1.34 | -20.55% | 40.7% | n/d | n/d | Solo Over con cuota (Under n/d) |
| LASK vs Liverpool | 3.5 | 36.4% | n/d | n/d | 63.6% | n/d | n/d | Cuotas no capturadas |
| Real Betis vs FC Porto | 1.5 | 85.3% | n/d | n/d | 14.7% | n/d | n/d | Cuotas no capturadas |
| Real Betis vs FC Porto | 2.5 | 79.1% | 1.79 | +41.52% | 20.9% | 2.19 | -54.14% | Value Over |
| Real Betis vs FC Porto | 3.5 | 65.0% | n/d | n/d | 35.0% | n/d | n/d | Cuotas no capturadas |
| Aston Villa vs Fenerbahce | 1.5 | 82.2% | 1.17 | -3.79% | 17.8% | 5.00 | -11.15% | Sin value |
| Aston Villa vs Fenerbahce | 2.5 | 73.8% | 1.57 | +15.90% | 26.2% | 2.38 | -37.69% | Value Over |
| Aston Villa vs Fenerbahce | 3.5 | 56.6% | 2.38 | +34.68% | 43.4% | 1.57 | -31.85% | Value Over |
| Shakhtar Donetsk vs AEK Athens | 1.5 | 52.8% | n/d | n/d | 47.1% | n/d | n/d | Cuotas no capturadas |
| Shakhtar Donetsk vs AEK Athens | 2.5 | 27.7% | 1.95 | -46.06% | 72.3% | 1.95 | +41.06% | Value Under |
| Shakhtar Donetsk vs AEK Athens | 3.5 | 8.6% | n/d | n/d | 91.4% | n/d | n/d | Cuotas no capturadas |
| Roma vs Real Madrid | 1.5 | 86.9% | n/d | n/d | 13.2% | n/d | n/d | Cuotas no capturadas |
| Roma vs Real Madrid | 2.5 | 81.6% | n/d | n/d | 18.4% | n/d | n/d | Cuotas no capturadas |
| Roma vs Real Madrid | 3.5 | 69.2% | 2.10 | +45.28% | 30.8% | 1.74 | -46.37% | Value Over |
| Manchester City vs Paris Saint-Germain | 1.5 | 87.0% | n/d | n/d | 13.0% | n/d | n/d | Cuotas no capturadas |
| Manchester City vs Paris Saint-Germain | 2.5 | 81.9% | n/d | n/d | 18.1% | n/d | n/d | Cuotas no capturadas |
| Manchester City vs Paris Saint-Germain | 3.5 | 69.6% | 2.05 | +42.70% | 30.4% | 1.77 | -46.21% | Value Over |
| Slovan Bratislava vs VfB Stuttgart | 1.5 | 87.3% | n/d | n/d | 12.7% | n/d | n/d | Cuotas no capturadas |
| Slovan Bratislava vs VfB Stuttgart | 2.5 | 82.4% | n/d | n/d | 17.6% | n/d | n/d | Cuotas no capturadas |
| Slovan Bratislava vs VfB Stuttgart | 3.5 | 70.6% | 1.83 | +29.16% | 29.4% | 1.95 | -42.63% | Value Over |
| Bodo/Glimt vs Borussia Dortmund | 1.5 | 83.0% | n/d | n/d | 17.0% | n/d | n/d | Cuotas no capturadas |
| Bodo/Glimt vs Borussia Dortmund | 2.5 | 75.3% | n/d | n/d | 24.7% | n/d | n/d | Cuotas no capturadas |
| Bodo/Glimt vs Borussia Dortmund | 3.5 | 58.9% | 1.95 | +14.85% | 41.1% | 1.87 | -23.14% | Value Over |
| Fluminense vs Palmeiras | 1.5 | 78.4% | 1.57 | +23.14% | 21.6% | 2.25 | -51.47% | Value Over |
| Fluminense vs Palmeiras | 2.5 | 67.2% | 2.87 | +92.95% | 32.8% | 1.40 | -54.12% | Value Over |
| Fluminense vs Palmeiras | 3.5 | 46.9% | 6.00 | +181.10% | 53.1% | 1.13 | -39.94% | Value Over |
| Atletico Mineiro vs Montevideo City Torque | 1.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Atletico Mineiro vs Montevideo City Torque | 2.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| Atletico Mineiro vs Montevideo City Torque | 3.5 | n/d | n/d | n/d | n/d | n/d | n/d | Cuotas no capturadas |
| CF Montreal vs Atlanta United FC | 1.5 | 79.7% | n/d | n/d | 20.3% | n/d | n/d | Cuotas no capturadas |
| CF Montreal vs Atlanta United FC | 2.5 | 69.4% | 1.54 | +6.92% | 30.6% | n/d | n/d | Solo Over con cuota (Under n/d) |
| CF Montreal vs Atlanta United FC | 3.5 | 50.0% | n/d | n/d | 50.0% | n/d | n/d | Cuotas no capturadas |
| Columbus Crew vs Charlotte FC | 1.5 | 75.6% | n/d | n/d | 24.4% | n/d | n/d | Cuotas no capturadas |
| Columbus Crew vs Charlotte FC | 2.5 | 62.3% | 1.52 | -5.24% | 37.7% | 2.48 | -6.60% | Sin value |
| Columbus Crew vs Charlotte FC | 3.5 | 40.2% | n/d | n/d | 59.8% | n/d | n/d | Cuotas no capturadas |
| DC United vs New York Red Bulls | 1.5 | 84.5% | n/d | n/d | 15.5% | n/d | n/d | Cuotas no capturadas |
| DC United vs New York Red Bulls | 2.5 | 77.8% | n/d | n/d | 22.2% | n/d | n/d | Cuotas no capturadas |
| DC United vs New York Red Bulls | 3.5 | 62.8% | n/d | n/d | 37.2% | n/d | n/d | Cuotas no capturadas |
| FC Cincinnati vs New England Revolution | 1.5 | 83.3% | n/d | n/d | 16.7% | n/d | n/d | Cuotas no capturadas |
| FC Cincinnati vs New England Revolution | 2.5 | 75.6% | n/d | n/d | 24.4% | n/d | n/d | Cuotas no capturadas |
| FC Cincinnati vs New England Revolution | 3.5 | 59.5% | 1.91 | +13.55% | 40.6% | 1.95 | -20.93% | Value Over |
| Inter Miami CF vs New York City FC | 1.5 | 83.6% | n/d | n/d | 16.4% | n/d | n/d | Cuotas no capturadas |
| Inter Miami CF vs New York City FC | 2.5 | 76.2% | n/d | n/d | 23.8% | n/d | n/d | Cuotas no capturadas |
| Inter Miami CF vs New York City FC | 3.5 | 60.3% | 1.80 | +8.56% | 39.7% | 1.96 | -22.21% | Value Over |
| Toronto FC vs Orlando City SC | 1.5 | 81.5% | n/d | n/d | 18.5% | n/d | n/d | Cuotas no capturadas |
| Toronto FC vs Orlando City SC | 2.5 | 72.5% | n/d | n/d | 27.5% | n/d | n/d | Cuotas no capturadas |
| Toronto FC vs Orlando City SC | 3.5 | 54.6% | 2.02 | +10.21% | 45.4% | 1.87 | -15.03% | Value Over |
| Chicago Fire vs Philadelphia Union | 1.5 | 83.6% | n/d | n/d | 16.4% | n/d | n/d | Cuotas no capturadas |
| Chicago Fire vs Philadelphia Union | 2.5 | 76.2% | n/d | n/d | 23.8% | n/d | n/d | Cuotas no capturadas |
| Chicago Fire vs Philadelphia Union | 3.5 | 60.3% | 2.05 | +23.64% | 39.7% | 1.95 | -22.60% | Value Over |
| FC Dallas vs Seattle Sounders | 1.5 | 77.5% | n/d | n/d | 22.5% | n/d | n/d | Cuotas no capturadas |
| FC Dallas vs Seattle Sounders | 2.5 | 65.7% | n/d | n/d | 34.3% | n/d | n/d | Cuotas no capturadas |
| FC Dallas vs Seattle Sounders | 3.5 | 44.6% | n/d | n/d | 55.4% | n/d | n/d | Cuotas no capturadas |
| Nashville SC vs Sporting Kansas City | 1.5 | 81.4% | n/d | n/d | 18.6% | n/d | n/d | Cuotas no capturadas |
| Nashville SC vs Sporting Kansas City | 2.5 | 72.5% | 1.29 | -6.49% | 27.5% | 3.50 | -3.72% | Sin value |
| Nashville SC vs Sporting Kansas City | 3.5 | 54.5% | 1.76 | -3.99% | 45.5% | 2.00 | -9.10% | Sin value |
| St. Louis CITY SC vs Vancouver Whitecaps | 1.5 | 81.5% | 1.14 | -7.11% | 18.5% | 5.50 | +1.86% | Sin value |
| St. Louis CITY SC vs Vancouver Whitecaps | 2.5 | 72.5% | 1.50 | +8.75% | 27.5% | 2.50 | -31.25% | Value Over |
| St. Louis CITY SC vs Vancouver Whitecaps | 3.5 | 54.6% | 2.20 | +20.03% | 45.4% | 1.62 | -26.39% | Value Over |
| Colorado Rapids vs Minnesota United | 1.5 | 81.2% | n/d | n/d | 18.8% | n/d | n/d | Cuotas no capturadas |
| Colorado Rapids vs Minnesota United | 2.5 | 72.1% | 1.61 | +16.11% | 27.9% | 2.30 | -35.88% | Value Over |
| Colorado Rapids vs Minnesota United | 3.5 | 54.0% | n/d | n/d | 46.0% | n/d | n/d | Cuotas no capturadas |
| Real Salt Lake vs San Jose Earthquakes | 1.5 | 81.3% | n/d | n/d | 18.7% | n/d | n/d | Cuotas no capturadas |
| Real Salt Lake vs San Jose Earthquakes | 2.5 | 72.3% | 1.48 | +6.94% | 27.7% | 2.75 | -23.72% | Value Over |
| Real Salt Lake vs San Jose Earthquakes | 3.5 | 54.2% | 2.15 | +16.53% | 45.8% | 1.69 | -22.60% | Value Over |
| LA Galaxy vs Portland Timbers | 1.5 | 83.4% | n/d | n/d | 16.6% | n/d | n/d | Cuotas no capturadas |
| LA Galaxy vs Portland Timbers | 2.5 | 75.8% | 1.40 | +6.05% | 24.2% | 3.20 | -22.40% | Value Over |
| LA Galaxy vs Portland Timbers | 3.5 | 59.6% | 2.00 | +19.24% | 40.4% | 1.80 | -27.32% | Value Over |
| LAFC vs Austin FC | 1.5 | 80.4% | n/d | n/d | 19.6% | n/d | n/d | Cuotas no capturadas |
| LAFC vs Austin FC | 2.5 | 70.7% | 1.57 | +11.05% | 29.3% | 2.35 | -31.22% | Value Over |
| LAFC vs Austin FC | 3.5 | 51.9% | 2.35 | +21.99% | 48.1% | 1.59 | -23.54% | Value Over |
| San Diego FC vs Houston Dynamo | 1.5 | 78.8% | n/d | n/d | 21.2% | n/d | n/d | Cuotas no capturadas |
| San Diego FC vs Houston Dynamo | 2.5 | 67.9% | 1.65 | +12.08% | 32.1% | 2.20 | -29.45% | Value Over |
| San Diego FC vs Houston Dynamo | 3.5 | 47.8% | n/d | n/d | 52.2% | n/d | n/d | Cuotas no capturadas |

## Picks Recomendados (Top 6)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Real Betis vs FC Porto | over_2_5 | Over 2.5 Goles | prioritario | 1.79 | 79.1% | 1.26 | +41.52% | +41.52% | +32.57% | 0.13u | Media-Alta |
| 2 | Fluminense vs Palmeiras | over_1_5 | Over 1.5 Goles | prioritario | 1.57 | 78.4% | 1.28 | +23.14% | +23.14% | +15.29% | 0.10u | Media-Alta |
| 3 | Aston Villa vs Fenerbahce | over_2_5 | Over 2.5 Goles | prioritario | 1.57 | 73.8% | 1.35 | +15.90% | +15.90% | +8.05% | 0.07u | Media-Alta |
| 4 | St. Louis CITY SC vs Vancouver Whitecaps | x2 | Doble Oportunidad Empate/Vancouver Whitecaps | prioritario | 1.72 | 73.0% | 1.37 | +25.59% | +25.59% | +16.99% | 0.09u | Media-Alta |
| 5 | Shakhtar Donetsk vs AEK Athens | under_2_5 | Under 2.5 Goles | prioritario | 1.95 | 72.3% | 1.38 | +41.06% | +41.06% | +31.31% | 0.11u | Media-Alta |
| 6 | Colorado Rapids vs Minnesota United | over_2_5 | Over 2.5 Goles | prioritario | 1.61 | 72.1% | 1.39 | +16.11% | +16.11% | +8.06% | 0.07u | Media-Alta |

## Detalle de Picks
### Pick 1: Real Betis vs FC Porto
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.79
- **Probabilidad modelo:** 79.1%
- **Probabilidad conservadora:** 74.1%
- **Probabilidad implícita:** 55.9%
- **Cuota justa:** 1.26
- **Edge:** +41.52%
- **EV:** +41.52%
- **EV robusto:** +32.57%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.35
- **Stake:** 0.13u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestras de 5-22 partidos segun liga
- **Por qué:** Elo casi identico (1842 vs 1823) pero Porto con mejor perfil de xG (2.12 a favor / 1.06 en contra) que un Betis que concede 1.75. El motor model-v1.3 estima 79.1% para 'Over 2.5 Goles' frente a una probabilidad implicita de 55.9% (cuota 1.79); edge +41.52% y EV robusto +32.57%.
- **Riesgos:** Solo 1X2, O/U 2.5 y BTTS cotizados; corners muy altos en contra del Betis (6.6) con muestra corta.
- **Fuentes:** querostats.com + statz.ai (xG), querostats.com + statz.ai + footymetrics.com (corners/tarjetas), clubelo.com (Elo), ESPN/FOX/bettingview/oddsportal (cuotas); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 2: Fluminense vs Palmeiras
- **Mercado:** over_1_5
- **Selección:** Over 1.5 Goles
- **Cuota:** 1.57
- **Probabilidad modelo:** 78.4%
- **Probabilidad conservadora:** 73.4%
- **Probabilidad implícita:** 63.7%
- **Cuota justa:** 1.28
- **Edge:** +23.14%
- **EV:** +23.14%
- **EV robusto:** +15.29%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.36
- **Stake:** 0.10u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestras de 5-22 partidos segun liga
- **Por qué:** Semifinal de Libertadores muy equilibrada: Palmeiras con mejor Elo (1856 vs 1769) y xG (1.85 a favor / 1.01 en contra) frente a un Fluminense local que concede 1.38. El motor model-v1.3 estima 78.4% para 'Over 1.5 Goles' frente a una probabilidad implicita de 63.7% (cuota 1.57); edge +23.14% y EV robusto +15.29%.
- **Riesgos:** Ventanas de datos distintas (xG = ultimos 10 partidos de Brasileirao; corners/tarjetas = ultimos 10 de todas las competiciones, incluida Libertadores). Sin 1X2 alternativo ni lineas de corners 8.5/10.5 ni tarjetas; semifinal a ida suele ser de bajo ritmo.
- **Fuentes:** statz.ai (xG/corners/tarjetas), clubelo.com (Elo), bwin/oddstorm/aiscore (cuotas); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 3: Aston Villa vs Fenerbahce
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.57
- **Probabilidad modelo:** 73.8%
- **Probabilidad conservadora:** 68.8%
- **Probabilidad implícita:** 63.7%
- **Cuota justa:** 1.35
- **Edge:** +15.90%
- **EV:** +15.90%
- **EV robusto:** +8.05%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.45
- **Stake:** 0.07u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestras de 5-22 partidos segun liga
- **Por qué:** Villa con Elo superior (1893 vs 1785) y localia; Fenerbahce llega con mejor xG a favor (2.05) pero defensa mas solida del local. El motor model-v1.3 estima 73.8% para 'Over 2.5 Goles' frente a una probabilidad implicita de 63.7% (cuota 1.57); edge +15.90% y EV robusto +8.05%.
- **Riesgos:** xG del Villa discrepa con su rendimiento liguero (1.43 a favor); corners del Villa inusualmente bajos (3.1); sin DNB cotizado.
- **Fuentes:** querostats.com + statz.ai (xG), querostats.com + statz.ai + footymetrics.com (corners/tarjetas), clubelo.com (Elo), ESPN/FOX/bettingview/oddsportal (cuotas); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 4: St. Louis CITY SC vs Vancouver Whitecaps
- **Mercado:** x2
- **Selección:** Doble Oportunidad Empate/Vancouver Whitecaps
- **Cuota:** 1.72
- **Probabilidad modelo:** 73.0%
- **Probabilidad conservadora:** 68.0%
- **Probabilidad implícita:** 58.1%
- **Cuota justa:** 1.37
- **Edge:** +25.59%
- **EV:** +25.59%
- **EV robusto:** +16.99%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.47
- **Stake:** 0.09u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestras de 5-22 partidos segun liga
- **Por qué:** Vancouver llega con el mejor ataque visitante del lote oeste (2.18 xG a favor, 1.10 en contra) y Elo ligeramente superior, pero cotiza a 3.00. El motor model-v1.3 estima 73.0% para 'Doble Oportunidad Empate/Vancouver Whitecaps' frente a una probabilidad implicita de 58.1% (cuota 1.72); edge +25.59% y EV robusto +16.99%.
- **Riesgos:** Sin corners cotizados pese a que Vancouver concede solo 2.96; xG del visitante muy alto con muestra de temporada MLS.
- **Fuentes:** pitchmath.com (xG y corners), statz.ai (tarjetas), oddalerts.com (xG MLS, lote oeste), clubelo.com/USA (Elo), bettingview.com + oddschecker (cuotas); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 5: Shakhtar Donetsk vs AEK Athens
- **Mercado:** under_2_5
- **Selección:** Under 2.5 Goles
- **Cuota:** 1.95
- **Probabilidad modelo:** 72.3%
- **Probabilidad conservadora:** 67.3%
- **Probabilidad implícita:** 51.3%
- **Cuota justa:** 1.38
- **Edge:** +41.06%
- **EV:** +41.06%
- **EV robusto:** +31.31%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.49
- **Stake:** 0.11u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestras de 5-22 partidos segun liga
- **Por qué:** Partido de Elo casi identico (1708 vs 1692) con xG bajo del local (0.62) en cancha neutral (Stamford Bridge), lo que reduce la ventaja de localia. El motor model-v1.3 estima 72.3% para 'Under 2.5 Goles' frente a una probabilidad implicita de 51.3% (cuota 1.95); edge +41.06% y EV robusto +31.31%.
- **Riesgos:** Localia neutral (sede designada); tarjetas/contadores del proveedor con valores extremos (6.0) y simetria invertida, se usan solo como contexto.
- **Fuentes:** querostats.com + statz.ai (xG), querostats.com + statz.ai + footymetrics.com (corners/tarjetas), clubelo.com (Elo), ESPN/FOX/bettingview/oddsportal (cuotas); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 6: Colorado Rapids vs Minnesota United
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.61
- **Probabilidad modelo:** 72.1%
- **Probabilidad conservadora:** 67.1%
- **Probabilidad implícita:** 62.1%
- **Cuota justa:** 1.39
- **Edge:** +16.11%
- **EV:** +16.11%
- **EV robusto:** +8.06%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.49
- **Stake:** 0.07u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3) sobre muestras de 5-22 partidos segun liga
- **Por qué:** Elo very similar (1561 vs 1540) con Minnesota algo mejor al ataque (1.73 vs 1.51) pero peor defensa (1.64 vs 1.19). El motor model-v1.3 estima 72.1% para 'Over 2.5 Goles' frente a una probabilidad implicita de 62.1% (cuota 1.61); edge +16.11% y EV robusto +8.06%.
- **Riesgos:** Sin lineas 1.5/3.5 de goles, sin doble oportunidad, DNB ni tarjetas; corners del local (4.96 a favor, 4.18 en contra) con dispersion baja.
- **Fuentes:** pitchmath.com (xG y corners), statz.ai (tarjetas), oddalerts.com (xG MLS, lote oeste), clubelo.com/USA (Elo), bettingview.com + oddschecker (cuotas); verosimilitud del modelo y calibracion Platt (model-v1.3).

## NO BET / Excluidos
- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**
  - Feyenoord vs Como — Over 1.5 Goles (over_1_5): Prob modelo 86.2%, EV -3.48%, EV robusto -9.08% → sin value.
  - Feyenoord vs Como — Under 1.5 Goles (under_1_5): Prob modelo 13.8%, EV -17.08%, EV robusto -47.08% → sin value.
  - Feyenoord vs Como — Under 2.5 Goles (under_2_5): Prob modelo 19.4%, EV -46.51%, EV robusto -60.26% → sin value.
  - Feyenoord vs Como — Under 3.5 Goles (under_3_5): Prob modelo 32.6%, EV -42.93%, EV robusto -51.68% → sin value.
  - LASK vs Liverpool — Over 2.5 Goles (over_2_5): Prob modelo 59.3%, EV -20.55%, EV robusto -27.25% → sin value.
  - Real Betis vs FC Porto — Under 2.5 Goles (under_2_5): Prob modelo 20.9%, EV -54.14%, EV robusto -65.09% → sin value.
  - Aston Villa vs Fenerbahce — Over 1.5 Goles (over_1_5): Prob modelo 82.2%, EV -3.79%, EV robusto -9.64% → sin value.
  - Aston Villa vs Fenerbahce — Under 1.5 Goles (under_1_5): Prob modelo 17.8%, EV -11.15%, EV robusto -36.15% → sin value.
  - Aston Villa vs Fenerbahce — Under 2.5 Goles (under_2_5): Prob modelo 26.2%, EV -37.69%, EV robusto -49.59% → sin value.
  - Aston Villa vs Fenerbahce — Under 3.5 Goles (under_3_5): Prob modelo 43.4%, EV -31.85%, EV robusto -39.70% → sin value.
  - Aston Villa vs Fenerbahce — Over 8.5 Córners (over_corners_8_5): Prob modelo 45.8%, EV -34.12%, EV robusto -41.32% → sin value.
  - Aston Villa vs Fenerbahce — Over 9.5 Córners (over_corners_9_5): Prob modelo 35.9%, EV -37.53%, EV robusto -46.23% → sin value.
  - Shakhtar Donetsk vs AEK Athens — Over 2.5 Goles (over_2_5): Prob modelo 27.7%, EV -46.06%, EV robusto -55.81% → sin value.
  - Shakhtar Donetsk vs AEK Athens — Over 8.5 Córners (over_corners_8_5): Prob modelo 40.4%, EV -30.85%, EV robusto -39.40% → sin value.
  - Roma vs Real Madrid — Under 3.5 Goles (under_3_5): Prob modelo 30.8%, EV -46.37%, EV robusto -55.07% → sin value.
  - Roma vs Real Madrid — Over 8.5 Córners (over_corners_8_5): Prob modelo 54.1%, EV -18.30%, EV robusto -25.85% → sin value.
  - Roma vs Real Madrid — Over 9.5 Córners (over_corners_9_5): Prob modelo 44.2%, EV -19.10%, EV robusto -28.25% → sin value.
  - Roma vs Real Madrid — Under 9.5 Córners (under_corners_9_5): Prob modelo 55.8%, EV +4.33%, EV robusto -5.02% → sin value.
  - Manchester City vs Paris Saint-Germain — Under 3.5 Goles (under_3_5): Prob modelo 30.4%, EV -46.21%, EV robusto -55.06% → sin value.
  - Manchester City vs Paris Saint-Germain — Over 8.5 Córners (over_corners_8_5): Prob modelo 50.0%, EV -15.42%, EV robusto -23.87% → sin value.
  - Manchester City vs Paris Saint-Germain — Under 8.5 Córners (under_corners_8_5): Prob modelo 50.0%, EV +2.41%, EV robusto -7.84% → sin value.
  - Manchester City vs Paris Saint-Germain — Over 9.5 Córners (over_corners_9_5): Prob modelo 40.1%, EV -13.75%, EV robusto -24.50% → sin value.
  - Manchester City vs Paris Saint-Germain — Under 9.5 Córners (under_corners_9_5): Prob modelo 59.9%, EV -2.39%, EV robusto -10.54% → sin value.
  - Slovan Bratislava vs VfB Stuttgart — Under 3.5 Goles (under_3_5): Prob modelo 29.4%, EV -42.63%, EV robusto -52.38% → sin value.
  - Slovan Bratislava vs VfB Stuttgart — Over 8.5 Córners (over_corners_8_5): Prob modelo 61.3%, EV -9.97%, EV robusto -17.32% → sin value.
  - Slovan Bratislava vs VfB Stuttgart — Under 8.5 Córners (under_corners_8_5): Prob modelo 38.8%, EV -3.11%, EV robusto -15.61% → sin value.
  - Slovan Bratislava vs VfB Stuttgart — Over 9.5 Córners (over_corners_9_5): Prob modelo 51.7%, EV -8.55%, EV robusto -17.40% → sin value.
  - Slovan Bratislava vs VfB Stuttgart — Under 9.5 Córners (under_corners_9_5): Prob modelo 48.3%, EV -7.68%, EV robusto -17.23% → sin value.
  - Bodo/Glimt vs Borussia Dortmund — Under 3.5 Goles (under_3_5): Prob modelo 41.1%, EV -23.14%, EV robusto -32.49% → sin value.
  - Bodo/Glimt vs Borussia Dortmund — Over 8.5 Córners (over_corners_8_5): Prob modelo 57.3%, EV -10.07%, EV robusto -17.92% → sin value.
  - Bodo/Glimt vs Borussia Dortmund — Under 8.5 Córners (under_corners_8_5): Prob modelo 42.7%, EV -3.88%, EV robusto -15.13% → sin value.
  - Bodo/Glimt vs Borussia Dortmund — Over 9.5 Córners (over_corners_9_5): Prob modelo 47.5%, EV -9.31%, EV robusto -18.86% → sin value.
  - Bodo/Glimt vs Borussia Dortmund — Under 9.5 Córners (under_corners_9_5): Prob modelo 52.5%, EV -7.04%, EV robusto -15.89% → sin value.
  - Fluminense vs Palmeiras — Under 1.5 Goles (under_1_5): Prob modelo 21.6%, EV -51.47%, EV robusto -62.72% → sin value.
  - Fluminense vs Palmeiras — Under 2.5 Goles (under_2_5): Prob modelo 32.8%, EV -54.12%, EV robusto -61.12% → sin value.
  - Fluminense vs Palmeiras — Under 3.5 Goles (under_3_5): Prob modelo 53.1%, EV -39.94%, EV robusto -45.59% → sin value.
  - Fluminense vs Palmeiras — Over 9.5 Córners (over_corners_9_5): Prob modelo 55.4%, EV -0.21%, EV robusto -9.21% → sin value.
  - Fluminense vs Palmeiras — Under 9.5 Córners (under_corners_9_5): Prob modelo 44.6%, EV -15.34%, EV robusto -24.84% → sin value.
  - CF Montreal vs Atlanta United FC — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 37.3%, EV -21.62%, EV robusto -32.12% → sin value.
  - CF Montreal vs Atlanta United FC — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 62.7%, EV +2.16%, EV robusto -5.99% → sin value.
  - Columbus Crew vs Charlotte FC — Over 2.5 Goles (over_2_5): Prob modelo 62.3%, EV -5.24%, EV robusto -12.84% → sin value.
  - Columbus Crew vs Charlotte FC — Under 2.5 Goles (under_2_5): Prob modelo 37.7%, EV -6.60%, EV robusto -19.00% → sin value.
  - Columbus Crew vs Charlotte FC — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 42.0%, EV -11.88%, EV robusto -22.38% → sin value.
  - Columbus Crew vs Charlotte FC — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 58.0%, EV -5.40%, EV robusto -13.55% → sin value.
  - DC United vs New York Red Bulls — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 37.6%, EV -21.13%, EV robusto -31.63% → sin value.
  - DC United vs New York Red Bulls — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 62.4%, EV +1.78%, EV robusto -6.37% → sin value.
  - FC Cincinnati vs New England Revolution — Under 3.5 Goles (under_3_5): Prob modelo 40.6%, EV -20.93%, EV robusto -30.68% → sin value.
  - FC Cincinnati vs New England Revolution — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 49.4%, EV -19.54%, EV robusto -27.69% → sin value.
  - Inter Miami CF vs New York City FC — Under 3.5 Goles (under_3_5): Prob modelo 39.7%, EV -22.21%, EV robusto -32.01% → sin value.
  - Inter Miami CF vs New York City FC — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 46.8%, EV -1.63%, EV robusto -12.13% → sin value.
  - Inter Miami CF vs New York City FC — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 53.2%, EV -13.35%, EV robusto -21.50% → sin value.
  - Toronto FC vs Orlando City SC — Under 3.5 Goles (under_3_5): Prob modelo 45.4%, EV -15.03%, EV robusto -24.38% → sin value.
  - Toronto FC vs Orlando City SC — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 37.9%, EV -24.12%, EV robusto -34.12% → sin value.
  - Toronto FC vs Orlando City SC — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 62.1%, EV +0.53%, EV robusto -7.57% → sin value.
  - Chicago Fire vs Philadelphia Union — Under 3.5 Goles (under_3_5): Prob modelo 39.7%, EV -22.60%, EV robusto -32.35% → sin value.
  - Chicago Fire vs Philadelphia Union — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 44.0%, EV -20.74%, EV robusto -29.74% → sin value.
  - Chicago Fire vs Philadelphia Union — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 56.0%, EV -0.38%, EV robusto -9.28% → sin value.
  - FC Dallas vs Seattle Sounders — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 50.0%, EV -13.98%, EV robusto -22.58% → sin value.
  - FC Dallas vs Seattle Sounders — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 50.0%, EV -6.02%, EV robusto -15.42% → sin value.
  - Nashville SC vs Sporting Kansas City — Over 2.5 Goles (over_2_5): Prob modelo 72.5%, EV -6.49%, EV robusto -12.94% → sin value.
  - Nashville SC vs Sporting Kansas City — Under 2.5 Goles (under_2_5): Prob modelo 27.5%, EV -3.72%, EV robusto -21.21% → sin value.
  - Nashville SC vs Sporting Kansas City — Over 3.5 Goles (over_3_5): Prob modelo 54.5%, EV -3.99%, EV robusto -12.79% → sin value.
  - Nashville SC vs Sporting Kansas City — Under 3.5 Goles (under_3_5): Prob modelo 45.5%, EV -9.10%, EV robusto -19.10% → sin value.
  - Nashville SC vs Sporting Kansas City — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 41.3%, EV -15.42%, EV robusto -25.67% → sin value.
  - Nashville SC vs Sporting Kansas City — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 58.7%, EV -6.01%, EV robusto -14.01% → sin value.
  - St. Louis CITY SC vs Vancouver Whitecaps — Over 1.5 Goles (over_1_5): Prob modelo 81.5%, EV -7.11%, EV robusto -12.81% → sin value.
  - St. Louis CITY SC vs Vancouver Whitecaps — Under 1.5 Goles (under_1_5): Prob modelo 18.5%, EV +1.86%, EV robusto -25.64% → sin value.
  - St. Louis CITY SC vs Vancouver Whitecaps — Under 2.5 Goles (under_2_5): Prob modelo 27.5%, EV -31.25%, EV robusto -43.75% → sin value.
  - St. Louis CITY SC vs Vancouver Whitecaps — Under 3.5 Goles (under_3_5): Prob modelo 45.4%, EV -26.39%, EV robusto -34.49% → sin value.
  - St. Louis CITY SC vs Vancouver Whitecaps — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 42.5%, EV -18.43%, EV robusto -28.03% → sin value.
  - St. Louis CITY SC vs Vancouver Whitecaps — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 57.5%, EV -3.37%, EV robusto -11.77% → sin value.
  - Colorado Rapids vs Minnesota United — Under 2.5 Goles (under_2_5): Prob modelo 27.9%, EV -35.88%, EV robusto -47.38% → sin value.
  - Colorado Rapids vs Minnesota United — Over 8.5 Córners (over_corners_8_5): Prob modelo 57.5%, EV -13.81%, EV robusto -21.31% → sin value.
  - Colorado Rapids vs Minnesota United — Under 8.5 Córners (under_corners_8_5): Prob modelo 42.5%, EV +4.22%, EV robusto -8.03% → sin value.
  - Colorado Rapids vs Minnesota United — Over 9.5 Córners (over_corners_9_5): Prob modelo 47.7%, EV -12.76%, EV robusto -21.91% → sin value.
  - Colorado Rapids vs Minnesota United — Under 9.5 Córners (under_corners_9_5): Prob modelo 52.3%, EV -2.14%, EV robusto -11.49% → sin value.
  - Real Salt Lake vs San Jose Earthquakes — Under 2.5 Goles (under_2_5): Prob modelo 27.7%, EV -23.72%, EV robusto -37.47% → sin value.
  - Real Salt Lake vs San Jose Earthquakes — Under 3.5 Goles (under_3_5): Prob modelo 45.8%, EV -22.60%, EV robusto -31.05% → sin value.
  - Real Salt Lake vs San Jose Earthquakes — Over 8.5 Córners (over_corners_8_5): Prob modelo 67.5%, EV -11.56%, EV robusto -18.11% → sin value.
  - Real Salt Lake vs San Jose Earthquakes — Under 8.5 Córners (under_corners_8_5): Prob modelo 32.5%, EV +2.34%, EV robusto -13.41% → sin value.
  - Real Salt Lake vs San Jose Earthquakes — Over 9.5 Córners (over_corners_9_5): Prob modelo 58.5%, EV -9.93%, EV robusto -17.63% → sin value.
  - Real Salt Lake vs San Jose Earthquakes — Under 9.5 Córners (under_corners_9_5): Prob modelo 41.5%, EV -2.45%, EV robusto -14.20% → sin value.
  - Real Salt Lake vs San Jose Earthquakes — Over 10.5 Córners (over_corners_10_5): Prob modelo 49.5%, EV -7.50%, EV robusto -16.85% → sin value.
  - Real Salt Lake vs San Jose Earthquakes — Under 10.5 Córners (under_corners_10_5): Prob modelo 50.5%, EV -7.52%, EV robusto -16.67% → sin value.
  - LA Galaxy vs Portland Timbers — Under 2.5 Goles (under_2_5): Prob modelo 24.2%, EV -22.40%, EV robusto -38.40% → sin value.
  - LA Galaxy vs Portland Timbers — Under 3.5 Goles (under_3_5): Prob modelo 40.4%, EV -27.32%, EV robusto -36.32% → sin value.
  - LA Galaxy vs Portland Timbers — Over 8.5 Córners (over_corners_8_5): Prob modelo 59.0%, EV -14.41%, EV robusto -21.66% → sin value.
  - LA Galaxy vs Portland Timbers — Under 8.5 Córners (under_corners_8_5): Prob modelo 41.0%, EV +4.47%, EV robusto -8.28% → sin value.
  - LA Galaxy vs Portland Timbers — Over 9.5 Córners (over_corners_9_5): Prob modelo 49.3%, EV -14.19%, EV robusto -22.89% → sin value.
  - LA Galaxy vs Portland Timbers — Under 9.5 Córners (under_corners_9_5): Prob modelo 50.7%, EV -1.17%, EV robusto -10.92% → sin value.
  - LAFC vs Austin FC — Under 2.5 Goles (under_2_5): Prob modelo 29.3%, EV -31.22%, EV robusto -42.97% → sin value.
  - LAFC vs Austin FC — Under 3.5 Goles (under_3_5): Prob modelo 48.1%, EV -23.54%, EV robusto -31.49% → sin value.
  - San Diego FC vs Houston Dynamo — Under 2.5 Goles (under_2_5): Prob modelo 32.1%, EV -29.45%, EV robusto -40.45% → sin value.
- **Candidatos con value excluidos por probabilidad-primero:**
  - Feyenoord vs Como: Over 2.5 Goles (over_2_5) EV +15.99% / EV rob +8.79%, Victoria Feyenoord (1) EV +56.62% / EV rob +40.12% — No cumple los mínimos de selección probabilidad-primero.
  - LASK vs Liverpool: Victoria LASK (1) EV +19.35% / EV rob -27.60%, Empate (X) EV +47.41% / EV rob +16.61% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Real Betis vs FC Porto: Ambos marcan (BTTS) (btts_yes) EV +6.71% / EV rob -1.34%, Victoria FC Porto (2) EV +84.45% / EV rob +66.95% — No cumple los mínimos de selección probabilidad-primero.
  - Aston Villa vs Fenerbahce: Over 3.5 Goles (over_3_5) EV +34.68% / EV rob +22.78%, Doble Oportunidad Empate/Fenerbahce (x2) EV +65.96% / EV rob +54.71%, Under 8.5 Córners (under_corners_8_5) EV +41.05% / EV rob +28.05%, Victoria Fenerbahce (2) EV +128.69% / EV rob +106.19% — No cumple los mínimos de selección probabilidad-primero.
  - Shakhtar Donetsk vs AEK Athens: Empate (X) EV +11.51% / EV rob -5.34%, Victoria AEK Athens (2) EV +21.24% / EV rob +7.89%, No ambos marcan (btts_no) EV +47.56% / EV rob +36.31% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Roma vs Real Madrid: Victoria Roma (1) EV +18.44% / EV rob +0.19%, Doble Oportunidad Roma/Empate (1x) EV +6.96% / EV rob -2.59%, Under 8.5 Córners (under_corners_8_5) EV +10.15% / EV rob -1.85% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Slovan Bratislava vs VfB Stuttgart: Empate (X) EV +22.88% / EV rob -5.87%, Ambos marcan (BTTS) (btts_yes) EV +5.55% / EV rob -2.30%, Victoria Slovan Bratislava (1) EV +203.60% / EV rob +166.10% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Fluminense vs Palmeiras: Victoria Palmeiras (2) EV +31.47% / EV rob +18.37%, Over 2.5 Goles (over_2_5) EV +92.95% / EV rob +78.60%, Ambos marcan (BTTS) (btts_yes) EV +31.13% / EV rob +19.88%, Doble Oportunidad Empate/Palmeiras (x2) EV +10.99% / EV rob +3.69%, DNB Palmeiras (dnb_away) EV +16.16% / EV rob +7.16%, Over 3.5 Goles (over_3_5) EV +181.10% / EV rob +151.10% — No cumple los mínimos de selección probabilidad-primero.
  - CF Montreal vs Atlanta United FC: Victoria Atlanta United FC (2) EV +8.13% / EV rob -6.12%, Over 2.5 Goles (over_2_5) EV +6.92% / EV rob -0.78%, No ambos marcan (btts_no) EV +9.51% / EV rob -3.99%, Doble Oportunidad Empate/Atlanta United FC (x2) EV +3.59% / EV rob -4.56%, DNB Atlanta United FC (dnb_away) EV +8.32% / EV rob -2.58% — No cumple los mínimos de selección probabilidad-primero.
  - Columbus Crew vs Charlotte FC: Empate (X) EV +7.40% / EV rob -12.60%, No ambos marcan (btts_no) EV +32.72% / EV rob +17.97%, DNB Charlotte FC (dnb_away) EV +25.60% / EV rob +12.50%, Victoria Charlotte FC (2) EV +35.68% / EV rob +17.68% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - DC United vs New York Red Bulls: Victoria New York Red Bulls (2) EV +25.65% / EV rob +8.15%, Doble Oportunidad Empate/New York Red Bulls (x2) EV +12.37% / EV rob +3.02%, DNB New York Red Bulls (dnb_away) EV +26.15% / EV rob +11.95% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - FC Cincinnati vs New England Revolution: Empate (X) EV +10.12% / EV rob -12.88%, Over 3.5 Goles (over_3_5) EV +13.55% / EV rob +4.00%, No ambos marcan (btts_no) EV +9.74% / EV rob -5.51%, Under 3.5 Tarjetas (under_cards_3_5) EV +6.34% / EV rob -4.16%, Victoria New England Revolution (2) EV +71.49% / EV rob +50.49%, DNB New England Revolution (dnb_away) EV +60.72% / EV rob +43.97% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Inter Miami CF vs New York City FC: Empate (X) EV +11.02% / EV rob -12.98%, Victoria New York City FC (2) EV +38.55% / EV rob +12.30%, Over 3.5 Goles (over_3_5) EV +8.56% / EV rob -0.44%, No ambos marcan (btts_no) EV +8.20% / EV rob -6.30%, Doble Oportunidad Empate/New York City FC (x2) EV +17.88% / EV rob +5.98%, DNB New York City FC (dnb_away) EV +31.33% / EV rob +10.83% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Toronto FC vs Orlando City SC: Victoria Orlando City SC (2) EV +10.15% / EV rob -4.10%, Over 3.5 Goles (over_3_5) EV +10.21% / EV rob +0.11%, Doble Oportunidad Empate/Orlando City SC (x2) EV +6.36% / EV rob -1.94%, DNB Orlando City SC (dnb_away) EV +10.44% / EV rob -0.56%, No ambos marcan (btts_no) EV +27.48% / EV rob +10.98% — No cumple los mínimos de selección probabilidad-primero.
  - Chicago Fire vs Philadelphia Union: Victoria Philadelphia Union (2) EV +5.20% / EV rob -7.80%, No ambos marcan (btts_no) EV +10.89% / EV rob -4.61% — No cumple los mínimos de selección probabilidad-primero.
  - FC Dallas vs Seattle Sounders: Empate (X) EV +7.62% / EV rob -12.88%, No ambos marcan (btts_no) EV +12.53% / EV rob -0.47%, DNB Seattle Sounders (dnb_away) EV +28.65% / EV rob +14.05%, Victoria Seattle Sounders (2) EV +40.28% / EV rob +20.28% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Nashville SC vs Sporting Kansas City: Empate (X) EV +43.59% / EV rob +11.08%, Victoria Sporting Kansas City (2) EV +72.40% / EV rob +22.40%, DNB Sporting Kansas City (dnb_away) EV +101.39% / EV rob +49.39%, Doble Oportunidad Empate/Sporting Kansas City (x2) EV +73.01% / EV rob +51.01% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - St. Louis CITY SC vs Vancouver Whitecaps: Over 2.5 Goles (over_2_5) EV +8.75% / EV rob +1.25%, Over 3.5 Goles (over_3_5) EV +20.03% / EV rob +9.03%, No ambos marcan (btts_no) EV +8.87% / EV rob -5.38%, DNB Vancouver Whitecaps (dnb_away) EV +35.98% / EV rob +24.48%, Victoria Vancouver Whitecaps (2) EV +45.29% / EV rob +30.29% — No cumple los mínimos de selección probabilidad-primero.
  - Colorado Rapids vs Minnesota United: Victoria Minnesota United (2) EV +12.29% / EV rob -3.71% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Real Salt Lake vs San Jose Earthquakes: Over 2.5 Goles (over_2_5) EV +6.94% / EV rob -0.46%, Over 3.5 Goles (over_3_5) EV +16.53% / EV rob +5.78%, No ambos marcan (btts_no) EV +7.27% / EV rob -6.73%, Victoria San Jose Earthquakes (2) EV +56.78% / EV rob +40.03% — No cumple los mínimos de selección probabilidad-primero.
  - LA Galaxy vs Portland Timbers: Victoria Portland Timbers (2) EV +21.74% / EV rob +6.24%, Over 2.5 Goles (over_2_5) EV +6.05% / EV rob -0.95%, No ambos marcan (btts_no) EV +13.68% / EV rob -2.07% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - LAFC vs Austin FC: Empate (X) EV +6.86% / EV rob -16.14%, Victoria Austin FC (2) EV +20.18% / EV rob -9.82%, Over 2.5 Goles (over_2_5) EV +11.05% / EV rob +3.20%, Over 3.5 Goles (over_3_5) EV +21.99% / EV rob +10.24% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - San Diego FC vs Houston Dynamo: Victoria Houston Dynamo (2) EV +6.93% / EV rob -8.32%, Over 2.5 Goles (over_2_5) EV +12.08% / EV rob +3.83%, Doble Oportunidad Empate/Houston Dynamo (x2) EV +11.69% / EV rob +2.49% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Manchester City vs Paris Saint-Germain: Victoria Paris Saint-Germain (2) EV +55.03% / EV rob +38.53% — Cuota alta admitida solo como excepción robusta.
  - Bodo/Glimt vs Borussia Dortmund: Victoria Bodo/Glimt (1) EV +54.26% / EV rob +39.26%, No ambos marcan (btts_no) EV +33.45% / EV rob +16.95% — Cuota alta admitida solo como excepción robusta.
- **Partidos sin datos suficientes (NO BET, motor no ejecutado):**
  - Atletico Mineiro vs Montevideo City Torque: Montevideo City Torque (Uruguay) no tiene xG por partido ni rating Elo en ninguna fuente consultada (statz.ai, understat y xg-edge no cubren la liga uruguaya). Ejecutar el motor habria exigido priors por defecto para el visitante, por lo que no se ejecuto.

## Portfolio y Correlaciones
- **Exposición total:** 0.57u
- **Correlaciones detectadas:** Mercados presentes: over_1_5, over_2_5, under_2_5, x2. Verificar solapamiento de mercado mismo partido.
- **Ajuste de stake por correlación:** Los picks pertenecen a partidos distintos; no se aplica reducción adicional por eventos dependientes.

## Tracking
_Fuente: resultados vía websearch (MCP apifootball no operativo — fallback activo). Actualizado 2026-10-23._
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1 (Real Betis vs FC Porto - over_2_5) | GANADA | 3 - 2 | +0.10u |
| Pick 2 (Fluminense vs Palmeiras - over_1_5) | GANADA | 1 - 2 | +0.06u |
| Pick 3 (Aston Villa vs Fenerbahce - over_2_5) | GANADA | 6 - 0 | +0.04u |
| Pick 4 (St. Louis CITY SC vs Vancouver Whitecaps - x2) | GANADA | 0 - 0 | +0.06u |
| Pick 5 (Shakhtar Donetsk vs AEK Athens - under_2_5) | PERDIDA | 3 - 1 | -0.11u |
| Pick 6 (Colorado Rapids vs Minnesota United - over_2_5) | GANADA | 2 - 2 | +0.04u |
| **Total** | | | **+0.19u (5 G / 1 P)** |
