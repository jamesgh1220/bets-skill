# Result Fetching Protocol

## Objetivo

Buscar automáticamente los resultados de los partidos usando web search y actualizar los artefactos con los estados de las apuestas.

## Proceso de Búsqueda

### Paso 1: Identificar Partidos a Buscar

De los artefactos `artifacts/analisis-*.md`, extraer:

- **Partido**: Equipo Local vs Equipo Visitante
- **Fecha del partido**: Fecha de kickoff
- **Mercado**: 1X2, O/U 2.5, BTTS, etc.
- **Selección**: Qué se apostó
- **Estado actual**: PENDIENTE

### Paso 2: Filtrar por Fecha

Solo buscar resultados de partidos que **ya jugaron**:

```
Si fecha_partido > fecha_actual → NO BUSCAR (partido pendiente)
Si fecha_partido <= fecha_actual → BUSCAR resultado
```

**Importante**: No buscar partidos futuros. No adelantar información.

### Paso 3: Formular Búsqueda Web

Usar `websearch` con consultas estratégicas:

#### Formato Principal

```
"[Equipo Local] vs [Equipo Visitante] resultado [fecha_completa]"
```

#### Formatos Alternativos (si el principal falla)

```
"[Equipo Local] [Equipo Visitante] score"
"[Liga] [Equipo Local] vs [Equipo Visitante] resultado [fecha]"
"[Equipo Local] [goles] - [goles] [Equipo Visitante]"
"resultado [Liga] [fecha]"
```

#### Ejemplos

```
"Arsenal vs Manchester City resultado 25 agosto 2026"
"Barcelona Real Madrid score"
"Premier League Arsenal vs Manchester City resultado"
```

### Paso 4: Parsear Resultado

Del resultado de la búsqueda, extraer:

1. **Goles del Local**: {home_goals}
2. **Goles del Visitante**: {away_goals}
3. **Marcador**: {home_goals} - {away_goals}
4. **Ganador**: Local / Empate / Visitante

#### Reglas de Parsing

- Buscar patrones como "2-1", "2 - 1", "2 a 1"
- Verificar que los números correspondan a goles
- Confirmar con múltiples fuentes si es posible

### Paso 5: Determinar Resultado del Pick

Según el mercado del pick:

#### 1X2

```
Si selección = "Home" y local gana → GANADA
Si selección = "Away" y visitante gana → GANADA
Si selección = "Draw" y hay empate → GANADA
Cualquier otro caso → PERDIDA
```

#### Over/Under 2.5

```
goles_totales = home_goals + away_goals
Si selección = "Over" y goles_totales > 2.5 → GANADA
Si selección = "Under" y goles_totales < 2.5 → GANADA
Si goles_totales = 2.5 → PUSH
```

#### BTTS (Both Teams To Score)

```
Si selección = "Yes" y home_goals > 0 y away_goals > 0 → GANADA
Si selección = "No" y (home_goals = 0 o away_goals = 0) → GANADA
```

#### Double Chance 1X (Home or Draw)

```
Si local gana o empata → GANADA
Si visitante gana → PERDIDA
```

#### Double Chance X2 (Draw or Away)

```
Si visitante gana o empata → GANADA
Si local gana → PERDIDA
```

#### Double Chance 12 (Home or Away)

```
Si hay ganador (no empate) → GANADA
Si empata → PERDIDA
```

#### Asian Handicap

```
Aplicar handicap al marcador
Si resultado ajustado gana → GANADA
Si resultado ajustado pierde → PERDIDA
Si resultado ajustado empata → PUSH
```

#### Team Totals

```
goles_equipo = goles del equipo seleccionado
Si selección = "Over X" y goles_equipo > X → GANADA
Si selección = "Under X" y goles_equipo < X → GANADA
```

### Paso 6: Calcular Profit

```
Si GANADA: profit = stake × (cuota - 1)
Si PERDIDA: profit = -stake
Si PUSH: profit = 0
Si VOID: profit = 0
```

### Paso 7: Actualizar Artefacto

Modificar el archivo `artifacts/analisis-*.md`:

1. Cambiar `Estado: PENDIENTE` → `Estado: GANADA` (o PERDIDA/PUSH/VOID)
2. Agregar `Resultado: {home_goals} - {away_goals}`
3. Agregar `Profit: {profit}u`

## Manejo de Errores

### Partido No Encontrado

Si la búsqueda no devuelve resultado claro:

1. Intentar formato de búsqueda alternativo
2. Si persiste → mantener como `PENDIENTE`
3. Reportar en la salida que no se encontró resultado

### Partido Aplazado/Cancelado

Si se detecta que el partido no se jugó:

1. Marcar como `VOID`
2. Profit = 0
3. Reportar en la salida

### Datos Ambiguos

Si el resultado no es claro:

1. Mantener como `PENDIENTE`
2. Solicitar verificación manual al usuario
3. No asumir resultado

## Validación de Resultados

Para cada resultado encontrado:

1. **Verificar fuente**: Usar sitios confiables (sitios oficiales, medios deportivos reconocidos)
2. **Cruzar información**: Si es posible, verificar con múltiples fuentes
3. **Consistencia**: Asegurar que el marcador sea consistente con la fecha y equipos

## Fuentes Prioritarias

1. Sitios oficiales de ligas (premierleague.com, laliga.com, etc.)
2. Medios deportivos internacionales (BBC Sport, ESPN, etc.)
3. Agregadores de resultados (FlashScore, Sofascore, etc.)

## Reporte de Resultados

Al finalizar la búsqueda, mostrar:

```
=== ACTUALIZACIÓN DE RESULTADOS ===
Artefacto: analisis-2026-08-25--gpt-5--v01.md
Partidos buscados: 4
Resultados encontrados: 3
Pendientes: 1

DETALLE:
✅ Arsenal vs Man City → 2-1 → GANADA (+0.75u)
✅ Barcelona vs Real Madrid → 3-2 → GANADA (+0.50u)
✅ Juventus vs Inter → 1-0 → PERDIDA (-0.50u)
⏳ AC Milan vs Napoli → Pendiente (partido hoy)
```
