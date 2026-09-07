# Calibration Protocol

## Qué es la Calibración

Un modelo está calibrado cuando sus probabilidades predichas coinciden con las frecuencias observadas. Si el modelo predice 30% de probabilidad para un evento, ese evento debería ocurrir ~30% de las veces.

## Metodología

### Paso 1: Definir Tramos

Cada mercado tiene sus propios tramos de calibración definidos en `model-v{X}.{Y}.json`:

| Mercado | Tramos Típicos |
|---------|----------------|
| 1X2 | 0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0 |
| Over/Under 2.5 | 0, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 1.0 |
| BTTS | 0, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0 |
| Double Chance | 0, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 |

### Paso 2: Agrupar Predicciones

Para cada tramo [a, b):
1. Filtrar predicciones con probabilidad en [a, b)
2. Calcular probabilidad promedio predicha
3. Calcular win rate observado
4. Contar N en el tramo

### Paso 3: Calcular Error

```
Calibration Error (tramo) = observed_rate - mean_predicted_probability
```

### Paso 4: Evaluar

| Error Absoluto | Estado |
|----------------|--------|
| < 0.03 | ✅ Excelente |
| 0.03 - 0.05 | ✅ Bueno |
| 0.05 - 0.10 | ⚠️ Aceptable |
| > 0.10 | ❌ Problema |

### Paso 5: Identificar Patrones

- **Subestimación sistemática**: observed > predicted en la mayoría de tramos
- **Sobreestimación sistemática**: predicted > observed en la mayoría de tramos
- **Problemas en extremos**: errores altos en tramos bajos o altos de probabilidad
- **No linealidad**: relación predicha-observada no es lineal

## Métodos de Calibración

### Isotonic Regression (Recomendado)

- No asume forma funcional
- Ajusta monotónicamente
- Requiere ≥30 muestras por tramo
- Bueno para modelos no lineales

### Platt Scaling

- Ajusta una regresión logística sobre las predicciones
- Asume relación log-lineal
- Funciona bien con muestras pequeñas
- Menos flexible que isotonic

## Gráfico de Calibración

```
Win Rate Observado
     ^
  1.0|                          *
     |                      *
  0.8|                  *
     |              *
  0.6|          *
     |      *
  0.4|  *
     |*
  0.2|
     +---------------------------> Probabilidad Predicha
     0    0.2   0.4   0.6   0.8   1.0
```

- Línea ideal: diagonal (predicha = observada)
- Puntos sobre la línea: subestimación
- Puntos bajo la línea: sobreestimación

## Recalibración

### Cuándo Recalibrar

- Mensual (frecuencia default en `model-v{X}.{Y}.json`)
- Cuando calibration_error > 0.10 en algún mercado
- Después de cambios estructurales (nueva temporada, cambio de formato)

### Cómo Recalibrar

1. Recopilar predicciones del período reciente
2. Aplicar isotonic regression o Platt scaling
3. Generar nueva función de calibración
4. Validar en held-out set
5. Actualizar `model-v{X}.{Y}.json` si mejora
