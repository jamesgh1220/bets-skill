# Metrics Reference

## Métricas de Calidad Predictiva

### Brier Score

Mide la precisión de predicciones probabilísticas.

```
Brier = mean((p - y)²)
```

- **Rango**: [0, 1]
- **Interpretación**: 0 = perfecto, 0.25 = predicción aleatoria
- **Umbrales**: <0.15 bueno, 0.15-0.20 aceptable, >0.20 pobre

### Log Loss (Cross-Entropy)

Penaliza más fuertemente las predicciones erróneas con alta confianza.

```
Log Loss = -mean(y * log(p) + (1-y) * log(1-p))
```

- **Clipping**: Aplicar epsilon = 1e-7 para evitar log(0)
- **Rango**: [0, ∞)
- **Interpretación**: Menor es mejor
- **Umbrales**: <0.45 bueno, 0.45-0.55 aceptable, >0.55 pobre

### Calibration Error

Diferencia entre probabilidad predicha y win rate observado.

```
Calibration Error = observed_rate - mean_predicted_probability
```

- **Por tramos**: Calcular en cada bin de probabilidad
- **Interpretación**: Cerca de 0 = bien calibrado
- **Umbrales**: |error| < 0.05 bueno, 0.05-0.10 aceptable, >0.10 pobre

### ROC AUC

Área bajo la curva ROC (Receiver Operating Characteristic).

- **Rango**: [0.5, 1.0]
- **Interpretación**: 0.5 = aleatorio, 1.0 = perfecto
- **Umbrales**: >0.70 bueno, 0.60-0.70 aceptable, <0.60 pobre

### PSI (Population Stability Index)

Mide si la distribución de predicciones ha cambiado.

```
PSI = Σ (actual% - predicted%) * ln(actual% / predicted%)
```

- **Interpretación**: <0.1 estable, 0.1-0.2 cambio moderado, >0.2 cambio significativo

---

## Métricas de Rendimiento Financiero

### ROI (Return on Investment)

```
ROI = (Profit / Stake Total) × 100
```

- **Interpretación**: >0% rentable a largo plazo
- **Umbrales**: >5% bueno, 0-5% aceptable, <0% pobre

### Yield

```
Yield = Profit / N (promedio por pick)
```

- **Interpretación**: Profit promedio por apuesta
- **Umbrales**: >0.05u bueno, 0-0.05u aceptable, <0u pobre

### Win Rate

```
Win Rate = (Picks Ganados / N) × 100
```

- **Interpretación**: Depende de cuotas promedio
- **Relación con cuotas**: Cuotas altas → win rate bajo es normal

---

## Métricas de Calidad de Precio

### CLV (Closing Line Value)

Compara cuota tomada vs cuota de cierre.

```
CLV = (1 / odds_taken) - (1 / closing_odds)
```

- **Interpretación**: >0 = mejor que el mercado al cierre
- **Prioridad**: Es la métrica más importante a largo plazo
- **Umbrales**: >0.02 bueno, 0-0.02 aceptable, <0 pobre

---

## Métricas de Riesgo

### Max Drawdown

Mayor caída acumulada desde un pico de bankroll.

```
Drawdown = max(peak - current) / peak
```

- **Interpretación**: Menor es mejor
- **Umbrales**: <10% bajo, 10-20% moderado, >20% alto

### Sharpe Ratio (adaptado)

```
Sharpe = mean(excess_returns) / std(excess_returns)
```

- **Interpretación**: >1 bueno, 0-1 aceptable, <0 pobre

---

## Prioridad de Métricas

1. **CLV** — Mejor indicador de calidad predictiva a largo plazo
2. **Calibration Error** — ¿Las probabilidades coinciden con la realidad?
3. **Brier Score** — Calidad probabilística general
4. **Log Loss** — Penalización por errores con alta confianza
5. **ROI/Yield** — Resultado financiero (depende de precio)
6. **Drawdown** — Estabilidad y riesgo de ruina

## Reglas

- **Siempre informar N**. No sacar conclusiones con N < 30.
- Separar calidad de predicción, precio pagado, stake y resultado.
- No confundir suerte con skill en muestras pequeñas.
- Preferir análisis por segmentos para detectar sesgos específicos.
