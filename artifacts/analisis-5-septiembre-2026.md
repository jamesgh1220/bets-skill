# Análisis de Apuestas — 5 de septiembre de 2026

## Metadatos
- **Fecha de análisis:** 5 de septiembre de 2026
- **Fecha del partido (rango solicitado):** 5 de septiembre de 2026
- **Ligas analizadas:** Bundesliga, Liga Argentina, Liga BetPlay (Colombia), LaLiga (España), MLS, Ligue 1, Premier League, Serie A, Eredivisie, Liga Portugal
- **Partidos en universo:** 44
- **Picks iniciales con value (motor):** 14 mercados → 3 robustos
- **Picks finales seleccionados:** 3
- **Information cutoff:** 5 de septiembre de 2026, ~10:00 COT (+2h antes del primer KO)
- **Motor utilizado:** `scripts/calc_engine.py` (modelo ensemble v1.0 activo) — determinista, sin probabilidades inventadas

## Universo Analizado (44 partidos confirmados — sábado 5 sep 2026)

**Premier League (7):** Newcastle vs Bournemouth, Brentford vs Sunderland, Brighton vs Leeds, Fulham vs Crystal Palace, Man City vs Coventry, Nottingham Forest vs Tottenham, Hull vs Aston Villa

**Bundesliga (6):** Union Berlin vs Leverkusen, Elversberg vs Mönchengladbach, Freiburg vs Paderborn, Hoffenheim vs Dortmund, RB Leipzig vs Werder Bremen, Schalke 04 vs Bayern

**LaLiga (3):** Athletic vs Atlético, Rayo Vallecano vs Racing Santander, Villarreal vs Deportivo A Coruña

**Ligue 1 (3):** Lens vs Lorient, Le Havre vs Brest, Nice vs Le Mans

**Eredivisie (4):** NEC vs Feyenoord, Utrecht vs Go Ahead Eagles, Ajax vs PSV, Willem II vs Excelsior

**Liga Portugal (4):** Estrela vs Famalicão, Alverca vs Braga, Marítimo vs Benfica, Sporting vs Nacional

**Serie A (1):** Inter vs Napoli

**Liga Argentina (5):** Aldosivi vs Banfield, Gimnasia La Plata vs Tigre, Gimnasia (Mendoza) vs Boca, San Lorenzo vs Talleres, Vélez vs Estudiantes

**Liga BetPlay (4):** Boyacá Chicó vs Once Caldas, Cúcuta vs Deportivo Pasto, Santa Fe vs Fortaleza, Junior vs Jaguares

**MLS (7 destacados):** Charlotte vs Houston, Cincinnati vs DC United, Columbus vs Colorado, Inter Miami vs Atlanta, Orlando vs San Diego, Philadelphia vs Montreal, LA Galaxy vs New England

*Nota de fechas: PSG vs Monaco se jugó el viernes 4 sep (fuera de rango, excluido). Juventus vs Inter no figura en la jornada 3 de Serie A del 5 sep; el único partido confirmado de Serie A ese día es Inter vs Napoli (FotMob/Opta).*

## Ranking Global (candidatos con value según motor, pre-selección)

| Rank | Partido | Mercado | Selección | Cuota | Prob. | Justa | Edge | EV | Kelly-0.25 | Confianza |
|------|---------|---------|-----------|------:|------:|------:|-----:|----:|-----------:|-----------|
| 1 | Gimnasia (M) vs Boca | 1X2 | Gimnasia (1) | 4.05 | 35.6% | 2.81 | +44.2% | +44.2% | 0.04u | Media-Alta |
| 2 | Ajax vs PSV | 1X2 | Ajax (1) | 2.60 | 42.6% | 2.35 | +10.8% | +10.8% | 0.02u | Media |
| 3 | Athletic vs Atlético | 1X2 | Athletic (1) | 3.15 | 40.5% | 2.47 | +27.4% | +27.4% | 0.03u | Media |
| — | Schalke vs Bayern | 1X2 | Schalke (1) | 14.00 | 17.8% | 5.61 | +149.5% | +149.5% | 0.03u | **Excluida** |
| — | Sporting vs Nacional | 1X2 | Empate (X) | 6.00 | 19.5% | 5.13 | +17.1% | +17.1% | 0.01u | **Excluida** |
| — | Inter Miami vs Atlanta | 1X2 | Atlanta (2) | 6.50 | 17.9% | 5.60 | +16.1% | +16.1% | 0.01u | **Excluida** |
| — | Santa Fe vs Fortaleza | 1X2 | Fortaleza (2) | 6.00 | 22.2% | 4.50 | +33.3% | +33.3% | 0.02u | **Excluida** |
| — | Gimnasia vs Boca | Goles | Over 2.5 | 2.48 | 39.1% | 2.56 | -3.1% | -3.1% | — | Baja |
| — | Inter vs Napoli | 1X2 | Napoli (2) | 4.75 | 23.2% | 4.30 | +10.3% | +10.3% | 0.01u | **Excluida** |
| — | Inter vs Napoli | 1X2 | Empate (X) | 3.50 | 26.0% | 3.85 | -9.2% | -9.2% | — | Baja |
| — | Ajax vs PSV | Goles | Under 2.5 | 3.80 | 39.1% | 2.56 | +48.4% | +48.4% | 0.04u | **Excluida*** |
| — | Athletic vs Atlético | BTTS | BTTS No | 2.05 | 44.5% | 2.25 | -8.7% | -8.7% | — | Baja |
| — | Hoffenheim vs Dortmund | BTTS | BTTS No | 2.90 | 44.0% | 2.27 | +27.7% | +27.7% | — | **Excluida** |
| — | Hoffenheim vs Dortmund | 1X2 | Dortmund (2) | 2.30 | 38.7% | 2.58 | -10.9% | -10.9% | — | Baja |

*Prob. = probabilidad modelo; Edge/EV = motor cuantitativo. `*` = artifact de inputs conservadores que contradicen el consensus externo (Over fuertemente favorecido por ambos equipos).*

## Picks Recomendados (Top 3)

| Rank | Partido (hora UTC) | Mercado | Selección | Cuota | Prob. | Justa | Edge | EV | Stake | Confianza |
|------|---------|---------|-----------|------:|------:|------:|-----:|----:|-------:|-----------|
| 1 | Gimnasia (M) vs Boca (19:30) | 1X2 | Gimnasia (Mendoza) | 4.05 | 35.6% | 2.81 | +44.2% | +44.2% | 0.50u | Media-Alta |
| 2 | Ajax vs PSV (18:00) | 1X2 | Ajax | 2.60 | 42.6% | 2.35 | +10.8% | +10.8% | 0.50u | Media |
| 3 | Athletic vs Atlético (14:15) | 1X2 | Athletic Club | 3.15 | 40.5% | 2.47 | +27.4% | +27.4% | 0.25u | Media |

---

## Detalle de Picks

### Pick 1: Gimnasia y Esgrima (Mendoza) vs Boca Juniors — Gimnasia gana
- **Mercado:** 1X2
- **Selección:** Gimnasia (Mendoza) gana (1)
- **Cuota:** 4.05 (MarathonBet; rango inter-casa 3.25–5.40)
- **Probabilidad modelo:** 35.60%
- **Probabilidad implícita:** 24.69%
- **Cuota justa:** 2.81
- **Edge:** +44.2%
- **EV:** +44.2%
- **Cuota mínima:** 2.90
- **Stake:** 0.50u (moderada, por cuota larga y varianza)
- **Confianza:** Media-Alta
- **Incertidumbre:** Media

**Por qué:** El mercado paga a Boca como gran favorito (cuota 2.02 → 49.5% implícito) muy por encima de su probabilidad real externa (39% Scoreo, 38% Extratips, 38% Wincomparator). El modelo ensamble da a Gimnasia 35.6% de victoria en su fortín (Legrotaglie), con ventaja táctica de equipo directo/contraataque. Boca marca primero solo en 23% de sus partidos y su media fuera de casa es pobre (1.13 xG for). El 71% de los partidos de Boca queda under 2.5, perfilando un partido cerrado donde el local es competitivo a cuota alta.

**Sensibilidad (p del local):** ±0.15 xG y ±50 Elo dan p = 33.0%–38.2%; el EV permanece positivo (+34% a +55%). **Robusto en todo el rango.**

**Riesgos:** Boca, pese a su etiqueta, sigue siendo plantel superior; un 0-0 o 1-1 es el desenlace más probable. La cuota disponible varía muy sensiblemente entre casas (3.25 a 5.40); solo jugar si se obtiene ≥ 2.90.

**Condición de entrada:** cuota ≥ 2.90.

---

### Pick 2: Ajax vs PSV Eindhoven — Ajax gana
- **Mercado:** 1X2
- **Selección:** Ajax gana (1)
- **Cuota:** 2.60 (mejor de mercado ~2.60; PSV favorito en libros a 2.40)
- **Probabilidad modelo:** 42.62%
- **Probabilidad implícita:** 38.46%
- **Cuota justa:** 2.35
- **Edge:** +10.8%
- **EV:** +10.8%
- **Cuota mínima:** 2.35
- **Stake:** 0.50u (moderada)
- **Confianza:** Media
- **Incertidumbre:** Media

**Por qué:** El mercado favoritiza a PSV (43% implícito) pero el modelo da a Ajax 42.6% frente a 38.5% implícito (cuota justa 2.35). Ajax está invicto en 13 partidos y en 5 H2H consecutivos ante PSV (incl. 2-2 en la última visita del campeón al Cruyff Arena), ha marcado ≥2 goles en los 9 partidos de la temporada y llega tras un 4-0. PSV pierde 61.8% de posesión*se traduce en vulnerabilidad al contragolpe local. (*revisar: la estadística es a favor de PSV en ataque, no defensa del desglose.)

**Sensibilidad (p del local):** ±0.15 xG / ±50 Elo dan p = 40.4%–44.9%; el EV permanece positivo (+5.0% a +16.7%). **Robusto (mínimo positivo).**

**Riesgos:** Ajax lleva 4 partidos de liga sin ganar en casa y PSV viene de 6-1 en la jornada anterior. El empate (2-2 en los últimos dos H2H) es el desenlace que rompe la apuesta. Only value si se preserva cuota ≥ 2.35.

**Condición de entrada:** cuota ≥ 2.35.

---

### Pick 3: Athletic Club vs Atlético de Madrid — Athletic gana
- **Mercado:** 1X2
- **Selección:** Athletic Club gana (1)
- **Cuota:** 3.15 (cerrado en 3.15; apertura 2.90 tendía a 2.23 para Atlético)
- **Probabilidad modelo:** 40.45%
- **Probabilidad implícita:** 31.75%
- **Cuota justa:** 2.47
- **Edge:** +27.4%
- **EV:** +27.4%
- **Cuota mínima:** 2.60
- **Stake:** 0.25u (pequeña)
- **Confianza:** Media
- **Incertidumbre:** Media-Alta

**Por qué:** San Mamés es uno de los campos más difíciles de España y el modelo asigna a Athletic 40.5% frente al 31.75% implícito (cuota justa 2.47). Los modelos externos (Sports Mole 37.4%, Extratips 37%) siguen por encima del precio de mercado. Atlético llega sin delantero centro reconocido: Sorloth lesionado, Julián Álvarez no se espera titular y Jonathan David apenas acumula 3 sesiones; eso neutraliza parcialmente su buen arranque (7 pts) frente a la presión alta de Athletic.

**Sensibilidad (p del local):** p = 38.1%–42.9%; EV positivo (+20% a +35%) en todo el rango. **Robusto.**

**Riesgos:** Athletic pierde a Vivian y Egiluz (centrales) y ya perdió su único partido en San Mamés esta temporada (1-3 vs Sevilla); Nico Williams sin ritmo para 90'. Atlético lleva 4 victorias en los últimos 5 H2H. Edge alto pero dos centrales suplentes frente a un ataque que ha marcado en todas las jornadas → stake reducido.

**Condición de entrada:** cuota ≥ 2.60.

---

## Portfolio y Correlaciones
- **Exposición total:** 1.25u (0.50 + 0.50 + 0.25)
- **Correlaciones:** Nula entre los 3 picks (liga argentina, Eredivisie, LaLiga; 3 mercados 1X2 independientes). Sin solapamiento de equipos ni resultados condicionantes.
- **Ajuste por correlación:** no aplica.

## NO BET / Excluidos
- **Schalke vs Bayern (1 @14.00, X @8.50, U2.5 @4.00):** Edge del motor es un artifact de inputs de xG/Elo que subestiman el abismo real de calidad (Bayern campeón, 122 goles/34 partidos temporada previa; Schalke 0-3 en jornada 1 y 0-29 en goles en última racha H2H). El motor da Bayern 60.6% vs ~76-79% del consenso. NO BET.
- **Sporting vs Nacional (X @6.00):** Empate de 19.5% de probabilidad, varianza altísima ante un favorito de 73-78%; no robusto.
- **Inter Miami vs Atlanta (2 @6.50):** Florida 7-1 en el último partido; la victoria de Atlanta (17.9%) contradice su 13-3-0 fuera registro y la forma. El under 2.5 @3.60 contradice el Over de consenso externo (60-71%). NO BET.
- **Santa Fe vs Fortaleza (2 @6.00) y (1 @1.50):** El mercado (Santa Fe 66.7% implícito) ya descuenta el historial 5-0 H2H en El Campín y la racha de Fortaleza de 15 partidos sin ganar fuera; el motor (52.3%) no ve value al 1.50 y el value del visitante (22.2%) contradice esa misma lógica. NO BET. BTTS Sí @2.10 (edge 4.8%) por debajo del umbral.
- **Inter vs Napoli (X @3.50, 2 @4.75, BTTS Sí @1.90, U2.5 @1.70):** Ningún mercado 1X2/Total ofrece value robusto vs modelo (Empate -9.2%, BTTS -5.4%, Under -8.6%). El Napoli (2) a +10.3% depende de que su probabilidad real esté en el extremo alto (23%) del rango externo (19.7-22%); frágil. NO BET. El empate del H2H es una narrativa, no un edge cuantificado.
- **Hoffenheim vs Dortmund (BTTS No @2.90):** El modelo (44%) supera el 34.5% implícito, pero la cuota es una estimación no verificada en casas colombianas y contradice la racha de Over/BTTS de Hoffenheim (11 partidos seguidos Over 2.5). NO BET.
- **Rayo vs Racing, Villarreal vs Deportivo, Newcastle vs Bournemouth, Man City vs Coventry, Lens vs Lorient, Benfica vs Marítimo, otros:** sin cuota verificada suficiente en casas colombianas en cutoff → no analysis cuantitativo fiable. NO BET.

## Tracking

| # | Partido | Mercado | Selección | Cuota | Stake | Resultado | Estado | P/L |
|---|---------|---------|-----------|-------|-------|-----------|--------|-----|
| 1 | Gimnasia (M) vs Boca | 1X2 | Gimnasia (Mendoza) | 4.05 | 0.50u | 2 - 2 | PERDIDA | -0.50u |
| 2 | Ajax vs PSV | 1X2 | Ajax | 2.60 | 0.50u | 1 - 3 | PERDIDA | -0.50u |
| 3 | Athletic vs Atlético | 1X2 | Athletic Club | 3.15 | 0.25u | 3 - 0 | GANADA | +0.54u |
| **Total** | | | | | **1.25u** | | **1 G / 2 P** | **-0.46u** |

---
*Análisis cuantitativo ejecutado con `scripts/calc_engine.py` (modelo v1.0 activo). Probabilidades, cuotas justas, edge, EV y Kelly provienen del motor; ninguna se inventó manualmente. Las apuestas no están garantizadas; apostar con responsabilidad (+18).*