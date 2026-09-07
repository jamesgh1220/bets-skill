# Football Betting Intelligence System

Sistema cuantitativo para análisis de apuestas de fútbol, búsqueda de value y evaluación del modelo.

## Arquitectura

### Directorios

- `AGENTS.md` — Reglas globales del sistema
- `.agents/skills/` — Skills especializadas (4 skills)
- `.agents/commands/` — Comandos de invocación
- `schemas/` — Contratos JSON para datos
- `artifacts/` — Análisis generados (histórico)
- `models/` — Versiones del modelo predictivo

---

## Skills

### 1. football-betting-analysis

**Qué hace:** Analiza partidos prepartido, estima probabilidades, compara cuotas, calcula value y asigna stake.

**Invocación:**

```
/football-betting-analysis ligas:[lista] fechas:[fecha/rango] partidos:[lista/todos] modelo:[id]
```

**Parámetros:**

- `ligas` (requerido): Lista de ligas separadas por comas
- `fechas` (requerido): Fecha única o rango de fechas
- `partidos` (requerido): `todos` o lista de partidos específicos
- `modelo` (requerido): identificador de la IA que ejecuta la corrida

**Ejemplos:**

```
/football-betting-analysis ligas:Premier League, LaLiga fechas:5 de septiembre de 2026 partidos:todos modelo:gpt-5
/football-betting-analysis ligas:Serie A fechas:5-7 septiembre 2026 partidos:Juventus vs Inter modelo:claude-sonnet
```

**Salida:**

- Ranking completo de candidatos con value
- Selección final de **0-6 picks más óptimos**
- Artefacto validado `artifacts/analisis-YYYY-MM-DD--{modelo-ia}--vNN.md`

---

### 2. football-betting-review

**Qué hace:** Revisa rendimiento histórico leyendo artefactos, cruzando con resultados y calculando métricas.

**Invocación:**

```
/football-review
```

**Métricas:** ROI, Yield, Win rate, CLV, Max drawdown, Calibración

**Segmentación:** Liga, mercado, cuota, stake, confianza, período

---

### 3. football-model-evaluation

**Qué hace:** Evalúa calidad estadística del modelo. **NUNCA modifica el modelo.**

**Invocación:**

```
/football-model
```

**Métricas:** Brier Score, Log Loss, Calibration Error, ROC AUC, PSI

**Análisis:** Calibración por tramos, sobreajuste, sensibilidad, estabilidad temporal, CLV

**Salida:** Diagnóstico completo con recomendaciones para refinement

---

### 4. football-model-refinement (NUEVA)

**Qué hace:** Refina el modelo de forma controlada con backtesting y versionado.

**Invocación:**

```
/football-refinement
```

**Proceso:**

1. Lee diagnóstico de `football-model-evaluation`
2. Busca datos históricos automáticamente
3. Propone cambios controlados
4. Ejecuta backtesting out-of-sample
5. Espera aprobación del usuario
6. Si aprueba: crea nueva versión en `models/`

**Tipos de cambios:**

- Pesos de componentes (Poisson, DC, Ratings, Regression)
- Pesos de features (offensive, defensive, contextual, form, player)
- Umbrales de decisión (min_edge, min_confidence)
- Calibración de mercados
- Remoción/adición de features
- Toggle de componentes

**Reglas:**

- Nunca modificar sin aprobación explícita
- Nunca saltar backtesting
- Nunca sobrescribir versiones
- Un cambio a la vez
- Documentar todo

---

## Orden de Ejecución (Ciclo Completo)

```
1. /football-betting-analysis  →  picks + artifacts/
2. (Esperar resultados)
3. /football-review            →  métricas de rendimiento
4. /football-model             →  diagnóstico (nunca modifica)
5. /football-refinement        →  propuesta → backtesting → aprobación → versión
6. (Volver al paso 1 con nueva versión)
```

---

## Ejemplo Práctico Completo

### Día 25 de Agosto — Generas Apuestas

Ejecutas: `/football-betting-analysis ligas:Premier League, LaLiga fechas:25-27 agosto partidos:todos modelo:gpt-5`

Resultado:
- 12 candidatos con value
- Selección final: 4 picks
- Artefacto: `artifacts/analisis-2026-08-25--gpt-5--v01.md`

Picks generados:
1. Arsenal vs Chelsea → Over 2.5 → Cuota 1.90 → 0.50u
2. Barcelona vs Sevilla → 1X2 Barcelona → Cuota 1.75 → 0.75u
3. Man City vs Liverpool → BTTS Yes → Cuota 1.85 → 0.50u
4. Real Madrid vs Atletico → Under 2.5 → Cuota 2.10 → 0.25u

Estado: Todos PENDIENTE

### Día 27 de Agosto — Actualizas Resultados

Ejecutas: `/football-review`

La skill automáticamente:
- Lee `artifacts/analisis-2026-08-25--gpt-5--v01.md` dentro de la serie `gpt-5 + model-v1.0`
- Busca resultados de los 4 partidos via web search
- Actualiza cada pick:
  - Arsenal 3-1 Chelsea → Over 2.5 → GANADA (+0.45u)
  - Barcelona 2-0 Sevilla → 1X2 Barcelona → GANADA (+0.56u)
  - Man City 2-2 Liverpool → BTTS Yes → GANADA (+0.43u)
  - Real Madrid 1-0 Atletico → Under 2.5 → PERDIDA (-0.25u)
- Calcula métricas: N=4, Stake=2.00u, Profit=+1.19u, ROI=+59.5%, Win rate=75%
- Actualiza artefacto con resultados
- Muestra reporte completo

### Día 3 de Septiembre — Evalúas el Modelo

Ejecutas: `/football-model`

La skill lee `artifacts/` (varios análisis acumulados) y calcula:
- Brier Score: 0.184
- Log Loss: 0.408
- Calibration Error: 0.023
- CLV promedio: +0.018

Diagnóstico:
- Modelo calibrado correctamente
- CLV positivo (mejor que el mercado)
- Over/Under 2.5 subestima en tramos 0.4-0.6
- Sin sobreajuste detectado

Recomendaciones:
1. Recalibrar tramos de Over/Under 2.5
2. Ajustar pesos: DC > Poisson en este tipo de mercados

### Día 3 de Septiembre — Refinas el Modelo

Ejecutas: `/football-refinement`

La skill:
1. Lee diagnóstico de `/football-model`
2. Busca datos históricos de Over/Under 2.5
3. Propone cambios:
   - Recalibrar tramos de Over/Under 2.5
   - Ajustar peso de DC: 0.30 → 0.35
   - Ajustar peso de Poisson: 0.35 → 0.30
4. Ejecuta backtesting out-of-sample:
   - Brier anterior: 0.191
   - Brier propuesto: 0.184
   - Mejora: -0.007
5. Espera tu aprobación: "¿Apruebas estos cambios?"
6. Si apruebas:
   - Crea `models/model-v1.1.json`
   - Actualiza `models/changelog.md`
   - Estado: v1.0 → deprecated, v1.1 → active

### Día 4 de Septiembre — Vuelves a Generar Apuestas

Ejecutas: `/football-betting-analysis ligas:Premier League fechas:4 septiembre partidos:todos`

Ahora usa `model-v1.1.json` (versión refinada) y genera nuevos picks con mejor calibración.

### Resumen en Una Línea por Skill

| Skill | Acción |
|-------|--------|
| `/football-betting-analysis ligas:... fechas:... partidos:...` | Genera 0-6 picks + artefacto |
| `/football-review` | Busca resultados automáticamente + calcula métricas |
| `/football-model` | Evalúa calidad del modelo (nunca modifica) |
| `/football-refinement` | Propone cambios → backtesting → tu apruebas → nueva versión |

---

## Sistema de Versionado

**Ubicación:** `models/`

```
models/
├── model-v1.0.json     ← Versión inicial (active)
├── model-v1.1.json     ← Refinamientos menores
├── model-v2.0.json     ← Cambios arquitectónicos
└── changelog.md        ← Historial de cambios
```

**Convención:**

- `v1.0 → v2.0`: Cambios mayores (arquitectura)
- `v1.0 → v1.1`: Cambios menores (pesos, umbrales)
- Solo UNA versión `active` a la vez
- Versiones anteriores → `deprecated`

---

## Schemas (Contratos JSON)

| Schema | Uso |
|--------|-----|
| `match.schema.json` | Datos de partido |
| `odds.schema.json` | Cuotas por bookmaker |
| `prediction.schema.json` | Predicciones del modelo |
| `result.schema.json` | Resultados y P/L |
| `source.schema.json` | Fuentes de información |

---

## Reglas Clave (AGENTS.md)

- Verificar actualidad antes de cada predicción
- Respetar rango de fechas estrictamente
- Máximo 6 picks finales
- Generar artefacto `.md` en `artifacts/` con cada análisis
- Stake en unidades; nunca martingala
- `NO BET` es válido
- Nunca presentar apuestas como seguras
- Nunca modificar modelo sin aprobación
- Nunca saltar backtesting
- Nunca sobrescribir versiones
