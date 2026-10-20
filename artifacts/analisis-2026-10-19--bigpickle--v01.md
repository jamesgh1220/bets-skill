# Análisis de Apuestas — 19 de octubre de 2026

## Metadatos
- **Fecha de análisis:** 2026-10-19T14:30:17Z
- **Fecha(s) de partido:** 19 de octubre de 2026
- **Information cutoff:** 2026-10-19T14:30:17Z
- **Modelo de IA:** bigpickle
- **Versión del motor predictivo:** model-v1.3
- **Ligas analizadas:** Liga Profesional Argentina (Clausura, F14), Liga BetPlay Colombia (Finalizacion, Fecha 15), Premier League (J7), LaLiga (J9), Serie A (J7) y Liga Portugal (jornada aplazada)
- **Rango de fechas solicitado:** 19 de octubre de 2026 - Liga Argentina, Liga Colombiana, Liga Espanola (LaLiga), Premier League, Serie A y Liga Portugal (todos los partidos)
- **Partidos en universo:** 9
- **Picks iniciales con value:** 85
- **Picks finales seleccionados:** 6

## Universo Analizado
Universo = interseccion(ligas: Liga Profesional Argentina, Liga BetPlay Colombia, Premier League, LaLiga, Serie A y Liga Portugal, fecha local 19 de octubre de 2026, todos los partidos programados). Cutoff de informacion 2026-10-19T14:30:17Z, anterior al primer kickoff (16:30 UTC, Monza vs Cagliari). No se usa informacion posterior a ningun kickoff. Universo final = 9 partidos, todos con los 4 valores de xG verificables y con los 8 campos obligatorios de corners/tarjetas (for/against por equipo) cargados antes de ejecutar el motor: Serie A J7 Monza vs Cagliari (16:30 UTC) y Parma vs Torino (18:45 UTC); Premier League J7 Tottenham vs Coventry (19:00 UTC); LaLiga J9 Getafe vs Rayo Vallecano (19:00 UTC); Liga Portugal SC Braga vs Gil Vicente (19:15 UTC, jornada aplazada); Liga Profesional Argentina Clausura F14 Newell's vs Central Cordoba y Sarmiento vs Barracas Central (22:00 UTC del 19/10) y Deportivo Riestra vs Union (00:15 UTC del 20/10 = 21:15 ART del 19/10, por lo que su fecha local cae dentro del rango); Liga BetPlay Colombia Deportivo Pasto vs Alianza Valledupar (01:05 UTC del 20/10 = 20:05 COL del 19/10, fecha local dentro del rango). Se verifico que no hubiera otros partidos de esas 6 ligas en la fecha: en Colombia Millonarios vs Jaguares (Fecha 15) se reprogramo al sabado 17/10 y queda fuera del universo; la Premier League, LaLiga, Serie A y Liga Portugal solo programan esos partidos ese dia. MCPs inoperativos en esta sesion (football-stats, odds-api y apifootball), por lo que toda la recoleccion se hizo via web del agente: understat.com y performanceodds.com (xG), FBref/ClubElo snapshot 2026-10-15 (Elo), statsbet.es y Sofascore publica (corners/tarjetas y xG de Argentina/Colombia), sportytrader.com y oddssafari.com (cuotas 1X2/DC/DNB/BTTS/O-U/corners/tarjetas). Mercados de corners y tarjetas: se cotizaron AMBOS lados de cada linea evaluada (goles 1.5/2.5/3.5, corners 8.5/9.5/10.5 y tarjetas 3.5/4.5/5.5) donde hubo cuota verificable; los tramos sin cuota quedan consignados como 'sin cotizar' y no se operan: Serie A (Monza-Cagliari y Parma-Torino) sin tarjetas 4.5/5.5 cotizadas; Tottenham sin tarjetas 4.5/5.5 (3.5 con una sola casa); Getafe sin tarjetas 3.5; Braga sin tarjetas 5.5. DISCREPANCIAS >2% reportadas y NO sustituidas (detalladas en notes por partido): xG de Barracas Central (statsbet 0.77 vs Sofascore 0.41 por partido), O2.5/U2.5 de Braga (oddssafari 2.03/1.86 vs 1.85/1.75 usados) y xG de Parma/Torino (performanceodds). BANDERAS DE BAJA CONFIANZA (documentadas, el motor se ejecuto igual porque los 4 xG existen): las paginas statsbet de Barracas Central y Riestra estan auto-encuadradas en Copa Sudamericana 2026 (ventana de stats ambigua); en los 4 partidos de Argentina y Colombia los for/against de corners/tarjetas se derivaron aritmeticamente donde la fuente no expone for/against directo; Alianza Valledupar no esta en clubelo (Elo nulo: se omitio la clave del input y el motor aplica su default neutral 1500/1500, por lo que ese partido se apoya mas en xG y menos en ratings); lesiones, suspensiones y estado de entrenamiento NO VERIFICADOS en los 4 partidos de Argentina y Colombia (la busqueda web no devolvio resultados confiables pre-kickoff).
1. **Premier League - jornada 7:** Tottenham vs Coventry City (19T19:00Z). 1X2 1.50 4.50 5.40; O1.5 1.19 U1.5 5.00 O2.5 1.53 U2.5 2.30 O3.5 2.52 U3.5 1.57; btts_yes 1.65 btts_no 2.04 1x 1.13 x2 2.38 over_corners_8_5 1.37 under_corners_8_5 3.20 over_corners_9_5 1.61 under_corners_9_5 2.30 over_corners_10_5 2.01 under_corners_10_5 1.80 over_cards_3_5 2.13 under_cards_3_5 1.63. Elo 1799/1705; xG 1.31/1.68 vs 1.11/1.8.
2. **LaLiga - jornada 9:** Getafe vs Rayo Vallecano (19T19:00Z). 1X2 2.92 2.90 2.55; O1.5 1.63 U1.5 2.50 O2.5 2.65 U2.5 1.38 O3.5 6.00 U3.5 1.17; btts_yes 2.13 btts_no 1.58 1x 1.44 x2 1.32 over_corners_8_5 1.62 under_corners_8_5 2.40 over_corners_9_5 1.98 under_corners_9_5 1.85 over_corners_10_5 2.55 under_corners_10_5 1.51 over_cards_4_5 1.40 under_cards_4_5 2.75 over_cards_5_5 1.80 under_cards_5_5 1.90. Elo 1700/1746; xG 0.81/1.71 vs 1.3/1.86.
3. **Liga Portugal - jornada 2 (aplazada):** SC Braga vs Gil Vicente (19T19:15Z). 1X2 1.47 3.95 6.25; O1.5 1.34 U1.5 3.50 O2.5 1.85 U2.5 1.75 O3.5 3.50 U3.5 1.33; btts_yes 1.98 btts_no 1.65 1x 1.11 x2 2.48 over_corners_8_5 1.75 under_corners_8_5 2.20 over_corners_9_5 2.30 under_corners_9_5 1.75 over_corners_10_5 3.10 under_corners_10_5 1.45 over_cards_3_5 1.45 under_cards_3_5 2.45 over_cards_4_5 2.10 under_cards_4_5 1.65. Elo 1726/1571; xG 1.52/0.92 vs 1.47/1.09.
4. **Liga Profesional Argentina - Clausura 2026, fecha 14:** Newell's Old Boys vs Central Córdoba (19T22:00Z). 1X2 1.90 3.40 5.25; O1.5 1.50 U1.5 2.75 O2.5 2.42 U2.5 1.57 O3.5 4.60 U3.5 1.20; btts_yes 2.20 btts_no 1.67 1x 1.21 x2 1.95 12 1.33 over_corners_8_5 1.81 under_corners_8_5 2.08 over_corners_9_5 2.38 under_corners_9_5 1.65 over_corners_10_5 3.25 under_corners_10_5 1.37 over_cards_3_5 1.33 under_cards_3_5 2.95 over_cards_4_5 1.80 under_cards_4_5 1.90. Elo 1625/1619; xG 0.94/1.36 vs 0.66/1.53.
5. **Liga Profesional Argentina - Clausura 2026, fecha 14:** Sarmiento vs Barracas Central (19T22:00Z). 1X2 2.35 3.00 3.70; O1.5 1.61 U1.5 2.38 O2.5 2.90 U2.5 1.48 O3.5 6.00 U3.5 1.17; btts_yes 2.30 btts_no 1.67 1x 1.33 x2 1.62 12 1.40 over_corners_8_5 1.95 under_corners_8_5 1.87 over_corners_9_5 2.62 under_corners_9_5 1.55 over_corners_10_5 3.70 under_corners_10_5 1.30 over_cards_4_5 1.47 under_cards_4_5 2.45 over_cards_5_5 1.95 under_cards_5_5 1.75. Elo 1625/1639; xG 0.93/1.31 vs 0.77/1.23.
6. **Liga Profesional Argentina - Clausura 2026, fecha 14:** Deportivo Riestra vs Unión de Santa Fe (20T00:15Z). 1X2 2.30 2.97 3.90; O1.5 1.60 U1.5 2.40 O2.5 2.90 U2.5 1.48 O3.5 6.00 U3.5 1.17; btts_yes 2.30 btts_no 1.67 1x 1.30 x2 1.67 12 1.40 over_corners_8_5 1.97 under_corners_8_5 1.90 over_corners_9_5 2.65 under_corners_9_5 1.53 over_corners_10_5 3.70 under_corners_10_5 1.30 over_cards_3_5 1.27 under_cards_3_5 3.25 over_cards_4_5 1.68 under_cards_4_5 2.05. Elo 1612/1627; xG 0.79/0.86 vs 1.41/1.12.
7. **Liga BetPlay Dimayor - Finalización 2026:** Deportivo Pasto vs Alianza Valledupar FC (20T01:05Z). 1X2 1.77 3.55 5.25; O1.5 1.40 U1.5 3.25 O2.5 2.20 U2.5 1.73 O3.5 4.20 U3.5 1.27; btts_yes 2.05 btts_no 1.80 1x 1.19 x2 2.12 12 1.30 over_corners_8_5 1.95 under_corners_8_5 1.95 over_corners_9_5 2.60 under_corners_9_5 1.60 over_corners_10_5 3.65 under_corners_10_5 1.37 over_cards_4_5 1.30 under_cards_4_5 3.00 over_cards_5_5 1.65 under_cards_5_5 2.10. Elo 1533/None; xG 0.81/0.69 vs 1.0/1.05.
8. **Serie A - jornada 7:** Monza vs Cagliari (19T16:30Z). 1X2 2.45 3.30 3.29; O1.5 1.37 U1.5 3.40 O2.5 2.13 U2.5 1.83 O3.5 3.70 U3.5 1.33; btts_yes 1.80 btts_no 2.05 1x 1.38 x2 1.65 12 1.38 over_corners_8_5 1.62 under_corners_8_5 2.30 over_corners_9_5 2.00 under_corners_9_5 1.78 over_corners_10_5 2.65 under_corners_10_5 1.48 over_cards_3_5 1.85 under_cards_3_5 1.85. Elo 1636/1678; xG 1.87/1.6 vs 1.04/1.86.
9. **Serie A - jornada 7:** Parma vs Torino (19T18:45Z). 1X2 3.43 3.17 2.45; O1.5 1.48 U1.5 3.00 O2.5 2.49 U2.5 1.63 O3.5 4.60 U3.5 1.23; btts_yes 2.00 btts_no 1.86 1x 1.62 x2 1.39 12 1.41 over_corners_8_5 1.86 under_corners_8_5 2.00 over_corners_9_5 2.45 under_corners_9_5 1.62 over_corners_10_5 3.40 under_corners_10_5 1.37 over_cards_3_5 1.70 under_cards_3_5 2.02. Elo 1643/1685; xG 0.78/2.12 vs 1.24/1.38.

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Deportivo Pasto vs Alianza Valledupar FC | under_3_5 | Under 3.5 Goles | excluido | 1.27 | 90.8% | 1.10 | +15.27% | +15.27% | +8.92% | 0.14u | Media-Alta |
| 2 | Monza vs Cagliari | over_1_5 | Over 1.5 Goles | excluido | 1.37 | 83.3% | 1.20 | +14.07% | +14.07% | +7.22% | 0.10u | Media-Alta |
| 3 | Deportivo Riestra vs Unión de Santa Fe | under_corners_10_5 | Under 10.5 Córners | excluido | 1.30 | 83.1% | 1.20 | +8.07% | +8.07% | +1.57% | 0.07u | Media-Alta |
| 4 | Parma vs Torino | x2 | Doble Oportunidad Empate/Torino | excluido | 1.39 | 79.7% | 1.25 | +10.84% | +10.84% | +3.89% | 0.07u | Media-Alta |
| 5 | Getafe vs Rayo Vallecano | over_1_5 | Over 1.5 Goles | prioritario | 1.63 | 78.3% | 1.28 | +27.58% | +27.58% | +19.43% | 0.11u | Media-Alta |
| 6 | Parma vs Torino | under_corners_10_5 | Under 10.5 Córners | excluido | 1.37 | 77.2% | 1.30 | +5.76% | +5.76% | -1.09% | 0.04u | Media-Alta |
| 7 | Parma vs Torino | over_1_5 | Over 1.5 Goles | excluido | 1.48 | 76.9% | 1.30 | +13.83% | +13.83% | +6.43% | 0.07u | Media-Alta |
| 8 | Monza vs Cagliari | 12 | Doble Oportunidad Monza/Cagliari | excluido | 1.38 | 76.4% | 1.31 | +5.81% | +5.81% | -1.11% | 0.04u | Media-Alta |
| 9 | Deportivo Riestra vs Unión de Santa Fe | under_corners_9_5 | Under 9.5 Córners | prioritario | 1.53 | 76.1% | 1.31 | +16.62% | +16.62% | +8.96% | 0.08u | Media-Alta |
| 10 | Parma vs Torino | under_cards_3_5 | Under 3.5 Tarjetas | prioritario | 2.02 | 75.9% | 1.32 | +53.43% | +53.43% | +43.33% | 0.13u | Media-Alta |
| 11 | Monza vs Cagliari | over_2_5 | Over 2.5 Goles | prioritario | 2.13 | 75.6% | 1.32 | +61.17% | +61.17% | +50.51% | 0.14u | Media-Alta |
| 12 | Parma vs Torino | 12 | Doble Oportunidad Parma/Torino | excluido | 1.41 | 74.8% | 1.34 | +5.30% | +5.30% | -1.74% | 0.03u | Media-Alta |
| 13 | Monza vs Cagliari | 1x | Doble Oportunidad Monza/Empate | excluido | 1.38 | 74.8% | 1.34 | +3.45% | +3.45% | -3.47% | 0.02u | Media-Alta |
| 14 | Deportivo Pasto vs Alianza Valledupar FC | under_2_5 | Under 2.5 Goles | prioritario | 1.73 | 71.2% | 1.40 | +22.96% | +22.96% | +14.33% | 0.08u | Media-Alta |
| 15 | Deportivo Riestra vs Unión de Santa Fe | x2 | Doble Oportunidad Empate/Unión de Santa Fe | prioritario | 1.67 | 70.3% | 1.42 | +17.14% | +17.14% | +8.81% | 0.06u | Media-Alta |
| 16 | Tottenham vs Coventry City | over_2_5 | Over 2.5 Goles | excluido | 1.53 | 70.0% | 1.43 | +7.04% | +7.04% | -0.61% | 0.03u | Media-Alta |
| 17 | Parma vs Torino | under_corners_9_5 | Under 9.5 Córners | excluido | 1.62 | 69.1% | 1.45 | +12.01% | +12.01% | +3.91% | 0.05u | Media-Alta |
| 18 | Getafe vs Rayo Vallecano | over_corners_8_5 | Over 8.5 Córners | excluido | 1.62 | 68.9% | 1.45 | +11.62% | +11.62% | +3.52% | 0.05u | Media-Alta |
| 19 | Deportivo Riestra vs Unión de Santa Fe | under_corners_8_5 | Under 8.5 Córners | prioritario | 1.90 | 67.2% | 1.49 | +27.67% | +27.67% | +18.17% | 0.08u | Media-Alta |
| 20 | Getafe vs Rayo Vallecano | over_2_5 | Over 2.5 Goles | excluido | 2.65 | 67.0% | 1.49 | +77.42% | +77.42% | +64.17% | 0.12u | Media-Alta |
| 21 | Deportivo Pasto vs Alianza Valledupar FC | btts_no | No ambos marcan | prioritario | 1.80 | 65.8% | 1.52 | +18.39% | +18.39% | +9.39% | 0.06u | Media-Alta |
| 22 | Monza vs Cagliari | under_cards_3_5 | Under 3.5 Tarjetas | prioritario | 1.85 | 64.9% | 1.54 | +20.01% | +20.01% | +10.76% | 0.06u | Media-Alta |
| 23 | Parma vs Torino | over_2_5 | Over 2.5 Goles | excluido | 2.49 | 64.6% | 1.55 | +60.71% | +60.71% | +48.27% | 0.10u | Media-Alta |
| 24 | Deportivo Pasto vs Alianza Valledupar FC | over_cards_5_5 | Over 5.5 Tarjetas | excluido | 1.65 | 64.1% | 1.56 | +5.74% | +5.74% | -2.51% | 0.02u | Media-Alta |
| 25 | Getafe vs Rayo Vallecano | under_cards_5_5 | Under 5.5 Tarjetas | prioritario | 1.90 | 63.4% | 1.58 | +20.39% | +20.39% | +10.89% | 0.06u | Media-Alta |
| 26 | Sarmiento vs Barracas Central | under_cards_5_5 | Under 5.5 Tarjetas | excluido | 1.75 | 63.4% | 1.58 | +10.88% | +10.88% | +2.13% | 0.04u | Media-Alta |
| 27 | Sarmiento vs Barracas Central | x2 | Doble Oportunidad Empate/Barracas Central | excluido | 1.62 | 63.0% | 1.59 | +2.03% | +2.03% | -6.07% | 0.01u | Media-Alta |
| 28 | Monza vs Cagliari | btts_yes | Ambos marcan (BTTS) | excluido | 1.80 | 60.8% | 1.65 | +9.40% | +9.40% | +0.40% | 0.03u | Media-Alta |
| 29 | Sarmiento vs Barracas Central | over_corners_8_5 | Over 8.5 Córners | prioritario | 1.95 | 60.2% | 1.66 | +17.33% | +17.33% | +7.58% | 0.05u | Media-Alta |
| 30 | Deportivo Pasto vs Alianza Valledupar FC | x2 | Doble Oportunidad Empate/Alianza Valledupar FC | prioritario | 2.12 | 60.1% | 1.66 | +27.48% | +27.48% | +16.88% | 0.06u | Media-Alta |
| 31 | SC Braga vs Gil Vicente | under_corners_9_5 | Under 9.5 Córners | excluido | 1.75 | 60.1% | 1.66 | +5.14% | +5.14% | -3.61% | 0.02u | Media-Alta |
| 32 | Getafe vs Rayo Vallecano | over_corners_9_5 | Over 9.5 Córners | prioritario | 1.98 | 60.0% | 1.67 | +18.88% | +18.88% | +8.98% | 0.05u | Media-Alta |
| 33 | Parma vs Torino | under_corners_8_5 | Under 8.5 Córners | prioritario | 2.00 | 59.6% | 1.68 | +19.12% | +19.12% | +9.12% | 0.05u | Media-Alta |
| 34 | Monza vs Cagliari | over_3_5 | Over 3.5 Goles | excepcional | 3.70 | 59.4% | 1.68 | +119.85% | +119.85% | +101.35% | 0.11u | Media-Alta |
| 35 | Tottenham vs Coventry City | under_corners_10_5 | Under 10.5 Córners | excluido | 1.80 | 58.7% | 1.70 | +5.64% | +5.64% | -3.36% | 0.02u | Media-Alta |
| 36 | Newell's Old Boys vs Central Córdoba | under_cards_4_5 | Under 4.5 Tarjetas | excluido | 1.90 | 58.6% | 1.71 | +11.41% | +11.41% | +1.91% | 0.03u | Media-Alta |
| 37 | Getafe vs Rayo Vallecano | btts_yes | Ambos marcan (BTTS) | prioritario | 2.13 | 58.2% | 1.72 | +23.90% | +23.90% | +13.25% | 0.05u | Media-Alta |
| 38 | SC Braga vs Gil Vicente | over_2_5 | Over 2.5 Goles | excluido | 1.85 | 56.3% | 1.78 | +4.10% | +4.10% | -5.15% | 0.01u | Media |
| 39 | Parma vs Torino | btts_yes | Ambos marcan (BTTS) | excluido | 2.00 | 56.0% | 1.79 | +11.90% | +11.90% | +1.90% | 0.03u | Media |
| 40 | Newell's Old Boys vs Central Córdoba | x2 | Doble Oportunidad Empate/Central Córdoba | excluido | 1.95 | 55.8% | 1.79 | +8.85% | +8.85% | -0.90% | 0.02u | Media |
| 41 | Parma vs Torino | 2 | Victoria Torino | excluido | 2.45 | 54.6% | 1.83 | +33.72% | +33.72% | +21.47% | 0.06u | Media |
| 42 | Parma vs Torino | dnb_away | DNB Torino | excluido | 1.67 | 54.6% | 1.37 | +16.31% | +16.31% | +7.96% | 0.06u | Media |
| 43 | Tottenham vs Coventry City | x2 | Doble Oportunidad Empate/Coventry City | excluido | 2.38 | 54.6% | 1.83 | +29.88% | +29.88% | +17.98% | 0.05u | Media |
| 44 | SC Braga vs Gil Vicente | x2 | Doble Oportunidad Empate/Gil Vicente | excluido | 2.48 | 54.3% | 1.84 | +34.71% | +34.71% | +22.31% | 0.06u | Media |
| 45 | Monza vs Cagliari | 1 | Victoria Monza | excluido | 2.45 | 51.2% | 1.95 | +25.31% | +25.31% | +13.08% | 0.04u | Media |
| 46 | Monza vs Cagliari | dnb_home | DNB Monza | excluido | 1.65 | 51.2% | 1.49 | +8.05% | +8.05% | -0.20% | 0.03u | Media |
| 47 | Getafe vs Rayo Vallecano | over_corners_10_5 | Over 10.5 Córners | excluido | 2.55 | 51.1% | 1.96 | +30.30% | +30.30% | +17.55% | 0.05u | Media |
| 48 | Tottenham vs Coventry City | over_3_5 | Over 3.5 Goles | excluido | 2.52 | 50.8% | 1.97 | +27.92% | +27.92% | +15.32% | 0.05u | Media |
| 49 | Sarmiento vs Barracas Central | over_corners_9_5 | Over 9.5 Córners | excluido | 2.62 | 50.5% | 1.98 | +32.62% | +32.62% | +19.49% | 0.05u | Media |
| 50 | SC Braga vs Gil Vicente | under_corners_8_5 | Under 8.5 Córners | excluido | 2.20 | 50.2% | 1.99 | +10.34% | +10.34% | -0.66% | 0.02u | Media |
| 51 | Getafe vs Rayo Vallecano | under_cards_4_5 | Under 4.5 Tarjetas | excluido | 2.75 | 50.0% | 2.00 | +37.60% | +37.60% | +23.85% | 0.05u | Media |
| 52 | Sarmiento vs Barracas Central | under_cards_4_5 | Under 4.5 Tarjetas | excluido | 2.45 | 50.0% | 2.00 | +22.58% | +22.58% | +10.33% | 0.04u | Media |
| 53 | Tottenham vs Coventry City | under_corners_9_5 | Under 9.5 Córners | excluido | 2.30 | 49.5% | 2.02 | +13.80% | +13.80% | +2.30% | 0.03u | Baja |
| 54 | SC Braga vs Gil Vicente | under_cards_3_5 | Under 3.5 Tarjetas | excluido | 2.45 | 47.7% | 2.10 | +16.86% | +16.86% | +4.61% | 0.03u | Baja |
| 55 | Newell's Old Boys vs Central Córdoba | over_2_5 | Over 2.5 Goles | excluido | 2.42 | 47.0% | 2.13 | +13.81% | +13.81% | +1.71% | 0.02u | Baja |
| 56 | Getafe vs Rayo Vallecano | over_3_5 | Over 3.5 Goles | excepcional | 6.00 | 46.4% | 2.15 | +178.64% | +178.64% | +148.64% | 0.09u | Baja |
| 57 | Deportivo Pasto vs Alianza Valledupar FC | under_1_5 | Under 1.5 Goles | excepcional | 3.25 | 46.3% | 2.16 | +50.34% | +50.34% | +34.10% | 0.06u | Baja |
| 58 | Parma vs Torino | over_3_5 | Over 3.5 Goles | excepcional | 4.60 | 43.2% | 2.31 | +98.86% | +98.86% | +75.86% | 0.07u | Baja |
| 59 | Newell's Old Boys vs Central Córdoba | under_cards_3_5 | Under 3.5 Tarjetas | excluido | 2.95 | 43.2% | 2.31 | +27.50% | +27.50% | +12.75% | 0.04u | Baja |
| 60 | Getafe vs Rayo Vallecano | 2 | Victoria Rayo Vallecano | excluido | 2.55 | 43.2% | 2.31 | +10.19% | +10.19% | -2.56% | 0.02u | Baja |
| 61 | Sarmiento vs Barracas Central | over_2_5 | Over 2.5 Goles | excluido | 2.90 | 42.2% | 2.37 | +22.52% | +22.52% | +8.02% | 0.03u | Baja |
| 62 | Sarmiento vs Barracas Central | over_corners_10_5 | Over 10.5 Córners | excepcional | 3.70 | 41.3% | 2.42 | +52.85% | +52.85% | +34.35% | 0.05u | Baja |
| 63 | Deportivo Riestra vs Unión de Santa Fe | over_2_5 | Over 2.5 Goles | excluido | 2.90 | 41.1% | 2.43 | +19.13% | +19.13% | +4.63% | 0.03u | Baja |
| 64 | Monza vs Cagliari | over_corners_10_5 | Over 10.5 Córners | excluido | 2.65 | 40.6% | 2.46 | +7.52% | +7.52% | -5.73% | 0.01u | Baja |
| 65 | Tottenham vs Coventry City | under_corners_8_5 | Under 8.5 Córners | excepcional | 3.20 | 39.8% | 2.51 | +27.45% | +27.45% | +11.45% | 0.03u | Baja |
| 66 | Deportivo Riestra vs Unión de Santa Fe | 2 | Victoria Unión de Santa Fe | excepcional | 3.90 | 39.5% | 2.53 | +53.93% | +53.93% | +34.43% | 0.05u | Baja |
| 67 | Deportivo Riestra vs Unión de Santa Fe | dnb_away | DNB Unión de Santa Fe | excluido | 2.50 | 39.5% | 1.75 | +29.49% | +29.49% | +16.99% | 0.05u | Baja |
| 68 | Newell's Old Boys vs Central Córdoba | over_corners_10_5 | Over 10.5 Córners | excluido | 3.25 | 33.9% | 2.95 | +10.01% | +10.01% | -6.24% | 0.01u | Baja |
| 69 | Deportivo Pasto vs Alianza Valledupar FC | X | Empate | excluido | 3.55 | 33.6% | 2.98 | +19.24% | +19.24% | +1.49% | 0.02u | Baja |
| 70 | SC Braga vs Gil Vicente | over_3_5 | Over 3.5 Goles | excluido | 3.50 | 32.7% | 3.05 | +14.59% | +14.59% | -2.91% | 0.01u | Baja |
| 71 | Sarmiento vs Barracas Central | 2 | Victoria Barracas Central | excluido | 3.70 | 32.3% | 3.10 | +19.40% | +19.40% | +0.90% | 0.02u | Baja |
| 72 | Sarmiento vs Barracas Central | dnb_away | DNB Barracas Central | excluido | 2.40 | 32.3% | 2.15 | +8.16% | +8.16% | -3.84% | 0.01u | Baja |
| 73 | Tottenham vs Coventry City | 2 | Victoria Coventry City | excluido | 5.40 | 29.9% | 3.34 | +61.68% | +61.68% | +34.68% | 0.04u | Baja |
| 74 | Tottenham vs Coventry City | dnb_away | DNB Coventry City | excluido | 3.95 | 29.9% | 2.52 | +42.90% | +42.90% | +23.15% | 0.04u | Baja |
| 75 | SC Braga vs Gil Vicente | 2 | Victoria Gil Vicente | excluido | 6.25 | 27.5% | 3.64 | +71.94% | +71.94% | +40.69% | 0.03u | Baja |
| 76 | SC Braga vs Gil Vicente | dnb_away | DNB Gil Vicente | excluido | 4.70 | 27.5% | 2.66 | +56.11% | +56.11% | +32.61% | 0.04u | Baja |
| 77 | SC Braga vs Gil Vicente | X | Empate | excluido | 3.95 | 26.8% | 3.73 | +5.90% | +5.90% | -13.85% | 0.00u | Baja |
| 78 | Newell's Old Boys vs Central Córdoba | 2 | Victoria Central Córdoba | excluido | 5.25 | 26.6% | 3.76 | +39.75% | +39.75% | +13.51% | 0.02u | Baja |
| 79 | Newell's Old Boys vs Central Córdoba | dnb_away | DNB Central Córdoba | excluido | 3.50 | 26.6% | 2.66 | +22.37% | +22.37% | +4.87% | 0.02u | Baja |
| 80 | Deportivo Pasto vs Alianza Valledupar FC | dnb_away | DNB Alianza Valledupar FC | excluido | 3.75 | 26.6% | 2.50 | +33.15% | +33.15% | +14.40% | 0.03u | Baja |
| 81 | Deportivo Pasto vs Alianza Valledupar FC | 2 | Victoria Alianza Valledupar FC | excluido | 5.25 | 26.6% | 3.77 | +39.39% | +39.39% | +13.14% | 0.02u | Baja |
| 82 | Tottenham vs Coventry City | X | Empate | excluido | 4.50 | 24.6% | 4.06 | +10.88% | +10.88% | -11.62% | 0.01u | Baja |
| 83 | Newell's Old Boys vs Central Córdoba | over_3_5 | Over 3.5 Goles | excluido | 4.60 | 23.0% | 4.34 | +5.94% | +5.94% | -17.06% | 0.00u | Baja |
| 84 | Sarmiento vs Barracas Central | over_3_5 | Over 3.5 Goles | excluido | 6.00 | 18.7% | 5.34 | +12.32% | +12.32% | -17.68% | 0.01u | Baja |
| 85 | Deportivo Riestra vs Unión de Santa Fe | over_3_5 | Over 3.5 Goles | excluido | 6.00 | 17.8% | 5.63 | +6.62% | +6.62% | -23.38% | 0.00u | Baja |

## Evaluación Over/Under por Partido
Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada (n/d = cuota no disponible en la corrida).
| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |
|---|---|---|---:|---:|---:|---:|---:|---|
| Tottenham vs Coventry City | 1.5 | 80.0% | 1.19 | -4.81% | 20.0% | 5.00 | +0.05% | Sin value |
| Tottenham vs Coventry City | 2.5 | 70.0% | 1.53 | +7.04% | 30.0% | 2.30 | -30.91% | Value Over |
| Tottenham vs Coventry City | 3.5 | 50.8% | 2.52 | +27.92% | 49.2% | 1.57 | -22.69% | Value Over |
| Getafe vs Rayo Vallecano | 1.5 | 78.3% | 1.63 | +27.58% | 21.7% | 2.50 | -45.67% | Value Over |
| Getafe vs Rayo Vallecano | 2.5 | 67.0% | 2.65 | +77.42% | 33.1% | 1.38 | -54.39% | Value Over |
| Getafe vs Rayo Vallecano | 3.5 | 46.4% | 6.00 | +178.64% | 53.6% | 1.17 | -37.33% | Value Over |
| SC Braga vs Gil Vicente | 1.5 | 72.0% | 1.34 | -3.49% | 28.0% | 3.50 | -2.07% | Sin value |
| SC Braga vs Gil Vicente | 2.5 | 56.3% | 1.85 | +4.10% | 43.7% | 1.75 | -23.47% | Value Over |
| SC Braga vs Gil Vicente | 3.5 | 32.7% | 3.50 | +14.59% | 67.3% | 1.33 | -10.54% | Value Over |
| Newell's Old Boys vs Central Córdoba | 1.5 | 66.4% | 1.50 | -0.41% | 33.6% | 2.75 | -7.57% | Sin value |
| Newell's Old Boys vs Central Córdoba | 2.5 | 47.0% | 2.42 | +13.81% | 53.0% | 1.57 | -16.78% | Value Over |
| Newell's Old Boys vs Central Córdoba | 3.5 | 23.0% | 4.60 | +5.94% | 77.0% | 1.20 | -7.64% | Value Over |
| Sarmiento vs Barracas Central | 1.5 | 63.3% | 1.61 | +2.29% | 36.7% | 2.38 | -12.75% | Sin value |
| Sarmiento vs Barracas Central | 2.5 | 42.2% | 2.90 | +22.52% | 57.8% | 1.48 | -14.53% | Value Over |
| Sarmiento vs Barracas Central | 3.5 | 18.7% | 6.00 | +12.32% | 81.3% | 1.17 | -4.90% | Value Over |
| Deportivo Riestra vs Unión de Santa Fe | 1.5 | 62.6% | 1.60 | +0.46% | 37.4% | 2.40 | -10.22% | Sin value |
| Deportivo Riestra vs Unión de Santa Fe | 2.5 | 41.1% | 2.90 | +19.13% | 58.9% | 1.48 | -12.80% | Value Over |
| Deportivo Riestra vs Unión de Santa Fe | 3.5 | 17.8% | 6.00 | +6.62% | 82.2% | 1.17 | -3.79% | Value Over |
| Deportivo Pasto vs Alianza Valledupar FC | 1.5 | 53.7% | 1.40 | -24.76% | 46.3% | 3.25 | +50.34% | Value Under |
| Deportivo Pasto vs Alianza Valledupar FC | 2.5 | 28.8% | 2.20 | -36.64% | 71.2% | 1.73 | +22.96% | Value Under |
| Deportivo Pasto vs Alianza Valledupar FC | 3.5 | 9.2% | 4.20 | -61.19% | 90.8% | 1.27 | +15.27% | Value Under |
| Monza vs Cagliari | 1.5 | 83.3% | 1.37 | +14.07% | 16.7% | 3.40 | -43.08% | Value Over |
| Monza vs Cagliari | 2.5 | 75.6% | 2.13 | +61.17% | 24.4% | 1.83 | -55.38% | Value Over |
| Monza vs Cagliari | 3.5 | 59.4% | 3.70 | +119.85% | 40.6% | 1.33 | -46.03% | Value Over |
| Parma vs Torino | 1.5 | 76.9% | 1.48 | +13.83% | 23.1% | 3.00 | -30.73% | Value Over |
| Parma vs Torino | 2.5 | 64.6% | 2.49 | +60.71% | 35.4% | 1.63 | -42.30% | Value Over |
| Parma vs Torino | 3.5 | 43.2% | 4.60 | +98.86% | 56.8% | 1.23 | -30.17% | Value Over |

## Picks Recomendados (Top 6)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Getafe vs Rayo Vallecano | over_1_5 | Over 1.5 Goles | prioritario | 1.63 | 78.3% | 1.28 | +27.58% | +27.58% | +19.43% | 0.11u | Media-Alta |
| 2 | Deportivo Riestra vs Unión de Santa Fe | under_corners_9_5 | Under 9.5 Córners | prioritario | 1.53 | 76.1% | 1.31 | +16.62% | +16.62% | +8.96% | 0.08u | Media-Alta |
| 3 | Parma vs Torino | under_cards_3_5 | Under 3.5 Tarjetas | prioritario | 2.02 | 75.9% | 1.32 | +53.43% | +53.43% | +43.33% | 0.13u | Media-Alta |
| 4 | Monza vs Cagliari | over_2_5 | Over 2.5 Goles | prioritario | 2.13 | 75.6% | 1.32 | +61.17% | +61.17% | +50.51% | 0.14u | Media-Alta |
| 5 | Deportivo Pasto vs Alianza Valledupar FC | under_2_5 | Under 2.5 Goles | prioritario | 1.73 | 71.2% | 1.40 | +22.96% | +22.96% | +14.33% | 0.08u | Media-Alta |
| 6 | Deportivo Riestra vs Unión de Santa Fe | x2 | Doble Oportunidad Empate/Unión de Santa Fe | prioritario | 1.67 | 70.3% | 1.42 | +17.14% | +17.14% | +8.81% | 0.06u | Media-Alta |

## Detalle de Picks
### Pick 1: Getafe vs Rayo Vallecano
- **Mercado:** over_1_5
- **Selección:** Over 1.5 Goles
- **Cuota:** 1.63
- **Probabilidad modelo:** 78.3%
- **Probabilidad conservadora:** 73.3%
- **Probabilidad implícita:** 61.4%
- **Cuota justa:** 1.28
- **Edge:** +27.58%
- **EV:** +27.58%
- **EV robusto:** +19.43%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.28
- **Stake:** 0.11u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1746 vs 1700, brecha 46) | perfil xG 0.81/1.71 (local) vs 1.30/1.86 (visitante). El motor model-v1.3 estima 78.3% para 'Over 1.5 Goles' frente a una probabilidad implicita de 61.4% (cuota 1.63); edge +27.58% y EV robusto +19.43%.
- **Riesgos:** Cuotas no cotizadas: over_cards_3_5, under_cards_3_5; Muestras desiguales: Getafe n=8, Rayo n=7 (Rayo no ha jugado liga desde 19/09 - 30 dias; CAUSA DEL PARON NO VERIFICADA, la busqueda web no devolvio explicacion; riesgo de sesgo por antiguedad de la muestra de Rayo). corners/cards n=5 (statsbet 'Ultimos 5'). against derivado aritmeticamente: GET 10.0-3.4=6.6 corners, 5.6-3.6=2.0 cards; RAY 12.2-5.2=7.0 corners, 4.2-2.8=1.4 cards. CARDS 3.5 SIN COTIZAR: oddssafari solo publica lineas 4.5 y 5.5 para este partido (ambas con UNA sola casa -> mercado de tarjetas fino). DISCREPANCIAS >2% (reportadas, no reemplazadas): O2.5 oddssafari 2.85 vs 2.65 usado (+7.5%), U2.5 1.48 vs 1.38 (+7.2%); 1X2 oddssafari best 3.13/3.09/2.69 vs sportytrader 2.92/2.90/2.55 (+7.2%/+6.6%/+5.5%). Contexto (fuentes: sportytrader.es paginas de partido 18/10/2026; marca.com y sportytrader.es 19/10/2026): Getafe 15o y Rayo 14o, ambos 8 pts. Getafe con SOLO 4 dias de descanso: juega Conference League el 15/10 (1-1 en Craiova) y venia de 0-3 en Barcelona (10/10) -> fatiga verificada por calendario. Bajas Getafe: Juanmi, Chistantus Uche; dudas: Unal, Mangala, Azon, Romero; Carvajal podria debutar (inscrito en LaLiga, marca.com 19/10). Bajas Rayo: Batalla, Luiz Felipe; duda: Ratiu. H2H ultimos 6: 3 victorias Rayo, 3 empates, 0 de Getafe (Betfair blog 19/10/2026) -> dominio historico reciente visitante. Getafe solo 0.81 xG a favor por partido (el mas bajo de los 6 equipos de esta recoleccion).
- **Fuentes:** xG: understat.com/getLeagueData/La%20liga/2026 (n=8 Getafe, n=7 Rayo, medias de history; GET 0.81/1.71, RAY 1.30/1.86); Elo: clubelo.com/Ranking via web.archive.org/web/20261015030319 (snapshot 15/10/2026: GET 1700, RAY 1746); corners/cards: statsbet.es/futbol/equipos/getafe y /rayo-vallecano (ventana 'Ultimos 5', n=5, descargado 19/10/2026 08:19 UTC; against = Media total - Media equipo); cuotas 1X2/DC/DNB/BTTS/O-U 2.5: sportytrader.com/cotes/cf-getafe-rayo-vallecano-8586497 (maximo por columna, 19/10/2026); O-U 1.5/3.5, corners y cards 4.5/5.5: oddssafari.com/api/match?EventID=3458333 (maximo entre 11-15 casas, 19/10/2026); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 2: Deportivo Riestra vs Unión de Santa Fe
- **Mercado:** under_corners_9_5
- **Selección:** Under 9.5 Córners
- **Cuota:** 1.53
- **Probabilidad modelo:** 76.1%
- **Probabilidad conservadora:** 71.1%
- **Probabilidad implícita:** 65.2%
- **Cuota justa:** 1.31
- **Edge:** +16.62%
- **EV:** +16.62%
- **EV robusto:** +8.96%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.31
- **Stake:** 0.08u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1627 vs 1612, brecha 15) | perfil xG 0.79/0.86 (local) vs 1.41/1.12 (visitante). El motor model-v1.3 estima 76.1% para 'Under 9.5 Córners' frente a una probabilidad implicita de 65.2% (cuota 1.53); edge +16.62% y EV robusto +8.96%. Atencion: el input de este partido arrastra banderas de baja confianza (ver Riesgos); la incertidumbre real es mayor que la base del motor.
- **Riesgos:** Corners/tarjetas statsbet: en contra = Media total − Media equipo (RIE córners 6.0−2.6=3.4, tarjetas 5.0−2.6=2.4; UNI córners 8.6−3.8=4.8, tarjetas 6.8−3.4=3.4). xG statsbet con etiqueta directa for/against, sin derivar. BAJA CONFIANZA en los stats de Riestra: la cabecera de su página statsbet (2026-10-19) está enmarcada en Copa Sudamericana 2026 (posición 3 con 5 pts en 6 partidos), ventana ambigua. Cross-check Sofascore temporada n=28 (2026-10-19): Riestra xG 11.8891/28=0.42 por partido vs statsbet 0.79 (DISCREPANCIA), córners 103+115=218/28=7.8 vs Media total 6.0 (DISCREPANCIA), amarillas 90/60. statsbet alterna Últimos 5/10/Temporada(28) sin marca legible -> ventana de stats no exacta (riesgo). Posiciones (Sofascore, Grupo A act 2026-10-12): UNI 11° 13 pts/12PJ; RIE 12° 11 pts/12PJ. Descanso: RIE 8 dias (perdió 0-1 vs San Lorenzo el 10-11); UNI 10 dias (perdió 0-2 vs Defensa y Justicia el 10-10). Kickoff verificado (FotMob + oddssafari + sportytrader). Lesiones, suspensiones y cambios de entrenador: NO VERIFICADOS (consulta 2026-10-19; búsqueda web sin resultados; MCPs inoperativos). Cuotas: mejor cuota entre casas; tarjetas 5.5 sin cotizar (se omiten ambos lados); mercados de tarjetas con n=1 casa (Fonbet). Página statsbet no especifica si las tarjetas incluyen rojas. CORRELACION: este mismo partido aporta 2 picks al portfolio (junto a x2 (1.67)); son eventos correlacionados y elevan la varianza conjunta mas alla de la de picks de partidos independientes, por lo que el stake agregado del partido deberia leerse como una sola exposicion.
- **Fuentes:** xG/corners/cards: statsbet.es/futbol/equipos/deportivo-riestra y /unin-santa-fe (vía r.jina.ai, consulta 2026-10-19); cross-check estadísticas: sofascore.com temporada n=28; Elo: clubelo.com/Ranking (HTML, consulta 2026-10-19); posiciones y fixtures: sofascore.com (Grupo A, act 2026-10-12); cuotas: oddssafari.com/api/match EventID=5271091 MarketTypes 101/102/103/105/108/130/186, mejor cuota entre casas (consulta 2026-10-19); fixture: sportytrader.com/es/apuestas/deportivo-riestra-union-de-santa-fe-8689634; verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 3: Parma vs Torino
- **Mercado:** under_cards_3_5
- **Selección:** Under 3.5 Tarjetas
- **Cuota:** 2.02
- **Probabilidad modelo:** 75.9%
- **Probabilidad conservadora:** 71.0%
- **Probabilidad implícita:** 49.5%
- **Cuota justa:** 1.32
- **Edge:** +53.43%
- **EV:** +53.43%
- **EV robusto:** +43.33%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.32
- **Stake:** 0.13u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1685 vs 1643, brecha 42) | perfil xG 0.78/2.12 (local) vs 1.24/1.38 (visitante). El motor model-v1.3 estima 75.9% para 'Under 3.5 Tarjetas' frente a una probabilidad implicita de 49.5% (cuota 2.02); edge +53.43% y EV robusto +43.33%.
- **Riesgos:** VENTANA: n=6 partidos de liga por equipo (Serie A 26/27) en xG, corners y cards; se excluyen Copa y amistosos (la fuente de corners/cards reporta MP=6 de liga). Formas en orden cronologico (mas antiguo primero): Parma P-P-N-P-G-P, ultimo partido 10/10; Torino P-P-G-P-N-G, ultimo 12/10. Derivacion xG por partido: 4.67/6=0.78, 12.72/6=2.12, 7.45/6=1.24, 8.25/6=1.38. DISCREPANCIA >2% xG (se reporta, no se sustituye): performanceodds.com promedia Parma 0.92 xG a favor / 1.94 en contra y Torino 1.09 / 1.62; familia de modelo distinta a understat. DISCREPANCIA >2% doble oportunidad x2: oddssafari 1.39 vs sportytrader 1.36 (+2.2%). ANOMALIA DE CROSS-CHECK (se reporta, no se sustituye): el widget resumido de sportytrader muestra -2.5=2.16 y +2.5=2.49 para este partido, par imposible dentro de una misma casa (probabilidades implicitas suman 0.865); su tabla detallada muestra que el 2.16 de under va apareado con over 1.71 en esa misma linea de bookmaker y que las casas cotizan under entre 1.57 y 2.16 y over entre 1.71 y 2.49; se mantiene oddssafari (over 2.487 / under 1.631, ambas 1xBet), consistente con el extremo de la tabla de sportytrader. Lineas omitidas: amarillas 4.5 y 5.5 no cotizadas (oddssafari solo publica 2.5 y 3.5 en este evento) y por eso no aparecen sus claves; sportytrader no cotiza O/U de corners ni de tarjetas (solo 1X2 de corners y de bookings). Cards = campo 'Cards' de performanceodds (Cards Won/Against suman el Match Total Cards: Parma 1.33+1.67=3.00, Torino 0.67+1.17=1.84 vs 1.83 publicado por redondeo); el mercado cotizado por oddssafari es 'Yellow Cards' (MarketType 186) y NO se pudo verificar si el agregado de equipo de performanceodds incluye rojas. CLASIFICACION (BBC 19/10/2026 13:47 y understat, que coinciden): Parma 16o con 4 puntos en 6 PJ, Torino 13o con 7 puntos en 6 PJ; el PDF oficial de la Lega Serie A confirma 4 y 7 puntos respectivamente, mientras fuentes secundarias (bottadiculo.it, 19/10) dan Parma 17o y Torino 12o - se descartan por no coincidir con la tabla oficial/bbc. DESCANSO: Parma juego el 10/10 (9 dias), Torino el 12/10 (7 dias). ACTUALIDAD 19/10/2026 (bajas y sanciones): Parma sin Nesta Elphege (operacion de apendicitis, baja de 3-4 semanas), Hans Nicolussi Caviglia y Pontus Almqvist; si esta Abdoulaye Ndiaye (recuperado); sin sancionados. Fuente primaria: lista oficial de convocados publicada por el club y recogida por parmalive.com (19/10/2026 13:33); confirmacion en toro.it (19/10 05:59) y zonapronostici.it. Torino sin Niccolò Fortini e Emirhan Ilkhan (zonapronostici.it, cuoretoro.it 18/10); elofoot.com anade ademas dudas de Israel y Pellegri, NO CONFIRMADAS por una lista de convocados oficial -> no verificado. Arbitro: Giovanni Ayroldi (PDF oficial MATCH PROGRAM de Lega Serie A para Parma-Torino, arbitro designado). CONTEXTO: Parma llega tras perder 0-3 en Inter y suma solo 2 victorias en sus ultimos 10 partidos de liga (la ultima 20/09 vs Genoa); Torino viene de ganar 2-1 a Udinese y llevo 7 puntos en las ultimas 4 jornadas (legaseriea.it 19/10/2026, diretta.it 19/10/2026). H2H: 21 precedentes oficiales en Parma - 11 victorias del Parma (ultima 2-1, Serie A 25/26), 6 empates (ultimo 2-2, Serie A 24/25) y 4 del Torino (ultima 0-3, Serie A 20/21), segun el comunicado de Lega Serie A del 19/10/2026; ultimos 5 enfrentamientos de Serie A: Torino 4-1 Parma (13/03/2026), Parma 2-1 Torino (29/09/2025), Parma 2-2 Torino (08/03/2025), Torino 0-0 Parma (05/01/2025), Torino 1-0 Parma (03/05/2021); el Torino perdio solo 1 de los ultimos 7 H2H de Serie A (3V, 3N, 1P) y los ultimos 6 disputados en Parma estan equilibrados 2-2-2 (diretta.it 19/10/2026). NO VERIFICADO: alineaciones titulares definitivas (formaciones probables con variantes entre fuentes: Parma 3-5-2 con dudas en banda y centro, Torino 3-4-2-1 o 4-4-2); corners y cards no pudieron contrastarse con una fuente primaria porque Sofascore (www y api) devuelve 403 y FBref devuelve 403.
- **Fuentes:** xG: understat.com/league/Serie_A/2026 (vía r.jina.ai, pagina leída el 19/10/2026; totales de la ventana Serie A 26/27 con n=6 partidos por equipo: Parma 4.67 xG / 12.72 xGA, Torino 7.45 xG / 8.25 xGA; xG por partido = total/6, aritmética propia). Corners/cards: performanceodds.com/team_stats_overall/17084/476 (Parma) y performanceodds.com/team_stats_overall/17084/456 (Torino), filas 'Corners Won'/'Corners Conceded' y 'Cards Won (For)'/'Cards Against', MP=6 (promedio por partido ya calculado por la fuente). Elo: snapshot de web.archive.org sobre clubelo.com/Ranking del 2026-10-15T03:03:19Z (clubelo.com y api.clubelo.com no responden: timeout de conexion). Cuotas: API publica de oddssafari.com (www.oddssafari.com/api/match?EventID=3477916&MarketTypeID={101|102|103|105|108|130|186}&ScopeID=103), scope Full time, mejor cuota sobre 15 casas: 1X2 1=3.43 (1xBet), X=3.17 (1xBet), 2=2.45 (Betsson/Fonbet/Novibet/Bet365/Betano/Bwin/Interwetten/Unibet); doble oportunidad 1x=1.621 (1xBet), x2=1.39 (Betano), 12=1.407 (1xBet); DNB 1=2.20 (Bet365), 2=1.67 (Betano/Unibet); BTTS si=2.00 (Fonbet), no=1.86 (Novibet); lineas de goles 1.5/2.5/3.5 y de corners 8.5/9.5/10.5 = mejor cuota del agregado (la API no informa la casa en las lineas con parametro, salvo 2.5: 2.487/1.631 ambas de 1xBet); amarillas solo 2.5 y 3.5 (3.5: 1.70/2.02). Cross-check 1X2/DC/DNB/BTTS/O-U 2.5: sportytrader.com/en/odds/parma-torino (vía r.jina.ai). Ascenso/descenso: bbc.com/sport/football/live/c32l4ke1zly1t (19/10/2026 13:47), understat y el PDF oficial MATCH PROGRAM de Lega Serie A para la jornada 7 (Parma 4 puntos, Torino 7 puntos en 6 PJ).; verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 4: Monza vs Cagliari
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 2.13
- **Probabilidad modelo:** 75.6%
- **Probabilidad conservadora:** 70.6%
- **Probabilidad implícita:** 46.9%
- **Cuota justa:** 1.32
- **Edge:** +61.17%
- **EV:** +61.17%
- **EV robusto:** +50.51%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.32
- **Stake:** 0.14u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1678 vs 1636, brecha 42) | perfil xG 1.87/1.60 (local) vs 1.04/1.86 (visitante). El motor model-v1.3 estima 75.6% para 'Over 2.5 Goles' frente a una probabilidad implicita de 46.9% (cuota 2.13); edge +61.17% y EV robusto +50.51%.
- **Riesgos:** VENTANA: n=6 partidos de liga por equipo (Serie A 26/27) en xG, corners y cards; se excluyen Copa y amistosos (la fuente de corners/cards reporta MP=6 de liga). Formas en orden cronologico (mas antiguo primero): Monza P-P-N-P-G-P, ultimo partido 11/10; Cagliari G-P-G-G-G-N, ultimo 11/10. Derivacion xG por partido: 11.22/6=1.87, 9.62/6=1.60, 6.26/6=1.04, 11.15/6=1.86. DISCREPANCIA >2% xG (se reporta, no se sustituye): performanceodds.com promedia Monza 1.63 xG a favor / 1.45 en contra y Cagliari 1.06 / 2.11 en su propia ventana de 6 partidos; familia de modelo distinta a understat. DISCREPANCIA >2% BTTS: oddssafari 'no'=2.05 vs sportytrader 'no'=2.00 (+2.5%). DISCREPANCIA >2% corners: performanceodds da 9.34 corners totales/partido en los partidos de Monza y 10.5 en los de Cagliari, mientras totalcorner.com registra en los ultimos 4 de liga 13+12+10+9=44 (11.0) para Monza y 10+17+5+12=44 (11.0) para Cagliari; se conserva performanceodds por ser la unica fuente con ventana declarada y sin huecos. Lineas omitidas: amarillas 4.5 y 5.5 no cotizadas (oddssafari solo publica 2.5 y 3.5 en este evento) y por eso no aparecen sus claves; sportytrader no cotiza O/U de corners ni de tarjetas (solo 1X2 de corners y de bookings). Cards = campo 'Cards' de performanceodds (Cards Won/Against suman el Match Total Cards: Monza 2.00+1.67=3.67, Cagliari 1.17+1.17=2.33); el mercado cotizado por oddssafari es 'Yellow Cards' (MarketType 186) y NO se pudo verificar si el agregado de equipo de performanceodds incluye rojas. CLASIFICACION (BBC 19/10/2026 13:47 y understat): Cagliari 6o-7o con 13 puntos en 6 PJ (BBC 6o, understat 7o por diferencia de gol: discrepancia de criterio de desempate) y Monza 15o con 4 puntos en 6 PJ (ambas fuentes coinciden). DESCANSO: ambos jugaron el 11/10, 8 dias. ACTUALIDAD 19/10/2026 (bajas y sanciones): Monza sin Lorenzo Lucchesi (sancionado tras la expulsion ante Lazio del 11/10), fuera tambien Pessina, Ziolkowski y Toure (lesiones), Zeballos (rodilla operada, fuera o a evaluar) y Ciurria (duda). Fuentes: zonapronostici.it/formazioni/monza-cagliari-2026-10-19, gazzetta.it/calcio/prob_form/monza-cagliari/2638187, monza-news.it (18/10), ttnews24.it (19/10 08:44). Cagliari: su entrenador Fabio Pisacane SANCIONADO (1 jornada por el incidente con Spalletti en Cagliari-Juventus del 11/10; lo dirige su vice Giacomo Murelli) y sin Mattia Felici (LC), Riyad Idrissi (LC) y Yael Trepy; Deiola recuperado y disponible. Fuentes: unionesarda.it (19/10 09:52), ttnews24.it (19/10 08:44), zonapronostici.it. Arbitro: Andrea Calzavara (seccion de Varese) segun unionesarda.it (19/10) y tuttomercatoweb (16/10). CONTEXTO: Cagliari invicto en 4 jornadas (3V+1N) y va 3 de 3 en salidas, buscando la cuarta victoria consecutiva fuera (unionesarda, 19/10); Monza 15o con 4 puntos y viene de perder 3-1 en Lazio. H2H (Serie A): los ultimos 4 cruces son 1-1-2 a favor de Cagliari - Cagliari 3-0 Monza (30/03/2025), Monza 1-2 Cagliari (05/01/2025), Monza 1-0 Cagliari (16/03/2024), Cagliari 1-1 Monza (26/11/2023); Cagliari gano los 2 ultimos (fantacalcio.it 18/10/2026, bbc.com 19/10 y totalcorner.com). Historico total (Serie A+B+Copa): 22 enfrentamientos, 9 victorias del Monza, 6 empates, 7 del Cagliari (monza-news.it 15/10/2026). NO VERIFICADO: alineaciones titulares definitivas (se publican aproximadamente 1 hora antes del kickoff); corners y cards no pudieron contrastarse con una fuente primaria porque Sofascore (www y api) devuelve 403 y FBref devuelve 403.
- **Fuentes:** xG: understat.com/league/Serie_A/2026 (vía r.jina.ai, pagina leída el 19/10/2026; totales de la ventana Serie A 26/27 con n=6 partidos por equipo: Monza 11.22 xG / 9.62 xGA, Cagliari 6.26 xG / 11.15 xGA; xG por partido = total/6, aritmética propia). Corners/cards: performanceodds.com/team_stats_overall/17084/2356 (Monza) y performanceodds.com/team_stats_overall/17084/455 (Cagliari), filas 'Corners Won'/'Corners Conceded' y 'Cards Won (For)'/'Cards Against', MP=6 (promedio por partido ya calculado por la fuente). Elo: snapshot de web.archive.org sobre clubelo.com/Ranking del 2026-10-15T03:03:19Z (clubelo.com y api.clubelo.com no responden: timeout de conexion). Cuotas: API publica de oddssafari.com (www.oddssafari.com/api/match?EventID=3478380&MarketTypeID={101|102|103|105|108|130|186}&ScopeID=103), scope Full time, mejor cuota sobre 15 casas: 1X2 1=2.447 (1xBet), X=3.30 (Bwin), 2=3.295 (1xBet); doble oportunidad 1x=1.384 (1xBet), x2=1.65 (Betano), 12=1.384 (1xBet); DNB 1=1.65 (10bet), 2=2.25 (Betway); BTTS si=1.80 (888Sport/William Hill/Bet365), no=2.05 (Unibet); lineas de goles 1.5/2.5/3.5 y de corners 8.5/9.5/10.5 = mejor cuota del agregado (la API no informa la casa en las lineas con parametro, salvo 2.5: 2.131/1.831 ambas de 1xBet); amarillas solo 2.5 y 3.5 (3.5: 1.85/1.85). Cross-check 1X2/DC/DNB/BTTS/O-U 2.5: sportytrader.com/en/odds/monza-cagliari-8522158 (vía r.jina.ai). Ascenso/descenso y stats de partido: bbc.com/sport/football/live/c32l4ke1zly1t (19/10/2026 13:47) y understat.; verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 5: Deportivo Pasto vs Alianza Valledupar FC
- **Mercado:** under_2_5
- **Selección:** Under 2.5 Goles
- **Cuota:** 1.73
- **Probabilidad modelo:** 71.2%
- **Probabilidad conservadora:** 66.2%
- **Probabilidad implícita:** 57.9%
- **Cuota justa:** 1.40
- **Edge:** +22.96%
- **EV:** +22.96%
- **EV robusto:** +14.33%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.40
- **Stake:** 0.08u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** perfil xG 0.81/0.69 (local) vs 1.00/1.05 (visitante). El motor model-v1.3 estima 71.2% para 'Under 2.5 Goles' frente a una probabilidad implicita de 57.9% (cuota 1.73); edge +22.96% y EV robusto +14.33%.
- **Riesgos:** Cuotas no cotizadas: over_cards_3_5, under_cards_3_5; Tasas sin publicar: elo_away; Estadísticas colombianas de Sofascore: promedio por partido de los últimos 5 partidos del Finalización (n=5 por equipo, orientación home/away verificada en el evento 16390731), valores directos for/against sin derivación. Pasto: xG 0.81/0.69, córners 4.0/2.0, tarjetas 4.0/3.2 (amarrillas 3.4/2.6 + rojas 0.6/0.6). Alianza: xG 1.00/1.05, córners 5.0/6.2, tarjetas 4.0/3.4 (amarrillas 3.8/3.2 + rojas 0.2/0.2). Tarjetas = amarrillas+rojas (n=5). Elo: Alianza Valledupar FC no está en clubelo -> elo_away null; NO usar 'Alianza Petrolera' (1510) ni 'Santa Fe' (1661): son clubes distintos. Posiciones (Sofascore, act 2026-10-19): Pasto 20° 9 pts/12PJ (2V-7D-3E); Alianza Valledupar 15° 12 pts/13PJ (3V-7D-3E). Descanso: Pasto ~15 dias (último partido 10-04, 0-0 vs Fortaleza; Atl. Nacional-Pasto del 11-10 POSTPONED); Alianza ~10 dias (empató 2-2 vs Rionegro el 10-09). H2H: 0-0, 2026-04-01 (Apertura, único cruce esta temporada); forma últimos 5: Pasto 2V-2E-1D, Alianza 2V-1E-2D. Kickoff verificado (FotMob + oddssafari; sportytrader UTC-4 20:15 consistente). Lesiones, suspensiones y cambios de entrenador: NO VERIFICADOS (consulta 2026-10-19; búsqueda web sin resultados; MCPs inoperativos). Cuotas: mejor cuota entre casas; tarjetas 3.5 sin cotizar (se omiten ambos lados); mercados de tarjetas con n=1 casa (Fonbet).
- **Fuentes:** xG/corners/cards: Sofascore API por evento (promedio de los últimos 5 partidos del Finalización; eventos Pasto 16390731,16390740,16390747,16390758,16390772 y Alianza 16736576,16390748,16390763,16390767,16390786, orientación home/away verificada en evento 16390731, consulta 2026-10-19; statsbet sin páginas colombianas); Elo: clubelo.com/Ranking (HTML, consulta 2026-10-19); posiciones, fixtures y H2H: sofascore.com (act 2026-10-19); cuotas: oddssafari.com/api/match EventID=5685706 MarketTypes 101/102/103/105/108/130/186, mejor cuota entre casas (consulta 2026-10-19); verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 6: Deportivo Riestra vs Unión de Santa Fe
- **Mercado:** x2
- **Selección:** Doble Oportunidad Empate/Unión de Santa Fe
- **Cuota:** 1.67
- **Probabilidad modelo:** 70.3%
- **Probabilidad conservadora:** 65.3%
- **Probabilidad implícita:** 60.0%
- **Cuota justa:** 1.42
- **Edge:** +17.14%
- **EV:** +17.14%
- **EV robusto:** +8.81%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.42
- **Stake:** 0.06u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1627 vs 1612, brecha 15) | perfil xG 0.79/0.86 (local) vs 1.41/1.12 (visitante). El motor model-v1.3 estima 70.3% para 'Doble Oportunidad Empate/Unión de Santa Fe' frente a una probabilidad implicita de 60.0% (cuota 1.67); edge +17.14% y EV robusto +8.81%. Atencion: el input de este partido arrastra banderas de baja confianza (ver Riesgos); la incertidumbre real es mayor que la base del motor.
- **Riesgos:** Corners/tarjetas statsbet: en contra = Media total − Media equipo (RIE córners 6.0−2.6=3.4, tarjetas 5.0−2.6=2.4; UNI córners 8.6−3.8=4.8, tarjetas 6.8−3.4=3.4). xG statsbet con etiqueta directa for/against, sin derivar. BAJA CONFIANZA en los stats de Riestra: la cabecera de su página statsbet (2026-10-19) está enmarcada en Copa Sudamericana 2026 (posición 3 con 5 pts en 6 partidos), ventana ambigua. Cross-check Sofascore temporada n=28 (2026-10-19): Riestra xG 11.8891/28=0.42 por partido vs statsbet 0.79 (DISCREPANCIA), córners 103+115=218/28=7.8 vs Media total 6.0 (DISCREPANCIA), amarillas 90/60. statsbet alterna Últimos 5/10/Temporada(28) sin marca legible -> ventana de stats no exacta (riesgo). Posiciones (Sofascore, Grupo A act 2026-10-12): UNI 11° 13 pts/12PJ; RIE 12° 11 pts/12PJ. Descanso: RIE 8 dias (perdió 0-1 vs San Lorenzo el 10-11); UNI 10 dias (perdió 0-2 vs Defensa y Justicia el 10-10). Kickoff verificado (FotMob + oddssafari + sportytrader). Lesiones, suspensiones y cambios de entrenador: NO VERIFICADOS (consulta 2026-10-19; búsqueda web sin resultados; MCPs inoperativos). Cuotas: mejor cuota entre casas; tarjetas 5.5 sin cotizar (se omiten ambos lados); mercados de tarjetas con n=1 casa (Fonbet). Página statsbet no especifica si las tarjetas incluyen rojas. CORRELACION: este mismo partido aporta 2 picks al portfolio (junto a under_corners_9_5 (1.53)); son eventos correlacionados y elevan la varianza conjunta mas alla de la de picks de partidos independientes, por lo que el stake agregado del partido deberia leerse como una sola exposicion.
- **Fuentes:** xG/corners/cards: statsbet.es/futbol/equipos/deportivo-riestra y /unin-santa-fe (vía r.jina.ai, consulta 2026-10-19); cross-check estadísticas: sofascore.com temporada n=28; Elo: clubelo.com/Ranking (HTML, consulta 2026-10-19); posiciones y fixtures: sofascore.com (Grupo A, act 2026-10-12); cuotas: oddssafari.com/api/match EventID=5271091 MarketTypes 101/102/103/105/108/130/186, mejor cuota entre casas (consulta 2026-10-19); fixture: sportytrader.com/es/apuestas/deportivo-riestra-union-de-santa-fe-8689634; verosimilitud del modelo y calibracion Platt (model-v1.3).

## NO BET / Excluidos
- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**
  - Tottenham vs Coventry City — Over 1.5 Goles (over_1_5): Prob modelo 80.0%, EV -4.81%, EV robusto -10.76% → sin value.
  - Tottenham vs Coventry City — Under 1.5 Goles (under_1_5): Prob modelo 20.0%, EV +0.05%, EV robusto -24.95% → sin value.
  - Tottenham vs Coventry City — Under 2.5 Goles (under_2_5): Prob modelo 30.0%, EV -30.91%, EV robusto -42.41% → sin value.
  - Tottenham vs Coventry City — Under 3.5 Goles (under_3_5): Prob modelo 49.2%, EV -22.69%, EV robusto -30.54% → sin value.
  - Tottenham vs Coventry City — Over 8.5 Córners (over_corners_8_5): Prob modelo 60.2%, EV -17.57%, EV robusto -24.42% → sin value.
  - Tottenham vs Coventry City — Over 9.5 Córners (over_corners_9_5): Prob modelo 50.5%, EV -18.66%, EV robusto -26.71% → sin value.
  - Tottenham vs Coventry City — Over 10.5 Córners (over_corners_10_5): Prob modelo 41.3%, EV -16.97%, EV robusto -27.02% → sin value.
  - Tottenham vs Coventry City — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 45.8%, EV -2.47%, EV robusto -13.12% → sin value.
  - Tottenham vs Coventry City — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 54.2%, EV -11.64%, EV robusto -19.79% → sin value.
  - Getafe vs Rayo Vallecano — Under 1.5 Goles (under_1_5): Prob modelo 21.7%, EV -45.67%, EV robusto -58.17% → sin value.
  - Getafe vs Rayo Vallecano — Under 2.5 Goles (under_2_5): Prob modelo 33.1%, EV -54.39%, EV robusto -61.29% → sin value.
  - Getafe vs Rayo Vallecano — Under 3.5 Goles (under_3_5): Prob modelo 53.6%, EV -37.33%, EV robusto -43.18% → sin value.
  - Getafe vs Rayo Vallecano — Under 8.5 Córners (under_corners_8_5): Prob modelo 31.1%, EV -25.36%, EV robusto -37.36% → sin value.
  - Getafe vs Rayo Vallecano — Under 9.5 Córners (under_corners_9_5): Prob modelo 40.0%, EV -26.07%, EV robusto -35.32% → sin value.
  - Getafe vs Rayo Vallecano — Under 10.5 Córners (under_corners_10_5): Prob modelo 48.9%, EV -26.16%, EV robusto -33.71% → sin value.
  - Getafe vs Rayo Vallecano — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 50.0%, EV -30.05%, EV robusto -37.05% → sin value.
  - Getafe vs Rayo Vallecano — Over 5.5 Tarjetas (over_cards_5_5): Prob modelo 36.6%, EV -34.05%, EV robusto -43.05% → sin value.
  - SC Braga vs Gil Vicente — Over 1.5 Goles (over_1_5): Prob modelo 72.0%, EV -3.49%, EV robusto -10.19% → sin value.
  - SC Braga vs Gil Vicente — Under 1.5 Goles (under_1_5): Prob modelo 28.0%, EV -2.07%, EV robusto -19.57% → sin value.
  - SC Braga vs Gil Vicente — Under 2.5 Goles (under_2_5): Prob modelo 43.7%, EV -23.47%, EV robusto -32.22% → sin value.
  - SC Braga vs Gil Vicente — Under 3.5 Goles (under_3_5): Prob modelo 67.3%, EV -10.54%, EV robusto -17.19% → sin value.
  - SC Braga vs Gil Vicente — Over 8.5 Córners (over_corners_8_5): Prob modelo 49.8%, EV -12.77%, EV robusto -21.52% → sin value.
  - SC Braga vs Gil Vicente — Over 9.5 Córners (over_corners_9_5): Prob modelo 39.9%, EV -8.19%, EV robusto -19.69% → sin value.
  - SC Braga vs Gil Vicente — Over 10.5 Córners (over_corners_10_5): Prob modelo 31.0%, EV -3.77%, EV robusto -19.27% → sin value.
  - SC Braga vs Gil Vicente — Under 10.5 Córners (under_corners_10_5): Prob modelo 69.0%, EV -0.01%, EV robusto -7.26% → sin value.
  - SC Braga vs Gil Vicente — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 52.3%, EV -24.16%, EV robusto -31.41% → sin value.
  - SC Braga vs Gil Vicente — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 36.8%, EV -22.76%, EV robusto -33.26% → sin value.
  - SC Braga vs Gil Vicente — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 63.2%, EV +4.31%, EV robusto -3.94% → sin value.
  - Newell's Old Boys vs Central Córdoba — Over 1.5 Goles (over_1_5): Prob modelo 66.4%, EV -0.41%, EV robusto -7.92% → sin value.
  - Newell's Old Boys vs Central Córdoba — Under 1.5 Goles (under_1_5): Prob modelo 33.6%, EV -7.57%, EV robusto -21.32% → sin value.
  - Newell's Old Boys vs Central Córdoba — Under 2.5 Goles (under_2_5): Prob modelo 53.0%, EV -16.78%, EV robusto -24.64% → sin value.
  - Newell's Old Boys vs Central Córdoba — Under 3.5 Goles (under_3_5): Prob modelo 77.0%, EV -7.64%, EV robusto -13.64% → sin value.
  - Newell's Old Boys vs Central Córdoba — Over 8.5 Córners (over_corners_8_5): Prob modelo 52.8%, EV -4.42%, EV robusto -13.47% → sin value.
  - Newell's Old Boys vs Central Córdoba — Under 8.5 Córners (under_corners_8_5): Prob modelo 47.2%, EV -1.84%, EV robusto -12.24% → sin value.
  - Newell's Old Boys vs Central Córdoba — Over 9.5 Córners (over_corners_9_5): Prob modelo 42.9%, EV +1.86%, EV robusto -10.01% → sin value.
  - Newell's Old Boys vs Central Córdoba — Under 9.5 Córners (under_corners_9_5): Prob modelo 57.1%, EV -5.77%, EV robusto -14.02% → sin value.
  - Newell's Old Boys vs Central Córdoba — Under 10.5 Córners (under_corners_10_5): Prob modelo 66.1%, EV -9.38%, EV robusto -16.23% → sin value.
  - Newell's Old Boys vs Central Córdoba — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 56.8%, EV -24.48%, EV robusto -31.13% → sin value.
  - Newell's Old Boys vs Central Córdoba — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 41.4%, EV -25.54%, EV robusto -34.54% → sin value.
  - Sarmiento vs Barracas Central — Over 1.5 Goles (over_1_5): Prob modelo 63.3%, EV +2.29%, EV robusto -5.78% → sin value.
  - Sarmiento vs Barracas Central — Under 1.5 Goles (under_1_5): Prob modelo 36.7%, EV -12.75%, EV robusto -24.65% → sin value.
  - Sarmiento vs Barracas Central — Under 2.5 Goles (under_2_5): Prob modelo 57.8%, EV -14.53%, EV robusto -21.93% → sin value.
  - Sarmiento vs Barracas Central — Under 3.5 Goles (under_3_5): Prob modelo 81.3%, EV -4.90%, EV robusto -10.75% → sin value.
  - Sarmiento vs Barracas Central — Under 8.5 Córners (under_corners_8_5): Prob modelo 39.8%, EV -25.52%, EV robusto -34.87% → sin value.
  - Sarmiento vs Barracas Central — Under 9.5 Córners (under_corners_9_5): Prob modelo 49.5%, EV -23.31%, EV robusto -31.06% → sin value.
  - Sarmiento vs Barracas Central — Under 10.5 Córners (under_corners_10_5): Prob modelo 58.7%, EV -23.70%, EV robusto -30.20% → sin value.
  - Sarmiento vs Barracas Central — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 50.0%, EV -26.55%, EV robusto -33.90% → sin value.
  - Sarmiento vs Barracas Central — Over 5.5 Tarjetas (over_cards_5_5): Prob modelo 36.6%, EV -28.56%, EV robusto -38.31% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Over 1.5 Goles (over_1_5): Prob modelo 62.6%, EV +0.46%, EV robusto -7.57% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Under 1.5 Goles (under_1_5): Prob modelo 37.4%, EV -10.22%, EV robusto -22.22% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Under 2.5 Goles (under_2_5): Prob modelo 58.9%, EV -12.80%, EV robusto -20.20% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Under 3.5 Goles (under_3_5): Prob modelo 82.2%, EV -3.79%, EV robusto -9.64% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Over 8.5 Córners (over_corners_8_5): Prob modelo 32.8%, EV -35.37%, EV robusto -45.22% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Over 9.5 Córners (over_corners_9_5): Prob modelo 23.9%, EV -36.60%, EV robusto -49.85% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Over 10.5 Córners (over_corners_10_5): Prob modelo 16.9%, EV -37.59%, EV robusto -56.09% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 74.9%, EV -4.84%, EV robusto -11.19% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 25.1%, EV -18.53%, EV robusto -34.78% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 62.2%, EV +4.50%, EV robusto -3.90% → sin value.
  - Deportivo Riestra vs Unión de Santa Fe — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 37.8%, EV -22.51%, EV robusto -32.76% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Over 1.5 Goles (over_1_5): Prob modelo 53.7%, EV -24.76%, EV robusto -31.76% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Over 2.5 Goles (over_2_5): Prob modelo 28.8%, EV -36.64%, EV robusto -47.64% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Over 3.5 Goles (over_3_5): Prob modelo 9.2%, EV -61.19%, EV robusto -82.19% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Over 8.5 Córners (over_corners_8_5): Prob modelo 46.8%, EV -8.76%, EV robusto -18.51% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Under 8.5 Córners (under_corners_8_5): Prob modelo 53.2%, EV +3.76%, EV robusto -5.99% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Over 9.5 Córners (over_corners_9_5): Prob modelo 36.9%, EV -4.03%, EV robusto -17.03% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Under 9.5 Córners (under_corners_9_5): Prob modelo 63.1%, EV +0.94%, EV robusto -7.06% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Over 10.5 Córners (over_corners_10_5): Prob modelo 28.2%, EV +3.11%, EV robusto -15.14% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Under 10.5 Córners (under_corners_10_5): Prob modelo 71.8%, EV -1.70%, EV robusto -8.55% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 74.9%, EV -2.66%, EV robusto -9.16% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 25.1%, EV -24.62%, EV robusto -39.62% → sin value.
  - Deportivo Pasto vs Alianza Valledupar FC — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 35.9%, EV -24.58%, EV robusto -35.08% → sin value.
  - Monza vs Cagliari — Under 1.5 Goles (under_1_5): Prob modelo 16.7%, EV -43.08%, EV robusto -60.08% → sin value.
  - Monza vs Cagliari — Under 2.5 Goles (under_2_5): Prob modelo 24.4%, EV -55.38%, EV robusto -64.53% → sin value.
  - Monza vs Cagliari — Under 3.5 Goles (under_3_5): Prob modelo 40.6%, EV -46.03%, EV robusto -52.68% → sin value.
  - Monza vs Cagliari — Over 8.5 Córners (over_corners_8_5): Prob modelo 59.5%, EV -3.66%, EV robusto -11.76% → sin value.
  - Monza vs Cagliari — Under 8.5 Córners (under_corners_8_5): Prob modelo 40.5%, EV -6.78%, EV robusto -18.28% → sin value.
  - Monza vs Cagliari — Over 9.5 Córners (over_corners_9_5): Prob modelo 49.8%, EV -0.44%, EV robusto -10.44% → sin value.
  - Monza vs Cagliari — Under 9.5 Córners (under_corners_9_5): Prob modelo 50.2%, EV -10.61%, EV robusto -19.51% → sin value.
  - Monza vs Cagliari — Under 10.5 Córners (under_corners_10_5): Prob modelo 59.4%, EV -12.05%, EV robusto -19.45% → sin value.
  - Monza vs Cagliari — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 35.1%, EV -35.01%, EV robusto -44.26% → sin value.
  - Parma vs Torino — Under 1.5 Goles (under_1_5): Prob modelo 23.1%, EV -30.73%, EV robusto -45.73% → sin value.
  - Parma vs Torino — Under 2.5 Goles (under_2_5): Prob modelo 35.4%, EV -42.30%, EV robusto -50.45% → sin value.
  - Parma vs Torino — Under 3.5 Goles (under_3_5): Prob modelo 56.8%, EV -30.17%, EV robusto -36.32% → sin value.
  - Parma vs Torino — Over 8.5 Córners (over_corners_8_5): Prob modelo 40.4%, EV -24.78%, EV robusto -34.08% → sin value.
  - Parma vs Torino — Over 9.5 Córners (over_corners_9_5): Prob modelo 30.9%, EV -24.40%, EV robusto -36.65% → sin value.
  - Parma vs Torino — Over 10.5 Córners (over_corners_10_5): Prob modelo 22.8%, EV -22.46%, EV robusto -39.46% → sin value.
  - Parma vs Torino — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 24.1%, EV -59.12%, EV robusto -67.62% → sin value.
- **Candidatos con value excluidos por probabilidad-primero:**
  - Tottenham vs Coventry City: Empate (X) EV +10.88% / EV rob -11.62%, Victoria Coventry City (2) EV +61.68% / EV rob +34.68%, Doble Oportunidad Empate/Coventry City (x2) EV +29.88% / EV rob +17.98%, DNB Coventry City (dnb_away) EV +42.90% / EV rob +23.15%, Over 2.5 Goles (over_2_5) EV +7.04% / EV rob -0.61%, Over 3.5 Goles (over_3_5) EV +27.92% / EV rob +15.32%, Under 9.5 Córners (under_corners_9_5) EV +13.80% / EV rob +2.30%, Under 10.5 Córners (under_corners_10_5) EV +5.64% / EV rob -3.36%, Under 8.5 Córners (under_corners_8_5) EV +27.45% / EV rob +11.45% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Getafe vs Rayo Vallecano: Victoria Rayo Vallecano (2) EV +10.19% / EV rob -2.56%, Over 2.5 Goles (over_2_5) EV +77.42% / EV rob +64.17%, Over 8.5 Córners (over_corners_8_5) EV +11.62% / EV rob +3.52%, Over 10.5 Córners (over_corners_10_5) EV +30.30% / EV rob +17.55%, Under 4.5 Tarjetas (under_cards_4_5) EV +37.60% / EV rob +23.85%, Over 3.5 Goles (over_3_5) EV +178.64% / EV rob +148.64% — No cumple los mínimos de selección probabilidad-primero.
  - SC Braga vs Gil Vicente: Empate (X) EV +5.90% / EV rob -13.85%, Victoria Gil Vicente (2) EV +71.94% / EV rob +40.69%, Doble Oportunidad Empate/Gil Vicente (x2) EV +34.71% / EV rob +22.31%, DNB Gil Vicente (dnb_away) EV +56.11% / EV rob +32.61%, Over 2.5 Goles (over_2_5) EV +4.10% / EV rob -5.15%, Over 3.5 Goles (over_3_5) EV +14.59% / EV rob -2.91%, Under 8.5 Córners (under_corners_8_5) EV +10.34% / EV rob -0.66%, Under 9.5 Córners (under_corners_9_5) EV +5.14% / EV rob -3.61%, Under 3.5 Tarjetas (under_cards_3_5) EV +16.86% / EV rob +4.61% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Newell's Old Boys vs Central Córdoba: Victoria Central Córdoba (2) EV +39.75% / EV rob +13.51%, Doble Oportunidad Empate/Central Córdoba (x2) EV +8.85% / EV rob -0.90%, DNB Central Córdoba (dnb_away) EV +22.37% / EV rob +4.87%, Over 2.5 Goles (over_2_5) EV +13.81% / EV rob +1.71%, Over 3.5 Goles (over_3_5) EV +5.94% / EV rob -17.06%, Over 10.5 Córners (over_corners_10_5) EV +10.01% / EV rob -6.24%, Under 3.5 Tarjetas (under_cards_3_5) EV +27.50% / EV rob +12.75%, Under 4.5 Tarjetas (under_cards_4_5) EV +11.41% / EV rob +1.91% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Sarmiento vs Barracas Central: Victoria Barracas Central (2) EV +19.40% / EV rob +0.90%, Doble Oportunidad Empate/Barracas Central (x2) EV +2.03% / EV rob -6.07%, DNB Barracas Central (dnb_away) EV +8.16% / EV rob -3.84%, Over 2.5 Goles (over_2_5) EV +22.52% / EV rob +8.02%, Over 3.5 Goles (over_3_5) EV +12.32% / EV rob -17.68%, Over 9.5 Córners (over_corners_9_5) EV +32.62% / EV rob +19.49%, Under 4.5 Tarjetas (under_cards_4_5) EV +22.58% / EV rob +10.33%, Under 5.5 Tarjetas (under_cards_5_5) EV +10.88% / EV rob +2.13%, Over 10.5 Córners (over_corners_10_5) EV +52.85% / EV rob +34.35% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Deportivo Riestra vs Unión de Santa Fe: DNB Unión de Santa Fe (dnb_away) EV +29.49% / EV rob +16.99%, Over 2.5 Goles (over_2_5) EV +19.13% / EV rob +4.63%, Over 3.5 Goles (over_3_5) EV +6.62% / EV rob -23.38%, Under 10.5 Córners (under_corners_10_5) EV +8.07% / EV rob +1.57%, Victoria Unión de Santa Fe (2) EV +53.93% / EV rob +34.43% — No cumple los mínimos de selección probabilidad-primero.
  - Deportivo Pasto vs Alianza Valledupar FC: Empate (X) EV +19.24% / EV rob +1.49%, Victoria Alianza Valledupar FC (2) EV +39.39% / EV rob +13.14%, DNB Alianza Valledupar FC (dnb_away) EV +33.15% / EV rob +14.40%, Under 3.5 Goles (under_3_5) EV +15.27% / EV rob +8.92%, Over 5.5 Tarjetas (over_cards_5_5) EV +5.74% / EV rob -2.51%, Under 1.5 Goles (under_1_5) EV +50.34% / EV rob +34.10% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Monza vs Cagliari: Victoria Monza (1) EV +25.31% / EV rob +13.08%, Doble Oportunidad Monza/Empate (1x) EV +3.45% / EV rob -3.47%, Doble Oportunidad Monza/Cagliari (12) EV +5.81% / EV rob -1.11%, DNB Monza (dnb_home) EV +8.05% / EV rob -0.20%, Ambos marcan (BTTS) (btts_yes) EV +9.40% / EV rob +0.40%, Over 1.5 Goles (over_1_5) EV +14.07% / EV rob +7.22%, Over 10.5 Córners (over_corners_10_5) EV +7.52% / EV rob -5.73%, Over 3.5 Goles (over_3_5) EV +119.85% / EV rob +101.35% — No cumple los mínimos de selección probabilidad-primero.
  - Parma vs Torino: Victoria Torino (2) EV +33.72% / EV rob +21.47%, Doble Oportunidad Empate/Torino (x2) EV +10.84% / EV rob +3.89%, Doble Oportunidad Parma/Torino (12) EV +5.30% / EV rob -1.74%, DNB Torino (dnb_away) EV +16.31% / EV rob +7.96%, Ambos marcan (BTTS) (btts_yes) EV +11.90% / EV rob +1.90%, Over 1.5 Goles (over_1_5) EV +13.83% / EV rob +6.43%, Over 2.5 Goles (over_2_5) EV +60.71% / EV rob +48.27%, Under 9.5 Córners (under_corners_9_5) EV +12.01% / EV rob +3.91%, Under 10.5 Córners (under_corners_10_5) EV +5.76% / EV rob -1.09%, Over 3.5 Goles (over_3_5) EV +98.86% / EV rob +75.86% — No cumple los mínimos de selección probabilidad-primero.

## Portfolio y Correlaciones
- **Exposición total:** 0.60u
- **Correlaciones detectadas:** Mercados presentes: over_1_5, over_2_5, under_2_5, under_cards_3_5, under_corners_9_5, x2. Verificar solapamiento de mercado mismo partido.

- **Ajuste de stake por correlación:** Hay picks del mismo partido (Deportivo Riestra vs Unión de Santa Fe (2 picks: under_corners_9_5, x2)); son eventos correlacionados y su exposición agregada debe leerse como una sola posición. El detalle de cada pick documenta la correlación en su sección de riesgos.

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1 (Getafe vs Rayo Vallecano - over_1_5) | PENDIENTE | — | — |
| Pick 2 (Deportivo Riestra vs Unión de Santa Fe - under_corners_9_5) | PENDIENTE | — | — |
| Pick 3 (Parma vs Torino - under_cards_3_5) | PENDIENTE | — | — |
| Pick 4 (Monza vs Cagliari - over_2_5) | PENDIENTE | — | — |
| Pick 5 (Deportivo Pasto vs Alianza Valledupar FC - under_2_5) | PENDIENTE | — | — |
| Pick 6 (Deportivo Riestra vs Unión de Santa Fe - x2) | PENDIENTE | — | — |
