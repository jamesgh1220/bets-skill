---
name: football-betting-review
description: Revisa apuestas históricas buscando resultados automáticamente, calculando P/L, ROI, CLV, EV, drawdown y rendimiento segmentado.
---

# Football Betting Review

## Fuentes de Datos

La skill carga predicciones desde los artefactos generados por `football-betting-analysis`:

- **Directorio:** `artifacts/`
- **Patrón de archivos:** `analisis-{dia}-{mes}-{año}.md`
- **Formato:** Markdown con secciones Metadatos, Picks Recomendados (tabla), Detalle de Picks, Portfolio y Tracking.

## Flujo Automatizado (Sin Input Manual)

```
1. Leer todos los artefactos artifacts/analisis-*.md
2. Identificar picks con estado PENDIENTE
3. Para cada pick PENDIENTE:
   a. Verificar si la fecha del partido ya pasó
   b. Si ya jugó → buscar resultado automáticamente via web search
   c. Determinar GANADA/PERDIDA/PUSH/VOID según mercado
   d. Calcular profit
   e. Actualizar artefacto con resultado
4. Calcular métricas de rendimiento globales
5. Mostrar reporte completo
```

## Paso 1: Cargar Artefactos

Leer todos los archivos `artifacts/analisis-*.md`:

1. Extraer metadatos: fecha de análisis, ligas, rango de fechas
2. Extraer picks de la tabla: Rank, Partido, Mercado, Selección, Cuota, Stake, Estado
3. Extraer detalle de picks: datos completos
4. Identificar picks con estado `PENDIENTE`

## Paso 2: Verificar Fechas

Para cada pick PENDIENTE:

1. Extraer fecha del partido del artefacto o del nombre del archivo
2. Comparar con fecha actual
3. **Si fecha_partido > fecha_actual** → Partido no jugado aún, mantener PENDIENTE
4. **Si fecha_partido <= fecha_actual** → Partido ya jugado, buscar resultado

## Paso 3: Buscar Resultados Automáticamente

Usar `websearch` para buscar resultados de cada partido:

### Formatos de Búsqueda

```
"[Equipo Local] vs [Equipo Visitante] resultado [fecha]"
"[Equipo Local] [Equipo Visitante] score [fecha]"
"[Liga] [Equipo Local] vs [Equipo Visitante] resultado"
```

### Parsing del Resultado

Del resultado de la búsqueda, extraer:

1. **Goles del local**: {home_goals}
2. **Goles del visitante**: {away_goals}
3. **Ganador**: Local / Visitante / Empate

### Cruce con Mercado del Pick

| Mercado | Regla de GANADA |
|---------|-----------------|
| **1X2** | Selección = resultado (Local gana si pick = Home, etc.) |
| **Over 2.5** | goles_totales > 2.5 |
| **Under 2.5** | goles_totales < 2.5 |
| **BTTS** | Ambos equipos marcaron (home_goals > 0 AND away_goals > 0) |
| **Double Chance 1X** | Local gana o empata |
| **Double Chance X2** | Visitante gana o empata |
| **Double Chance 12** | No hay empate |
| **Asian Handicap** | Según handicap aplicado |
| **Team Totals** | Goles del equipo vs línea |

### Determinar Estado

- **GANADA**: Regla del mercado se cumple
- **PERDIDA**: Regla del mercado no se cumple
- **PUSH**: Empate en mercados con línea (Asian Handicap,某些 totals)
- **VOID**: Partido cancelado, aplazado o sin datos

## Paso 4: Calcular Profit

Para cada pick con resultado:

```
Si GANADA: profit = stake × (cuota - 1)
Si PERDIDA: profit = -stake
Si PUSH: profit = 0
Si VOID: profit = 0
```

## Paso 5: Actualizar Artefacto

Para cada pick actualizado, modificar el artefacto:

1. Cambiar estado de `PENDIENTE` a `GANADA`/`PERDIDA`/`PUSH`/`VOID`
2. Agregar campo `Resultado: [goles_local] - [goles_visitante]`
3. Agregar campo `Profit: {profit}u`
4. Agregar campo `P/L Acumulado: {acumulado}u`

## Paso 6: Calcular Métricas

Una vez todos los picks tengan resultado:

| Métrica | Fórmula/Descripción |
|---------|---------------------|
| **N** | Total de picks analizados |
| **Stake total** | Suma de todos los stakes |
| **Profit** | Ganancia neta en unidades |
| **ROI** | Profit / Stake total × 100 |
| **Yield** | Profit / N |
| **Win rate** | Picks ganados / N × 100 |
| **Odds media** | Promedio de cuotas |
| **EV medio** | Promedio de EV |
| **CLV** | Closing Line Value (si hay datos de cierre) |
| **Max drawdown** | Mayor caída acumulada |

## Paso 7: Segmentación

Analizar rendimiento por:

- **Liga**: rendimiento por competición
- **Mercado**: 1X2, O/U, BTTS, etc.
- **Rango de cuotas**: picks de cuota baja vs alta
- **Rango de stake**: picks pequeños vs grandes
- **Confianza**: low vs medium vs high
- **Período**: por semana/mes

## Paso 8: Análisis Adicional

### Calibración
- Comparar probabilidad modelo vs win rate observado por tramos
- Calcular Brier Score y Log Loss si hay muestras suficientes

### Drawdown y Rachas
- Calcular máxima racha negativa
- Identificar rachas ganadoras/perdedoras
- Separar varianza de evidencia real

## Formato de Salida

### Resumen General

```
=== RESUMEN DE RENDIMIENTO ===
Período: {fecha_inicio} - {fecha_fin}
N picks: {N}
Stake total: {stake}u
Profit: {profit}u
ROI: {roi}%
Yield: {yield}
Win rate: {win_rate}%
Odds media: {odds}
EV medio: {ev}
Max drawdown: {drawdown}u
```

### Tabla de Historial

| Fecha | Partido | Mercado | Selección | Cuota | Stake | Resultado | Profit | P/L Acum. |
|-------|---------|---------|-----------|-------|-------|-----------|--------|-----------|

### Segmentación por Liga

| Liga | N | Win Rate | ROI | Yield |
|------|---|----------|-----|-------|

### Segmentación por Mercado

| Mercado | N | Win Rate | ROI | Yield |
|---------|---|----------|-----|-------|

### Picks Pendientes (no actualizados)

Si hay picks que no se pudieron actualizar (partidos futuros o sin datos):

| Partido | Mercado | Selección | Fecha | Estado |
|---------|---------|-----------|-------|--------|

### Conclusiones

- Calidad de predicción vs precio pagado
- Sesgos detectados
- Recomendaciones para ajustar el modelo

Consultar `references/result-fetching.md` y `evaluation-framework.md`.
