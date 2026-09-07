# Overfitting Detection Protocol

## Qué es el Sobreajuste

El modelo aprende ruido del conjunto de entrenamiento en lugar de patrones reales, resultando en buen rendimiento en training pero pobre en datos nuevos.

## Detección

### Método 1: Train/Test Split Temporal

**Importante**: Usar split POR TIEMPO, no aleatorio. Los datos futuros nunca deben estar en training.

```
Datos históricos: 2024-08-01 a 2026-07-31
├── Train: 2024-08-01 a 2026-01-31 (70%)
└── Test:  2026-02-01 a 2026-07-31 (30%)
```

Calcular métricas en ambos:

| Métrica | Train | Test | Ratio | Diagnóstico |
|---------|-------|------|-------|-------------|
| Brier | 0.12 | 0.18 | 0.67 | Sobreajuste si ratio < 0.7 |
| Log Loss | 0.35 | 0.48 | 0.73 | Sobreajuste si ratio < 0.7 |
| Calibration | 0.02 | 0.08 | 0.25 | Sobreajuste si ratio < 0.3 |

**Regla**: Si train_metric es significativamente mejor que test_metric → sobreajuste.

### Método 2: Learning Curves

Si hay suficientes datos, entrenar con subconjuntos crecientes:

```
N muestras:  100   500   1000  2000  5000
Train Brier: 0.08  0.10  0.11  0.12  0.13
Test Brier:  0.25  0.18  0.16  0.15  0.14
```

- **Convergencia**: Train y test se acercan → modelo sano
- **Brecha grande**: Train mucho mejor que test → sobreajuste
- **Ambos altos**: Underfitting (modelo demasiado simple)

### Método 3: Validación Cruzada Temporal (Time Series CV)

```
Fold 1: Train [1-50]   Test [51-60]
Fold 2: Train [1-60]   Test [61-70]
Fold 3: Train [1-70]   Test [71-80]
Fold 4: Train [1-80]   Test [81-90]
Fold 5: Train [1-90]   Test [91-100]
```

Promediar métricas across folds. Si varianza alta → modelo inestable.

### Método 4: Análisis de Complejidad

Contar parámetros activos del modelo vs tamaño de datos:

| Parámetros | N datos | Ratio | Riesgo |
|------------|---------|-------|--------|
| 10 | 100 | 0.10 | Bajo |
| 50 | 100 | 0.50 | Moderado |
| 100 | 100 | 1.00 | Alto |
| 50 | 1000 | 0.05 | Bajo |

## Señales de Sobreajuste

1. **Train Brier << Test Brier** (diferencia > 0.05)
2. **Calibración pobre en test** pero buena en train
3. **CLV negativo** en datos recientes pero positivo en históricos
4. **ROI deteriorándose** con el tiempo
5. **Features con pesos extremos** en regression
6. **Sensibilidad alta** a pequeños cambios en parámetros

## Consecuencias del Sobreajuste

- Modelo "memoriza" en lugar de generalizar
- Rendimiento pobre en partidos nuevos
- Decisiones de apuesta basadas en ruido, no señal
- Pérdida financiera real

## Prevención

1. **Regularización**: L1/L2 en regression
2. **Early stopping**: Detener entrenamiento cuando test empeora
3. **Feature selection**: Remover features ruidosas
4. **Cross-validation**: Siempre validar out-of-sample
5. **Monitoreo**: Evaluar periódicamente en datos nuevos
6. **Parsimony**: Preferir modelos simples cuando sea posible

## Acción

Si se detecta sobreajuste:
1. Documentar en diagnóstico de `football-model-evaluation`
2. Recomendar a `football-model-refinement`:
   - Reducir complejidad del modelo
   - Aumentar regularización
   - Remover features problemáticas
   - Reducir pesos de componentes inestables
