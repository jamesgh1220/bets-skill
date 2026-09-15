---
name: football-betting-analysis
description: Analiza partidos y mercados de fútbol, verifica actualidad, estima probabilidades, compara cuotas, calcula value y asigna stake mediante el motor de cálculo en Python.
---

# Football Betting Analysis

## Formato de Invocación

La skill se invoca con el siguiente formato:

```
/football-betting-analysis ligas:[lista] fechas:[fecha/rango] partidos:[lista/todos] modelo:[id]
```

### Parámetros

- **ligas** (requerido): Lista de ligas separadas por comas. Ejemplo: `Premier League, LaLiga, Serie A, Ligue 1`
- **fechas** (requerido): Una fecha o rango de fechas. Formatos aceptados:
  - Fecha única: `5 de septiembre de 2026` o `2026-09-05`
  - Rango: `5-7 de septiembre de 2026` o `2026-09-05 a 2026-09-07`
- **partidos** (requerido): 
  - `todos` para analizar todos los partidos de las ligas en las fechas especificadas
  - Lista de partidos específicos: `Juventus vs Inter, Milan vs Napoli`
- **modelo** (requerido): Identificador de la IA que ejecuta la corrida. Ejemplo: `gpt-5`, `claude-sonnet` o `gemini-2-5-pro`. No es la versión del motor predictivo.

## Proceso de Análisis

1. **Parsear parámetros**: Extraer ligas, fechas, partidos y el identificador obligatorio `modelo` de la invocación.
2. **Construir el universo**: Universo = intersección(ligas, fechas, partidos). Solo incluir partidos dentro del rango de fechas especificado. Usar los MCPs disponibles (`apifootball.search_football_leagues` → `league_id`; `apifootball.get_football_matches` con `date_from`/`date_to`) para obtener fixtures reales del rango y aplicar filtrado estricto por ligas/fechas. Si los MCPs no están operativos, fallback a websearch/web scraping.
3. **Verificar actualidad de equipos y jugadores**: usando `apifootball.get_football_standings` (posición/importancia), `apifootball.get_head_to_head` (H2H + forma), `apifootball.get_football_matches` (rest_days/congestión), `apifootball.get_match_details` (lineups) e investigación del agente (entrenador, lesiones, transferencias, viajes).
4. **Buscar cuotas (por capas)**:
   - **Capa 1 (MCP odds-api, The Odds API)**: `get_events` / `get_odds` / `get_event_odds` para cuotas de Betsson, 1xBet, Pinnacle, Unibet, Betano, William Hill. Registrar timestamp de captura para CLV posterior.
   - **Capa 2 (manual)**: Betplay, Wplay, Rushbet, Zamba, Sportium (web scraping/búsqueda) para cuotas faltantes o mercado corners/cards (Betsson es la fuente principal de corners/cards).
   - **Capa 3 (agregadores)**: OddsPortal, FlashScore, SofaScore, BetExplorer como respaldo.
5. **Recopilar estadísticas y contexto**: 
   - `football-stats.get_team_stats` / `compare_teams` para xG for/against, shots, possession, big chances y ClubElo.
   - **CORNERS Y CARDS OBLIGATORIOS (8 campos)**: exigir tasas `for/against` de corners y cards de AMBOS equipos, acumulando los últimos 5–10 partidos vía `apifootball.get_match_details` (include `statistics`) o investigación en SofaScore/FlashScore. Sin esos 8 datos el mercado de corners/cards queda no disponible (consignarlo explícitamente, nunca omitirlo silenciosamente).
   - **COBRAR SIEMPRE AMBOS LADOS O/U**: para cada línea de goles (1.5, 2.5, 3.5) y de corners (8.5/9.5/10.5) y cards (3.5/4.5/5.5) capturar cuotas de `over_X` Y `under_X`. El motor calcula las probabilidades de los seis lados; un mercado O/U está incompleto si solo se provee el lado over.
6. **EJECUTAR MOTOR CUANTITATIVO DE CÁLCULO EN PYTHON (MANDATORIO)**:
   - **VALIDACIÓN PREVIA OBLIGATORIA**: antes de ejecutar `calc_engine.py`, confirmar que existen los 8 campos de corners/cards (`corners_home_for/against`, `corners_away_for/against`, `cards_home_for/against`, `cards_away_for/against`). Si faltan, recolectarlos; si es imposible, consignar explícitamente "corners/cards no disponibles" en `NO BET` — nunca omitirlos silenciosamente, y si el mercado de corners/cards llegara a faltar de cuota, NO inventarla.
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
"odds": {
          "1": 1.95, "X": 3.40, "2": 4.10,
          "over_1_5": 1.55, "under_1_5": 3.20, "under_2_5": 2.05,
          "over_3_5": 2.45, "under_3_5": 1.65,
          "btts_yes": 1.85, "1x": 1.35, "dnb_home": 1.45
        },
       "corners_home_for": 5.4,
       "corners_home_against": 4.2,
       "corners_away_for": 4.8,
       "corners_away_against": 5.1,
       "cards_home_for": 2.1,
       "cards_home_against": 2.4,
       "cards_away_for": 2.3,
       "cards_away_against": 2.0
     }
     ```
   - Ejecutar en la terminal vía `run_command`:
     `python3 scripts/calc_engine.py --input scratch/match_input.json --output scratch/match_output.json`
   - **NUNCA inferir ni inventar probabilidades manualmente.** Utilizar estrictamente las probabilidades, cuotas justas, Edge, EV y Kelly asignados por la salida JSON del script de Python.
7. **Hacer sensibilidad y robustez.**
8. **Detectar correlaciones.**
9. **Comparar candidatos globalmente** mediante `scripts.selection.select_portfolio`.
10. **Aplicar selección probabilidad-primero**: un pick prioritario requiere cuota 1.50–2.20, probabilidad modelo >=55% y EV robusto >=5%. Las cuotas >=3.00 requieren probabilidad >=30%, EV robusto >=10%, y como máximo una puede entrar con stake máximo 0.25u. Los demás candidatos se consignan como `NO BET / Excluidos`, incluso con EV bruto positivo.
11. **Emitir picks y `NO BET`.** No llenar artificialmente el máximo de seis picks.
12. **SELECCIONAR TOP 0-6**: Del total de picks con value devolver de 0 a 6 apuestas óptimas.
13. **GENERAR Y PUBLICAR ARTEFACTO (OBLIGATORIO)**:
   - Leer y respetar `references/output-format.md` antes de redactarlo.
   - Registrar por separado el `Modelo de IA` recibido y la `Versión del motor predictivo` activa.
   - **Documentar SIEMPRE ambos lados O/U**: el artefacto debe incluir la sección `## Evaluación Over/Under por Partido` (over y under por línea 1.5/2.5/3.5) y, en `NO BET / Excluidos`, justificar explícitamente el lado rechazado (típicamente el under) con el EV del motor. Un pick over SIN justificar el under analizado es un artefacto incompleto.
   - Recomendado: generar el temporal con `python3 scripts/render_artifact.py --results {results.json} --meta {meta.json} --output scratch/temp_artifact.md` para respetar el contrato y la sección O/U de forma determinista.
   - Crear un temporal único dentro de `scratch/`; no escribir directamente en `artifacts/`.
   - Ejecutar `python3 scripts/publish_analysis_artifact.py --input {temporal} --analysis-date {YYYY-MM-DD} --model "{modelo}"`.
   - El publicador valida el contrato y asigna atómicamente `analisis-YYYY-MM-DD--{modelo-slug}--vNN.md`. Si falla, corregir el archivo y volver a ejecutarlo. **No finalizar el análisis sin una ruta final publicada.**

## Reglas Críticas de Filtrado

- **Filtrado estricto por fechas**: Solo analizar partidos cuya fecha de juego esté dentro del rango proporcionado.
- **Filtrado por ligas**: Solo analizar partidos de las ligas especificadas.
- **Cálculo Determinista**: Todos los cálculos cuantitativos son ejecutados por `scripts/calc_engine.py`.
- **Corners y Cards SIEMPRE activos**: Todo partido analizado incluye los 8 campos `corners_*_for/against` y `cards_*_for/against` en `match_input.json` (obligatorios antes de `calc_engine.py`). Fuentes: `apifootball.get_match_details` (statistics, últimos 5-10 partidos por equipo) e investigación en SofaScore/FlashScore. `football-stats` NO expone corners/cards, no usarlo para eso.
- **Cuotas por capas**: Capa 1 = `odds-api` (MCP, The Odds API, 500 créditos/mes — priorizar y registrar timestamp + closing odds para CLV); Capa 2 = investigación manual (Betplay, Wplay, Rushbet, Zamba, Sportium; Betsson principal para corners/cards); Capa 3 = agregadores. Si `remaining_requests: 0`, pasar a capas 2/3.
- **Sin mercados inventados**: Corners y tarjetas solo se calculan al tener sus tasas de ambos equipos y una cuota verificable; props de tiros/jugadores quedan fuera de `v1.1` hasta disponer de un modelo y datos específicos.
- **Activación controlada**: `model-v1.2` es ACTIVE. La calibración Platt (1X2 local/visitante y O/U 2.5) se aplica automáticamente en `calc_engine.py`; no sustituir la versión activa sin backtest out-of-sample y aprobación explícita del usuario.
- **Contrato de salida**: `references/output-format.md` es obligatorio; no se permiten secciones, etiquetas o columnas alternativas.
