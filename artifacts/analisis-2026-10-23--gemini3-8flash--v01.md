# Análisis de Apuestas — 23 de octubre de 2026

## Metadatos
- **Fecha de análisis:** 2026-10-23T09:00:00Z
- **Fecha(s) de partido:** 23 de octubre de 2026
- **Information cutoff:** 2026-10-23T08:55:00Z
- **Modelo de IA:** gemini3.8flash
- **Versión del motor predictivo:** model-v1.4
- **Ligas analizadas:** Bundesliga, Liga Profesional Argentina, Liga BetPlay Dimayor, LaLiga, Ligue 1, Premier League, Serie A, Eredivisie, Liga Portugal
- **Rango de fechas solicitado:** 2026-10-23 (todos los partidos de las 9 ligas solicitadas)
- **Partidos en universo:** 12
- **Picks iniciales con value:** 41
- **Picks finales seleccionados:** 6

## Universo Analizado
Universo = 12 partidos programados para el viernes 23 de octubre de 2026 en las 9 ligas solicitadas (Bundesliga: 1, Premier League: 1, LaLiga: 1, Serie A: 1, Ligue 1: 1, Eredivisie: 1, Liga Portugal: 1, Liga Profesional Argentina: 3, Liga BetPlay Dimayor: 2). Recolección de cuotas Capa 1 y Capa 2 (1X2, totales de goles O/U 1.5, 2.5, 3.5, BTTS, DNB, córners y tarjetas). Se garantizaron los 8 campos obligatorios de córners y tarjetas (tasas for/against para ambos equipos basadas en los últimos 5-10 partidos). Evaluación cuantitativa determinista con scripts/calc_engine.py y calibración Platt de model-v1.4.
- **Bundesliga (1 partido):** VfB Stuttgart vs. Borussia Mönchengladbach (MHP Arena, Stuttgart)
- **Premier League (1 partido):** Ipswich Town vs. Nottingham Forest (Portman Road, Ipswich)
- **LaLiga (1 partido):** Deportivo Alavés vs. Málaga (Estadio de Mendizorroza, Vitoria-Gasteiz)
- **Serie A (1 partido):** Torino vs. Monza (Stadio Olimpico Grande Torino, Turín)
- **Ligue 1 (1 partido):** Brest vs. Nice (Stade Francis-Le Blé, Brest)
- **Eredivisie (1 partido):** Go Ahead Eagles vs. Telstar (De Adelaarshorst, Deventer)
- **Liga Portugal (1 partido):** Vitória Guimarães vs. Marítimo (Estádio D. Afonso Henriques, Guimarães)
- **Liga Argentina (3 partidos):** Gimnasia La Plata vs. Sarmiento de Junín, Gimnasia de Mendoza vs. Platense, Tigre vs. Atlético Tucumán
- **Liga Colombiana (2 partidos):** Boyacá Chicó vs. Atlético Bucaramanga (La Independencia, Tunja), Junior vs. Águilas Doradas (Estadio Romelio Martínez / Metropolitano, Barranquilla)

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Boyacá Chicó vs Atlético Bucaramanga | x2 | Doble Oportunidad Empate/Atlético Bucaramanga | excluido | 1.28 | 83.8% | 1.19 | +7.26% | +7.26% | +0.86% | 0.06u | Media-Alta |
| 2 | VfB Stuttgart vs Borussia Mönchengladbach | over_2_5 | Over 2.5 Goles | prioritario | 1.50 | 75.9% | 1.32 | +13.92% | +13.92% | +6.42% | 0.07u | Media-Alta |
| 3 | Go Ahead Eagles vs Telstar | over_2_5 | Over 2.5 Goles | prioritario | 1.68 | 71.2% | 1.40 | +19.68% | +19.68% | +11.28% | 0.07u | Media-Alta |
| 4 | Ipswich Town vs Nottingham Forest | over_2_5 | Over 2.5 Goles | prioritario | 1.88 | 70.0% | 1.43 | +31.52% | +31.52% | +22.12% | 0.09u | Media-Alta |
| 5 | Brest vs Nice | over_2_5 | Over 2.5 Goles | prioritario | 1.92 | 66.5% | 1.50 | +27.74% | +27.74% | +18.14% | 0.08u | Media-Alta |
| 6 | Torino vs Monza | over_2_5 | Over 2.5 Goles | prioritario | 1.98 | 65.1% | 1.54 | +28.84% | +28.84% | +18.94% | 0.07u | Media-Alta |
| 7 | Gimnasia de Mendoza vs Platense | under_corners_9_5 | Under 9.5 Córners | excluido | 1.68 | 62.6% | 1.60 | +5.15% | +5.15% | -3.25% | 0.02u | Media-Alta |
| 8 | Deportivo Alavés vs Málaga | over_2_5 | Over 2.5 Goles | prioritario | 2.05 | 62.5% | 1.60 | +28.08% | +28.08% | +17.83% | 0.07u | Media-Alta |
| 9 | Tigre vs Atlético Tucumán | under_corners_9_5 | Under 9.5 Córners | excluido | 1.75 | 62.1% | 1.61 | +8.65% | +8.65% | -0.10% | 0.03u | Media-Alta |
| 10 | Gimnasia La Plata vs Sarmiento de Junín | under_corners_9_5 | Under 9.5 Córners | excluido | 1.72 | 62.1% | 1.61 | +6.79% | +6.79% | -1.81% | 0.02u | Media-Alta |
| 11 | Junior vs Águilas Doradas | under_corners_9_5 | Under 9.5 Córners | excluido | 1.82 | 58.1% | 1.72 | +5.74% | +5.74% | -3.36% | 0.02u | Media-Alta |
| 12 | Boyacá Chicó vs Atlético Bucaramanga | 2 | Victoria Atlético Bucaramanga | prioritario | 2.02 | 57.3% | 1.74 | +15.77% | +15.77% | +5.67% | 0.04u | Media |
| 13 | Boyacá Chicó vs Atlético Bucaramanga | dnb_away | DNB Atlético Bucaramanga | excluido | 1.50 | 57.3% | 1.28 | +12.46% | +12.46% | +4.97% | 0.06u | Media |
| 14 | Vitória Guimarães vs Marítimo | over_cards_4_5 | Over 4.5 Tarjetas | excluido | 1.85 | 57.0% | 1.75 | +5.52% | +5.52% | -3.73% | 0.02u | Media |
| 15 | Vitória Guimarães vs Marítimo | over_2_5 | Over 2.5 Goles | excluido | 2.05 | 53.1% | 1.88 | +8.88% | +8.88% | -1.37% | 0.02u | Media |
| 16 | Gimnasia de Mendoza vs Platense | under_corners_8_5 | Under 8.5 Córners | excluido | 2.15 | 52.7% | 1.90 | +13.30% | +13.30% | +2.55% | 0.03u | Media |
| 17 | Tigre vs Atlético Tucumán | under_corners_8_5 | Under 8.5 Córners | excluido | 2.25 | 52.2% | 1.92 | +17.41% | +17.41% | +6.16% | 0.03u | Media |
| 18 | Gimnasia La Plata vs Sarmiento de Junín | under_corners_8_5 | Under 8.5 Córners | excluido | 2.20 | 52.2% | 1.92 | +14.80% | +14.80% | +3.80% | 0.03u | Media |
| 19 | Boyacá Chicó vs Atlético Bucaramanga | over_2_5 | Over 2.5 Goles | excluido | 2.35 | 51.8% | 1.93 | +21.82% | +21.82% | +10.07% | 0.04u | Media |
| 20 | Tigre vs Atlético Tucumán | over_2_5 | Over 2.5 Goles | excluido | 2.25 | 50.9% | 1.96 | +14.59% | +14.59% | +3.34% | 0.03u | Media |
| 21 | Junior vs Águilas Doradas | over_2_5 | Over 2.5 Goles | excluido | 2.15 | 50.9% | 1.96 | +9.50% | +9.50% | -1.25% | 0.02u | Media |
| 22 | Deportivo Alavés vs Málaga | under_corners_8_5 | Under 8.5 Córners | excluido | 2.20 | 49.6% | 2.01 | +9.24% | +9.24% | -1.76% | 0.02u | Baja |
| 23 | Boyacá Chicó vs Atlético Bucaramanga | under_corners_8_5 | Under 8.5 Córners | excluido | 2.20 | 49.2% | 2.03 | +8.14% | +8.14% | -2.86% | 0.02u | Baja |
| 24 | Junior vs Águilas Doradas | under_corners_8_5 | Under 8.5 Córners | excluido | 2.35 | 48.2% | 2.08 | +13.20% | +13.20% | +1.45% | 0.02u | Baja |
| 25 | Ipswich Town vs Nottingham Forest | 2 | Victoria Nottingham Forest | excluido | 2.23 | 47.2% | 2.12 | +5.35% | +5.35% | -5.80% | 0.01u | Baja |
| 26 | Gimnasia de Mendoza vs Platense | over_2_5 | Over 2.5 Goles | excluido | 2.45 | 46.9% | 2.13 | +14.78% | +14.78% | +2.53% | 0.03u | Baja |
| 27 | Vitória Guimarães vs Marítimo | under_corners_8_5 | Under 8.5 Córners | excluido | 2.40 | 46.7% | 2.14 | +12.10% | +12.10% | +0.10% | 0.02u | Baja |
| 28 | Gimnasia La Plata vs Sarmiento de Junín | over_cards_5_5 | Over 5.5 Tarjetas | excluido | 2.40 | 46.4% | 2.16 | +11.25% | +11.25% | -0.75% | 0.02u | Baja |
| 29 | Gimnasia de Mendoza vs Platense | over_cards_5_5 | Over 5.5 Tarjetas | excluido | 2.35 | 46.4% | 2.16 | +8.94% | +8.94% | -2.81% | 0.02u | Baja |
| 30 | Torino vs Monza | under_corners_8_5 | Under 8.5 Córners | excluido | 2.30 | 46.2% | 2.16 | +6.33% | +6.33% | -5.17% | 0.01u | Baja |
| 31 | Brest vs Nice | under_corners_8_5 | Under 8.5 Córners | excluido | 2.40 | 44.8% | 2.23 | +7.53% | +7.53% | -4.47% | 0.01u | Baja |
| 32 | Boyacá Chicó vs Atlético Bucaramanga | over_cards_5_5 | Over 5.5 Tarjetas | excluido | 2.40 | 44.5% | 2.25 | +6.75% | +6.75% | -5.25% | 0.01u | Baja |
| 33 | Vitória Guimarães vs Marítimo | over_cards_5_5 | Over 5.5 Tarjetas | excluido | 2.55 | 43.9% | 2.28 | +11.81% | +11.81% | -0.94% | 0.02u | Baja |
| 34 | Deportivo Alavés vs Málaga | over_cards_5_5 | Over 5.5 Tarjetas | excluido | 2.50 | 43.9% | 2.28 | +9.62% | +9.62% | -2.88% | 0.02u | Baja |
| 35 | Tigre vs Atlético Tucumán | over_cards_5_5 | Over 5.5 Tarjetas | excluido | 2.45 | 43.9% | 2.28 | +7.42% | +7.42% | -4.83% | 0.01u | Baja |
| 36 | Junior vs Águilas Doradas | over_cards_5_5 | Over 5.5 Tarjetas | excluido | 2.48 | 43.2% | 2.31 | +7.16% | +7.16% | -5.24% | 0.01u | Baja |
| 37 | Brest vs Nice | 2 | Victoria Nice | excluido | 2.95 | 35.2% | 2.84 | +3.81% | +3.81% | -10.94% | 0.00u | Baja |
| 38 | Ipswich Town vs Nottingham Forest | over_3_5 | Over 3.5 Goles | excluido | 3.10 | 34.2% | 2.93 | +5.87% | +5.87% | -9.63% | 0.01u | Baja |
| 39 | Torino vs Monza | over_3_5 | Over 3.5 Goles | excluido | 3.45 | 30.2% | 3.31 | +4.33% | +4.33% | -12.92% | 0.00u | Baja |
| 40 | Vitória Guimarães vs Marítimo | under_1_5 | Under 1.5 Goles | excluido | 3.50 | 29.9% | 3.34 | +4.82% | +4.82% | -12.68% | 0.00u | Baja |
| 41 | Gimnasia La Plata vs Sarmiento de Junín | X | Empate | excluido | 3.80 | 27.2% | 3.68 | +3.28% | +3.28% | -15.72% | 0.00u | Baja |

## Evaluación Over/Under por Partido
Ambos lados del mercado de goles (over y under) para las líneas 1.5, 2.5 y 3.5. Prob. = probabilidad del modelo; Cuota/EV = solo si la cuota fue capturada (n/d = cuota no disponible en la corrida).
| Partido | Línea | Prob Over | Cuota Over | EV Over | Prob Under | Cuota Under | EV Under | Veredicto |
|---|---|---|---:|---:|---:|---:|---:|---|
| VfB Stuttgart vs Borussia Mönchengladbach | 1.5 | 83.4% | 1.15 | -4.07% | 16.6% | 5.50 | -8.81% | Sin value |
| VfB Stuttgart vs Borussia Mönchengladbach | 2.5 | 75.9% | 1.50 | +13.92% | 24.1% | 2.60 | -37.47% | Value Over |
| VfB Stuttgart vs Borussia Mönchengladbach | 3.5 | 39.7% | 2.25 | -10.63% | 60.3% | 1.65 | -0.54% | Sin value |
| Ipswich Town vs Nottingham Forest | 1.5 | 80.0% | 1.28 | +2.41% | 20.0% | 3.75 | -25.04% | Sin value |
| Ipswich Town vs Nottingham Forest | 2.5 | 70.0% | 1.88 | +31.52% | 30.0% | 1.95 | -41.42% | Value Over |
| Ipswich Town vs Nottingham Forest | 3.5 | 34.2% | 3.10 | +5.87% | 65.8% | 1.38 | -9.13% | Value Over |
| Deportivo Alavés vs Málaga | 1.5 | 75.6% | 1.35 | +2.07% | 24.4% | 3.25 | -20.73% | Sin value |
| Deportivo Alavés vs Málaga | 2.5 | 62.5% | 2.05 | +28.08% | 37.5% | 1.78 | -33.21% | Value Over |
| Deportivo Alavés vs Málaga | 3.5 | 28.4% | 3.60 | +2.10% | 71.6% | 1.30 | -6.87% | Sin value |
| Torino vs Monza | 1.5 | 77.1% | 1.32 | +1.82% | 22.9% | 3.40 | -22.28% | Sin value |
| Torino vs Monza | 2.5 | 65.1% | 1.98 | +28.84% | 34.9% | 1.85 | -35.38% | Value Over |
| Torino vs Monza | 3.5 | 30.2% | 3.45 | +4.33% | 69.8% | 1.32 | -7.92% | Value Over |
| Brest vs Nice | 1.5 | 78.0% | 1.30 | +1.41% | 22.0% | 3.55 | -21.94% | Sin value |
| Brest vs Nice | 2.5 | 66.5% | 1.92 | +27.74% | 33.5% | 1.90 | -36.41% | Value Over |
| Brest vs Nice | 3.5 | 31.4% | 3.30 | +3.49% | 68.6% | 1.34 | -8.02% | Sin value |
| Go Ahead Eagles vs Telstar | 1.5 | 80.7% | 1.20 | -3.17% | 19.3% | 4.60 | -11.17% | Sin value |
| Go Ahead Eagles vs Telstar | 2.5 | 71.2% | 1.68 | +19.68% | 28.8% | 2.20 | -36.73% | Value Over |
| Go Ahead Eagles vs Telstar | 3.5 | 35.3% | 2.70 | -4.80% | 64.7% | 1.48 | -4.18% | Sin value |
| Vitória Guimarães vs Marítimo | 1.5 | 70.0% | 1.30 | -8.93% | 29.9% | 3.50 | +4.82% | Value Under |
| Vitória Guimarães vs Marítimo | 2.5 | 53.1% | 2.05 | +8.88% | 46.9% | 1.75 | -17.94% | Value Over |
| Vitória Guimarães vs Marítimo | 3.5 | 22.3% | 3.65 | -18.50% | 77.7% | 1.28 | -0.58% | Sin value |
| Gimnasia La Plata vs Sarmiento de Junín | 1.5 | 65.0% | 1.42 | -7.71% | 35.0% | 2.85 | -0.22% | Sin value |
| Gimnasia La Plata vs Sarmiento de Junín | 2.5 | 44.9% | 2.30 | +3.36% | 55.1% | 1.62 | -10.80% | Sin value |
| Gimnasia La Plata vs Sarmiento de Junín | 3.5 | 17.9% | 4.30 | -23.16% | 82.1% | 1.22 | +0.20% | Sin value |
| Gimnasia de Mendoza vs Platense | 1.5 | 66.3% | 1.48 | -1.91% | 33.7% | 2.60 | -12.33% | Sin value |
| Gimnasia de Mendoza vs Platense | 2.5 | 46.9% | 2.45 | +14.78% | 53.1% | 1.55 | -17.62% | Value Over |
| Gimnasia de Mendoza vs Platense | 3.5 | 18.9% | 4.80 | -9.47% | 81.1% | 1.18 | -4.25% | Sin value |
| Tigre vs Atlético Tucumán | 1.5 | 68.8% | 1.40 | -3.75% | 31.2% | 2.90 | -9.38% | Sin value |
| Tigre vs Atlético Tucumán | 2.5 | 50.9% | 2.25 | +14.59% | 49.1% | 1.65 | -19.03% | Value Over |
| Tigre vs Atlético Tucumán | 3.5 | 21.1% | 4.20 | -11.42% | 78.9% | 1.23 | -2.94% | Sin value |
| Boyacá Chicó vs Atlético Bucaramanga | 1.5 | 69.4% | 1.45 | +0.60% | 30.6% | 2.70 | -17.33% | Sin value |
| Boyacá Chicó vs Atlético Bucaramanga | 2.5 | 51.8% | 2.35 | +21.82% | 48.2% | 1.60 | -22.94% | Value Over |
| Boyacá Chicó vs Atlético Bucaramanga | 3.5 | 21.6% | 4.50 | -2.76% | 78.4% | 1.20 | -5.93% | Sin value |
| Junior vs Águilas Doradas | 1.5 | 68.8% | 1.38 | -5.11% | 31.2% | 3.05 | -4.72% | Sin value |
| Junior vs Águilas Doradas | 2.5 | 50.9% | 2.15 | +9.50% | 49.1% | 1.70 | -16.58% | Value Over |
| Junior vs Águilas Doradas | 3.5 | 21.1% | 3.90 | -17.75% | 78.9% | 1.26 | -0.57% | Sin value |

## Picks Recomendados (Top 6)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | VfB Stuttgart vs Borussia Mönchengladbach | over_2_5 | Over 2.5 Goles | prioritario | 1.50 | 75.9% | 1.32 | +13.92% | +13.92% | +6.42% | 0.07u | Media-Alta |
| 2 | Go Ahead Eagles vs Telstar | over_2_5 | Over 2.5 Goles | prioritario | 1.68 | 71.2% | 1.40 | +19.68% | +19.68% | +11.28% | 0.07u | Media-Alta |
| 3 | Ipswich Town vs Nottingham Forest | over_2_5 | Over 2.5 Goles | prioritario | 1.88 | 70.0% | 1.43 | +31.52% | +31.52% | +22.12% | 0.09u | Media-Alta |
| 4 | Brest vs Nice | over_2_5 | Over 2.5 Goles | prioritario | 1.92 | 66.5% | 1.50 | +27.74% | +27.74% | +18.14% | 0.08u | Media-Alta |
| 5 | Torino vs Monza | over_2_5 | Over 2.5 Goles | prioritario | 1.98 | 65.1% | 1.54 | +28.84% | +28.84% | +18.94% | 0.07u | Media-Alta |
| 6 | Deportivo Alavés vs Málaga | over_2_5 | Over 2.5 Goles | prioritario | 2.05 | 62.5% | 1.60 | +28.08% | +28.08% | +17.83% | 0.07u | Media-Alta |

## Detalle de Picks
### Pick 1: VfB Stuttgart vs Borussia Mönchengladbach
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.50
- **Probabilidad modelo:** 75.9%
- **Probabilidad conservadora:** 71.0%
- **Probabilidad implícita:** 66.7%
- **Cuota justa:** 1.32
- **Edge:** +13.92%
- **EV:** +13.92%
- **EV robusto:** +6.42%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.41
- **Stake:** 0.07u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 2: Go Ahead Eagles vs Telstar
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.68
- **Probabilidad modelo:** 71.2%
- **Probabilidad conservadora:** 66.2%
- **Probabilidad implícita:** 59.5%
- **Cuota justa:** 1.40
- **Edge:** +19.68%
- **EV:** +19.68%
- **EV robusto:** +11.28%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.51
- **Stake:** 0.07u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 3: Ipswich Town vs Nottingham Forest
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.88
- **Probabilidad modelo:** 70.0%
- **Probabilidad conservadora:** 65.0%
- **Probabilidad implícita:** 53.2%
- **Cuota justa:** 1.43
- **Edge:** +31.52%
- **EV:** +31.52%
- **EV robusto:** +22.12%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.54
- **Stake:** 0.09u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 4: Brest vs Nice
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.92
- **Probabilidad modelo:** 66.5%
- **Probabilidad conservadora:** 61.5%
- **Probabilidad implícita:** 52.1%
- **Cuota justa:** 1.50
- **Edge:** +27.74%
- **EV:** +27.74%
- **EV robusto:** +18.14%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.63
- **Stake:** 0.08u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 5: Torino vs Monza
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 1.98
- **Probabilidad modelo:** 65.1%
- **Probabilidad conservadora:** 60.1%
- **Probabilidad implícita:** 50.5%
- **Cuota justa:** 1.54
- **Edge:** +28.84%
- **EV:** +28.84%
- **EV robusto:** +18.94%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.66
- **Stake:** 0.07u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

### Pick 6: Deportivo Alavés vs Málaga
- **Mercado:** over_2_5
- **Selección:** Over 2.5 Goles
- **Cuota:** 2.05
- **Probabilidad modelo:** 62.5%
- **Probabilidad conservadora:** 57.5%
- **Probabilidad implícita:** 48.8%
- **Cuota justa:** 1.60
- **Edge:** +28.08%
- **EV:** +28.08%
- **EV robusto:** +17.83%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.74
- **Stake:** 0.07u
- **Confianza:** Media-Alta
- **Incertidumbre:** Base +/- 5.0%
- **Por qué:** Selección con value según el motor (probabilidad modelo y EV robusto por encima de umbrales).
- **Riesgos:** Impacto de la varianza intrínseca del fútbol y de la diferencia de cuota real capturada.
- **Fuentes:** Motor predictivo model-v1.2, odds cutoff del artefacto

## NO BET / Excluidos
- **Lado opuesto del mercado O/U evaluado explícitamente (sin value):**
  - VfB Stuttgart vs Borussia Mönchengladbach — Over 1.5 Goles (over_1_5): Prob modelo 83.4%, EV -4.07%, EV robusto -9.82% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Under 1.5 Goles (under_1_5): Prob modelo 16.6%, EV -8.81%, EV robusto -36.31% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Under 2.5 Goles (under_2_5): Prob modelo 24.1%, EV -37.47%, EV robusto -50.47% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Over 3.5 Goles (over_3_5): Prob modelo 39.7%, EV -10.63%, EV robusto -21.88% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Under 3.5 Goles (under_3_5): Prob modelo 60.3%, EV -0.54%, EV robusto -8.79% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Over 8.5 Córners (over_corners_8_5): Prob modelo 63.5%, EV -7.87%, EV robusto -15.12% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Under 8.5 Córners (under_corners_8_5): Prob modelo 36.5%, EV -3.37%, EV robusto -16.62% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Over 9.5 Córners (over_corners_9_5): Prob modelo 54.1%, EV -5.28%, EV robusto -14.03% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Under 9.5 Córners (under_corners_9_5): Prob modelo 45.9%, EV -5.96%, EV robusto -16.21% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Over 10.5 Córners (over_corners_10_5): Prob modelo 45.0%, EV -1.10%, EV robusto -12.10% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Under 10.5 Córners (under_corners_10_5): Prob modelo 55.0%, EV -9.18%, EV robusto -17.43% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 58.2%, EV -9.80%, EV robusto -17.55% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 41.8%, EV -1.75%, EV robusto -13.50% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 42.9%, EV -12.15%, EV robusto -22.40% → sin value.
  - VfB Stuttgart vs Borussia Mönchengladbach — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 57.1%, EV +0.00%, EV robusto -8.75% → sin value.
  - Ipswich Town vs Nottingham Forest — Over 1.5 Goles (over_1_5): Prob modelo 80.0%, EV +2.41%, EV robusto -3.99% → sin value.
  - Ipswich Town vs Nottingham Forest — Under 1.5 Goles (under_1_5): Prob modelo 20.0%, EV -25.04%, EV robusto -43.79% → sin value.
  - Ipswich Town vs Nottingham Forest — Under 2.5 Goles (under_2_5): Prob modelo 30.0%, EV -41.42%, EV robusto -51.17% → sin value.
  - Ipswich Town vs Nottingham Forest — Under 3.5 Goles (under_3_5): Prob modelo 65.8%, EV -9.13%, EV robusto -16.03% → sin value.
  - Ipswich Town vs Nottingham Forest — Over 8.5 Córners (over_corners_8_5): Prob modelo 62.3%, EV -6.55%, EV robusto -14.05% → sin value.
  - Ipswich Town vs Nottingham Forest — Under 8.5 Córners (under_corners_8_5): Prob modelo 37.7%, EV -5.75%, EV robusto -18.25% → sin value.
  - Ipswich Town vs Nottingham Forest — Over 9.5 Córners (over_corners_9_5): Prob modelo 52.8%, EV -2.33%, EV robusto -11.58% → sin value.
  - Ipswich Town vs Nottingham Forest — Under 9.5 Córners (under_corners_9_5): Prob modelo 47.2%, EV -7.95%, EV robusto -17.70% → sin value.
  - Ipswich Town vs Nottingham Forest — Over 10.5 Córners (over_corners_10_5): Prob modelo 43.6%, EV +2.46%, EV robusto -9.29% → sin value.
  - Ipswich Town vs Nottingham Forest — Under 10.5 Córners (under_corners_10_5): Prob modelo 56.4%, EV -9.76%, EV robusto -17.76% → sin value.
  - Ipswich Town vs Nottingham Forest — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 58.2%, EV -6.89%, EV robusto -14.89% → sin value.
  - Ipswich Town vs Nottingham Forest — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 41.8%, EV -5.94%, EV robusto -17.19% → sin value.
  - Ipswich Town vs Nottingham Forest — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 42.9%, EV -7.86%, EV robusto -18.61% → sin value.
  - Ipswich Town vs Nottingham Forest — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 57.1%, EV -4.00%, EV robusto -12.40% → sin value.
  - Deportivo Alavés vs Málaga — Over 1.5 Goles (over_1_5): Prob modelo 75.6%, EV +2.07%, EV robusto -4.68% → sin value.
  - Deportivo Alavés vs Málaga — Under 1.5 Goles (under_1_5): Prob modelo 24.4%, EV -20.73%, EV robusto -36.98% → sin value.
  - Deportivo Alavés vs Málaga — Under 2.5 Goles (under_2_5): Prob modelo 37.5%, EV -33.21%, EV robusto -42.11% → sin value.
  - Deportivo Alavés vs Málaga — Over 3.5 Goles (over_3_5): Prob modelo 28.4%, EV +2.10%, EV robusto -15.90% → sin value.
  - Deportivo Alavés vs Málaga — Under 3.5 Goles (under_3_5): Prob modelo 71.6%, EV -6.87%, EV robusto -13.37% → sin value.
  - Deportivo Alavés vs Málaga — Over 8.5 Córners (over_corners_8_5): Prob modelo 50.3%, EV -16.93%, EV robusto -25.18% → sin value.
  - Deportivo Alavés vs Málaga — Over 9.5 Córners (over_corners_9_5): Prob modelo 40.4%, EV -17.15%, EV robusto -27.40% → sin value.
  - Deportivo Alavés vs Málaga — Under 9.5 Córners (under_corners_9_5): Prob modelo 59.6%, EV +4.27%, EV robusto -4.48% → sin value.
  - Deportivo Alavés vs Málaga — Over 10.5 Córners (over_corners_10_5): Prob modelo 31.5%, EV -16.50%, EV robusto -29.75% → sin value.
  - Deportivo Alavés vs Málaga — Under 10.5 Córners (under_corners_10_5): Prob modelo 68.5%, EV +1.37%, EV robusto -6.03% → sin value.
  - Deportivo Alavés vs Málaga — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 70.7%, EV +0.44%, EV robusto -6.66% → sin value.
  - Deportivo Alavés vs Málaga — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 29.3%, EV -19.52%, EV robusto -33.27% → sin value.
  - Deportivo Alavés vs Málaga — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 57.0%, EV +3.81%, EV robusto -5.29% → sin value.
  - Deportivo Alavés vs Málaga — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 43.0%, EV -16.22%, EV robusto -25.97% → sin value.
  - Deportivo Alavés vs Málaga — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 56.1%, EV -14.65%, EV robusto -22.25% → sin value.
  - Torino vs Monza — Over 1.5 Goles (over_1_5): Prob modelo 77.1%, EV +1.82%, EV robusto -4.78% → sin value.
  - Torino vs Monza — Under 1.5 Goles (under_1_5): Prob modelo 22.9%, EV -22.28%, EV robusto -39.28% → sin value.
  - Torino vs Monza — Under 2.5 Goles (under_2_5): Prob modelo 34.9%, EV -35.38%, EV robusto -44.63% → sin value.
  - Torino vs Monza — Under 3.5 Goles (under_3_5): Prob modelo 69.8%, EV -7.92%, EV robusto -14.52% → sin value.
  - Torino vs Monza — Over 8.5 Córners (over_corners_8_5): Prob modelo 53.8%, EV -13.97%, EV robusto -21.97% → sin value.
  - Torino vs Monza — Over 9.5 Córners (over_corners_9_5): Prob modelo 43.9%, EV -13.14%, EV robusto -23.04% → sin value.
  - Torino vs Monza — Under 9.5 Córners (under_corners_9_5): Prob modelo 56.1%, EV +2.16%, EV robusto -6.94% → sin value.
  - Torino vs Monza — Over 10.5 Córners (over_corners_10_5): Prob modelo 34.8%, EV -11.29%, EV robusto -24.04% → sin value.
  - Torino vs Monza — Under 10.5 Córners (under_corners_10_5): Prob modelo 65.2%, EV -0.88%, EV robusto -8.48% → sin value.
  - Torino vs Monza — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 61.6%, EV -7.67%, EV robusto -15.17% → sin value.
  - Torino vs Monza — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 38.4%, EV -3.89%, EV robusto -16.39% → sin value.
  - Torino vs Monza — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 46.5%, EV -9.35%, EV robusto -19.10% → sin value.
  - Torino vs Monza — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 53.5%, EV -2.60%, EV robusto -11.70% → sin value.
  - Brest vs Nice — Over 1.5 Goles (over_1_5): Prob modelo 78.0%, EV +1.41%, EV robusto -5.09% → sin value.
  - Brest vs Nice — Under 1.5 Goles (under_1_5): Prob modelo 22.0%, EV -21.94%, EV robusto -39.69% → sin value.
  - Brest vs Nice — Under 2.5 Goles (under_2_5): Prob modelo 33.5%, EV -36.41%, EV robusto -45.91% → sin value.
  - Brest vs Nice — Over 3.5 Goles (over_3_5): Prob modelo 31.4%, EV +3.49%, EV robusto -13.01% → sin value.
  - Brest vs Nice — Under 3.5 Goles (under_3_5): Prob modelo 68.6%, EV -8.02%, EV robusto -14.72% → sin value.
  - Brest vs Nice — Over 8.5 Córners (over_corners_8_5): Prob modelo 55.2%, EV -14.45%, EV robusto -22.20% → sin value.
  - Brest vs Nice — Over 9.5 Córners (over_corners_9_5): Prob modelo 45.3%, EV -12.98%, EV robusto -22.58% → sin value.
  - Brest vs Nice — Under 9.5 Córners (under_corners_9_5): Prob modelo 54.7%, EV +2.79%, EV robusto -6.61% → sin value.
  - Brest vs Nice — Over 10.5 Córners (over_corners_10_5): Prob modelo 36.2%, EV -11.32%, EV robusto -23.57% → sin value.
  - Brest vs Nice — Under 10.5 Córners (under_corners_10_5): Prob modelo 63.8%, EV -1.10%, EV robusto -8.85% → sin value.
  - Brest vs Nice — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 56.8%, EV -11.99%, EV robusto -19.74% → sin value.
  - Brest vs Nice — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 43.2%, EV +3.73%, EV robusto -8.27% → sin value.
  - Brest vs Nice — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 41.4%, EV -15.20%, EV robusto -25.45% → sin value.
  - Brest vs Nice — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 58.6%, EV +2.61%, EV robusto -6.14% → sin value.
  - Go Ahead Eagles vs Telstar — Over 1.5 Goles (over_1_5): Prob modelo 80.7%, EV -3.17%, EV robusto -9.17% → sin value.
  - Go Ahead Eagles vs Telstar — Under 1.5 Goles (under_1_5): Prob modelo 19.3%, EV -11.17%, EV robusto -34.17% → sin value.
  - Go Ahead Eagles vs Telstar — Under 2.5 Goles (under_2_5): Prob modelo 28.8%, EV -36.73%, EV robusto -47.73% → sin value.
  - Go Ahead Eagles vs Telstar — Over 3.5 Goles (over_3_5): Prob modelo 35.3%, EV -4.80%, EV robusto -18.30% → sin value.
  - Go Ahead Eagles vs Telstar — Under 3.5 Goles (under_3_5): Prob modelo 64.7%, EV -4.18%, EV robusto -11.58% → sin value.
  - Go Ahead Eagles vs Telstar — Over 8.5 Córners (over_corners_8_5): Prob modelo 60.6%, EV -9.10%, EV robusto -16.60% → sin value.
  - Go Ahead Eagles vs Telstar — Under 8.5 Córners (under_corners_8_5): Prob modelo 39.4%, EV +0.46%, EV robusto -12.29% → sin value.
  - Go Ahead Eagles vs Telstar — Over 9.5 Córners (over_corners_9_5): Prob modelo 51.0%, EV -5.69%, EV robusto -14.94% → sin value.
  - Go Ahead Eagles vs Telstar — Under 9.5 Córners (under_corners_9_5): Prob modelo 49.0%, EV -4.41%, EV robusto -14.16% → sin value.
  - Go Ahead Eagles vs Telstar — Over 10.5 Córners (over_corners_10_5): Prob modelo 41.8%, EV -1.84%, EV robusto -13.59% → sin value.
  - Go Ahead Eagles vs Telstar — Under 10.5 Córners (under_corners_10_5): Prob modelo 58.2%, EV -6.83%, EV robusto -14.83% → sin value.
  - Go Ahead Eagles vs Telstar — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 53.8%, EV -11.18%, EV robusto -19.43% → sin value.
  - Go Ahead Eagles vs Telstar — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 46.2%, EV +1.57%, EV robusto -9.43% → sin value.
  - Go Ahead Eagles vs Telstar — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 38.3%, EV -15.68%, EV robusto -26.68% → sin value.
  - Go Ahead Eagles vs Telstar — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 61.7%, EV +1.76%, EV robusto -6.49% → sin value.
  - Vitória Guimarães vs Marítimo — Over 1.5 Goles (over_1_5): Prob modelo 70.0%, EV -8.93%, EV robusto -15.43% → sin value.
  - Vitória Guimarães vs Marítimo — Under 2.5 Goles (under_2_5): Prob modelo 46.9%, EV -17.94%, EV robusto -26.69% → sin value.
  - Vitória Guimarães vs Marítimo — Over 3.5 Goles (over_3_5): Prob modelo 22.3%, EV -18.50%, EV robusto -36.75% → sin value.
  - Vitória Guimarães vs Marítimo — Under 3.5 Goles (under_3_5): Prob modelo 77.7%, EV -0.58%, EV robusto -6.98% → sin value.
  - Vitória Guimarães vs Marítimo — Over 8.5 Córners (over_corners_8_5): Prob modelo 53.3%, EV -17.40%, EV robusto -25.15% → sin value.
  - Vitória Guimarães vs Marítimo — Over 9.5 Córners (over_corners_9_5): Prob modelo 43.4%, EV -15.41%, EV robusto -25.16% → sin value.
  - Vitória Guimarães vs Marítimo — Under 9.5 Córners (under_corners_9_5): Prob modelo 56.6%, EV +4.75%, EV robusto -4.50% → sin value.
  - Vitória Guimarães vs Marítimo — Over 10.5 Córners (over_corners_10_5): Prob modelo 34.3%, EV -14.20%, EV robusto -26.70% → sin value.
  - Vitória Guimarães vs Marítimo — Under 10.5 Córners (under_corners_10_5): Prob modelo 65.7%, EV -0.17%, EV robusto -7.77% → sin value.
  - Vitória Guimarães vs Marítimo — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 70.7%, EV +2.57%, EV robusto -4.68% → sin value.
  - Vitória Guimarães vs Marítimo — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 29.3%, EV -22.45%, EV robusto -35.70% → sin value.
  - Vitória Guimarães vs Marítimo — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 43.0%, EV -17.51%, EV robusto -27.11% → sin value.
  - Vitória Guimarães vs Marítimo — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 56.1%, EV -15.77%, EV robusto -23.27% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Over 1.5 Goles (over_1_5): Prob modelo 65.0%, EV -7.71%, EV robusto -14.81% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Under 1.5 Goles (under_1_5): Prob modelo 35.0%, EV -0.22%, EV robusto -14.47% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Over 2.5 Goles (over_2_5): Prob modelo 44.9%, EV +3.36%, EV robusto -8.14% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Under 2.5 Goles (under_2_5): Prob modelo 55.1%, EV -10.80%, EV robusto -18.90% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Over 3.5 Goles (over_3_5): Prob modelo 17.9%, EV -23.16%, EV robusto -44.66% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Under 3.5 Goles (under_3_5): Prob modelo 82.1%, EV +0.20%, EV robusto -5.90% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Over 8.5 Córners (over_corners_8_5): Prob modelo 47.8%, EV -21.10%, EV robusto -29.35% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Over 9.5 Córners (over_corners_9_5): Prob modelo 37.9%, EV -20.38%, EV robusto -30.88% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Over 10.5 Córners (over_corners_10_5): Prob modelo 29.2%, EV -19.76%, EV robusto -33.51% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Under 10.5 Córners (under_corners_10_5): Prob modelo 70.8%, EV +2.69%, EV robusto -4.56% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 72.7%, EV +0.30%, EV robusto -6.60% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 27.3%, EV -19.40%, EV robusto -34.15% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 59.4%, EV +3.95%, EV robusto -4.80% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 40.6%, EV -16.77%, EV robusto -27.02% → sin value.
  - Gimnasia La Plata vs Sarmiento de Junín — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 53.6%, EV -16.85%, EV robusto -24.60% → sin value.
  - Gimnasia de Mendoza vs Platense — Over 1.5 Goles (over_1_5): Prob modelo 66.3%, EV -1.91%, EV robusto -9.31% → sin value.
  - Gimnasia de Mendoza vs Platense — Under 1.5 Goles (under_1_5): Prob modelo 33.7%, EV -12.33%, EV robusto -25.33% → sin value.
  - Gimnasia de Mendoza vs Platense — Under 2.5 Goles (under_2_5): Prob modelo 53.1%, EV -17.62%, EV robusto -25.37% → sin value.
  - Gimnasia de Mendoza vs Platense — Over 3.5 Goles (over_3_5): Prob modelo 18.9%, EV -9.47%, EV robusto -33.47% → sin value.
  - Gimnasia de Mendoza vs Platense — Under 3.5 Goles (under_3_5): Prob modelo 81.1%, EV -4.25%, EV robusto -10.15% → sin value.
  - Gimnasia de Mendoza vs Platense — Over 8.5 Córners (over_corners_8_5): Prob modelo 47.3%, EV -20.53%, EV robusto -28.93% → sin value.
  - Gimnasia de Mendoza vs Platense — Over 9.5 Córners (over_corners_9_5): Prob modelo 37.4%, EV -19.56%, EV robusto -30.31% → sin value.
  - Gimnasia de Mendoza vs Platense — Over 10.5 Córners (over_corners_10_5): Prob modelo 28.7%, EV -18.17%, EV robusto -32.42% → sin value.
  - Gimnasia de Mendoza vs Platense — Under 10.5 Córners (under_corners_10_5): Prob modelo 71.3%, EV +1.23%, EV robusto -5.87% → sin value.
  - Gimnasia de Mendoza vs Platense — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 72.7%, EV -1.16%, EV robusto -7.96% → sin value.
  - Gimnasia de Mendoza vs Platense — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 27.3%, EV -16.67%, EV robusto -31.92% → sin value.
  - Gimnasia de Mendoza vs Platense — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 59.4%, EV +0.98%, EV robusto -7.52% → sin value.
  - Gimnasia de Mendoza vs Platense — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 40.6%, EV -13.93%, EV robusto -24.53% → sin value.
  - Gimnasia de Mendoza vs Platense — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 53.6%, EV -14.17%, EV robusto -22.17% → sin value.
  - Tigre vs Atlético Tucumán — Over 1.5 Goles (over_1_5): Prob modelo 68.8%, EV -3.75%, EV robusto -10.75% → sin value.
  - Tigre vs Atlético Tucumán — Under 1.5 Goles (under_1_5): Prob modelo 31.2%, EV -9.38%, EV robusto -23.88% → sin value.
  - Tigre vs Atlético Tucumán — Under 2.5 Goles (under_2_5): Prob modelo 49.1%, EV -19.03%, EV robusto -27.28% → sin value.
  - Tigre vs Atlético Tucumán — Over 3.5 Goles (over_3_5): Prob modelo 21.1%, EV -11.42%, EV robusto -32.42% → sin value.
  - Tigre vs Atlético Tucumán — Under 3.5 Goles (under_3_5): Prob modelo 78.9%, EV -2.94%, EV robusto -9.09% → sin value.
  - Tigre vs Atlético Tucumán — Over 8.5 Córners (over_corners_8_5): Prob modelo 47.8%, EV -22.54%, EV robusto -30.64% → sin value.
  - Tigre vs Atlético Tucumán — Over 9.5 Córners (over_corners_9_5): Prob modelo 37.9%, EV -22.27%, EV robusto -32.52% → sin value.
  - Tigre vs Atlético Tucumán — Over 10.5 Córners (over_corners_10_5): Prob modelo 29.2%, EV -21.22%, EV robusto -34.72% → sin value.
  - Tigre vs Atlético Tucumán — Under 10.5 Córners (under_corners_10_5): Prob modelo 70.8%, EV +3.40%, EV robusto -3.90% → sin value.
  - Tigre vs Atlético Tucumán — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 70.7%, EV -0.97%, EV robusto -7.97% → sin value.
  - Tigre vs Atlético Tucumán — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 29.3%, EV -16.59%, EV robusto -30.84% → sin value.
  - Tigre vs Atlético Tucumán — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 57.0%, EV +1.53%, EV robusto -7.37% → sin value.
  - Tigre vs Atlético Tucumán — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 43.0%, EV -13.22%, EV robusto -23.32% → sin value.
  - Tigre vs Atlético Tucumán — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 56.1%, EV -12.96%, EV robusto -20.71% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Over 1.5 Goles (over_1_5): Prob modelo 69.4%, EV +0.60%, EV robusto -6.65% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Under 1.5 Goles (under_1_5): Prob modelo 30.6%, EV -17.33%, EV robusto -30.83% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Under 2.5 Goles (under_2_5): Prob modelo 48.2%, EV -22.94%, EV robusto -30.94% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Over 3.5 Goles (over_3_5): Prob modelo 21.6%, EV -2.76%, EV robusto -25.26% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Under 3.5 Goles (under_3_5): Prob modelo 78.4%, EV -5.93%, EV robusto -11.93% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Over 8.5 Córners (over_corners_8_5): Prob modelo 50.8%, EV -16.11%, EV robusto -24.36% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Over 9.5 Córners (over_corners_9_5): Prob modelo 40.9%, EV -14.08%, EV robusto -24.58% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Under 9.5 Córners (under_corners_9_5): Prob modelo 59.1%, EV +1.63%, EV robusto -6.97% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Over 10.5 Córners (over_corners_10_5): Prob modelo 32.0%, EV -10.47%, EV robusto -24.47% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Under 10.5 Córners (under_corners_10_5): Prob modelo 68.0%, EV -2.05%, EV robusto -9.25% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 71.2%, EV -1.70%, EV robusto -8.60% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 28.8%, EV -15.14%, EV robusto -29.89% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 57.6%, EV +0.87%, EV robusto -7.88% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 42.4%, EV -13.16%, EV robusto -23.41% → sin value.
  - Boyacá Chicó vs Atlético Bucaramanga — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 55.5%, EV -13.94%, EV robusto -21.69% → sin value.
  - Junior vs Águilas Doradas — Over 1.5 Goles (over_1_5): Prob modelo 68.8%, EV -5.11%, EV robusto -12.01% → sin value.
  - Junior vs Águilas Doradas — Under 1.5 Goles (under_1_5): Prob modelo 31.2%, EV -4.72%, EV robusto -19.97% → sin value.
  - Junior vs Águilas Doradas — Under 2.5 Goles (under_2_5): Prob modelo 49.1%, EV -16.58%, EV robusto -25.08% → sin value.
  - Junior vs Águilas Doradas — Over 3.5 Goles (over_3_5): Prob modelo 21.1%, EV -17.75%, EV robusto -37.25% → sin value.
  - Junior vs Águilas Doradas — Under 3.5 Goles (under_3_5): Prob modelo 78.9%, EV -0.57%, EV robusto -6.87% → sin value.
  - Junior vs Águilas Doradas — Over 8.5 Córners (over_corners_8_5): Prob modelo 51.8%, EV -18.11%, EV robusto -26.01% → sin value.
  - Junior vs Águilas Doradas — Over 9.5 Córners (over_corners_9_5): Prob modelo 41.9%, EV -17.03%, EV robusto -26.93% → sin value.
  - Junior vs Águilas Doradas — Over 10.5 Córners (over_corners_10_5): Prob modelo 32.9%, EV -14.43%, EV robusto -27.43% → sin value.
  - Junior vs Águilas Doradas — Under 10.5 Córners (under_corners_10_5): Prob modelo 67.1%, EV +0.63%, EV robusto -6.87% → sin value.
  - Junior vs Águilas Doradas — Over 3.5 Tarjetas (over_cards_3_5): Prob modelo 70.2%, EV -1.68%, EV robusto -8.68% → sin value.
  - Junior vs Águilas Doradas — Under 3.5 Tarjetas (under_cards_3_5): Prob modelo 29.8%, EV -15.15%, EV robusto -29.40% → sin value.
  - Junior vs Águilas Doradas — Over 4.5 Tarjetas (over_cards_4_5): Prob modelo 56.4%, EV +1.57%, EV robusto -7.43% → sin value.
  - Junior vs Águilas Doradas — Under 4.5 Tarjetas (under_cards_4_5): Prob modelo 43.6%, EV -12.86%, EV robusto -22.86% → sin value.
  - Junior vs Águilas Doradas — Under 5.5 Tarjetas (under_cards_5_5): Prob modelo 56.8%, EV -13.68%, EV robusto -21.28% → sin value.
- **Candidatos con value excluidos por probabilidad-primero:**
  - Ipswich Town vs Nottingham Forest: Victoria Nottingham Forest (2) EV +5.35% / EV rob -5.80%, Over 3.5 Goles (over_3_5) EV +5.87% / EV rob -9.63% — No cumple los mínimos de selección probabilidad-primero.
  - Deportivo Alavés vs Málaga: Under 8.5 Córners (under_corners_8_5) EV +9.24% / EV rob -1.76%, Over 5.5 Tarjetas (over_cards_5_5) EV +9.62% / EV rob -2.88% — No cumple los mínimos de selección probabilidad-primero.
  - Torino vs Monza: Over 3.5 Goles (over_3_5) EV +4.33% / EV rob -12.92%, Under 8.5 Córners (under_corners_8_5) EV +6.33% / EV rob -5.17% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Brest vs Nice: Victoria Nice (2) EV +3.81% / EV rob -10.94%, Under 8.5 Córners (under_corners_8_5) EV +7.53% / EV rob -4.47% — No cumple los mínimos de selección probabilidad-primero.
  - Vitória Guimarães vs Marítimo: Under 1.5 Goles (under_1_5) EV +4.82% / EV rob -12.68%, Over 2.5 Goles (over_2_5) EV +8.88% / EV rob -1.37%, Under 8.5 Córners (under_corners_8_5) EV +12.10% / EV rob +0.10%, Over 4.5 Tarjetas (over_cards_4_5) EV +5.52% / EV rob -3.73%, Over 5.5 Tarjetas (over_cards_5_5) EV +11.81% / EV rob -0.94% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Gimnasia La Plata vs Sarmiento de Junín: Empate (X) EV +3.28% / EV rob -15.72%, Under 8.5 Córners (under_corners_8_5) EV +14.80% / EV rob +3.80%, Under 9.5 Córners (under_corners_9_5) EV +6.79% / EV rob -1.81%, Over 5.5 Tarjetas (over_cards_5_5) EV +11.25% / EV rob -0.75% — Cuota alta sin los mínimos reforzados de probabilidad y EV robusto.
  - Gimnasia de Mendoza vs Platense: Over 2.5 Goles (over_2_5) EV +14.78% / EV rob +2.53%, Under 8.5 Córners (under_corners_8_5) EV +13.30% / EV rob +2.55%, Under 9.5 Córners (under_corners_9_5) EV +5.15% / EV rob -3.25%, Over 5.5 Tarjetas (over_cards_5_5) EV +8.94% / EV rob -2.81% — No cumple los mínimos de selección probabilidad-primero.
  - Tigre vs Atlético Tucumán: Over 2.5 Goles (over_2_5) EV +14.59% / EV rob +3.34%, Under 8.5 Córners (under_corners_8_5) EV +17.41% / EV rob +6.16%, Under 9.5 Córners (under_corners_9_5) EV +8.65% / EV rob -0.10%, Over 5.5 Tarjetas (over_cards_5_5) EV +7.42% / EV rob -4.83% — No cumple los mínimos de selección probabilidad-primero.
  - Boyacá Chicó vs Atlético Bucaramanga: Doble Oportunidad Empate/Atlético Bucaramanga (x2) EV +7.26% / EV rob +0.86%, DNB Atlético Bucaramanga (dnb_away) EV +12.46% / EV rob +4.97%, Over 2.5 Goles (over_2_5) EV +21.82% / EV rob +10.07%, Under 8.5 Córners (under_corners_8_5) EV +8.14% / EV rob -2.86%, Over 5.5 Tarjetas (over_cards_5_5) EV +6.75% / EV rob -5.25% — No cumple los mínimos de selección probabilidad-primero.
  - Junior vs Águilas Doradas: Over 2.5 Goles (over_2_5) EV +9.50% / EV rob -1.25%, Under 8.5 Córners (under_corners_8_5) EV +13.20% / EV rob +1.45%, Under 9.5 Córners (under_corners_9_5) EV +5.74% / EV rob -3.36%, Over 5.5 Tarjetas (over_cards_5_5) EV +7.16% / EV rob -5.24% — No cumple los mínimos de selección probabilidad-primero.

## Portfolio y Correlaciones
- **Exposición total:** 0.45u
- **Correlaciones detectadas:** Los 6 picks pertenecen todos al mercado Over 2.5 Goles en ligas/equipos distintos; sin correlación directa por equipo, aunque el riesgo de sesgo global al mercado es común.

- **Ajuste de stake por correlación:** Los picks pertenecen a partidos distintos; no se aplica reducción adicional por eventos dependientes.

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1 (VfB Stuttgart vs Borussia Mönchengladbach - over_2_5) | PENDIENTE | — | — |
| Pick 2 (Go Ahead Eagles vs Telstar - over_2_5) | PENDIENTE | — | — |
| Pick 3 (Ipswich Town vs Nottingham Forest - over_2_5) | PENDIENTE | — | — |
| Pick 4 (Brest vs Nice - over_2_5) | PENDIENTE | — | — |
| Pick 5 (Torino vs Monza - over_2_5) | PENDIENTE | — | — |
| Pick 6 (Deportivo Alavés vs Málaga - over_2_5) | PENDIENTE | — | — |
