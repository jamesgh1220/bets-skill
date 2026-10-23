# Análisis de Apuestas — 16 de octubre de 2026

## Metadatos
- **Fecha de análisis:** 2026-10-16T13:35:15Z
- **Fecha(s) de partido:** 16 de octubre de 2026
- **Information cutoff:** 2026-10-16T13:35:15Z
- **Modelo de IA:** bigpickle
- **Versión del motor predictivo:** model-v1.3
- **Ligas analizadas:** Bundesliga (J6), LaLiga (J9), Serie A (J7), Ligue 1 (J7), Eredivisie (J9) y Liga Profesional Argentina (Clausura, F13)
- **Rango de fechas solicitado:** 16 de octubre de 2026 - Bundesliga, Liga Argentina, Liga Espanola (LaLiga), Ligue 1, Serie A y Eredivisie (todos los partidos)
- **Partidos en universo:** 7
- **Picks iniciales con value:** 59
- **Picks finales seleccionados:** 6

## Universo Analizado
Universo = interseccion(ligas: Bundesliga, LaLiga, Serie A, Ligue 1, Eredivisie y Liga Profesional Argentina, fecha 16 de octubre de 2026, todos los partidos programados). Cutoff de informacion 2026-10-16T13:35:15Z, anterior al primer kickoff (18:00 UTC, Heerenveen vs Excelsior). No se usa informacion posterior a ningun kickoff. Universo final = 7 partidos, todos con los 4 valores de xG verificables y con los 8 campos obligatorios de corners/tarjetas (for/against por equipo) cargados antes de ejecutar el motor: Bundesliga J6 Eintracht Frankfurt vs FC Cologne (18:30 UTC); Ligue 1 J7 Le Mans vs Toulouse (18:45 UTC); Serie A J7 Frosinone vs Sassuolo (18:45 UTC); Eredivisie J9 Heerenveen vs Excelsior (18:00 UTC); LaLiga J9 Deportivo La Coruna vs Levante (19:00 UTC); Liga Profesional Argentina Clausura F13 Defensa y Justicia vs Instituto (22:00 UTC del 16/10) y Boca Juniors vs Talleres (00:30 UTC del 17/10 = 21:30 ART del 16/10, por lo que su fecha local cae dentro del rango solicitado). Se verifico que no hubiera otros partidos de esas 6 ligas en la fecha: la Bundesliga solo programa el viernes 1 partido (Frankfurt-Koln), LaLiga 1 (Depor-Levante), Serie A 1 (Frosinone-Sassuolo), Ligue 1 1 (Le Mans-Toulouse), Eredivisie 1 (Heerenveen-Excelsior); la Liga Profesional Argentina programa 2 el 16/10 (DyJ-Instituto y Boca-Talleres). MCPs inoperativos en esta sesion (football-stats, odds-api y apifootball), por lo que toda la recoleccion se hizo via web del agente: understat.com (xG), Sofascore public API y performanceodds.com (corners y tarjetas), clubelo.com (Elo), sportytrader.com (1X2/DC/DNB/BTTS/O-U 2.5), oddssafari.com (O-U 1.5/3.5, corners y tarjetas), statsbet.es (Argentina), dailysportpick.com, BetMGM y fuentes locales de contraste. CORRECCIONES DE KICKOFF (ET/ART -> UTC): Heerenveen 18:00Z, Frankfurt 18:30Z, Frosinone 18:45Z, Le Mans 18:45Z, Deportivo 19:00Z, Defensa y Justicia 22:00Z, Boca 00:30Z del 17/10 (21:30 ART del 16/10). Mercados de corners y tarjetas: se cotizaron AMBOS lados de cada linea evaluada (corners 8.5/9.5/10.5 y tarjetas 3.5/4.5/5.5) donde hubo cuota verificable; los tramos sin cuota (p. ej. tarjetas 5.5 en la mayoria de los partidos y la totalidad del mercado de tarjetas de Heerenveen-Excelsior) quedan consignados como 'sin cotizar' y no se operan. DISCREPANCIAS de la linea 2.5 reportadas y NO sustituidas: Eintracht over 2.5 (1.44 usado vs 1.34 oddssafari / 1.36 dailysportpick) y Defensa under 2.5 (1.99 usado vs 1.65 oddssafari / 1.54 BetMGM). BANDERAS DE BAJA CONFIANZA (documentadas, el motor se ejecuto igual porque los 4 xG existen): la pagina de StatsBet de Boca Juniors esta auto-encuadrada en Copa Libertadores 2026 (los datos de Boca son de baja confianza); la ventana temporal de xG de Defensa y Justicia e Instituto no esta determinada (~16 partidos implicados por 'Diferencia xG'); los for/against de corners y tarjetas de ambos partidos argentinos fueron derivados aritmeticamente (against = Media total - Media equipo) porque StatsBet no expone for/against directo. Lesiones, suspensiones y estado de entrenador NO VERIFICADOS en 6 de los 7 partidos: la busqueda web devolvio cero resultados en todos los idiomas consultados y FBref/footystats/soccerstats respondieron 403; solo el partido de Boca tiene bajas y descanso verificados por fuente local (lanumero12).
1. **Bundesliga - jornada 6:** Eintracht Frankfurt vs FC Cologne (16T18:30Z). 1X2 1.92 4.40 3.76; O1.5 1.10 U1.5 8.00 O2.5 1.44 U2.5 3.40 O3.5 1.91 U3.5 2.05; btts_yes 1.40 btts_no 3.30 1x 1.34 x2 1.98 over_corners_8_5 1.38 under_corners_8_5 3.30 over_corners_9_5 1.66 under_corners_9_5 2.40 over_corners_10_5 2.09 under_corners_10_5 1.85 over_cards_3_5 1.80 under_cards_3_5 1.90. Elo 1732/1659; xG 2.17/2.73 vs 2.1/1.95.
2. **Serie A - jornada 7:** Frosinone vs Sassuolo (16T18:45Z). 1X2 2.51 3.85 2.86; O1.5 1.14 U1.5 6.50 O2.5 1.45 U2.5 3.00 O3.5 2.11 U3.5 1.84; btts_yes 1.45 btts_no 3.00 1x 1.48 x2 1.62 over_corners_8_5 1.41 under_corners_8_5 3.00 over_corners_9_5 1.71 under_corners_9_5 2.25 over_corners_10_5 2.20 under_corners_10_5 1.75 over_cards_3_5 1.60 under_cards_3_5 2.20 over_cards_4_5 2.35 under_cards_4_5 1.50. Elo 1684/1698; xG 1.48/2.42 vs 1.78/1.68.
3. **LaLiga - jornada 9:** Deportivo vs Levante (16T19:00Z). 1X2 2.17 3.61 3.61; O1.5 1.29 U1.5 4.00 O2.5 1.98 U2.5 2.04 O3.5 3.25 U3.5 1.40; btts_yes 1.72 btts_no 2.12 1x 1.33 x2 1.77 over_corners_8_5 1.51 under_corners_8_5 2.52 over_corners_9_5 1.87 under_corners_9_5 1.91 over_corners_10_5 2.45 under_corners_10_5 1.55 over_cards_3_5 1.32 under_cards_3_5 3.05 over_cards_4_5 1.75 under_cards_4_5 1.95. Elo 1688/1709; xG 1.34/1.47 vs 1.62/2.36.
4. **Ligue 1 - jornada 7:** Le Mans vs Toulouse (16T18:45Z). 1X2 3.21 3.70 2.31; O1.5 1.22 U1.5 5.00 O2.5 1.70 U2.5 2.38 O3.5 2.62 U3.5 1.58; btts_yes 1.62 btts_no 2.50 1x 1.69 x2 1.40 over_corners_8_5 1.65 under_corners_8_5 2.45 over_corners_9_5 2.10 under_corners_9_5 1.85 over_corners_10_5 2.80 under_corners_10_5 1.50 over_cards_3_5 1.65 under_cards_3_5 2.10 over_cards_4_5 2.45 under_cards_4_5 1.45. Elo 1595/1691; xG 1.67/2.45 vs 2.0/1.59.
5. **Eredivisie - jornada 9:** Heerenveen vs Excelsior (16T18:00Z). 1X2 1.60 4.60 5.50; O1.5 1.14 U1.5 6.50 O2.5 1.45 U2.5 2.90 O3.5 2.05 U3.5 1.84; btts_yes 1.50 btts_no 2.67 1x 1.18 x2 2.45 over_corners_8_5 1.44 under_corners_8_5 2.92 over_corners_9_5 1.75 under_corners_9_5 2.20 over_corners_10_5 2.25 under_corners_10_5 1.75. Elo 1550/1494; xG 1.73/1.68 vs 1.34/1.7.
6. **Liga Profesional Argentina - Clausura F13:** Defensa y Justicia vs Instituto (16T22:00Z). 1X2 2.52 3.10 3.20; O1.5 1.45 U1.5 3.00 O2.5 2.37 U2.5 1.99 O3.5 4.50 U3.5 1.25; btts_yes 2.00 btts_no 1.84 1x 1.40 x2 1.55 12 1.40 over_corners_8_5 1.80 under_corners_8_5 2.05 over_corners_9_5 2.35 under_corners_9_5 1.62 over_corners_10_5 3.25 under_corners_10_5 1.40 over_cards_3_5 1.40 under_cards_3_5 2.65 over_cards_4_5 1.95 under_cards_4_5 1.75. Elo 1660/1688; xG 0.96/1.17 vs 1.34/0.79.
7. **Liga Profesional Argentina - Clausura F13:** Boca Juniors vs Talleres (17T00:30Z). 1X2 1.60 3.92 6.25; O1.5 1.35 U1.5 3.40 O2.5 2.03 U2.5 1.80 O3.5 3.60 U3.5 1.30; btts_yes 2.04 btts_no 1.75 1x 1.14 x2 2.45 12 1.25 over_corners_8_5 1.61 under_corners_8_5 2.30 over_corners_9_5 2.02 under_corners_9_5 1.77 over_corners_10_5 2.70 under_corners_10_5 1.48 over_cards_4_5 1.60 under_cards_4_5 2.20 over_cards_5_5 2.20 under_cards_5_5 1.60. Elo 1767/1637; xG 1.22/0.66 vs 0.97/0.9.

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Eintracht Frankfurt vs FC Cologne | over_2_5 | Over 2.5 Goles | excluido | 1.44 | 92.9% | 1.08 | +33.72% | +33.72% | +26.52% | 0.19u | Media-Alta |
| 2 | Le Mans vs Toulouse | over_1_5 | Over 1.5 Goles | excluido | 1.22 | 90.2% | 1.11 | +10.00% | +10.00% | +3.90% | 0.11u | Media-Alta |
| 3 | Eintracht Frankfurt vs FC Cologne | over_3_5 | Over 3.5 Goles | prioritario | 1.91 | 88.4% | 1.13 | +68.86% | +68.86% | +59.31% | 0.19u | Media-Alta |
| 4 | Boca Juniors vs Talleres | under_3_5 | Under 3.5 Goles | excluido | 1.30 | 88.4% | 1.13 | +14.91% | +14.91% | +8.41% | 0.12u | Media-Alta |
| 5 | Le Mans vs Toulouse | over_2_5 | Over 2.5 Goles | prioritario | 1.70 | 87.0% | 1.15 | +47.88% | +47.88% | +39.38% | 0.17u | Media-Alta |
| 6 | Deportivo vs Levante | over_1_5 | Over 1.5 Goles | excluido | 1.29 | 85.8% | 1.17 | +10.69% | +10.69% | +4.24% | 0.09u | Media-Alta |
| 7 | Frosinone vs Sassuolo | over_2_5 | Over 2.5 Goles | excluido | 1.45 | 84.6% | 1.18 | +22.71% | +22.71% | +15.46% | 0.13u | Media-Alta |
| 8 | Eintracht Frankfurt vs FC Cologne | btts_yes | Ambos marcan (BTTS) | excluido | 1.40 | 80.0% | 1.25 | +12.07% | +12.07% | +5.07% | 0.08u | Media-Alta |
| 9 | Deportivo vs Levante | over_2_5 | Over 2.5 Goles | prioritario | 1.98 | 79.9% | 1.25 | +58.20% | +58.20% | +48.30% | 0.15u | Media-Alta |
| 10 | Le Mans vs Toulouse | x2 | Doble Oportunidad Empate/Toulouse | excluido | 1.40 | 78.3% | 1.28 | +9.69% | +9.69% | +2.69% | 0.06u | Media-Alta |
| 11 | Le Mans vs Toulouse | over_3_5 | Over 3.5 Goles | excluido | 2.62 | 78.3% | 1.28 | +105.17% | +105.17% | +92.07% | 0.16u | Media-Alta |
| 12 | Defensa y Justicia vs Instituto | over_cards_3_5 | Over 3.5 Tarjetas | excluido | 1.40 | 78.2% | 1.28 | +9.42% | +9.42% | +2.42% | 0.06u | Media-Alta |
| 13 | Boca Juniors vs Talleres | under_corners_10_5 | Under 10.5 Córners | excluido | 1.48 | 78.1% | 1.28 | +15.55% | +15.55% | +8.15% | 0.08u | Media-Alta |
| 14 | Heerenveen vs Excelsior | over_2_5 | Over 2.5 Goles | excluido | 1.45 | 76.5% | 1.31 | +10.94% | +10.94% | +3.69% | 0.06u | Media-Alta |
| 15 | Defensa y Justicia vs Instituto | x2 | Doble Oportunidad Empate/Instituto | prioritario | 1.55 | 76.4% | 1.31 | +18.44% | +18.44% | +10.69% | 0.08u | Media-Alta |
| 16 | Frosinone vs Sassuolo | x2 | Doble Oportunidad Empate/Sassuolo | prioritario | 1.62 | 74.7% | 1.34 | +20.95% | +20.95% | +12.85% | 0.08u | Media-Alta |
| 17 | Frosinone vs Sassuolo | over_3_5 | Over 3.5 Goles | prioritario | 2.11 | 74.3% | 1.35 | +56.69% | +56.69% | +46.14% | 0.13u | Media-Alta |
| 18 | Le Mans vs Toulouse | btts_yes | Ambos marcan (BTTS) | prioritario | 1.62 | 73.0% | 1.37 | +18.31% | +18.31% | +10.21% | 0.07u | Media-Alta |
| 19 | Boca Juniors vs Talleres | under_corners_9_5 | Under 9.5 Córners | prioritario | 1.77 | 70.2% | 1.43 | +24.16% | +24.16% | +15.31% | 0.08u | Media-Alta |
| 20 | Deportivo vs Levante | under_cards_4_5 | Under 4.5 Tarjetas | prioritario | 1.95 | 69.5% | 1.44 | +35.55% | +35.55% | +25.80% | 0.09u | Media-Alta |
| 21 | Boca Juniors vs Talleres | under_2_5 | Under 2.5 Goles | prioritario | 1.80 | 67.3% | 1.49 | +21.21% | +21.21% | +12.21% | 0.07u | Media-Alta |
| 22 | Eintracht Frankfurt vs FC Cologne | x2 | Doble Oportunidad Empate/FC Cologne | prioritario | 1.98 | 67.0% | 1.49 | +32.60% | +32.60% | +22.70% | 0.08u | Media-Alta |
| 23 | Deportivo vs Levante | over_3_5 | Over 3.5 Goles | excepcional | 3.25 | 66.3% | 1.51 | +115.64% | +115.64% | +99.39% | 0.13u | Media-Alta |
| 24 | Defensa y Justicia vs Instituto | over_cards_4_5 | Over 4.5 Tarjetas | prioritario | 1.95 | 66.3% | 1.51 | +29.34% | +29.34% | +19.59% | 0.08u | Media-Alta |
| 25 | Deportivo vs Levante | btts_yes | Ambos marcan (BTTS) | excluido | 1.72 | 65.9% | 1.52 | +13.28% | +13.28% | +4.68% | 0.05u | Media-Alta |
| 26 | Frosinone vs Sassuolo | over_corners_9_5 | Over 9.5 Córners | excluido | 1.71 | 65.4% | 1.53 | +11.82% | +11.82% | +3.27% | 0.04u | Media-Alta |
| 27 | Boca Juniors vs Talleres | btts_no | No ambos marcan | excluido | 1.75 | 64.6% | 1.55 | +13.12% | +13.12% | +4.37% | 0.04u | Media-Alta |
| 28 | Heerenveen vs Excelsior | over_3_5 | Over 3.5 Goles | prioritario | 2.05 | 60.8% | 1.64 | +24.68% | +24.68% | +14.43% | 0.06u | Media-Alta |
| 29 | Boca Juniors vs Talleres | under_corners_8_5 | Under 8.5 Córners | excluido | 2.30 | 60.6% | 1.65 | +39.47% | +39.47% | +27.97% | 0.08u | Media-Alta |
| 30 | Defensa y Justicia vs Instituto | under_2_5 | Under 2.5 Goles | excluido | 1.99 | 57.4% | 1.74 | +14.17% | +14.17% | +4.22% | 0.04u | Media |
| 31 | Frosinone vs Sassuolo | over_corners_10_5 | Over 10.5 Córners | prioritario | 2.20 | 56.9% | 1.76 | +25.07% | +25.07% | +14.07% | 0.05u | Media |
| 32 | Le Mans vs Toulouse | 2 | Victoria Toulouse | excluido | 2.31 | 56.8% | 1.76 | +31.09% | +31.09% | +19.54% | 0.06u | Media |
| 33 | Le Mans vs Toulouse | dnb_away | DNB Toulouse | prioritario | 1.67 | 56.8% | 1.38 | +16.37% | +16.37% | +8.02% | 0.06u | Media |
| 34 | Heerenveen vs Excelsior | x2 | Doble Oportunidad Empate/Excelsior | excluido | 2.45 | 54.6% | 1.83 | +33.82% | +33.82% | +21.57% | 0.06u | Media |
| 35 | Deportivo vs Levante | under_cards_3_5 | Under 3.5 Tarjetas | excepcional | 3.05 | 54.2% | 1.84 | +65.34% | +65.34% | +50.09% | 0.08u | Media |
| 36 | Frosinone vs Sassuolo | 2 | Victoria Sassuolo | excluido | 2.86 | 52.9% | 1.89 | +51.29% | +51.29% | +36.99% | 0.07u | Media |
| 37 | Frosinone vs Sassuolo | dnb_away | DNB Sassuolo | excluido | 2.06 | 52.9% | 1.48 | +30.73% | +30.73% | +20.43% | 0.07u | Media |
| 38 | Defensa y Justicia vs Instituto | under_corners_8_5 | Under 8.5 Córners | excluido | 2.05 | 52.2% | 1.92 | +6.98% | +6.98% | -3.27% | 0.02u | Media |
| 39 | Le Mans vs Toulouse | under_cards_3_5 | Under 3.5 Tarjetas | excluido | 2.10 | 51.7% | 1.93 | +8.57% | +8.57% | -1.93% | 0.02u | Media |
| 40 | Boca Juniors vs Talleres | x2 | Doble Oportunidad Empate/Talleres | excluido | 2.45 | 50.7% | 1.97 | +24.29% | +24.29% | +12.04% | 0.04u | Media |
| 41 | Eintracht Frankfurt vs FC Cologne | over_corners_10_5 | Over 10.5 Córners | excluido | 2.09 | 50.2% | 1.99 | +5.01% | +5.01% | -5.44% | 0.01u | Media |
| 42 | Heerenveen vs Excelsior | under_corners_9_5 | Under 9.5 Córners | excluido | 2.20 | 49.4% | 2.02 | +8.75% | +8.75% | -2.25% | 0.02u | Baja |
| 43 | Eintracht Frankfurt vs FC Cologne | 2 | Victoria FC Cologne | excepcional | 3.76 | 47.6% | 2.10 | +78.90% | +78.90% | +60.10% | 0.07u | Baja |
| 44 | Eintracht Frankfurt vs FC Cologne | dnb_away | DNB FC Cologne | excluido | 2.50 | 47.6% | 1.69 | +38.34% | +38.34% | +25.84% | 0.06u | Baja |
| 45 | Defensa y Justicia vs Instituto | 2 | Victoria Instituto | excepcional | 3.20 | 46.6% | 2.15 | +48.99% | +48.99% | +32.99% | 0.06u | Baja |
| 46 | Defensa y Justicia vs Instituto | dnb_away | DNB Instituto | excluido | 2.10 | 46.6% | 1.51 | +27.63% | +27.63% | +17.13% | 0.06u | Baja |
| 47 | Le Mans vs Toulouse | under_corners_8_5 | Under 8.5 Córners | excluido | 2.45 | 45.9% | 2.18 | +12.56% | +12.56% | +0.31% | 0.02u | Baja |
| 48 | Boca Juniors vs Talleres | under_1_5 | Under 1.5 Goles | excepcional | 3.40 | 43.3% | 2.31 | +47.36% | +47.36% | +30.36% | 0.05u | Baja |
| 49 | Heerenveen vs Excelsior | under_corners_8_5 | Under 8.5 Córners | excluido | 2.92 | 39.8% | 2.51 | +16.18% | +16.18% | +1.58% | 0.02u | Baja |
| 50 | Defensa y Justicia vs Instituto | under_1_5 | Under 1.5 Goles | excluido | 3.00 | 36.4% | 2.75 | +9.17% | +9.17% | -5.83% | 0.01u | Baja |
| 51 | Eintracht Frankfurt vs FC Cologne | under_corners_8_5 | Under 8.5 Córners | excluido | 3.30 | 31.8% | 3.14 | +5.03% | +5.03% | -11.47% | 0.01u | Baja |
| 52 | Deportivo vs Levante | 2 | Victoria Levante | excluido | 3.61 | 31.6% | 3.17 | +13.90% | +13.90% | -4.15% | 0.01u | Baja |
| 53 | Boca Juniors vs Talleres | X | Empate | excluido | 3.92 | 31.2% | 3.20 | +22.34% | +22.34% | +2.74% | 0.02u | Baja |
| 54 | Heerenveen vs Excelsior | 2 | Victoria Excelsior | excepcional | 5.50 | 31.0% | 3.22 | +70.67% | +70.67% | +43.17% | 0.04u | Baja |
| 55 | Heerenveen vs Excelsior | dnb_away | DNB Excelsior | excluido | 3.00 | 31.0% | 2.46 | +16.68% | +16.68% | +1.68% | 0.02u | Baja |
| 56 | Heerenveen vs Excelsior | X | Empate | excluido | 4.60 | 23.6% | 4.24 | +8.51% | +8.51% | -14.49% | 0.01u | Baja |
| 57 | Boca Juniors vs Talleres | dnb_away | DNB Talleres | excluido | 4.50 | 19.5% | 3.52 | +19.05% | +19.05% | -3.45% | 0.01u | Baja |
| 58 | Boca Juniors vs Talleres | 2 | Victoria Talleres | excluido | 6.25 | 19.5% | 5.12 | +22.00% | +22.00% | -9.25% | 0.01u | Baja |
| 59 | Heerenveen vs Excelsior | under_1_5 | Under 1.5 Goles | excluido | 6.50 | 16.2% | 6.17 | +5.30% | +5.30% | -27.20% | 0.00u | Baja |

## Evaluación Over/Under por Partido
Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada (n/d = cuota no disponible en la corrida).
| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |
|---|---|---|---:|---:|---:|---:|---:|---|
| Eintracht Frankfurt vs FC Cologne | 1.5 | 94.0% | 1.10 | +3.46% | 5.9% | 8.00 | -52.40% | Sin value |
| Eintracht Frankfurt vs FC Cologne | 2.5 | 92.9% | 1.44 | +33.72% | 7.1% | 3.40 | -75.72% | Value Over |
| Eintracht Frankfurt vs FC Cologne | 3.5 | 88.4% | 1.91 | +68.86% | 11.6% | 2.05 | -76.24% | Value Over |
| Frosinone vs Sassuolo | 1.5 | 88.7% | 1.14 | +1.11% | 11.3% | 6.50 | -26.48% | Sin value |
| Frosinone vs Sassuolo | 2.5 | 84.6% | 1.45 | +22.71% | 15.4% | 3.00 | -53.89% | Value Over |
| Frosinone vs Sassuolo | 3.5 | 74.3% | 2.11 | +56.69% | 25.7% | 1.84 | -52.64% | Value Over |
| Deportivo vs Levante | 1.5 | 85.8% | 1.29 | +10.69% | 14.2% | 4.00 | -43.24% | Value Over |
| Deportivo vs Levante | 2.5 | 79.9% | 1.98 | +58.20% | 20.1% | 2.04 | -59.00% | Value Over |
| Deportivo vs Levante | 3.5 | 66.3% | 3.25 | +115.64% | 33.7% | 1.40 | -52.89% | Value Over |
| Le Mans vs Toulouse | 1.5 | 90.2% | 1.22 | +10.00% | 9.8% | 5.00 | -50.80% | Value Over |
| Le Mans vs Toulouse | 2.5 | 87.0% | 1.70 | +47.88% | 13.0% | 2.38 | -69.04% | Value Over |
| Le Mans vs Toulouse | 3.5 | 78.3% | 2.62 | +105.17% | 21.7% | 1.58 | -65.73% | Value Over |
| Heerenveen vs Excelsior | 1.5 | 83.8% | 1.14 | -4.47% | 16.2% | 6.50 | +5.30% | Value Under |
| Heerenveen vs Excelsior | 2.5 | 76.5% | 1.45 | +10.94% | 23.5% | 2.90 | -31.88% | Value Over |
| Heerenveen vs Excelsior | 3.5 | 60.8% | 2.05 | +24.68% | 39.2% | 1.84 | -27.91% | Value Over |
| Defensa y Justicia vs Instituto | 1.5 | 63.6% | 1.45 | -7.77% | 36.4% | 3.00 | +9.17% | Value Under |
| Defensa y Justicia vs Instituto | 2.5 | 42.6% | 2.37 | +1.03% | 57.4% | 1.99 | +14.17% | Value Under |
| Defensa y Justicia vs Instituto | 3.5 | 19.1% | 4.50 | -14.18% | 80.9% | 1.25 | +1.16% | Sin value |
| Boca Juniors vs Talleres | 1.5 | 56.7% | 1.35 | -23.51% | 43.3% | 3.40 | +47.36% | Value Under |
| Boca Juniors vs Talleres | 2.5 | 32.7% | 2.03 | -33.70% | 67.3% | 1.80 | +21.21% | Value Under |
| Boca Juniors vs Talleres | 3.5 | 11.6% | 3.60 | -58.20% | 88.4% | 1.30 | +14.91% | Value Under |

## Picks Recomendados (Top 6)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Eintracht Frankfurt vs FC Cologne | over_3_5 | Over 3.5 Goles | prioritario | 1.91 | 88.4% | 1.13 | +68.86% | +68.86% | +59.31% | 0.19u | Media-Alta |
| 2 | Le Mans vs Toulouse | over_2_5 | Over 2.5 Goles | prioritario | 1.70 | 87.0% | 1.15 | +47.88% | +47.88% | +39.38% | 0.17u | Media-Alta |
| 3 | Deportivo vs Levante | over_2_5 | Over 2.5 Goles | prioritario | 1.98 | 79.9% | 1.25 | +58.20% | +58.20% | +48.30% | 0.15u | Media-Alta |
| 4 | Defensa y Justicia vs Instituto | x2 | Doble Oportunidad Empate/Instituto | prioritario | 1.55 | 76.4% | 1.31 | +18.44% | +18.44% | +10.69% | 0.08u | Media-Alta |
| 5 | Frosinone vs Sassuolo | x2 | Doble Oportunidad Empate/Sassuolo | prioritario | 1.62 | 74.7% | 1.34 | +20.95% | +20.95% | +12.85% | 0.08u | Media-Alta |
| 6 | Frosinone vs Sassuolo | over_3_5 | Over 3.5 Goles | prioritario | 2.11 | 74.3% | 1.35 | +56.69% | +56.69% | +46.14% | 0.13u | Media-Alta |

## Detalle de Picks
### Pick 1: Eintracht Frankfurt vs FC Cologne
- **Mercado:** over_3_5
- **Selección:** Over 3.5 Goles
- **Cuota:** 1.91
- **Probabilidad modelo:** 88.4%
- **Probabilidad conservadora:** 83.4%
- **Probabilidad implícita:** 52.4%
- **Cuota justa:** 1.13
- **Edge:** +68.86%
- **EV:** +68.86%
- **EV robusto:** +59.31%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.13
- **Stake:** 0.19u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al local (1732 vs 1659, brecha 73) | perfil xG 2.17/2.73 (local) vs 2.10/1.95 (visitante). El motor model-v1.3 estima 88.4% para 'Over 3.5 Goles' frente a una probabilidad implicita de 52.4% (cuota 1.91); edge +68.86% y EV robusto +59.31%.
- **Riesgos:** Muestra n=5 partidos de Bundesliga 26/27 (ventana exacta 5-10). xG de understat y corners/cards de Sofascore son familias distintas (ninguna fuente alcanzable expone ambos); n coincide (5 y 5). Sofascore no expone xG-against -> xG_against solo de understat. Cards = amarillas (Frankfurt con 0 amarillas-rojas). Cards 4.5 y 5.5 sin cotizar (solo 3.5). DISCREPANCIA 2.5 OVER: oddssafari 1.34 y dailysportpick 1.36 vs 1.44 usado (>2% abs) -> se reporta, no se reemplaza. Lesiones/suspensiones y estado de entrenador NO VERIFICADOS: la busqueda web devolvio cero resultados en todos los idiomas; FBref 403. Contexto: Frankfurt 14o (5 pts, 9 GF/16 GA), Koln 10o (7 pts, 8 GF/10 GA); Frankfurt viene de 0-6 en Leipzig, 6 dias de descanso; Koln 5 dias. H2H Sofascore: 10 cruces, 2-3-5.
- **Fuentes:** xG: understat.com/getTeamData/Eintracht_Frankfurt/2026 y /FC_Cologne/2026 (n=5 cada uno, media por partido); corners/cards: sofascore.com/api/v1/team/2674 y /2671/unique-tournament/35/season/97464/statistics/overall (n=5); Elo: clubelo.com/Ranking (Frankfurt 1732, Koln 1659); cuotas 1X2/DC/DNB/BTTS/O-U 2.5: sportytrader.com/en/odds/eintracht-frankfurt-koln-8595807 (via r.jina.ai); O-U 1.5/3.5, corners y cards 3.5: oddssafari.com/matches/soccer/germany/bundesliga/eintracht-frankfurt-vs-fc-cologne/3343090; verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 2: Le Mans vs Toulouse
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.70
- **Probabilidad modelo:** 87.0%
- **Probabilidad conservadora:** 82.0%
- **Probabilidad implícita:** 58.8%
- **Cuota justa:** 1.15
- **Edge:** +47.88%
- **EV:** +47.88%
- **EV robusto:** +39.38%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.15
- **Stake:** 0.17u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1691 vs 1595, brecha 96) | perfil xG 1.67/2.45 (local) vs 2.00/1.59 (visitante). El motor model-v1.3 estima 87.0% para 'Over 2.5 Goles' frente a una probabilidad implicita de 58.8% (cuota 1.70); edge +47.88% y EV robusto +39.38%.
- **Riesgos:** Muestra n=6 (jornada 6 de Ligue 1 completada). Los totales de corners de ambos equipos suman 56 en 6 partidos (9.33/partido) contra 9.65 de media de liga (performanceodds) -> consistencia interna verificada. cards_home_for = amarillas + rojas (14+1)/6 = 2.50; solo amarillas = 2.33 (Le Mans lidera la liga en amonestaciones con 14 y en penaltis concedidos con 3). Cards 5.5 sin cotizar. Cross-check 2.5: oddssafari 1.70/2.38 IDENTICO al capturado. Aviso: Le Mans xG_against 2.45 es la peor de la liga; Toulouse crea mas de lo que concede (12.01 vs 9.53) pero convierte mal. Entrenador de Toulouse cambiado en mayo-2026 (Askou por Martinez Novell) -> incertidumbre elevada. Fuentes descartadas: goalstatslab (numeros internamente inconsistentes: xGA 0.16 en Toulouse), performanceodds (sin tabla Ligue 1), footystats/fbref/soccerstats (403). Contexto: Le Mans 14o (6 pts), Toulouse 15o (6 pts); ambos 6 dias de descanso; Toulouse 0-0-3 como visitante con los tres empates 2-2.
- **Fuentes:** xG: understat.com/league/Ligue_1 (via r.jina.ai; Le Mans 10.01/14.69, Toulouse 12.01/9.53 en 6 partidos) con cross-check sofascore.com/api/v1/team/1672 y /1681/unique-tournament/34/season/96127/statistics/overall; corners/cards: sofascore (Le Mans corners 17/39, amarillas 14 + 1 roja; Toulouse 27/29, amarillas 10) sobre n=6; Elo: clubelo.com/Ranking (Le Mans 1595, Toulouse 1691); cuotas 1X2/DC/DNB/BTTS/O-U 2.5: sportytrader.com/en/odds/le-mans-uc-72-toulouse-8532687 (via r.jina.ai); O-U 1.5/3.5, corners y cards: oddssafari.com/matches/soccer/france/ligue-1/le-mans-vs-toulouse/3367763; verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 3: Deportivo vs Levante
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.98
- **Probabilidad modelo:** 79.9%
- **Probabilidad conservadora:** 74.9%
- **Probabilidad implícita:** 50.5%
- **Cuota justa:** 1.25
- **Edge:** +58.20%
- **EV:** +58.20%
- **EV robusto:** +48.30%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.25
- **Stake:** 0.15u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1709 vs 1688, brecha 21) | perfil xG 1.34/1.47 (local) vs 1.62/2.36 (visitante). El motor model-v1.3 estima 79.9% para 'Over 2.5 Goles' frente a una probabilidad implicita de 50.5% (cuota 1.98); edge +58.20% y EV robusto +48.30%.
- **Riesgos:** Muestras n=8 (Depor) y n=7 (Levante), ambas temporada 26/27 completa hasta la fecha (Depor jugo una jornada mas). Depor tiene el xG a favor mas bajo del grupo (1.34); Levante concede 2.36 xG/partido y promedia 3.3 corners a favor (el mas bajo). Cards 5.5 sin cotizar. Velocidad de juego: Levante con 4 dias de descanso (el menor del grupo) y partido el 21-10. Lesiones/suspensiones/entrenador NO VERIFICADOS. Contexto: Depor 8o (10 pts, 12 GF/11 GA), Levante 17o (6 pts, 11 GF/15 GA). H2H Sofascore: 10 cruces, 3-3-4; primer enfrentamiento en 26/27 (Depor ascendido).
- **Fuentes:** xG: understat.com/getTeamData/Deportivo_La_Coruna/2026 y /Levante/2026 (n=8 y n=7); corners/cards: sofascore.com/api/v1/team/2832 y /2849/unique-tournament/8/season/97268/statistics/overall (n=8 y n=7); Elo: clubelo.com/Ranking (Depor 1688, Levante 1709); cuotas 1X2/DC/DNB/BTTS/O-U 2.5: sportytrader.com/en/odds/la-coruna-levante-8586495 (via r.jina.ai); O-U 1.5/3.5, corners y cards: oddssafari.com/matches/soccer/spain/laliga/la-coruna-vs-levante/3457763; verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 4: Defensa y Justicia vs Instituto
- **Mercado:** x2
- **Selección:** Doble Oportunidad Empate/Instituto
- **Cuota:** 1.55
- **Probabilidad modelo:** 76.4%
- **Probabilidad conservadora:** 71.4%
- **Probabilidad implícita:** 64.5%
- **Cuota justa:** 1.31
- **Edge:** +18.44%
- **EV:** +18.44%
- **EV robusto:** +10.69%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.31
- **Stake:** 0.08u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1688 vs 1660, brecha 28) | perfil xG 0.96/1.17 (local) vs 1.34/0.79 (visitante). El motor model-v1.3 estima 76.4% para 'Doble Oportunidad Empate/Instituto' frente a una probabilidad implicita de 64.5% (cuota 1.55); edge +18.44% y EV robusto +10.69%. Atencion: el input de este partido arrastra banderas de baja confianza (ver Riesgos); la incertidumbre real es mayor que la base del motor.
- **Riesgos:** VENTANA xG NO DETERMINADA: StatsBet ofrece Ultimos 5 / Ultimos 10 / Temporada (28) y sus tablas se contradicen (la fila Temporada duplica Ultimos 10 con 0.63/0.73 por partido) mientras 'Diferencia xG' (-3.38 DyJ; +8.93 Instituto) implica ~16 partidos -> tratar xG como indicativo, no como hecho consolidado. for/against de corners y cards DERIVADOS de la aritmetica documentada against = Media total - Media equipo (DyJ: 10.2-3.2=7.0 corners, 5.4-2.2=3.2 cards; Instituto: 7.2-4.8=2.4, 7.2-4.0=3.2), porque StatsBet no expone for/against directo; la derivacion asume la misma ventana para ambos. Cards 5.5 sin cotizar. DISCREPANCIA 2.5 UNDER: oddssafari 1.65 y BetMGM 1.54 vs 1.99 usado (>15% abs) -> se reporta, no se reemplaza. HORARIO: 19:00 ART segun fuente local (22:00Z); el widget de StatsBet muestra 17 oct 00:00 sin reconciliar. Bajas: DyJ con Sosa Yung expulsado + Roman y Souto lesionados; Instituto con Albarracin, Cerato, Moyano y Romero. Contexto: Instituto lider (26 pts, 8G-2E-2P), DyJ 2o (24 pts, 7G-3E-2P); descansos 6 y 7 dias. H2H ultimos 5: 2-2-1, goles 4-7, ultimo Instituto 2-0 (07-04-2026).
- **Fuentes:** xG/corners/cards: statsbet.es/futbol/equipos/defensa-y-justicia y /instituto (bloques Media equipo / Media total, n no determinada); Elo: clubelo.com/Ranking (DyJ 1660, Instituto 1688); cuotas 1X2/DC/DNB/BTTS/O-U 2.5: sportytrader.com/es/apuestas/defensa-y-justicia-instituto-accordoba-8689633 (via r.jina.ai); O-U 1.5/3.5, corners y cards: oddssafari.com/matches/soccer/argentina/liga-profesional/defensa-justicia-vs-instituto/5271080; clasificacion: valuestats.com y alargue.com; bajas: planetagrandt.com.ar/search/label/Lesionados; verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 5: Frosinone vs Sassuolo
- **Mercado:** x2
- **Selección:** Doble Oportunidad Empate/Sassuolo
- **Cuota:** 1.62
- **Probabilidad modelo:** 74.7%
- **Probabilidad conservadora:** 69.7%
- **Probabilidad implícita:** 61.7%
- **Cuota justa:** 1.34
- **Edge:** +20.95%
- **EV:** +20.95%
- **EV robusto:** +12.85%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.34
- **Stake:** 0.08u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1698 vs 1684, brecha 14) | perfil xG 1.48/2.42 (local) vs 1.78/1.68 (visitante). El motor model-v1.3 estima 74.7% para 'Doble Oportunidad Empate/Sassuolo' frente a una probabilidad implicita de 61.7% (cuota 1.62); edge +20.95% y EV robusto +12.85%.
- **Riesgos:** Muestra n=6 partidos de Serie A 26/27. Frosinone tiene la peor tasa de corners en contra del grupo (7.3/partido) y Sassuolo la menor de corners a favor (4.3). Cards 5.5 sin cotizar. Cross-check 2.5: oddssafari 1.45/2.85 vs 1.45/3.00 capturado (under difiere ~5%, se conserva el capturado). Lesiones/suspensiones/entrenador NO VERIFICADOS (busqueda web sin resultados). Contexto: Frosinone 9o (10 pts), Sassuolo 11o (8 pts); descansos 6 y 5 dias. H2H Sofascore: 10 cruces, 2-6-2 (Sassuolo historicamente dominante). CORRELACION: este mismo partido aporta 2 picks al portfolio (junto a over_3_5 (2.11)); son eventos correlacionados y elevan la varianza conjunta mas alla de la de picks de partidos independientes, por lo que el stake agregado del partido deberia leerse como una sola exposicion.
- **Fuentes:** xG: understat.com/getTeamData/Frosinone/2026 y /Sassuolo/2026 (n=6 cada uno); corners/cards: sofascore.com/api/v1/team/2801 y /2793/unique-tournament/23/season/95836/statistics/overall (n=6); Elo: clubelo.com/Ranking (Frosinone 1684, Sassuolo 1698); cuotas 1X2/DC/DNB/BTTS/O-U 2.5: sportytrader.com/en/odds/frosinone-sassuolo-8522155 (via r.jina.ai); O-U 1.5/3.5, corners y cards: oddssafari.com/matches/soccer/italy/serie-a/frosinone-vs-sassuolo/3477690; verosimilitud del modelo y calibracion Platt (model-v1.3).

### Pick 6: Frosinone vs Sassuolo
- **Mercado:** over_3_5
- **Selección:** Over 3.5 Goles
- **Cuota:** 2.11
- **Probabilidad modelo:** 74.3%
- **Probabilidad conservadora:** 69.3%
- **Probabilidad implícita:** 47.4%
- **Cuota justa:** 1.35
- **Edge:** +56.69%
- **EV:** +56.69%
- **EV robusto:** +46.14%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.35
- **Stake:** 0.13u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0% (model-v1.3); muestras 5-8 partidos por equipo en ligas domesticas 26/27
- **Por qué:** Elo favorece al visitante (1698 vs 1684, brecha 14) | perfil xG 1.48/2.42 (local) vs 1.78/1.68 (visitante). El motor model-v1.3 estima 74.3% para 'Over 3.5 Goles' frente a una probabilidad implicita de 47.4% (cuota 2.11); edge +56.69% y EV robusto +46.14%.
- **Riesgos:** Muestra n=6 partidos de Serie A 26/27. Frosinone tiene la peor tasa de corners en contra del grupo (7.3/partido) y Sassuolo la menor de corners a favor (4.3). Cards 5.5 sin cotizar. Cross-check 2.5: oddssafari 1.45/2.85 vs 1.45/3.00 capturado (under difiere ~5%, se conserva el capturado). Lesiones/suspensiones/entrenador NO VERIFICADOS (busqueda web sin resultados). Contexto: Frosinone 9o (10 pts), Sassuolo 11o (8 pts); descansos 6 y 5 dias. H2H Sofascore: 10 cruces, 2-6-2 (Sassuolo historicamente dominante). CORRELACION: este mismo partido aporta 2 picks al portfolio (junto a x2 (1.62)); son eventos correlacionados y elevan la varianza conjunta mas alla de la de picks de partidos independientes, por lo que el stake agregado del partido deberia leerse como una sola exposicion.
- **Fuentes:** xG: understat.com/getTeamData/Frosinone/2026 y /Sassuolo/2026 (n=6 cada uno); corners/cards: sofascore.com/api/v1/team/2801 y /2793/unique-tournament/23/season/95836/statistics/overall (n=6); Elo: clubelo.com/Ranking (Frosinone 1684, Sassuolo 1698); cuotas 1X2/DC/DNB/BTTS/O-U 2.5: sportytrader.com/en/odds/frosinone-sassuolo-8522155 (via r.jina.ai); O-U 1.5/3.5, corners y cards: oddssafari.com/matches/soccer/italy/serie-a/frosinone-vs-sassuolo/3477690; verosimilitud del modelo y calibracion Platt (model-v1.3).

## NO BET / Excluidos
- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**
  - Eintracht Frankfurt vs FC Cologne — Over 1.5 Goles (over_1_5): Prob modelo 94.0%, EV +3.46%, EV robusto -2.04% → sin value.
  - Eintracht Frankfurt vs FC Cologne — Under 1.5 Goles (under_1_5): Prob modelo 5.9%, EV -52.40%, EV robusto -92.40% → sin value.
  - Eintracht Frankfurt vs FC Cologne — Under 2.5 Goles (under_2_5): Prob modelo 7.1%, EV -75.72%, EV robusto -92.72% → sin value.
  - Eintracht Frankfurt vs FC Cologne — Under 3.5 Goles (under_3_5): Prob modelo 11.6%, EV -76.24%, EV robusto -86.49% → sin value.
  - Eintracht Frankfurt vs FC Cologne — Over 8.5 Córners (over_corners_8_5): Prob modelo 68.2%, EV -5.92%, EV robusto -12.82% → sin value.
  - Eintracht Frankfurt vs FC Cologne — Over 9.5 Córners (over_corners_9_5): Prob modelo 59.2%, EV -1.68%, EV robusto -9.98% → sin value.
  - Eintracht Frankfurt vs FC Cologne — Under 9.5 Córners (under_corners_9_5): Prob modelo 40.8%, EV -2.15%, EV robusto -14.15% → sin value.
  - Eintracht Frankfurt vs FC Cologne — Under 10.5 Córners (under_corners_10_5): Prob modelo 49.8%, EV -7.95%, EV robusto -17.20% → sin value.
  - Eintracht Frankfurt vs FC Cologne — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 45.8%, EV -17.58%, EV robusto -26.58% → sin value.
  - Eintracht Frankfurt vs FC Cologne — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 54.2%, EV +3.00%, EV robusto -6.50% → sin value.
  - Frosinone vs Sassuolo — Over 1.5 Goles (over_1_5): Prob modelo 88.7%, EV +1.11%, EV robusto -4.59% → sin value.
  - Frosinone vs Sassuolo — Under 1.5 Goles (under_1_5): Prob modelo 11.3%, EV -26.48%, EV robusto -58.98% → sin value.
  - Frosinone vs Sassuolo — Under 2.5 Goles (under_2_5): Prob modelo 15.4%, EV -53.89%, EV robusto -68.89% → sin value.
  - Frosinone vs Sassuolo — Under 3.5 Goles (under_3_5): Prob modelo 25.7%, EV -52.64%, EV robusto -61.84% → sin value.
  - Frosinone vs Sassuolo — Over 8.5 Córners (over_corners_8_5): Prob modelo 73.6%, EV +3.78%, EV robusto -3.27% → sin value.
  - Frosinone vs Sassuolo — Under 8.5 Córners (under_corners_8_5): Prob modelo 26.4%, EV -20.80%, EV robusto -35.80% → sin value.
  - Frosinone vs Sassuolo — Under 9.5 Córners (under_corners_9_5): Prob modelo 34.6%, EV -22.14%, EV robusto -33.39% → sin value.
  - Frosinone vs Sassuolo — Under 10.5 Córners (under_corners_10_5): Prob modelo 43.1%, EV -24.48%, EV robusto -33.23% → sin value.
  - Frosinone vs Sassuolo — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 53.8%, EV -13.87%, EV robusto -21.87% → sin value.
  - Frosinone vs Sassuolo — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 46.2%, EV +1.57%, EV robusto -9.43% → sin value.
  - Frosinone vs Sassuolo — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 38.3%, EV -9.93%, EV robusto -21.68% → sin value.
  - Frosinone vs Sassuolo — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 61.7%, EV -7.49%, EV robusto -14.99% → sin value.
  - Deportivo vs Levante — Under 1.5 Goles (under_1_5): Prob modelo 14.2%, EV -43.24%, EV robusto -63.24% → sin value.
  - Deportivo vs Levante — Under 2.5 Goles (under_2_5): Prob modelo 20.1%, EV -59.00%, EV robusto -69.20% → sin value.
  - Deportivo vs Levante — Under 3.5 Goles (under_3_5): Prob modelo 33.7%, EV -52.89%, EV robusto -59.89% → sin value.
  - Deportivo vs Levante — Over 8.5 Córners (over_corners_8_5): Prob modelo 58.4%, EV -11.81%, EV robusto -19.36% → sin value.
  - Deportivo vs Levante — Under 8.5 Córners (under_corners_8_5): Prob modelo 41.6%, EV +4.81%, EV robusto -7.79% → sin value.
  - Deportivo vs Levante — Over 9.5 Córners (over_corners_9_5): Prob modelo 48.7%, EV -9.00%, EV robusto -18.35% → sin value.
  - Deportivo vs Levante — Under 9.5 Córners (under_corners_9_5): Prob modelo 51.3%, EV -1.94%, EV robusto -11.49% → sin value.
  - Deportivo vs Levante — Over 10.5 Córners (over_corners_10_5): Prob modelo 39.5%, EV -3.32%, EV robusto -15.57% → sin value.
  - Deportivo vs Levante — Under 10.5 Córners (under_corners_10_5): Prob modelo 60.5%, EV -6.16%, EV robusto -13.91% → sin value.
  - Deportivo vs Levante — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 45.8%, EV -39.56%, EV robusto -46.16% → sin value.
  - Deportivo vs Levante — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 30.5%, EV -46.64%, EV robusto -55.39% → sin value.
  - Le Mans vs Toulouse — Under 1.5 Goles (under_1_5): Prob modelo 9.8%, EV -50.80%, EV robusto -75.80% → sin value.
  - Le Mans vs Toulouse — Under 2.5 Goles (under_2_5): Prob modelo 13.0%, EV -69.04%, EV robusto -80.94% → sin value.
  - Le Mans vs Toulouse — Under 3.5 Goles (under_3_5): Prob modelo 21.7%, EV -65.73%, EV robusto -73.63% → sin value.
  - Le Mans vs Toulouse — Over 8.5 Córners (over_corners_8_5): Prob modelo 54.1%, EV -10.80%, EV robusto -19.05% → sin value.
  - Le Mans vs Toulouse — Over 9.5 Córners (over_corners_9_5): Prob modelo 44.2%, EV -7.26%, EV robusto -17.76% → sin value.
  - Le Mans vs Toulouse — Under 9.5 Córners (under_corners_9_5): Prob modelo 55.8%, EV +3.30%, EV robusto -5.95% → sin value.
  - Le Mans vs Toulouse — Over 10.5 Córners (over_corners_10_5): Prob modelo 35.1%, EV -1.80%, EV robusto -15.80% → sin value.
  - Le Mans vs Toulouse — Under 10.5 Córners (under_corners_10_5): Prob modelo 64.9%, EV -2.60%, EV robusto -10.10% → sin value.
  - Le Mans vs Toulouse — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 48.3%, EV -20.30%, EV robusto -28.55% → sin value.
  - Le Mans vs Toulouse — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 32.9%, EV -19.48%, EV robusto -31.73% → sin value.
  - Le Mans vs Toulouse — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 67.1%, EV -2.65%, EV robusto -9.90% → sin value.
  - Heerenveen vs Excelsior — Over 1.5 Goles (over_1_5): Prob modelo 83.8%, EV -4.47%, EV robusto -10.17% → sin value.
  - Heerenveen vs Excelsior — Under 2.5 Goles (under_2_5): Prob modelo 23.5%, EV -31.88%, EV robusto -46.38% → sin value.
  - Heerenveen vs Excelsior — Under 3.5 Goles (under_3_5): Prob modelo 39.2%, EV -27.91%, EV robusto -37.11% → sin value.
  - Heerenveen vs Excelsior — Over 8.5 Córners (over_corners_8_5): Prob modelo 60.2%, EV -13.29%, EV robusto -20.49% → sin value.
  - Heerenveen vs Excelsior — Over 9.5 Córners (over_corners_9_5): Prob modelo 50.6%, EV -11.51%, EV robusto -20.26% → sin value.
  - Heerenveen vs Excelsior — Over 10.5 Córners (over_corners_10_5): Prob modelo 41.4%, EV -6.95%, EV robusto -18.20% → sin value.
  - Heerenveen vs Excelsior — Under 10.5 Córners (under_corners_10_5): Prob modelo 58.6%, EV +2.63%, EV robusto -6.12% → sin value.
  - Defensa y Justicia vs Instituto — Over 1.5 Goles (over_1_5): Prob modelo 63.6%, EV -7.77%, EV robusto -15.02% → sin value.
  - Defensa y Justicia vs Instituto — Over 2.5 Goles (over_2_5): Prob modelo 42.6%, EV +1.03%, EV robusto -10.82% → sin value.
  - Defensa y Justicia vs Instituto — Over 3.5 Goles (over_3_5): Prob modelo 19.1%, EV -14.18%, EV robusto -36.69% → sin value.
  - Defensa y Justicia vs Instituto — Under 3.5 Goles (under_3_5): Prob modelo 80.9%, EV +1.16%, EV robusto -5.09% → sin value.
  - Defensa y Justicia vs Instituto — Over 8.5 Córners (over_corners_8_5): Prob modelo 47.8%, EV -13.93%, EV robusto -22.93% → sin value.
  - Defensa y Justicia vs Instituto — Over 9.5 Córners (over_corners_9_5): Prob modelo 37.9%, EV -10.90%, EV robusto -22.65% → sin value.
  - Defensa y Justicia vs Instituto — Under 9.5 Córners (under_corners_9_5): Prob modelo 62.1%, EV +0.58%, EV robusto -7.52% → sin value.
  - Defensa y Justicia vs Instituto — Over 10.5 Córners (over_corners_10_5): Prob modelo 29.2%, EV -5.18%, EV robusto -21.43% → sin value.
  - Defensa y Justicia vs Instituto — Under 10.5 Córners (under_corners_10_5): Prob modelo 70.8%, EV -0.85%, EV robusto -7.85% → sin value.
  - Defensa y Justicia vs Instituto — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 21.8%, EV -42.11%, EV robusto -55.36% → sin value.
  - Defensa y Justicia vs Instituto — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 33.7%, EV -41.07%, EV robusto -49.82% → sin value.
  - Boca Juniors vs Talleres — Over 1.5 Goles (over_1_5): Prob modelo 56.7%, EV -23.51%, EV robusto -30.26% → sin value.
  - Boca Juniors vs Talleres — Over 2.5 Goles (over_2_5): Prob modelo 32.7%, EV -33.70%, EV robusto -43.85% → sin value.
  - Boca Juniors vs Talleres — Over 3.5 Goles (over_3_5): Prob modelo 11.6%, EV -58.20%, EV robusto -76.20% → sin value.
  - Boca Juniors vs Talleres — Over 8.5 Córners (over_corners_8_5): Prob modelo 39.4%, EV -36.63%, EV robusto -44.68% → sin value.
  - Boca Juniors vs Talleres — Over 9.5 Córners (over_corners_9_5): Prob modelo 29.8%, EV -39.70%, EV robusto -49.80% → sin value.
  - Boca Juniors vs Talleres — Over 10.5 Córners (over_corners_10_5): Prob modelo 21.9%, EV -40.81%, EV robusto -54.31% → sin value.
  - Boca Juniors vs Talleres — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 58.8%, EV -5.89%, EV robusto -13.89% → sin value.
  - Boca Juniors vs Talleres — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 41.2%, EV -9.41%, EV robusto -20.41% → sin value.
  - Boca Juniors vs Talleres — Over 5.5 Tarjetas (over_cards_5_5): Prob modelo 45.7%, EV +0.62%, EV robusto -10.38% → sin value.
  - Boca Juniors vs Talleres — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 54.3%, EV -13.18%, EV robusto -21.18% → sin value.
- **Candidatos con value excluidos por probabilidad-primero:**
  - Eintracht Frankfurt vs FC Cologne: DNB FC Cologne (dnb_away) EV +38.34% / EV rob +25.84%, Ambos marcan (BTTS) (btts_yes) EV +12.07% / EV rob +5.07%, Over 2.5 Goles (over_2_5) EV +33.72% / EV rob +26.52%, Under 8.5 Córners (under_corners_8_5) EV +5.03% / EV rob -11.47%, Over 10.5 Córners (over_corners_10_5) EV +5.01% / EV rob -5.44%, Victoria FC Cologne (2) EV +78.90% / EV rob +60.10% — No cumple los mínimos de selección probabilidad-primero.
  - Frosinone vs Sassuolo: Victoria Sassuolo (2) EV +51.29% / EV rob +36.99%, DNB Sassuolo (dnb_away) EV +30.73% / EV rob +20.43%, Over 2.5 Goles (over_2_5) EV +22.71% / EV rob +15.46%, Over 9.5 Córners (over_corners_9_5) EV +11.82% / EV rob +3.27% — No cumple los mínimos de selección probabilidad-primero.
  - Deportivo vs Levante: Victoria Levante (2) EV +13.90% / EV rob -4.15%, Ambos marcan (BTTS) (btts_yes) EV +13.28% / EV rob +4.68%, Over 1.5 Goles (over_1_5) EV +10.69% / EV rob +4.24%, Over 3.5 Goles (over_3_5) EV +115.64% / EV rob +99.39%, Under 3.5 Tarjetas (under_cards_3_5) EV +65.34% / EV rob +50.09% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Le Mans vs Toulouse: Victoria Toulouse (2) EV +31.09% / EV rob +19.54%, Doble Oportunidad Empate/Toulouse (x2) EV +9.69% / EV rob +2.69%, Over 1.5 Goles (over_1_5) EV +10.00% / EV rob +3.90%, Over 3.5 Goles (over_3_5) EV +105.17% / EV rob +92.07%, Under 8.5 Córners (under_corners_8_5) EV +12.56% / EV rob +0.31%, Under 3.5 Tarjetas (under_cards_3_5) EV +8.57% / EV rob -1.93% — No cumple los mínimos de selección probabilidad-primero.
  - Heerenveen vs Excelsior: Empate (X) EV +8.51% / EV rob -14.49%, Doble Oportunidad Empate/Excelsior (x2) EV +33.82% / EV rob +21.57%, DNB Excelsior (dnb_away) EV +16.68% / EV rob +1.68%, Under 1.5 Goles (under_1_5) EV +5.30% / EV rob -27.20%, Over 2.5 Goles (over_2_5) EV +10.94% / EV rob +3.69%, Under 8.5 Córners (under_corners_8_5) EV +16.18% / EV rob +1.58%, Under 9.5 Córners (under_corners_9_5) EV +8.75% / EV rob -2.25%, Victoria Excelsior (2) EV +70.67% / EV rob +43.17% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Defensa y Justicia vs Instituto: DNB Instituto (dnb_away) EV +27.63% / EV rob +17.13%, Under 1.5 Goles (under_1_5) EV +9.17% / EV rob -5.83%, Under 2.5 Goles (under_2_5) EV +14.17% / EV rob +4.22%, Under 8.5 Córners (under_corners_8_5) EV +6.98% / EV rob -3.27%, Over 3.5 Tarjetas (over_cards_3_5) EV +9.42% / EV rob +2.42%, Victoria Instituto (2) EV +48.99% / EV rob +32.99% — No cumple los mínimos de selección probabilidad-primero.
  - Boca Juniors vs Talleres: Empate (X) EV +22.34% / EV rob +2.74%, Victoria Talleres (2) EV +22.00% / EV rob -9.25%, Doble Oportunidad Empate/Talleres (x2) EV +24.29% / EV rob +12.04%, DNB Talleres (dnb_away) EV +19.05% / EV rob -3.45%, No ambos marcan (btts_no) EV +13.12% / EV rob +4.37%, Under 3.5 Goles (under_3_5) EV +14.91% / EV rob +8.41%, Under 8.5 Córners (under_corners_8_5) EV +39.47% / EV rob +27.97%, Under 10.5 Córners (under_corners_10_5) EV +15.55% / EV rob +8.15%, Under 1.5 Goles (under_1_5) EV +47.36% / EV rob +30.36% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.

## Portfolio y Correlaciones
- **Exposición total:** 0.80u
- **Correlaciones detectadas:** Mercados presentes: over_2_5, over_3_5, x2. Verificar solapamiento de mercado mismo partido.
- **Ajuste de stake por correlación:** Los picks pertenecen a partidos distintos; no se aplica reducción adicional por eventos dependientes.

## Tracking
_Fuente: resultados vía websearch (MCP apifootball no operativo — fallback activo). Actualizado 2026-10-23._
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1 (Eintracht Frankfurt vs FC Cologne - over_3_5) | PERDIDA | 1 - 0 | -0.19u |
| Pick 2 (Le Mans vs Toulouse - over_2_5) | GANADA | 0 - 3 | +0.12u |
| Pick 3 (Deportivo vs Levante - over_2_5) | PERDIDA | 1 - 1 | -0.15u |
| Pick 4 (Defensa y Justicia vs Instituto - x2) | GANADA | 0 - 1 | +0.04u |
| Pick 5 (Frosinone vs Sassuolo - x2) | PERDIDA | 4 - 2 | -0.08u |
| Pick 6 (Frosinone vs Sassuolo - over_3_5) | GANADA | 4 - 2 | +0.14u |
| **Total** | | | **-0.12u (3 G / 3 P)** |
