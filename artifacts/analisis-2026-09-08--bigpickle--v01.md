# Análisis de Apuestas — 8 de septiembre de 2026

## Metadatos
- **Fecha de análisis:** 2026-09-08T07:00:00-05:00
- **Fecha(s) de partido:** 2026-09-08
- **Information cutoff:** 2026-09-07T23:59:00-05:00
- **Modelo de IA:** bigpickle
- **Versión del motor predictivo:** model-v1.2
- **Ligas analizadas:** Champions League, EFL Cup (Inglaterra), Eredivisie, Copa Libertadores, Copa Sudamericana
- **Rango de fechas solicitado:** 2026-09-08
- **Partidos en universo:** 15
- **Picks iniciales con value:** 21
- **Picks finales seleccionados:** 3

## Universo Analizado
Se analizaron estrictamente los partidos programados para el 2026-09-08 (ninguno fuera del rango):

- **Champions League (MD1):** AEK Atenas vs LASK Linz; Club Brugge vs Aston Villa; Borussia Dortmund vs Villarreal; FC Porto vs Manchester City; Lille vs Real Betis; Real Madrid vs Inter Milan.
- **EFL Cup (Ronda 3, Inglaterra):** Bournemouth vs Lincoln City; Crystal Palace vs Middlesbrough; Leyton Orient vs Bradford City; Millwall vs Newcastle United; Sunderland vs Hull City.
- **Eredivisie:** NEC Nijmegen vs Excelsior.
- **Copa Libertadores (CF ida):** Fluminense vs Platense.
- **Copa Sudamericana (CF ida):** Independiente Santa Fe vs Vasco da Gama; Boca Juniors vs São Paulo.

Todos los parámetros cuantitativos (lambdas xG, probabilidades del ensamble Poisson + Dixon-Coles + Elo + regresión, probabilidades Platt-calibradas para 1, 2 y Over 2.5, cuotas justas, edge, EV, EV robusto y stake Kelly fraccionado/4) provienen del ejecutor determinista `scripts/calc_engine.py` con `models/model-v1.2.json` (status active). El ranking y las exclusiones aplican `scripts/selection.py`. Los mercados de córners/tarjetas se omitieron por falta de tasas verificadas por equipo; los totales solo se incluyeron cuando existía cuota contrastable.

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | NEC Nijmegen vs Excelsior | 1X2 | Excelsior (2) | excepcional | 5.60 | 41.6% | 2.40 | +133.1% | +133.1% | +105.1% | 0.07u | Media |
| 2 | Crystal Palace vs Middlesbrough | 1X2 | Middlesbrough (2) | excepcional | 4.40 | 39.5% | 2.53 | +73.6% | +73.6% | +51.6% | 0.05u | Media |
| 3 | Sunderland vs Hull City | 1X2 | Hull City (2) | excepcional | 4.70 | 34.4% | 2.91 | +61.5% | +61.5% | +38.0% | 0.04u | Media |
| 4 | Bournemouth vs Lincoln City | 1X2 | Lincoln City (2) | excluido | 8.20 | 19.5% | 5.14 | +59.6% | +59.6% | +18.6% | 0.02u | Baja |
| 5 | Boca Juniors vs São Paulo | 1X2 | São Paulo (2) | excepcional | 4.10 | 32.3% | 3.10 | +32.4% | +32.4% | +11.8% | 0.03u | Media |
| 6 | Lille vs Real Betis | O/U 2.5 | Over 2.5 | prioritario | 1.83 | 65.8% | 1.52 | +20.4% | +20.4% | +11.3% | 0.06u | Media |
| 7 | Borussia Dortmund vs Villarreal | O/U 2.5 | Over 2.5 | prioritario | 1.62 | 70.6% | 1.42 | +14.4% | +14.4% | +6.3% | 0.06u | Media |
| 8 | FC Porto vs Manchester City | O/U 2.5 | Over 2.5 | excluido | 1.64 | 67.9% | 1.47 | +11.4% | +11.4% | +3.2% | 0.04u | Baja |
| 9 | Real Madrid vs Inter Milan | 1X2 | Inter Milan (2) | excluido | 4.85 | 26.1% | 3.83 | +26.8% | +26.8% | +2.5% | 0.02u | Baja |
| 10 | Millwall vs Newcastle United | O/U 2.5 | Over 2.5 | excluido | 1.64 | 66.5% | 1.50 | +9.1% | +9.1% | +0.9% | 0.04u | Baja |
| 11 | Bournemouth vs Lincoln City | 1X2 | Empate (X) | excluido | 5.40 | 23.4% | 4.27 | +26.4% | +26.4% | -0.6% | 0.01u | Baja |
| 12 | AEK Atenas vs LASK Linz | O/U 2.5 | Over 2.5 | excluido | 1.63 | 65.8% | 1.52 | +7.2% | +7.2% | -0.9% | 0.03u | Baja |
| 13 | Sunderland vs Hull City | O/U 2.5 | Under 2.5 | excluido | 1.85 | 58.5% | 1.71 | +8.3% | +8.3% | -1.0% | 0.02u | Baja |
| 14 | Independiente Santa Fe vs Vasco da Gama | 1X2 | Vasco da Gama (2) | excluido | 3.25 | 35.4% | 2.83 | +14.9% | +14.9% | -1.3% | 0.02u | Baja |
| 15 | Club Brugge vs Aston Villa | O/U 2.5 | Over 2.5 | excluido | 1.63 | 65.1% | 1.54 | +6.1% | +6.1% | -2.1% | 0.02u | Baja |
| 16 | Leyton Orient vs Bradford City | O/U 2.5 | Over 2.5 | excluido | 2.00 | 53.6% | 1.86 | +7.3% | +7.3% | -2.7% | 0.02u | Baja |
| 17 | Sunderland vs Hull City | BTTS | No ambos marcan | excluido | 1.85 | 57.3% | 1.75 | +6.0% | +6.0% | -3.3% | 0.02u | Baja |
| 18 | Sunderland vs Hull City | 1X2 | Empate (X) | excluido | 3.70 | 30.8% | 3.25 | +13.8% | +13.8% | -4.7% | 0.01u | Baja |
| 19 | Fluminense vs Platense | 1X2 | Platense (2) | excluido | 10.00 | 14.3% | 7.01 | +42.7% | +42.7% | -7.3% | 0.01u | Baja |
| 20 | Leyton Orient vs Bradford City | 1X2 | Leyton Orient (1) | excluido | 3.05 | 35.1% | 2.84 | +7.2% | +7.2% | -8.0% | 0.01u | Baja |
| 21 | NEC Nijmegen vs Excelsior | 1X2 | Empate (X) | excluido | 4.33 | 24.9% | 4.01 | +7.9% | +7.9% | -13.8% | 0.01u | Baja |

## Picks Recomendados (Top 3)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | NEC Nijmegen vs Excelsior | 1X2 | Excelsior (2) | excepcional | 5.60 | 41.6% | 2.40 | +133.1% | +133.1% | +105.1% | 0.07u | Media |
| 2 | Lille vs Real Betis | O/U 2.5 | Over 2.5 | prioritario | 1.83 | 65.8% | 1.52 | +20.4% | +20.4% | +11.3% | 0.06u | Media |
| 3 | Borussia Dortmund vs Villarreal | O/U 2.5 | Over 2.5 | prioritario | 1.62 | 70.6% | 1.42 | +14.4% | +14.4% | +6.3% | 0.06u | Media |

## Detalle de Picks

### Pick 1: NEC Nijmegen vs Excelsior
- **Mercado:** 1X2
- **Selección:** Excelsior (2)
- **Cuota:** 5.60
- **Probabilidad modelo:** 41.6%
- **Probabilidad conservadora:** 36.6%
- **Probabilidad implícita:** 17.9%
- **Cuota justa:** 2.40
- **Edge:** +133.1%
- **EV:** +133.1%
- **EV robusto:** +105.1%
- **Perfil de selección:** excepcional
- **Cuota mínima:** 2.73
- **Stake:** 0.07u
- **Confianza:** Media
- **Incertidumbre:** Alta (divergencia modelo-mercado severa; muestra Eredivisie pequeña)
- **Por qué:** Las lambdas del motor (NEC 1.48 – 1.45 Excelsior; Elo 1580 vs 1520 + localía) y el ensamble determinista dan 41.6% a la victoria de Excelsior, frente a un 17.9% implícito en la cuota 5.60. NEC llega eliminado de la UCL (derrota global vs Bodo/Glimt), con mal rendimiento local esta temporada, baja de su portero suspendido e incertidumbre directiva; Excelsior no pierde contra el NEC en los últimos 10 duelos (mayoría de empates) y llega con buenas prestaciones en Eredivisie (victorias ante Cambuur, Sparta Rotterdam y Willem II). La calibración Platt de visitantes (corregida en v1.2, mercado 1X2 visitante con mejor ROI en backtest) soporta el juicio. El único longshot del portfolio admite el pick como excepción robusta.
- **Riesgos:** El edge es enorme y depende de que las cuotas estén severamente desalineadas; si el mercado (NEC favorito claro) está mejor informado, el EV real puede ser negativo. Rotaciones/titulares del Excelsior, muestra de solo 4 jornadas de Eredivisie y tendencia histórica al empate en el H2H elevan la varianza. La cuota puede bajar antes del kickoff.
- **Fuentes:** OddsSafari (cuota 5.60 visitante), Sports Mole prediction (NEC 1-2 Excelsior), telecomasia/1xBet cuotas 1X2, transfermarkt tabla Eredivisie 2026/27, EFL/Sporting Life cronología UCL NEC vs Bodo/Glimt.

### Pick 2: Lille vs Real Betis
- **Mercado:** O/U 2.5
- **Selección:** Over 2.5
- **Cuota:** 1.83
- **Probabilidad modelo:** 65.8%
- **Probabilidad conservadora:** 60.8%
- **Probabilidad implícita:** 54.6%
- **Cuota justa:** 1.52
- **Edge:** +20.4%
- **EV:** +20.4%
- **EV robusto:** +11.3%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.64
- **Stake:** 0.06u
- **Confianza:** Media
- **Incertidumbre:** Media-Alta (el Over 2.5 dependió históricamente de supuestos de xG; sensibilidad: con xG −0.15 el valor se anula)
- **Por qué:** El modelo de goles (λ total ≈ 2.8) produce un 65.8% de Over 2.5 frente al 54.6% implícito. Lille juega en casa con intensidad ofensiva y el Betis afronta la gira con plantilla corta y rotaciones; la cuota 1.83 está por encima de la cuota justa 1.52. La calibración Platt de Over 2.5 (v1.2) corrige la miscalibración previa de este mercado.
- **Riesgos:** En el análisis de sensibilidad, un shock de xG de ±0.15 en ambos equipos deja el EV robusto en negativo (−6.2%), por lo que el valor es frágil a los supuestos de input. Primer partido de fase de grupos suele ser cauto y el modelo Extratips público (52% Under) contradice el Over. Vigilar alineaciones de Pellegrini (rotaciones) antes del cierre.
- **Fuentes:** OddsSafari/ESPN odds (Over 2.5 1.83), BetMGM opciones Over/Under, Extratips xG, Sports Mole preview Lille vs Betis (alineaciones y bajas).

### Pick 3: Borussia Dortmund vs Villarreal
- **Mercado:** O/U 2.5
- **Selección:** Over 2.5
- **Cuota:** 1.62
- **Probabilidad modelo:** 70.6%
- **Probabilidad conservadora:** 65.6%
- **Probabilidad implícita:** 61.7%
- **Cuota justa:** 1.42
- **Edge:** +14.4%
- **EV:** +14.4%
- **EV robusto:** +6.3%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.52
- **Stake:** 0.06u
- **Confianza:** Media
- **Incertidumbre:** Alta (margen EV robusto ajustado al umbral; sensible a −0.15 de xG)
- **Por qué:** El Dortmund es de los equipos con mayor producción ofensiva en la clasificación de CL (16 goles) y Villarreal, aún fuerte en ataque, concede goles fuera de casa; λ total ≈ 2.97 → 70.6% Over 2.5 (calibrado Platt) frente al 61.7% implícito. La cuota 1.62 supera el umbral probabilidad-primero con EV robusto +6.3% y cuota justa 1.42.
- **Riesgos:** Valor al filo del umbral: un shock de −0.15 en xG deja EV robusto en −7.6%, por lo que la probabilidad dependió críticamente de los inputs agregados al motor. Rotaciones del BVB con la agenda cargada y la costumbre del Villarreal de partidos trabados en la fase de grupos son los principales riesgos.
- **Fuentes:** mrfixstips/TelecomAsia odds (1X2 y Over/Under), OddsSafari splits Over 2.5, ESPN odds line, Sports Mole preview con datos de producción ofensiva del Dortmund.

## NO BET / Excluidos
- **Real Madrid vs Inter Milan — Inter (2) a 4.85:** probabilidad modelo 26.1% por debajo del mínimo reforzado del 30% (solamente EV bruto positivo).
- **FC Porto vs Manchester City — Over 2.5 a 1.64:** EV robusto +3.2%, por debajo del mínimo 5%.
- **Club Brugge vs Aston Villa — Over 2.5 a 1.63:** EV robusto −2.1%. No hay valor.
- **AEK Atenas vs LASK Linz — Over 2.5 a 1.63:** EV robusto −0.9%. No hay valor.
- **Millwall vs Newcastle — Over 2.5 a 1.64:** EV robusto +0.9%, insuficiente.
- **Bournemouth vs Lincoln — Lincoln (2) a 8.20 y Empate a 5.40:** probabilidad modelo 19.5% y EV robusto negativo: máximos de longshot no alcanzados.
- **Crystal Palace vs Middlesbrough — Middlesbrough (2) a 4.40:** excepcional robusto (EV robusto +51.6%) pero se permite un único longshot por portfolio; se prioriza el de mayor EV robusto/probabilidad (NEC–Excelsior).
- **Sunderland vs Hull — Hull (2) a 4.70, Empate a 3.70, Under 2.5 a 1.85 y No ambos marcan a 1.85:** el único longshot del portfolio se destina al pick NEC; los mercados de cuota media no alcanzan EV robusto ≥5%.
- **Fluminense vs Platense — Platense (2) a 10.00:** probabilidad 14.3% y EV robusto −7.3%: fuera de los mínimos reforzados.
- **Independiente Santa Fe vs Vasco — Vasco (2) a 3.25:** EV robusto −1.3%. No hay valor.
- **Boca Juniors vs São Paulo — São Paulo (2) a 4.10:** excepcional robusto (EV robusto +11.8%) sin cupo: un solo longshot por portfolio.
- **Leyton Orient vs Bradford — Orient (1) a 3.05 y Over 2.5 a 2.00:** EV robusto −8.0% y −2.7%. No hay valor.
- **NEC vs Excelsior — Empate a 4.33:** EV robusto −13.8% aunque el mercado esté al alcance.

## Portfolio y Correlaciones
- **Exposición total:** 0.19u
- **Correlaciones detectadas:** Ninguna de solapamiento de equipos: los 3 picks son partidos distintos y ligas distintas (Eredivisie + Champions League). Los dos Over 2.5 son independientes entre sí (no comparten equipos) y están no correlacionados con el 1X2 de Excelsior.
- **Ajuste de stake por correlación:** No procede ajuste por correlación; los stakes ya reflejan Kelly fraccionado/4 del motor (0.06–0.07u) y el tope de longshot de 0.25u.

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| NEC Nijmegen vs Excelsior (2) a 5.60 | PENDIENTE | — | — |
| Lille vs Real Betis (Over 2.5) a 1.83 | PENDIENTE | — | — |
| Borussia Dortmund vs Villarreal (Over 2.5) a 1.62 | PENDIENTE | — | — |