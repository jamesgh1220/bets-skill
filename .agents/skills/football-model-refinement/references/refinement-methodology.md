# Refinement Methodology

## Tipos de Cambios

### 1. Ajuste de Pesos de Componentes

Cambiar la contribución de cada modelo en el ensemble.

| Componente | Rango Aceptable | Paso Mínimo |
|------------|-----------------|-------------|
| Poisson | 0.15 - 0.50 | 0.05 |
| Dixon-Coles | 0.15 - 0.50 | 0.05 |
| Ratings | 0.10 - 0.35 | 0.05 |
| Regression | 0.10 - 0.30 | 0.05 |

**Restricción**: Suma de pesos = 1.0

**Ejemplo**:
```
Actual:    Poisson 0.35, DC 0.30, Ratings 0.20, Regression 0.15
Propuesto: Poisson 0.30, DC 0.35, Ratings 0.20, Regression 0.15
Motivo:    DC mejor calibrado que Poisson en análisis reciente
```

### 2. Ajuste de Pesos de Features

Cambiar la importancia de cada tipo de feature.

| Feature Group | Rango Aceptable | Paso Mínimo |
|---------------|-----------------|-------------|
| offensive | 0.20 - 0.40 | 0.05 |
| defensive | 0.15 - 0.35 | 0.05 |
| contextual | 0.10 - 0.30 | 0.05 |
| form | 0.05 - 0.25 | 0.05 |
| player | 0.05 - 0.20 | 0.05 |

**Restricción**: Suma de pesos = 1.0

### 3. Ajuste de Umbrales

Cambiar valores de corte para decisiones.

| Umbral | Mercado | Rango | Paso |
|--------|---------|-------|------|
| min_edge | Todos | 0.02 - 0.10 | 0.01 |
| min_confidence | Todos | medium - high | N/A |
| min_matches | Todos | 5 - 30 | 5 |

### 4. Recalibración de Mercados

Ajustar tramos de calibración para mercados específicos.

**Proceso**:
1. Identificar tramos con error > 0.05
2. Dividir tramos problemáticos en sub-tramos
3. O fusionar tramos con pocos datos
4. Validar que mejora calibration error total

### 5. Remoción de Features

Eliminar features que causan ruido o sobreajuste.

**Criterios de remoción**:
- Correlación > 0.8 con otra feature
- Importancia < 0.02 en regression
- Causa sobreajuste (diferencia train/test significativa)
- Datos insuficientes (< 70% completitud)

### 6. Adición de Features

Agregar nuevas features que puedan mejorar predicción.

**Requisitos**:
- Datos disponibles para > 80% de partidos en test set
- Correlación < 0.5 con features existentes
- Justificación teórica de por qué mejora
- Validación out-of-sample positiva

### 7. Toggle de Componentes

Habilitar o deshabilitar componentes del ensemble.

**Cuándo deshabilitar**:
- Componente tiene CLV negativo consistente
- Componente causa sobreajuste
- Componente no aporta valor incremental

**Cuándo habilitar**:
- Nuevos datos disponibles
- Cambio estructural que beneficia al componente

## Protocolo de Backtesting

### Separación de Datos

```
Datos totales: [Fecha inicio] - [Fecha fin]
├── Train: [Inicio] - [Inicio + 70%] (para entrenar)
└── Test:  [Inicio + 70%] - [Fin] (para validar)
```

**IMPORTANTE**: Split POR TIEMPO, nunca aleatorio.

### Proceso

1. **Entrenar modelo actual** con datos de train
2. **Generar predicciones** en datos de test
3. **Calcular métricas** en test
4. **Entrenar modelo propuesto** con mismos datos de train
5. **Generar predicciones** en datos de test
6. **Calcular métricas** en test
7. **Comparar** ambas versiones

### Métricas de Comparación

| Métrica | Mejora Requerida | Empeoramiento Máximo |
|---------|------------------|----------------------|
| Brier | -0.005 | +0.002 |
| Log Loss | -0.01 | +0.005 |
| Calibration Error | -0.01 | +0.005 |
| CLV | +0.005 | -0.01 |
| ROI | +1% | -2% |

### Validación Cruzada Temporal

Para mayor robustez:

```
Fold 1: Train [1-60%]  Test [60-70%]
Fold 2: Train [1-70%]  Test [70-80%]
Fold 3: Train [1-80%]  Test [80-90%]
Fold 4: Train [1-90%]  Test [90-100%]
```

El cambio se aprueba solo si mejora en ≥3 de 4 folds.

## Criterios de Aprobación

### Aprobar SI:

1. ✅ Brier mejora en test set
2. ✅ Calibration error disminuye o se mantiene
3. ✅ CLV no se deteriora > 0.01
4. ✅ No hay sobreajuste nuevo
5. ✅ Mejora es consistente across folds
6. ✅ Cambio es justificable teóricamente

### Rechazar SI:

1. ❌ Brier empeora en test
2. ❌ CLV disminuye > 0.01
3. ❌ Nuevo sobreajuste detectado
4. ❌ Mejora solo en train (no generaliza)
5. ❌ Cambio es arbitrario sin justificación
6. ❌ Datos insuficientes para validar

### Pedir Modificación SI:

1. ⚠️ Cambio es demasiado agresivo (reducir magnitud)
2. ⚠️ Hay múltiples cambios (separar en propuestas)
3. ⚠️ Backtesting es borderline (necesita más validación)
