# Output Format

## Pantalla — Ranking Global (pre-selección)

Mostrar primero el ranking completo de todos los candidatos con value (antes de la selección top 0-6):

| Rank | Partido | Mercado | Selección | Cuota | Prob. | Justa | Edge | EV | Stake | Confianza |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|

Ordenar por value robusto, no por cuota alta.

Luego mostrar la **selección final (0-6 picks)** con el siguiente formato en pantalla:

---

## Pantalla — Picks Seleccionados (Top 0-6)

### Resumen
- **Picks candidatos totales:** N
- **Picks seleccionados:** M (M <= 6)
- **Excluidos por:** (breve justificación de por qué no entraron)

### Tabla Top Picks

| Rank | Partido | Mercado | Selección | Cuota | Prob. | Justa | Edge | EV | Stake | Confianza |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|

---

## Pick (detalle de cada uno)

**Partido:** A vs B
**Mercado:** ...
**Selección:** ...
**Cuota:** ...
**Probabilidad modelo:** ...
**Probabilidad implícita:** ...
**Cuota justa:** ...
**Edge:** ...
**EV:** ...
**Cuota mínima:** ...
**Stake:** ...
**Confianza:** ...
**Incertidumbre:** ...

**Por qué:** ...
**Riesgos:** ...
**Condición de entrada:** cuota >= cuota mínima.

Incluir NO BET y portfolio/correlaciones.

---

## Artefacto .md — Estructura del Archivo

Cada análisis genera un archivo en `artifacts/analisis-{dia}-{mes}-{año}.md` con esta estructura exacta:

```markdown
# Análisis de Apuestas — {fecha_en_texto}

## Metadatos
- **Fecha de análisis:** {analysis_date}
- **Ligas analizadas:** {lista de ligas}
- **Rango de fechas solicitado:** {rango}
- **Partidos en universo:** {N}
- **Picks iniciales con value:** {N_candidatos}
- **Picks finales seleccionados:** {N_seleccionados}

## Picks Recomendados (Top {N})

| Rank | Partido | Mercado | Selección | Cuota | Prob. | Justa | Edge | EV | Stake | Confianza |
|------|---------|---------|-----------|-------|-------|-------|------|-----|-------|-----------|
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
- **Stake:** ...u ({descripción})
- **Confianza:** ...
- **Incertidumbre:** ...
- **Por qué:** ...
- **Riesgos:** ...
- **Fuentes:** ...

### Pick 2: ...
(repetir para cada pick)

## Portfolio y Correlaciones
- **Exposición total:** {total_stake}u
- **Correlaciones detectadas:** ...
- **Ajuste de stake por correlación:** ...

## Tracking
- **Estado:** PENDIENTE
- **Resultado:** (completar después del partido)
- **Profit/Loss:** (completar después del partido)
```

### Convención de Nombres de Archivo

- Formato: `analisis-{dia}-{mes}-{año}.md`
- Mes en español minúsculas: enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre
- Ejemplos:
  - `analisis-26-agosto-2026.md`
  - `analisis-5-septiembre-2026.md`
  - `analisis-15-octubre-2026.md`

### Tracking de Picks

El artefacto incluye una sección `## Tracking` con estado:
- `PENDIENTE` — Pick registrado, esperando resultado
- `GANADA` — Pick ganado, profit positivo
- `PERDIDA` — Pick perdido
- `PUSH` — Empate/devolución
- `VOID` — Anulado

La skill `football-betting-review` puede leer estos artefactos para calcular métricas de rendimiento.
