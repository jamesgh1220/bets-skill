# Análisis de Apuestas — 2026-09-19

## Metadatos
- **Fecha de análisis:** 2026-09-19T02:29:10Z
- **Fecha(s) de partido:** 2026-09-19
- **Information cutoff:** 2026-09-19T02:29:10Z
- **Modelo de IA:** bigpickle
- **Versión del motor predictivo:** model-v1.3
- **Ligas analizadas:** Premier League, Bundesliga, Ligue 1, Serie A, La Liga, Eredivisie, Primeira Liga, MLS, Liga Argentina (Primera División), Liga Colombiana (Primera A)
- **Rango de fechas solicitado:** 19 de septiembre de 2026 (un día)
- **Partidos en universo:** 53
- **Picks iniciales con value:** 136
- **Picks finales seleccionados:** 6

## Universo Analizado
Universo = 53 partidos del 2026-09-19 por liga solicitada (todos los partidos de las ligas en la fecha: The Odds API REST). Cuotas capa 1: The Odds API vía REST (fallback documentado; el MCP `odds-api` no estaba operativo) — plan gratis expone solo h2h y totals (2.5/3.5). Timestamp de captura de cuotas: 2026-09-18T21:22Z (referencia CLV). El MCP `apifootball` estaba inoperativo ('Authentification failed!'); el MCP local `football-stats` devolvió MISSING_SOURCE. xG: Understat (big-5), Statz.ai (Eredivisie y Liga Prof Argentina), FotMob/Opta (Primeira Liga), ASA (MLS), apwin.com (Colombia; Alianza FC proxy GF/GA). Elo: ClubElo para 98 equipos; Colombia estimado por regresión elo=70.3*xgd+1664.7 (r2=0.22, n=93) -> `elo_estimado`. Liga Colombiana no disponible en The Odds API: cuotas h2h tomadas del agregador football-predictions.ai (Pinnacle/best, Capa 3), solo 1X2 (totals n/d). Mercados sin cuota capturada (1.5 goles, BTTS, DO, DNB, córners, tarjetas): n/d, nunca inventados. Córners/tarjetas: tasas de ambos equipos no disponibles (librería parcial cubre 5 equipos sin ningún partido con ambas escuadras); los 8 campos quedan `null` y se documenta 'corners/cards no disponibles' -> mercados no disponibles, nunca omitidos silenciosamente.
- **Tottenham Hotspur vs Aston Villa, Brighton vs Arsenal, Everton vs Ipswich, Newcastle vs Hull City, Nottingham Forest vs Coventry City** (Premier League) — 5 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Hamburger SV vs 1. FC Köln, Werder Bremen vs Augsburg, Gladbach vs Mainz, Eintracht Frankfurt vs SC Freiburg, VfB Stuttgart vs Borussia Dortmund** (Bundesliga) — 5 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Osasuna vs Rayo Vallecano, Athletic Bilbao vs Alavés, Celta Vigo vs Racing Santander, Sevilla vs Barcelona** (La Liga) — 4 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Bologna vs Torino, Udinese vs Cagliari, AS Roma vs Inter Milan, Venezia vs Lazio** (Serie A) — 4 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Paris FC vs Strasbourg, Angers vs Troyes, Toulouse vs Le Havre, Le Mans FC vs Lorient, Lyon vs Rennes** (Ligue 1) — 5 partidos — cuotas 1X2 y totals (2.5/3.5).
- **ADO Den Haag vs SC Cambuur, Sparta Rotterdam vs Heerenveen, Ajax vs Excelsior, Willem II vs Fortuna Sittard** (Eredivisie) — 4 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Gil Vicente vs CS Maritimo, Nacional vs Famalicão, Alverca vs Rio Ave, Sporting Lisbon vs Arouca** (Primeira Liga) — 4 partidos — cuotas 1X2 y totals (2.5/3.5).
- **Gimnasia La Plata vs Banfield, Gimnasia Mendoza vs Deportivo Riestra, Unión vs Independiente, River Plate vs Atlético Huracán, Instituto vs Talleres** (Liga Argentina) — 5 partidos — cuotas 1X2 y totals (2.5/3.5).
- **13 partidos MLS** (CF Montreal vs Columbus, D.C. United vs Charlotte, San Jose vs LAFC, New England vs Orlando, FC Dallas vs Austin, Houston vs Cincinnati, Minnesota vs LA Galaxy, Sporting KC vs Philadelphia, St. Louis vs Toronto, Nashville vs Chicago, Colorado vs Seattle, Real Salt Lake vs Vancouver, Portland vs Atlanta) — cuotas 1X2 y totals (2.5/3.5).
- **Millonarios vs Boyacá Chicó, Alianza FC vs Santa Fe, Deportivo Cali vs Cúcuta, Deportivo Pasto vs Once Caldas** (Liga Colombiana, Clausura jornada 11) — 4 partidos — solo h2h (Capa 3, agregador football-predictions.ai; Pinnacle como principal).

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | VfB Stuttgart vs Borussia Dortmund | over_2_5 | Over 2.5 Goles | excluido | 1.38 | 93.5% | 1.07 | +28.99% | +28.99% | +22.09% | 0.19u | Media-Alta |
| 2 | AS Roma vs Inter Milan | over_2_5 | Over 2.5 Goles | prioritario | 1.66 | 92.0% | 1.09 | +52.79% | +52.79% | +44.49% | 0.20u | Media-Alta |
| 3 | VfB Stuttgart vs Borussia Dortmund | over_3_5 | Over 3.5 Goles | prioritario | 1.99 | 89.5% | 1.12 | +78.05% | +78.05% | +68.10% | 0.20u | Media-Alta |
| 4 | Borussia Monchengladbach vs FSV Mainz 05 | over_2_5 | Over 2.5 Goles | prioritario | 1.55 | 87.7% | 1.14 | +35.98% | +35.98% | +28.23% | 0.16u | Media-Alta |
| 5 | Sevilla vs Barcelona | over_2_5 | Over 2.5 Goles | excluido | 1.28 | 87.2% | 1.15 | +11.59% | +11.59% | +5.19% | 0.10u | Media-Alta |
| 6 | AS Roma vs Inter Milan | over_3_5 | Over 3.5 Goles | excluido | 2.35 | 87.0% | 1.15 | +104.47% | +104.47% | +92.72% | 0.19u | Media-Alta |
| 7 | Venezia vs Lazio | over_2_5 | Over 2.5 Goles | prioritario | 1.80 | 86.9% | 1.15 | +56.46% | +56.46% | +47.46% | 0.18u | Media-Alta |
| 8 | Werder Bremen vs Augsburg | over_2_5 | Over 2.5 Goles | excluido | 1.44 | 85.9% | 1.16 | +23.68% | +23.68% | +16.48% | 0.13u | Media-Alta |
| 9 | Hamburger SV vs 1. FC Köln | over_2_5 | Over 2.5 Goles | prioritario | 1.65 | 85.2% | 1.17 | +40.56% | +40.56% | +32.31% | 0.16u | Media-Alta |
| 10 | Brighton and Hove Albion vs Arsenal | over_2_5 | Over 2.5 Goles | prioritario | 1.84 | 85.0% | 1.18 | +56.38% | +56.38% | +47.18% | 0.17u | Media-Alta |
| 11 | Willem II vs Fortuna Sittard | over_2_5 | Over 2.5 Goles | prioritario | 1.54 | 84.4% | 1.18 | +29.98% | +29.98% | +22.28% | 0.14u | Media-Alta |
| 12 | Sparta Rotterdam vs Heerenveen | over_2_5 | Over 2.5 Goles | excluido | 1.45 | 83.6% | 1.20 | +21.19% | +21.19% | +13.94% | 0.12u | Media-Alta |
| 13 | Minnesota United FC vs LA Galaxy | over_2_5 | Over 2.5 Goles | excluido | 1.39 | 81.4% | 1.23 | +13.20% | +13.20% | +6.25% | 0.08u | Media-Alta |
| 14 | New England Revolution vs Orlando City SC | over_2_5 | Over 2.5 Goles | excluido | 1.41 | 80.6% | 1.24 | +13.70% | +13.70% | +6.65% | 0.08u | Media-Alta |
| 15 | Sporting Kansas City vs Philadelphia Union | over_2_5 | Over 2.5 Goles | excluido | 1.43 | 80.5% | 1.24 | +15.19% | +15.19% | +8.04% | 0.09u | Media-Alta |
| 16 | San Jose Earthquakes vs Los Angeles FC | over_2_5 | Over 2.5 Goles | prioritario | 1.50 | 80.2% | 1.25 | +20.28% | +20.28% | +12.78% | 0.10u | Media-Alta |
| 17 | Eintracht Frankfurt vs SC Freiburg | over_2_5 | Over 2.5 Goles | excluido | 1.44 | 80.0% | 1.25 | +15.20% | +15.20% | +8.00% | 0.09u | Media-Alta |
| 18 | Borussia Monchengladbach vs FSV Mainz 05 | over_3_5 | Over 3.5 Goles | excluido | 2.34 | 79.6% | 1.26 | +86.26% | +86.26% | +74.56% | 0.16u | Media-Alta |
| 19 | Udinese vs Cagliari | over_2_5 | Over 2.5 Goles | prioritario | 2.16 | 79.3% | 1.26 | +71.40% | +71.40% | +60.60% | 0.15u | Media-Alta |
| 20 | Lyon vs Rennes | over_2_5 | Over 2.5 Goles | prioritario | 1.54 | 79.2% | 1.26 | +22.05% | +22.05% | +14.34% | 0.10u | Media-Alta |
| 21 | Portland Timbers vs Atlanta United FC | over_2_5 | Over 2.5 Goles | excluido | 1.49 | 79.1% | 1.26 | +17.93% | +17.93% | +10.48% | 0.09u | Media-Alta |
| 22 | Real Salt Lake vs Vancouver Whitecaps FC | over_2_5 | Over 2.5 Goles | prioritario | 1.52 | 79.1% | 1.26 | +20.17% | +20.17% | +12.57% | 0.10u | Media-Alta |
| 23 | Sevilla vs Barcelona | over_3_5 | Over 3.5 Goles | prioritario | 1.74 | 78.6% | 1.27 | +36.85% | +36.85% | +28.15% | 0.12u | Media-Alta |
| 24 | Paris FC vs Strasbourg | over_2_5 | Over 2.5 Goles | prioritario | 1.70 | 78.3% | 1.28 | +33.18% | +33.18% | +24.68% | 0.12u | Media-Alta |
| 25 | Le Mans FC vs Lorient | over_2_5 | Over 2.5 Goles | prioritario | 1.84 | 77.5% | 1.29 | +42.51% | +42.51% | +33.31% | 0.13u | Media-Alta |
| 26 | D.C. United vs Charlotte FC | over_2_5 | Over 2.5 Goles | prioritario | 1.62 | 77.0% | 1.30 | +24.82% | +24.82% | +16.72% | 0.10u | Media-Alta |
| 27 | Werder Bremen vs Augsburg | over_3_5 | Over 3.5 Goles | prioritario | 2.07 | 76.4% | 1.31 | +58.17% | +58.17% | +47.82% | 0.14u | Media-Alta |
| 28 | Toulouse vs Le Havre | over_2_5 | Over 2.5 Goles | prioritario | 1.76 | 76.3% | 1.31 | +34.25% | +34.25% | +25.45% | 0.11u | Media-Alta |
| 29 | CA Osasuna vs Rayo Vallecano | over_2_5 | Over 2.5 Goles | prioritario | 2.15 | 76.1% | 1.31 | +63.55% | +63.55% | +52.80% | 0.14u | Media-Alta |
| 30 | Everton vs Ipswich Town | over_2_5 | Over 2.5 Goles | prioritario | 1.79 | 76.0% | 1.32 | +35.99% | +35.99% | +27.04% | 0.11u | Media-Alta |
| 31 | Nashville SC vs Chicago Fire | over_2_5 | Over 2.5 Goles | prioritario | 1.55 | 75.6% | 1.32 | +17.24% | +17.24% | +9.49% | 0.08u | Media-Alta |
| 32 | Angers vs Troyes | over_2_5 | Over 2.5 Goles | prioritario | 2.04 | 75.6% | 1.32 | +54.29% | +54.29% | +44.09% | 0.13u | Media-Alta |
| 33 | FC Dallas vs Austin FC | over_2_5 | Over 2.5 Goles | prioritario | 1.55 | 75.6% | 1.32 | +17.23% | +17.23% | +9.48% | 0.08u | Media-Alta |
| 34 | Hamburger SV vs 1. FC Köln | over_3_5 | Over 3.5 Goles | excluido | 2.30 | 75.2% | 1.33 | +73.05% | +73.05% | +61.55% | 0.14u | Media-Alta |
| 35 | ADO Den Haag vs SC Cambuur | over_2_5 | Over 2.5 Goles | excluido | 1.48 | 75.1% | 1.33 | +11.12% | +11.12% | +3.72% | 0.06u | Media-Alta |
| 36 | Athletic Bilbao vs Alavés | over_2_5 | Over 2.5 Goles | prioritario | 1.97 | 74.6% | 1.34 | +47.02% | +47.02% | +37.17% | 0.12u | Media-Alta |
| 37 | Houston Dynamo vs FC Cincinnati | over_2_5 | Over 2.5 Goles | excluido | 1.52 | 74.1% | 1.35 | +12.56% | +12.56% | +4.96% | 0.06u | Media-Alta |
| 38 | Willem II vs Fortuna Sittard | over_3_5 | Over 3.5 Goles | excluido | 2.38 | 73.9% | 1.35 | +75.83% | +75.83% | +63.93% | 0.14u | Media-Alta |
| 39 | Celta Vigo vs Real Racing Club de Santander | over_2_5 | Over 2.5 Goles | prioritario | 1.68 | 72.8% | 1.37 | +22.22% | +22.22% | +13.82% | 0.08u | Media-Alta |
| 40 | Colorado Rapids vs Seattle Sounders FC | over_2_5 | Over 2.5 Goles | prioritario | 1.77 | 72.5% | 1.38 | +28.31% | +28.31% | +19.46% | 0.09u | Media-Alta |
| 41 | Sparta Rotterdam vs Heerenveen | over_3_5 | Over 3.5 Goles | excluido | 2.26 | 72.5% | 1.38 | +63.80% | +63.80% | +52.50% | 0.13u | Media-Alta |
| 42 | Tottenham Hotspur vs Aston Villa | over_2_5 | Over 2.5 Goles | prioritario | 1.84 | 71.1% | 1.41 | +30.86% | +30.86% | +21.66% | 0.09u | Media-Alta |
| 43 | CF Montreal vs Columbus Crew SC | over_2_5 | Over 2.5 Goles | prioritario | 1.64 | 70.6% | 1.42 | +15.80% | +15.80% | +7.60% | 0.06u | Media-Alta |
| 44 | Borussia Monchengladbach vs FSV Mainz 05 | 2 | Victoria FSV Mainz 05 | excluido | 2.30 | 70.4% | 1.42 | +61.94% | +61.94% | +50.44% | 0.12u | Media-Alta |
| 45 | Minnesota United FC vs LA Galaxy | over_3_5 | Over 3.5 Goles | prioritario | 2.05 | 68.9% | 1.45 | +41.22% | +41.22% | +30.97% | 0.10u | Media-Alta |
| 46 | Nottingham Forest vs Coventry City | over_2_5 | Over 2.5 Goles | prioritario | 1.87 | 68.1% | 1.47 | +27.27% | +27.27% | +17.92% | 0.08u | Media-Alta |
| 47 | New England Revolution vs Orlando City SC | over_3_5 | Over 3.5 Goles | prioritario | 2.16 | 67.6% | 1.48 | +45.93% | +45.93% | +35.13% | 0.10u | Media-Alta |
| 48 | Sporting Kansas City vs Philadelphia Union | over_3_5 | Over 3.5 Goles | prioritario | 2.14 | 67.4% | 1.48 | +44.26% | +44.26% | +33.56% | 0.10u | Media-Alta |
| 49 | San Jose Earthquakes vs Los Angeles FC | over_3_5 | Over 3.5 Goles | excluido | 2.34 | 66.8% | 1.50 | +56.34% | +56.34% | +44.64% | 0.11u | Media-Alta |
| 50 | Bologna vs Torino | over_2_5 | Over 2.5 Goles | prioritario | 2.12 | 66.8% | 1.50 | +41.64% | +41.64% | +31.04% | 0.09u | Media-Alta |
| 51 | Newcastle United vs Hull City | over_2_5 | Over 2.5 Goles | prioritario | 1.70 | 66.8% | 1.50 | +13.58% | +13.58% | +5.08% | 0.05u | Media-Alta |
| 52 | Eintracht Frankfurt vs SC Freiburg | over_3_5 | Over 3.5 Goles | prioritario | 2.15 | 66.5% | 1.50 | +42.98% | +42.98% | +32.22% | 0.09u | Media-Alta |
| 53 | Lyon vs Rennes | over_3_5 | Over 3.5 Goles | excluido | 2.42 | 65.3% | 1.53 | +57.95% | +57.95% | +45.85% | 0.10u | Media-Alta |
| 54 | Portland Timbers vs Atlanta United FC | over_3_5 | Over 3.5 Goles | excluido | 2.28 | 65.1% | 1.54 | +48.45% | +48.45% | +37.05% | 0.09u | Media-Alta |
| 55 | Alverca vs Rio Ave FC | over_2_5 | Over 2.5 Goles | prioritario | 2.07 | 65.1% | 1.54 | +34.69% | +34.69% | +24.34% | 0.08u | Media-Alta |
| 56 | Real Salt Lake vs Vancouver Whitecaps FC | over_3_5 | Over 3.5 Goles | excluido | 2.40 | 64.9% | 1.54 | +55.83% | +55.83% | +43.83% | 0.10u | Media-Alta |
| 57 | Ajax vs Excelsior | over_3_5 | Over 3.5 Goles | excluido | 1.69 | 64.6% | 1.55 | +9.17% | +9.17% | +0.72% | 0.03u | Media-Alta |
| 58 | Nottingham Forest vs Coventry City | 1 | Victoria Nottingham Forest | excluido | 1.70 | 62.9% | 1.59 | +6.96% | +6.96% | -1.54% | 0.02u | Media-Alta |
| 59 | Sporting Kansas City vs Philadelphia Union | 2 | Victoria Philadelphia Union | excluido | 1.65 | 62.9% | 1.59 | +3.80% | +3.80% | -4.45% | 0.01u | Media-Alta |
| 60 | Nacional vs Famalicão | over_2_5 | Over 2.5 Goles | excluido | 2.28 | 62.6% | 1.60 | +42.82% | +42.82% | +31.42% | 0.08u | Media-Alta |
| 61 | Paris FC vs Strasbourg | 1 | Victoria Paris FC | prioritario | 2.08 | 62.3% | 1.61 | +29.56% | +29.56% | +19.16% | 0.07u | Media-Alta |
| 62 | VfB Stuttgart vs Borussia Dortmund | 2 | Victoria Borussia Dortmund | excluido | 2.86 | 62.0% | 1.61 | +77.29% | +77.29% | +62.99% | 0.10u | Media-Alta |
| 63 | D.C. United vs Charlotte FC | over_3_5 | Over 3.5 Goles | excluido | 2.40 | 61.7% | 1.62 | +48.01% | +48.01% | +36.01% | 0.09u | Media-Alta |
| 64 | Hamburger SV vs 1. FC Köln | 2 | Victoria 1. FC Köln | excluido | 2.60 | 60.4% | 1.66 | +57.07% | +57.07% | +44.07% | 0.09u | Media-Alta |
| 65 | Real Salt Lake vs Vancouver Whitecaps FC | 2 | Victoria Vancouver Whitecaps FC | prioritario | 1.91 | 60.2% | 1.66 | +14.98% | +14.98% | +5.43% | 0.04u | Media-Alta |
| 66 | Nashville SC vs Chicago Fire | over_3_5 | Over 3.5 Goles | excluido | 2.42 | 59.5% | 1.68 | +43.87% | +43.87% | +31.77% | 0.08u | Media-Alta |
| 67 | FC Dallas vs Austin FC | over_3_5 | Over 3.5 Goles | excluido | 2.48 | 59.4% | 1.68 | +47.36% | +47.36% | +34.96% | 0.08u | Media-Alta |
| 68 | ADO Den Haag vs SC Cambuur | over_3_5 | Over 3.5 Goles | excluido | 2.28 | 58.6% | 1.71 | +33.54% | +33.54% | +22.14% | 0.07u | Media-Alta |
| 69 | Sporting Lisbon vs Arouca | under_3_5 | Under 3.5 Goles | excluido | 1.89 | 58.4% | 1.71 | +10.41% | +10.41% | +0.96% | 0.03u | Media-Alta |
| 70 | Venezia vs Lazio | 2 | Victoria Lazio | prioritario | 2.02 | 57.8% | 1.73 | +16.84% | +16.84% | +6.74% | 0.04u | Media |
| 71 | Werder Bremen vs Augsburg | 2 | Victoria Augsburg | excluido | 2.88 | 57.5% | 1.74 | +65.51% | +65.51% | +51.11% | 0.09u | Media |
| 72 | Gimnasia La Plata vs Banfield | over_2_5 | Over 2.5 Goles | prioritario | 2.15 | 57.5% | 1.74 | +23.54% | +23.54% | +12.79% | 0.05u | Media |
| 73 | Houston Dynamo vs FC Cincinnati | over_3_5 | Over 3.5 Goles | excluido | 2.46 | 57.0% | 1.76 | +40.10% | +40.10% | +27.80% | 0.07u | Media |
| 74 | Bologna vs Torino | 1 | Victoria Bologna | excluido | 2.04 | 55.9% | 1.79 | +14.02% | +14.02% | +3.82% | 0.03u | Media |
| 75 | Eintracht Frankfurt vs SC Freiburg | 2 | Victoria SC Freiburg | excluido | 2.76 | 52.9% | 1.89 | +45.98% | +45.98% | +32.18% | 0.07u | Media |
| 76 | Union Santa Fe vs Independiente | over_2_5 | Over 2.5 Goles | excluido | 2.46 | 52.4% | 1.91 | +28.90% | +28.90% | +16.60% | 0.05u | Media |
| 77 | Alianza FC vs Independiente Santa Fe | 2 | Victoria Independiente Santa Fe | excluido | 2.55 | 51.8% | 1.93 | +31.99% | +31.99% | +19.24% | 0.05u | Media |
| 78 | CF Montreal vs Columbus Crew SC | over_3_5 | Over 3.5 Goles | excluido | 2.38 | 51.7% | 1.93 | +23.12% | +23.12% | +11.22% | 0.04u | Media |
| 79 | St. Louis City SC vs Toronto FC | over_3_5 | Over 3.5 Goles | excluido | 2.28 | 51.7% | 1.93 | +17.94% | +17.94% | +6.54% | 0.04u | Media |
| 80 | Gil Vicente vs CS Maritimo | over_2_5 | Over 2.5 Goles | excluido | 2.32 | 51.7% | 1.94 | +19.85% | +19.85% | +8.25% | 0.04u | Media |
| 81 | River Plate vs Atlético Huracán | over_2_5 | Over 2.5 Goles | excluido | 2.42 | 50.4% | 1.98 | +21.94% | +21.94% | +9.84% | 0.04u | Media |
| 82 | Le Mans FC vs Lorient | 2 | Victoria Lorient | excluido | 2.70 | 48.6% | 2.06 | +31.17% | +31.17% | +17.67% | 0.05u | Baja |
| 83 | Instituto de Córdoba vs Talleres | over_2_5 | Over 2.5 Goles | excluido | 2.52 | 48.3% | 2.07 | +21.82% | +21.82% | +9.22% | 0.04u | Baja |
| 84 | Nacional vs Famalicão | 2 | Victoria Famalicão | excluido | 2.18 | 48.3% | 2.07 | +5.34% | +5.34% | -5.56% | 0.01u | Baja |
| 85 | ADO Den Haag vs SC Cambuur | 2 | Victoria SC Cambuur | excepcional | 4.30 | 47.8% | 2.09 | +105.37% | +105.37% | +83.87% | 0.08u | Baja |
| 86 | Angers vs Troyes | 1 | Victoria Angers | excluido | 2.23 | 47.3% | 2.12 | +5.41% | +5.41% | -5.74% | 0.01u | Baja |
| 87 | D.C. United vs Charlotte FC | 2 | Victoria Charlotte FC | excluido | 2.40 | 46.5% | 2.15 | +11.65% | +11.65% | -0.35% | 0.02u | Baja |
| 88 | Udinese vs Cagliari | 2 | Victoria Cagliari | excepcional | 3.55 | 46.4% | 2.16 | +64.65% | +64.65% | +46.90% | 0.06u | Baja |
| 89 | Willem II vs Fortuna Sittard | 1 | Victoria Willem II | excluido | 2.72 | 45.4% | 2.20 | +23.57% | +23.57% | +9.97% | 0.03u | Baja |
| 90 | AS Roma vs Inter Milan | 1 | Victoria AS Roma | excluido | 2.80 | 43.6% | 2.29 | +22.22% | +22.22% | +8.22% | 0.03u | Baja |
| 91 | Sparta Rotterdam vs Heerenveen | 2 | Victoria Heerenveen | excluido | 2.70 | 43.4% | 2.31 | +17.13% | +17.13% | +3.63% | 0.03u | Baja |
| 92 | CF Montreal vs Columbus Crew SC | 2 | Victoria Columbus Crew SC | excluido | 2.74 | 42.9% | 2.33 | +17.44% | +17.44% | +3.74% | 0.03u | Baja |
| 93 | Nashville SC vs Chicago Fire | 2 | Victoria Chicago Fire | excepcional | 4.22 | 41.9% | 2.39 | +76.86% | +76.86% | +55.76% | 0.06u | Baja |
| 94 | Lyon vs Rennes | 2 | Victoria Rennes | excepcional | 3.40 | 41.7% | 2.40 | +41.64% | +41.64% | +24.64% | 0.04u | Baja |
| 95 | Gimnasia Mendoza vs Deportivo Riestra | over_2_5 | Over 2.5 Goles | excluido | 2.95 | 41.3% | 2.42 | +21.75% | +21.75% | +7.00% | 0.03u | Baja |
| 96 | Athletic Bilbao vs Alavés | 2 | Victoria Alavés | excepcional | 5.90 | 41.1% | 2.43 | +142.43% | +142.43% | +112.93% | 0.07u | Baja |
| 97 | Newcastle United vs Hull City | 2 | Victoria Hull City | excepcional | 5.60 | 41.0% | 2.44 | +129.38% | +129.38% | +101.38% | 0.07u | Baja |
| 98 | CA Osasuna vs Rayo Vallecano | 1 | Victoria CA Osasuna | excluido | 2.70 | 40.6% | 2.47 | +9.51% | +9.51% | -3.99% | 0.01u | Baja |
| 99 | Portland Timbers vs Atlanta United FC | 2 | Victoria Atlanta United FC | excepcional | 3.25 | 39.1% | 2.56 | +26.98% | +26.98% | +10.73% | 0.03u | Baja |
| 100 | Gimnasia Mendoza vs Deportivo Riestra | 2 | Victoria Deportivo Riestra | excepcional | 4.30 | 38.0% | 2.63 | +63.44% | +63.44% | +41.94% | 0.05u | Baja |
| 101 | Houston Dynamo vs FC Cincinnati | 2 | Victoria FC Cincinnati | excepcional | 3.85 | 36.7% | 2.73 | +41.26% | +41.26% | +22.01% | 0.04u | Baja |
| 102 | Sporting Lisbon vs Arouca | under_2_5 | Under 2.5 Goles | excluido | 2.88 | 36.6% | 2.73 | +5.41% | +5.41% | -8.99% | 0.01u | Baja |
| 103 | CA Osasuna vs Rayo Vallecano | 2 | Victoria Rayo Vallecano | excluido | 3.02 | 35.1% | 2.85 | +6.09% | +6.09% | -9.01% | 0.01u | Baja |
| 104 | New England Revolution vs Orlando City SC | 2 | Victoria Orlando City SC | excepcional | 3.85 | 34.9% | 2.87 | +34.37% | +34.37% | +15.11% | 0.03u | Baja |
| 105 | San Jose Earthquakes vs Los Angeles FC | 1 | Victoria San Jose Earthquakes | excluido | 3.10 | 34.8% | 2.87 | +7.94% | +7.94% | -7.56% | 0.01u | Baja |
| 106 | Colorado Rapids vs Seattle Sounders FC | 2 | Victoria Seattle Sounders FC | excepcional | 3.95 | 34.0% | 2.94 | +34.14% | +34.14% | +14.39% | 0.03u | Baja |
| 107 | Minnesota United FC vs LA Galaxy | 2 | Victoria LA Galaxy | excepcional | 4.75 | 33.2% | 3.01 | +57.60% | +57.60% | +33.85% | 0.04u | Baja |
| 108 | Celta Vigo vs Real Racing Club de Santander | 2 | Victoria Real Racing Club de Santander | excepcional | 4.40 | 32.5% | 3.08 | +42.96% | +42.96% | +20.96% | 0.03u | Baja |
| 109 | Union Santa Fe vs Independiente | 2 | Victoria Independiente | excluido | 3.19 | 32.3% | 3.10 | +3.04% | +3.04% | -12.91% | 0.00u | Baja |
| 110 | Alverca vs Rio Ave FC | 2 | Victoria Rio Ave FC | excepcional | 4.20 | 32.3% | 3.10 | +35.49% | +35.49% | +14.49% | 0.03u | Baja |
| 111 | Tottenham Hotspur vs Aston Villa | 2 | Victoria Aston Villa | excluido | 3.85 | 31.7% | 3.15 | +22.16% | +22.16% | +2.91% | 0.02u | Baja |
| 112 | Everton vs Ipswich Town | 2 | Victoria Ipswich Town | excluido | 4.80 | 29.9% | 3.35 | +43.42% | +43.42% | +19.42% | 0.03u | Baja |
| 113 | Angers vs Troyes | 2 | Victoria Troyes | excluido | 3.65 | 28.9% | 3.46 | +5.41% | +5.41% | -12.84% | 0.01u | Baja |
| 114 | St. Louis City SC vs Toronto FC | 2 | Victoria Toronto FC | excluido | 5.20 | 28.3% | 3.53 | +47.11% | +47.11% | +21.11% | 0.03u | Baja |
| 115 | Brighton and Hove Albion vs Arsenal | 1 | Victoria Brighton and Hove Albion | excluido | 5.30 | 27.9% | 3.58 | +47.98% | +47.98% | +21.48% | 0.03u | Baja |
| 116 | Gimnasia La Plata vs Banfield | 2 | Victoria Banfield | excluido | 4.90 | 27.5% | 3.64 | +34.75% | +34.75% | +10.25% | 0.02u | Baja |
| 117 | River Plate vs Atlético Huracán | X | Empate | excluido | 4.00 | 27.4% | 3.65 | +9.64% | +9.64% | -10.36% | 0.01u | Baja |
| 118 | Millonarios vs Boyacá Chicó F.C. | X | Empate | excluido | 5.45 | 25.8% | 3.88 | +40.61% | +40.61% | +13.36% | 0.02u | Baja |
| 119 | Deportivo Cali vs Cúcuta Deportivo | X | Empate | excluido | 4.33 | 24.9% | 4.02 | +7.73% | +7.73% | -13.92% | 0.01u | Baja |
| 120 | Houston Dynamo vs FC Cincinnati | X | Empate | excluido | 4.20 | 24.6% | 4.07 | +3.24% | +3.24% | -17.76% | 0.00u | Baja |
| 121 | St. Louis City SC vs Toronto FC | X | Empate | excluido | 4.60 | 24.4% | 4.09 | +12.47% | +12.47% | -10.53% | 0.01u | Baja |
| 122 | Newcastle United vs Hull City | X | Empate | excluido | 4.52 | 24.3% | 4.12 | +9.66% | +9.66% | -12.94% | 0.01u | Baja |
| 123 | Gil Vicente vs CS Maritimo | 2 | Victoria CS Maritimo | excluido | 4.50 | 23.5% | 4.26 | +5.71% | +5.71% | -16.79% | 0.00u | Baja |
| 124 | New England Revolution vs Orlando City SC | X | Empate | excluido | 4.50 | 23.4% | 4.28 | +5.21% | +5.21% | -17.29% | 0.00u | Baja |
| 125 | Minnesota United FC vs LA Galaxy | X | Empate | excluido | 4.65 | 22.8% | 4.39 | +5.93% | +5.93% | -17.32% | 0.00u | Baja |
| 126 | Instituto de Córdoba vs Talleres | 2 | Victoria Talleres | excluido | 4.90 | 22.7% | 4.40 | +11.43% | +11.43% | -13.07% | 0.01u | Baja |
| 127 | FC Dallas vs Austin FC | 2 | Victoria Austin FC | excluido | 4.80 | 21.6% | 4.62 | +3.82% | +3.82% | -20.18% | 0.00u | Baja |
| 128 | Ajax vs Excelsior | X | Empate | excluido | 8.00 | 21.4% | 4.68 | +71.04% | +71.04% | +31.04% | 0.03u | Baja |
| 129 | Toulouse vs Le Havre | 2 | Victoria Le Havre | excluido | 5.10 | 21.0% | 4.76 | +7.05% | +7.05% | -18.45% | 0.00u | Baja |
| 130 | Millonarios vs Boyacá Chicó F.C. | 2 | Victoria Boyacá Chicó F.C. | excluido | 11.54 | 20.6% | 4.84 | +138.19% | +138.19% | +80.49% | 0.03u | Baja |
| 131 | River Plate vs Atlético Huracán | 2 | Victoria Atlético Huracán | excluido | 8.00 | 20.6% | 4.85 | +65.04% | +65.04% | +25.04% | 0.02u | Baja |
| 132 | Sporting Lisbon vs Arouca | X | Empate | excluido | 8.40 | 19.9% | 5.02 | +67.50% | +67.50% | +25.50% | 0.02u | Baja |
| 133 | Ajax vs Excelsior | 2 | Victoria Excelsior | excluido | 13.00 | 19.7% | 5.08 | +155.84% | +155.84% | +90.84% | 0.03u | Baja |
| 134 | Deportivo Cali vs Cúcuta Deportivo | 2 | Victoria Cúcuta Deportivo | excluido | 6.59 | 18.5% | 5.39 | +22.18% | +22.18% | -10.77% | 0.01u | Baja |
| 135 | Sevilla vs Barcelona | X | Empate | excluido | 8.20 | 16.5% | 6.07 | +35.05% | +35.05% | -5.95% | 0.01u | Baja |
| 136 | Sporting Lisbon vs Arouca | 2 | Victoria Arouca | excluido | 16.00 | 7.0% | 14.22 | +12.48% | +12.48% | -67.52% | 0.00u | Baja |

## Evaluación Over/Under por Partido
Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada (n/d = cuota no disponible en la corrida).
| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |
|---|---|---|---:|---:|---:|---:|---:|---|
| Tottenham Hotspur vs Aston Villa | 1.5 | 80.7% | n/d | n/d | 19.4% | n/d | n/d | Cuotas no capturadas |
| Tottenham Hotspur vs Aston Villa | 2.5 | 71.1% | 1.84 | +30.86% | 28.9% | 2.11 | -39.06% | Value Over |
| Tottenham Hotspur vs Aston Villa | 3.5 | 52.5% | n/d | n/d | 47.5% | n/d | n/d | Cuotas no capturadas |
| Brighton and Hove Albion vs Arsenal | 1.5 | 88.9% | n/d | n/d | 11.1% | n/d | n/d | Cuotas no capturadas |
| Brighton and Hove Albion vs Arsenal | 2.5 | 85.0% | 1.84 | +56.38% | 15.0% | 2.19 | -67.13% | Value Over |
| Brighton and Hove Albion vs Arsenal | 3.5 | 74.9% | n/d | n/d | 25.1% | n/d | n/d | Cuotas no capturadas |
| Everton vs Ipswich Town | 1.5 | 83.5% | n/d | n/d | 16.5% | n/d | n/d | Cuotas no capturadas |
| Everton vs Ipswich Town | 2.5 | 76.0% | 1.79 | +35.99% | 24.0% | 2.23 | -46.41% | Value Over |
| Everton vs Ipswich Town | 3.5 | 60.0% | n/d | n/d | 40.0% | n/d | n/d | Cuotas no capturadas |
| Newcastle United vs Hull City | 1.5 | 78.2% | n/d | n/d | 21.8% | n/d | n/d | Cuotas no capturadas |
| Newcastle United vs Hull City | 2.5 | 66.8% | 1.70 | +13.58% | 33.2% | 2.40 | -20.34% | Value Over |
| Newcastle United vs Hull City | 3.5 | 46.2% | n/d | n/d | 53.8% | n/d | n/d | Cuotas no capturadas |
| Nottingham Forest vs Coventry City | 1.5 | 78.8% | n/d | n/d | 21.2% | n/d | n/d | Cuotas no capturadas |
| Nottingham Forest vs Coventry City | 2.5 | 68.1% | 1.87 | +27.27% | 31.9% | 2.14 | -31.65% | Value Over |
| Nottingham Forest vs Coventry City | 3.5 | 48.0% | n/d | n/d | 52.0% | n/d | n/d | Cuotas no capturadas |
| Hamburger SV vs 1. FC Köln | 1.5 | 89.0% | n/d | n/d | 11.0% | n/d | n/d | Cuotas no capturadas |
| Hamburger SV vs 1. FC Köln | 2.5 | 85.2% | 1.65 | +40.56% | 14.8% | 2.45 | -63.72% | Value Over |
| Hamburger SV vs 1. FC Köln | 3.5 | 75.2% | 2.30 | +73.05% | 24.8% | 1.55 | -61.62% | Value Over |
| Werder Bremen vs Augsburg | 1.5 | 89.5% | n/d | n/d | 10.5% | n/d | n/d | Cuotas no capturadas |
| Werder Bremen vs Augsburg | 2.5 | 85.9% | 1.44 | +23.68% | 14.1% | 2.91 | -58.94% | Value Over |
| Werder Bremen vs Augsburg | 3.5 | 76.4% | 2.07 | +58.17% | 23.6% | 1.88 | -55.65% | Value Over |
| Borussia Monchengladbach vs FSV Mainz 05 | 1.5 | 90.6% | n/d | n/d | 9.4% | n/d | n/d | Cuotas no capturadas |
| Borussia Monchengladbach vs FSV Mainz 05 | 2.5 | 87.7% | 1.55 | +35.98% | 12.3% | 2.67 | -67.24% | Value Over |
| Borussia Monchengladbach vs FSV Mainz 05 | 3.5 | 79.6% | 2.34 | +86.26% | 20.4% | 1.70 | -65.32% | Value Over |
| Eintracht Frankfurt vs SC Freiburg | 1.5 | 85.9% | n/d | n/d | 14.1% | n/d | n/d | Cuotas no capturadas |
| Eintracht Frankfurt vs SC Freiburg | 2.5 | 80.0% | 1.44 | +15.20% | 20.0% | 2.88 | -42.40% | Value Over |
| Eintracht Frankfurt vs SC Freiburg | 3.5 | 66.5% | 2.15 | +42.98% | 33.5% | 1.83 | -38.69% | Value Over |
| VfB Stuttgart vs Borussia Dortmund | 1.5 | 94.5% | n/d | n/d | 5.5% | n/d | n/d | Cuotas no capturadas |
| VfB Stuttgart vs Borussia Dortmund | 2.5 | 93.5% | 1.38 | +28.99% | 6.5% | 3.10 | -79.76% | Value Over |
| VfB Stuttgart vs Borussia Dortmund | 3.5 | 89.5% | 1.99 | +78.05% | 10.5% | 2.00 | -78.94% | Value Over |
| CA Osasuna vs Rayo Vallecano | 1.5 | 83.5% | n/d | n/d | 16.4% | n/d | n/d | Cuotas no capturadas |
| CA Osasuna vs Rayo Vallecano | 2.5 | 76.1% | 2.15 | +63.55% | 23.9% | 1.86 | -55.49% | Value Over |
| CA Osasuna vs Rayo Vallecano | 3.5 | 60.1% | n/d | n/d | 39.9% | n/d | n/d | Cuotas no capturadas |
| Athletic Bilbao vs Alavés | 1.5 | 82.7% | n/d | n/d | 17.3% | n/d | n/d | Cuotas no capturadas |
| Athletic Bilbao vs Alavés | 2.5 | 74.6% | 1.97 | +47.02% | 25.4% | 2.00 | -49.26% | Value Over |
| Athletic Bilbao vs Alavés | 3.5 | 57.9% | n/d | n/d | 42.1% | n/d | n/d | Cuotas no capturadas |
| Celta Vigo vs Real Racing Club de Santander | 1.5 | 81.6% | n/d | n/d | 18.4% | n/d | n/d | Cuotas no capturadas |
| Celta Vigo vs Real Racing Club de Santander | 2.5 | 72.8% | 1.68 | +22.22% | 27.3% | 2.40 | -34.60% | Value Over |
| Celta Vigo vs Real Racing Club de Santander | 3.5 | 54.9% | n/d | n/d | 45.1% | n/d | n/d | Cuotas no capturadas |
| Sevilla vs Barcelona | 1.5 | 90.2% | n/d | n/d | 9.8% | n/d | n/d | Cuotas no capturadas |
| Sevilla vs Barcelona | 2.5 | 87.2% | 1.28 | +11.59% | 12.8% | 3.80 | -51.28% | Value Over |
| Sevilla vs Barcelona | 3.5 | 78.6% | 1.74 | +36.85% | 21.3% | 2.34 | -50.04% | Value Over |
| Bologna vs Torino | 1.5 | 78.1% | n/d | n/d | 21.9% | n/d | n/d | Cuotas no capturadas |
| Bologna vs Torino | 2.5 | 66.8% | 2.12 | +41.64% | 33.2% | 1.89 | -37.27% | Value Over |
| Bologna vs Torino | 3.5 | 46.2% | n/d | n/d | 53.8% | n/d | n/d | Cuotas no capturadas |
| Udinese vs Cagliari | 1.5 | 85.5% | n/d | n/d | 14.5% | n/d | n/d | Cuotas no capturadas |
| Udinese vs Cagliari | 2.5 | 79.3% | 2.16 | +71.40% | 20.6% | 1.84 | -62.00% | Value Over |
| Udinese vs Cagliari | 3.5 | 65.4% | n/d | n/d | 34.6% | n/d | n/d | Cuotas no capturadas |
| AS Roma vs Inter Milan | 1.5 | 93.5% | n/d | n/d | 6.5% | n/d | n/d | Cuotas no capturadas |
| AS Roma vs Inter Milan | 2.5 | 92.0% | 1.66 | +52.79% | 8.0% | 2.43 | -80.66% | Value Over |
| AS Roma vs Inter Milan | 3.5 | 87.0% | 2.35 | +104.47% | 13.0% | 1.55 | -79.87% | Value Over |
| Venezia vs Lazio | 1.5 | 90.1% | n/d | n/d | 9.9% | n/d | n/d | Cuotas no capturadas |
| Venezia vs Lazio | 2.5 | 86.9% | 1.80 | +56.46% | 13.1% | 2.20 | -71.22% | Value Over |
| Venezia vs Lazio | 3.5 | 78.2% | n/d | n/d | 21.8% | n/d | n/d | Cuotas no capturadas |
| Paris FC vs Strasbourg | 1.5 | 84.8% | n/d | n/d | 15.2% | n/d | n/d | Cuotas no capturadas |
| Paris FC vs Strasbourg | 2.5 | 78.3% | 1.70 | +33.18% | 21.7% | 2.34 | -49.32% | Value Over |
| Paris FC vs Strasbourg | 3.5 | 63.8% | n/d | n/d | 36.2% | n/d | n/d | Cuotas no capturadas |
| Angers vs Troyes | 1.5 | 83.3% | n/d | n/d | 16.7% | n/d | n/d | Cuotas no capturadas |
| Angers vs Troyes | 2.5 | 75.6% | 2.04 | +54.29% | 24.4% | 1.95 | -52.48% | Value Over |
| Angers vs Troyes | 3.5 | 59.4% | n/d | n/d | 40.6% | n/d | n/d | Cuotas no capturadas |
| Toulouse vs Le Havre | 1.5 | 83.6% | n/d | n/d | 16.4% | n/d | n/d | Cuotas no capturadas |
| Toulouse vs Le Havre | 2.5 | 76.3% | 1.76 | +34.25% | 23.7% | 2.23 | -47.10% | Value Over |
| Toulouse vs Le Havre | 3.5 | 60.5% | n/d | n/d | 39.5% | n/d | n/d | Cuotas no capturadas |
| Le Mans FC vs Lorient | 1.5 | 84.4% | n/d | n/d | 15.6% | n/d | n/d | Cuotas no capturadas |
| Le Mans FC vs Lorient | 2.5 | 77.5% | 1.84 | +42.51% | 22.6% | 2.12 | -52.19% | Value Over |
| Le Mans FC vs Lorient | 3.5 | 62.3% | n/d | n/d | 37.7% | n/d | n/d | Cuotas no capturadas |
| Lyon vs Rennes | 1.5 | 85.4% | n/d | n/d | 14.6% | n/d | n/d | Cuotas no capturadas |
| Lyon vs Rennes | 2.5 | 79.2% | 1.54 | +22.05% | 20.8% | 2.52 | -47.71% | Value Over |
| Lyon vs Rennes | 3.5 | 65.3% | 2.42 | +57.95% | 34.7% | 1.66 | -42.35% | Value Over |
| ADO Den Haag vs SC Cambuur | 1.5 | 83.0% | n/d | n/d | 17.0% | n/d | n/d | Cuotas no capturadas |
| ADO Den Haag vs SC Cambuur | 2.5 | 75.1% | 1.48 | +11.12% | 24.9% | 2.56 | -36.20% | Value Over |
| ADO Den Haag vs SC Cambuur | 3.5 | 58.6% | 2.28 | +33.54% | 41.4% | 1.70 | -29.57% | Value Over |
| Sparta Rotterdam vs Heerenveen | 1.5 | 88.0% | n/d | n/d | 12.0% | n/d | n/d | Cuotas no capturadas |
| Sparta Rotterdam vs Heerenveen | 2.5 | 83.6% | 1.45 | +21.19% | 16.4% | 2.66 | -56.32% | Value Over |
| Sparta Rotterdam vs Heerenveen | 3.5 | 72.5% | 2.26 | +63.80% | 27.5% | 1.73 | -52.39% | Value Over |
| Ajax vs Excelsior | 1.5 | 85.2% | n/d | n/d | 14.8% | n/d | n/d | Cuotas no capturadas |
| Ajax vs Excelsior | 2.5 | 78.8% | 1.24 | -2.23% | 21.1% | 3.92 | -17.09% | Sin value |
| Ajax vs Excelsior | 3.5 | 64.6% | 1.69 | +9.17% | 35.4% | 2.38 | -15.75% | Value Over |
| Willem II vs Fortuna Sittard | 1.5 | 88.5% | n/d | n/d | 11.5% | n/d | n/d | Cuotas no capturadas |
| Willem II vs Fortuna Sittard | 2.5 | 84.4% | 1.54 | +29.98% | 15.6% | 2.47 | -61.47% | Value Over |
| Willem II vs Fortuna Sittard | 3.5 | 73.9% | 2.38 | +75.83% | 26.1% | 1.67 | -56.38% | Value Over |
| Gil Vicente vs CS Maritimo | 1.5 | 69.2% | n/d | n/d | 30.8% | n/d | n/d | Cuotas no capturadas |
| Gil Vicente vs CS Maritimo | 2.5 | 51.7% | 2.32 | +19.85% | 48.3% | 1.65 | -20.24% | Value Over |
| Gil Vicente vs CS Maritimo | 3.5 | 27.7% | n/d | n/d | 72.4% | n/d | n/d | Cuotas no capturadas |
| Nacional vs Famalicão | 1.5 | 75.8% | n/d | n/d | 24.2% | n/d | n/d | Cuotas no capturadas |
| Nacional vs Famalicão | 2.5 | 62.6% | 2.28 | +42.82% | 37.4% | 1.75 | -34.62% | Value Over |
| Nacional vs Famalicão | 3.5 | 40.6% | n/d | n/d | 59.4% | n/d | n/d | Cuotas no capturadas |
| Alverca vs Rio Ave FC | 1.5 | 77.2% | n/d | n/d | 22.8% | n/d | n/d | Cuotas no capturadas |
| Alverca vs Rio Ave FC | 2.5 | 65.1% | 2.07 | +34.69% | 34.9% | 1.90 | -33.63% | Value Over |
| Alverca vs Rio Ave FC | 3.5 | 43.9% | n/d | n/d | 56.1% | n/d | n/d | Cuotas no capturadas |
| Sporting Lisbon vs Arouca | 1.5 | 76.1% | n/d | n/d | 23.9% | n/d | n/d | Cuotas no capturadas |
| Sporting Lisbon vs Arouca | 2.5 | 63.4% | 1.41 | -10.61% | 36.6% | 2.88 | +5.41% | Value Under |
| Sporting Lisbon vs Arouca | 3.5 | 41.6% | 2.08 | -13.51% | 58.4% | 1.89 | +10.41% | Value Under |
| Gimnasia La Plata vs Banfield | 1.5 | 72.7% | n/d | n/d | 27.3% | n/d | n/d | Cuotas no capturadas |
| Gimnasia La Plata vs Banfield | 2.5 | 57.5% | 2.15 | +23.54% | 42.5% | 1.76 | -25.13% | Value Over |
| Gimnasia La Plata vs Banfield | 3.5 | 34.1% | n/d | n/d | 65.9% | n/d | n/d | Cuotas no capturadas |
| Gimnasia Mendoza vs Deportivo Riestra | 1.5 | 62.7% | n/d | n/d | 37.3% | n/d | n/d | Cuotas no capturadas |
| Gimnasia Mendoza vs Deportivo Riestra | 2.5 | 41.3% | 2.95 | +21.75% | 58.7% | 1.39 | -18.37% | Value Over |
| Gimnasia Mendoza vs Deportivo Riestra | 3.5 | 17.9% | n/d | n/d | 82.1% | n/d | n/d | Cuotas no capturadas |
| Union Santa Fe vs Independiente | 1.5 | 69.7% | n/d | n/d | 30.3% | n/d | n/d | Cuotas no capturadas |
| Union Santa Fe vs Independiente | 2.5 | 52.4% | 2.46 | +28.90% | 47.6% | 1.56 | -25.74% | Value Over |
| Union Santa Fe vs Independiente | 3.5 | 28.4% | n/d | n/d | 71.6% | n/d | n/d | Cuotas no capturadas |
| River Plate vs Atlético Huracán | 1.5 | 68.4% | n/d | n/d | 31.6% | n/d | n/d | Cuotas no capturadas |
| River Plate vs Atlético Huracán | 2.5 | 50.4% | 2.42 | +21.94% | 49.6% | 1.64 | -18.64% | Value Over |
| River Plate vs Atlético Huracán | 3.5 | 26.3% | n/d | n/d | 73.7% | n/d | n/d | Cuotas no capturadas |
| Instituto de Córdoba vs Talleres | 1.5 | 67.2% | n/d | n/d | 32.8% | n/d | n/d | Cuotas no capturadas |
| Instituto de Córdoba vs Talleres | 2.5 | 48.3% | 2.52 | +21.82% | 51.7% | 1.52 | -21.48% | Value Over |
| Instituto de Córdoba vs Talleres | 3.5 | 24.3% | n/d | n/d | 75.7% | n/d | n/d | Cuotas no capturadas |
| CF Montreal vs Columbus Crew SC | 1.5 | 80.4% | n/d | n/d | 19.6% | n/d | n/d | Cuotas no capturadas |
| CF Montreal vs Columbus Crew SC | 2.5 | 70.6% | 1.64 | +15.80% | 29.4% | 2.44 | -28.29% | Value Over |
| CF Montreal vs Columbus Crew SC | 3.5 | 51.7% | 2.38 | +23.12% | 48.3% | 1.55 | -25.18% | Value Over |
| D.C. United vs Charlotte FC | 1.5 | 84.1% | n/d | n/d | 15.9% | n/d | n/d | Cuotas no capturadas |
| D.C. United vs Charlotte FC | 2.5 | 77.0% | 1.62 | +24.82% | 22.9% | 2.50 | -42.62% | Value Over |
| D.C. United vs Charlotte FC | 3.5 | 61.7% | 2.40 | +48.01% | 38.3% | 1.63 | -37.52% | Value Over |
| San Jose Earthquakes vs Los Angeles FC | 1.5 | 86.0% | n/d | n/d | 14.0% | n/d | n/d | Cuotas no capturadas |
| San Jose Earthquakes vs Los Angeles FC | 2.5 | 80.2% | 1.50 | +20.28% | 19.8% | 2.58 | -48.89% | Value Over |
| San Jose Earthquakes vs Los Angeles FC | 3.5 | 66.8% | 2.34 | +56.34% | 33.2% | 1.73 | -42.58% | Value Over |
| New England Revolution vs Orlando City SC | 1.5 | 86.3% | n/d | n/d | 13.7% | n/d | n/d | Cuotas no capturadas |
| New England Revolution vs Orlando City SC | 2.5 | 80.6% | 1.41 | +13.70% | 19.4% | 2.85 | -44.82% | Value Over |
| New England Revolution vs Orlando City SC | 3.5 | 67.6% | 2.16 | +45.93% | 32.4% | 1.85 | -39.99% | Value Over |
| FC Dallas vs Austin FC | 1.5 | 83.3% | n/d | n/d | 16.7% | n/d | n/d | Cuotas no capturadas |
| FC Dallas vs Austin FC | 2.5 | 75.6% | 1.55 | +17.23% | 24.4% | 2.38 | -42.00% | Value Over |
| FC Dallas vs Austin FC | 3.5 | 59.4% | 2.48 | +47.36% | 40.6% | 1.63 | -33.85% | Value Over |
| Houston Dynamo vs FC Cincinnati | 1.5 | 82.4% | n/d | n/d | 17.6% | n/d | n/d | Cuotas no capturadas |
| Houston Dynamo vs FC Cincinnati | 2.5 | 74.1% | 1.52 | +12.56% | 25.9% | 2.45 | -36.42% | Value Over |
| Houston Dynamo vs FC Cincinnati | 3.5 | 57.0% | 2.46 | +40.10% | 43.0% | 1.65 | -28.97% | Value Over |
| Minnesota United FC vs LA Galaxy | 1.5 | 86.7% | n/d | n/d | 13.3% | n/d | n/d | Cuotas no capturadas |
| Minnesota United FC vs LA Galaxy | 2.5 | 81.4% | 1.39 | +13.20% | 18.6% | 2.92 | -45.80% | Value Over |
| Minnesota United FC vs LA Galaxy | 3.5 | 68.9% | 2.05 | +41.22% | 31.1% | 1.92 | -40.27% | Value Over |
| Sporting Kansas City vs Philadelphia Union | 1.5 | 86.2% | n/d | n/d | 13.8% | n/d | n/d | Cuotas no capturadas |
| Sporting Kansas City vs Philadelphia Union | 2.5 | 80.5% | 1.43 | +15.19% | 19.4% | 2.80 | -45.54% | Value Over |
| Sporting Kansas City vs Philadelphia Union | 3.5 | 67.4% | 2.14 | +44.26% | 32.6% | 1.83 | -40.36% | Value Over |
| St. Louis City SC vs Toronto FC | 1.5 | 80.4% | n/d | n/d | 19.6% | n/d | n/d | Cuotas no capturadas |
| St. Louis City SC vs Toronto FC | 2.5 | 70.6% | 1.47 | +3.80% | 29.4% | 2.62 | -23.00% | Sin value |
| St. Louis City SC vs Toronto FC | 3.5 | 51.7% | 2.28 | +17.94% | 48.3% | 1.73 | -16.49% | Value Over |
| Nashville SC vs Chicago Fire | 1.5 | 83.3% | n/d | n/d | 16.7% | n/d | n/d | Cuotas no capturadas |
| Nashville SC vs Chicago Fire | 2.5 | 75.6% | 1.55 | +17.24% | 24.4% | 2.52 | -38.61% | Value Over |
| Nashville SC vs Chicago Fire | 3.5 | 59.5% | 2.42 | +43.87% | 40.6% | 1.67 | -32.28% | Value Over |
| Colorado Rapids vs Seattle Sounders FC | 1.5 | 81.5% | n/d | n/d | 18.5% | n/d | n/d | Cuotas no capturadas |
| Colorado Rapids vs Seattle Sounders FC | 2.5 | 72.5% | 1.77 | +28.31% | 27.5% | 2.23 | -38.65% | Value Over |
| Colorado Rapids vs Seattle Sounders FC | 3.5 | 54.6% | n/d | n/d | 45.4% | n/d | n/d | Cuotas no capturadas |
| Real Salt Lake vs Vancouver Whitecaps FC | 1.5 | 85.3% | n/d | n/d | 14.7% | n/d | n/d | Cuotas no capturadas |
| Real Salt Lake vs Vancouver Whitecaps FC | 2.5 | 79.1% | 1.52 | +20.17% | 20.9% | 2.48 | -48.07% | Value Over |
| Real Salt Lake vs Vancouver Whitecaps FC | 3.5 | 64.9% | 2.40 | +55.83% | 35.1% | 1.67 | -41.43% | Value Over |
| Portland Timbers vs Atlanta United FC | 1.5 | 85.4% | n/d | n/d | 14.6% | n/d | n/d | Cuotas no capturadas |
| Portland Timbers vs Atlanta United FC | 2.5 | 79.1% | 1.49 | +17.93% | 20.8% | 2.58 | -46.21% | Value Over |
| Portland Timbers vs Atlanta United FC | 3.5 | 65.1% | 2.28 | +48.45% | 34.9% | 1.71 | -40.34% | Value Over |
| Millonarios vs Boyacá Chicó F.C. | 1.5 | 73.3% | n/d | n/d | 26.7% | n/d | n/d | Cuotas no capturadas |
| Millonarios vs Boyacá Chicó F.C. | 2.5 | 58.5% | n/d | n/d | 41.5% | n/d | n/d | Cuotas no capturadas |
| Millonarios vs Boyacá Chicó F.C. | 3.5 | 35.4% | n/d | n/d | 64.6% | n/d | n/d | Cuotas no capturadas |
| Alianza FC vs Independiente Santa Fe | 1.5 | 76.2% | n/d | n/d | 23.8% | n/d | n/d | Cuotas no capturadas |
| Alianza FC vs Independiente Santa Fe | 2.5 | 63.4% | n/d | n/d | 36.6% | n/d | n/d | Cuotas no capturadas |
| Alianza FC vs Independiente Santa Fe | 3.5 | 41.6% | n/d | n/d | 58.4% | n/d | n/d | Cuotas no capturadas |
| Deportivo Cali vs Cúcuta Deportivo | 1.5 | 74.6% | n/d | n/d | 25.4% | n/d | n/d | Cuotas no capturadas |
| Deportivo Cali vs Cúcuta Deportivo | 2.5 | 60.8% | n/d | n/d | 39.2% | n/d | n/d | Cuotas no capturadas |
| Deportivo Cali vs Cúcuta Deportivo | 3.5 | 38.2% | n/d | n/d | 61.8% | n/d | n/d | Cuotas no capturadas |
| Deportivo Pasto vs Once Caldas | 1.5 | 77.9% | n/d | n/d | 22.1% | n/d | n/d | Cuotas no capturadas |
| Deportivo Pasto vs Once Caldas | 2.5 | 66.4% | n/d | n/d | 33.6% | n/d | n/d | Cuotas no capturadas |
| Deportivo Pasto vs Once Caldas | 3.5 | 45.6% | n/d | n/d | 54.4% | n/d | n/d | Cuotas no capturadas |

## Picks Recomendados (Top 6)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | AS Roma vs Inter Milan | over_2_5 | Over 2.5 Goles | prioritario | 1.66 | 92.0% | 1.09 | +52.79% | +52.79% | +44.49% | 0.20u | Media-Alta |
| 2 | VfB Stuttgart vs Borussia Dortmund | over_3_5 | Over 3.5 Goles | prioritario | 1.99 | 89.5% | 1.12 | +78.05% | +78.05% | +68.10% | 0.20u | Media-Alta |
| 3 | Borussia Monchengladbach vs FSV Mainz 05 | over_2_5 | Over 2.5 Goles | prioritario | 1.55 | 87.7% | 1.14 | +35.98% | +35.98% | +28.23% | 0.16u | Media-Alta |
| 4 | Venezia vs Lazio | over_2_5 | Over 2.5 Goles | prioritario | 1.80 | 86.9% | 1.15 | +56.46% | +56.46% | +47.46% | 0.18u | Media-Alta |
| 5 | Hamburger SV vs 1. FC Köln | over_2_5 | Over 2.5 Goles | prioritario | 1.65 | 85.2% | 1.17 | +40.56% | +40.56% | +32.31% | 0.16u | Media-Alta |
| 6 | Brighton and Hove Albion vs Arsenal | over_2_5 | Over 2.5 Goles | prioritario | 1.84 | 85.0% | 1.18 | +56.38% | +56.38% | +47.18% | 0.17u | Media-Alta |

## Detalle de Picks
### Pick 1: AS Roma vs Inter Milan
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.66
- **Probabilidad modelo:** 92.0%
- **Probabilidad conservadora:** 87.0%
- **Probabilidad implícita:** 60.2%
- **Cuota justa:** 1.09
- **Edge:** +52.79%
- **EV:** +52.79%
- **EV robusto:** +44.49%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.15
- **Stake:** 0.20u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/-5.0%. Sensibilidad: rEV +36.2% (prob-10%) a +44.5% (base).
- **Por qué:** Inter genera 3.25 xGF por partido y Roma 3.45 xGF (n=4, ambos con ritmo altísimo). El Elo favorece levemente a Inter (1947 vs 1856) y el mercado paga 1.66 por un over 2.5 con probabilidad modelo 92.0% (implícita 60.2%). La cuota justa de 1.09 deja un edge amplio.
- **Riesgos:** Derbi con contexto de odio que puede frenar el ritmo; si ambos plantean bloque alto se apuesta mucho al guion ofensivo. n=4 de xG aún corto para concluir.
- **Fuentes:** The Odds API totals (best 1.66, timestamp 2026-09-18T21:22Z); Understat Serie A xG; ClubElo.

### Pick 2: VfB Stuttgart vs Borussia Dortmund
- **Mercado:** over_3_5
- **Selección:** Over 3.5 Goles
- **Cuota:** 1.99
- **Probabilidad modelo:** 89.5%
- **Probabilidad conservadora:** 84.5%
- **Probabilidad implícita:** 50.2%
- **Cuota justa:** 1.12
- **Edge:** +78.05%
- **EV:** +78.05%
- **EV robusto:** +68.10%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.18
- **Stake:** 0.20u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/-5.0% del motor. Sensibilidad robusta (colchón pequeño por n=3 jornadas de Understat): rEV +58.2% a +68.1%. El `small_sample_penalty` del config no se aplica automáticamente en el motor; se verificó manualmente que el pick sobrevive hasta prob-15% (rEV +48.2%).
- **Por qué:** xG combinados de ambos equipos muy por encima de la media (Stuttgart 2.48 GF / 3.30 GA; Dortmund 3.30 xGA visitante en n=1 pero 2.16 GF). El Elo favorece a Dortmund pero el contexto de goles es extremo. Probabilidad modelo 89.5% (cuota justa 1.12) vs 50.2% implícita. Line 3.5 con under_3_5 bien pagado (2.00) cubre el riesgo.
- **Riesgos:** Muestras pequeñas de Understat (n=3); si Stuttgart corrige su fragilidad defensiva el total baja. Partido de alto riesgo en defensa; dos equipos ofensivos pueden igualmente cerrarse en 0-0 en derbi regional.
- **Fuentes:** The Odds API totals (best 1.99, timestamp 2026-09-18T21:22Z); Understat Bundesliga xG; ClubElo 2026-09.

### Pick 3: Borussia Monchengladbach vs FSV Mainz 05
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.55
- **Probabilidad modelo:** 87.7%
- **Probabilidad conservadora:** 82.7%
- **Probabilidad implícita:** 64.5%
- **Cuota justa:** 1.14
- **Edge:** +35.98%
- **EV:** +35.98%
- **EV robusto:** +28.23%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.21
- **Stake:** 0.16u
- **Confianza:** Media
- **Incertidumbre:** Base +/-5.0%. Sensibilidad: rEV +20.5% (prob-10%) a +28.2% (base).
- **Por qué:** Mainz viaja con 70.4% de victoria modelo (Elo 1700+) y Gladbach encaja (xGA 2.6+). El mercado paga 1.55 por over 2.5 con probabilidad 87.7% (implícita 64.5%). El contexto favorece goles con Mainz como atacante clave.
- **Riesgos:** Muestras n=3; si el partido lo controla Mainz a 0-1/0-2 el under gana. Edge menor entre las selecciones: sensibilidad lo deja en +12.7% con colchón -15%.
- **Fuentes:** The Odds API totals (best 1.55, timestamp 2026-09-18T21:22Z); Understat Bundesliga xG; ClubElo.

### Pick 4: Venezia vs Lazio
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.80
- **Probabilidad modelo:** 86.9%
- **Probabilidad conservadora:** 81.9%
- **Probabilidad implícita:** 55.6%
- **Cuota justa:** 1.15
- **Edge:** +56.46%
- **EV:** +56.46%
- **EV robusto:** +47.46%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.22
- **Stake:** 0.18u
- **Confianza:** Media
- **Incertidumbre:** Base +/-5.0%. Sensibilidad: rEV +38.5% (prob-10%) a +47.5% (base).
- **Por qué:** Venezia muestra un perfil de ida y vuelta (2.65 xGA local) y Lazio genera ofensiva consistente. Prob 86.9% vs 55.6% implícita; la cuota 1.80 (fair 1.15) deja EV amplio. Lazio favorito por Elo (1772 vs 1651).
- **Riesgos:** Venezia en casa puede bajar la línea defensiva ante Lazio; n=4 de xG. Si app Lazio domina sin goles del contrario el over 2.5 depende de un solo equipo.
- **Fuentes:** The Odds API totals (best 1.80, timestamp 2026-09-18T21:22Z); Understat Serie A xG; ClubElo.

### Pick 5: Hamburger SV vs 1. FC Köln
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.65
- **Probabilidad modelo:** 85.2%
- **Probabilidad conservadora:** 80.2%
- **Probabilidad implícita:** 60.6%
- **Cuota justa:** 1.17
- **Edge:** +40.56%
- **EV:** +40.56%
- **EV robusto:** +32.31%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.25
- **Stake:** 0.16u
- **Confianza:** Media
- **Incertidumbre:** Base +/-5.0%. Sensibilidad: rEV +24.1% (prob-10%) a +32.3% (base).
- **Por qué:** Hamburger SV muestra 2.35 xGA por partido y Köln genera volumen ofensivo (2.26 xGF). Prob 85.2% vs 60.6% implícita; cuota 1.65 (fair 1.17). Elo parejo (1664 vs 1660).
- **Riesgos:** Köln con 60% de victoria modelo puede dominar y cerrar el marcador; HSV en casa con fragilidad defensiva real (n=3). Partido de derbi del norte con ritmo alto.
- **Fuentes:** The Odds API totals (best 1.65, timestamp 2026-09-18T21:22Z); Understat Bundesliga xG; ClubElo.

### Pick 6: Brighton and Hove Albion vs Arsenal
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.84
- **Probabilidad modelo:** 85.0%
- **Probabilidad conservadora:** 80.0%
- **Probabilidad implícita:** 54.4%
- **Cuota justa:** 1.18
- **Edge:** +56.38%
- **EV:** +56.38%
- **EV robusto:** +47.18%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.25
- **Stake:** 0.17u
- **Confianza:** Alta
- **Incertidumbre:** Base +/-5.0%. Sensibilidad: rEV +38.0% (prob-10%) a +47.2% (base).
- **Por qué:** El Arsenal con 2.33 xGF en casa y Brighton con 3.11 xGF local y 1.85 xGA. Prob modelo 85.0% (fair 1.18) vs 54.4% implícita con cuota 1.84. Contexto de goles y ambos equipos en zona atacante.
- **Riesgos:** Arsenal muy sólido defensivamente (0.83 xGA) puede ganar 0-2 o 1-0 en Amex si Brighton no aparece; partido con ritmo alto pero posible control del visitante.
- **Fuentes:** The Odds API totals (best 1.84, timestamp 2026-09-18T21:22Z); Understat EPL xG; ClubElo.

## NO BET / Excluidos
- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**
  - Tottenham Hotspur vs Aston Villa — Under 2.5 Goles (under_2_5): Prob modelo 28.9%, EV -39.06%, EV robusto -49.61% → sin value.
  - Brighton and Hove Albion vs Arsenal — Under 2.5 Goles (under_2_5): Prob modelo 15.0%, EV -67.13%, EV robusto -78.08% → sin value.
  - Everton vs Ipswich Town — Under 2.5 Goles (under_2_5): Prob modelo 24.0%, EV -46.41%, EV robusto -57.56% → sin value.
  - Newcastle United vs Hull City — Under 2.5 Goles (under_2_5): Prob modelo 33.2%, EV -20.34%, EV robusto -32.34% → sin value.
  - Nottingham Forest vs Coventry City — Under 2.5 Goles (under_2_5): Prob modelo 31.9%, EV -31.65%, EV robusto -42.35% → sin value.
  - Hamburger SV vs 1. FC Köln — Under 2.5 Goles (under_2_5): Prob modelo 14.8%, EV -63.72%, EV robusto -75.97% → sin value.
  - Hamburger SV vs 1. FC Köln — Under 3.5 Goles (under_3_5): Prob modelo 24.8%, EV -61.62%, EV robusto -69.37% → sin value.
  - Werder Bremen vs Augsburg — Under 2.5 Goles (under_2_5): Prob modelo 14.1%, EV -58.94%, EV robusto -73.49% → sin value.
  - Werder Bremen vs Augsburg — Under 3.5 Goles (under_3_5): Prob modelo 23.6%, EV -55.65%, EV robusto -65.05% → sin value.
  - Borussia Monchengladbach vs FSV Mainz 05 — Under 2.5 Goles (under_2_5): Prob modelo 12.3%, EV -67.24%, EV robusto -80.59% → sin value.
  - Borussia Monchengladbach vs FSV Mainz 05 — Under 3.5 Goles (under_3_5): Prob modelo 20.4%, EV -65.32%, EV robusto -73.82% → sin value.
  - Eintracht Frankfurt vs SC Freiburg — Under 2.5 Goles (under_2_5): Prob modelo 20.0%, EV -42.40%, EV robusto -56.80% → sin value.
  - Eintracht Frankfurt vs SC Freiburg — Under 3.5 Goles (under_3_5): Prob modelo 33.5%, EV -38.69%, EV robusto -47.84% → sin value.
  - VfB Stuttgart vs Borussia Dortmund — Under 2.5 Goles (under_2_5): Prob modelo 6.5%, EV -79.76%, EV robusto -95.26% → sin value.
  - VfB Stuttgart vs Borussia Dortmund — Under 3.5 Goles (under_3_5): Prob modelo 10.5%, EV -78.94%, EV robusto -88.94% → sin value.
  - CA Osasuna vs Rayo Vallecano — Under 2.5 Goles (under_2_5): Prob modelo 23.9%, EV -55.49%, EV robusto -64.79% → sin value.
  - Athletic Bilbao vs Alavés — Under 2.5 Goles (under_2_5): Prob modelo 25.4%, EV -49.26%, EV robusto -59.26% → sin value.
  - Celta Vigo vs Real Racing Club de Santander — Under 2.5 Goles (under_2_5): Prob modelo 27.3%, EV -34.60%, EV robusto -46.60% → sin value.
  - Sevilla vs Barcelona — Under 2.5 Goles (under_2_5): Prob modelo 12.8%, EV -51.28%, EV robusto -70.28% → sin value.
  - Sevilla vs Barcelona — Under 3.5 Goles (under_3_5): Prob modelo 21.3%, EV -50.04%, EV robusto -61.74% → sin value.
  - Bologna vs Torino — Under 2.5 Goles (under_2_5): Prob modelo 33.2%, EV -37.27%, EV robusto -46.72% → sin value.
  - Udinese vs Cagliari — Under 2.5 Goles (under_2_5): Prob modelo 20.6%, EV -62.00%, EV robusto -71.20% → sin value.
  - AS Roma vs Inter Milan — Under 2.5 Goles (under_2_5): Prob modelo 8.0%, EV -80.66%, EV robusto -92.81% → sin value.
  - AS Roma vs Inter Milan — Under 3.5 Goles (under_3_5): Prob modelo 13.0%, EV -79.87%, EV robusto -87.62% → sin value.
  - Venezia vs Lazio — Under 2.5 Goles (under_2_5): Prob modelo 13.1%, EV -71.22%, EV robusto -82.22% → sin value.
  - Paris FC vs Strasbourg — Under 2.5 Goles (under_2_5): Prob modelo 21.7%, EV -49.32%, EV robusto -61.02% → sin value.
  - Angers vs Troyes — Under 2.5 Goles (under_2_5): Prob modelo 24.4%, EV -52.48%, EV robusto -62.23% → sin value.
  - Toulouse vs Le Havre — Under 2.5 Goles (under_2_5): Prob modelo 23.7%, EV -47.10%, EV robusto -58.25% → sin value.
  - Le Mans FC vs Lorient — Under 2.5 Goles (under_2_5): Prob modelo 22.6%, EV -52.19%, EV robusto -62.79% → sin value.
  - Lyon vs Rennes — Under 2.5 Goles (under_2_5): Prob modelo 20.8%, EV -47.71%, EV robusto -60.31% → sin value.
  - Lyon vs Rennes — Under 3.5 Goles (under_3_5): Prob modelo 34.7%, EV -42.35%, EV robusto -50.65% → sin value.
  - ADO Den Haag vs SC Cambuur — Under 2.5 Goles (under_2_5): Prob modelo 24.9%, EV -36.20%, EV robusto -49.00% → sin value.
  - ADO Den Haag vs SC Cambuur — Under 3.5 Goles (under_3_5): Prob modelo 41.4%, EV -29.57%, EV robusto -38.07% → sin value.
  - Sparta Rotterdam vs Heerenveen — Under 2.5 Goles (under_2_5): Prob modelo 16.4%, EV -56.32%, EV robusto -69.62% → sin value.
  - Sparta Rotterdam vs Heerenveen — Under 3.5 Goles (under_3_5): Prob modelo 27.5%, EV -52.39%, EV robusto -61.04% → sin value.
  - Ajax vs Excelsior — Over 2.5 Goles (over_2_5): Prob modelo 78.8%, EV -2.23%, EV robusto -8.43% → sin value.
  - Ajax vs Excelsior — Under 2.5 Goles (under_2_5): Prob modelo 21.1%, EV -17.09%, EV robusto -36.69% → sin value.
  - Ajax vs Excelsior — Under 3.5 Goles (under_3_5): Prob modelo 35.4%, EV -15.75%, EV robusto -27.65% → sin value.
  - Willem II vs Fortuna Sittard — Under 2.5 Goles (under_2_5): Prob modelo 15.6%, EV -61.47%, EV robusto -73.82% → sin value.
  - Willem II vs Fortuna Sittard — Under 3.5 Goles (under_3_5): Prob modelo 26.1%, EV -56.38%, EV robusto -64.73% → sin value.
  - Gil Vicente vs CS Maritimo — Under 2.5 Goles (under_2_5): Prob modelo 48.3%, EV -20.24%, EV robusto -28.49% → sin value.
  - Nacional vs Famalicão — Under 2.5 Goles (under_2_5): Prob modelo 37.4%, EV -34.62%, EV robusto -43.37% → sin value.
  - Alverca vs Rio Ave FC — Under 2.5 Goles (under_2_5): Prob modelo 34.9%, EV -33.63%, EV robusto -43.13% → sin value.
  - Sporting Lisbon vs Arouca — Over 2.5 Goles (over_2_5): Prob modelo 63.4%, EV -10.61%, EV robusto -17.66% → sin value.
  - Sporting Lisbon vs Arouca — Over 3.5 Goles (over_3_5): Prob modelo 41.6%, EV -13.51%, EV robusto -23.91% → sin value.
  - Gimnasia La Plata vs Banfield — Under 2.5 Goles (under_2_5): Prob modelo 42.5%, EV -25.13%, EV robusto -33.93% → sin value.
  - Gimnasia Mendoza vs Deportivo Riestra — Under 2.5 Goles (under_2_5): Prob modelo 58.7%, EV -18.37%, EV robusto -25.32% → sin value.
  - Union Santa Fe vs Independiente — Under 2.5 Goles (under_2_5): Prob modelo 47.6%, EV -25.74%, EV robusto -33.54% → sin value.
  - River Plate vs Atlético Huracán — Under 2.5 Goles (under_2_5): Prob modelo 49.6%, EV -18.64%, EV robusto -26.84% → sin value.
  - Instituto de Córdoba vs Talleres — Under 2.5 Goles (under_2_5): Prob modelo 51.7%, EV -21.48%, EV robusto -29.08% → sin value.
  - CF Montreal vs Columbus Crew SC — Under 2.5 Goles (under_2_5): Prob modelo 29.4%, EV -28.29%, EV robusto -40.49% → sin value.
  - CF Montreal vs Columbus Crew SC — Under 3.5 Goles (under_3_5): Prob modelo 48.3%, EV -25.18%, EV robusto -32.93% → sin value.
  - D.C. United vs Charlotte FC — Under 2.5 Goles (under_2_5): Prob modelo 22.9%, EV -42.62%, EV robusto -55.12% → sin value.
  - D.C. United vs Charlotte FC — Under 3.5 Goles (under_3_5): Prob modelo 38.3%, EV -37.52%, EV robusto -45.67% → sin value.
  - San Jose Earthquakes vs Los Angeles FC — Under 2.5 Goles (under_2_5): Prob modelo 19.8%, EV -48.89%, EV robusto -61.79% → sin value.
  - San Jose Earthquakes vs Los Angeles FC — Under 3.5 Goles (under_3_5): Prob modelo 33.2%, EV -42.58%, EV robusto -51.23% → sin value.
  - New England Revolution vs Orlando City SC — Under 2.5 Goles (under_2_5): Prob modelo 19.4%, EV -44.82%, EV robusto -59.07% → sin value.
  - New England Revolution vs Orlando City SC — Under 3.5 Goles (under_3_5): Prob modelo 32.4%, EV -39.99%, EV robusto -49.24% → sin value.
  - FC Dallas vs Austin FC — Under 2.5 Goles (under_2_5): Prob modelo 24.4%, EV -42.00%, EV robusto -53.90% → sin value.
  - FC Dallas vs Austin FC — Under 3.5 Goles (under_3_5): Prob modelo 40.6%, EV -33.85%, EV robusto -42.00% → sin value.
  - Houston Dynamo vs FC Cincinnati — Under 2.5 Goles (under_2_5): Prob modelo 25.9%, EV -36.42%, EV robusto -48.67% → sin value.
  - Houston Dynamo vs FC Cincinnati — Under 3.5 Goles (under_3_5): Prob modelo 43.0%, EV -28.97%, EV robusto -37.22% → sin value.
  - Minnesota United FC vs LA Galaxy — Under 2.5 Goles (under_2_5): Prob modelo 18.6%, EV -45.80%, EV robusto -60.40% → sin value.
  - Minnesota United FC vs LA Galaxy — Under 3.5 Goles (under_3_5): Prob modelo 31.1%, EV -40.27%, EV robusto -49.87% → sin value.
  - Sporting Kansas City vs Philadelphia Union — Under 2.5 Goles (under_2_5): Prob modelo 19.4%, EV -45.54%, EV robusto -59.54% → sin value.
  - Sporting Kansas City vs Philadelphia Union — Under 3.5 Goles (under_3_5): Prob modelo 32.6%, EV -40.36%, EV robusto -49.51% → sin value.
  - St. Louis City SC vs Toronto FC — Over 2.5 Goles (over_2_5): Prob modelo 70.6%, EV +3.80%, EV robusto -3.55% → sin value.
  - St. Louis City SC vs Toronto FC — Under 2.5 Goles (under_2_5): Prob modelo 29.4%, EV -23.00%, EV robusto -36.10% → sin value.
  - St. Louis City SC vs Toronto FC — Under 3.5 Goles (under_3_5): Prob modelo 48.3%, EV -16.49%, EV robusto -25.14% → sin value.
  - Nashville SC vs Chicago Fire — Under 2.5 Goles (under_2_5): Prob modelo 24.4%, EV -38.61%, EV robusto -51.21% → sin value.
  - Nashville SC vs Chicago Fire — Under 3.5 Goles (under_3_5): Prob modelo 40.6%, EV -32.28%, EV robusto -40.63% → sin value.
  - Colorado Rapids vs Seattle Sounders FC — Under 2.5 Goles (under_2_5): Prob modelo 27.5%, EV -38.65%, EV robusto -49.80% → sin value.
  - Real Salt Lake vs Vancouver Whitecaps FC — Under 2.5 Goles (under_2_5): Prob modelo 20.9%, EV -48.07%, EV robusto -60.47% → sin value.
  - Real Salt Lake vs Vancouver Whitecaps FC — Under 3.5 Goles (under_3_5): Prob modelo 35.1%, EV -41.43%, EV robusto -49.78% → sin value.
  - Portland Timbers vs Atlanta United FC — Under 2.5 Goles (under_2_5): Prob modelo 20.8%, EV -46.21%, EV robusto -59.11% → sin value.
  - Portland Timbers vs Atlanta United FC — Under 3.5 Goles (under_3_5): Prob modelo 34.9%, EV -40.34%, EV robusto -48.89% → sin value.
- **Candidatos con value excluidos por probabilidad-primero:**
  - Tottenham Hotspur vs Aston Villa: Victoria Aston Villa (2) EV +22.16% / EV rob +2.91% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Brighton and Hove Albion vs Arsenal: Victoria Brighton and Hove Albion (1) EV +47.98% / EV rob +21.48% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Everton vs Ipswich Town: Victoria Ipswich Town (2) EV +43.42% / EV rob +19.42% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Newcastle United vs Hull City: Empate (X) EV +9.66% / EV rob -12.94%, Victoria Hull City (2) EV +129.38% / EV rob +101.38% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Nottingham Forest vs Coventry City: Victoria Nottingham Forest (1) EV +6.96% / EV rob -1.54% — No cumple los mínimos de selección probabilidad-primero.
  - Hamburger SV vs 1. FC Köln: Victoria 1. FC Köln (2) EV +57.07% / EV rob +44.07%, Over 3.5 Goles (over_3_5) EV +73.05% / EV rob +61.55% — No cumple los mínimos de selección probabilidad-primero.
  - Werder Bremen vs Augsburg: Victoria Augsburg (2) EV +65.51% / EV rob +51.11%, Over 2.5 Goles (over_2_5) EV +23.68% / EV rob +16.48% — No cumple los mínimos de selección probabilidad-primero.
  - Borussia Monchengladbach vs FSV Mainz 05: Victoria FSV Mainz 05 (2) EV +61.94% / EV rob +50.44%, Over 3.5 Goles (over_3_5) EV +86.26% / EV rob +74.56% — No cumple los mínimos de selección probabilidad-primero.
  - Eintracht Frankfurt vs SC Freiburg: Victoria SC Freiburg (2) EV +45.98% / EV rob +32.18%, Over 2.5 Goles (over_2_5) EV +15.20% / EV rob +8.00% — No cumple los mínimos de selección probabilidad-primero.
  - VfB Stuttgart vs Borussia Dortmund: Victoria Borussia Dortmund (2) EV +77.29% / EV rob +62.99%, Over 2.5 Goles (over_2_5) EV +28.99% / EV rob +22.09% — No cumple los mínimos de selección probabilidad-primero.
  - CA Osasuna vs Rayo Vallecano: Victoria CA Osasuna (1) EV +9.51% / EV rob -3.99%, Victoria Rayo Vallecano (2) EV +6.09% / EV rob -9.01% — No cumple los mínimos de selección probabilidad-primero.
  - Sevilla vs Barcelona: Empate (X) EV +35.05% / EV rob -5.95%, Over 2.5 Goles (over_2_5) EV +11.59% / EV rob +5.19% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Bologna vs Torino: Victoria Bologna (1) EV +14.02% / EV rob +3.82% — No cumple los mínimos de selección probabilidad-primero.
  - AS Roma vs Inter Milan: Victoria AS Roma (1) EV +22.22% / EV rob +8.22%, Over 3.5 Goles (over_3_5) EV +104.47% / EV rob +92.72% — No cumple los mínimos de selección probabilidad-primero.
  - Angers vs Troyes: Victoria Angers (1) EV +5.41% / EV rob -5.74%, Victoria Troyes (2) EV +5.41% / EV rob -12.84% — No cumple los mínimos de selección probabilidad-primero.
  - Toulouse vs Le Havre: Victoria Le Havre (2) EV +7.05% / EV rob -18.45% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Le Mans FC vs Lorient: Victoria Lorient (2) EV +31.17% / EV rob +17.67% — No cumple los mínimos de selección probabilidad-primero.
  - Lyon vs Rennes: Over 3.5 Goles (over_3_5) EV +57.95% / EV rob +45.85%, Victoria Rennes (2) EV +41.64% / EV rob +24.64% — No cumple los mínimos de selección probabilidad-primero.
  - ADO Den Haag vs SC Cambuur: Over 2.5 Goles (over_2_5) EV +11.12% / EV rob +3.72%, Over 3.5 Goles (over_3_5) EV +33.54% / EV rob +22.14%, Victoria SC Cambuur (2) EV +105.37% / EV rob +83.87% — No cumple los mínimos de selección probabilidad-primero.
  - Sparta Rotterdam vs Heerenveen: Victoria Heerenveen (2) EV +17.13% / EV rob +3.63%, Over 2.5 Goles (over_2_5) EV +21.19% / EV rob +13.94%, Over 3.5 Goles (over_3_5) EV +63.80% / EV rob +52.50% — No cumple los mínimos de selección probabilidad-primero.
  - Ajax vs Excelsior: Empate (X) EV +71.04% / EV rob +31.04%, Victoria Excelsior (2) EV +155.84% / EV rob +90.84%, Over 3.5 Goles (over_3_5) EV +9.17% / EV rob +0.72% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Willem II vs Fortuna Sittard: Victoria Willem II (1) EV +23.57% / EV rob +9.97%, Over 3.5 Goles (over_3_5) EV +75.83% / EV rob +63.93% — No cumple los mínimos de selección probabilidad-primero.
  - Gil Vicente vs CS Maritimo: Victoria CS Maritimo (2) EV +5.71% / EV rob -16.79%, Over 2.5 Goles (over_2_5) EV +19.85% / EV rob +8.25% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Nacional vs Famalicão: Victoria Famalicão (2) EV +5.34% / EV rob -5.56%, Over 2.5 Goles (over_2_5) EV +42.82% / EV rob +31.42% — No cumple los mínimos de selección probabilidad-primero.
  - Sporting Lisbon vs Arouca: Empate (X) EV +67.50% / EV rob +25.50%, Victoria Arouca (2) EV +12.48% / EV rob -67.52%, Under 2.5 Goles (under_2_5) EV +5.41% / EV rob -8.99%, Under 3.5 Goles (under_3_5) EV +10.41% / EV rob +0.96% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Gimnasia La Plata vs Banfield: Victoria Banfield (2) EV +34.75% / EV rob +10.25% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Gimnasia Mendoza vs Deportivo Riestra: Over 2.5 Goles (over_2_5) EV +21.75% / EV rob +7.00%, Victoria Deportivo Riestra (2) EV +63.44% / EV rob +41.94% — No cumple los mínimos de selección probabilidad-primero.
  - Union Santa Fe vs Independiente: Victoria Independiente (2) EV +3.04% / EV rob -12.91%, Over 2.5 Goles (over_2_5) EV +28.90% / EV rob +16.60% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - River Plate vs Atlético Huracán: Empate (X) EV +9.64% / EV rob -10.36%, Victoria Atlético Huracán (2) EV +65.04% / EV rob +25.04%, Over 2.5 Goles (over_2_5) EV +21.94% / EV rob +9.84% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Instituto de Córdoba vs Talleres: Victoria Talleres (2) EV +11.43% / EV rob -13.07%, Over 2.5 Goles (over_2_5) EV +21.82% / EV rob +9.22% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - CF Montreal vs Columbus Crew SC: Victoria Columbus Crew SC (2) EV +17.44% / EV rob +3.74%, Over 3.5 Goles (over_3_5) EV +23.12% / EV rob +11.22% — No cumple los mínimos de selección probabilidad-primero.
  - D.C. United vs Charlotte FC: Victoria Charlotte FC (2) EV +11.65% / EV rob -0.35%, Over 3.5 Goles (over_3_5) EV +48.01% / EV rob +36.01% — No cumple los mínimos de selección probabilidad-primero.
  - San Jose Earthquakes vs Los Angeles FC: Victoria San Jose Earthquakes (1) EV +7.94% / EV rob -7.56%, Over 3.5 Goles (over_3_5) EV +56.34% / EV rob +44.64% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - New England Revolution vs Orlando City SC: Empate (X) EV +5.21% / EV rob -17.29%, Over 2.5 Goles (over_2_5) EV +13.70% / EV rob +6.65%, Victoria Orlando City SC (2) EV +34.37% / EV rob +15.11% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - FC Dallas vs Austin FC: Victoria Austin FC (2) EV +3.82% / EV rob -20.18%, Over 3.5 Goles (over_3_5) EV +47.36% / EV rob +34.96% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Houston Dynamo vs FC Cincinnati: Empate (X) EV +3.24% / EV rob -17.76%, Over 2.5 Goles (over_2_5) EV +12.56% / EV rob +4.96%, Over 3.5 Goles (over_3_5) EV +40.10% / EV rob +27.80%, Victoria FC Cincinnati (2) EV +41.26% / EV rob +22.01% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Minnesota United FC vs LA Galaxy: Empate (X) EV +5.93% / EV rob -17.32%, Over 2.5 Goles (over_2_5) EV +13.20% / EV rob +6.25%, Victoria LA Galaxy (2) EV +57.60% / EV rob +33.85% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Sporting Kansas City vs Philadelphia Union: Victoria Philadelphia Union (2) EV +3.80% / EV rob -4.45%, Over 2.5 Goles (over_2_5) EV +15.19% / EV rob +8.04% — No cumple los mínimos de selección probabilidad-primero.
  - St. Louis City SC vs Toronto FC: Empate (X) EV +12.47% / EV rob -10.53%, Victoria Toronto FC (2) EV +47.11% / EV rob +21.11%, Over 3.5 Goles (over_3_5) EV +17.94% / EV rob +6.54% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Nashville SC vs Chicago Fire: Over 3.5 Goles (over_3_5) EV +43.87% / EV rob +31.77%, Victoria Chicago Fire (2) EV +76.86% / EV rob +55.76% — No cumple los mínimos de selección probabilidad-primero.
  - Real Salt Lake vs Vancouver Whitecaps FC: Over 3.5 Goles (over_3_5) EV +55.83% / EV rob +43.83% — No cumple los mínimos de selección probabilidad-primero.
  - Portland Timbers vs Atlanta United FC: Over 2.5 Goles (over_2_5) EV +17.93% / EV rob +10.48%, Over 3.5 Goles (over_3_5) EV +48.45% / EV rob +37.05%, Victoria Atlanta United FC (2) EV +26.98% / EV rob +10.73% — No cumple los mínimos de selección probabilidad-primero.
  - Millonarios vs Boyacá Chicó F.C.: Empate (X) EV +40.61% / EV rob +13.36%, Victoria Boyacá Chicó F.C. (2) EV +138.19% / EV rob +80.49% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Alianza FC vs Independiente Santa Fe: Victoria Independiente Santa Fe (2) EV +31.99% / EV rob +19.24% — No cumple los mínimos de selección probabilidad-primero.
  - Deportivo Cali vs Cúcuta Deportivo: Empate (X) EV +7.73% / EV rob -13.92%, Victoria Cúcuta Deportivo (2) EV +22.18% / EV rob -10.77% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Athletic Bilbao vs Alavés: Victoria Alavés (2) EV +142.43% / EV rob +112.93% — Cuota alta admitida solo como excepción robusta.
  - Celta Vigo vs Real Racing Club de Santander: Victoria Real Racing Club de Santander (2) EV +42.96% / EV rob +20.96% — Cuota alta admitida solo como excepción robusta.
  - Udinese vs Cagliari: Victoria Cagliari (2) EV +64.65% / EV rob +46.90% — Cuota alta admitida solo como excepción robusta.
  - Alverca vs Rio Ave FC: Victoria Rio Ave FC (2) EV +35.49% / EV rob +14.49% — Cuota alta admitida solo como excepción robusta.
  - Colorado Rapids vs Seattle Sounders FC: Victoria Seattle Sounders FC (2) EV +34.14% / EV rob +14.39% — Cuota alta admitida solo como excepción robusta.

## Portfolio y Correlaciones
- **Exposición total:** 1.07u
- **Correlaciones detectadas:** Mercados presentes: over_2_5, over_3_5. Verificar solapamiento de mercado mismo partido.
- **Ajuste de stake por correlación:** Los picks pertenecen a partidos distintos; no se aplica reducción adicional por eventos dependientes.

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1 (AS Roma vs Inter Milan - over_2_5) | PENDIENTE | — | — |
| Pick 2 (VfB Stuttgart vs Borussia Dortmund - over_3_5) | PENDIENTE | — | — |
| Pick 3 (Borussia Monchengladbach vs FSV Mainz 05 - over_2_5) | PENDIENTE | — | — |
| Pick 4 (Venezia vs Lazio - over_2_5) | PENDIENTE | — | — |
| Pick 5 (Hamburger SV vs 1. FC Köln - over_2_5) | PENDIENTE | — | — |
| Pick 6 (Brighton and Hove Albion vs Arsenal - over_2_5) | PENDIENTE | — | — |
