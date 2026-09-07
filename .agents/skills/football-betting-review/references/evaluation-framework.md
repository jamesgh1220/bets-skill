# Evaluation Framework

## Flujo Automatizado

La skill `football-betting-review` opera de forma completamente automática:

1. **Lee artefactos** de `artifacts/analisis-*.md`
2. **Busca resultados** automáticamente via web search
3. **Actualiza** cada pick con su resultado
4. **Calcula** métricas de rendimiento
5. **Muestra** reporte completo

**No requiere input manual del usuario.**

## Fuente de Datos

Cargar artefactos desde `artifacts/analisis-{dia}-{mes}-{año}.md`.

Cada artefacto contiene:
- Metadatos del análisis (fecha, ligas, universo)
- Tabla de picks recomendados (0-6 picks)
- Detalle de cada pick (cuota, probabilidades, edge, EV, stake, confianza)
- Sección de Tracking (PENDIENTE/GANADA/PERDIDA/PUSH/VOID)

## Proceso de Evaluación

1. **Cargar artefactos**: Leer todos los archivos `analisis-*.md` del directorio `artifacts/`.
2. **Identificar picks PENDIENTES**: Buscar picks que aún no tienen resultado.
3. **Buscar resultados automáticamente**: Usar web search para cada pick PENDIENTE con fecha pasada.
4. **Actualizar artefactos**: Cambiar estado de PENDIENTE a GANADA/PERDIDA/PUSH/VOID.
5. **Calcular métricas**: N, stake, profit, ROI, yield, win rate, odds media, EV medio, CLV, max drawdown.
6. **Segmentar**: Por liga, mercado, rango de cuotas, stake, confianza, período.
7. **Analizar calibración**: Probabilidad modelo vs win rate observado.
8. **Estudiar drawdown**: Rachas, caídas máximas, varianza vs evidencia.

## Métricas Clave

| Métrica | Descripción | Umbral Acceptable |
|---------|-------------|-------------------|
| **N** | Total de picks | >= 30 para conclusions fuertes |
| **ROI** | Return on Investment | > 0% a largo plazo |
| **Yield** | Profit promedio por pick | > 0.05u |
| **Win rate** | % de picks ganados | Depende de cuotas |
| **CLV** | Closing Line Value | > 0 (mejor que el mercado) |
| **Max drawdown** | Mayor caída acumulada | < 20% del bankroll |

## Prioridad de Métricas

1. **CLV** — Mejor indicador de calidad predictiva a largo plazo.
2. **Calibración** — ¿Las probabilidades del modelo coinciden con la realidad?
3. **Brier/Log Loss** — Medida de calidad probabilística.
4. **ROI/Yield** — Resultado financiero (depende de precio, no solo predicción).
5. **Drawdown** — Estabilidad y riesgo de ruina.
6. **Estabilidad temporal** — ¿El rendimiento es consistente?

## Reglas

- ROI positivo no prueba por sí solo un buen modelo.
- ROI negativo con CLV positivo puede ocurrir en muestras cortas.
- **Siempre informar N**. No sacar conclusiones con N < 10.
- Separar calidad de predicción, precio pagado, stake y resultado.
- No confundir suerte con skill en muestras pequeñas.
- Preferir análisis por segmentos para detectar sesgos específicos.

## Formato de Salida del Review

### Resumen
```
=== RESUMEN DE RENDIMIENTO ===
Período: {inicio} - {fin}
Artefactos analizados: {N_archivos}
Total picks: {N}
Stake total: {stake}u
Profit: {profit}u
ROI: {roi}%
Yield: {yield}
Win rate: {win_rate}%
```

### Tabla Histórica
| Fecha | Partido | Mercado | Selección | Cuota | Stake | Resultado | Profit | P/L Acum. |

### Segmentación
| Segmento | N | Win Rate | ROI | Yield |

### Conclusiones
- Sesgos detectados.
- Recomendaciones de ajuste.
- Calidad de predicción vs precio.
