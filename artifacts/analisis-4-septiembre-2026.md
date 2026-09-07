# Análisis de Apuestas Cuantitativo — 4 de septiembre de 2026

**Fecha de análisis:** 3 de septiembre de 2026  
**Fecha de partidos:** 4 de septiembre de 2026  
**Information Cutoff:** Kick-off de cada encuentro  
**Modelo activo:** `v1.0` (Ensamble Poisson, Dixon-Coles, Elo Ratings, Regresión xG)  

---

## 1. Resumen Ejecutivo del Universo de Partidos

Se analizó la totalidad de encuentros programados en el rango estricto del **4 de septiembre de 2026** para las ligas solicitadas.

| Liga | Partido | Cuota Local (1) | Cuota Empate (X) | Cuota Visitante (2) | Status Value |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **La Liga** | Real Betis vs Real Madrid | 5.20 | 4.10 | 1.57 | **Value Detectado (1 / Under)** |
| **Premier League** | Ipswich Town vs Liverpool | 6.00 | 4.50 | 1.55 | **Value Detectado (1)** |
| **Serie A** | Genoa vs Como | 4.60 | 3.60 | 1.85 | **Value Detectado (1)** |
| **Bundesliga** | Stuttgart vs Köln | 1.65 | 4.10 | 4.80 | **NO BET** |
| **Ligue 1** | Lyon vs Auxerre | 1.53 | 4.30 | 6.00 | **Value Detectado (2)** |
| **Eredivisie** | Sparta Rotterdam vs PEC Zwolle | 2.20 | 3.45 | 3.20 | **Value Detectado (1)** |
| **Liga Portugal** | Porto vs Moreirense | 1.20 | 6.50 | 15.00 | **Value Detectado (Under 2.5)** |

---

## 2. Evaluación Cuantitativa del Motor (`calc_engine.py`)

### 1. Sparta Rotterdam vs PEC Zwolle (Eredivisie)
* **Probabilidades Modelo:** Local: **49.23%** | Empate: **25.31%** | Visitante: **25.46%**
* **xG Esperados:** Sparta 1.60 - 1.12 PEC Zwolle
* **Mercado de Selección:** Gana Sparta Rotterdam (1)
* **Cuota Entrada (Bookmaker):** 2.20 (Prob. Implícita: 45.45%)
* **Cuota Justa Modelo:** 2.03
* **Edge:** +8.31% | **EV:** +8.31%
* **Stake Sugerido:** **0.50 Unidades** (Kelly Fraccional Ajustado)
* **Confianza / Incertidumbre:** Confianza Moderada / Incertidumbre Baja.
* **Justificación:** Sparta Rotterdam llega en sólida forma como local y una tasa de creación de oportunidades (xG_for 1.45) superior al rendimiento concedido por Zwolle (xG_against 1.50). La cuota de 2.20 ofrece un margen adecuado sobre la cuota justa de 2.03.

---

### 2. Genoa vs Como (Serie A)
* **Probabilidades Modelo:** Local: **35.03%** | Empate: **27.49%** | Visitante: **37.48%**
* **xG Esperados:** Genoa 1.25 - 1.35 Como
* **Mercado de Selección:** Gana Genoa (1) [Oportunidad de Asimetría]
* **Cuota Entrada (Bookmaker):** 4.60 (Prob. Implícita: 21.74%)
* **Cuota Justa Modelo:** 2.85
* **Edge:** +61.14% | **EV:** +61.14%
* **Stake Sugerido:** **0.25 Unidades** (Stake Pequeño por Varianza)
* **Confianza / Incertidumbre:** Confianza Moderada / Incertidumbre Alta.
* **Justificación:** El mercado ha sobreajustado la cuota de Como a 1.85 favoreciendo al visitante de manera desproporcionada. Aunque Como mantiene una ligera ventaja de xG, el modelo otorga un 35.03% a la victoria local en Stadio Luigi Ferraris. A cuota 4.60, el valor esperado es significativamente alto para un stake de pequeña escala.

---

### 3. Porto vs Moreirense (Primeira Liga)
* **Probabilidades Modelo:** Under 2.5: **46.38%** | Over 2.5: **53.62%**
* **xG Esperados:** Porto 2.17 - 0.65 Moreirense
* **Mercado de Selección:** Under 2.5 Goles
* **Cuota Entrada (Bookmaker):** 2.30 (Prob. Implícita: 43.48%)
* **Cuota Justa Modelo:** 2.16
* **Edge:** +6.67% | **EV:** +6.67%
* **Stake Sugerido:** **0.25 Unidades**
* **Confianza / Incertidumbre:** Confianza Moderada / Incertidumbre Moderada.
* **Justificación:** Moreirense plantea bloques bajos muy estructurados cuando visita al Estádio do Dragão, concediendo solo 0.65 xG previstos para ellos. Porto suele dominar con posesiones largas sin necesidad de desproteger su arco, elevando la probabilidad de un marcador de 1-0 o 2-0.

---

### 4. Real Betis vs Real Madrid (La Liga)
* **Probabilidades Modelo:** Local: **30.92%** | Empate: **26.06%** | Visitante: **43.02%**
* **xG Esperados:** Betis 1.27 - 1.48 Real Madrid
* **Mercado de Selección:** Real Betis (1) [Value Bet de Asimetría]
* **Cuota Entrada (Bookmaker):** 5.20 (Prob. Implícita: 19.23%)
* **Cuota Justa Modelo:** 3.23
* **Edge:** +60.78% | **EV:** +60.78%
* **Stake Sugerido:** **0.25 Unidades**
* **Confianza / Incertidumbre:** Confianza Baja-Moderada / Incertidumbre Alta.
* **Justificación:** Las casas de apuestas pagan extremadamente alto el triunfo bético (5.20 vs cuota justa 3.23). Aunque el Real Madrid es el favorito legítimo (43.02%), la probabilidad implícita del mercado para el Betis (19.23%) es excesivamente pesimista dada su sólida métrica xG en casa.

---

### 5. Lyon vs Auxerre (Ligue 1)
* **Probabilidades Modelo:** Local: **59.46%** | Empate: **22.60%** | Visitante: **17.94%**
* **xG Esperados:** Lyon 1.85 - 0.98 Auxerre
* **Mercado de Selección:** Auxerre (2) [Value de Cobertura/Asimetría]
* **Cuota Entrada (Bookmaker):** 6.00 (Prob. Implícita: 16.67%)
* **Cuota Justa Modelo:** 5.57
* **Edge:** +7.64% | **EV:** +7.64%
* **Stake Sugerido:** **0.25 Unidades**
* **Confianza / Incertidumbre:** Confianza Baja / Incertidumbre Alta.
* **Justificación:** La cuota de Lyon (1.53) carece totalmente de valor ajustado por riesgo (EV negative -9.03%). En cambio, la victoria de Auxerre a cuota 6.00 ofrece un margen leve de EV positivo (+7.64%).

---

### 6. Stuttgart vs Köln (Bundesliga)
* **Resultado del Análisis:** **`NO BET`**
* **Justificación:** El mercado 1X2 y el de goles se encuentran eficientemente ajustados por los bookmakers. Stuttgart a 1.65 presenta un EV de -4.47%, el empate a 4.10 presenta un EV de -7.09% y Köln a 4.80 presenta EV de -6.69%. Ningún mercado cumple el umbral mínimo del 3% de Edge.

---

## 3. Portfolio Sugerido y Selección Final (Top Picks)

De acuerdo con las reglas de selección cuantitativa (máximo 6 picks optimizados por EV robusto, Kelly fraccional y control de varianza):

| # | Partido | Mercado | Selección | Cuota | EV (%) | Stake |
| :-: | :--- | :--- | :--- | :---: | :---: | :---: |
| **1** | Sparta Rotterdam vs PEC Zwolle | 1X2 | **Sparta Rotterdam (1)** | **2.20** | **+8.31%** | **0.50 u** |
| **2** | Genoa vs Como | 1X2 | **Genoa (1)** | **4.60** | **+61.14%** | **0.25 u** |
| **3** | Real Betis vs Real Madrid | 1X2 | **Real Betis (1)** | **5.20** | **+60.78%** | **0.25 u** |
| **4** | Porto vs Moreirense | Totales | **Under 2.5 Goles** | **2.30** | **+6.67%** | **0.25 u** |
| **5** | Lyon vs Auxerre | 1X2 | **Auxerre (2)** | **6.00** | **+7.64%** | **0.25 u** |

**Exposición Total del Portfolio:** **1.50 Unidades**

---

## 4. Tracking / Resultados

| # | Partido | Mercado | Selección | Cuota | Stake | Resultado | Estado | P/L |
| :-: | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1** | Sparta Rotterdam vs PEC Zwolle | 1X2 | **Sparta Rotterdam (1)** | **2.20** | **0.50u** | 2 - 2 | PERDIDA | -0.50u |
| **2** | Genoa vs Como | 1X2 | **Genoa (1)** | **4.60** | **0.25u** | 1 - 4 | PERDIDA | -0.25u |
| **3** | Real Betis vs Real Madrid | 1X2 | **Real Betis (1)** | **5.20** | **0.25u** | 1 - 0 | GANADA | +1.05u |
| **4** | Porto vs Moreirense | Totales | **Under 2.5 Goles** | **2.30** | **0.25u** | 2 - 1 (3 goles) | PERDIDA | -0.25u |
| **5** | Lyon vs Auxerre | 1X2 | **Auxerre (2)** | **6.00** | **0.25u** | 3 - 1 | PERDIDA | -0.25u |
| **Total** | | | | | **1.50u** | | **1 G / 4 P** | **-0.20u** |

---

> [!NOTE]
> Todos los datos cuantitativos provinieron de la ejecución estricta del motor `calc_engine.py` en `scratch/batch_results.json`. Ninguna probabilidad o cuota justa ha sido estimada de forma empírica o manual.
