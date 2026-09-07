---
name: football-betting-analysis
description: Analiza partidos y mercados de fútbol, verifica actualidad, estima probabilidades, compara cuotas, calcula value y asigna stake mediante el motor de cálculo en Python.
---

# Football Betting Analysis

## Formato de Invocación

La skill se invoca con el siguiente formato:

```
/football-betting-analysis ligas:[lista] fechas:[fecha/rango] partidos:[lista/todos]
```

### Parámetros

- **ligas** (requerido): Lista de ligas separadas por comas. Ejemplo: `Premier League, LaLiga, Serie A, Ligue 1`
- **fechas** (requerido): Una fecha o rango de fechas. Formatos aceptados:
  - Fecha única: `5 de septiembre de 2026` o `2026-09-05`
  - Rango: `5-7 de septiembre de 2026` o `2026-09-05 a 2026-09-07`
- **partidos** (requerido): 
  - `todos` para analizar todos los partidos de las ligas en las fechas especificadas
  - Lista de partidos específicos: `Juventus vs Inter, Milan vs Napoli`

## Proceso de Análisis

1. **Parsear parámetros**: Extraer ligas, fechas y partidos de la invocación.
2. **Construir el universo**: Universo = intersección(ligas, fechas, partidos). Solo incluir partidos dentro del rango de fechas especificado.
3. **Verificar actualidad de equipos y jugadores.**
4. **Buscar cuotas en bookmakers colombianos**: Consultar cuotas en las casas de apuestas configuradas (Betplay, Betsson, Wplay, Rushbet, Zamba, Sportium) usando web scraping/búsqueda.
5. **Recopilar estadísticas y contexto**: Extraer xG_for, xG_against, Elo ratings y cuotas de entrada.
6. **EJECUTAR MOTOR CUANTITATIVO DE CÁLCULO EN PYTHON (MANDATORIO)**:
   - Crear archivo temporal JSON en `scratch/match_input.json` con la información del partido:
     ```json
     {
       "home_team": "...",
       "away_team": "...",
       "xg_home_for": 1.5,
       "xg_home_against": 1.0,
       "xg_away_for": 1.2,
       "xg_away_against": 1.3,
       "elo_home": 1600,
       "elo_away": 1500,
       "odds": { "1": 1.95, "X": 3.40, "2": 4.10, "under_2_5": 2.05 }
     }
     ```
   - Ejecutar en la terminal vía `run_command`:
     `python3 scripts/calc_engine.py --input scratch/match_input.json --output scratch/match_output.json`
   - **NUNCA inferir ni inventar probabilidades manualmente.** Utilizar estrictamente las probabilidades, cuotas justas, Edge, EV y Kelly asignados por la salida JSON del script de Python.
7. **Hacer sensibilidad y robustez.**
8. **Detectar correlaciones.**
9. **Comparar candidatos globalmente.**
10. **Emitir picks y `NO BET`.**
11. **SELECCIONAR TOP 0-6**: Del total de picks con value devolver de 0 a 6 apuestas óptimas.
12. **GENERAR ARTEFACTO**: Crear archivo `artifacts/analisis-{dia}-{mes}-{año}.md`.

## Reglas Críticas de Filtrado

- **Filtrado estricto por fechas**: Solo analizar partidos cuya fecha de juego esté dentro del rango proporcionado.
- **Filtrado por ligas**: Solo analizar partidos de las ligas especificadas.
- **Cálculo Determinista**: Todos los cálculos cuantitativos son ejecutados por `scripts/calc_engine.py`.
