# Football Betting Intelligence System

## Propósito
Sistema cuantitativo para análisis de apuestas de fútbol, búsqueda de value y evaluación del modelo.

## Reglas críticas
- Verificar actualidad antes de cada predicción.
- Registrar `analysis_date`, `match_date` e `information_cutoff`.
- No usar información posterior al kickoff.
- Verificar club actual, transferencias, entrenador, lesiones, suspensiones, disponibilidad y calendario.
- No elegir por fama; analizar todo el universo solicitado.
- **Respetar estrictamente el rango de fechas proporcionado en la invocación. No analizar partidos fuera del rango bajo ninguna circunstancia.**
- Una cuota baja puede tener value; una cuota alta no implica value.
- `NO BET` es válido.
- Separar probabilidad modelo y probabilidad implícita.
- Calcular cuota justa, edge y EV.
- Ajustar por incertidumbre, robustez y correlación.
- Stake en unidades; nunca martingala.
- Registrar fuentes y timestamps de hechos críticos.
- Evitar hindsight/look-ahead bias.

## Datos
Goles, xG/xGA, tiros, tiros a puerta, grandes ocasiones, xG/tiro, posesión, progresión, creación, PPDA, errores, balón parado, localía, descanso, viajes, congestión, calendario, competición, importancia, rotaciones, jugadores, minutos, xG/xA, tiros y penaltis.

## Modelos
Poisson, Dixon-Coles, ratings, regresión, Bayes, Monte Carlo y ensembles según disponibilidad. Aumentar incertidumbre ante muestras pequeñas o grandes cambios de plantilla/entrenador.

## Stake orientativo
0.25u pequeña; 0.50u moderada; 0.75u buena; 1.00u fuerte; 1.25u muy fuerte; 1.50u excepcional. Kelly solo como referencia y preferiblemente fractional Kelly.

## Salida
- Cada pick debe incluir partido, mercado, selección, cuota, probabilidades, cuota justa, edge, EV, cuota mínima, stake, confianza, incertidumbre, razones, riesgos y fuentes.
- **Máximo 6 picks finales.** Seleccionar los más óptimos por EV robusto, edge y diversificación. No forzar a llegar a 6 si no hay value suficiente.
- **Generar artefacto `.md` validado** en `artifacts/` con cada análisis completo. Nombre: `analisis-YYYY-MM-DD--{modelo-ia}--vNN.md`; `modelo:` es obligatorio y la publicación debe usar `scripts/publish_analysis_artifact.py`.
- Luego ranking global y portfolio.
- La skill `football-betting-review` lee estos artefactos para evaluar rendimiento histórico.

Nunca presentar apuestas como seguras o garantizadas.

## Ciclo de Modelado

```
1. /football-betting-analysis → picks + artifacts/
2. (Resultados de partidos)
3. /football-review → métricas de rendimiento
4. /football-model → diagnóstico (NUNCA modifica)
5. /football-refinement → propuesta → backtesting → aprobación → versión
```

### Reglas de Evaluación (football-model-evaluation)
- **NUNCA modificar el modelo directamente.** Solo diagnosticar.
- Siempre informar N (mínimo 30 para conclusiones).
- Comparar con versión anterior cuando exista.
- Generar recomendaciones accionables para refinement.

### Reglas de Refinamiento (football-model-refinement)
- **NUNCA modificar el modelo sin aprobación explícita del usuario.**
- **NUNCA saltar backtesting.** Todo cambio debe ser validado out-of-sample.
- **NUNCA sobrescribir versiones.** Crear nueva versión, no modificar existente.
- **Un cambio a la vez.** No combinar múltiples cambios en una propuesta.
- Priorizar sobre calibración. La calibración es más importante que el ROI.
- Documentar todo: cambios, métricas, justificación.

### Sistema de Versionado
- Modelos en `models/model-v{X}.{Y}.json`
- Versión mayor (v1.0 → v2.0): cambios arquitectónicos
- Versión menor (v1.0 → v1.1): refinamientos de pesos/umbrales
- Solo UNA versión `active` a la vez
- Versiones anteriores → `deprecated`
- Changelog en `models/changelog.md`
