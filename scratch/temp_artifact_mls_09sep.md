# Análisis de Apuestas — 9 de septiembre de 2026

## Metadatos
- **Fecha de análisis:** 2026-09-09T07:00:00-05:00
- **Fecha(s) de partido:** 2026-09-09
- **Information cutoff:** 2026-09-08T21:30:00-05:00
- **Modelo de IA:** big-pickle
- **Versión del motor predictivo:** model-v1.2
- **Ligas analizadas:** Major League Soccer (MLS)
- **Rango de fechas solicitado:** 2026-09-09
- **Partidos en universo:** 14
- **Picks iniciales con value:** 25
- **Picks finales seleccionados:** 3

## Universo Analizado
Se analizaron estrictamente los 14 partidos de la MLS programados para el 2026-09-09 (jornada única; ningún partido fuera del rango de fechas el 2026-09-09):

- Toronto FC vs Nashville SC; CF Montreal vs Charlotte FC; D.C. United vs Columbus Crew; Atlanta United vs Orlando City; Philadelphia Union vs FC Cincinnati; New York City FC vs New England Revolution; Minnesota United vs FC Dallas; Houston Dynamo vs Real Salt Lake; Chicago Fire vs Inter Miami; Austin FC vs Colorado Rapids; Vancouver Whitecaps vs LA Galaxy; San Diego FC vs San Jose Earthquakes; Portland Timbers vs St. Louis City; LAFC vs New York Red Bulls.

Todos los parámetros cuantitativos (lambdas xG por regresión sobre xG_xGA de temporada de FootyStats, probabilidades del ensamble Poisson + Dixon-Coles + Elo + regresión, calibración Platt para 1/2/Over 2.5 de model-v1.2, cuotas justas, edge, EV, EV robusto y stake Kelly fraccionado/4) provienen del ejecutor determinista `scripts/calc_engine.py` con `models/model-v1.2.json` (status active). Elos asignados desde posiciones/diferencial de goles al corte. El ranking y las exclusiones aplican `scripts/selection.py`. Córners/tarjetas omitidos por falta de tasas por equipo verificadas. Over/Under para Atlanta-Orlando y Portland-St. Louis no se evaluaron 2.5 por no existir cuota 2.5 verificable (totales de las casas a 3.0).

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Houston Dynamo vs Real Salt Lake | Over 2.5 | Over 2.5 | prioritario | 1.60 | 71.0% | 1.41 | +13.6% | +13.6% | +5.6% | 0.06u | Baja/Media |
| 2 | CF Montreal vs Charlotte FC | Over 2.5 | Over 2.5 | excluido | 1.55 | 70.6% | 1.42 | +9.4% | +9.4% | +1.7% | 0.04u | Baja/Media |
| 3 | Austin FC vs Colorado Rapids | Over 2.5 | Over 2.5 | prioritario | 1.74 | 68.6% | 1.46 | +19.4% | +19.4% | +10.7% | 0.07u | Baja/Media |
| 4 | New York City FC vs New England Revolution | Over 2.5 | Over 2.5 | prioritario | 1.85 | 68.5% | 1.46 | +26.7% | +26.7% | +17.4% | 0.08u | Baja/Media |
| 5 | Minnesota United vs FC Dallas | Over 2.5 | Over 2.5 | excluido | 1.54 | 67.7% | 1.48 | +4.2% | +4.2% | +-3.5% | 0.02u | Baja/Media |
| 6 | D.C. United vs Columbus Crew | Over 2.5 | Over 2.5 | excluido | 1.66 | 66.8% | 1.50 | +10.9% | +10.9% | +2.6% | 0.04u | Baja/Media |
| 7 | Toronto FC vs Nashville SC | Over 2.5 | Over 2.5 | excluido | 1.67 | 62.6% | 1.60 | +4.6% | +4.6% | +-3.7% | 0.02u | Baja/Media |
| 8 | Portland Timbers vs St. Louis City | 2 | 2 | excluido | 2.80 | 49.9% | 2.00 | +39.8% | +39.8% | +25.8% | 0.06u | Baja/Media |
| 9 | Austin FC vs Colorado Rapids | 2 | 2 | excluido | 2.70 | 49.8% | 2.01 | +34.6% | +34.6% | +21.1% | 0.05u | Baja/Media |
| 10 | Toronto FC vs Nashville SC | 2 | 2 | excluido | 2.30 | 47.1% | 2.12 | +8.3% | +8.3% | +-3.2% | 0.02u | Baja/Media |
| 11 | Chicago Fire vs Inter Miami | 2 | 2 | excluido | 2.80 | 42.2% | 2.37 | +18.3% | +18.3% | +4.3% | 0.03u | Baja/Media |
| 12 | D.C. United vs Columbus Crew | 2 | 2 | excluido | 2.60 | 41.9% | 2.39 | +8.9% | +8.9% | +-4.1% | 0.01u | Baja/Media |
| 13 | San Diego FC vs San Jose Earthquakes | 2 | 2 | excepcional | 3.80 | 40.2% | 2.49 | +52.6% | +52.6% | +33.6% | 0.05u | Baja/Media |
| 14 | New York City FC vs New England Revolution | 2 | 2 | excluido | 3.00 | 36.8% | 2.72 | +10.4% | +10.4% | +-4.6% | 0.01u | Baja/Media |
| 15 | Houston Dynamo vs Real Salt Lake | 2 | 2 | excepcional | 4.20 | 36.2% | 2.76 | +52.1% | +52.1% | +31.1% | 0.04u | Baja/Media |
| 16 | Minnesota United vs FC Dallas | 2 | 2 | excluido | 3.20 | 35.2% | 2.84 | +12.6% | +12.6% | +-3.4% | 0.01u | Baja/Media |
| 17 | LAFC vs New York Red Bulls | 2 | 2 | excepcional | 6.00 | 33.4% | 3.00 | +100.2% | +100.2% | +70.2% | 0.05u | Baja/Media |
| 18 | San Diego FC vs San Jose Earthquakes | Under 2.5 | Under 2.5 | excluido | 3.40 | 30.8% | 3.24 | +4.9% | +4.9% | +-12.1% | 0.01u | Baja/Media |
| 19 | Philadelphia Union vs FC Cincinnati | 2 | 2 | excluido | 4.20 | 27.4% | 3.65 | +15.1% | +15.1% | +-5.9% | 0.01u | Baja/Media |
| 20 | San Diego FC vs San Jose Earthquakes | X | X | excluido | 4.20 | 25.8% | 3.88 | +8.2% | +8.2% | +-12.8% | 0.01u | Baja/Media |
| 21 | Chicago Fire vs Inter Miami | X | X | excluido | 4.20 | 25.4% | 3.93 | +6.8% | +6.8% | +-14.2% | 0.01u | Baja/Media |
| 22 | LAFC vs New York Red Bulls | X | X | excluido | 5.60 | 24.1% | 4.15 | +35.0% | +35.0% | +7.0% | 0.02u | Baja/Media |
| 23 | Philadelphia Union vs FC Cincinnati | X | X | excluido | 4.33 | 24.1% | 4.15 | +4.2% | +4.2% | +-17.4% | 0.00u | Baja/Media |
| 24 | Vancouver Whitecaps vs LA Galaxy | X | X | excluido | 5.75 | 22.5% | 4.44 | +29.4% | +29.4% | +0.6% | 0.02u | Baja/Media |
| 25 | Vancouver Whitecaps vs LA Galaxy | 2 | 2 | excluido | 6.50 | 17.3% | 5.78 | +12.5% | +12.5% | +-20.0% | 0.01u | Baja/Media |

## Picks Recomendados (Top 3)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Houston Dynamo vs Real Salt Lake | Over 2.5 | Over 2.5 | prioritario | 1.60 | 71.0% | 1.41 | +13.6% | +13.6% | +5.6% | 0.06u | Media |
| 2 | Austin FC vs Colorado Rapids | Over 2.5 | Over 2.5 | prioritario | 1.74 | 68.6% | 1.46 | +19.4% | +19.4% | +10.7% | 0.07u | Media |
| 3 | New York City FC vs New England Revolution | Over 2.5 | Over 2.5 | prioritario | 1.85 | 68.5% | 1.46 | +26.7% | +26.7% | +17.4% | 0.08u | Media-Alta |

## Detalle de Picks
### Pick 1: Houston Dynamo vs Real Salt Lake
- **Mercado:** O/U 2.5
- **Selección:** Over 2.5
- **Cuota:** 1.6
- **Probabilidad modelo:** 71.0%
- **Probabilidad conservadora:** 66.0%
- **Probabilidad implícita:** 62.5%
- **Cuota justa:** 1.41
- **Edge:** +13.6%
- **EV:** +13.6%
- **EV robusto:** +5.6%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.52
- **Stake:** 0.06u
- **Confianza:** Media
- **Incertidumbre:** Media-Alta (EV robusto al filo del umbral +5.6%; un shock de −0.15 en ataque lo deja en −0.9%)
- **Por qué:** El motor (λ 1.59–1.40; xG temporada HOU 1.46/1.44, RSL 1.61/1.47) proyecta 71.0% de Over 2.5 calibrado (Platt) frente al 62.5% implícito en la cuota 1.60. Real Salt Lake llega en caída libre (0 victorias en 5, 1-3-7 fuera de casa) y sus partidos de visitante promedian ~3.1 goles con BTTS en 9 de 10, mientras Houston es sólido en casa (6-2-2 últimos 10) con defensa de 0.6 GA/g. La cuota 1.60 (sportsgambler/transfermarkt) está por encima de la justa 1.41. El perfil bajogol local de Houston se compensa con la tendencia altogol visitante de RSL.
- **Riesgos:** Valor frágil: en el análisis de sensibilidad, −0.15 de xG en ambos ataques reduce el EV robusto a −0.9%. Si RSL (1 gol en 2 de los últimos 5) no comparece en ataque, el partido puede quedar 1-0/2-0. Houston controló 0-0 ante Charlotte en la última jornada.
- **Fuentes:** sportsgambler.com O/U 1.60/2.30; Wincomparator 1X2 (HOU 1.88, draw 4.09); transfermarkt BTTS 1.62; xG FootyStats; forma por sportsline.com tabla de oponentes.

### Pick 2: New York City FC vs New England Revolution
- **Mercado:** O/U 2.5
- **Selección:** Over 2.5
- **Cuota:** 1.85
- **Probabilidad modelo:** 68.5%
- **Probabilidad conservadora:** 63.5%
- **Probabilidad implícita:** 54.0%
- **Cuota justa:** 1.46
- **Edge:** +26.7%
- **EV:** +26.7%
- **EV robusto:** +17.4%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.58
- **Stake:** 0.08u
- **Confianza:** Media-Alta
- **Incertidumbre:** Media (robusto: con shock −0.15 en ambos ataques el EV robusto se mantiene en +9.5%)
- **Por qué:** El motor (λ 1.60–1.29; xG temporada NYC 1.39/1.43, NE 1.41/1.56) proyecta 68.5% de Over 2.5 calibrado frente al 54.1% implícito en la cuota 1.85 (SportsLine opened +118/+122). New England fuera de casa concede 2.26 goles/partido (scoreo) y su marcador típico como visitante es altogol (3-1 @CLB, 3-0 @DCU, 1-2 @TOR recientes); NYC mantiene producción en casa pese a la racha de 5 sin ganar. La cuota 1.85 es la más generosa del panel y supera claramente la justa 1.46; cuota mínima exigida 1.58.
- **Riesgos:** NYC viene de empates de bajo gol (0-0 vs NSH, 1-1 @TOR, 1-1 @NE en el H2H de agosto) y su xG ofensivo de temporada es moderado (1.39) para un equipo de casa. Si el juego se traba en la medular el Under es posible. Rotaciones por congestión del calendario MLS.
- **Fuentes:** sportsline.com O/U 1.85/1.86 (jalones +118/+122); transfermarkt 1X2 2.20/3.60/3.10 y BTTS 1.57/2.40; xG FootyStats; forma y rachas por transfermarkt.

### Pick 3: Austin FC vs Colorado Rapids
- **Mercado:** O/U 2.5
- **Selección:** Over 2.5
- **Cuota:** 1.74
- **Probabilidad modelo:** 68.6%
- **Probabilidad conservadora:** 63.6%
- **Probabilidad implícita:** 57.5%
- **Cuota justa:** 1.46
- **Edge:** +19.4%
- **EV:** +19.4%
- **EV robusto:** +10.7%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.57
- **Stake:** 0.07u
- **Confianza:** Media
- **Incertidumbre:** Media (frente a un shock de −0.15 en ambos ataques el EV robusto baja a +3.2%)
- **Por qué:** El motor (λ 1.40–1.50; xG temporada ATX 1.26/1.91 —una de las peores defensas del Oeste—, COL 1.35/1.28) proyecta 68.6% de Over 2.5 calibrado frente al 57.5% implícito en la cuota 1.74 (sportsgambler −135). Austin en casa genera partidos abiertos (marcó al menos 1 en 9 de 10 en casa y su xGA es 1.91) y Colorado llega en la mejor forma del Oeste (4W-1L en 5), anotando con regularidad. La cuota justa 1.46 deja margen; BTTS -172 refuerza el perfil.
- **Riesgos:** El punto débil es la producción a domicilio de Colorado (0.9 GF fuera, 2-1-7 en últimos 10 como visitante): si los Rapids no comparecen con gol, partidos 1-0/2-0. El valor se erosiona rápido (−0.15 de xG deja EVr en +3.2%).
- **Fuentes:** sportsgambler.com O/U 1.74/2.05 y BTTS −172; sportshub O/U −159/+123; xG FootyStats; forma por sportsline (COL 4W-1L en 5).

## NO BET / Excluidos
- **San Diego FC vs San Jose Earthquakes — SJ (2) a 3.80:** el motor marcó el longshot con EV robusto +33.6%, pero es el menos robusto del panel: con un descuento de forma coherente (SJ con 2 goles en sus últimos 5, 0W-2D-3L; SD con 3 victorias en casa por 3-0, 3-1 y 1-0) el EV robusto colapsa a +1.5% (−15% con descuento mayor). Longshot excluido por robustez/actualidad.
- **Houston Dynamo vs Real Salt Lake — RSL (2) a 4.20:** EV robusto +31.1%→−2.1% con el descuento de forma real de RSL (0-1-4 en 5, 1-3-7 fuera). Cuota alta sin value real.
- **Austin FC vs Colorado Rapids — COL (2) a 2.70:** +21.1%→+0.5% al aplicar el split real de Colorado como visitante (0.9 GF, 2-1-7). Valor evaporado.
- **Portland Timbers vs St. Louis — STL (2) a 2.80:** EV robusto +25.8% se mantiene (+14.9% con shock), pero la cuota 2.80 cae fuera de las bandas probabilidad-primero (longshot exige ≥3.00 y prioritario ≤2.20). Marginado por regla, no por falta de valor.
- **LAFC vs NY Red Bulls — NYRB (2) a 6.00:** excepcional del motor (+70% EVr) sin cupo (una sola excepción por portfolio) y con plausibilidad baja: NYRB perdió 5 de 8, 46 goles en contra y sin victoria en casa del LAFC en el tramo reciente. Excluido.
- **Resto sin valor robusto suficiente:** Toronto–Nashville (2 a 2.30, EVr −3.2%; Over 1.67, −3.7%); Montreal–Charlotte (Over 1.55, +1.7%); DC United–Columbus (2 a 2.60, −4.1%; Over 1.66, +2.6%); Philadelphia–Cincinnati (X a 4.33, −17.4%; 2 a 4.20, −5.9%; Over 1.36, −5.6%); NYCFC–New England (2 a 3.00, −4.6%); Minnesota–Dallas (2 a 3.20, −3.4%; Over 1.54, −3.5%); Chicago–Miami (X a 4.20, −14.2%; 2 a 2.80, +4.3%<5%; Over 1.26, −15.1%); Vancouver–LA Galaxy (X a 5.75, +0.6%; 2 a 6.50, −20.0%; Over 1.34, −11.8%); San Diego–San Jose (Under 3.40, −12.1%; X 4.20, −12.8%); LAFC–NYRB (X a 5.60, +7.0%<mínimo longshot 10%; Over 1.32, −10.6%).
- Atlanta–Orlando y Portland–St. Louis: sin mercado Over/Under 2.5 disponible (totales a 3.0 y/o sin cuota 2.5 verificable); solo 1X2 analizado.

## Portfolio y Correlaciones
- **Exposición total:** 0.21u (0.08u + 0.06u + 0.07u)
- **Correlaciones detectadas:** Sin solapamiento de equipos (3 partidos distintos). Los tres picks son Over 2.5 en la misma fecha de MLS, por lo que existe una correlación débil y transversal por inflación de goles de la jornada (congestión de calendario, arbitrajes favorables al gol). No hay correlación de mercado cruzada entre partidos.
- **Ajuste de stake por correlación:** No procede reducir más: los stakes ya aplican Kelly fraccionado/4 del motor (0.06–0.08u) y son conservadores; se documenta la correlación débil de jornada como riesgo lateral.

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Houston Dynamo vs Real Salt Lake (Over 2.5) a 1.60 | PENDIENTE | — | — |
| New York City FC vs New England Revolution (Over 2.5) a 1.85 | PENDIENTE | — | — |
| Austin FC vs Colorado Rapids (Over 2.5) a 1.74 | PENDIENTE | — | — |
