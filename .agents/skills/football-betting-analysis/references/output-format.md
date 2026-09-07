# Output Format

El artefacto es un contrato de datos para review, evaluation y refinement. No se publica ningún análisis que no supere `scripts/validate_analysis_artifact.py`.

## Pantalla

Mostrar primero `Ranking Global` de los candidatos con value y después la selección final de 0 a 6 picks. Cada pick mostrado incluye cuota, probabilidad modelo e implícita, justa, edge, EV, stake, confianza, incertidumbre, razones, riesgos y cuota mínima. Incluir siempre los `NO BET` relevantes y el portfolio.

## Artefacto obligatorio

La plantilla siguiente debe respetarse literalmente en títulos, etiquetas y columnas. Sustituir todos los marcadores; para cero picks conservar las tablas sin filas y escribir `- Ninguno.` en NO BET cuando corresponda.

```markdown
# Análisis de Apuestas — {fecha_en_texto}

## Metadatos
- **Fecha de análisis:** {YYYY-MM-DDTHH:MM:SS±HH:MM}
- **Fecha(s) de partido:** {fecha o rango solicitado}
- **Information cutoff:** {YYYY-MM-DDTHH:MM:SS±HH:MM}
- **Modelo de IA:** {identificador recibido en modelo}
- **Versión del motor predictivo:** {model-vX.Y}
- **Ligas analizadas:** {lista}
- **Rango de fechas solicitado:** {rango original}
- **Partidos en universo:** {N}
- **Picks iniciales con value:** {N}
- **Picks finales seleccionados:** {N, entre 0 y 6}

## Universo Analizado
{partidos incluidos y exclusiones por fecha/liga}

## Ranking Global
| Rank | Partido | Mercado | Selección | Cuota | Prob. | Justa | Edge | EV | Stake | Confianza |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| ... |

## Picks Recomendados (Top {N})
| Rank | Partido | Mercado | Selección | Cuota | Prob. | Justa | Edge | EV | Stake | Confianza |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Detalle de Picks
### Pick 1: {Equipo A} vs {Equipo B}
- **Mercado:** ...
- **Selección:** ...
- **Cuota:** ...
- **Probabilidad modelo:** ...
- **Probabilidad implícita:** ...
- **Cuota justa:** ...
- **Edge:** ...
- **EV:** ...
- **Cuota mínima:** ...
- **Stake:** ...u
- **Confianza:** ...
- **Incertidumbre:** ...
- **Por qué:** ...
- **Riesgos:** ...
- **Fuentes:** ...

## NO BET / Excluidos
- {partido/mercado}: {razón}, o `Ninguno.`

## Portfolio y Correlaciones
- **Exposición total:** {total_stake}u
- **Correlaciones detectadas:** ...
- **Ajuste de stake por correlación:** ...

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| {Pick 1} | PENDIENTE | — | — |
```

## Nombre y publicación

- Formato final: `artifacts/analisis-YYYY-MM-DD--{modelo-slug}--vNN.md`.
- `{modelo-slug}` es la versión minúscula, ASCII y con guiones del parámetro obligatorio `modelo:`. El valor original se mantiene en `Modelo de IA`.
- La revisión comienza en `v01`; ejecuciones posteriores con misma fecha y modelo reciben `v02`, `v03`, etc.
- Crear un temporal único en `scratch/`, validarlo y publicarlo exclusivamente con:

  ```bash
  python3 scripts/publish_analysis_artifact.py --input {temporal} --analysis-date {YYYY-MM-DD} --model "{modelo}"
  ```

- Si el comando falla, corregir el temporal y repetir. No terminar ni presentar la corrida como completada hasta que el comando imprima la ruta final.

## Tracking de Picks

Estados permitidos: `PENDIENTE`, `GANADA`, `PERDIDA`, `PUSH` y `VOID`. Review actualiza exclusivamente las filas de Tracking del artefacto publicado.
