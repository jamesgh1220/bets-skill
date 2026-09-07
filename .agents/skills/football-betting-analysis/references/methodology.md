# Methodology

## Construcción del Universo

**Universo = intersección(ligas, fechas, partidos)**

El universo de análisis se define estrictamente por la intersección de los tres parámetros de invocación:

1. **Ligas**: Solo partidos de las ligas especificadas.
2. **Fechas**: Solo partidos cuya fecha de juego esté dentro del rango proporcionado.
3. **Partidos**: 
   - Si `partidos:todos` → todos los partidos de las ligas en las fechas.
   - Si se listan partidos específicos → solo esos partidos (verificando que estén en las ligas y fechas correctas).

**Ejemplo:**
- Invocación: `ligas:Premier League, LaLiga fechas:5-7 de septiembre de 2026 partidos:todos`
- Universo: Todos los partidos de Premier League y LaLiga jugados entre el 5 y 7 de septiembre de 2026.
- **Excluidos**: Partidos de Serie A, partidos de Premier League el 4 de septiembre, partidos de LaLiga el 8 de septiembre.

## Métricas
Ataque: goles, xG, tiros, tiros a puerta, grandes ocasiones, xG/tiro, toques en área, progresiones, creación y balón parado.

Defensa: goles concedidos, xGA, tiros concedidos, tiros a puerta concedidos, grandes ocasiones concedidas, PPDA, errores y balón parado.

Contexto: localía, descanso, viajes, congestión, calendario, competición, importancia, rotaciones y Europa/copas.

Jugadores: minutos esperados, xG, xA, tiros, tiros a puerta, rol, penaltis, balón parado y disponibilidad.

Ajustar por fuerza de oposición cuando sea posible. Combinar temporada actual, forma reciente, temporada anterior y ratings históricos.

Modelos: Poisson/Dixon-Coles, ratings, regresión, Bayes, Monte Carlo y ensembles.

`implied_probability = 1 / odds`
`fair_odds = 1 / p`
`edge = p - implied_probability`
`EV = p * odds - 1`

Usar escenarios conservador/base/optimista. Reducir stake si el value desaparece con pequeños cambios.

## Obtención de Cuotas (Bookmakers Colombianos)

El sistema busca cuotas en las siguientes casas de apuestas colombianas:

1. **Betplay** (regulado por Coljuegos) - https://www.betplay.com.co
2. **Betsson** (internacional) - https://www.betsson.com/co
3. **Wplay** (local) - https://www.wplay.co
4. **Rushbet** (local) - https://www.rushbet.co
5. **Zamba** (local) - https://www.zamba.bet
6. **Sportium** (internacional) - https://sportium.es/apostas-colombia

### Protocolo de Scraping

Para cada partido en el universo:

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

### Comparación entre Bookmakers

Para cada partido y mercado:

1. Obtener cuotas de todos los bookmakers disponibles.
2. Identificar la **mejor cuota** para cada selección.
3. Calcular el **margen promedio** del mercado.
4. Detectar **outliers** (cuotas significativamente diferentes).
5. Usar la mejor cuota disponible para calcular edge y EV.
