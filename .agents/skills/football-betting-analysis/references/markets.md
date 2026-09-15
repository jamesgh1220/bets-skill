# Betting Markets

Analizar 1X2, double chance, DNB, Asian Handicap, Over/Under, BTTS, team totals y player props cuando existan datos suficientes.

**Over/Under: evaluar SIEMPRE los dos lados.** Para cada línea (1.5, 2.5, 3.5) capturar la cuota de `over_X` y de `under_X` e informar ambos en el análisis. Un lado puede tener value aunque el otro no lo tenga; el lado sin value debe consignarse en `NO BET` con su EV del motor, nunca omitirse.

**Corners y Cards: obligatorios y SIEMPRE con ambos lados O/U.** El motor activa estos mercados automáticamente (`_count_market_probabilities`) cuando existen los 8 campos de entrada. Para cada línea de corners (8.5/9.5/10.5) y de cards (3.5/4.5/5.5) se captura over Y under. Betsson es la fuente principal de cuota; capa 2 (manual) si The Odds API no la cubre. Sin cuota verificable: "no disponible", nunca inventar.

Player props requieren minutos, rol, titularidad, volumen, rival, balón parado y sustitución esperada.

Para cada candidato comparar: cuota, probabilidad implícita, probabilidad modelo, cuota justa, edge, EV, robustez y stake.

Calcular `minimum_acceptable_odds`. Detectar mercados correlacionados y reducir exposición conjunta.

## Bookmakers Colombianos

Las cuotas se obtienen por capas (ver `bookmakers.md`): **Capa 1** `odds-api` MCP (The Odds API) cuando el mercado/casa esté cubierto; **Capa 2** investigación manual para el resto:

| Bookmaker | Capa | 1X2 | O/U | BTTS | Handicap | DO | Correct Score | Player Props | Corners | Cards |
|-----------|------|-----|-----|------|----------|-----|---------------|--------------|---------|-------|
| Betsson | 1 (MCP) + 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Betplay | 2 (manual) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| Wplay | 2 (manual) | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Rushbet | 2 (manual) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| Zamba | 2 (manual) | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Sportium | 2 (manual) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |

**Leyenda:**
- ✓ = Disponible
- ✗ = No disponible
- DO = Doble Oportunidad
- Capa 1 = The Odds API vía MCP (`odds-api`); Capa 2 = investigación manual

### Proceso de Obtención de Cuotas

1. Buscar cuotas en todos los bookmakers para el partido y mercado específicos.
2. Identificar la **mejor cuota** disponible para cada selección.
3. Usar la mejor cuota para calcular edge y EV.
4. Si un bookmaker no tiene el mercado, usar los demás.
5. Si ninguno tiene el mercado, reportar "mercado no disponible".
