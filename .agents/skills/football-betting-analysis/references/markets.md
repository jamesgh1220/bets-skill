# Betting Markets

Analizar 1X2, double chance, DNB, Asian Handicap, Over/Under, BTTS, team totals y player props cuando existan datos suficientes.

Player props requieren minutos, rol, titularidad, volumen, rival, balón parado y sustitución esperada.

Para cada candidato comparar: cuota, probabilidad implícita, probabilidad modelo, cuota justa, edge, EV, robustez y stake.

Calcular `minimum_acceptable_odds`. Detectar mercados correlacionados y reducir exposición conjunta.

## Bookmakers Colombianos

Las cuotas se obtienen de las siguientes casas de apuestas colombianas (ver `bookmakers.md` para detalles completos):

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

### Proceso de Obtención de Cuotas

1. Buscar cuotas en todos los bookmakers para el partido y mercado específicos.
2. Identificar la **mejor cuota** disponible para cada selección.
3. Usar la mejor cuota para calcular edge y EV.
4. Si un bookmaker no tiene el mercado, usar los demás.
5. Si ninguno tiene el mercado, reportar "mercado no disponible".
