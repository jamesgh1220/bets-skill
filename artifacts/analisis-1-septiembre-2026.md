# Análisis de Apuestas — 1 de septiembre de 2026

## Metadatos
- **Fecha de análisis:** 2026-08-31T22:00:00Z
- **Fecha de partidos:** 2026-09-01
- **Corte de información (information_cutoff):** 2026-08-31T22:00:00Z
- **Ligas analizadas:** Liga BetPlay (Colombia), Categoría Primera B (Colombia), Coppa Italia, Saudi Pro League
- **Rango de fechas solicitado:** 1 de septiembre de 2026
- **Partidos en universo:** 6
- **Picks iniciales con value:** 7
- **Picks finales seleccionados:** 3
- **Modelo utilizado:** Ensemble (Poisson 35%, Dixon-Coles 30%, Elo Ratings 20%, Regression 15%)
- **Configuración:** model-v1.0.json (active)

## Universo de Partidos

| # | Partido | Liga | Estado |
|---|---------|------|--------|
| 1 | Fortaleza vs Once Caldas | Liga BetPlay | Analizado → NO BET |
| 2 | Envigado vs Unión Magdalena | Primera B | Analizado → PICK |
| 3 | Barranquilla vs Boca Juniors de Cali | Primera B | Analizado → PICK |
| 4 | Parma vs Cremonese | Coppa Italia | Analizado → NO BET (pick marginal descartado) |
| 5 | Torino vs Monza | Coppa Italia | Analizado → PICK |
| 6 | Al-Hilal vs Al-Ahli SC | Saudi Pro League | Analizado → NO BET |

> **Nota de cuotas:** Las cuotas de bookmakers colombianos (Betplay/Betsson/Wplay/Rushbet/Zamba/Sportium) no estuvieron accesibles por scraping directo. Se utilizaron cuotas de respaldo de Bet365 y estimaciones de mejores cuotas de agregadores (Wincomparator, oddschecker). Metodología antropométrica sujeto a margen. El modelo usa la cuota de entrada como referencia. Recomendable confirmar la cuota en caja antes de entrar.

## Ranking Global de Candidatos con Value

Ordenado por EV robusto (Edge sostenido bajo escenarios adversos).

| Rank | Partido | Mercado | Selección | Cuota | Prob. Modelo | Cuota Justa | Edge | EV | Stake | Confianza | Robustez |
|------|---------|---------|-----------|-------|--------------|-------------|------|-----|-------|-----------|----------|
| 1 | Torino vs Monza | BTTS | Sí | 2.00 | 60.98% | 1.64 | 21.96% | 21.96% | 0.50u | Media-Alta | Alta (19-22%) |
| 2 | Envigado vs Unión Magdalena | 1X2 | Local (Envigado) | 2.15 | 52.28% | 1.91 | 12.40% | 12.40% | 0.50u | Media | Media (4-12%) |
| 3 | Barranquilla vs Boca Cali | 1X2 | Local (Barranquilla) | 2.60 | 44.46% | 2.25 | 15.60% | 15.60% | 0.25u | Media | Media (8-16%) |
| 4 | Torino vs Monza | O/U 2.5 | Over 2.5 | 1.90 | 58.79% | 1.70 | 11.70% | 11.70% | — | Media | Media | 
| 5 | Envigado vs Unión Magdalena | O/U 2.5 | Over 2.5 | 2.38 | 46.89% | 2.13 | 11.60% | 11.60% | — | Baja | Baja |
| 6 | Parma vs Cremonese | O/U 2.5 | Under 2.5 | 1.85 | 56.97% | 1.76 | 5.39% | 5.39% | — | Baja | Baja |
| 7 | Torino vs Monza | 1X2 | Visitante (Monza) | 3.90 | 27.23% | 3.67 | 6.20% | 6.20% | — | Baja | — |

> Los coeficientes #4 y #5 (Torino Over 2.5) son **altamente correlacionados** con el #1 (BTTS Yes del mismo partido): se descartan para no duplicar exposición. #5 y #6 tienen EV marginal y baja robustez → se descartan.

---

## Picks Seleccionados (Top 3)

| Rank | Partido | Mercado | Selección | Cuota | Prob. | Justa | Edge | EV | Stake | Confianza |
|------|---------|---------|-----------|-------|-------|-------|------|-----|-------|-----------|
| 1 | Torino vs Monza | BTTS | Sí | 2.00 | 60.98% | 1.64 | 21.96% | 21.96% | 0.50u | Media-Alta |
| 2 | Envigado vs Unión Magdalena | 1X2 | Local | 2.15 | 52.28% | 1.91 | 12.40% | 12.40% | 0.50u | Media |
| 3 | Barranquilla vs Boca Cali | 1X2 | Local | 2.60 | 44.46% | 2.25 | 15.60% | 15.60% | 0.25u | Media |

---

## Detalle de Picks

### Pick 1: Torino vs Monza — BTTS Sí
- **Mercado:** Ambos equipos marcan (BTTS)
- **Selección:** Sí
- **Cuota:** 2.00
- **Probabilidad modelo:** 60.98%
- **Probabilidad implícita:** 50.00%
- **Cuota justa:** 1.64
- **Edge:** 21.96%
- **EV:** 21.96%
- **Cuota mínima:** 1.64
- **Stake:** 0.50u (moderada)
- **Confianza:** Media-Alta
- **Incertidumbre:** Moderada — rotación típica de Coppa Italia; con apertura del partido probable. Robustez alta (vigor a 19% en escenario adverso).
- **Por qué:** Monza lleva un ataque en forma (Varela, 6 goles últimos 5 partidos; 44 tiros en 5 partidos) y defensa muy vulnerable (7 goles recibidos en 2 jornadas de Serie A). Torino, pese a su irregularidad, anota con regularidad en casa (7 de 10 últimos con BTTS). Ambas defensorías débiles + ritmo de copa con rotaciones → alta probabilidad de gol de ambos. El modelo asigna 61%, cuota implica 50%.
- **Riesgos:** Rotación de titulares puede bajar el volumen ofensivo de Torino; Monza jugando de visitante puede replegarse. Under 2.5 en los últimos Torino-Monza H2H (partidos cerrados en liga).
- **Fuentes:** Wincomparator, SportsGambler, Tips.gg (01/09/2026); form Serie A 22-29/08.

### Pick 2: Envigado vs Unión Magdalena — Victoria Envigado
- **Mercado:** 1X2
- **Selección:** Local (Envigado)
- **Cuota:** 2.15
- **Probabilidad modelo:** 52.28%
- **Probabilidad implícita:** 46.51%
- **Cuota justa:** 1.91
- **Edge:** 12.40%
- **EV:** 12.40%
- **Cuota mínima:** 1.91
- **Stake:** 0.50u (moderada)
- **Confianza:** Media
- **Incertidumbre:** Alta-Moderada — liga de bajo volumen de datos (Primera B); robustez media (edge cae a 4% en escenario adverso).
- **Por qué:** Unión Magdalena llega en pésima forma (0 victorias en últimos 5, 3 derrotas, sin goles; 16º puesto, 1 punto en 4). Envigado, 13º con 4 puntos, juega en casa (Polideportivo Sur) y domina el H2H reciente (2-1 en 2025). Modelo asigna 52% vs 46.5% implícito.
- **Riesgos:** Envigado también irregular (3 derrotas en últimos 4); H2H de Primera B voluble. Si Unión Magdalena mejora ofensivamente podría empatar.
- **Fuentes:** Wincomparator (1/9/26), APWin (31/08/26) — forma y clasificación.

### Pick 3: Barranquilla vs Boca Juniors de Cali — Victoria Barranquilla
- **Mercado:** 1X2
- **Selección:** Local (Barranquilla)
- **Cuota:** 2.60
- **Probabilidad modelo:** 44.46%
- **Probabilidad implícita:** 38.46%
- **Cuota justa:** 2.25
- **Edge:** 15.60%
- **EV:** 15.60%
- **Cuota mínima:** 2.25
- **Stake:** 0.25u (pequeña)
- **Confianza:** Media
- **Incertidumbre:** Alta — Primera B con muestra pequeña; robustez media (edge 8% en escenario adverso).
- **Por qué:** Barranquilla acumula 7 partidos consecutivos sin perder en casa (Estadio Romelio Martínez), ventaja de localía clara. Boca Cali llega de 2 derrotas seguidas con 5 goles recibidos y sin regularidad. Modelo asigna 44.5% vs 38.5% implícito a cuota 2.60.
- **Riesgos:** Barranquilla lleva 10 partidos sin mantener portería a cero, por lo que la victoria no es cómoda; partidos H2H cortos. Boca puede competir fuera.
- **Fuentes:** ApuestasGanadas (31/08/26), Betimate, Wincomparator — forma y localía.

---

## NO BET / Descartados

- **Fortaleza vs Once Caldas:** Todas las selecciones 1X2 con edge negativo (mejor -4.96% en el Local). Sin value.
- **Al-Hilal vs Al-Ahli SC:** Local a 1.66 con fair 1.67 (edge -0.73%) — sin value suficiente para justificar riesgo. NO BET.
- **Parma vs Cremonese:** Under 2.5 +5.4% marginal y baja robustez (ambos sin goles; pero rotación/incertidumbre alta). Descartado.
- **Torino/Monza Over 2.5 y Envigado Over 2.5:** EV positivo pero correlacionados o menos robustos que el pick principal de cada partido. Excluidos por concentración.

## Portfolio y Correlaciones
- **Exposición total:** 1.25u
- **Correlaciones detectadas:**
  - Torino vs Monza: BTTS Yes desechó el Over 2.5 correlacionado (no duplicar).
  - Envigado: se eligió la victoria local sobre el Over (menos correlacionado con el resultado), evitando dos posiciones en la misma liga redundantes.
- **Ajuste por correlación:** Exposición controlada; picks en 3 partidos independientes entre sí (2 Coppa/serie separadas, 2 Primera B).
- **Diversificación:** 3 mercados distintos (BTTS, 1X2 local x2) en 3 partidos.

## Riesgos Globales
- Cuotas de bookmakers colombianos no confirmadas; confirmar en caja antes de entrar (condición de cuota >= cuota mínima en cada pick).
- Ligas de baja liquidez de datos (Primera B) aumentan incertidumbre del modelo.
- Coppa Italia con riesgo de rotación.

## Tracking

| # | Partido | Mercado | Selección | Cuota | Stake | Resultado | Estado | P/L |
|---|---------|---------|-----------|-------|-------|-----------|--------|-----|
| 1 | Torino vs Monza | BTTS | Sí | 2.00 | 0.50u | 0 - 1 (sin BTTS) | PERDIDA | -0.50u |
| 2 | Envigado vs Unión Magdalena | 1X2 | Local (Envigado) | 2.15 | 0.50u | 0 - 1 | PERDIDA | -0.50u |
| 3 | Barranquilla vs Boca Cali | 1X2 | Local (Barranquilla) | 2.60 | 0.25u | 2 - 1 | GANADA | +0.40u |
| **Total** | | | | | **1.25u** | | **1 G / 2 P** | **-0.60u** |
