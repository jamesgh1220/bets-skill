# Bookmakers Colombianos

## Configuración de Casas de Apuestas

### 1. Betplay (Coljuegos)
- **URL base:** https://www.betplay.com.co
- **Método:** Web scraping
- **Mercados disponibles:** 1X2, Over/Under, BTTS, Handicap, Doble Oportunidad, Total Goles, Correct Score
- **Moneda:** COP
- **Regulación:** Coljuegos
- **Notas:** Casa de apuestas regulada en Colombia. Cuotas actualizadas frecuentemente. Mercados completos para Liga BetPlay y ligas internacionales.

### 2. Betsson
- **URL base:** https://www.betsson.com/co
- **Método:** Web scraping
- **Mercados disponibles:** 1X2, Over/Under, BTTS, Handicap, Doble Oportunidad, Total Goles, Correct Score, Player Props, Corners, Cards
- **Moneda:** COP
- **Regulación:** Coljuegos
- **Notas:** Casa internacional con fuerte presencia en Colombia. Alta liquidez y cuotas competitivas. Amplia cobertura de ligas colombianas e internacionales.

### 3. Wplay
- **URL base:** https://www.wplay.co
- **Método:** Web scraping
- **Mercados disponibles:** 1X2, Over/Under, BTTS, Handicap, Doble Oportunidad, Total Goles
- **Moneda:** COP
- **Regulación:** Coljuegos
- **Notas:** Casa de apuestas popular en Colombia. Buena cobertura de Liga BetPlay y ligas sudamericanas. Cuotas competitivas en mercados principales.

### 4. Rushbet
- **URL base:** https://www.rushbet.co
- **Método:** Web scraping
- **Mercados disponibles:** 1X2, Over/Under, BTTS, Handicap, Doble Oportunidad, Total Goles, Correct Score
- **Moneda:** COP
- **Regulación:** Coljuegos
- **Notas:** Cuotas competitivas en Liga BetPlay. Interfaz fácil de usar. Promociones frecuentes para clientes colombianos.

### 5. Zamba
- **URL base:** https://www.zamba.bet
- **Método:** Web scraping
- **Mercados disponibles:** 1X2, Over/Under, BTTS, Handicap, Doble Oportunidad
- **Moneda:** COP
- **Regulación:** Coljuegos
- **Notas:** Enfocado en el mercado colombiano. Buena oferta en ligas locales. Cuotas estándar en mercados principales.

### 6. Sportium
- **URL base:** https://sportium.es/apostas-colombia
- **Método:** Web scraping
- **Mercados disponibles:** 1X2, Over/Under, BTTS, Handicap, Doble Oportunidad, Total Goles, Correct Score, Player Props
- **Moneda:** COP
- **Regulación:** Coljuegos
- **Notas:** Casa internacional con operación en Colombia. Amplia cobertura de mercados y ligas. Cuotas competitivas en mercados principales.

## Protocolo de Scraping

### Capas de Obtención de Cuotas

| Capa | Fuente | Bookmakers | Cuándo |
|------|--------|-----------|--------|
| **Capa 1 (MCP)** | `odds-api` (The Odds API vía MCP local `uvx mcp-odds-api`) | Betsson, 1xBet, Pinnacle, Unibet, Betano, William Hill | Siempre primero; registrar timestamp de captura y, tras el partido, **closing odds** para CLV |
| **Capa 2 (manual)** | Investigación del agente (websearch/webfetch) | Betplay, Wplay, Rushbet, Zamba, Sportium | Para cuotas faltantes o mercado corners/cards |
| **Capa 3 (agregadores)** | OddsPortal, FlashScore, SofaScore, BetExplorer | — | Respaldo si 1 y 2 fallan |

- Betplay, Wplay, Rushbet, Zamba **NO están** en The Odds API → siempre por capa 2.
- Betsson publica mercados de corners/cards → fuente principal de cuota para esos mercados (capa 2 si Odds API no lo cubre).
- **CLV**: registrar siempre la cuota de captura (timestamp). El cierre se obtiene luego con Historical Odds (`https://api.the-odds-api.com/v4/historical/sports/{sport}/odds/`) en el paso de review; el campo CLV de los modelos deja de ser `null`.

### Proceso General

1. **Verificar disponibilidad**: Confirmar que cada bookmaker está operativo y accesible.
2. **Buscar partido**: Localizar el partido específico en la plataforma del bookmaker.
3. **Extraer cuotas**: Obtener cuotas de todos los mercados disponibles para ese partido.
4. **Normalizar formato**: Convertir cuotas a formato decimal si es necesario.
5. **Calcular probability implied**: `implied = 1 / odds`.
6. **Almacenar**: Guardar cuotas con timestamp y metadatos del bookmaker.

### Prioridad de Búsqueda

1. **Betplay** (regulador local, cuotas de referencia en Colombia)
2. **Betsson** (alta liquidez, amplia cobertura)
3. **Wplay** (popular, buena cobertura local)
4. **Rushbet** (competitivo en Liga BetPlay)
5. **Zamba** (enfocado en Colombia)
6. **Sportium** (internacional, amplia oferta)

### Manejo de Errores

- Si un bookmaker no está accesible, continuar con los demás.
- Registrar qué bookmakers fallaron para análisis posterior.
- Si todos fallan, usar cuotas de un agregador como respaldo (OddsPortal, FlashScore).
- Nunca inventar cuotas: si no se puede obtener, reportar "cuota no disponible".

### Normalización de Cuotas

```python
# De fraccionales a decimales
decimal_odds = fractional_odds + 1

# De americanas a decimales
if american_odds > 0:
    decimal_odds = (american_odds / 100) + 1
else:
    decimal_odds = (100 / abs(american_odds)) + 1

# Probability implied
implied_probability = 1 / decimal_odds
```

## Mercados por Bookmaker

| Bookmaker | 1X2 | O/U | BTTS | Handicap | DO | Correct Score | Player Props |
|-----------|-----|-----|------|----------|-----|---------------|--------------|
| Betplay | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| Betsson | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Wplay | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| Rushbet | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| Zamba | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| Sportium | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Leyenda:**
- ✓ = Disponible
- ✗ = No disponible
- DO = Doble Oportunidad

## Comparación entre Bookmakers

Para cada partido y mercado, el sistema debe:

1. Obtener cuotas de todos los bookmakers disponibles.
2. Identificar la **mejor cuota** para cada selección.
3. Calcular el **margen promedio** del mercado.
4. Detectar **outliers** (cuotas significativamente diferentes).
5. Usar la mejor cuota disponible para calcular edge y EV.

### Ejemplo de Comparación

```
Partido: Junior vs Millonarios
Mercado: 1X2

Bookmaker    | Local | Empate | Visitante
-------------|-------|--------|----------
Betplay      | 1.85  | 3.40   | 4.20
Betsson      | 1.90  | 3.35   | 4.10
Wplay        | 1.82  | 3.45   | 4.25
Rushbet      | 1.88  | 3.38   | 4.15

Mejor cuota: Local 1.90 (Betsson), Empate 3.45 (Wplay), Visitante 4.25 (Wplay)
```

## Fuentes de Respaldo

Si el scraping directo falla, usar fuentes alternativas:

1. **OddsPortal** (oddsportal.com) - Agregador de cuotas
2. **FlashScore** (flashscore.com) - Resultados y cuotas en vivo
3. **SofaScore** (sofascore.com) - Estadísticas y cuotas
4. **BetExplorer** (betexplorer.com) - Historial de cuotas

Estas fuentes son útiles para:
- Verificar cuotas cuando un bookmaker no está accesible.
- Obtener cuotas históricas para análisis de tendencias.
- Comparar márgenes entre bookmakers.
