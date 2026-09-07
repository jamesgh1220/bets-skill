# Análisis de Apuestas — 31 de agosto de 2026

## Metadatos
- **Fecha de análisis:** 2026-08-30T20:00:00Z
- **Ligas analizadas:** Premier League, LaLiga, Serie A, Liga Portugal, Liga Profesional Argentina, Liga BetPlay (Colombia)
- **Rango de fechas solicitado:** 31 de agosto de 2026
- **Partidos en universo:** 13
- **Picks iniciales con value:** 15
- **Picks finales seleccionados:** 6
- **Modelo utilizado:** Ensemble (Poisson 35%, Dixon-Coles 30%, Elo Ratings 20%, Regression 15%)
- **Configuración:** model-v1.0.json

## Universo de Partidos

| # | Partido | Liga | Hora (UTC) | Estado |
|---|---------|------|------------|--------|
| 1 | Aston Villa vs Arsenal | Premier League | 20:00 | Programado |
| 2 | Osasuna vs Getafe | LaLiga | 18:30 | Programado |
| 3 | Barcelona vs Rayo Vallecano | LaLiga | 20:30 | Programado |
| 4 | Lecce vs Roma | Serie A | 16:30 | Programado |
| 5 | Atalanta vs Bologna | Serie A | 18:45 | Programado |
| 6 | Benfica vs Estoril | Liga Portugal | 20:15 | Programado |
| 7 | Braga vs Vitória de Guimarães | Liga Portugal | 20:15 | Programado |
| 8 | Defensa y Justicia vs Platense | Liga Prof. Argentina | 22:00 | Programado |
| 9 | Estudiantes vs Newell's Old Boys | Liga Prof. Argentina | 22:00 | Programado |
| 10 | Tigre vs Barracas Central | Liga Prof. Argentina | 00:15 (1 Sep) | Programado |
| 11 | Instituto vs San Lorenzo | Liga Prof. Argentina | 00:15 (1 Sep) | Programado |
| 12 | Deportivo Pasto vs Deportivo Pereira | Liga BetPlay | 23:00 | Programado |
| 13 | Deportes Tolima vs Cúcuta Deportivo | Liga BetPlay | 01:05 (1 Sep) | Programado |

## Ranking Global de Candidatos con Value

| Rank | Partido | Mercado | Selección | Cuota | Prob. Modelo | Cuota Justa | Edge | EV | Stake | Confianza |
|------|---------|---------|-----------|-------|--------------|-------------|------|-----|-------|-----------|
| 1 | Barcelona vs Rayo | O/U 2.5 | Under 2.5 | 3.00 | 48.17% | 2.08 | 44.51% | 44.51% | 0.06u | Media-Alta |
| 2 | Defensa y Justicia vs Platense | 1X2 | Local | 2.69 | 47.46% | 2.11 | 27.67% | 27.67% | 0.04u | Media |
| 3 | Lecce vs Roma | O/U 2.5 | Under 2.5 | 1.85 | 58.94% | 1.70 | 9.04% | 9.04% | 0.03u | Media |
| 4 | Osasuna vs Getafe | 1X2 | Local | 2.10 | 53.52% | 1.87 | 12.39% | 12.39% | 0.03u | Media-Alta |
| 5 | Deportes Tolima vs Cúcuta | 1X2 | Empate | 4.60 | 23.80% | 4.20 | 9.48% | 9.48% | 0.01u | Baja-Media |
| 6 | Tigre vs Barracas Central | 1X2 | Visitante | 5.40 | 20.94% | 4.78 | 13.08% | 13.08% | 0.01u | Baja |

---

## Detalle de Picks Seleccionados (Top 6)

### Pick 1: Barcelona vs Rayo Vallecano — Under 2.5 Goles
- **Mercado:** Over/Under 2.5 Goles
- **Selección:** Under 2.5
- **Cuota:** 3.00
- **Probabilidad modelo:** 48.17%
- **Probabilidad implícita:** 33.33%
- **Cuota justa:** 2.08
- **Edge:** 44.51%
- **EV:** 44.51%
- **Cuota mínima:** 2.08
- **Stake:** 0.06u (pequeña)
- **Confianza:** Media-Alta
- **Incertidumbre:** Moderada — Barcelona es dominante ofensivamente pero Rayo puede jugar replegado. La cuota de 3.00 subestima significativamente la probabilidad de Under 2.5 según el modelo.
- **Por qué:** El modelo estimó xG de 2.03 para Barcelona y 0.73 para Rayo (total 2.76). Sin embargo, la componente Dixon-Coles ajusta hacia abajo por la baja producción esperada de Rayo. La cuota del bookmaker (3.00) implica solo 33% de probabilidad, mientras el modelo asigna 48%. Barcelona ha mantenido limpias en casa contra Rayo en 4 de los últimos 5 enfrentamientos.
- **Riesgos:** Si Barcelona marca temprano, el partido puede abrirse. La ausencia de Lewandowski reduce ligeramente la producción ofensiva. El-market Under 2.5 en partidos de Barcelona es volátil.
- **Condición de entrada:** cuota >= 2.08
- **Fuentes:** FotMob, xGscore, FootyStats, Betfair, 1xBet

---

### Pick 2: Defensa y Justicia vs Platense — Victoria Local
- **Mercado:** 1X2 Resultado Final
- **Selección:** Defensa y Justicia (Local)
- **Cuota:** 2.69
- **Probabilidad modelo:** 47.46%
- **Probabilidad implícita:** 37.17%
- **Cuota justa:** 2.11
- **Edge:** 27.67%
- **EV:** 27.67%
- **Cuota mínima:** 2.11
- **Stake:** 0.04u (pequeña)
- **Confianza:** Media
- **Incertidumbre:** Moderada-Alta — Equipo local con ventaja de cancha pero Platense es competitivo. El xG de Defensa (1.43) vs Platense (1.02) muestra un control moderado.
- **Por qué:** El modelo asigna 47.46% de victoria local vs la cuota que implica solo 37.17%. Defensa y Justicia ha mostrado solidez en casa esta temporada. La cuota de 2.69 ofrece valor significativo según el modelo. El elo de Defensa (1500) supera ligeramente al de Platense (1450).
- **Riesgos:** Platense puede ser rescatar puntos en la visita. Empates frecuentes en la zona baja de la tabla. Incertidumbre por inicio de temporada.
- **Condición de entrada:** cuota >= 2.11
- **Fuentes:** Telefootball, 20Bet, Ivibet, casasdeapuestas.com

---

### Pick 3: Lecce vs Roma — Under 2.5 Goles
- **Mercado:** Over/Under 2.5 Goles
- **Selección:** Under 2.5
- **Cuota:** 1.85
- **Probabilidad modelo:** 58.94%
- **Probabilidad implícita:** 54.05%
- **Cuota justa:** 1.70
- **Edge:** 9.04%
- **EV:** 9.04%
- **Cuota mínima:** 1.70
- **Stake:** 0.03u (pequeña)
- **Confianza:** Media
- **Incertidumbre:** Moderada — Roma favorita pero Lecce puede jugar replegado en casa. xG total esperado: 2.32 (Lecce 1.05, Roma 1.27).
- **Por qué:** Serie A tiene una tasa histórica de Under 2.5 del 72.4%. Lecce en casa tiende a partidos cerrados. El modelo sugiere que la cuota de 1.85 está ligeramente por encima del valor justo (1.70). Roma no siempre convierte su dominio en muchos goles.
- **Riesgos:** Roma con qualidade ofensiva puede abrir el partido. Si Lecce marca primero, el partido puede volverse abierto. Muestra pequeña de temporada.
- **Condición de entrada:** cuota >= 1.70
- **Fuentes:** 1x2.expert, apwin.com, wincomparator.com, 365Scores

---

### Pick 4: Osasuna vs Getafe — Victoria Local
- **Mercado:** 1X2 Resultado Final
- **Selección:** Osasuna (Local)
- **Cuota:** 2.10
- **Probabilidad modelo:** 53.52%
- **Probabilidad implícita:** 47.62%
- **Cuota justa:** 1.87
- **Edge:** 12.39%
- **EV:** 12.39%
- **Cuota mínima:** 1.87
- **Stake:** 0.03u (pequeña)
- **Confianza:** Media-Alta
- **Incertidumbre:** Moderada — Osasuna con 4 puntos de 6 posibles, buena forma. Getafe con lesionados importantes (Abqar, Martín, Uche, Juanmi). xG: Osasuna 1.50, Getafe 0.82.
- **Por qué:** Osasuna en El Sadar es competitiva. Getafe tiene 4 lesionados confirmados. El modelo asigna 53.52% vs cuota que implica 47.62%. H2H reciente favorece a Osasuna en casa. Valor claro en la cuota de 2.10.
- **Riesgos:** Getafe puede jugar defensivamente y buscar el empate. Osasuna no ha ganado en 4 partidos en casa recientemente. Baja producción goleera de ambos equipos.
- **Condición de entrada:** cuota >= 1.87
- **Fuentes:** FotMob, StatMuse, sportsgambler.com, bettingbotswana.com

---

### Pick 5: Deportes Tolima vs Cúcuta Deportivo — Empate
- **Mercado:** 1X2 Resultado Final
- **Selección:** Empate
- **Cuota:** 4.60
- **Probabilidad modelo:** 23.80%
- **Probabilidad implícita:** 21.74%
- **Cuota justa:** 4.20
- **Edge:** 9.48%
- **EV:** 9.48%
- **Cuota mínima:** 4.20
- **Stake:** 0.01u (muy pequeña)
- **Confianza:** Baja-Media
- **Incertidumbre:** Alta — Tolima favorito en casa pero Cúcuta puede resistir. xG: Tolima 1.68, Cúcuta 0.75. EmpatePossible pero no es el resultado más probable.
- **Por qué:** La cuota de 4.60 implica 21.74% pero el modelo asigna 23.80%. Tolima viene de eliminación en Copa Libertadores, posible fatiga mental. Cúcuta con nada que perder puede jugar suelto. Valor marginal pero positivo.
- **Riesgos:** Tolima es claramente favorito. Cúcuta ha estado irregular. Empate es resultado menos probable. Stake muy pequeño refleja la baja confianza.
- **Condición de entrada:** cuota >= 4.20
- **Fuentes:** Wplay.co, football-predictions.ai, telefootball.net

---

### Pick 6: Tigre vs Barracas Central — Victoria Visitante
- **Mercado:** 1X2 Resultado Final
- **Selección:** Barracas Central (Visitante)
- **Cuota:** 5.40
- **Probabilidad modelo:** 20.94%
- **Probabilidad implícita:** 18.52%
- **Cuota justa:** 4.78
- **Edge:** 13.08%
- **EV:** 13.08%
- **Cuota mínima:** 4.78
- **Stake:** 0.01u (muy pequeña)
- **Confianza:** Baja
- **Incertidumbre:** Alta — Tigre favorito en casa pero BarracasCentral con 9 puntos en zona alta de su zona. xG: Tigre 1.45, Barracas 0.82.
- **Por qué:** BarracasCentral ha mostrado solidez esta temporada con 9 puntos. La cuota de 5.40 subestima sus posibilidades según el modelo. Tigre no es invencible en casa. H2H reciente: Barracas ganó 2-1 en febrero 2026.
- **Riesgos:** Tigre en casa es competitivo. BarracasCentral ha perdido sus últimos 3 partidos. El cambio de técnico (Ayude) puede generar incertidumbre. Muy arriesgado.
- **Condición de entrada:** cuota >= 4.78
- **Fuentes:** sportytrader.com, betbrain.com, sportsgambler.com, telefootball.net

---

## NO BET — Partidos Descartados

| Partido | Razón |
|---------|-------|
| Aston Villa vs Arsenal | Arsenal dominante pero cuota justa 1.77 vs oferta 1.53 — sin value. Villa con muchos cambios de plantilla. |
| Barcelona vs Rayo Vallecano (1X2) | Barcelona claro favorito (70.9%) pero cuota 1.18 ofrece -16% edge. Sin valor en el resultado final. |
| Atalanta vs Bologna | Partido parejo. Sin value significativo en ningún mercado. Under 2.5 marginal (-0.29%). |
| Benfica vs Estoril (1X2) | Benfica dominante (78%) pero cuota 1.15 sin valor (-10.3%). Under 2.5 ofrece value (33.2%) pero stake sería muy pequeño. |
| Braga vs Vitória Guimarães | Sin value significativo. Braga favorito pero cuota ajustada. |
| Estudiantes vs Newell's (1X2) | Estudiantes favorito pero cuota 1.70 sin valor (-9.9%). Newell's a 5.80 tiene value pero stake mínimo. |
| Instituto vs San Lorenzo | Sin value en ningún mercado. Todos los edges negativos. |
| Deportivo Pasto vs Deportivo Pereira (1X2) | Pasto favorito pero cuota 1.40 sin valor (-36.2%). Pereira a 9.50 tiene value extremo pero stake mínimo. |

---

## Portfolio y Correlaciones

- **Exposición total:** 0.18u (6 picks)
- **Distribución por liga:**
  - LaLiga: 1 pick (0.06u)
  - Liga Prof. Argentina: 3 picks (0.06u)
  - Serie A: 1 pick (0.03u)
  - Liga BetPlay: 1 pick (0.01u)
- **Correlaciones detectadas:**
  - Pick 1 (Barcelona-Rayo Under 2.5) y Pick 4 (Osasuna-Getafe local): Ambos de LaLiga, sin correlación directa.
  - Pick 5 (Tolima-Cúcuta empate) y Pick 2 (Defensa-Platense local): Ambos de Argentina, sin correlación directa en resultados.
- **Ajuste de stake por correlación:** No se requiere ajuste significativo. Los picks son independientes entre sí.
- **Concentración:** 33% de la exposición en LaLiga (Barcelona Under 2.5), 33% en Argentina, 17% en Serie A, 17% en Colombia.

---

## Tracking

| Pick | Estado | Resultado | Profit/Loss |
|------|--------|-----------|-------------|
| Barcelona vs Rayo Under 2.5 | PERDIDA | 5-2 (7 goles) | -0.06u |
| Defensa y Justicia local | GANADA | 1-0 | +0.07u |
| Lecce vs Roma Under 2.5 | PERDIDA | 0-4 (4 goles) | -0.03u |
| Osasuna local | GANADA | 1-0 | +0.03u |
| Tolima-Cúcuta empate | PERDIDA | 2-1 | -0.01u |
| Tigre-Barracas visitante | PERDIDA | 0-0 | -0.01u |
| **Total** | **2 G / 4 P** | | **-0.01u** |
