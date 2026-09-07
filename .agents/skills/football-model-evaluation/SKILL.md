---
name: football-model-evaluation
description: Evalúa calidad estadística mediante calibración, Brier, Log Loss, CLV, sensibilidad, estabilidad y sobreajuste.
---

# Football Model Evaluation

## Propósito

Diagnosticar la calidad del modelo predictivo. **NUNCA modificar el modelo directamente.**

La skill `football-model-refinement` toma el diagnóstico y propone cambios controlados.

## Fuentes de Datos

- **Artefactos**: `artifacts/analisis-*.md` (picks generados por analysis, agrupados por modelo de IA y versión de motor)
- **Modelo actual**: `models/model-v{X}.{Y}.json` (configuración activa)
- **Resultados**: Proporcionados por el usuario o desde archivos externos

## Proceso de Evaluación

### Paso 1: Cargar Datos

1. Leer modelo actual desde `models/` (versión con estado `active`)
2. Cargar artefactos de predicciones desde `artifacts/` y formar series independientes `modelo-ia + versión-motor`; los legacy se mantienen como `legacy-unknown`
3. Cargar o solicitar resultados reales (GANADA/PERDIDA/PUSH/VOID)
4. Construir un dataset de predicciones vs resultados por serie, nunca un agregado que mezcle modelos de IA

### Paso 2: Métricas de Calidad

Calcular para cada mercado habilitado:

| Métrica | Fórmula | Interpretación |
|---------|---------|----------------|
| **Brier Score** | `mean((p-y)²)` | Menor es mejor (0 = perfecto) |
| **Log Loss** | `-mean(y·log(p)+(1-y)·log(1-p))` | Menor es mejor |
| **Calibration Error** | `observed_rate - mean_predicted_probability` | Cerca de 0 = calibrado |
| **ROC AUC** | Área bajo curva ROC | Mayor es mejor (>0.7 bueno) |
| **PSI** | Population Stability Index | <0.1 estable, >0.2 cambio significativo |

### Paso 3: Calibración por Tramos

Para cada mercado, analizar calibración en tramos:

1. Agrupar predicciones por tramo de probabilidad (ej: 0.2-0.3, 0.3-0.4, etc.)
2. Calcular win rate observado vs probabilidad predicha por tramo
3. Identificar tramos con desviación significativa (>5%)
4. Generar gráfico de calibración conceptual

Ver `references/calibration.md` para metodología detallada.

### Paso 4: Detección de Sobreajuste

1. Dividir datos en train (70%) y test (30%) por tiempo
2. Calcular métricas en ambos conjuntos
3. Si train >> test → sobreajuste
4. Analizar learning curves si hay suficientes datos
5. Verificar estabilidad temporal de métricas

Ver `references/overfitting.md` para detección detallada.

### Paso 5: Análisis de Sensibilidad

Para cada parámetro clave del modelo:

1. Variar ±10%, ±20%
2. Medir impacto en Brier, calibration error, ROI
3. Identificar parámetros sensibles vs estables
4. Documentar rangos aceptables

### Paso 6: Estabilidad Temporal

1. Dividir datos en períodos (mensual, trimestral)
2. Calcular métricas por período
3. Detectar tendencias (mejora/ deterioro)
4. Identificar estacionalidad o cambios estructurales

### Paso 7: CLV (Closing Line Value)

1. Comparar cuota tomada vs cuota de cierre
2. Calcular CLV promedio y por mercado
3. CLV positivo = modelo es mejor que el mercado
4. CLV negativo = modelo está por debajo del mercado

### Paso 8: Comparación con Versión Anterior

Si existe versión anterior en `models/`:

1. Cargar métricas de versión anterior
2. Comparar todas las métricas
3. Identificar deterioros y mejoras
4. Documentar cambios significativos

### Paso 9: Diagnóstico Final

Generar reporte con:

```
=== DIAGNÓSTICO DEL MODELO ===
Versión: {version}
Modelo de IA: {modelo_ia}
Período evaluado: {inicio} - {fin}
N predicciones: {N}

--- Calidad General ---
Brier Score: {brier} (anterior: {prev})
Log Loss: {log_loss} (anterior: {prev})
Calibration Error: {cal_error} (anterior: {prev})
ROC AUC: {auc} (anterior: {prev})

--- Calibración ---
Mercados bien calibrados: {lista}
Mercados con problemas: {lista}
Tramos con desviación: {lista}

--- Sobreajuste ---
Train Brier: {train_brier}
Test Brier: {test_brier}
Ratio train/test: {ratio}
Diagnóstico: {ok/sobreajuste/underfit}

--- CLV ---
CLV promedio: {clv}
CLV positivo: {pct}%
Mejores mercados: {lista}
Peores mercados: {lista}

--- Estabilidad ---
Tendencia: {estable/mejora/deterioro}
Períodos problemáticos: {lista}

--- Recomendaciones ---
1. {recomendación}
2. {recomendación}
3. {recomendación}
```

## Reglas Críticas

- **NUNCA modificar el modelo directamente.** Solo diagnosticar.
- **Siempre informar N.** No sacar conclusiones con N < 30.
- **Comparar con versión anterior** cuando exista.
- **Separar calidad de predicción de precio pagado.**
- **No confundir suerte con skill** en muestras pequeñas.
- **Generar recomendaciones accionables** para `football-model-refinement`.
- **Series aisladas:** Mostrar las métricas de cada combinación de modelo de IA y motor por separado. No comparar ni combinar series distintas como si fueran una sola muestra.
- **Ambigüedad:** Si no se puede identificar una serie concreta para una recomendación accionable, limitarse a reportar diagnóstico descriptivo y solicitar el modelo/versión objetivo antes de refinement.

Consultar `references/metrics.md`, `calibration.md` y `overfitting.md`.
