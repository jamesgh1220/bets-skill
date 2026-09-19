# Análisis de Apuestas — 2026-09-18

## Metadatos
- **Fecha de análisis:** 2026-09-18T01:48:28Z
- **Fecha(s) de partido:** 2026-09-18
- **Information cutoff:** 2026-09-18T01:48:28Z
- **Modelo de IA:** bigpickle
- **Versión del motor predictivo:** model-v1.3
- **Ligas analizadas:** Premier League, Bundesliga, Ligue 1, Serie A, La Liga, Eredivisie, MLS, Liga Argentina (Primera División), Liga Colombiana (Primera A)
- **Rango de fechas solicitado:** 18 de septiembre de 2026 (un día)
- **Partidos en universo:** 9
- **Picks iniciales con value:** 24
- **Picks finales seleccionados:** 4

## Universo Analizado
Universo = partidos del 2026-09-18 por liga solicitada (top-1 por liga en la fecha). Cuotas: The Odds API vía REST (fallback documentado; el MCP `odds-api` devolvió vacío y el plan gratis expone solo h2h y totals). Timestamp de captura de cuotas: 2026-09-18T01:48:28Z (referencia CLV). El MCP `apifootball` estaba inoperativo ('Authentification failed!'); el MCP local `football-stats` devolvió MISSING_SOURCE para varias ligas; se usó fallback con datos Understat para xG y Elo. Liga Colombiana no disponible en The Odds API: cuotas h2h tomadas del agregador (bwin/admiralbet) — Capa 3, solo 1X2. xG estimados (sin serie completa) en Monza, Espanyol, NYCFC, Central Córdoba y Medellín: se marcó `xg_estimado` en los inputs y se aplicó incertidumbre adicional. Mercados sin cuota capturada (1.5 goles, BTTS, DO, DNB, córners, tarjetas): n/d, nunca inventados; la probabilidad de córners/tarjetas se documenta solo cuando los 8 campos estaban disponibles y con cuota n/d se deja el mercado como no disponible.
- **Brentford vs Chelsea** (Premier League) — 18-09 19:00 UTC — cuotas 1X2 y totals (2.5/3.5).
- **Bayern Munich vs Union Berlin** (Bundesliga) — 18-09 18:30 UTC — cuotas 1X2 y totals (2.5/3.5).
- **AS Monaco vs RC Lens** (Ligue 1) — 18-09 18:45 UTC — cuotas 1X2 y totals (2.5/3.5).
- **Monza vs Sassuolo** (Serie A) — 18-09 18:45 UTC — cuotas 1X2 y totals (2.5).
- **Espanyol vs Elche CF** (La Liga) — 18-09 19:00 UTC — cuotas 1X2 y totals (2.5).
- **Groningen vs FC Zwolle** (Eredivisie) — 18-09 18:00 UTC — cuotas 1X2 y totals (2.5/3.5).
- **New York City FC vs New York Red Bulls** (MLS) — 18-09 23:30 UTC — cuotas 1X2 y totals (2.5/3.5).
- **Central Córdoba vs Defensa y Justicia** (Argentina) — 18-09 21:00 UTC — cuotas 1X2 y totals (2.5).
- **Independiente Medellín vs Jaguares** (Colombia) — 18-09 20:10 COL — solo h2h (Capa 3, agregador).

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | AS Monaco vs RC Lens | over_2_5 | Over 2.5 Goles | prioritario | 1.56 | 81.0% | 1.23 | +26.36% | +26.36% | +18.56% | 0.12u | Media-Alta |
| 2 | Groningen vs FC Zwolle | over_2_5 | Over 2.5 Goles | excluido | 1.42 | 76.0% | 1.32 | +7.86% | +7.86% | +0.76% | 0.05u | Media-Alta |
| 3 | Brentford vs Chelsea | over_2_5 | Over 2.5 Goles | excluido | 1.49 | 75.9% | 1.32 | +13.03% | +13.03% | +5.58% | 0.07u | Media-Alta |
| 4 | Monza vs Sassuolo | over_2_5 | Over 2.5 Goles | prioritario | 1.82 | 71.3% | 1.40 | +29.69% | +29.69% | +20.59% | 0.09u | Media-Alta |
| 5 | Central Córdoba vs Defensa y Justicia | over_2_5 | Over 2.5 Goles | excluido | 2.48 | 68.5% | 1.46 | +69.83% | +69.83% | +57.43% | 0.12u | Media-Alta |
| 6 | AS Monaco vs RC Lens | over_3_5 | Over 3.5 Goles | excluido | 2.38 | 68.2% | 1.47 | +62.22% | +62.22% | +50.32% | 0.11u | Media-Alta |
| 7 | Espanyol vs Elche CF | over_2_5 | Over 2.5 Goles | prioritario | 1.90 | 65.8% | 1.52 | +25.02% | +25.02% | +15.52% | 0.07u | Media-Alta |
| 8 | Groningen vs FC Zwolle | over_3_5 | Over 3.5 Goles | excluido | 2.12 | 60.0% | 1.67 | +27.09% | +27.09% | +16.49% | 0.06u | Media-Alta |
| 9 | Brentford vs Chelsea | over_3_5 | Over 3.5 Goles | excluido | 2.23 | 59.8% | 1.67 | +33.33% | +33.33% | +22.18% | 0.07u | Media-Alta |
| 10 | New York City FC vs New York Red Bulls | over_3_5 | Over 3.5 Goles | excluido | 2.30 | 51.9% | 1.93 | +19.39% | +19.39% | +7.89% | 0.04u | Media |
| 11 | Monza vs Sassuolo | 2 | Victoria Sassuolo | excluido | 2.56 | 47.4% | 2.11 | +21.34% | +21.34% | +8.54% | 0.03u | Baja |
| 12 | AS Monaco vs RC Lens | 2 | Victoria RC Lens | excepcional | 3.65 | 46.4% | 2.16 | +69.36% | +69.36% | +51.11% | 0.07u | Baja |
| 13 | Central Córdoba vs Defensa y Justicia | 2 | Victoria Defensa y Justicia | excluido | 2.85 | 46.3% | 2.16 | +31.84% | +31.84% | +17.59% | 0.04u | Baja |
| 14 | Brentford vs Chelsea | 1 | Victoria Brentford | excluido | 2.90 | 41.0% | 2.44 | +18.84% | +18.84% | +4.34% | 0.02u | Baja |
| 15 | New York City FC vs New York Red Bulls | 2 | Victoria New York Red Bulls | excepcional | 4.30 | 37.8% | 2.65 | +62.54% | +62.54% | +41.04% | 0.05u | Baja |
| 16 | Espanyol vs Elche CF | 2 | Victoria Elche CF | excluido | 5.00 | 28.0% | 3.58 | +39.85% | +39.85% | +14.85% | 0.02u | Baja |
| 17 | New York City FC vs New York Red Bulls | X | Empate | excluido | 4.35 | 24.8% | 4.03 | +7.92% | +7.92% | -13.83% | 0.01u | Baja |
| 18 | Independiente Medellín vs Jaguares | X | Empate | excluido | 4.60 | 24.5% | 4.07 | +12.88% | +12.88% | -10.12% | 0.01u | Baja |
| 19 | Groningen vs FC Zwolle | X | Empate | excluido | 4.60 | 22.7% | 4.42 | +4.19% | +4.19% | -18.81% | 0.00u | Baja |
| 20 | Groningen vs FC Zwolle | 2 | Victoria FC Zwolle | excluido | 5.39 | 21.6% | 4.63 | +16.53% | +16.53% | -10.42% | 0.01u | Baja |
| 21 | Independiente Medellín vs Jaguares | 2 | Victoria Jaguares | excluido | 8.10 | 18.7% | 5.36 | +51.23% | +51.23% | +10.73% | 0.02u | Baja |
| 22 | Bayern Munich vs Union Berlin | under_2_5 | Under 2.5 Goles | excluido | 6.50 | 17.2% | 5.82 | +11.74% | +11.74% | -20.77% | 0.01u | Baja |
| 23 | Bayern Munich vs Union Berlin | X | Empate | excluido | 19.50 | 17.1% | 5.85 | +233.25% | +233.25% | +135.75% | 0.03u | Baja |
| 24 | Bayern Munich vs Union Berlin | 2 | Victoria Union Berlin | excluido | 40.00 | 8.5% | 11.81 | +238.80% | +238.80% | +38.80% | 0.02u | Baja |

## Evaluación Over/Under por Partido
Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada (n/d = cuota no disponible en la corrida).
| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |
|---|---|---|---:|---:|---:|---:|---:|---|
| Brentford vs Chelsea | 1.5 | 83.4% | n/d | n/d | 16.6% | n/d | n/d | Cuotas no capturadas |
| Brentford vs Chelsea | 2.5 | 75.9% | 1.49 | +13.03% | 24.1% | 2.66 | -35.79% | Value Over |
| Brentford vs Chelsea | 3.5 | 59.8% | 2.23 | +33.33% | 40.2% | 1.76 | -29.23% | Value Over |
| Bayern Munich vs Union Berlin | 1.5 | 87.5% | n/d | n/d | 12.5% | n/d | n/d | Cuotas no capturadas |
| Bayern Munich vs Union Berlin | 2.5 | 82.8% | 1.12 | -7.25% | 17.2% | 6.50 | +11.74% | Value Under |
| Bayern Munich vs Union Berlin | 3.5 | 71.2% | n/d | n/d | 28.8% | n/d | n/d | Cuotas no capturadas |
| AS Monaco vs RC Lens | 1.5 | 86.5% | n/d | n/d | 13.5% | n/d | n/d | Cuotas no capturadas |
| AS Monaco vs RC Lens | 2.5 | 81.0% | 1.56 | +26.36% | 19.0% | 2.52 | -52.12% | Value Over |
| AS Monaco vs RC Lens | 3.5 | 68.2% | 2.38 | +62.22% | 31.8% | 1.68 | -46.51% | Value Over |
| Monza vs Sassuolo | 1.5 | 80.8% | n/d | n/d | 19.2% | n/d | n/d | Cuotas no capturadas |
| Monza vs Sassuolo | 2.5 | 71.3% | 1.82 | +29.69% | 28.7% | 2.24 | -35.62% | Value Over |
| Monza vs Sassuolo | 3.5 | 52.7% | n/d | n/d | 47.3% | n/d | n/d | Cuotas no capturadas |
| Espanyol vs Elche CF | 1.5 | 77.6% | n/d | n/d | 22.4% | n/d | n/d | Cuotas no capturadas |
| Espanyol vs Elche CF | 2.5 | 65.8% | 1.90 | +25.02% | 34.2% | 2.05 | -29.89% | Value Over |
| Espanyol vs Elche CF | 3.5 | 44.8% | n/d | n/d | 55.2% | n/d | n/d | Cuotas no capturadas |
| Groningen vs FC Zwolle | 1.5 | 83.5% | n/d | n/d | 16.6% | n/d | n/d | Cuotas no capturadas |
| Groningen vs FC Zwolle | 2.5 | 76.0% | 1.42 | +7.86% | 24.0% | 2.79 | -32.93% | Value Over |
| Groningen vs FC Zwolle | 3.5 | 60.0% | 2.12 | +27.09% | 40.1% | 1.86 | -25.51% | Value Over |
| New York City FC vs New York Red Bulls | 1.5 | 80.5% | n/d | n/d | 19.5% | n/d | n/d | Cuotas no capturadas |
| New York City FC vs New York Red Bulls | 2.5 | 70.7% | 1.47 | +3.99% | 29.3% | 2.62 | -23.34% | Sin value |
| New York City FC vs New York Red Bulls | 3.5 | 51.9% | 2.30 | +19.39% | 48.1% | 1.78 | -14.40% | Value Over |
| Central Córdoba vs Defensa y Justicia | 1.5 | 79.1% | n/d | n/d | 20.8% | n/d | n/d | Cuotas no capturadas |
| Central Córdoba vs Defensa y Justicia | 2.5 | 68.5% | 2.48 | +69.83% | 31.5% | 1.55 | -51.14% | Value Over |
| Central Córdoba vs Defensa y Justicia | 3.5 | 48.6% | n/d | n/d | 51.4% | n/d | n/d | Cuotas no capturadas |
| Independiente Medellín vs Jaguares | 1.5 | 75.1% | n/d | n/d | 24.9% | n/d | n/d | Cuotas no capturadas |
| Independiente Medellín vs Jaguares | 2.5 | 61.6% | n/d | n/d | 38.5% | n/d | n/d | Cuotas no capturadas |
| Independiente Medellín vs Jaguares | 3.5 | 39.2% | n/d | n/d | 60.8% | n/d | n/d | Cuotas no capturadas |

## Picks Recomendados (Top 4)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | AS Monaco vs RC Lens | over_2_5 | Over 2.5 Goles | prioritario | 1.56 | 81.0% | 1.23 | +26.36% | +26.36% | +18.56% | 0.12u | Media-Alta |
| 2 | Monza vs Sassuolo | over_2_5 | Over 2.5 Goles | prioritario | 1.82 | 71.3% | 1.40 | +29.69% | +29.69% | +20.59% | 0.09u | Media-Alta |
| 3 | Espanyol vs Elche CF | over_2_5 | Over 2.5 Goles | prioritario | 1.90 | 65.8% | 1.52 | +25.02% | +25.02% | +15.52% | 0.07u | Media-Alta |
| 4 | AS Monaco vs RC Lens | 2 | Victoria RC Lens | excepcional | 3.65 | 46.4% | 2.16 | +69.36% | +69.36% | +51.11% | 0.07u | Baja |

## Detalle de Picks
### Pick 1: AS Monaco vs RC Lens
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.56
- **Probabilidad modelo:** 81.0%
- **Probabilidad conservadora:** 76.0%
- **Probabilidad implícita:** 64.1%
- **Cuota justa:** 1.23
- **Edge:** +26.36%
- **EV:** +26.36%
- **EV robusto:** +18.56%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.32
- **Stake:** 0.12u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/-5.0% del motor. Datos xG completos (Ligue 1). Backtest de sensibilidad: +14.8% a +19.9% rEV (escenarios s1/s2).
- **Por qué:** Lens es el 2º mejor ataque de la liga en xG generado y el peor perfil defensivo acumulado (2.08 xGA); Monaco viene de 3 victorias seguidas y ambos equipos generan contexto de goles. Probabilidad modelo 81% vs 64.1% implícita.
- **Riesgos:** Monaco con cambio de DT; Lens con interino tras cese. Si Lens cae en intensidad con nueva gestión puede bajar el ritmo. Varianza de goles en partido único.
- **Fuentes:** The Odds API (best price across books, timestamp 18-09 01:48Z); Understat xG 2026-27; ClubElo 2026-09.

### Pick 2: Monza vs Sassuolo
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.82
- **Probabilidad modelo:** 71.3%
- **Probabilidad conservadora:** 66.3%
- **Probabilidad implícita:** 54.9%
- **Cuota justa:** 1.40
- **Edge:** +29.69%
- **EV:** +29.69%
- **EV robusto:** +20.59%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.51
- **Stake:** 0.09u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/-5.0% + incertidumbre por xG estimado de Sassuolo (5%).
- **Por qué:** Monza anota y encaja (6 GF / 11 GA en 4 partidos, última derrota 3-2) y Sassuolo suma 11 goles en 4 con una victoria 3-2 ante Juventus. xG estimados por encima de promedio de la liga en ambos. Prob 71.3% vs 55.0% implícita.
- **Riesgos:** xG de Sassuolo estimado (falta serie completa); si el partido se controla en medio campo puede caer en pocos goles. Monza sin victoria local este curso.
- **Fuentes:** The Odds API totals (best 1.82, timestamp 18-09 01:48Z); Understat xG parcial; resultados recientes 2026-27.

### Pick 3: Espanyol vs Elche CF
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.90
- **Probabilidad modelo:** 65.8%
- **Probabilidad conservadora:** 60.8%
- **Probabilidad implícita:** 52.6%
- **Cuota justa:** 1.52
- **Edge:** +25.02%
- **EV:** +25.02%
- **EV robusto:** +15.52%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.64
- **Stake:** 0.07u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/-5.0% + incertidumbre por xG estimado (5%). Sensibilidad: rEV +15.5% a +18.2% (s3/s4).
- **Por qué:** Elche tiene el peor registro defensivo de La Liga (16 goles encajados en 4 partidos) y Espanyol genera volumen ofensivo en casa pese a xG modesto. Prob 65.8% vs 52.6% implícita. La cuota 1.90 está bien pagada para la probabilidad.
- **Riesgos:** Espanyol con ataque inconstante (xG estimado bajo); si Elche plantea bloque bajo, el juego puede ser de pocas ocasiones. Partido 1-0 posible.
- **Fuentes:** The Odds API totals (best 1.90, timestamp 18-09 01:48Z); Understat xG parcial; resultados La Liga.

### Pick 4: AS Monaco vs RC Lens
- **Mercado:** 2
- **Selección:** Victoria RC Lens
- **Cuota:** 3.65
- **Probabilidad modelo:** 46.4%
- **Probabilidad conservadora:** 41.4%
- **Probabilidad implícita:** 27.4%
- **Cuota justa:** 2.16
- **Edge:** +69.36%
- **EV:** +69.36%
- **EV robusto:** +51.11%
- **Perfil de selección:** excepcional
- **Cuota mínima:** 2.42
- **Stake:** 0.07u
- **Confianza:** Media
- **Incertidumbre:** Base +/-5.0%. Premium por cambio de entrenador interino en Lens y rotaciones post-parón FIFA. Sensibilidad: rEV +26.0% (s1) a +42.2% (s2).
- **Por qué:** El conjunto Elo favorece claramente a Lens (1.798 vs 1.749) y en xG Lens domina el cómputo (2.23 xGF prom). El mercado paga 3.65 (27.4% implícito) por una probabilidad modelo 46.4%. Longshot admitido como excepción robusta (prob >30%, rEV +51.1% > +10%).
- **Riesgos:** Monaco está 2º con 10 puntos y juega en casa; Lens con interino (Cahuzac). Un Lens mas conservador reduce su xG real. Stops de largo recorrido.
- **Fuentes:** The Odds API h2h (best 3.65, timestamp 18-09 01:48Z); ClubElo; Understat xG.

## NO BET / Excluidos
- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**
  - Brentford vs Chelsea — Under 2.5 Goles (under_2_5): Prob modelo 24.1%, EV -35.79%, EV robusto -49.09% → sin value.
  - Brentford vs Chelsea — Under 3.5 Goles (under_3_5): Prob modelo 40.2%, EV -29.23%, EV robusto -38.03% → sin value.
  - Bayern Munich vs Union Berlin — Over 2.5 Goles (over_2_5): Prob modelo 82.8%, EV -7.25%, EV robusto -12.85% → sin value.
  - AS Monaco vs RC Lens — Under 2.5 Goles (under_2_5): Prob modelo 19.0%, EV -52.12%, EV robusto -64.72% → sin value.
  - AS Monaco vs RC Lens — Under 3.5 Goles (under_3_5): Prob modelo 31.8%, EV -46.51%, EV robusto -54.91% → sin value.
  - Monza vs Sassuolo — Under 2.5 Goles (under_2_5): Prob modelo 28.7%, EV -35.62%, EV robusto -46.82% → sin value.
  - Espanyol vs Elche CF — Under 2.5 Goles (under_2_5): Prob modelo 34.2%, EV -29.89%, EV robusto -40.14% → sin value.
  - Groningen vs FC Zwolle — Under 2.5 Goles (under_2_5): Prob modelo 24.0%, EV -32.93%, EV robusto -46.88% → sin value.
  - Groningen vs FC Zwolle — Under 3.5 Goles (under_3_5): Prob modelo 40.1%, EV -25.51%, EV robusto -34.81% → sin value.
  - New York City FC vs New York Red Bulls — Over 2.5 Goles (over_2_5): Prob modelo 70.7%, EV +3.99%, EV robusto -3.36% → sin value.
  - New York City FC vs New York Red Bulls — Under 2.5 Goles (under_2_5): Prob modelo 29.3%, EV -23.34%, EV robusto -36.44% → sin value.
  - New York City FC vs New York Red Bulls — Under 3.5 Goles (under_3_5): Prob modelo 48.1%, EV -14.40%, EV robusto -23.30% → sin value.
  - Central Córdoba vs Defensa y Justicia — Under 2.5 Goles (under_2_5): Prob modelo 31.5%, EV -51.14%, EV robusto -58.89% → sin value.
- **Candidatos con value excluidos por probabilidad-primero:**
  - Brentford vs Chelsea: Victoria Brentford (1) EV +18.84% / EV rob +4.34%, Over 2.5 Goles (over_2_5) EV +13.03% / EV rob +5.58%, Over 3.5 Goles (over_3_5) EV +33.33% / EV rob +22.18% — No cumple los mínimos de selección probabilidad-primero.
  - Bayern Munich vs Union Berlin: Empate (X) EV +233.25% / EV rob +135.75%, Victoria Union Berlin (2) EV +238.80% / EV rob +38.80%, Under 2.5 Goles (under_2_5) EV +11.74% / EV rob -20.77% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - AS Monaco vs RC Lens: Over 3.5 Goles (over_3_5) EV +62.22% / EV rob +50.32% — No cumple los mínimos de selección probabilidad-primero.
  - Monza vs Sassuolo: Victoria Sassuolo (2) EV +21.34% / EV rob +8.54% — No cumple los mínimos de selección probabilidad-primero.
  - Espanyol vs Elche CF: Victoria Elche CF (2) EV +39.85% / EV rob +14.85% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Groningen vs FC Zwolle: Empate (X) EV +4.19% / EV rob -18.81%, Victoria FC Zwolle (2) EV +16.53% / EV rob -10.42%, Over 2.5 Goles (over_2_5) EV +7.86% / EV rob +0.76%, Over 3.5 Goles (over_3_5) EV +27.09% / EV rob +16.49% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto. Over 3.5 (EV rob +16.49%) quedó además **invalidado por el análisis de sensibilidad s6** (reduciendo xG del Groningen a 1.35 la prob cae a 49.8% y el EV robusto a -5.0%): no se incluye en el portfolio pese a cumplir la banda.
  - New York City FC vs New York Red Bulls: Empate (X) EV +7.92% / EV rob -13.83%, Over 3.5 Goles (over_3_5) EV +19.39% / EV rob +7.89%, Victoria New York Red Bulls (2) EV +62.54% / EV rob +41.04% — Victoria NY Red Bulls (2) era candidata excepción longshot (prob 37.8%, rEV +41%) pero **no superó la sensibilidad s8/s9**: con xG de RBNY 1.2-1.4 la prob cae a 23-30% y el rEV a +5.2%/-21.2% → descartada en favor de la única excepción (Lens).
  - Central Córdoba vs Defensa y Justicia: Victoria Defensa y Justicia (2) EV +31.84% / EV rob +17.59%, Over 2.5 Goles (over_2_5) EV +69.83% / EV rob +57.43% — No cumple los mínimos de selección probabilidad-primero.
  - Independiente Medellín vs Jaguares: Empate (X) EV +12.88% / EV rob -10.12%, Victoria Jaguares (2) EV +51.23% / EV rob +10.73% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.

## Portfolio y Correlaciones
- **Exposición total:** 0.35u
- **Correlaciones detectadas:** Mercados presentes: 2, over_2_5. **AS Monaco vs RC Lens tiene 2 picks correlacionados** (Over 2.5 según la 1X2): ambos favorecen un partido abierto con ventaja de Lens; combinación 0.12u + 0.07u = 0.19u sobre un único resultado. Se mantienen porque fueron seleccionados por el pipeline determinista (motor + selector) y son los de mayor EV robusto de la jornada; la exposición conjunta queda documentada y dentro del cap de 0.25u del longshot.
- **Ajuste de stake por correlación:** No se aplica reducción adicional más allá del stake Kelly que ya pondera la varianza; la pareja Monaco queda marcada para revisión en /football-review. El resto de picks pertenecen a partidos distintos (sin solapamiento directo por equipo).

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1 (AS Monaco vs RC Lens - over_2_5) | PENDIENTE | — | — |
| Pick 2 (Monza vs Sassuolo - over_2_5) | PENDIENTE | — | — |
| Pick 3 (Espanyol vs Elche CF - over_2_5) | PENDIENTE | — | — |
| Pick 4 (AS Monaco vs RC Lens - 2) | PENDIENTE | — | — |
