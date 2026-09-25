# Análisis de Apuestas — 2026-09-20

## Metadatos
- **Fecha de análisis:** 2026-09-20T03:33:53Z
- **Fecha(s) de partido:** 2026-09-20
- **Information cutoff:** 2026-09-20T03:01:00Z
- **Modelo de IA:** bigpickle
- **Versión del motor predictivo:** model-v1.3
- **Ligas analizadas:** Premier League, Bundesliga, Serie A, La Liga, Ligue 1, Eredivisie, Primeira Liga, MLS, Liga Argentina (Primera División), Liga Colombiana (Primera A)
- **Rango de fechas solicitado:** 20 de septiembre de 2026 (un día)
- **Partidos en universo:** 35
- **Picks iniciales con value:** 75
- **Picks finales seleccionados:** 6

## Universo Analizado
Universo = 35 partidos del 2026-09-20 por liga solicitada (todos los partidos de las ligas en la fecha: The Odds API REST). Cutoff del análisis: 2026-09-20T03:01Z; 4 partidos MLS previos al cutoff (Nashville SC, Real Salt Lake, Portland Timbers, Colorado Rapids) excluidos del universo. Cuotas capa 1: The Odds API vía REST (el MCP `odds-api` no estaba operativo) — plan gratis expone h2h y totals; el plan no expone deducidas (BTTS, DO, DNB). Timestamp de captura de cuotas: 2026-09-18T21:22Z (referencia CLV). El MCP `apifootball` estaba inoperativo ('Authentification failed!') y el MCP local `football-stats` devolvió MISSING_SOURCE. xG: Understat (big-5), Statz.ai (Eredivisie, MLS y Liga Arg), FotMob/Opta (Primeira Liga), apwin.com (Colombia). Elo: ClubElo real para los 70 equipos del universo (clubelo.com, sin regresiones). Liga Colombiana no disponible en The Odds API: cuotas h2h y O/U 2.5 tomadas del agregador football-predictions.ai (Pinnacle/best, Capa 3). Mercados sin cuota capturada (1.5 goles, BTTS, DO, DNB, córners, tarjetas): n/d, nunca inventados. Córners/tarjetas: tasas de ambos equipos no disponibles (sin librería corners/cards para 20-sep); los 8 campos quedan `null` y se documenta 'corners/cards no disponibles' -> mercados no disponibles, nunca omitidos silenciosamente.
- **Bournemouth vs Liverpool, Leeds United vs Crystal Palace, Manchester City vs Sunderland, Fulham vs Manchester United** (Premier League) — 4 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Bayer Leverkusen vs RB Leipzig, FC Schalke 04 vs SV Elversberg, SC Paderborn vs TSG Hoffenheim** (Bundesliga) — 3 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Getafe vs Malaga, Atletico Madrid vs Real Madrid, Deportivo La Coruna vs Real Betis, Villarreal vs Levante, Valencia vs Real Sociedad** (La Liga) — 5 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Fiorentina vs Napoli, Frosinone vs Como, Parma vs Genoa, Juventus vs Atalanta, AC Milan vs Lecce** (Serie A) — 5 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Auxerre vs Brest, Nice vs Lille, Marseille vs Paris Saint-Germain** (Ligue 1) — 3 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Feyenoord vs FC Utrecht, AZ Alkmaar vs SC Telstar, FC Twente vs PSV Eindhoven, NEC Nijmegen vs Go Ahead Eagles** (Eredivisie) — 4 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Estrela da Amadora vs Academico de Viseu, Vitoria SC vs Moreirense, Santa Clara vs Braga, Estoril vs Casa Pia, FC Porto vs Benfica** (Primeira Liga) — 5 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Inter Miami vs San Diego FC** (MLS) — 1 partido — cuotas 1X2 y totals (2.5/3.5).
- **San Lorenzo vs Boca Juniors, Rosario Central vs Argentinos Juniors, Platense vs Newell's Old Boys, Belgrano de Cordoba vs Estudiantes de Rio Cuarto** (Liga Argentina) — 4 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Fortaleza CEIF vs Atletico Junior** (Liga Colombiana) — 1 partido — cuotas 1X2 (Capa 3) y O/U 2.5.

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Auxerre vs Brest | over_2_5 | Over 2.5 Goles | prioritario | 1.83 | 85.2% | 1.17 | +55.92% | +55.92% | +46.77% | 0.17u | Media-Alta |
| 2 | Fulham vs Manchester United | over_2_5 | Over 2.5 Goles | prioritario | 1.54 | 83.3% | 1.20 | +28.34% | +28.34% | +20.64% | 0.13u | Media-Alta |
| 3 | Leeds United vs Crystal Palace | over_2_5 | Over 2.5 Goles | prioritario | 1.70 | 82.2% | 1.22 | +39.74% | +39.74% | +31.24% | 0.14u | Media-Alta |
| 4 | FC Schalke 04 vs SV Elversberg | over_3_5 | Over 3.5 Goles | excluido | 2.35 | 81.6% | 1.23 | +91.76% | +91.76% | +80.01% | 0.17u | Media-Alta |
| 5 | Atletico Madrid vs Real Madrid | over_3_5 | Over 3.5 Goles | prioritario | 2.10 | 80.0% | 1.25 | +67.92% | +67.92% | +57.42% | 0.15u | Media-Alta |
| 6 | Villarreal vs Levante | over_3_5 | Over 3.5 Goles | excluido | 2.25 | 79.0% | 1.27 | +77.84% | +77.84% | +66.59% | 0.16u | Media-Alta |
| 7 | NEC Nijmegen vs Go Ahead Eagles | over_3_5 | Over 3.5 Goles | prioritario | 1.88 | 78.5% | 1.27 | +47.58% | +47.58% | +38.18% | 0.14u | Media-Alta |
| 8 | FC Porto vs Benfica | over_2_5 | Over 2.5 Goles | prioritario | 1.87 | 77.9% | 1.28 | +45.62% | +45.62% | +36.27% | 0.13u | Media-Alta |
| 9 | Fiorentina vs Napoli | over_2_5 | Over 2.5 Goles | prioritario | 1.85 | 77.9% | 1.28 | +44.04% | +44.04% | +34.79% | 0.13u | Media-Alta |
| 10 | Manchester City vs Sunderland | over_2_5 | Over 2.5 Goles | prioritario | 1.57 | 77.5% | 1.29 | +21.75% | +21.75% | +13.90% | 0.10u | Media-Alta |
| 11 | AC Milan vs Lecce | over_2_5 | Over 2.5 Goles | prioritario | 1.62 | 75.2% | 1.33 | +21.79% | +21.79% | +13.69% | 0.09u | Media-Alta |
| 12 | AZ Alkmaar vs SC Telstar | over_3_5 | Over 3.5 Goles | prioritario | 1.71 | 74.2% | 1.35 | +26.95% | +26.95% | +18.40% | 0.09u | Media-Alta |
| 13 | Deportivo La Coruna vs Real Betis | over_2_5 | Over 2.5 Goles | prioritario | 1.83 | 73.9% | 1.35 | +35.29% | +35.29% | +26.14% | 0.11u | Media-Alta |
| 14 | Juventus vs Atalanta | 1 | Victoria Juventus | prioritario | 1.72 | 73.0% | 1.37 | +25.53% | +25.53% | +16.93% | 0.09u | Media-Alta |
| 15 | Getafe vs Malaga | over_1_5 | Over 1.5 Goles | prioritario | 1.57 | 72.5% | 1.38 | +13.90% | +13.90% | +6.05% | 0.06u | Media-Alta |
| 16 | Valencia vs Real Sociedad | over_2_5 | Over 2.5 Goles | prioritario | 1.95 | 72.2% | 1.38 | +40.89% | +40.89% | +31.14% | 0.11u | Media-Alta |
| 17 | Fulham vs Manchester United | over_3_5 | Over 3.5 Goles | excluido | 2.35 | 72.1% | 1.39 | +69.39% | +69.39% | +57.64% | 0.13u | Media-Alta |
| 18 | Estrela da Amadora vs Academico de Viseu | over_2_5 | Over 2.5 Goles | prioritario | 2.05 | 71.0% | 1.41 | +45.53% | +45.53% | +35.28% | 0.11u | Media-Alta |
| 19 | Rosario Central vs Argentinos Juniors | over_1_5 | Over 1.5 Goles | excluido | 1.50 | 69.8% | 1.43 | +4.74% | +4.74% | -2.75% | 0.02u | Media-Alta |
| 20 | FC Twente vs PSV Eindhoven | over_3_5 | Over 3.5 Goles | prioritario | 1.73 | 69.7% | 1.43 | +20.65% | +20.65% | +12.00% | 0.07u | Media-Alta |
| 21 | Vitoria SC vs Moreirense | 1 | Victoria Vitoria SC | excluido | 1.53 | 67.5% | 1.48 | +3.34% | +3.34% | -4.31% | 0.02u | Media-Alta |
| 22 | Bayer Leverkusen vs RB Leipzig | over_3_5 | Over 3.5 Goles | prioritario | 1.88 | 66.5% | 1.50 | +25.00% | +25.00% | +15.60% | 0.07u | Media-Alta |
| 23 | Feyenoord vs FC Utrecht | over_3_5 | Over 3.5 Goles | prioritario | 1.78 | 66.0% | 1.51 | +17.50% | +17.50% | +8.60% | 0.06u | Media-Alta |
| 24 | Vitoria SC vs Moreirense | over_2_5 | Over 2.5 Goles | prioritario | 1.93 | 64.1% | 1.56 | +23.81% | +23.81% | +14.16% | 0.06u | Media-Alta |
| 25 | Nice vs Lille | over_2_5 | Over 2.5 Goles | prioritario | 1.93 | 63.7% | 1.57 | +22.96% | +22.96% | +13.31% | 0.06u | Media-Alta |
| 26 | Bournemouth vs Liverpool | over_3_5 | Over 3.5 Goles | prioritario | 2.16 | 62.7% | 1.60 | +35.37% | +35.37% | +24.57% | 0.08u | Media-Alta |
| 27 | Frosinone vs Como | over_3_5 | Over 3.5 Goles | prioritario | 2.10 | 60.3% | 1.66 | +26.65% | +26.65% | +16.15% | 0.06u | Media-Alta |
| 28 | Auxerre vs Brest | 2 | Victoria Brest | excluido | 2.47 | 58.4% | 1.71 | +44.32% | +44.32% | +31.97% | 0.08u | Media-Alta |
| 29 | Atletico Madrid vs Real Madrid | 2 | Victoria Real Madrid | prioritario | 2.02 | 58.2% | 1.72 | +17.66% | +17.66% | +7.56% | 0.04u | Media-Alta |
| 30 | Getafe vs Malaga | 1 | Victoria Getafe | prioritario | 2.06 | 57.5% | 1.74 | +18.53% | +18.53% | +8.23% | 0.04u | Media |
| 31 | Juventus vs Atalanta | over_2_5 | Over 2.5 Goles | excluido | 1.89 | 56.9% | 1.76 | +7.58% | +7.58% | -1.87% | 0.02u | Media |
| 32 | Estoril vs Casa Pia | over_2_5 | Over 2.5 Goles | excluido | 1.89 | 56.4% | 1.77 | +6.65% | +6.65% | -2.80% | 0.02u | Media |
| 33 | Deportivo La Coruna vs Real Betis | 2 | Victoria Real Betis | excluido | 2.05 | 52.6% | 1.90 | +7.83% | +7.83% | -2.42% | 0.02u | Media |
| 34 | Parma vs Genoa | over_2_5 | Over 2.5 Goles | excluido | 2.45 | 52.4% | 1.91 | +28.38% | +28.38% | +16.13% | 0.05u | Media |
| 35 | Fulham vs Manchester United | 2 | Victoria Manchester United | excluido | 2.05 | 52.0% | 1.92 | +6.54% | +6.54% | -3.71% | 0.02u | Media |
| 36 | Belgrano de Cordoba vs Estudiantes de Rio Cuarto | over_2_5 | Over 2.5 Goles | excluido | 2.30 | 51.8% | 1.93 | +19.23% | +19.23% | +7.73% | 0.04u | Media |
| 37 | SC Paderborn vs TSG Hoffenheim | over_3_5 | Over 3.5 Goles | excluido | 2.10 | 51.5% | 1.94 | +8.23% | +8.23% | -2.27% | 0.02u | Media |
| 38 | Estrela da Amadora vs Academico de Viseu | 1 | Victoria Estrela da Amadora | excluido | 2.20 | 51.0% | 1.96 | +12.29% | +12.29% | +1.29% | 0.03u | Media |
| 39 | San Lorenzo vs Boca Juniors | 2 | Victoria Boca Juniors | excluido | 2.10 | 50.2% | 1.99 | +5.40% | +5.40% | -5.10% | 0.01u | Media |
| 40 | FC Schalke 04 vs SV Elversberg | 2 | Victoria SV Elversberg | excepcional | 3.55 | 49.9% | 2.01 | +77.00% | +77.00% | +59.25% | 0.08u | Baja |
| 41 | FC Porto vs Benfica | 2 | Victoria Benfica | excluido | 2.54 | 49.7% | 2.01 | +26.21% | +26.21% | +13.51% | 0.04u | Baja |
| 42 | Platense vs Newell's Old Boys | over_2_5 | Over 2.5 Goles | excluido | 2.45 | 48.0% | 2.08 | +17.55% | +17.55% | +5.30% | 0.03u | Baja |
| 43 | Santa Clara vs Braga | over_2_5 | Over 2.5 Goles | excluido | 2.45 | 45.7% | 2.19 | +11.99% | +11.99% | -0.26% | 0.02u | Baja |
| 44 | San Lorenzo vs Boca Juniors | over_2_5 | Over 2.5 Goles | excluido | 2.50 | 44.2% | 2.26 | +10.42% | +10.42% | -2.08% | 0.02u | Baja |
| 45 | Nice vs Lille | 1 | Victoria Nice | excepcional | 3.76 | 42.9% | 2.33 | +61.38% | +61.38% | +42.58% | 0.06u | Baja |
| 46 | FC Twente vs PSV Eindhoven | 1 | Victoria FC Twente | excepcional | 3.00 | 42.8% | 2.34 | +28.34% | +28.34% | +13.34% | 0.04u | Baja |
| 47 | Fiorentina vs Napoli | 1 | Victoria Fiorentina | excepcional | 3.22 | 42.3% | 2.36 | +36.30% | +36.30% | +20.20% | 0.04u | Baja |
| 48 | Fortaleza CEIF vs Atletico Junior | 2 | Victoria Atletico Junior | excluido | 2.52 | 42.3% | 2.36 | +6.60% | +6.60% | -6.00% | 0.01u | Baja |
| 49 | Valencia vs Real Sociedad | 1 | Victoria Valencia | excluido | 2.80 | 40.5% | 2.47 | +13.34% | +13.34% | -0.66% | 0.02u | Baja |
| 50 | Bournemouth vs Liverpool | 1 | Victoria Bournemouth | excluido | 3.20 | 38.0% | 2.63 | +21.66% | +21.66% | +5.66% | 0.02u | Baja |
| 51 | Rosario Central vs Argentinos Juniors | 2 | Victoria Argentinos Juniors | excepcional | 3.46 | 37.9% | 2.64 | +31.03% | +31.03% | +13.73% | 0.03u | Baja |
| 52 | Parma vs Genoa | 1 | Victoria Parma | excluido | 3.19 | 32.9% | 3.04 | +5.08% | +5.08% | -10.87% | 0.01u | Baja |
| 53 | Inter Miami vs San Diego FC | 2 | Victoria San Diego FC | excepcional | 6.50 | 31.7% | 3.15 | +106.12% | +106.12% | +73.62% | 0.05u | Baja |
| 54 | Santa Clara vs Braga | 1 | Victoria Santa Clara | excluido | 3.60 | 31.7% | 3.16 | +13.98% | +13.98% | -4.02% | 0.01u | Baja |
| 55 | Leeds United vs Crystal Palace | 2 | Victoria Crystal Palace | excepcional | 5.10 | 31.6% | 3.16 | +61.31% | +61.31% | +35.81% | 0.04u | Baja |
| 56 | Villarreal vs Levante | 2 | Victoria Levante | excepcional | 6.10 | 30.2% | 3.31 | +84.04% | +84.04% | +53.54% | 0.04u | Baja |
| 57 | Marseille vs Paris Saint-Germain | 1 | Victoria Marseille | excluido | 7.50 | 28.4% | 3.52 | +113.30% | +113.30% | +75.80% | 0.04u | Baja |
| 58 | Platense vs Newell's Old Boys | 2 | Victoria Newell's Old Boys | excluido | 3.87 | 28.3% | 3.53 | +9.60% | +9.60% | -9.75% | 0.01u | Baja |
| 59 | Estoril vs Casa Pia | X | Empate | excluido | 3.80 | 27.1% | 3.69 | +3.09% | +3.09% | -15.91% | 0.00u | Baja |
| 60 | Belgrano de Cordoba vs Estudiantes de Rio Cuarto | X | Empate | excluido | 4.35 | 26.8% | 3.73 | +16.67% | +16.67% | -5.08% | 0.01u | Baja |
| 61 | Estoril vs Casa Pia | 2 | Victoria Casa Pia | excluido | 4.70 | 26.2% | 3.82 | +23.09% | +23.09% | -0.41% | 0.02u | Baja |
| 62 | Marseille vs Paris Saint-Germain | X | Empate | excluido | 5.55 | 25.4% | 3.93 | +41.19% | +41.19% | +13.44% | 0.02u | Baja |
| 63 | SC Paderborn vs TSG Hoffenheim | X | Empate | excluido | 4.49 | 25.2% | 3.96 | +13.37% | +13.37% | -9.08% | 0.01u | Baja |
| 64 | SC Paderborn vs TSG Hoffenheim | 1 | Victoria SC Paderborn | excluido | 4.47 | 24.4% | 4.10 | +9.02% | +9.02% | -13.33% | 0.01u | Baja |
| 65 | Frosinone vs Como | X | Empate | excluido | 4.70 | 23.4% | 4.27 | +10.03% | +10.03% | -13.47% | 0.01u | Baja |
| 66 | Inter Miami vs San Diego FC | X | Empate | excluido | 5.50 | 22.7% | 4.40 | +25.07% | +25.07% | -2.43% | 0.01u | Baja |
| 67 | AC Milan vs Lecce | X | Empate | excluido | 6.00 | 21.4% | 4.67 | +28.52% | +28.52% | -1.48% | 0.01u | Baja |
| 68 | Manchester City vs Sunderland | X | Empate | excluido | 5.65 | 21.2% | 4.72 | +19.78% | +19.78% | -8.47% | 0.01u | Baja |
| 69 | Feyenoord vs FC Utrecht | X | Empate | excluido | 6.57 | 20.6% | 4.84 | +35.67% | +35.67% | +2.82% | 0.02u | Baja |
| 70 | Belgrano de Cordoba vs Estudiantes de Rio Cuarto | 2 | Victoria Estudiantes de Rio Cuarto | excluido | 8.50 | 20.1% | 4.97 | +71.02% | +71.02% | +28.52% | 0.02u | Baja |
| 71 | Frosinone vs Como | 1 | Victoria Frosinone | excluido | 6.75 | 19.8% | 5.04 | +33.92% | +33.92% | +0.17% | 0.01u | Baja |
| 72 | Manchester City vs Sunderland | 2 | Victoria Sunderland | excluido | 9.50 | 18.7% | 5.35 | +77.46% | +77.46% | +29.96% | 0.02u | Baja |
| 73 | Feyenoord vs FC Utrecht | 2 | Victoria FC Utrecht | excluido | 9.40 | 16.6% | 6.02 | +56.13% | +56.13% | +9.13% | 0.02u | Baja |
| 74 | AC Milan vs Lecce | 2 | Victoria Lecce | excluido | 12.50 | 16.4% | 6.11 | +104.63% | +104.63% | +42.13% | 0.02u | Baja |
| 75 | AZ Alkmaar vs SC Telstar | X | Empate | excluido | 7.05 | 15.5% | 6.45 | +9.27% | +9.27% | -25.98% | 0.00u | Baja |

## Evaluación Over/Under por Partido
Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada (n/d = cuota no disponible en la corrida).
| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |
|---|---|---|---:|---:|---:|---:|---:|---|
| Bournemouth vs Liverpool | 1.5 | 84.5% | n/d | n/d | 15.5% | n/d | n/d | Cuotas no capturadas |
| Bournemouth vs Liverpool | 2.5 | 77.7% | n/d | n/d | 22.3% | n/d | n/d | Cuotas no capturadas |
| Bournemouth vs Liverpool | 3.5 | 62.7% | 2.16 | +35.37% | 37.3% | 1.72 | -35.79% | Value Over |
| Leeds United vs Crystal Palace | 1.5 | 87.2% | n/d | n/d | 12.8% | n/d | n/d | Cuotas no capturadas |
| Leeds United vs Crystal Palace | 2.5 | 82.2% | 1.70 | +39.74% | 17.8% | 2.30 | -59.06% | Value Over |
| Leeds United vs Crystal Palace | 3.5 | 70.2% | n/d | n/d | 29.8% | n/d | n/d | Cuotas no capturadas |
| Manchester City vs Sunderland | 1.5 | 84.4% | n/d | n/d | 15.6% | n/d | n/d | Cuotas no capturadas |
| Manchester City vs Sunderland | 2.5 | 77.5% | 1.57 | +21.75% | 22.4% | 2.35 | -47.24% | Value Over |
| Manchester City vs Sunderland | 3.5 | 62.5% | n/d | n/d | 37.5% | n/d | n/d | Cuotas no capturadas |
| Fulham vs Manchester United | 1.5 | 87.9% | n/d | n/d | 12.1% | n/d | n/d | Cuotas no capturadas |
| Fulham vs Manchester United | 2.5 | 83.3% | 1.54 | +28.34% | 16.7% | 2.30 | -61.68% | Value Over |
| Fulham vs Manchester United | 3.5 | 72.1% | 2.35 | +69.39% | 27.9% | 1.57 | -56.17% | Value Over |
| Bayer Leverkusen vs RB Leipzig | 1.5 | 85.9% | n/d | n/d | 14.1% | n/d | n/d | Cuotas no capturadas |
| Bayer Leverkusen vs RB Leipzig | 2.5 | 80.0% | n/d | n/d | 20.0% | n/d | n/d | Cuotas no capturadas |
| Bayer Leverkusen vs RB Leipzig | 3.5 | 66.5% | 1.88 | +25.00% | 33.5% | 1.95 | -34.66% | Value Over |
| FC Schalke 04 vs SV Elversberg | 1.5 | 91.4% | n/d | n/d | 8.6% | n/d | n/d | Cuotas no capturadas |
| FC Schalke 04 vs SV Elversberg | 2.5 | 88.9% | n/d | n/d | 11.1% | n/d | n/d | Cuotas no capturadas |
| FC Schalke 04 vs SV Elversberg | 3.5 | 81.6% | 2.35 | +91.76% | 18.4% | 1.61 | -70.38% | Value Over |
| SC Paderborn vs TSG Hoffenheim | 1.5 | 80.3% | n/d | n/d | 19.7% | n/d | n/d | Cuotas no capturadas |
| SC Paderborn vs TSG Hoffenheim | 2.5 | 70.5% | n/d | n/d | 29.5% | n/d | n/d | Cuotas no capturadas |
| SC Paderborn vs TSG Hoffenheim | 3.5 | 51.5% | 2.10 | +8.23% | 48.5% | 1.79 | -13.26% | Value Over |
| Fiorentina vs Napoli | 1.5 | 84.6% | n/d | n/d | 15.4% | n/d | n/d | Cuotas no capturadas |
| Fiorentina vs Napoli | 2.5 | 77.9% | 1.85 | +44.04% | 22.1% | 2.05 | -54.61% | Value Over |
| Fiorentina vs Napoli | 3.5 | 63.0% | n/d | n/d | 37.0% | n/d | n/d | Cuotas no capturadas |
| Frosinone vs Como | 1.5 | 83.6% | n/d | n/d | 16.4% | n/d | n/d | Cuotas no capturadas |
| Frosinone vs Como | 2.5 | 76.2% | n/d | n/d | 23.8% | n/d | n/d | Cuotas no capturadas |
| Frosinone vs Como | 3.5 | 60.3% | 2.10 | +26.65% | 39.7% | 1.71 | -32.13% | Value Over |
| Parma vs Genoa | 1.5 | 69.7% | n/d | n/d | 30.3% | n/d | n/d | Cuotas no capturadas |
| Parma vs Genoa | 2.5 | 52.4% | 2.45 | +28.38% | 47.6% | 1.51 | -28.12% | Value Over |
| Parma vs Genoa | 3.5 | 28.4% | n/d | n/d | 71.6% | n/d | n/d | Cuotas no capturadas |
| Juventus vs Atalanta | 1.5 | 72.2% | n/d | n/d | 27.8% | n/d | n/d | Cuotas no capturadas |
| Juventus vs Atalanta | 2.5 | 56.9% | 1.89 | +7.58% | 43.1% | 2.02 | -12.98% | Value Over |
| Juventus vs Atalanta | 3.5 | 33.5% | n/d | n/d | 66.5% | n/d | n/d | Cuotas no capturadas |
| AC Milan vs Lecce | 1.5 | 83.0% | n/d | n/d | 17.0% | n/d | n/d | Cuotas no capturadas |
| AC Milan vs Lecce | 2.5 | 75.2% | 1.62 | +21.79% | 24.8% | 2.33 | -42.17% | Value Over |
| AC Milan vs Lecce | 3.5 | 58.7% | n/d | n/d | 41.3% | n/d | n/d | Cuotas no capturadas |
| Getafe vs Malaga | 1.5 | 72.5% | 1.57 | +13.90% | 27.5% | 2.40 | -34.12% | Value Over |
| Getafe vs Malaga | 2.5 | 57.3% | n/d | n/d | 42.7% | n/d | n/d | Cuotas no capturadas |
| Getafe vs Malaga | 3.5 | 33.9% | n/d | n/d | 66.1% | n/d | n/d | Cuotas no capturadas |
| Atletico Madrid vs Real Madrid | 1.5 | 90.8% | n/d | n/d | 9.2% | n/d | n/d | Cuotas no capturadas |
| Atletico Madrid vs Real Madrid | 2.5 | 87.9% | n/d | n/d | 12.0% | n/d | n/d | Cuotas no capturadas |
| Atletico Madrid vs Real Madrid | 3.5 | 80.0% | 2.10 | +67.92% | 20.0% | 1.71 | -65.73% | Value Over |
| Deportivo La Coruna vs Real Betis | 1.5 | 82.3% | n/d | n/d | 17.7% | n/d | n/d | Cuotas no capturadas |
| Deportivo La Coruna vs Real Betis | 2.5 | 73.9% | 1.83 | +35.29% | 26.1% | 2.02 | -47.34% | Value Over |
| Deportivo La Coruna vs Real Betis | 3.5 | 56.8% | n/d | n/d | 43.2% | n/d | n/d | Cuotas no capturadas |
| Villarreal vs Levante | 1.5 | 90.4% | n/d | n/d | 9.6% | n/d | n/d | Cuotas no capturadas |
| Villarreal vs Levante | 2.5 | 87.4% | n/d | n/d | 12.6% | n/d | n/d | Cuotas no capturadas |
| Villarreal vs Levante | 3.5 | 79.0% | 2.25 | +77.84% | 21.0% | 1.62 | -66.04% | Value Over |
| Valencia vs Real Sociedad | 1.5 | 81.3% | n/d | n/d | 18.7% | n/d | n/d | Cuotas no capturadas |
| Valencia vs Real Sociedad | 2.5 | 72.2% | 1.95 | +40.89% | 27.8% | 1.88 | -47.83% | Value Over |
| Valencia vs Real Sociedad | 3.5 | 54.2% | n/d | n/d | 45.8% | n/d | n/d | Cuotas no capturadas |
| Auxerre vs Brest | 1.5 | 89.0% | n/d | n/d | 11.0% | n/d | n/d | Cuotas no capturadas |
| Auxerre vs Brest | 2.5 | 85.2% | 1.83 | +55.92% | 14.8% | 2.07 | -69.36% | Value Over |
| Auxerre vs Brest | 3.5 | 75.2% | n/d | n/d | 24.8% | n/d | n/d | Cuotas no capturadas |
| Nice vs Lille | 1.5 | 76.4% | n/d | n/d | 23.6% | n/d | n/d | Cuotas no capturadas |
| Nice vs Lille | 2.5 | 63.7% | 1.93 | +22.96% | 36.3% | 1.89 | -31.41% | Value Over |
| Nice vs Lille | 3.5 | 42.0% | n/d | n/d | 58.0% | n/d | n/d | Cuotas no capturadas |
| Marseille vs Paris Saint-Germain | 1.5 | 78.6% | n/d | n/d | 21.4% | n/d | n/d | Cuotas no capturadas |
| Marseille vs Paris Saint-Germain | 2.5 | 67.5% | n/d | n/d | 32.5% | n/d | n/d | Cuotas no capturadas |
| Marseille vs Paris Saint-Germain | 3.5 | 47.2% | 1.95 | -7.88% | 52.8% | 1.89 | -0.28% | Sin value |
| Feyenoord vs FC Utrecht | 1.5 | 85.7% | n/d | n/d | 14.3% | n/d | n/d | Cuotas no capturadas |
| Feyenoord vs FC Utrecht | 2.5 | 79.7% | n/d | n/d | 20.3% | n/d | n/d | Cuotas no capturadas |
| Feyenoord vs FC Utrecht | 3.5 | 66.0% | 1.78 | +17.50% | 34.0% | 2.05 | -30.32% | Value Over |
| AZ Alkmaar vs SC Telstar | 1.5 | 88.5% | n/d | n/d | 11.5% | n/d | n/d | Cuotas no capturadas |
| AZ Alkmaar vs SC Telstar | 2.5 | 84.6% | n/d | n/d | 15.4% | n/d | n/d | Cuotas no capturadas |
| AZ Alkmaar vs SC Telstar | 3.5 | 74.2% | 1.71 | +26.95% | 25.8% | 2.16 | -44.36% | Value Over |
| FC Twente vs PSV Eindhoven | 1.5 | 87.0% | n/d | n/d | 13.0% | n/d | n/d | Cuotas no capturadas |
| FC Twente vs PSV Eindhoven | 2.5 | 82.0% | n/d | n/d | 18.1% | n/d | n/d | Cuotas no capturadas |
| FC Twente vs PSV Eindhoven | 3.5 | 69.7% | 1.73 | +20.65% | 30.3% | 2.10 | -36.45% | Value Over |
| NEC Nijmegen vs Go Ahead Eagles | 1.5 | 90.2% | n/d | n/d | 9.8% | n/d | n/d | Cuotas no capturadas |
| NEC Nijmegen vs Go Ahead Eagles | 2.5 | 87.1% | n/d | n/d | 12.9% | n/d | n/d | Cuotas no capturadas |
| NEC Nijmegen vs Go Ahead Eagles | 3.5 | 78.5% | 1.88 | +47.58% | 21.5% | 1.95 | -58.07% | Value Over |
| Estrela da Amadora vs Academico de Viseu | 1.5 | 80.6% | n/d | n/d | 19.4% | n/d | n/d | Cuotas no capturadas |
| Estrela da Amadora vs Academico de Viseu | 2.5 | 71.0% | 2.05 | +45.53% | 29.0% | 1.74 | -49.52% | Value Over |
| Estrela da Amadora vs Academico de Viseu | 3.5 | 52.3% | n/d | n/d | 47.7% | n/d | n/d | Cuotas no capturadas |
| Vitoria SC vs Moreirense | 1.5 | 76.5% | n/d | n/d | 23.5% | n/d | n/d | Cuotas no capturadas |
| Vitoria SC vs Moreirense | 2.5 | 64.1% | 1.93 | +23.81% | 35.9% | 1.89 | -32.24% | Value Over |
| Vitoria SC vs Moreirense | 3.5 | 42.6% | n/d | n/d | 57.4% | n/d | n/d | Cuotas no capturadas |
| Santa Clara vs Braga | 1.5 | 65.6% | n/d | n/d | 34.4% | n/d | n/d | Cuotas no capturadas |
| Santa Clara vs Braga | 2.5 | 45.7% | 2.45 | +11.99% | 54.3% | 1.55 | -15.85% | Value Over |
| Santa Clara vs Braga | 3.5 | 21.8% | n/d | n/d | 78.2% | n/d | n/d | Cuotas no capturadas |
| Estoril vs Casa Pia | 1.5 | 72.1% | n/d | n/d | 27.9% | n/d | n/d | Cuotas no capturadas |
| Estoril vs Casa Pia | 2.5 | 56.4% | 1.89 | +6.65% | 43.6% | 1.93 | -15.91% | Value Over |
| Estoril vs Casa Pia | 3.5 | 32.9% | n/d | n/d | 67.1% | n/d | n/d | Cuotas no capturadas |
| FC Porto vs Benfica | 1.5 | 84.6% | n/d | n/d | 15.4% | n/d | n/d | Cuotas no capturadas |
| FC Porto vs Benfica | 2.5 | 77.9% | 1.87 | +45.62% | 22.1% | 1.95 | -56.85% | Value Over |
| FC Porto vs Benfica | 3.5 | 63.0% | n/d | n/d | 37.0% | n/d | n/d | Cuotas no capturadas |
| Inter Miami vs San Diego FC | 1.5 | 86.0% | n/d | n/d | 14.0% | n/d | n/d | Cuotas no capturadas |
| Inter Miami vs San Diego FC | 2.5 | 80.3% | n/d | n/d | 19.7% | n/d | n/d | Cuotas no capturadas |
| Inter Miami vs San Diego FC | 3.5 | 67.0% | n/d | n/d | 33.0% | n/d | n/d | Cuotas no capturadas |
| San Lorenzo vs Boca Juniors | 1.5 | 64.6% | 1.50 | -3.09% | 35.4% | 2.40 | -15.06% | Sin value |
| San Lorenzo vs Boca Juniors | 2.5 | 44.2% | 2.50 | +10.42% | 55.8% | 1.49 | -16.81% | Value Over |
| San Lorenzo vs Boca Juniors | 3.5 | 20.4% | n/d | n/d | 79.6% | n/d | n/d | Cuotas no capturadas |
| Rosario Central vs Argentinos Juniors | 1.5 | 69.8% | 1.50 | +4.74% | 30.2% | 2.48 | -25.18% | Value Over |
| Rosario Central vs Argentinos Juniors | 2.5 | 52.6% | n/d | n/d | 47.4% | n/d | n/d | Cuotas no capturadas |
| Rosario Central vs Argentinos Juniors | 3.5 | 28.6% | n/d | n/d | 71.4% | n/d | n/d | Cuotas no capturadas |
| Platense vs Newell's Old Boys | 1.5 | 67.0% | 1.50 | +0.49% | 33.0% | 2.40 | -20.78% | Sin value |
| Platense vs Newell's Old Boys | 2.5 | 48.0% | 2.45 | +17.55% | 52.0% | 1.50 | -21.97% | Value Over |
| Platense vs Newell's Old Boys | 3.5 | 23.9% | n/d | n/d | 76.1% | n/d | n/d | Cuotas no capturadas |
| Belgrano de Cordoba vs Estudiantes de Rio Cuarto | 1.5 | 69.3% | n/d | n/d | 30.7% | n/d | n/d | Cuotas no capturadas |
| Belgrano de Cordoba vs Estudiantes de Rio Cuarto | 2.5 | 51.8% | 2.30 | +19.23% | 48.2% | 1.60 | -22.94% | Value Over |
| Belgrano de Cordoba vs Estudiantes de Rio Cuarto | 3.5 | 27.8% | n/d | n/d | 72.2% | n/d | n/d | Cuotas no capturadas |
| Fortaleza CEIF vs Atletico Junior | 1.5 | 67.1% | n/d | n/d | 32.9% | n/d | n/d | Cuotas no capturadas |
| Fortaleza CEIF vs Atletico Junior | 2.5 | 48.2% | 2.10 | +1.14% | 51.8% | 1.80 | -6.69% | Sin value |
| Fortaleza CEIF vs Atletico Junior | 3.5 | 24.1% | n/d | n/d | 75.9% | n/d | n/d | Cuotas no capturadas |

## Picks Recomendados (Top 6)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Auxerre vs Brest | over_2_5 | Over 2.5 Goles | prioritario | 1.83 | 85.2% | 1.17 | +55.92% | +55.92% | +46.77% | 0.17u | Media-Alta |
| 2 | Fulham vs Manchester United | over_2_5 | Over 2.5 Goles | prioritario | 1.54 | 83.3% | 1.20 | +28.34% | +28.34% | +20.64% | 0.13u | Media-Alta |
| 3 | Leeds United vs Crystal Palace | over_2_5 | Over 2.5 Goles | prioritario | 1.70 | 82.2% | 1.22 | +39.74% | +39.74% | +31.24% | 0.14u | Media-Alta |
| 4 | Atletico Madrid vs Real Madrid | over_3_5 | Over 3.5 Goles | prioritario | 2.10 | 80.0% | 1.25 | +67.92% | +67.92% | +57.42% | 0.15u | Media-Alta |
| 5 | NEC Nijmegen vs Go Ahead Eagles | over_3_5 | Over 3.5 Goles | prioritario | 1.88 | 78.5% | 1.27 | +47.58% | +47.58% | +38.18% | 0.14u | Media-Alta |
| 6 | FC Porto vs Benfica | over_2_5 | Over 2.5 Goles | prioritario | 1.87 | 77.9% | 1.28 | +45.62% | +45.62% | +36.27% | 0.13u | Media-Alta |

## Detalle de Picks
### Pick 1: Auxerre vs Brest
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.83
- **Probabilidad modelo:** 85.2%
- **Probabilidad conservadora:** 80.2%
- **Probabilidad implícita:** 54.6%
- **Cuota justa:** 1.17
- **Edge:** +55.92%
- **EV:** +55.92%
- **EV robusto:** +46.77%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.25
- **Stake:** 0.17u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 2: Fulham vs Manchester United
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.54
- **Probabilidad modelo:** 83.3%
- **Probabilidad conservadora:** 78.3%
- **Probabilidad implícita:** 64.9%
- **Cuota justa:** 1.20
- **Edge:** +28.34%
- **EV:** +28.34%
- **EV robusto:** +20.64%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.28
- **Stake:** 0.13u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 3: Leeds United vs Crystal Palace
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.70
- **Probabilidad modelo:** 82.2%
- **Probabilidad conservadora:** 77.2%
- **Probabilidad implícita:** 58.8%
- **Cuota justa:** 1.22
- **Edge:** +39.74%
- **EV:** +39.74%
- **EV robusto:** +31.24%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.30
- **Stake:** 0.14u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 4: Atletico Madrid vs Real Madrid
- **Mercado:** over_3_5
- **Selección:** Over 3.5 Goles
- **Cuota:** 2.10
- **Probabilidad modelo:** 80.0%
- **Probabilidad conservadora:** 75.0%
- **Probabilidad implícita:** 47.6%
- **Cuota justa:** 1.25
- **Edge:** +67.92%
- **EV:** +67.92%
- **EV robusto:** +57.42%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.33
- **Stake:** 0.15u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 5: NEC Nijmegen vs Go Ahead Eagles
- **Mercado:** over_3_5
- **Selección:** Over 3.5 Goles
- **Cuota:** 1.88
- **Probabilidad modelo:** 78.5%
- **Probabilidad conservadora:** 73.5%
- **Probabilidad implícita:** 53.2%
- **Cuota justa:** 1.27
- **Edge:** +47.58%
- **EV:** +47.58%
- **EV robusto:** +38.18%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.36
- **Stake:** 0.14u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 6: FC Porto vs Benfica
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.87
- **Probabilidad modelo:** 77.9%
- **Probabilidad conservadora:** 72.9%
- **Probabilidad implícita:** 53.5%
- **Cuota justa:** 1.28
- **Edge:** +45.62%
- **EV:** +45.62%
- **EV robusto:** +36.27%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.37
- **Stake:** 0.13u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

## NO BET / Excluidos
- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**
  - Bournemouth vs Liverpool — Under 3.5 Goles (under_3_5): Prob modelo 37.3%, EV -35.79%, EV robusto -44.39% → sin value.
  - Leeds United vs Crystal Palace — Under 2.5 Goles (under_2_5): Prob modelo 17.8%, EV -59.06%, EV robusto -70.56% → sin value.
  - Manchester City vs Sunderland — Under 2.5 Goles (under_2_5): Prob modelo 22.4%, EV -47.24%, EV robusto -58.99% → sin value.
  - Fulham vs Manchester United — Under 2.5 Goles (under_2_5): Prob modelo 16.7%, EV -61.68%, EV robusto -73.18% → sin value.
  - Fulham vs Manchester United — Under 3.5 Goles (under_3_5): Prob modelo 27.9%, EV -56.17%, EV robusto -64.02% → sin value.
  - Bayer Leverkusen vs RB Leipzig — Under 3.5 Goles (under_3_5): Prob modelo 33.5%, EV -34.66%, EV robusto -44.41% → sin value.
  - FC Schalke 04 vs SV Elversberg — Under 3.5 Goles (under_3_5): Prob modelo 18.4%, EV -70.38%, EV robusto -78.43% → sin value.
  - SC Paderborn vs TSG Hoffenheim — Under 3.5 Goles (under_3_5): Prob modelo 48.5%, EV -13.26%, EV robusto -22.21% → sin value.
  - Fiorentina vs Napoli — Under 2.5 Goles (under_2_5): Prob modelo 22.1%, EV -54.61%, EV robusto -64.86% → sin value.
  - Frosinone vs Como — Under 3.5 Goles (under_3_5): Prob modelo 39.7%, EV -32.13%, EV robusto -40.68% → sin value.
  - Parma vs Genoa — Under 2.5 Goles (under_2_5): Prob modelo 47.6%, EV -28.12%, EV robusto -35.67% → sin value.
  - Juventus vs Atalanta — Under 2.5 Goles (under_2_5): Prob modelo 43.1%, EV -12.98%, EV robusto -23.08% → sin value.
  - AC Milan vs Lecce — Under 2.5 Goles (under_2_5): Prob modelo 24.8%, EV -42.17%, EV robusto -53.82% → sin value.
  - Getafe vs Malaga — Under 1.5 Goles (under_1_5): Prob modelo 27.5%, EV -34.12%, EV robusto -46.12% → sin value.
  - Atletico Madrid vs Real Madrid — Under 3.5 Goles (under_3_5): Prob modelo 20.0%, EV -65.73%, EV robusto -74.28% → sin value.
  - Deportivo La Coruna vs Real Betis — Under 2.5 Goles (under_2_5): Prob modelo 26.1%, EV -47.34%, EV robusto -57.44% → sin value.
  - Villarreal vs Levante — Under 3.5 Goles (under_3_5): Prob modelo 21.0%, EV -66.04%, EV robusto -74.14% → sin value.
  - Valencia vs Real Sociedad — Under 2.5 Goles (under_2_5): Prob modelo 27.8%, EV -47.83%, EV robusto -57.23% → sin value.
  - Auxerre vs Brest — Under 2.5 Goles (under_2_5): Prob modelo 14.8%, EV -69.36%, EV robusto -79.71% → sin value.
  - Nice vs Lille — Under 2.5 Goles (under_2_5): Prob modelo 36.3%, EV -31.41%, EV robusto -40.86% → sin value.
  - Marseille vs Paris Saint-Germain — Over 3.5 Goles (over_3_5): Prob modelo 47.2%, EV -7.88%, EV robusto -17.63% → sin value.
  - Marseille vs Paris Saint-Germain — Under 3.5 Goles (under_3_5): Prob modelo 52.8%, EV -0.28%, EV robusto -9.73% → sin value.
  - Feyenoord vs FC Utrecht — Under 3.5 Goles (under_3_5): Prob modelo 34.0%, EV -30.32%, EV robusto -40.57% → sin value.
  - AZ Alkmaar vs SC Telstar — Under 3.5 Goles (under_3_5): Prob modelo 25.8%, EV -44.36%, EV robusto -55.16% → sin value.
  - FC Twente vs PSV Eindhoven — Under 3.5 Goles (under_3_5): Prob modelo 30.3%, EV -36.45%, EV robusto -46.95% → sin value.
  - NEC Nijmegen vs Go Ahead Eagles — Under 3.5 Goles (under_3_5): Prob modelo 21.5%, EV -58.07%, EV robusto -67.83% → sin value.
  - Estrela da Amadora vs Academico de Viseu — Under 2.5 Goles (under_2_5): Prob modelo 29.0%, EV -49.52%, EV robusto -58.22% → sin value.
  - Vitoria SC vs Moreirense — Under 2.5 Goles (under_2_5): Prob modelo 35.9%, EV -32.24%, EV robusto -41.69% → sin value.
  - Santa Clara vs Braga — Under 2.5 Goles (under_2_5): Prob modelo 54.3%, EV -15.85%, EV robusto -23.60% → sin value.
  - Estoril vs Casa Pia — Under 2.5 Goles (under_2_5): Prob modelo 43.6%, EV -15.91%, EV robusto -25.56% → sin value.
  - FC Porto vs Benfica — Under 2.5 Goles (under_2_5): Prob modelo 22.1%, EV -56.85%, EV robusto -66.60% → sin value.
  - San Lorenzo vs Boca Juniors — Over 1.5 Goles (over_1_5): Prob modelo 64.6%, EV -3.09%, EV robusto -10.59% → sin value.
  - San Lorenzo vs Boca Juniors — Under 1.5 Goles (under_1_5): Prob modelo 35.4%, EV -15.06%, EV robusto -27.06% → sin value.
  - San Lorenzo vs Boca Juniors — Under 2.5 Goles (under_2_5): Prob modelo 55.8%, EV -16.81%, EV robusto -24.26% → sin value.
  - Rosario Central vs Argentinos Juniors — Under 1.5 Goles (under_1_5): Prob modelo 30.2%, EV -25.18%, EV robusto -37.58% → sin value.
  - Platense vs Newell's Old Boys — Over 1.5 Goles (over_1_5): Prob modelo 67.0%, EV +0.49%, EV robusto -7.01% → sin value.
  - Platense vs Newell's Old Boys — Under 1.5 Goles (under_1_5): Prob modelo 33.0%, EV -20.78%, EV robusto -32.78% → sin value.
  - Platense vs Newell's Old Boys — Under 2.5 Goles (under_2_5): Prob modelo 52.0%, EV -21.97%, EV robusto -29.47% → sin value.
  - Belgrano de Cordoba vs Estudiantes de Rio Cuarto — Under 2.5 Goles (under_2_5): Prob modelo 48.2%, EV -22.94%, EV robusto -30.94% → sin value.
  - Fortaleza CEIF vs Atletico Junior — Over 2.5 Goles (over_2_5): Prob modelo 48.2%, EV +1.14%, EV robusto -9.36% → sin value.
  - Fortaleza CEIF vs Atletico Junior — Under 2.5 Goles (under_2_5): Prob modelo 51.8%, EV -6.69%, EV robusto -15.69% → sin value.
- **Candidatos con value excluidos por probabilidad-primero:**
  - Bournemouth vs Liverpool: Victoria Bournemouth (1) EV +21.66% / EV rob +5.66% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Manchester City vs Sunderland: Empate (X) EV +19.78% / EV rob -8.47%, Victoria Sunderland (2) EV +77.46% / EV rob +29.96% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Fulham vs Manchester United: Victoria Manchester United (2) EV +6.54% / EV rob -3.71%, Over 3.5 Goles (over_3_5) EV +69.39% / EV rob +57.64% — No cumple los mínimos de selección probabilidad-primero.
  - FC Schalke 04 vs SV Elversberg: Over 3.5 Goles (over_3_5) EV +91.76% / EV rob +80.01%, Victoria SV Elversberg (2) EV +77.00% / EV rob +59.25% — No cumple los mínimos de selección probabilidad-primero.
  - SC Paderborn vs TSG Hoffenheim: Victoria SC Paderborn (1) EV +9.02% / EV rob -13.33%, Empate (X) EV +13.37% / EV rob -9.08%, Over 3.5 Goles (over_3_5) EV +8.23% / EV rob -2.27% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Frosinone vs Como: Victoria Frosinone (1) EV +33.92% / EV rob +0.17%, Empate (X) EV +10.03% / EV rob -13.47% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Parma vs Genoa: Victoria Parma (1) EV +5.08% / EV rob -10.87%, Over 2.5 Goles (over_2_5) EV +28.38% / EV rob +16.13% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Juventus vs Atalanta: Over 2.5 Goles (over_2_5) EV +7.58% / EV rob -1.87% — No cumple los mínimos de selección probabilidad-primero.
  - AC Milan vs Lecce: Empate (X) EV +28.52% / EV rob -1.48%, Victoria Lecce (2) EV +104.63% / EV rob +42.13% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Deportivo La Coruna vs Real Betis: Victoria Real Betis (2) EV +7.83% / EV rob -2.42% — No cumple los mínimos de selección probabilidad-primero.
  - Villarreal vs Levante: Over 3.5 Goles (over_3_5) EV +77.84% / EV rob +66.59%, Victoria Levante (2) EV +84.04% / EV rob +53.54% — No cumple los mínimos de selección probabilidad-primero.
  - Valencia vs Real Sociedad: Victoria Valencia (1) EV +13.34% / EV rob -0.66% — No cumple los mínimos de selección probabilidad-primero.
  - Auxerre vs Brest: Victoria Brest (2) EV +44.32% / EV rob +31.97% — No cumple los mínimos de selección probabilidad-primero.
  - Marseille vs Paris Saint-Germain: Victoria Marseille (1) EV +113.30% / EV rob +75.80%, Empate (X) EV +41.19% / EV rob +13.44% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Feyenoord vs FC Utrecht: Empate (X) EV +35.67% / EV rob +2.82%, Victoria FC Utrecht (2) EV +56.13% / EV rob +9.13% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - AZ Alkmaar vs SC Telstar: Empate (X) EV +9.27% / EV rob -25.98% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Estrela da Amadora vs Academico de Viseu: Victoria Estrela da Amadora (1) EV +12.29% / EV rob +1.29% — No cumple los mínimos de selección probabilidad-primero.
  - Vitoria SC vs Moreirense: Victoria Vitoria SC (1) EV +3.34% / EV rob -4.31% — No cumple los mínimos de selección probabilidad-primero.
  - Santa Clara vs Braga: Victoria Santa Clara (1) EV +13.98% / EV rob -4.02%, Over 2.5 Goles (over_2_5) EV +11.99% / EV rob -0.26% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Estoril vs Casa Pia: Empate (X) EV +3.09% / EV rob -15.91%, Victoria Casa Pia (2) EV +23.09% / EV rob -0.41%, Over 2.5 Goles (over_2_5) EV +6.65% / EV rob -2.80% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - FC Porto vs Benfica: Victoria Benfica (2) EV +26.21% / EV rob +13.51% — No cumple los mínimos de selección probabilidad-primero.
  - Inter Miami vs San Diego FC: Empate (X) EV +25.07% / EV rob -2.43%, Victoria San Diego FC (2) EV +106.12% / EV rob +73.62% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - San Lorenzo vs Boca Juniors: Victoria Boca Juniors (2) EV +5.40% / EV rob -5.10%, Over 2.5 Goles (over_2_5) EV +10.42% / EV rob -2.08% — No cumple los mínimos de selección probabilidad-primero.
  - Rosario Central vs Argentinos Juniors: Over 1.5 Goles (over_1_5) EV +4.74% / EV rob -2.75%, Victoria Argentinos Juniors (2) EV +31.03% / EV rob +13.73% — No cumple los mínimos de selección probabilidad-primero.
  - Platense vs Newell's Old Boys: Victoria Newell's Old Boys (2) EV +9.60% / EV rob -9.75%, Over 2.5 Goles (over_2_5) EV +17.55% / EV rob +5.30% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Belgrano de Cordoba vs Estudiantes de Rio Cuarto: Empate (X) EV +16.67% / EV rob -5.08%, Victoria Estudiantes de Rio Cuarto (2) EV +71.02% / EV rob +28.52%, Over 2.5 Goles (over_2_5) EV +19.23% / EV rob +7.73% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Fortaleza CEIF vs Atletico Junior: Victoria Atletico Junior (2) EV +6.60% / EV rob -6.00% — No cumple los mínimos de selección probabilidad-primero.
  - Leeds United vs Crystal Palace: Victoria Crystal Palace (2) EV +61.31% / EV rob +35.81% — Cuota alta admitida solo como excepción robusta.
  - Fiorentina vs Napoli: Victoria Fiorentina (1) EV +36.30% / EV rob +20.20% — Cuota alta admitida solo como excepción robusta.
  - Nice vs Lille: Victoria Nice (1) EV +61.38% / EV rob +42.58% — Cuota alta admitida solo como excepción robusta.
  - FC Twente vs PSV Eindhoven: Victoria FC Twente (1) EV +28.34% / EV rob +13.34% — Cuota alta admitida solo como excepción robusta.

## Portfolio y Correlaciones
- **Exposición total:** 0.86u
- **Correlaciones detectadas:** Mercados presentes: over_2_5, over_3_5. Verificar solapamiento de mercado mismo partido.
- **Ajuste de stake por correlación:** Los picks pertenecen a partidos distintos; no se aplica reducción adicional por eventos dependientes.

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1 (Auxerre vs Brest - over_2_5) | PENDIENTE | — | — |
| Pick 2 (Fulham vs Manchester United - over_2_5) | PENDIENTE | — | — |
| Pick 3 (Leeds United vs Crystal Palace - over_2_5) | PENDIENTE | — | — |
| Pick 4 (Atletico Madrid vs Real Madrid - over_3_5) | PENDIENTE | — | — |
| Pick 5 (NEC Nijmegen vs Go Ahead Eagles - over_3_5) | PENDIENTE | — | — |
| Pick 6 (FC Porto vs Benfica - over_2_5) | PENDIENTE | — | — |
