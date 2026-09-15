# Currentness Protocol

La actualidad es condición de entrada.

## Filtrado por Fechas (CRÍTICO)

- **Solo analizar partidos dentro del rango de fechas proporcionado en la invocación.**
- Registrar explícitamente: `requested_date_range`, `included_matches`, `excluded_matches`.
- Si un partido de las ligas especificadas cae fuera del rango, **excluirlo del análisis**.
- No analizar partidos "cercanos" al rango por si acaso. Respetar límites exactos.
- Ejemplo: Si se solicita `5 de septiembre de 2026`, un partido el `4 de septiembre` o el `8 de septiembre` **no se analiza**.

Registrar `analysis_date`, `match_date` e `information_cutoff`; nunca usar información posterior al cutoff.

Verificar equipo: identidad actual, competición, entrenador, plantilla, entradas/salidas, lesiones, suspensiones, disponibilidad, calendario, congestión y cambios tácticos.

Verificar jugador: club actual, fecha de transferencia, rol, minutos esperados, lesión, sanción y disponibilidad. Nunca trasladar automáticamente estadísticas de un club a otro.

**Fuentes vía MCPs (apifootball):**
- Fixtures del rango: `get_football_matches` (filtro estricto por fechas; rango máx. 15 días por request).
- `rest_days` / congestión: `get_football_matches` — días desde el último partido de cada equipo (incluye copas/Europa).
- Lineups / lesiones confirmadas en alineación: `get_match_details` (include lineups).
- Standings (importancia/rotaciones): `get_football_standings`.

Prioridad de fuentes: club oficial; competición/federación; proveedor estadístico fiable; medio fiable; agregador.

Clasificar hechos como `confirmed`, `probable`, `uncertain` o `rumor`. Los rumores no son hechos.

Separar periodos antes/después de cambios de entrenador. Al inicio de temporada combinar datos nuevos, anteriores, fuerza histórica, plantilla y entrenador actuales y aumentar incertidumbre.
