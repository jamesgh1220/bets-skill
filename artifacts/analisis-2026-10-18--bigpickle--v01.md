# Análisis de Apuestas — 18 de octubre de 2026

## Metadatos
- **Fecha de análisis:** 2026-10-18T02:35:08+00:00
- **Fecha(s) de partido:** 18 de octubre de 2026
- **Information cutoff:** 2026-10-18T02:35:08+00:00
- **Modelo de IA:** bigpickle
- **Versión del motor predictivo:** model-v1.3
- **Ligas analizadas:** Premier League, La Liga, Serie A, Bundesliga, Ligue 1, Eredivisie, MLS, Liga Profesional Argentina (Liga BetPlay Colombia excluida: sin fuente de datos)
- **Rango de fechas solicitado:** 2026-10-18
- **Partidos en universo:** 29
- **Picks iniciales con value:** 141
- **Picks finales seleccionados:** 6

## Universo Analizado
Universo: 29 partidos del 2026-10-18 en 8 ligas, delimitados por FECHA LOCAL del partido (no por marca UTC): los 7 partidos de MLS con kickoff 00:40/02:30 UTC del 2026-10-18 pertenecen al 2026-10-17 en local y quedan fuera; los eventos del 2026-10-19 UTC que son 2026-10-19 en local también quedan fuera. Ligas: Premier League (4), La Liga (4), Bundesliga (2), Serie A (4), Ligue 1 (5), Eredivisie (5), Liga Profesional Argentina (4), MLS (1). EXCLUIDA la Liga BetPlay (Colombia): solicitada en el rango de ligas, no aparece en el proveedor de cuotas ni en ninguna fuente de datos disponible (The Odds API no la cubre; apifootball con autenticación fallida); sin fixtures, cuotas ni estadísticas verificables, por lo que no se analiza ningún partido de esa liga (no se inventan datos). xG real (Understat) en las 5 grandes ligas; para Eredivisie, MLS y Argentina se usa proxy GF/GA por partido de Wikipedia ante la ausencia de xG (documentado por partido). Córners/Tarjetas NO DISPONIBLES en ninguna fuente (apifootball sin autenticación, SofaScore 403, The Odds API sin esos mercados): consignado explícitamente, nunca omitido en silencio. El mercado draw_no_bet NO fue capturado en esta corrida (presupuesto de créditos de The Odds API casi agotado: los endpoints por evento se consultaron con h2h, totals, alternate_totals, btts y double_chance; DNB quedó fuera), por lo que se evalúan 1X2, doble oportunidad, BTTS y totales. Cuota = mejor precio disponible entre las casas de The Odds API al cutoff. ACTUALIDAD: identidad de clubes y pertenencia a torneos 2026 verificadas contra las tablas de Wikipedia y los rankings ClubElo/Understat vigentes; la verificación en vivo de lesiones, suspensiones y alineaciones probables NO pudo completarse (apifootball con autenticación fallida, SofaScore 403), por lo que esa incertidumbre se asume en el margen base del motor y se declara por pick.
- FC Zwolle vs Go Ahead Eagles (Eredivisie) — 10:15 UTC
- Udinese vs Lecce (Serie A) — 10:30 UTC
- CA Osasuna vs Real Racing Club de Santander (La Liga) — 12:00 UTC
- SC Cambuur vs AZ Alkmaar (Eredivisie) — 12:30 UTC
- Angers vs Marseille (Ligue 1) — 13:00 UTC
- Fiorentina vs Como (Serie A) — 13:00 UTC
- Bournemouth vs Sunderland (Premier League) — 13:00 UTC
- Brighton and Hove Albion vs Crystal Palace (Premier League) — 13:00 UTC
- Leeds United vs Manchester United (Premier League) — 13:00 UTC
- Bayer Leverkusen vs SC Freiburg (Bundesliga) — 13:30 UTC
- Celta Vigo vs Alavés (La Liga) — 14:15 UTC
- Groningen vs Ajax (Eredivisie) — 14:45 UTC
- Lorient vs AS Monaco (Ligue 1) — 15:15 UTC
- Le Havre vs Auxerre (Ligue 1) — 15:15 UTC
- Paris FC vs Rennes (Ligue 1) — 15:15 UTC
- Borussia Monchengladbach vs TSG Hoffenheim (Bundesliga) — 15:30 UTC
- Nottingham Forest vs Arsenal (Premier League) — 15:30 UTC
- AC Milan vs Atalanta BC (Serie A) — 16:00 UTC
- Málaga vs Real Sociedad (La Liga) — 16:30 UTC
- Racing Club vs Independiente (Liga Profesional Argentina) — 17:45 UTC
- FC Twente Enschede vs FC Utrecht (Eredivisie) — 18:00 UTC
- NEC Nijmegen vs Fortuna Sittard (Eredivisie) — 18:00 UTC
- Lyon vs Nice (Ligue 1) — 18:45 UTC
- Juventus vs Lazio (Serie A) — 18:45 UTC
- Real Madrid vs Sevilla (La Liga) — 19:00 UTC
- Estudiantes de Río Cuarto vs Aldosivi Mar del Plata (Liga Profesional Argentina) — 21:00 UTC
- Estudiantes vs San Lorenzo (Liga Profesional Argentina) — 21:00 UTC
- FC Cincinnati vs Columbus Crew SC (MLS) — 21:00 UTC
- Belgrano de Cordoba vs River Plate (Liga Profesional Argentina) — 23:15 UTC

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Brighton and Hove Albion vs Crystal Palace | over_1_5 | Over 1.5 Goles | excluido | 1.19 | 91.0% | 1.10 | +8.27% | +8.27% | +2.32% | 0.11u | Media-Alta |
| 2 | Borussia Monchengladbach vs TSG Hoffenheim | over_2_5 | Over 2.5 Goles | excluido | 1.40 | 90.6% | 1.10 | +26.91% | +26.91% | +19.91% | 0.17u | Media-Alta |
| 3 | SC Cambuur vs AZ Alkmaar | x2 | Doble Oportunidad Empate/AZ Alkmaar | excluido | 1.14 | 90.2% | 1.11 | +2.82% | +2.82% | -2.88% | 0.05u | Media-Alta |
| 4 | Groningen vs Ajax | over_2_5 | Over 2.5 Goles | excluido | 1.36 | 90.0% | 1.11 | +22.36% | +22.36% | +15.56% | 0.16u | Media-Alta |
| 5 | Udinese vs Lecce | over_1_5 | Over 1.5 Goles | excluido | 1.37 | 89.2% | 1.12 | +22.23% | +22.23% | +15.38% | 0.15u | Media-Alta |
| 6 | Angers vs Marseille | over_1_5 | Over 1.5 Goles | excluido | 1.21 | 88.8% | 1.13 | +7.47% | +7.47% | +1.42% | 0.09u | Media-Alta |
| 7 | Brighton and Hove Albion vs Crystal Palace | over_2_5 | Over 2.5 Goles | prioritario | 1.63 | 88.3% | 1.13 | +43.96% | +43.96% | +35.81% | 0.17u | Media-Alta |
| 8 | FC Zwolle vs Go Ahead Eagles | over_2_5 | Over 2.5 Goles | excluido | 1.45 | 88.0% | 1.14 | +27.54% | +27.54% | +20.29% | 0.15u | Media-Alta |
| 9 | FC Twente Enschede vs FC Utrecht | over_2_5 | Over 2.5 Goles | excluido | 1.33 | 87.9% | 1.14 | +16.92% | +16.92% | +10.27% | 0.13u | Media-Alta |
| 10 | FC Cincinnati vs Columbus Crew SC | over_2_5 | Over 2.5 Goles | excluido | 1.35 | 87.0% | 1.15 | +17.44% | +17.44% | +10.69% | 0.12u | Media-Alta |
| 11 | Fiorentina vs Como | over_1_5 | Over 1.5 Goles | excluido | 1.23 | 86.8% | 1.15 | +6.78% | +6.78% | +0.63% | 0.07u | Media-Alta |
| 12 | Udinese vs Lecce | over_2_5 | Over 2.5 Goles | prioritario | 2.09 | 85.5% | 1.17 | +78.72% | +78.72% | +68.27% | 0.18u | Media-Alta |
| 13 | FC Zwolle vs Go Ahead Eagles | x2 | Doble Oportunidad Empate/Go Ahead Eagles | excluido | 1.31 | 85.4% | 1.17 | +11.87% | +11.87% | +5.32% | 0.10u | Media-Alta |
| 14 | Le Havre vs Auxerre | over_1_5 | Over 1.5 Goles | excluido | 1.30 | 84.9% | 1.18 | +10.33% | +10.33% | +3.83% | 0.09u | Media-Alta |
| 15 | Angers vs Marseille | over_2_5 | Over 2.5 Goles | prioritario | 1.67 | 84.8% | 1.18 | +41.68% | +41.68% | +33.33% | 0.16u | Media-Alta |
| 16 | Bournemouth vs Sunderland | over_1_5 | Over 1.5 Goles | excluido | 1.30 | 84.7% | 1.18 | +10.12% | +10.12% | +3.62% | 0.08u | Media-Alta |
| 17 | Borussia Monchengladbach vs TSG Hoffenheim | over_3_5 | Over 3.5 Goles | prioritario | 2.06 | 84.6% | 1.18 | +74.32% | +74.32% | +64.02% | 0.18u | Media-Alta |
| 18 | AC Milan vs Atalanta BC | over_1_5 | Over 1.5 Goles | excluido | 1.26 | 84.0% | 1.19 | +5.84% | +5.84% | -0.46% | 0.06u | Media-Alta |
| 19 | AC Milan vs Atalanta BC | 1x | Doble Oportunidad AC Milan/Empate | excluido | 1.25 | 83.9% | 1.19 | +4.91% | +4.91% | -1.34% | 0.05u | Media-Alta |
| 20 | Groningen vs Ajax | over_3_5 | Over 3.5 Goles | prioritario | 1.99 | 83.4% | 1.20 | +66.05% | +66.05% | +56.10% | 0.17u | Media-Alta |
| 21 | Nottingham Forest vs Arsenal | over_1_5 | Over 1.5 Goles | excluido | 1.32 | 83.0% | 1.21 | +9.49% | +9.49% | +2.89% | 0.07u | Media-Alta |
| 22 | Estudiantes vs San Lorenzo | 1x | Doble Oportunidad Estudiantes/Empate | excluido | 1.28 | 82.3% | 1.22 | +5.33% | +5.33% | -1.07% | 0.05u | Media-Alta |
| 23 | NEC Nijmegen vs Fortuna Sittard | over_2_5 | Over 2.5 Goles | excluido | 1.38 | 81.8% | 1.22 | +12.86% | +12.86% | +5.96% | 0.08u | Media-Alta |
| 24 | SC Cambuur vs AZ Alkmaar | over_2_5 | Over 2.5 Goles | excluido | 1.38 | 81.8% | 1.22 | +12.83% | +12.83% | +5.93% | 0.08u | Media-Alta |
| 25 | Fiorentina vs Como | over_2_5 | Over 2.5 Goles | prioritario | 1.73 | 81.6% | 1.23 | +41.10% | +41.10% | +32.45% | 0.14u | Media-Alta |
| 26 | Brighton and Hove Albion vs Crystal Palace | over_3_5 | Over 3.5 Goles | excluido | 2.48 | 80.6% | 1.24 | +99.94% | +99.94% | +87.54% | 0.17u | Media-Alta |
| 27 | FC Zwolle vs Go Ahead Eagles | 12 | Doble Oportunidad FC Zwolle/Go Ahead Eagles | excluido | 1.28 | 80.1% | 1.25 | +2.55% | +2.55% | -3.85% | 0.02u | Media-Alta |
| 28 | FC Zwolle vs Go Ahead Eagles | over_3_5 | Over 3.5 Goles | excluido | 2.22 | 80.0% | 1.25 | +77.58% | +77.58% | +66.48% | 0.16u | Media-Alta |
| 29 | FC Twente Enschede vs FC Utrecht | over_3_5 | Over 3.5 Goles | prioritario | 1.94 | 79.9% | 1.25 | +55.03% | +55.03% | +45.33% | 0.15u | Media-Alta |
| 30 | CA Osasuna vs Real Racing Club de Santander | over_2_5 | Over 2.5 Goles | prioritario | 1.68 | 79.1% | 1.26 | +32.85% | +32.85% | +24.45% | 0.12u | Media-Alta |
| 31 | Juventus vs Lazio | over_1_5 | Over 1.5 Goles | excluido | 1.34 | 79.0% | 1.27 | +5.91% | +5.91% | -0.79% | 0.04u | Media-Alta |
| 32 | AC Milan vs Atalanta BC | 12 | Doble Oportunidad AC Milan/Atalanta BC | excluido | 1.30 | 78.9% | 1.27 | +2.57% | +2.57% | -3.93% | 0.02u | Media-Alta |
| 33 | Udinese vs Lecce | 12 | Doble Oportunidad Udinese/Lecce | excluido | 1.32 | 78.6% | 1.27 | +3.82% | +3.82% | -2.78% | 0.03u | Media-Alta |
| 34 | Fiorentina vs Como | x2 | Doble Oportunidad Empate/Como | excluido | 1.34 | 78.5% | 1.27 | +5.19% | +5.19% | -1.51% | 0.04u | Media-Alta |
| 35 | FC Cincinnati vs Columbus Crew SC | over_3_5 | Over 3.5 Goles | prioritario | 1.97 | 78.3% | 1.28 | +54.27% | +54.27% | +44.42% | 0.14u | Media-Alta |
| 36 | Le Havre vs Auxerre | over_2_5 | Over 2.5 Goles | prioritario | 1.95 | 78.3% | 1.28 | +52.70% | +52.70% | +42.95% | 0.14u | Media-Alta |
| 37 | Bayer Leverkusen vs SC Freiburg | over_2_5 | Over 2.5 Goles | excluido | 1.47 | 78.1% | 1.28 | +14.76% | +14.76% | +7.41% | 0.08u | Media-Alta |
| 38 | Bournemouth vs Sunderland | over_2_5 | Over 2.5 Goles | prioritario | 1.96 | 78.0% | 1.28 | +52.96% | +52.96% | +43.16% | 0.14u | Media-Alta |
| 39 | Paris FC vs Rennes | over_2_5 | Over 2.5 Goles | prioritario | 1.72 | 77.7% | 1.29 | +33.63% | +33.63% | +25.03% | 0.12u | Media-Alta |
| 40 | Real Madrid vs Sevilla | over_2_5 | Over 2.5 Goles | excluido | 1.42 | 77.7% | 1.29 | +10.29% | +10.29% | +3.19% | 0.06u | Media-Alta |
| 41 | Fiorentina vs Como | 12 | Doble Oportunidad Fiorentina/Como | excluido | 1.32 | 77.3% | 1.29 | +2.05% | +2.05% | -4.55% | 0.02u | Media-Alta |
| 42 | Borussia Monchengladbach vs TSG Hoffenheim | btts_yes | Ambos marcan (BTTS) | excluido | 1.43 | 77.1% | 1.30 | +10.28% | +10.28% | +3.13% | 0.06u | Media-Alta |
| 43 | AC Milan vs Atalanta BC | over_2_5 | Over 2.5 Goles | prioritario | 1.81 | 77.0% | 1.30 | +39.30% | +39.30% | +30.25% | 0.12u | Media-Alta |
| 44 | Bournemouth vs Sunderland | 12 | Doble Oportunidad Bournemouth/Sunderland | excluido | 1.34 | 76.9% | 1.30 | +3.10% | +3.10% | -3.60% | 0.02u | Media-Alta |
| 45 | Groningen vs Ajax | btts_yes | Ambos marcan (BTTS) | excluido | 1.44 | 76.5% | 1.31 | +10.19% | +10.19% | +2.99% | 0.06u | Media-Alta |
| 46 | Paris FC vs Rennes | 12 | Doble Oportunidad Paris FC/Rennes | excluido | 1.36 | 76.2% | 1.31 | +3.65% | +3.65% | -3.15% | 0.03u | Media-Alta |
| 47 | Le Havre vs Auxerre | 12 | Doble Oportunidad Le Havre/Auxerre | excluido | 1.35 | 76.0% | 1.32 | +2.55% | +2.55% | -4.20% | 0.02u | Media-Alta |
| 48 | Udinese vs Lecce | over_3_5 | Over 3.5 Goles | excepcional | 3.80 | 75.8% | 1.32 | +187.93% | +187.93% | +168.93% | 0.17u | Media-Alta |
| 49 | Nottingham Forest vs Arsenal | over_2_5 | Over 2.5 Goles | prioritario | 1.98 | 75.0% | 1.33 | +48.58% | +48.58% | +38.68% | 0.12u | Media-Alta |
| 50 | Leeds United vs Manchester United | over_2_5 | Over 2.5 Goles | prioritario | 1.71 | 75.0% | 1.33 | +28.23% | +28.23% | +19.68% | 0.10u | Media-Alta |
| 51 | Borussia Monchengladbach vs TSG Hoffenheim | x2 | Doble Oportunidad Empate/TSG Hoffenheim | excluido | 1.40 | 74.7% | 1.34 | +4.62% | +4.62% | -2.38% | 0.03u | Media-Alta |
| 52 | Angers vs Marseille | over_3_5 | Over 3.5 Goles | excluido | 2.60 | 74.6% | 1.34 | +94.04% | +94.04% | +81.04% | 0.15u | Media-Alta |
| 53 | Belgrano de Cordoba vs River Plate | 1x | Doble Oportunidad Belgrano de Cordoba/Empate | prioritario | 1.62 | 73.5% | 1.36 | +19.10% | +19.10% | +11.00% | 0.08u | Media-Alta |
| 54 | Brighton and Hove Albion vs Crystal Palace | btts_yes | Ambos marcan (BTTS) | prioritario | 1.72 | 71.3% | 1.40 | +22.62% | +22.62% | +14.02% | 0.08u | Media-Alta |
| 55 | SC Cambuur vs AZ Alkmaar | 2 | Victoria AZ Alkmaar | excluido | 1.52 | 71.0% | 1.41 | +7.86% | +7.86% | +0.26% | 0.04u | Media-Alta |
| 56 | Angers vs Marseille | btts_yes | Ambos marcan (BTTS) | excluido | 1.56 | 70.9% | 1.41 | +10.54% | +10.54% | +2.74% | 0.05u | Media-Alta |
| 57 | Udinese vs Lecce | btts_yes | Ambos marcan (BTTS) | prioritario | 1.96 | 70.7% | 1.41 | +38.61% | +38.61% | +28.81% | 0.10u | Media-Alta |
| 58 | Málaga vs Real Sociedad | over_2_5 | Over 2.5 Goles | prioritario | 1.86 | 70.5% | 1.42 | +31.09% | +31.09% | +21.79% | 0.09u | Media-Alta |
| 59 | Lyon vs Nice | over_2_5 | Over 2.5 Goles | prioritario | 1.75 | 70.3% | 1.42 | +22.97% | +22.97% | +14.22% | 0.08u | Media-Alta |
| 60 | Leeds United vs Manchester United | x2 | Doble Oportunidad Empate/Manchester United | prioritario | 1.64 | 70.2% | 1.43 | +15.06% | +15.06% | +6.86% | 0.06u | Media-Alta |
| 61 | Celta Vigo vs Alavés | x2 | Doble Oportunidad Empate/Alavés | prioritario | 1.71 | 69.7% | 1.43 | +19.20% | +19.20% | +10.65% | 0.07u | Media-Alta |
| 62 | Racing Club vs Independiente | x2 | Doble Oportunidad Empate/Independiente | prioritario | 1.73 | 69.6% | 1.44 | +20.39% | +20.39% | +11.74% | 0.07u | Media-Alta |
| 63 | NEC Nijmegen vs Fortuna Sittard | over_3_5 | Over 3.5 Goles | prioritario | 2.02 | 69.5% | 1.44 | +40.31% | +40.31% | +30.21% | 0.10u | Media-Alta |
| 64 | SC Cambuur vs AZ Alkmaar | over_3_5 | Over 3.5 Goles | prioritario | 2.03 | 69.4% | 1.44 | +40.96% | +40.96% | +30.81% | 0.10u | Media-Alta |
| 65 | Fiorentina vs Como | over_3_5 | Over 3.5 Goles | excluido | 2.73 | 69.1% | 1.45 | +88.62% | +88.62% | +74.97% | 0.13u | Media-Alta |
| 66 | Juventus vs Lazio | over_2_5 | Over 2.5 Goles | prioritario | 2.04 | 68.4% | 1.46 | +39.50% | +39.50% | +29.30% | 0.09u | Media-Alta |
| 67 | Fiorentina vs Como | btts_yes | Ambos marcan (BTTS) | excluido | 1.62 | 68.2% | 1.47 | +10.40% | +10.40% | +2.30% | 0.04u | Media-Alta |
| 68 | Estudiantes de Río Cuarto vs Aldosivi Mar del Plata | over_1_5 | Over 1.5 Goles | excluido | 1.60 | 67.5% | 1.48 | +8.02% | +8.02% | +0.02% | 0.03u | Media-Alta |
| 69 | FC Twente Enschede vs FC Utrecht | btts_yes | Ambos marcan (BTTS) | excluido | 1.63 | 66.8% | 1.50 | +8.90% | +8.90% | +0.75% | 0.04u | Media-Alta |
| 70 | Estudiantes vs San Lorenzo | btts_no | No ambos marcan | excluido | 1.62 | 66.7% | 1.50 | +8.02% | +8.02% | -0.08% | 0.03u | Media-Alta |
| 71 | Le Havre vs Auxerre | btts_yes | Ambos marcan (BTTS) | excluido | 1.73 | 65.7% | 1.52 | +13.59% | +13.59% | +4.94% | 0.05u | Media-Alta |
| 72 | FC Zwolle vs Go Ahead Eagles | 2 | Victoria Go Ahead Eagles | prioritario | 2.00 | 65.5% | 1.53 | +31.04% | +31.04% | +21.04% | 0.08u | Media-Alta |
| 73 | Bournemouth vs Sunderland | btts_yes | Ambos marcan (BTTS) | prioritario | 1.76 | 65.3% | 1.53 | +14.96% | +14.96% | +6.16% | 0.05u | Media-Alta |
| 74 | CA Osasuna vs Real Racing Club de Santander | over_3_5 | Over 3.5 Goles | excluido | 2.57 | 65.0% | 1.54 | +67.02% | +67.02% | +54.17% | 0.11u | Media-Alta |
| 75 | FC Cincinnati vs Columbus Crew SC | x2 | Doble Oportunidad Empate/Columbus Crew SC | excluido | 1.62 | 64.4% | 1.55 | +4.39% | +4.39% | -3.71% | 0.02u | Media-Alta |
| 76 | Le Havre vs Auxerre | over_3_5 | Over 3.5 Goles | excepcional | 3.24 | 63.7% | 1.57 | +106.45% | +106.45% | +90.25% | 0.12u | Media-Alta |
| 77 | Nottingham Forest vs Arsenal | btts_yes | Ambos marcan (BTTS) | prioritario | 2.00 | 63.3% | 1.58 | +26.68% | +26.68% | +16.68% | 0.07u | Media-Alta |
| 78 | Bayer Leverkusen vs SC Freiburg | over_3_5 | Over 3.5 Goles | excluido | 2.27 | 63.3% | 1.58 | +43.76% | +43.76% | +32.41% | 0.09u | Media-Alta |
| 79 | Bournemouth vs Sunderland | over_3_5 | Over 3.5 Goles | excepcional | 3.30 | 63.3% | 1.58 | +108.82% | +108.82% | +92.32% | 0.12u | Media-Alta |
| 80 | Le Havre vs Auxerre | x2 | Doble Oportunidad Empate/Auxerre | excluido | 1.66 | 63.0% | 1.59 | +4.63% | +4.63% | -3.67% | 0.02u | Media-Alta |
| 81 | AC Milan vs Atalanta BC | 1 | Victoria AC Milan | prioritario | 1.87 | 62.8% | 1.59 | +17.49% | +17.49% | +8.14% | 0.05u | Media-Alta |
| 82 | Paris FC vs Rennes | over_3_5 | Over 3.5 Goles | excluido | 2.54 | 62.7% | 1.59 | +59.28% | +59.28% | +46.58% | 0.10u | Media-Alta |
| 83 | Real Madrid vs Sevilla | over_3_5 | Over 3.5 Goles | prioritario | 2.12 | 62.7% | 1.60 | +32.88% | +32.88% | +22.28% | 0.07u | Media-Alta |
| 84 | AC Milan vs Atalanta BC | over_3_5 | Over 3.5 Goles | excluido | 2.95 | 61.6% | 1.62 | +81.57% | +81.57% | +66.82% | 0.10u | Media-Alta |
| 85 | Lorient vs AS Monaco | 1x | Doble Oportunidad Lorient/Empate | excluido | 1.82 | 61.1% | 1.64 | +11.27% | +11.27% | +2.17% | 0.03u | Media-Alta |
| 86 | NEC Nijmegen vs Fortuna Sittard | x2 | Doble Oportunidad Empate/Fortuna Sittard | excluido | 2.27 | 58.8% | 1.70 | +33.45% | +33.45% | +22.10% | 0.07u | Media-Alta |
| 87 | Real Madrid vs Sevilla | btts_yes | Ambos marcan (BTTS) | excluido | 1.94 | 58.7% | 1.70 | +13.86% | +13.86% | +4.16% | 0.04u | Media-Alta |
| 88 | Angers vs Marseille | 1x | Doble Oportunidad Angers/Empate | excluido | 1.85 | 58.6% | 1.71 | +8.43% | +8.43% | -0.82% | 0.02u | Media-Alta |
| 89 | Lyon vs Nice | 1 | Victoria Lyon | excluido | 1.89 | 58.5% | 1.71 | +10.60% | +10.60% | +1.15% | 0.03u | Media-Alta |
| 90 | Nottingham Forest vs Arsenal | over_3_5 | Over 3.5 Goles | excepcional | 3.45 | 58.5% | 1.71 | +101.79% | +101.79% | +84.54% | 0.10u | Media-Alta |
| 91 | Leeds United vs Manchester United | over_3_5 | Over 3.5 Goles | excluido | 2.73 | 58.4% | 1.71 | +59.46% | +59.46% | +45.81% | 0.09u | Media-Alta |
| 92 | CA Osasuna vs Real Racing Club de Santander | x2 | Doble Oportunidad Empate/Real Racing Club de Santander | excluido | 1.88 | 58.0% | 1.72 | +9.04% | +9.04% | -0.36% | 0.03u | Media-Alta |
| 93 | Fiorentina vs Como | 2 | Victoria Como | prioritario | 2.18 | 55.8% | 1.79 | +21.67% | +21.67% | +10.77% | 0.05u | Media |
| 94 | Bayer Leverkusen vs SC Freiburg | x2 | Doble Oportunidad Empate/SC Freiburg | excluido | 2.28 | 55.6% | 1.80 | +26.75% | +26.75% | +15.35% | 0.05u | Media |
| 95 | Juventus vs Lazio | btts_yes | Ambos marcan (BTTS) | excluido | 2.00 | 55.5% | 1.80 | +10.90% | +10.90% | +0.90% | 0.03u | Media |
| 96 | Celta Vigo vs Alavés | over_2_5 | Over 2.5 Goles | excluido | 2.36 | 54.6% | 1.83 | +28.76% | +28.76% | +16.96% | 0.05u | Media |
| 97 | Borussia Monchengladbach vs TSG Hoffenheim | 2 | Victoria TSG Hoffenheim | excluido | 2.22 | 54.2% | 1.84 | +20.37% | +20.37% | +9.27% | 0.04u | Media |
| 98 | Groningen vs Ajax | 2 | Victoria Ajax | excluido | 1.97 | 53.8% | 1.86 | +5.95% | +5.95% | -3.90% | 0.02u | Media |
| 99 | Nottingham Forest vs Arsenal | 1x | Doble Oportunidad Nottingham Forest/Empate | excluido | 2.38 | 52.9% | 1.89 | +25.93% | +25.93% | +14.03% | 0.05u | Media |
| 100 | Málaga vs Real Sociedad | over_3_5 | Over 3.5 Goles | excepcional | 3.05 | 51.5% | 1.94 | +57.20% | +57.20% | +41.95% | 0.07u | Media |
| 101 | Lyon vs Nice | over_3_5 | Over 3.5 Goles | excluido | 2.71 | 51.2% | 1.95 | +38.83% | +38.83% | +25.28% | 0.06u | Media |
| 102 | Estudiantes vs San Lorenzo | 1 | Victoria Estudiantes | excluido | 2.42 | 50.9% | 1.96 | +23.23% | +23.23% | +11.13% | 0.04u | Media |
| 103 | Lorient vs AS Monaco | btts_no | No ambos marcan | excluido | 2.12 | 50.9% | 1.96 | +7.93% | +7.93% | -2.67% | 0.02u | Media |
| 104 | Udinese vs Lecce | x2 | Doble Oportunidad Empate/Lecce | excluido | 2.05 | 50.4% | 1.98 | +3.36% | +3.36% | -6.89% | 0.01u | Media |
| 105 | Estudiantes de Río Cuarto vs Aldosivi Mar del Plata | over_2_5 | Over 2.5 Goles | excluido | 2.85 | 48.8% | 2.05 | +39.02% | +39.02% | +24.77% | 0.05u | Baja |
| 106 | Racing Club vs Independiente | over_2_5 | Over 2.5 Goles | excluido | 2.35 | 48.8% | 2.05 | +14.63% | +14.63% | +2.88% | 0.03u | Baja |
| 107 | Málaga vs Real Sociedad | 2 | Victoria Real Sociedad | excluido | 2.22 | 48.7% | 2.05 | +8.11% | +8.11% | -2.99% | 0.02u | Baja |
| 108 | Juventus vs Lazio | over_3_5 | Over 3.5 Goles | excepcional | 3.55 | 48.5% | 2.06 | +72.10% | +72.10% | +54.35% | 0.07u | Baja |
| 109 | Paris FC vs Rennes | 1 | Victoria Paris FC | excluido | 2.37 | 46.6% | 2.15 | +10.42% | +10.42% | -1.43% | 0.02u | Baja |
| 110 | Leeds United vs Manchester United | 2 | Victoria Manchester United | excepcional | 3.05 | 45.5% | 2.20 | +38.87% | +38.87% | +23.62% | 0.05u | Baja |
| 111 | Juventus vs Lazio | x2 | Doble Oportunidad Empate/Lazio | excluido | 2.31 | 44.8% | 2.23 | +3.42% | +3.42% | -8.13% | 0.01u | Baja |
| 112 | Estudiantes vs San Lorenzo | under_1_5 | Under 1.5 Goles | excluido | 2.40 | 44.6% | 2.24 | +6.97% | +6.97% | -5.03% | 0.01u | Baja |
| 113 | FC Cincinnati vs Columbus Crew SC | 2 | Victoria Columbus Crew SC | excluido | 2.75 | 42.6% | 2.35 | +17.21% | +17.21% | +3.46% | 0.02u | Baja |
| 114 | Belgrano de Cordoba vs River Plate | 1 | Victoria Belgrano de Cordoba | excepcional | 3.65 | 42.5% | 2.35 | +55.02% | +55.02% | +36.77% | 0.05u | Baja |
| 115 | Celta Vigo vs Alavés | 2 | Victoria Alavés | excepcional | 3.68 | 41.9% | 2.38 | +54.38% | +54.38% | +35.98% | 0.05u | Baja |
| 116 | Brighton and Hove Albion vs Crystal Palace | x2 | Doble Oportunidad Empate/Crystal Palace | excluido | 2.72 | 40.7% | 2.46 | +10.62% | +10.62% | -2.98% | 0.02u | Baja |
| 117 | Racing Club vs Independiente | 2 | Victoria Independiente | excepcional | 3.80 | 40.6% | 2.46 | +54.20% | +54.20% | +35.20% | 0.05u | Baja |
| 118 | Le Havre vs Auxerre | 2 | Victoria Auxerre | excepcional | 3.30 | 39.0% | 2.56 | +28.67% | +28.67% | +12.17% | 0.03u | Baja |
| 119 | Estudiantes de Río Cuarto vs Aldosivi Mar del Plata | 1 | Victoria Estudiantes de Río Cuarto | excluido | 3.05 | 37.5% | 2.67 | +14.41% | +14.41% | -0.84% | 0.02u | Baja |
| 120 | NEC Nijmegen vs Fortuna Sittard | 2 | Victoria Fortuna Sittard | excepcional | 4.80 | 36.4% | 2.75 | +74.53% | +74.53% | +50.53% | 0.05u | Baja |
| 121 | Angers vs Marseille | 1 | Victoria Angers | excepcional | 3.70 | 36.1% | 2.77 | +33.61% | +33.61% | +15.11% | 0.03u | Baja |
| 122 | CA Osasuna vs Real Racing Club de Santander | 2 | Victoria Real Racing Club de Santander | excepcional | 3.82 | 34.6% | 2.89 | +32.32% | +32.32% | +13.22% | 0.03u | Baja |
| 123 | Bournemouth vs Sunderland | 2 | Victoria Sunderland | excluido | 3.75 | 32.9% | 3.04 | +23.53% | +23.53% | +4.78% | 0.02u | Baja |
| 124 | Bayer Leverkusen vs SC Freiburg | 2 | Victoria SC Freiburg | excepcional | 4.90 | 32.4% | 3.09 | +58.81% | +58.81% | +34.31% | 0.04u | Baja |
| 125 | Lorient vs AS Monaco | 1 | Victoria Lorient | excluido | 3.95 | 32.0% | 3.12 | +26.40% | +26.40% | +6.65% | 0.02u | Baja |
| 126 | Celta Vigo vs Alavés | over_3_5 | Over 3.5 Goles | excluido | 4.20 | 30.8% | 3.25 | +29.36% | +29.36% | +8.36% | 0.02u | Baja |
| 127 | Real Madrid vs Sevilla | x2 | Doble Oportunidad Empate/Sevilla | excepcional | 4.40 | 30.7% | 3.26 | +35.17% | +35.17% | +13.17% | 0.03u | Baja |
| 128 | Lorient vs AS Monaco | under_1_5 | Under 1.5 Goles | excluido | 3.75 | 30.2% | 3.31 | +13.21% | +13.21% | -5.54% | 0.01u | Baja |
| 129 | Nottingham Forest vs Arsenal | 1 | Victoria Nottingham Forest | excluido | 6.80 | 29.4% | 3.40 | +99.78% | +99.78% | +65.78% | 0.04u | Baja |
| 130 | Lorient vs AS Monaco | X | Empate | excluido | 3.60 | 29.1% | 3.43 | +4.90% | +4.90% | -13.10% | 0.00u | Baja |
| 131 | Udinese vs Lecce | 2 | Victoria Lecce | excluido | 4.90 | 29.1% | 3.44 | +42.44% | +42.44% | +17.94% | 0.03u | Baja |
| 132 | Estudiantes de Río Cuarto vs Aldosivi Mar del Plata | over_3_5 | Over 3.5 Goles | excluido | 6.37 | 24.7% | 4.05 | +57.40% | +57.40% | +25.55% | 0.03u | Baja |
| 133 | Racing Club vs Independiente | over_3_5 | Over 3.5 Goles | excluido | 4.70 | 24.7% | 4.05 | +16.14% | +16.14% | -7.36% | 0.01u | Baja |
| 134 | Bayer Leverkusen vs SC Freiburg | X | Empate | excluido | 4.70 | 23.2% | 4.31 | +8.95% | +8.95% | -14.55% | 0.01u | Baja |
| 135 | NEC Nijmegen vs Fortuna Sittard | X | Empate | excluido | 4.60 | 22.4% | 4.46 | +3.18% | +3.18% | -19.82% | 0.00u | Baja |
| 136 | Brighton and Hove Albion vs Crystal Palace | 2 | Victoria Crystal Palace | excluido | 6.80 | 21.0% | 4.75 | +43.07% | +43.07% | +9.07% | 0.02u | Baja |
| 137 | Juventus vs Lazio | 2 | Victoria Lazio | excluido | 5.80 | 20.8% | 4.80 | +20.81% | +20.81% | -8.19% | 0.01u | Baja |
| 138 | Real Madrid vs Sevilla | X | Empate | excluido | 7.40 | 19.4% | 5.16 | +43.49% | +43.49% | +6.49% | 0.02u | Baja |
| 139 | FC Twente Enschede vs FC Utrecht | X | Empate | excluido | 6.10 | 17.7% | 5.65 | +7.97% | +7.97% | -22.53% | 0.00u | Baja |
| 140 | FC Twente Enschede vs FC Utrecht | 2 | Victoria FC Utrecht | excluido | 8.50 | 12.9% | 7.75 | +9.65% | +9.65% | -32.85% | 0.00u | Baja |
| 141 | Real Madrid vs Sevilla | 2 | Victoria Sevilla | excluido | 14.00 | 11.3% | 8.83 | +58.62% | +58.62% | -11.38% | 0.01u | Baja |

## Evaluación Over/Under por Partido
Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada (n/d = cuota no disponible en la corrida).
| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |
|---|---|---|---:|---:|---:|---:|---:|---|
| FC Zwolle vs Go Ahead Eagles | 1.5 | 90.8% | 1.14 | +3.47% | 9.2% | 6.03 | -44.28% | Sin value |
| FC Zwolle vs Go Ahead Eagles | 2.5 | 88.0% | 1.45 | +27.54% | 12.0% | 2.66 | -67.97% | Value Over |
| FC Zwolle vs Go Ahead Eagles | 3.5 | 80.0% | 2.22 | +77.58% | 20.0% | 1.76 | -64.78% | Value Over |
| Udinese vs Lecce | 1.5 | 89.2% | 1.37 | +22.23% | 10.8% | 3.38 | -63.56% | Value Over |
| Udinese vs Lecce | 2.5 | 85.5% | 2.09 | +78.72% | 14.5% | 1.87 | -72.90% | Value Over |
| Udinese vs Lecce | 3.5 | 75.8% | 3.80 | +187.93% | 24.2% | 1.31 | -68.26% | Value Over |
| CA Osasuna vs Real Racing Club de Santander | 1.5 | 85.3% | 1.20 | +2.40% | 14.7% | 5.00 | -26.65% | Sin value |
| CA Osasuna vs Real Racing Club de Santander | 2.5 | 79.1% | 1.68 | +32.85% | 20.9% | 2.40 | -49.79% | Value Over |
| CA Osasuna vs Real Racing Club de Santander | 3.5 | 65.0% | 2.57 | +67.02% | 35.0% | 1.57 | -45.03% | Value Over |
| SC Cambuur vs AZ Alkmaar | 1.5 | 86.9% | 1.13 | -1.80% | 13.1% | 6.68 | -12.49% | Sin value |
| SC Cambuur vs AZ Alkmaar | 2.5 | 81.8% | 1.38 | +12.83% | 18.2% | 3.00 | -45.28% | Value Over |
| SC Cambuur vs AZ Alkmaar | 3.5 | 69.4% | 2.03 | +40.96% | 30.6% | 1.92 | -41.32% | Value Over |
| Angers vs Marseille | 1.5 | 88.8% | 1.21 | +7.47% | 11.2% | 4.90 | -45.22% | Value Over |
| Angers vs Marseille | 2.5 | 84.8% | 1.67 | +41.68% | 15.2% | 2.40 | -63.62% | Value Over |
| Angers vs Marseille | 3.5 | 74.6% | 2.60 | +94.04% | 25.4% | 1.55 | -60.68% | Value Over |
| Fiorentina vs Como | 1.5 | 86.8% | 1.23 | +6.78% | 13.2% | 4.60 | -39.33% | Value Over |
| Fiorentina vs Como | 2.5 | 81.6% | 1.73 | +41.10% | 18.4% | 2.29 | -57.77% | Value Over |
| Fiorentina vs Como | 3.5 | 69.1% | 2.73 | +88.62% | 30.9% | 1.51 | -53.33% | Value Over |
| Bournemouth vs Sunderland | 1.5 | 84.7% | 1.30 | +10.12% | 15.3% | 3.78 | -42.20% | Value Over |
| Bournemouth vs Sunderland | 2.5 | 78.0% | 1.96 | +52.96% | 22.0% | 2.02 | -55.64% | Value Over |
| Bournemouth vs Sunderland | 3.5 | 63.3% | 3.30 | +108.82% | 36.7% | 1.37 | -49.69% | Value Over |
| Brighton and Hove Albion vs Crystal Palace | 1.5 | 91.0% | 1.19 | +8.27% | 9.0% | 5.20 | -53.10% | Value Over |
| Brighton and Hove Albion vs Crystal Palace | 2.5 | 88.3% | 1.63 | +43.96% | 11.7% | 2.51 | -70.68% | Value Over |
| Brighton and Hove Albion vs Crystal Palace | 3.5 | 80.6% | 2.48 | +99.94% | 19.4% | 1.66 | -67.83% | Value Over |
| Leeds United vs Manchester United | 1.5 | 82.9% | 1.23 | +1.99% | 17.1% | 4.55 | -22.29% | Sin value |
| Leeds United vs Manchester United | 2.5 | 75.0% | 1.71 | +28.23% | 25.0% | 2.32 | -41.98% | Value Over |
| Leeds United vs Manchester United | 3.5 | 58.4% | 2.73 | +59.46% | 41.6% | 1.50 | -37.61% | Value Over |
| Bayer Leverkusen vs SC Freiburg | 1.5 | 84.7% | 1.16 | -1.71% | 15.3% | 6.00 | -8.38% | Sin value |
| Bayer Leverkusen vs SC Freiburg | 2.5 | 78.1% | 1.47 | +14.76% | 21.9% | 2.72 | -40.35% | Value Over |
| Bayer Leverkusen vs SC Freiburg | 3.5 | 63.3% | 2.27 | +43.76% | 36.7% | 1.80 | -33.99% | Value Over |
| Celta Vigo vs Alavés | 1.5 | 71.0% | 1.41 | +0.15% | 29.0% | 3.12 | -9.61% | Sin value |
| Celta Vigo vs Alavés | 2.5 | 54.6% | 2.36 | +28.76% | 45.4% | 1.78 | -19.12% | Value Over |
| Celta Vigo vs Alavés | 3.5 | 30.8% | 4.20 | +29.36% | 69.2% | 1.26 | -12.81% | Value Over |
| Groningen vs Ajax | 1.5 | 92.1% | 1.11 | +2.22% | 7.9% | 7.09 | -43.92% | Sin value |
| Groningen vs Ajax | 2.5 | 90.0% | 1.36 | +22.36% | 10.0% | 3.04 | -69.51% | Value Over |
| Groningen vs Ajax | 3.5 | 83.4% | 1.99 | +66.05% | 16.6% | 1.91 | -68.37% | Value Over |
| Lorient vs AS Monaco | 1.5 | 69.8% | 1.32 | -7.85% | 30.2% | 3.75 | +13.21% | Value Under |
| Lorient vs AS Monaco | 2.5 | 52.5% | 1.97 | +3.52% | 47.4% | 1.97 | -6.52% | Sin value |
| Lorient vs AS Monaco | 3.5 | 28.6% | 3.35 | -4.22% | 71.4% | 1.37 | -2.17% | Sin value |
| Le Havre vs Auxerre | 1.5 | 84.9% | 1.30 | +10.33% | 15.1% | 3.87 | -41.45% | Value Over |
| Le Havre vs Auxerre | 2.5 | 78.3% | 1.95 | +52.70% | 21.7% | 2.00 | -56.62% | Value Over |
| Le Havre vs Auxerre | 3.5 | 63.7% | 3.24 | +106.45% | 36.3% | 1.36 | -50.66% | Value Over |
| Paris FC vs Rennes | 1.5 | 84.5% | 1.22 | +3.07% | 15.5% | 4.50 | -30.16% | Sin value |
| Paris FC vs Rennes | 2.5 | 77.7% | 1.72 | +33.63% | 22.3% | 2.30 | -48.69% | Value Over |
| Paris FC vs Rennes | 3.5 | 62.7% | 2.54 | +59.28% | 37.3% | 1.53 | -42.95% | Value Over |
| Borussia Monchengladbach vs TSG Hoffenheim | 1.5 | 92.5% | 1.12 | +3.64% | 7.5% | 6.50 | -51.51% | Sin value |
| Borussia Monchengladbach vs TSG Hoffenheim | 2.5 | 90.6% | 1.40 | +26.91% | 9.3% | 3.05 | -71.48% | Value Over |
| Borussia Monchengladbach vs TSG Hoffenheim | 3.5 | 84.6% | 2.06 | +74.32% | 15.4% | 1.93 | -70.32% | Value Over |
| Nottingham Forest vs Arsenal | 1.5 | 83.0% | 1.32 | +9.49% | 17.1% | 3.74 | -36.23% | Value Over |
| Nottingham Forest vs Arsenal | 2.5 | 75.0% | 1.98 | +48.58% | 25.0% | 2.00 | -50.08% | Value Over |
| Nottingham Forest vs Arsenal | 3.5 | 58.5% | 3.45 | +101.79% | 41.5% | 1.36 | -43.55% | Value Over |
| AC Milan vs Atalanta BC | 1.5 | 84.0% | 1.26 | +5.84% | 16.0% | 4.20 | -32.80% | Value Over |
| AC Milan vs Atalanta BC | 2.5 | 77.0% | 1.81 | +39.30% | 23.0% | 2.15 | -50.46% | Value Over |
| AC Milan vs Atalanta BC | 3.5 | 61.6% | 2.95 | +81.57% | 38.5% | 1.46 | -43.86% | Value Over |
| Málaga vs Real Sociedad | 1.5 | 80.3% | 1.27 | +1.99% | 19.7% | 4.10 | -19.27% | Sin value |
| Málaga vs Real Sociedad | 2.5 | 70.5% | 1.86 | +31.09% | 29.5% | 2.10 | -38.01% | Value Over |
| Málaga vs Real Sociedad | 3.5 | 51.5% | 3.05 | +57.20% | 48.5% | 1.43 | -30.70% | Value Over |
| Racing Club vs Independiente | 1.5 | 67.5% | 1.45 | -2.11% | 32.5% | 2.84 | -7.73% | Sin value |
| Racing Club vs Independiente | 2.5 | 48.8% | 2.35 | +14.63% | 51.2% | 1.65 | -15.49% | Value Over |
| Racing Club vs Independiente | 3.5 | 24.7% | 4.70 | +16.14% | 75.3% | 1.20 | -9.65% | Value Over |
| FC Twente Enschede vs FC Utrecht | 1.5 | 90.7% | 1.11 | +0.63% | 9.3% | 7.04 | -34.25% | Sin value |
| FC Twente Enschede vs FC Utrecht | 2.5 | 87.9% | 1.33 | +16.92% | 12.1% | 3.26 | -60.59% | Value Over |
| FC Twente Enschede vs FC Utrecht | 3.5 | 79.9% | 1.94 | +55.03% | 20.1% | 2.00 | -59.82% | Value Over |
| NEC Nijmegen vs Fortuna Sittard | 1.5 | 87.0% | 1.12 | -2.62% | 13.1% | 6.58 | -14.13% | Sin value |
| NEC Nijmegen vs Fortuna Sittard | 2.5 | 81.8% | 1.38 | +12.86% | 18.2% | 2.94 | -46.43% | Value Over |
| NEC Nijmegen vs Fortuna Sittard | 3.5 | 69.5% | 2.02 | +40.31% | 30.5% | 1.88 | -42.58% | Value Over |
| Lyon vs Nice | 1.5 | 80.1% | 1.22 | -2.23% | 19.9% | 4.40 | -12.62% | Sin value |
| Lyon vs Nice | 2.5 | 70.3% | 1.75 | +22.97% | 29.7% | 2.30 | -31.62% | Value Over |
| Lyon vs Nice | 3.5 | 51.2% | 2.71 | +38.83% | 48.8% | 1.49 | -27.33% | Value Over |
| Juventus vs Lazio | 1.5 | 79.0% | 1.34 | +5.91% | 21.0% | 3.59 | -24.75% | Value Over |
| Juventus vs Lazio | 2.5 | 68.4% | 2.04 | +39.50% | 31.6% | 1.94 | -38.66% | Value Over |
| Juventus vs Lazio | 3.5 | 48.5% | 3.55 | +72.10% | 51.5% | 1.34 | -30.96% | Value Over |
| Real Madrid vs Sevilla | 1.5 | 84.4% | 1.14 | -3.77% | 15.6% | 6.60 | +2.89% | Sin value |
| Real Madrid vs Sevilla | 2.5 | 77.7% | 1.42 | +10.29% | 22.3% | 2.94 | -34.35% | Value Over |
| Real Madrid vs Sevilla | 3.5 | 62.7% | 2.12 | +32.88% | 37.3% | 1.84 | -31.33% | Value Over |
| Estudiantes de Río Cuarto vs Aldosivi Mar del Plata | 1.5 | 67.5% | 1.60 | +8.02% | 32.5% | 2.43 | -21.05% | Value Over |
| Estudiantes de Río Cuarto vs Aldosivi Mar del Plata | 2.5 | 48.8% | 2.85 | +39.02% | 51.2% | 1.39 | -28.80% | Value Over |
| Estudiantes de Río Cuarto vs Aldosivi Mar del Plata | 3.5 | 24.7% | 6.37 | +57.40% | 75.3% | 1.13 | -14.92% | Value Over |
| Estudiantes vs San Lorenzo | 1.5 | 55.4% | 1.58 | -12.42% | 44.6% | 2.40 | +6.97% | Value Under |
| Estudiantes vs San Lorenzo | 2.5 | 31.1% | 2.72 | -15.52% | 68.9% | 1.44 | -0.73% | Sin value |
| Estudiantes vs San Lorenzo | 3.5 | 10.6% | 5.87 | -37.90% | 89.4% | 1.14 | +1.94% | Sin value |
| FC Cincinnati vs Columbus Crew SC | 1.5 | 90.2% | 1.11 | +0.09% | 9.8% | 7.00 | -31.19% | Sin value |
| FC Cincinnati vs Columbus Crew SC | 2.5 | 87.0% | 1.35 | +17.44% | 13.0% | 3.15 | -59.02% | Value Over |
| FC Cincinnati vs Columbus Crew SC | 3.5 | 78.3% | 1.97 | +54.27% | 21.7% | 2.04 | -55.75% | Value Over |
| Belgrano de Cordoba vs River Plate | 1.5 | 61.3% | 1.54 | -5.63% | 38.7% | 2.47 | -4.36% | Sin value |
| Belgrano de Cordoba vs River Plate | 2.5 | 39.2% | 2.53 | -0.90% | 60.8% | 1.54 | -6.32% | Sin value |
| Belgrano de Cordoba vs River Plate | 3.5 | 16.2% | 4.97 | -19.24% | 83.8% | 1.19 | -0.34% | Sin value |

## Picks Recomendados (Top 6)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Brighton and Hove Albion vs Crystal Palace | over_2_5 | Over 2.5 Goles | prioritario | 1.63 | 88.3% | 1.13 | +43.96% | +43.96% | +35.81% | 0.17u | Media-Alta |
| 2 | Udinese vs Lecce | over_2_5 | Over 2.5 Goles | prioritario | 2.09 | 85.5% | 1.17 | +78.72% | +78.72% | +68.27% | 0.18u | Media-Alta |
| 3 | Angers vs Marseille | over_2_5 | Over 2.5 Goles | prioritario | 1.67 | 84.8% | 1.18 | +41.68% | +41.68% | +33.33% | 0.16u | Media-Alta |
| 4 | Borussia Monchengladbach vs TSG Hoffenheim | over_3_5 | Over 3.5 Goles | prioritario | 2.06 | 84.6% | 1.18 | +74.32% | +74.32% | +64.02% | 0.18u | Media-Alta |
| 5 | Groningen vs Ajax | over_3_5 | Over 3.5 Goles | prioritario | 1.99 | 83.4% | 1.20 | +66.05% | +66.05% | +56.10% | 0.17u | Media-Alta |
| 6 | Fiorentina vs Como | over_2_5 | Over 2.5 Goles | prioritario | 1.73 | 81.6% | 1.23 | +41.10% | +41.10% | +32.45% | 0.14u | Media-Alta |

## Detalle de Picks
### Pick 1: Brighton and Hove Albion vs Crystal Palace
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.63
- **Probabilidad modelo:** 88.3%
- **Probabilidad conservadora:** 83.3%
- **Probabilidad implícita:** 61.4%
- **Cuota justa:** 1.13
- **Edge:** +43.96%
- **EV:** +43.96%
- **EV robusto:** +35.81%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.20
- **Stake:** 0.17u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** P(Over 2.5 goles)=88.3% frente a la implícita 61.4%; cuota justa 1.13 vs cuota capturada 1.63. Goles esperados del motor: 2.48 - 1.49. EV robusto +35.81% con cuota en perfil prioritario.
- **Riesgos:** Varianza intrínseca del fútbol; el EV depende de cuotas de mejor precio entre casas (puede no estar disponible al mismo precio). Córners/tarjetas no disponibles: no se evalúan esos mercados. Lesiones/suspensiones/alineaciones no verificables en vivo (fuentes no operativas) y no modeladas: no se descarta un cambio de última hora.
- **Fuentes:** Understat EPL 2026 (xG real) + ClubElo + The Odds API (Brighton and Hove Albion 2.42/1.58, Crystal Palace 1.64/2.30); Elo 1897/1825; The Odds API cuota 1.63

### Pick 2: Udinese vs Lecce
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 2.09
- **Probabilidad modelo:** 85.5%
- **Probabilidad conservadora:** 80.5%
- **Probabilidad implícita:** 47.9%
- **Cuota justa:** 1.17
- **Edge:** +78.72%
- **EV:** +78.72%
- **EV robusto:** +68.27%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.24
- **Stake:** 0.18u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** P(Over 2.5 goles)=85.5% frente a la implícita 47.9%; cuota justa 1.17 vs cuota capturada 2.09. Goles esperados del motor: 2.16 - 1.58. EV robusto +68.27% con cuota en perfil prioritario.
- **Riesgos:** Varianza intrínseca del fútbol; el EV depende de cuotas de mejor precio entre casas (puede no estar disponible al mismo precio). Córners/tarjetas no disponibles: no se evalúan esos mercados. Lesiones/suspensiones/alineaciones no verificables en vivo (fuentes no operativas) y no modeladas: no se descarta un cambio de última hora.
- **Fuentes:** Understat Serie A 2026 (xG real) + ClubElo + The Odds API (Udinese 1.28/2.16, Lecce 1.25/2.80); Elo 1690/1610; The Odds API cuota 2.09

### Pick 3: Angers vs Marseille
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.67
- **Probabilidad modelo:** 84.8%
- **Probabilidad conservadora:** 79.8%
- **Probabilidad implícita:** 59.9%
- **Cuota justa:** 1.18
- **Edge:** +41.68%
- **EV:** +41.68%
- **EV robusto:** +33.33%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.25
- **Stake:** 0.16u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** P(Over 2.5 goles)=84.8% frente a la implícita 59.9%; cuota justa 1.18 vs cuota capturada 1.67. Goles esperados del motor: 2.04 - 1.66. EV robusto +33.33% con cuota en perfil prioritario.
- **Riesgos:** Varianza intrínseca del fútbol; el EV depende de cuotas de mejor precio entre casas (puede no estar disponible al mismo precio). Córners/tarjetas no disponibles: no se evalúan esos mercados. Lesiones/suspensiones/alineaciones no verificables en vivo (fuentes no operativas) y no modeladas: no se descarta un cambio de última hora.
- **Fuentes:** Understat Ligue 1 2026 (xG real) + ClubElo + The Odds API (Angers 1.59/1.93, Marseille 1.63/2.24); Elo 1611/1759; The Odds API cuota 1.67

### Pick 4: Borussia Monchengladbach vs TSG Hoffenheim
- **Mercado:** over_3_5
- **Selección:** Over 3.5 Goles
- **Cuota:** 2.06
- **Probabilidad modelo:** 84.6%
- **Probabilidad conservadora:** 79.6%
- **Probabilidad implícita:** 48.5%
- **Cuota justa:** 1.18
- **Edge:** +74.32%
- **EV:** +74.32%
- **EV robusto:** +64.02%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.26
- **Stake:** 0.18u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** P(Over 3.5 goles)=84.6% frente a la implícita 48.5%; cuota justa 1.18 vs cuota capturada 2.06. Goles esperados del motor: 1.96 - 2.24. EV robusto +64.02% con cuota en perfil prioritario.
- **Riesgos:** Varianza intrínseca del fútbol; el EV depende de cuotas de mejor precio entre casas (puede no estar disponible al mismo precio). Córners/tarjetas no disponibles: no se evalúan esos mercados. Lesiones/suspensiones/alineaciones no verificables en vivo (fuentes no operativas) y no modeladas: no se descarta un cambio de última hora.
- **Fuentes:** Understat Bundesliga 2026 (xG real) + ClubElo + The Odds API (Borussia Monchengladbach 1.70/2.79, TSG Hoffenheim 1.93/1.97); Elo 1667/1713; The Odds API cuota 2.06

### Pick 5: Groningen vs Ajax
- **Mercado:** over_3_5
- **Selección:** Over 3.5 Goles
- **Cuota:** 1.99
- **Probabilidad modelo:** 83.4%
- **Probabilidad conservadora:** 78.4%
- **Probabilidad implícita:** 50.2%
- **Cuota justa:** 1.20
- **Edge:** +66.05%
- **EV:** +66.05%
- **EV robusto:** +56.10%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.27
- **Stake:** 0.17u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%; xG por proxy GF/GA (sin Understat)
- **Por qué:** P(Over 3.5 goles)=83.4% frente a la implícita 50.2%; cuota justa 1.20 vs cuota capturada 1.99. Goles esperados del motor: 2.0 - 2.12. EV robusto +56.10% con cuota en perfil prioritario.
- **Riesgos:** Varianza intrínseca del fútbol; el EV depende de cuotas de mejor precio entre casas (puede no estar disponible al mismo precio). Datos de entrada por proxy GF/GA (sin xG real): mayor incertidumbre estructural. Córners/tarjetas no disponibles: no se evalúan esos mercados. Lesiones/suspensiones/alineaciones no verificables en vivo (fuentes no operativas) y no modeladas: no se descarta un cambio de última hora.
- **Fuentes:** Wikipedia Eredivisie 2026 (proxy GF/GA) + ClubElo + The Odds API (Groningen 2.50/1.75, Ajax 2.75/1.25); Elo 1539/1679; The Odds API cuota 1.99

### Pick 6: Fiorentina vs Como
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.73
- **Probabilidad modelo:** 81.6%
- **Probabilidad conservadora:** 76.6%
- **Probabilidad implícita:** 57.8%
- **Cuota justa:** 1.23
- **Edge:** +41.10%
- **EV:** +41.10%
- **EV robusto:** +32.45%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.31
- **Stake:** 0.14u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** P(Over 2.5 goles)=81.6% frente a la implícita 57.8%; cuota justa 1.23 vs cuota capturada 1.73. Goles esperados del motor: 1.58 - 1.91. EV robusto +32.45% con cuota en perfil prioritario.
- **Riesgos:** Varianza intrínseca del fútbol; el EV depende de cuotas de mejor precio entre casas (puede no estar disponible al mismo precio). Córners/tarjetas no disponibles: no se evalúan esos mercados. Lesiones/suspensiones/alineaciones no verificables en vivo (fuentes no operativas) y no modeladas: no se descarta un cambio de última hora.
- **Fuentes:** Understat Serie A 2026 (xG real) + ClubElo + The Odds API (Fiorentina 1.41/1.83, Como 2.23/1.50); Elo 1715/1800; The Odds API cuota 1.73

## NO BET / Excluidos
- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**
  - FC Zwolle vs Go Ahead Eagles — Under 2.5 Goles (under_2_5): Prob modelo 12.0%, EV -67.97%, EV robusto -81.27% → sin value.
  - FC Zwolle vs Go Ahead Eagles — Over 1.5 Goles (over_1_5): Prob modelo 90.8%, EV +3.47%, EV robusto -2.23% → sin value.
  - FC Zwolle vs Go Ahead Eagles — Under 1.5 Goles (under_1_5): Prob modelo 9.2%, EV -44.28%, EV robusto -74.43% → sin value.
  - FC Zwolle vs Go Ahead Eagles — Under 3.5 Goles (under_3_5): Prob modelo 20.0%, EV -64.78%, EV robusto -73.58% → sin value.
  - Udinese vs Lecce — Under 2.5 Goles (under_2_5): Prob modelo 14.5%, EV -72.90%, EV robusto -82.25% → sin value.
  - Udinese vs Lecce — Under 1.5 Goles (under_1_5): Prob modelo 10.8%, EV -63.56%, EV robusto -80.46% → sin value.
  - Udinese vs Lecce — Under 3.5 Goles (under_3_5): Prob modelo 24.2%, EV -68.26%, EV robusto -74.81% → sin value.
  - CA Osasuna vs Real Racing Club de Santander — Under 2.5 Goles (under_2_5): Prob modelo 20.9%, EV -49.79%, EV robusto -61.79% → sin value.
  - CA Osasuna vs Real Racing Club de Santander — Over 1.5 Goles (over_1_5): Prob modelo 85.3%, EV +2.40%, EV robusto -3.60% → sin value.
  - CA Osasuna vs Real Racing Club de Santander — Under 1.5 Goles (under_1_5): Prob modelo 14.7%, EV -26.65%, EV robusto -51.65% → sin value.
  - CA Osasuna vs Real Racing Club de Santander — Under 3.5 Goles (under_3_5): Prob modelo 35.0%, EV -45.03%, EV robusto -52.88% → sin value.
  - SC Cambuur vs AZ Alkmaar — Under 2.5 Goles (under_2_5): Prob modelo 18.2%, EV -45.28%, EV robusto -60.28% → sin value.
  - SC Cambuur vs AZ Alkmaar — Over 1.5 Goles (over_1_5): Prob modelo 86.9%, EV -1.80%, EV robusto -7.45% → sin value.
  - SC Cambuur vs AZ Alkmaar — Under 1.5 Goles (under_1_5): Prob modelo 13.1%, EV -12.49%, EV robusto -45.89% → sin value.
  - SC Cambuur vs AZ Alkmaar — Under 3.5 Goles (under_3_5): Prob modelo 30.6%, EV -41.32%, EV robusto -50.92% → sin value.
  - Angers vs Marseille — Under 2.5 Goles (under_2_5): Prob modelo 15.2%, EV -63.62%, EV robusto -75.62% → sin value.
  - Angers vs Marseille — Under 1.5 Goles (under_1_5): Prob modelo 11.2%, EV -45.22%, EV robusto -69.72% → sin value.
  - Angers vs Marseille — Under 3.5 Goles (under_3_5): Prob modelo 25.4%, EV -60.68%, EV robusto -68.43% → sin value.
  - Fiorentina vs Como — Under 2.5 Goles (under_2_5): Prob modelo 18.4%, EV -57.77%, EV robusto -69.22% → sin value.
  - Fiorentina vs Como — Under 1.5 Goles (under_1_5): Prob modelo 13.2%, EV -39.33%, EV robusto -62.33% → sin value.
  - Fiorentina vs Como — Under 3.5 Goles (under_3_5): Prob modelo 30.9%, EV -53.33%, EV robusto -60.88% → sin value.
  - Bournemouth vs Sunderland — Under 2.5 Goles (under_2_5): Prob modelo 22.0%, EV -55.64%, EV robusto -65.74% → sin value.
  - Bournemouth vs Sunderland — Under 1.5 Goles (under_1_5): Prob modelo 15.3%, EV -42.20%, EV robusto -61.10% → sin value.
  - Bournemouth vs Sunderland — Under 3.5 Goles (under_3_5): Prob modelo 36.7%, EV -49.69%, EV robusto -56.54% → sin value.
  - Brighton and Hove Albion vs Crystal Palace — Under 2.5 Goles (under_2_5): Prob modelo 11.7%, EV -70.68%, EV robusto -83.23% → sin value.
  - Brighton and Hove Albion vs Crystal Palace — Under 1.5 Goles (under_1_5): Prob modelo 9.0%, EV -53.10%, EV robusto -79.10% → sin value.
  - Brighton and Hove Albion vs Crystal Palace — Under 3.5 Goles (under_3_5): Prob modelo 19.4%, EV -67.83%, EV robusto -76.13% → sin value.
  - Leeds United vs Manchester United — Under 2.5 Goles (under_2_5): Prob modelo 25.0%, EV -41.98%, EV robusto -53.58% → sin value.
  - Leeds United vs Manchester United — Over 1.5 Goles (over_1_5): Prob modelo 82.9%, EV +1.99%, EV robusto -4.16% → sin value.
  - Leeds United vs Manchester United — Under 1.5 Goles (under_1_5): Prob modelo 17.1%, EV -22.29%, EV robusto -45.04% → sin value.
  - Leeds United vs Manchester United — Under 3.5 Goles (under_3_5): Prob modelo 41.6%, EV -37.61%, EV robusto -45.11% → sin value.
  - Bayer Leverkusen vs SC Freiburg — Under 2.5 Goles (under_2_5): Prob modelo 21.9%, EV -40.35%, EV robusto -53.95% → sin value.
  - Bayer Leverkusen vs SC Freiburg — Over 1.5 Goles (over_1_5): Prob modelo 84.7%, EV -1.71%, EV robusto -7.51% → sin value.
  - Bayer Leverkusen vs SC Freiburg — Under 1.5 Goles (under_1_5): Prob modelo 15.3%, EV -8.38%, EV robusto -38.38% → sin value.
  - Bayer Leverkusen vs SC Freiburg — Under 3.5 Goles (under_3_5): Prob modelo 36.7%, EV -33.99%, EV robusto -42.99% → sin value.
  - Celta Vigo vs Alavés — Under 2.5 Goles (under_2_5): Prob modelo 45.4%, EV -19.12%, EV robusto -28.02% → sin value.
  - Celta Vigo vs Alavés — Over 1.5 Goles (over_1_5): Prob modelo 71.0%, EV +0.15%, EV robusto -6.90% → sin value.
  - Celta Vigo vs Alavés — Under 1.5 Goles (under_1_5): Prob modelo 29.0%, EV -9.61%, EV robusto -25.21% → sin value.
  - Celta Vigo vs Alavés — Under 3.5 Goles (under_3_5): Prob modelo 69.2%, EV -12.81%, EV robusto -19.11% → sin value.
  - Groningen vs Ajax — Under 2.5 Goles (under_2_5): Prob modelo 10.0%, EV -69.51%, EV robusto -84.71% → sin value.
  - Groningen vs Ajax — Over 1.5 Goles (over_1_5): Prob modelo 92.1%, EV +2.22%, EV robusto -3.33% → sin value.
  - Groningen vs Ajax — Under 1.5 Goles (under_1_5): Prob modelo 7.9%, EV -43.92%, EV robusto -79.37% → sin value.
  - Groningen vs Ajax — Under 3.5 Goles (under_3_5): Prob modelo 16.6%, EV -68.37%, EV robusto -77.92% → sin value.
  - Lorient vs AS Monaco — Over 2.5 Goles (over_2_5): Prob modelo 52.5%, EV +3.52%, EV robusto -6.33% → sin value.
  - Lorient vs AS Monaco — Under 2.5 Goles (under_2_5): Prob modelo 47.4%, EV -6.52%, EV robusto -16.37% → sin value.
  - Lorient vs AS Monaco — Over 1.5 Goles (over_1_5): Prob modelo 69.8%, EV -7.85%, EV robusto -14.45% → sin value.
  - Lorient vs AS Monaco — Over 3.5 Goles (over_3_5): Prob modelo 28.6%, EV -4.22%, EV robusto -20.97% → sin value.
  - Lorient vs AS Monaco — Under 3.5 Goles (under_3_5): Prob modelo 71.4%, EV -2.17%, EV robusto -9.02% → sin value.
  - Le Havre vs Auxerre — Under 2.5 Goles (under_2_5): Prob modelo 21.7%, EV -56.62%, EV robusto -66.62% → sin value.
  - Le Havre vs Auxerre — Under 1.5 Goles (under_1_5): Prob modelo 15.1%, EV -41.45%, EV robusto -60.80% → sin value.
  - Le Havre vs Auxerre — Under 3.5 Goles (under_3_5): Prob modelo 36.3%, EV -50.66%, EV robusto -57.46% → sin value.
  - Paris FC vs Rennes — Under 2.5 Goles (under_2_5): Prob modelo 22.3%, EV -48.69%, EV robusto -60.19% → sin value.
  - Paris FC vs Rennes — Over 1.5 Goles (over_1_5): Prob modelo 84.5%, EV +3.07%, EV robusto -3.03% → sin value.
  - Paris FC vs Rennes — Under 1.5 Goles (under_1_5): Prob modelo 15.5%, EV -30.16%, EV robusto -52.66% → sin value.
  - Paris FC vs Rennes — Under 3.5 Goles (under_3_5): Prob modelo 37.3%, EV -42.95%, EV robusto -50.60% → sin value.
  - Borussia Monchengladbach vs TSG Hoffenheim — Under 2.5 Goles (under_2_5): Prob modelo 9.3%, EV -71.48%, EV robusto -86.73% → sin value.
  - Borussia Monchengladbach vs TSG Hoffenheim — Over 1.5 Goles (over_1_5): Prob modelo 92.5%, EV +3.64%, EV robusto -1.96% → sin value.
  - Borussia Monchengladbach vs TSG Hoffenheim — Under 1.5 Goles (under_1_5): Prob modelo 7.5%, EV -51.51%, EV robusto -84.01% → sin value.
  - Borussia Monchengladbach vs TSG Hoffenheim — Under 3.5 Goles (under_3_5): Prob modelo 15.4%, EV -70.32%, EV robusto -79.97% → sin value.
  - Nottingham Forest vs Arsenal — Under 2.5 Goles (under_2_5): Prob modelo 25.0%, EV -50.08%, EV robusto -60.08% → sin value.
  - Nottingham Forest vs Arsenal — Under 1.5 Goles (under_1_5): Prob modelo 17.1%, EV -36.23%, EV robusto -54.93% → sin value.
  - Nottingham Forest vs Arsenal — Under 3.5 Goles (under_3_5): Prob modelo 41.5%, EV -43.55%, EV robusto -50.35% → sin value.
  - AC Milan vs Atalanta BC — Under 2.5 Goles (under_2_5): Prob modelo 23.0%, EV -50.46%, EV robusto -61.21% → sin value.
  - AC Milan vs Atalanta BC — Under 1.5 Goles (under_1_5): Prob modelo 16.0%, EV -32.80%, EV robusto -53.80% → sin value.
  - AC Milan vs Atalanta BC — Under 3.5 Goles (under_3_5): Prob modelo 38.5%, EV -43.86%, EV robusto -51.16% → sin value.
  - Málaga vs Real Sociedad — Under 2.5 Goles (under_2_5): Prob modelo 29.5%, EV -38.01%, EV robusto -48.51% → sin value.
  - Málaga vs Real Sociedad — Over 1.5 Goles (over_1_5): Prob modelo 80.3%, EV +1.99%, EV robusto -4.36% → sin value.
  - Málaga vs Real Sociedad — Under 1.5 Goles (under_1_5): Prob modelo 19.7%, EV -19.27%, EV robusto -39.77% → sin value.
  - Málaga vs Real Sociedad — Under 3.5 Goles (under_3_5): Prob modelo 48.5%, EV -30.70%, EV robusto -37.85% → sin value.
  - Racing Club vs Independiente — Under 2.5 Goles (under_2_5): Prob modelo 51.2%, EV -15.49%, EV robusto -23.74% → sin value.
  - Racing Club vs Independiente — Over 1.5 Goles (over_1_5): Prob modelo 67.5%, EV -2.11%, EV robusto -9.36% → sin value.
  - Racing Club vs Independiente — Under 1.5 Goles (under_1_5): Prob modelo 32.5%, EV -7.73%, EV robusto -21.93% → sin value.
  - Racing Club vs Independiente — Under 3.5 Goles (under_3_5): Prob modelo 75.3%, EV -9.65%, EV robusto -15.65% → sin value.
  - FC Twente Enschede vs FC Utrecht — Under 2.5 Goles (under_2_5): Prob modelo 12.1%, EV -60.59%, EV robusto -76.89% → sin value.
  - FC Twente Enschede vs FC Utrecht — Over 1.5 Goles (over_1_5): Prob modelo 90.7%, EV +0.63%, EV robusto -4.92% → sin value.
  - FC Twente Enschede vs FC Utrecht — Under 1.5 Goles (under_1_5): Prob modelo 9.3%, EV -34.25%, EV robusto -69.45% → sin value.
  - FC Twente Enschede vs FC Utrecht — Under 3.5 Goles (under_3_5): Prob modelo 20.1%, EV -59.82%, EV robusto -69.82% → sin value.
  - NEC Nijmegen vs Fortuna Sittard — Under 2.5 Goles (under_2_5): Prob modelo 18.2%, EV -46.43%, EV robusto -61.13% → sin value.
  - NEC Nijmegen vs Fortuna Sittard — Over 1.5 Goles (over_1_5): Prob modelo 87.0%, EV -2.62%, EV robusto -8.22% → sin value.
  - NEC Nijmegen vs Fortuna Sittard — Under 1.5 Goles (under_1_5): Prob modelo 13.1%, EV -14.13%, EV robusto -47.03% → sin value.
  - NEC Nijmegen vs Fortuna Sittard — Under 3.5 Goles (under_3_5): Prob modelo 30.5%, EV -42.58%, EV robusto -51.98% → sin value.
  - Lyon vs Nice — Under 2.5 Goles (under_2_5): Prob modelo 29.7%, EV -31.62%, EV robusto -43.12% → sin value.
  - Lyon vs Nice — Over 1.5 Goles (over_1_5): Prob modelo 80.1%, EV -2.23%, EV robusto -8.33% → sin value.
  - Lyon vs Nice — Under 1.5 Goles (under_1_5): Prob modelo 19.9%, EV -12.62%, EV robusto -34.62% → sin value.
  - Lyon vs Nice — Under 3.5 Goles (under_3_5): Prob modelo 48.8%, EV -27.33%, EV robusto -34.78% → sin value.
  - Juventus vs Lazio — Under 2.5 Goles (under_2_5): Prob modelo 31.6%, EV -38.66%, EV robusto -48.36% → sin value.
  - Juventus vs Lazio — Under 1.5 Goles (under_1_5): Prob modelo 21.0%, EV -24.75%, EV robusto -42.70% → sin value.
  - Juventus vs Lazio — Under 3.5 Goles (under_3_5): Prob modelo 51.5%, EV -30.96%, EV robusto -37.66% → sin value.
  - Real Madrid vs Sevilla — Under 2.5 Goles (under_2_5): Prob modelo 22.3%, EV -34.35%, EV robusto -49.05% → sin value.
  - Real Madrid vs Sevilla — Over 1.5 Goles (over_1_5): Prob modelo 84.4%, EV -3.77%, EV robusto -9.47% → sin value.
  - Real Madrid vs Sevilla — Under 1.5 Goles (under_1_5): Prob modelo 15.6%, EV +2.89%, EV robusto -30.11% → sin value.
  - Real Madrid vs Sevilla — Under 3.5 Goles (under_3_5): Prob modelo 37.3%, EV -31.33%, EV robusto -40.53% → sin value.
  - Estudiantes de Río Cuarto vs Aldosivi Mar del Plata — Under 2.5 Goles (under_2_5): Prob modelo 51.2%, EV -28.80%, EV robusto -35.75% → sin value.
  - Estudiantes de Río Cuarto vs Aldosivi Mar del Plata — Under 1.5 Goles (under_1_5): Prob modelo 32.5%, EV -21.05%, EV robusto -33.20% → sin value.
  - Estudiantes de Río Cuarto vs Aldosivi Mar del Plata — Under 3.5 Goles (under_3_5): Prob modelo 75.3%, EV -14.92%, EV robusto -20.57% → sin value.
  - Estudiantes vs San Lorenzo — Over 2.5 Goles (over_2_5): Prob modelo 31.1%, EV -15.52%, EV robusto -29.12% → sin value.
  - Estudiantes vs San Lorenzo — Under 2.5 Goles (under_2_5): Prob modelo 68.9%, EV -0.73%, EV robusto -7.93% → sin value.
  - Estudiantes vs San Lorenzo — Over 1.5 Goles (over_1_5): Prob modelo 55.4%, EV -12.42%, EV robusto -20.32% → sin value.
  - Estudiantes vs San Lorenzo — Over 3.5 Goles (over_3_5): Prob modelo 10.6%, EV -37.90%, EV robusto -67.25% → sin value.
  - Estudiantes vs San Lorenzo — Under 3.5 Goles (under_3_5): Prob modelo 89.4%, EV +1.94%, EV robusto -3.76% → sin value.
  - FC Cincinnati vs Columbus Crew SC — Under 2.5 Goles (under_2_5): Prob modelo 13.0%, EV -59.02%, EV robusto -74.77% → sin value.
  - FC Cincinnati vs Columbus Crew SC — Over 1.5 Goles (over_1_5): Prob modelo 90.2%, EV +0.09%, EV robusto -5.46% → sin value.
  - FC Cincinnati vs Columbus Crew SC — Under 1.5 Goles (under_1_5): Prob modelo 9.8%, EV -31.19%, EV robusto -66.19% → sin value.
  - FC Cincinnati vs Columbus Crew SC — Under 3.5 Goles (under_3_5): Prob modelo 21.7%, EV -55.75%, EV robusto -65.95% → sin value.
  - Belgrano de Cordoba vs River Plate — Over 2.5 Goles (over_2_5): Prob modelo 39.2%, EV -0.90%, EV robusto -13.55% → sin value.
  - Belgrano de Cordoba vs River Plate — Under 2.5 Goles (under_2_5): Prob modelo 60.8%, EV -6.32%, EV robusto -14.02% → sin value.
  - Belgrano de Cordoba vs River Plate — Over 1.5 Goles (over_1_5): Prob modelo 61.3%, EV -5.63%, EV robusto -13.33% → sin value.
  - Belgrano de Cordoba vs River Plate — Under 1.5 Goles (under_1_5): Prob modelo 38.7%, EV -4.36%, EV robusto -16.71% → sin value.
  - Belgrano de Cordoba vs River Plate — Over 3.5 Goles (over_3_5): Prob modelo 16.2%, EV -19.24%, EV robusto -44.09% → sin value.
  - Belgrano de Cordoba vs River Plate — Under 3.5 Goles (under_3_5): Prob modelo 83.8%, EV -0.34%, EV robusto -6.29% → sin value.
- **Candidatos con value excluidos por probabilidad-primero:**
  - FC Zwolle vs Go Ahead Eagles: Over 2.5 Goles (over_2_5) EV +27.54% / EV rob +20.29%, Over 3.5 Goles (over_3_5) EV +77.58% / EV rob +66.48%, Doble Oportunidad Empate/Go Ahead Eagles (x2) EV +11.87% / EV rob +5.32%, Doble Oportunidad FC Zwolle/Go Ahead Eagles (12) EV +2.55% / EV rob -3.85% — No cumple los mínimos de selección probabilidad-primero.
  - Udinese vs Lecce: Victoria Lecce (2) EV +42.44% / EV rob +17.94%, Over 1.5 Goles (over_1_5) EV +22.23% / EV rob +15.38%, Doble Oportunidad Empate/Lecce (x2) EV +3.36% / EV rob -6.89%, Doble Oportunidad Udinese/Lecce (12) EV +3.82% / EV rob -2.78%, Over 3.5 Goles (over_3_5) EV +187.93% / EV rob +168.93% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - CA Osasuna vs Real Racing Club de Santander: Over 3.5 Goles (over_3_5) EV +67.02% / EV rob +54.17%, Doble Oportunidad Empate/Real Racing Club de Santander (x2) EV +9.04% / EV rob -0.36%, Victoria Real Racing Club de Santander (2) EV +32.32% / EV rob +13.22% — No cumple los mínimos de selección probabilidad-primero.
  - SC Cambuur vs AZ Alkmaar: Victoria AZ Alkmaar (2) EV +7.86% / EV rob +0.26%, Over 2.5 Goles (over_2_5) EV +12.83% / EV rob +5.93%, Doble Oportunidad Empate/AZ Alkmaar (x2) EV +2.82% / EV rob -2.88% — No cumple los mínimos de selección probabilidad-primero.
  - Angers vs Marseille: Over 1.5 Goles (over_1_5) EV +7.47% / EV rob +1.42%, Over 3.5 Goles (over_3_5) EV +94.04% / EV rob +81.04%, Ambos marcan (BTTS) (btts_yes) EV +10.54% / EV rob +2.74%, Doble Oportunidad Angers/Empate (1x) EV +8.43% / EV rob -0.82%, Victoria Angers (1) EV +33.61% / EV rob +15.11% — No cumple los mínimos de selección probabilidad-primero.
  - Fiorentina vs Como: Over 1.5 Goles (over_1_5) EV +6.78% / EV rob +0.63%, Over 3.5 Goles (over_3_5) EV +88.62% / EV rob +74.97%, Ambos marcan (BTTS) (btts_yes) EV +10.40% / EV rob +2.30%, Doble Oportunidad Empate/Como (x2) EV +5.19% / EV rob -1.51%, Doble Oportunidad Fiorentina/Como (12) EV +2.05% / EV rob -4.55% — No cumple los mínimos de selección probabilidad-primero.
  - Bournemouth vs Sunderland: Victoria Sunderland (2) EV +23.53% / EV rob +4.78%, Over 1.5 Goles (over_1_5) EV +10.12% / EV rob +3.62%, Doble Oportunidad Bournemouth/Sunderland (12) EV +3.10% / EV rob -3.60%, Over 3.5 Goles (over_3_5) EV +108.82% / EV rob +92.32% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Brighton and Hove Albion vs Crystal Palace: Victoria Crystal Palace (2) EV +43.07% / EV rob +9.07%, Over 1.5 Goles (over_1_5) EV +8.27% / EV rob +2.32%, Over 3.5 Goles (over_3_5) EV +99.94% / EV rob +87.54%, Doble Oportunidad Empate/Crystal Palace (x2) EV +10.62% / EV rob -2.98% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Leeds United vs Manchester United: Over 3.5 Goles (over_3_5) EV +59.46% / EV rob +45.81%, Victoria Manchester United (2) EV +38.87% / EV rob +23.62% — No cumple los mínimos de selección probabilidad-primero.
  - Bayer Leverkusen vs SC Freiburg: Empate (X) EV +8.95% / EV rob -14.55%, Over 2.5 Goles (over_2_5) EV +14.76% / EV rob +7.41%, Over 3.5 Goles (over_3_5) EV +43.76% / EV rob +32.41%, Doble Oportunidad Empate/SC Freiburg (x2) EV +26.75% / EV rob +15.35%, Victoria SC Freiburg (2) EV +58.81% / EV rob +34.31% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Celta Vigo vs Alavés: Over 2.5 Goles (over_2_5) EV +28.76% / EV rob +16.96%, Over 3.5 Goles (over_3_5) EV +29.36% / EV rob +8.36%, Victoria Alavés (2) EV +54.38% / EV rob +35.98% — No cumple los mínimos de selección probabilidad-primero.
  - Groningen vs Ajax: Victoria Ajax (2) EV +5.95% / EV rob -3.90%, Over 2.5 Goles (over_2_5) EV +22.36% / EV rob +15.56%, Ambos marcan (BTTS) (btts_yes) EV +10.19% / EV rob +2.99% — No cumple los mínimos de selección probabilidad-primero.
  - Lorient vs AS Monaco: Victoria Lorient (1) EV +26.40% / EV rob +6.65%, Empate (X) EV +4.90% / EV rob -13.10%, Under 1.5 Goles (under_1_5) EV +13.21% / EV rob -5.54%, No ambos marcan (btts_no) EV +7.93% / EV rob -2.67%, Doble Oportunidad Lorient/Empate (1x) EV +11.27% / EV rob +2.17% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Le Havre vs Auxerre: Over 1.5 Goles (over_1_5) EV +10.33% / EV rob +3.83%, Ambos marcan (BTTS) (btts_yes) EV +13.59% / EV rob +4.94%, Doble Oportunidad Empate/Auxerre (x2) EV +4.63% / EV rob -3.67%, Doble Oportunidad Le Havre/Auxerre (12) EV +2.55% / EV rob -4.20%, Victoria Auxerre (2) EV +28.67% / EV rob +12.17%, Over 3.5 Goles (over_3_5) EV +106.45% / EV rob +90.25% — No cumple los mínimos de selección probabilidad-primero.
  - Paris FC vs Rennes: Victoria Paris FC (1) EV +10.42% / EV rob -1.43%, Over 3.5 Goles (over_3_5) EV +59.28% / EV rob +46.58%, Doble Oportunidad Paris FC/Rennes (12) EV +3.65% / EV rob -3.15% — No cumple los mínimos de selección probabilidad-primero.
  - Borussia Monchengladbach vs TSG Hoffenheim: Victoria TSG Hoffenheim (2) EV +20.37% / EV rob +9.27%, Over 2.5 Goles (over_2_5) EV +26.91% / EV rob +19.91%, Ambos marcan (BTTS) (btts_yes) EV +10.28% / EV rob +3.13%, Doble Oportunidad Empate/TSG Hoffenheim (x2) EV +4.62% / EV rob -2.38% — No cumple los mínimos de selección probabilidad-primero.
  - Nottingham Forest vs Arsenal: Victoria Nottingham Forest (1) EV +99.78% / EV rob +65.78%, Over 1.5 Goles (over_1_5) EV +9.49% / EV rob +2.89%, Doble Oportunidad Nottingham Forest/Empate (1x) EV +25.93% / EV rob +14.03%, Over 3.5 Goles (over_3_5) EV +101.79% / EV rob +84.54% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - AC Milan vs Atalanta BC: Over 1.5 Goles (over_1_5) EV +5.84% / EV rob -0.46%, Over 3.5 Goles (over_3_5) EV +81.57% / EV rob +66.82%, Doble Oportunidad AC Milan/Empate (1x) EV +4.91% / EV rob -1.34%, Doble Oportunidad AC Milan/Atalanta BC (12) EV +2.57% / EV rob -3.93% — No cumple los mínimos de selección probabilidad-primero.
  - Málaga vs Real Sociedad: Victoria Real Sociedad (2) EV +8.11% / EV rob -2.99%, Over 3.5 Goles (over_3_5) EV +57.20% / EV rob +41.95% — No cumple los mínimos de selección probabilidad-primero.
  - Racing Club vs Independiente: Over 2.5 Goles (over_2_5) EV +14.63% / EV rob +2.88%, Over 3.5 Goles (over_3_5) EV +16.14% / EV rob -7.36%, Victoria Independiente (2) EV +54.20% / EV rob +35.20% — No cumple los mínimos de selección probabilidad-primero.
  - FC Twente Enschede vs FC Utrecht: Victoria FC Utrecht (2) EV +9.65% / EV rob -32.85%, Empate (X) EV +7.97% / EV rob -22.53%, Over 2.5 Goles (over_2_5) EV +16.92% / EV rob +10.27%, Ambos marcan (BTTS) (btts_yes) EV +8.90% / EV rob +0.75% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - NEC Nijmegen vs Fortuna Sittard: Empate (X) EV +3.18% / EV rob -19.82%, Over 2.5 Goles (over_2_5) EV +12.86% / EV rob +5.96%, Doble Oportunidad Empate/Fortuna Sittard (x2) EV +33.45% / EV rob +22.10%, Victoria Fortuna Sittard (2) EV +74.53% / EV rob +50.53% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Lyon vs Nice: Victoria Lyon (1) EV +10.60% / EV rob +1.15%, Over 3.5 Goles (over_3_5) EV +38.83% / EV rob +25.28% — No cumple los mínimos de selección probabilidad-primero.
  - Juventus vs Lazio: Victoria Lazio (2) EV +20.81% / EV rob -8.19%, Over 1.5 Goles (over_1_5) EV +5.91% / EV rob -0.79%, Ambos marcan (BTTS) (btts_yes) EV +10.90% / EV rob +0.90%, Doble Oportunidad Empate/Lazio (x2) EV +3.42% / EV rob -8.13%, Over 3.5 Goles (over_3_5) EV +72.10% / EV rob +54.35% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Real Madrid vs Sevilla: Victoria Sevilla (2) EV +58.62% / EV rob -11.38%, Empate (X) EV +43.49% / EV rob +6.49%, Over 2.5 Goles (over_2_5) EV +10.29% / EV rob +3.19%, Ambos marcan (BTTS) (btts_yes) EV +13.86% / EV rob +4.16%, Doble Oportunidad Empate/Sevilla (x2) EV +35.17% / EV rob +13.17% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Estudiantes de Río Cuarto vs Aldosivi Mar del Plata: Victoria Estudiantes de Río Cuarto (1) EV +14.41% / EV rob -0.84%, Over 2.5 Goles (over_2_5) EV +39.02% / EV rob +24.77%, Over 1.5 Goles (over_1_5) EV +8.02% / EV rob +0.02%, Over 3.5 Goles (over_3_5) EV +57.40% / EV rob +25.55% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Estudiantes vs San Lorenzo: Victoria Estudiantes (1) EV +23.23% / EV rob +11.13%, Under 1.5 Goles (under_1_5) EV +6.97% / EV rob -5.03%, No ambos marcan (btts_no) EV +8.02% / EV rob -0.08%, Doble Oportunidad Estudiantes/Empate (1x) EV +5.33% / EV rob -1.07% — No cumple los mínimos de selección probabilidad-primero.
  - FC Cincinnati vs Columbus Crew SC: Victoria Columbus Crew SC (2) EV +17.21% / EV rob +3.46%, Over 2.5 Goles (over_2_5) EV +17.44% / EV rob +10.69%, Doble Oportunidad Empate/Columbus Crew SC (x2) EV +4.39% / EV rob -3.71% — No cumple los mínimos de selección probabilidad-primero.
  - Belgrano de Cordoba vs River Plate: Victoria Belgrano de Cordoba (1) EV +55.02% / EV rob +36.77% — Cuota alta admitida solo como excepción robusta.

## Portfolio y Correlaciones
- **Exposición total:** 1.00u
- **Correlaciones detectadas:** Mercados presentes: over_2_5, over_3_5. Verificar solapamiento de mercado mismo partido.
- **Ajuste de stake por correlación:** Los picks pertenecen a partidos distintos; no se aplica reducción adicional por eventos dependientes.

## Tracking
_Fuente: resultados vía websearch (MCP apifootball no operativo — fallback activo). Actualizado 2026-10-23._
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1 (Brighton and Hove Albion vs Crystal Palace - over_2_5) | GANADA | 5 - 0 | +0.11u |
| Pick 2 (Udinese vs Lecce - over_2_5) | GANADA | 0 - 3 | +0.20u |
| Pick 3 (Angers vs Marseille - over_2_5) | GANADA | 2 - 5 | +0.11u |
| Pick 4 (Borussia Monchengladbach vs TSG Hoffenheim - over_3_5) | PERDIDA | 1 - 2 | -0.18u |
| Pick 5 (Groningen vs Ajax - over_3_5) | GANADA | 2 - 5 | +0.17u |
| Pick 6 (Fiorentina vs Como - over_2_5) | GANADA | 1 - 3 | +0.10u |
| **Total** | | | **+0.51u (5 G / 1 P)** |
