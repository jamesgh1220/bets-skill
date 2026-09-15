# Plan de Instalación de MCP Servers

**Fecha:** 14 de septiembre de 2026
**Estado:** EN EJECUCIÓN — Instalado en la máquina principal (14/09/2026). Datos de `football-data-mcp` descargando, resto completado.

**Objetivo:** Integrar 3 MCP servers gratuitos en el proyecto `bets-skill` para automatizar la recolección de datos de fútbol y cuotas, garantizar que los mercados de corners/cards estén SIEMPRE operativos y que las features aspiracionales del modelo se recojan SIEMPRE.

### Desviaciones corregidas en la implementación (verificado empíricamente)

- **`mcp-odds-api` NO es un paquete npm.** Es un paquete **Python** (PyPI) que se ejecuta con `uvx`, no con `npx`. Además, **`mcp` 2.x rompe FastMCP** (`mcp.server.fastmcp` renombrado), por lo que se **fija `mcp<2`**. Comando final: `uvx --with "mcp<2" --env-file .env mcp-odds-api` (lee `ODDS_API_KEY` directamente de `.env`).
- **opencode NO carga `.env` automáticamente** (verificado con `opencode debug config` en v1.18.30). Consecuencia:
  - `ODDS_API_KEY` → la lee `uvx --env-file .env` (funciona solo con el `.env`).
  - `APIFOOTBALL_KEY` → opencode interpola `{env:APIFOOTBALL_KEY}` **desde el proceso**, así que necesita `export` o `source .env` antes de lanzar opencode (o añadirla a `~/.zshrc`).
- **Python 3.9.6 del sistema insuficiente**: `football-data-mcp` requiere ≥3.10. Instalado **Python 3.12.14** (gestionado por `uv`) y el paquete con `uv tool install football-data-mcp` (shims `soccer-mcp`/`collect-data` en `~/.local/bin`, ya en PATH).
- `apifootball` remoto: se añadió `"oauth": false` (es autenticación por bearer header, no OAuth).
- `collect-data` usa Chrome (Selenium Manager resuelve chromedriver); Chrome 152 detectado y descarga en curso.

---

## Tabla de Contenidos

1. [Resumen de MCPs a instalar](#1-resumen-de-mcps-a-instalar)
2. [Prerrequisitos](#2-prerrequisitos)
3. [Paso 1: football-data-mcp](#3-paso-1-football-data-mcp)
4. [Paso 2: mcp-odds-api (The Odds API)](#4-paso-2-mcp-odds-api-the-odds-api)
5. [Paso 3: APIfootball MCP](#5-paso-3-apifootball-mcp)
6. [Configuración en opencode](#6-configuración-en-opencode)
7. [Verificación de instalación](#7-verificación-de-instalación)
8. [Integración con el workflow de análisis](#8-integración-con-el-workflow-de-análisis)
9. [Garantías de datos: corners/cards y features aspiracionales](#9-garantías-de-datos-cornerscards-y-features-aspiracionales)
10. [Modificaciones de archivos de skill](#10-modificaciones-de-archivos-de-skill)
11. [Troubleshooting](#11-troubleshooting)

---

## 1. Resumen de MCPs a instalar

| MCP | Tipo | API Key | Costo | Rol |
|-----|------|---------|-------|-----|
| `football-data-mcp` | Local (Python) | No | Gratis | xG, shots, possession, form, stats jugadores/equipos |
| `mcp-odds-api` (The Odds API) | Local (npx) | Sí (gratis) | Gratis | Cuotas reales de bookmakers + histórico para CLV |
| `APIfootball MCP` | Remoto (HTTP) | Sí (gratis) | Gratis | Fixtures, resultados, H2H, standings, predicciones, statistics |

**Decisiones de diseño de este plan:**

- `mcp-server-scraper` fue evaluado y **descartado**: no ejecuta JavaScript ni atraviesa protección anti-bot de casas de apuestas colombianas (Betplay, Wplay). No aporta valor a este proyecto.
- APIfootball en plan gratuito **NO incluye odds**. La fuente de cuotas programáticas es `mcp-odds-api` (The Odds API), cuyo plan gratuito (500 créditos/mes) **sí incluye Historical Odds** → habilita el cálculo de CLV (hoy `null` en todos los modelos).

---

## 2. Prerrequisitos

### Requisitos del sistema

```bash
python3 --version   # Necesario >= 3.10
node --version      # Necesario >= 18 (para npx)
npm --version       # Cualquier versión moderna
```

### API Keys gratuitas necesarias

| Key | Dónde obtenerla | Límite gratuito |
|-----|----------------|-----------------|
| `ODDS_API_KEY` | https://the-odds-api.com/ | 500 créditos/mes |
| `APIFOOTBALL_KEY` | https://apifootball.com/register/ | 100 requests/día |

### Variables de entorno

Agregar al archivo `~/.zshrc` o `~/.bashrc`:

```bash
export ODDS_API_KEY="tu-key-the-odds-api"
export APIFOOTBALL_KEY="tu-key-apifootball"
```

Recargar shell: `source ~/.zshrc`

---

## 3. Paso 1: football-data-mcp

**Qué es:** Servidor MCP con stats avanzadas de 10 ligas, 3 temporadas (2023-24, 2024-25, 2025-26), 18,800+ registros de jugadores. Fuentes: FBref, SofaScore, Understat, Transfermarkt, ClubElo, Capology.

### 3.1 Instalar el paquete

```bash
pip install football-data-mcp

# Verificar instalación
which soccer-mcp      # Comando del servidor MCP
which collect-data    # Comando de descarga de datos
```

**Si `soccer-mcp` no se encuentra en PATH:**

```bash
pip show football-data-mcp | grep Location
python3 -m soccer_server   # arranque alternativo del servidor
```

### 3.2 Descargar datos (primera vez)

```bash
# Descarga completa (15-30 minutos; abre navegador headless)
collect-data
```

**Opciones de refresco incremental:**

```bash
collect-data --sofascore-only           # Stats de jugadores
collect-data --understat-only           # xG, tiros, positional
collect-data --transfermarkt-only       # Valores de mercado
collect-data --understat-tables-only    # Tablas xG por liga
collect-data --understat-matches-only   # Datos match-by-match
collect-data --rebuild-only             # Reconstruir sin re-descargar
```

**Nota:** Requiere navegador (Chrome/Chromium) para scraping. En macOS: `brew install --cask chromium`.

### 3.3 Herramientas (10 tools)

| Tool | Descripción | Uso en análisis |
|------|-------------|-----------------|
| `get_player` | Stats de temporada de un jugador | Rendimiento individual |
| `get_eafc_player_attributes` | Atributos EA FC | Contexto de habilidades |
| `scout_position` | Ranking por posición | Jugadores clave |
| `compare_players` | Comparar dos jugadores | Evaluación de impacto |
| `get_team_stats` | Stats y tabla de liga del equipo | **xG, posesión, tiros, grandes ocasiones** |
| `compare_teams` | Comparar dos equipos | Match preview cuantitativo |
| `get_match` | Resumen de un partido | Score, possession, xG, shots, big chances |
| `get_match_player_stats` | Stats de todos los jugadores de un partido | Análisis post-partido |
| `get_player_match_stats` | Un jugador en un rango de fechas | **Forma reciente** |
| `get_match_shots` | Mapa de tiros de un partido | Análisis de ocasiones |

**Dato verificado:** `get_team_stats` expone `avg_xg_for`, `avg_xg_against`, `avg_possession`, `avg_shots`, `avg_big_chances_for`, `home_avg_xg_for`, `away_avg_xg_for` (ver `output_schema.py`). **NO expone corners ni cards** → esos datos vienen de APIfootball/investigación (ver §9).

### 3.4 Variables que alimenta en el proyecto

| Campo del modelo | Tool de football-data-mcp |
|------------------|---------------------------|
| `xg_home_for` / `xg_home_against` | `get_team_stats` (avg_xg_for / avg_xg_against) |
| `xg_away_for` / `xg_away_against` | `get_team_stats` |
| `elo_home` / `elo_away` | ClubElo (rastreado por el paquete) |
| `shots_per_game` | `get_team_stats` (avg_shots) |
| `possession_avg` | `get_team_stats` (avg_possession) |
| `big_chances_created` | `get_team_stats` (avg_big_chances_for) |
| `form_last_5` / `xG_form_last_5` | `get_player_match_stats` (rangos de fechas) |

---

## 4. Paso 2: mcp-odds-api (The Odds API)

**Qué es:** MCP server que consulta The Odds API: cuotas de bookmakers para deportes y mercados configurados. Plan gratuito con **Historical Odds incluido**.

### 4.1 Obtener API Key (GRATIS)

1. Ir a https://the-odds-api.com/
2. Suscribirse al plan **Starter (FREE, 500 créditos/mes)**
3. Recibir la key por email
4. Exportarla: `export ODDS_API_KEY="tu-key"`

### 4.2 Cobertura de bookmakers (verificada)

The Odds API **cubre estos bookmakers que el proyecto ya usa**:
- **Betsson** (región `eu`) — una de las 6 casas colombianas del proyecto
- **1xBet, Pinnacle, Unibet, Betano, William Hill**

**NO cubre** (quedan en flujo manual, ver §8.4): Betplay, Wplay, Rushbet, Zamba.

### 4.3 Herramientas (3 tools)

| Tool | Descripción | Uso en análisis |
|------|-------------|-----------------|
| `get_events` | Eventos próximos y en vivo | Descubrir partidos con cuotas |
| `get_odds` | Cuotas de todos los eventos de un deporte/mercado | Cuotas en bloque |
| `get_event_odds` | Cuotas de un evento puntual | Cuota de un partido específico |

### 4.4 Mercados y deportes

- Mercados: head-to-head (moneyline), spreads (handicap), totals (O/U), outrights
- Sport keys de fútbol: `soccer_epl`, `soccer_la_liga`, `soccer_serie_a`, `soccer_ligue_one`, `soccer_germany_bundesliga`, `soccer_brazil_campeonato`, y más
- Descubrir keys disponibles:

```bash
curl "https://api.the-odds-api.com/v4/sports/?apiKey=$ODDS_API_KEY"
```

**Limitaciones conocidas:**
- El server MCP (`mcp-odds-api`) configura **un solo deporte** vía `ODDS_API_SPORT`. Para otras ligas, ajustar la variable o usar `webfetch` directo a `https://api.the-odds-api.com/v4/sports/{sport}/odds/`.
- Cada request a una combinación (deporte, mercado, región) consume 1 crédito (500/mes).
- No lista corners/cards → sus cuotas se obtienen de bookmakers con ese mercado (Betsson) vía investigación del agente (§8.4 capa 2).

### 4.5 Historical Odds (CLV)

El plan gratuito incluye `https://api.the-odds-api.com/v4/historical/sports/{sport}/odds/` para obtener snapshots de cuotas históricas → **cuota de cierre (closing odds)** → calcular **CLV** por pick (hoy `null` en `model-v1.0/v1.1/v1.2.json`).

---

## 5. Paso 3: APIfootball MCP

**Qué es:** Servidor MCP remoto (no requiere instalación local) sobre la REST API de APIfootball.

### 5.1 Obtener API Key (GRATIS)

1. Ir a https://apifootball.com/register/
2. Crear cuenta gratuita
3. Copiar la key del dashboard
4. Exportarla: `export APIFOOTBALL_KEY="tu-key"`

### 5.2 Herramientas (10 tools)

| Tool | Descripción | Uso en análisis |
|------|-------------|-----------------|
| `search_football_leagues` | Buscar ligas por país/nombre | Obtener `league_id` |
| `get_football_matches` | Fixtures y resultados (hasta 15 días) | Construir universo; **calcular rest_days** |
| `get_live_football_matches` | Partidos en vivo | Monitoreo |
| `get_football_standings` | Tabla de posiciones | Contexto de liga / importancia |
| `get_match_details` | Goles, cards, lineups, **statistics** | **Corners/cards por partido**; resultados review |
| `get_head_to_head` | Historial + forma reciente de ambos equipos | H2H y `form_last_5` |
| `get_football_predictions` | Probabilidades matemáticas 1X2/O-U | Baseline de comparación |
| `get_football_odds` | Cuotas (plan de pago) | **NO disponible en plan gratis** |
| `get_football_topscorers` | Top goleadores | Contexto ofensivo |
| `get_live_football_odds_comments` | Odds en vivo (plan de pago) | **NO disponible en plan gratis** |

### 5.3 Limitaciones del plan gratuito

- **Odds NO disponibles** → la fuente de cuotas es The Odds API (§4); `get_football_predictions` como baseline de probabilidades de mercado
- Rango máximo 15 días por request
- `get_match_details` con `include: ["statistics"]` entrega estadísticas por partido (útil para promedios de **corners y cards**, ver §9.1)

---

## 6. Configuración en opencode

### 6.1 Crear/editar `opencode.jsonc` en la raíz

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "football-stats": {
      "type": "local",
      "command": ["soccer-mcp"],
      "description": "Stats avanzadas: xG, shots, possession, form, big chances (FBref/Understat/SofaScore/ClubElo)."
    },
    "odds-api": {
      "type": "local",
      "command": ["npx", "-y", "mcp-odds-api"],
      "environment": {
        "ODDS_API_KEY": "{env:ODDS_API_KEY}",
        "ODDS_API_REGIONS": "eu,br,co,us",
        "ODDS_API_SPORT": "soccer_epl"
      },
      "description": "Cuotas reales de bookmakers (Betsson, 1xBet, Pinnacle, Unibet) + histórico para CLV."
    },
    "apifootball": {
      "type": "remote",
      "url": "https://mcp.apifootball.com/mcp",
      "headers": {
        "Authorization": "Bearer {env:APIFOOTBALL_KEY}"
      },
      "description": "Fixtures, resultados, H2H, standings, predicciones, statistics (corners/cards). Sin odds en plan gratis."
    }
  }
}
```

**Nota:** `ODDS_API_SPORT` limita a un deporte por server. Para cubrir varias ligas:
- Duplicar el server con un nombre distinto y otro sport key, o
- Que el agente llame a la REST API de The Odds API vía `webfetch` para deportes adicionales.

### 6.2 Si `soccer-mcp` no está en PATH

```bash
which soccer-mcp
# Si vacío, usar:
python3 -m soccer_server
```

En `opencode.jsonc`:

```jsonc
"football-stats": {
  "type": "local",
  "command": ["python3", "-m", "soccer_server"],
  "description": "Stats avanzadas de fútbol."
}
```

---

## 7. Verificación de instalación

```bash
# 1. Comandos de football-data-mcp
which collect-data
which soccer-mcp

# 2. Node para npx (odds-api)
node --version   # >= 18

# 3. API keys configuradas
echo "Odds:    ${ODDS_API_KEY:0:8}..."
echo "ApiFoot: ${APIFOOTBALL_KEY:0:8}..."

# 4. Descubrir deportes en The Odds API
curl "https://api.the-odds-api.com/v4/sports/?apiKey=$ODDS_API_KEY"

# 5. Probar APIfootball vía REST (misma key que usa el MCP)
curl -s "https://v3.football.api-sports.io/leagues?country=England" \
  -H "x-apisports-key: $APIFOOTBALL_KEY" | head -c 200

# 6. Listar MCPs conectados en opencode
opencode mcp list
# Esperado: football-stats (connected), odds-api (connected), apifootball (connected)
```

---

## 8. Integración con el workflow de análisis

### 8.1 Pipeline actual (sin MCPs)

```
Agente IA → websearch manual → JSON manual → calc_engine.py → artefacto
```

### 8.2 Pipeline con MCPs

```
Agente IA → MCPs automatizados → JSON enriquecido → calc_engine.py → artefacto
```

### 8.3 Flujo mejorado paso a paso

```
1. CONSTRUIR UNIVERSO
   ├── apifootball.search_football_leagues → league_id por liga
   ├── apifootball.get_football_matches (date_from/date_to) → fixtures del rango
   └── Aplicar filtrado estricto por ligas/fechas (regla del skill)

2. CONTEXTO DE LIGA (importancia)
   ├── apifootball.get_football_standings → posición, puntos
   └── apifootball.get_football_topscorers → contexto ofensivo

3. CONTEXTO DE EQUIPOS (features aspiracionales)
   ├── football-stats.get_team_stats → xG for/against, shots, possession, big chances
   ├── apifootball.get_head_to_head → H2H record + forma reciente ambos equipos
   ├── apifootball.get_football_matches → últimos resultados → rest_days / congestión
   └── Investigación del agente (websearch) → manager, lesiones, viajes, transferencias

4. CORNERS Y CARDS (SIEMPRE, ver §9.1)
   ├── apifootball.get_match_details (include=statistics) → corners/cards por partido (últimos 5-10)
   ├── Investigación en SofaScore/FlashScore → promedios for/against
   └── Se completan los 8 campos del input

5. CUOTAS (capa 1)
   ├── odds-api.get_events / get_odds / get_event_odds → cuotas reales (Betsson, 1xBet, Pinnacle, Unibet...)
   ├── COBRAR ambos lados O/U (1.5/2.5/3.5) → matriz completa de 6 lados
   └── Si no hay cuota → capa manual (§8.4): Betplay/Wplay/Rushbet/Zamba

6. MOTOR (sin cambios)
   ├── Validación previa: los 8 campos de corners/cards deben existir
   └── calc_engine.py → prob, cuota justa, edge, EV, Kelly

7. SELECCIÓN Y PUBLICACIÓN (sin cambios)
   └── selection.py → render_artifact.py → publish_analysis_artifact.py
```

### 8.4 Capas de obtención de cuotas

| Capa | Fuente | Bookmakers | Cuándo |
|------|--------|-----------|--------|
| **Capa 1 (MCP)** | `odds-api` (The Odds API) | Betsson, 1xBet, Pinnacle, Unibet, Betano, William Hill | Siempre primero; registra timestamp y closing odds (CLV) |
| **Capa 2 (manual)** | Investigación del agente (websearch/webfetch) | Betplay, Wplay, Rushbet, Zamba, Sportium | Para cuotas faltantes o mercado corners/cards |
| **Capa 3 (agregadores)** | OddsPortal, FlashScore, SofaScore, BetExplorer | — | Respaldo si 1 y 2 fallan |

---

## 9. Garantías de datos: corners/cards y features aspiracionales

> **Contexto verificado en el código:**
> - El motor **ya soporta** corners/cards. `model-v1.2.json` define corners (líneas 8.5/9.5/10.5, dispersion 12) y cards (líneas 3.5/4.5/5.5, dispersion 7); `_count_market_probabilities` en `calc_engine.py` los activa automáticamente cuando existen los 8 campos de entrada.
> - Históricamente **cero inputs han incluido esos campos** → los mercados nunca se operaron. Este plan los convierte en **OBLIGATORIOS**.
> - Las features aspiracionales (shots, possession, form, rest_days, etc.) NO alimentan el cálculo probabilístico todavía: el motor solo lee `xg_*`, `elo_*`, `corners/cards`. Recolectarlas y documentarlas SIEMPRE es posible sin tocar el modelo; integrarlas al cálculo requiere el ciclo de refinement (Fase 2, §9.3).

### 9.1 Corners y Cards — SIEMPRE activos

**Regla nueva (obligatoria):** Todo partido analizado debe incluir los 8 campos en `match_input.json`:

```json
{
  "corners_home_for": 5.4, "corners_home_against": 4.2,
  "corners_away_for": 4.8,  "corners_away_against": 5.1,
  "cards_home_for": 2.1,    "cards_home_against": 2.4,
  "cards_away_for": 2.3,    "cards_away_against": 2.0
}
```

**Fuentes de las tasas for/against:**
1. **APIfootball** `get_match_details` (include `statistics`) → acumular últimos 5–10 partidos de cada equipo → promedio corners/cards for/against
2. **Investigación del agente** en SofaScore/FlashScore (tablas de corners/cards por equipo home/away)
3. `football-data-mcp` **no expone corners/cards** → no usar como fuente para esto

**Reglas de mercado (refuerzo de la skill):**
- Sin cuota verificable → mercado "no disponible" (nunca inventar cuota)
- **Cobrar SIEMPRE ambos lados** over Y under de cada línea de corners y cards
- Betsson publica mercados de corners/cards → fuente principal de cuota (capa 2 si Odds API no lo cubre)

**Validación en el proceso (mandatoria):** antes de ejecutar `calc_engine.py`, confirmar que los 8 campos existen. Si faltan, recolectarlos; si es imposible, consignar explícitamente "corners/cards no disponibles" en `NO BET` — nunca omitirlos silenciosamente.

### 9.2 Features aspiracionales — recolección SIEMPRE

| Feature del modelo | Fuente | Herramienta |
|---|---|---|
| `xg_home_for/against`, `xg_away_for/against` | football-data-mcp | `get_team_stats` (avg_xg_for/against) |
| `shots_per_game` | football-data-mcp | `get_team_stats` (avg_shots) |
| `possession_avg` | football-data-mcp | `get_team_stats` (avg_possession) |
| `big_chances_created` | football-data-mcp | `get_team_stats` (avg_big_chances_for) |
| `form_last_5` / `xG_form_last_5` | APIfootball | `get_head_to_head` (recent_form) o `get_football_matches` |
| `head_to_head_record` | APIfootball | `get_head_to_head` |
| `rest_days` / congestión | APIfootball | `get_football_matches` (días desde el último partido de cada equipo) |
| `competition_importance` | APIfootball | `get_football_standings` |
| `travel_distance` | Investigación del agente | Distancia entre sedes (derby vs. viaje largo) |
| `manager_tenure` / `referee` / `line` | Investigación del agente | websearch / webfetch |

Estas features se registran SIEMPRE en el artefacto de análisis como contexto documentado, aunque no alimenten el motor (hoy solo lee `xg_*`, `elo_*`, `corners/cards`).

### 9.3 Fase 2 (futura): features en el cálculo

Integrar estas features al motor probabilístico es un **cambio de modelo** y debe seguir el ciclo del AGENTS.md:
1. `/football-model-evaluation` sobre el modelo actual
2. `/football-model-refinement` → propuesta → **backtesting out-of-sample**
3. nueva versión de modelo `models/model-v1.3.json` (nunca sobrescribir existentes)
4. aprobación explícita del usuario antes de activar

---

## 10. Modificaciones de archivos de skill

Cuando se ejecute este plan, además de la instalación, se aplicarán estos cambios de archivos:

| Archivo | Cambio |
|---------|--------|
| `MCP-INSTALLATION-PLAN.md` (este) | Plan completo de instalación y workflow |
| `opencode.jsonc` (nuevo, raíz) | Configuración de los 3 MCPs (ver §6) |
| `.agents/skills/football-betting-analysis/SKILL.md` | Paso de recolección vía MCPs; corners/cards obligatorios; validación de los 8 campos antes de `calc_engine.py` |
| `.../references/bookmakers.md` | Capas de obtención de cuotas (§8.4) + registrar cuota de cierre para CLV |
| `.../references/methodology.md` | Enfoque por capas + fuentes de tasas corners/cards + features recolectadas (§9.2) |
| `.../references/markets.md` | Columna "Capa" (MCP vs Manual) + cobrar SIEMPRE ambos lados O/U por línea de corners/cards |
| `.../references/currentness.md` | Fixtures vía `get_football_matches` (rest_days/congestión), lineups vía `get_match_details` |
| `.agents/skills/football-betting-review/SKILL.md` | Resultados vía APIfootball `get_football_matches`/`get_match_details` (fallback websearch) + CLV con Historical Odds |
| `AGENTS.md` | Sección "MCPs disponibles y cuándo usarlos" + garantía corners/cards y features (§9) |

---

## 11. Troubleshooting

| Problema | Solución |
|----------|----------|
| `soccer-mcp: command not found` | Usar `python3 -m soccer_server`; verificar `pip show football-data-mcp` |
| `collect-data` falla por navegador | Instalar Chromium: `brew install --cask chromium` |
| Odds API devuelve `401` | Verificar `ODDS_API_KEY` exportada y `source ~/.zshrc` |
| `remaining_requests: 0` | Plan gratuito agotado (500/mes); esperar reinicio mensual o mover requests a `webfetch` |
| Cuota de Betplay/Wplay no encontrada | Flujo manual (§8.4 capa 2); estas casas NO están en The Odds API |
| APIfootball devuelve `403/429` | Limite 100 req/día alcanzado; priorizar herramientas de menor costo |
| signature_match no coincide en APIfootball | Usar el valor exacto de `match_id` devuelto por `get_football_matches` |
| `ODDS_API_SPORT` no tiene la liga | Cambiar sport key o consultar REST vía `webfetch` |
| Partido sin odds de corners/cards | Consignar "no disponible" explícitamente; NO inventar cuota |

---

## Checklist de ejecución (para el equipo autorizado)

```
[x] python3 >= 3.10, node >= 18   (Python 3.12.14 vía uv; node v22)
[ ] ODDS_API_KEY obtenida (the-odds-api.com, plan FREE) → rellenar .env
[ ] APIFOOTBALL_KEY obtenida (apifootball.com/register) → rellenar .env y export (o source .env)
[~] Variables de entorno exportadas y recargadas   (APIFOOTBALL_KEY pendiente de export)
[x] Instalar football-data-mcp   (uv tool install; soccer-mcp/collect-data en ~/.local/bin)
[~] collect-data (descarga inicial)   (EN CURSO — 14/09/2026, log en scratch/collect-data.log)
[x] opencode.jsonc creado con los 3 MCPs (raíz del proyecto)
[ ] opencode mcp list → 3 connected   (requiere datos completos + keys; hoy: football-stats/odds-api pendientes de key/datos, apifootball falla con 400 por key vacía)
[ ] Probar get_team_stats / compare_teams (football-stats)
[ ] Probar get_odds / get_event_odds (odds-api)
[ ] Probar get_football_matches / get_match_details (apifootball)
[x] Aplicar cambios de archivos de skill (tabla §10)
[ ] Ejecutar un análisis piloto y validar que corners/cards aparecen en el artefacto
```

**Desviaciones de la implementación (ver cabecera):** `uvx` en lugar de `npx` para `mcp-odds-api` + pin `mcp<2`; `.env` leído solo por `uvx --env-file`; `APIFOOTBALL_KEY` debe exportarse en el shell; Python 3.12.14 instalado; `soccer-mcp` requiere el dataset completo (duckdb falla hasta que `collect-data` termine).