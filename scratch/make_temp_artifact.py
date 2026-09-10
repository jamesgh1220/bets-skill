import os
import sys

content = """# Análisis de Apuestas — 10 de septiembre de 2026

## Metadatos
- **Fecha de análisis:** 2026-09-09T20:18:42-05:00
- **Fecha(s) de partido:** 10 de septiembre de 2026
- **Information cutoff:** 2026-09-09T20:18:42-05:00
- **Modelo de IA:** gemini3.6flash
- **Versión del motor predictivo:** model-v1.2
- **Ligas analizadas:** Liga BetPlay (Colombia), Copa Colombia, Champions League, Liga Portugal, Copa Libertadores, Copa Sudamericana
- **Rango de fechas solicitado:** 10 de septiembre de 2026
- **Partidos en universo:** 10
- **Picks iniciales con value:** 17
- **Picks finales seleccionados:** 4

## Universo Analizado
- **Liga BetPlay (Colombia):** 1 partido analizado (Millonarios vs Deportivo Cali).
- **Copa Libertadores:** 1 partido analizado (Independiente del Valle vs Flamengo).
- **Copa Sudamericana:** 1 partido analizado (Cienciano vs Montevideo City Torque).
- **UEFA Champions League:** 6 partidos analizados (Fenerbahçe vs AS Roma, Como vs RB Leipzig, Bayern Múnich vs Bodø/Glimt, PSV Eindhoven vs Shakhtar Donetsk, Slavia Praga vs RC Lens, Manchester United vs Sabah FK).
- **Liga Portugal:** 1 partido analizado (Estrela Amadora vs Braga).
- **Copa Colombia:** 0 partidos programados en la fecha 10 de septiembre de 2026.

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Como vs RB Leipzig | over_2_5 | Más de 2.5 Goles | prioritario | 1.75 | 65.07% | 1.54 | +13.87% | +13.87% | +5.12% | 0.05u | Media-Alta |
| 2 | Independiente del Valle vs Flamengo | over_2_5 | Más de 2.5 Goles | prioritario | 2.05 | 62.80% | 1.59 | +28.74% | +28.74% | +18.49% | 0.07u | Alta |
| 3 | Slavia Praga vs RC Lens | over_2_5 | Más de 2.5 Goles | prioritario | 1.90 | 60.43% | 1.65 | +14.82% | +14.82% | +5.32% | 0.04u | Media-Alta |
| 4 | Bayern Múnich vs Bodø/Glimt | under_3_5 | Menos de 3.5 Goles | prioritario | 2.00 | 59.81% | 1.67 | +19.62% | +19.62% | +9.62% | 0.05u | Alta |
| 5 | Cienciano vs Montevideo City Torque | 2 | Victoria visitante | excluido | 5.50 | 24.85% | 4.02 | +36.67% | +36.67% | +9.18% | 0.02u | Baja |
| 6 | Cienciano vs Montevideo City Torque | over_2_5 | Más de 2.5 Goles | excluido | 1.85 | 61.23% | 1.63 | +13.28% | +13.28% | +4.03% | 0.04u | Media |
| 7 | Cienciano vs Montevideo City Torque | x2 | Empate o Visitante | excluido | 2.30 | 50.76% | 1.97 | +16.75% | +16.75% | +5.25% | 0.03u | Media |
| 8 | Millonarios vs Deportivo Cali | 2 | Victoria visitante | excluido | 5.25 | 22.86% | 4.37 | +20.02% | +20.02% | -6.24% | 0.01u | Baja |
| 9 | Millonarios vs Deportivo Cali | x2 | Empate o Visitante | excluido | 2.15 | 50.92% | 1.96 | +9.48% | +9.48% | -1.27% | 0.02u | Media |
| 10 | Millonarios vs Deportivo Cali | over_2_5 | Más de 2.5 Goles | excluido | 2.15 | 49.09% | 2.04 | +5.54% | +5.54% | -5.21% | 0.01u | Media |
| 11 | Fenerbahçe vs AS Roma | over_2_5 | Más de 2.5 Goles | excluido | 1.73 | 64.32% | 1.55 | +11.27% | +11.27% | +2.62% | 0.04u | Media |
| 12 | Estrela Amadora vs Braga | over_2_5 | Más de 2.5 Goles | excluido | 1.85 | 60.43% | 1.65 | +11.80% | +11.80% | +2.55% | 0.03u | Media |
| 13 | Estrela Amadora vs Braga | 2 | Victoria visitante | excluido | 1.78 | 59.82% | 1.67 | +6.48% | +6.48% | -2.42% | 0.02u | Media |
| 14 | Bayern Múnich vs Bodø/Glimt | X | Empate | excluido | 8.50 | 13.66% | 7.32 | +16.11% | +16.11% | -26.39% | 0.01u | Baja |
| 15 | Manchester United vs Sabah FK | X | Empate | excluido | 9.50 | 12.18% | 8.21 | +15.71% | +15.71% | -31.79% | 0.00u | Baja |
| 16 | PSV Eindhoven vs Shakhtar Donetsk | over_2_5 | Más de 2.5 Goles | excluido | 1.45 | 71.86% | 1.39 | +4.20% | +4.20% | -3.05% | 0.02u | Media |
| 17 | Estrela Amadora vs Braga | dnb_away | Empate no Apuesta | excluido | 1.30 | 59.82% | 1.26 | +2.61% | +2.61% | -3.89% | 0.02u | Media |

## Picks Recomendados (Top 4)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Como vs RB Leipzig | over_2_5 | Más de 2.5 Goles | prioritario | 1.75 | 65.07% | 1.54 | +13.87% | +13.87% | +5.12% | 0.05u | Media-Alta |
| 2 | Independiente del Valle vs Flamengo | over_2_5 | Más de 2.5 Goles | prioritario | 2.05 | 62.80% | 1.59 | +28.74% | +28.74% | +18.49% | 0.07u | Alta |
| 3 | Slavia Praga vs RC Lens | over_2_5 | Más de 2.5 Goles | prioritario | 1.90 | 60.43% | 1.65 | +14.82% | +14.82% | +5.32% | 0.04u | Media-Alta |
| 4 | Bayern Múnich vs Bodø/Glimt | under_3_5 | Menos de 3.5 Goles | prioritario | 2.00 | 59.81% | 1.67 | +19.62% | +19.62% | +9.62% | 0.05u | Alta |

## Detalle de Picks
### Pick 1: Como vs RB Leipzig
- **Mercado:** over_2_5
- **Selección:** Más de 2.5 Goles
- **Cuota:** 1.75
- **Probabilidad modelo:** 65.07%
- **Probabilidad conservadora:** 60.07%
- **Probabilidad implícita:** 57.14%
- **Cuota justa:** 1.54
- **Edge:** 13.87%
- **EV:** +13.87%
- **EV robusto:** +5.12%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.60
- **Stake:** 0.05u
- **Confianza:** Media-Alta
- **Incertidumbre:** 5.0%
- **Por qué:** El modelo ensemble estima 2.77 goles esperados totales (1.35 Como, 1.42 Leipzig). Tras aplicar la calibración Platt activa del motor v1.2, la probabilidad del Over 2.5 asciende a 65.07% frente a una probabilidad implícita de cuota del 57.14%, generando un EV robusto del +5.12%.
- **Riesgos:** Planteamiento defensivo de especulación por ser el primer partido de fase de liga.
- **Fuentes:** bwin, Betplay, Transfermarkt, motor cuantitativo model-v1.2.

### Pick 2: Independiente del Valle vs Flamengo
- **Mercado:** over_2_5
- **Selección:** Más de 2.5 Goles
- **Cuota:** 2.05
- **Probabilidad modelo:** 62.80%
- **Probabilidad conservadora:** 57.80%
- **Probabilidad implícita:** 48.78%
- **Cuota justa:** 1.59
- **Edge:** 28.74%
- **EV:** +28.74%
- **EV robusto:** +18.49%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.70
- **Stake:** 0.07u
- **Confianza:** Alta
- **Incertidumbre:** 5.0%
- **Por qué:** Ambos conjuntos son los líderes en goles esperados generados en la Copa Libertadores (IDV 16.1 xG, Flamengo 15.2 xG). La altitud de Quito (2.850m) impulsa duelos de alta velocidad en transiciones ofensivas. La probabilidad calibrada del 62.80% supera holgadamente el 48.78% de las casas.
- **Riesgos:** Que Flamengo administre el ritmo del juego para minimizar el impacto del factor altitud.
- **Fuentes:** CONMEBOL.com, Betplay, Wplay, PrensaFútbol.

### Pick 3: Slavia Praga vs RC Lens
- **Mercado:** over_2_5
- **Selección:** Más de 2.5 Goles
- **Cuota:** 1.90
- **Probabilidad modelo:** 60.43%
- **Probabilidad conservadora:** 55.43%
- **Probabilidad implícita:** 52.63%
- **Cuota justa:** 1.65
- **Edge:** 14.82%
- **EV:** +14.82%
- **EV robusto:** +5.32%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.75
- **Stake:** 0.04u
- **Confianza:** Media-Alta
- **Incertidumbre:** 5.0%
- **Por qué:** Slavia Praga presenta un perfil local ofensivo intenso (xG for 1.35) y Lens aporta pegada en contraataque (xG for 1.45). Con probabilidad modelo del 60.43% y cuota 1.90, el EV robusto se mantiene en +5.32% tras aplicar la incertidumbre base.
- **Riesgos:** Falta de puntería en la definición o bloqueos defensivos en balones parados.
- **Fuentes:** UEFA.com, Betsson, Flashscore.

### Pick 4: Bayern Múnich vs Bodø/Glimt
- **Mercado:** under_3_5
- **Selección:** Menos de 3.5 Goles
- **Cuota:** 2.00
- **Probabilidad modelo:** 59.81%
- **Probabilidad conservadora:** 54.81%
- **Probabilidad implícita:** 50.00%
- **Cuota justa:** 1.67
- **Edge:** 19.62%
- **EV:** +19.62%
- **EV robusto:** +9.62%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.78
- **Stake:** 0.05u
- **Confianza:** Alta
- **Incertidumbre:** 5.0%
- **Por qué:** Bodø/Glimt planteará una estructura ultradefensiva en el Allianz Arena. Las simulaciones Monte Carlo y Poisson indican que la probabilidad de 4 o más goles es de solo 40.19%, dejando la probabilidad de Under 3.5 en 59.81% con excelente margen frente al 50.00% implícito.
- **Riesgos:** Goleada temprana de Bayern que desarticule el esquema visitante.
- **Fuentes:** UEFA.com, Betplay, Wplay.

## NO BET / Excluidos
- **Millonarios vs Deportivo Cali (Victoria Cali @5.25 / Over 2.5 @2.15 / X2 @2.15):** Excluidos por tener EV robusto negativo (-6.24%, -5.21% y -1.27%) tras el descuento de incertidumbre.
- **Cienciano vs Montevideo City Torque (Victoria Torque @5.50 / Over 2.5 @1.85 / X2 @2.30):** Excluidos por requerir mayor soporte probabilístico en cuotas altas (24.85% vs 30% exigido) o EV robusto inferior al 5% (+4.03%).
- **Fenerbahçe vs AS Roma (Over 2.5 @1.73):** Excluido porque su EV robusto (+2.62%) no alcanza el umbral mínimo del +5.0% para perfil prioritario.
- **Bayern Múnich vs Bodø/Glimt (Empate @8.50):** Excluido por probabilidad modelo del 13.66%, insuficiente para cuota >=3.00.
- **PSV Eindhoven vs Shakhtar Donetsk (Over 2.5 @1.45):** Excluido por cuota inferior al rango prioritario (1.50-2.20) y EV robusto negativo (-3.05%).
- **Manchester United vs Sabah FK (Empate @9.50):** Excluido por probabilidad modelo del 12.18%, insuficiente para cuota >=3.00.
- **Estrela Amadora vs Braga (Victoria Braga @1.78 / Over 2.5 @1.85 / DNB Braga @1.30):** Excluidos por EV robusto negativo tras la prueba de sensibilidad.

## Portfolio y Correlaciones
- **Exposición total:** 0.21u (0.05u + 0.07u + 0.04u + 0.05u)
- **Correlaciones detectadas:** Tres elecciones corresponden al mercado Over 2.5 en torneos distintos (UCL y Libertadores).
- **Ajuste de stake por correlación:** Sin penalización acumulada por tratarse de competiciones e instancias completamente independientes.

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Pick 1: Como vs RB Leipzig (Over 2.5) | PENDIENTE | — | — |
| Pick 2: Independiente del Valle vs Flamengo (Over 2.5) | PENDIENTE | — | — |
| Pick 3: Slavia Praga vs RC Lens (Over 2.5) | PENDIENTE | — | — |
| Pick 4: Bayern Múnich vs Bodø/Glimt (Under 3.5) | PENDIENTE | — | — |
"""

os.makedirs("scratch", exist_ok=True)
with open("scratch/temp_artifact.md", "w", encoding="utf-8") as f:
    f.write(content)

print("scratch/temp_artifact.md creado exitosamente")
