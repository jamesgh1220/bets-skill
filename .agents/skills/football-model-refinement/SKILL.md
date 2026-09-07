---
name: football-model-refinement
description: Refina el modelo predictivo de forma controlada con backtesting, validación out-of-sample y versionado.
---

# Football Model Refinement

## Propósito

Tomar el diagnóstico de `football-model-evaluation` y proponer mejoras controladas al modelo. **NUNCA modificar directamente sin aprobación.**

## Flujo del Proceso

```
1. Cargar diagnóstico de evaluation
2. Identificar problemas específicos
3. Buscar datos históricos automáticamente
4. Proponer cambios controlados
5. Ejecutar backtesting out-of-sample
6. Comparar con versión actual
7. Esperar aprobación del usuario
8. Si aprueba: crear nueva versión en models/
9. Si rechaza: descartar cambios
```

## Fuentes de Datos

- **Diagnóstico**: Resultado de `football-model-evaluation`
- **Modelo actual**: `models/model-v{X}.{Y}.json` (versión active)
- **Datos históricos**: Búsqueda automática de estadísticas, resultados, xG
- **Artefactos**: `artifacts/analisis-*.md` (predicciones anteriores, separadas por modelo de IA y versión del motor)

## Proceso Detallado

### Paso 1: Cargar Diagnóstico

1. Leer diagnóstico generado por `football-model-evaluation`
   - El diagnóstico debe identificar una única serie `modelo-ia + versión-motor`; no usar resultados agregados de series distintas.
2. Identificar mercados con problemas de calibración
3. Identificar métricas deterioradas vs versión anterior
4. Identificar señales de sobreajuste

### Paso 2: Identificar Problemas

Clasificar cada problema:

| Tipo | Ejemplo | Prioridad |
|------|---------|-----------|
| **Calibración** | Over/Under 2.5 subestimado en tramos 0.4-0.6 | Alta |
| **Sobreajuste** | Train Brier 0.12, Test Brier 0.22 | Crítica |
| **Sensibilidad** | Parámetro X varía mucho con cambios pequeños | Media |
| **Estabilidad** | ROI deteriorándose en últimos 3 meses | Alta |
| **CLV negativo** | Modelo peor que el mercado en BTTS | Alta |

### Paso 3: Buscar Datos Históricos

**Búsqueda automática** para respaldar cambios propuestos:

1. **Resultados recientes**: Buscar resultados de las ligas evaluadas
2. **Estadísticas xG**: Buscar datos de xG/xGA recientes
3. **Tendencias de mercado**: Cómo se han movido las cuotas
4. **Cambios estructurales**: Transferencias, lesiones, cambios de entrenador

Fuentes prioritarias:
- Sitios oficiales de ligas
- Proveedores estadísticos fiables
- Agregadores de datos

### Paso 4: Proponer Cambios

Para cada problema identificado, generar propuesta con:

```
=== PROPUESTA DE CAMBIO ===
Problema: {descripción del problema}
Mercado afectado: {mercado}
Cambio propuesto: {tipo de cambio}
Parámetro: {nombre del parámetro}
Valor actual: {valor}
Valor propuesto: {nuevo valor}
Justificación: {por qué este cambio}
Riesgo: {bajo/medio/alto}
```

**Tipos de cambios permitidos:**

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **weight_adjustment** | Cambiar pesos de componentes | Poisson: 0.35 → 0.30 |
| **feature_weight** | Cambiar importancia de features | xG_for: 0.15 → 0.12 |
| **threshold** | Ajustar umbrales de decisión | min_edge: 0.03 → 0.04 |
| **calibration** | Ajustar tramos de calibración | Tramos O/U: recalibrar |
| **feature_removal** | Remover feature problemática | Excluir travel_distance |
| **feature_addition** | Agregar nueva feature | Incluir momentum_score |
| **component_toggle** | Habilitar/deshabilitar componente | Deshabilitar regression |

### Paso 5: Backtesting Out-of-Sample

**Obligatorio antes de proponer aprobación:**

1. **Separar datos**: 70% entrenamiento, 30% validación (por tiempo)
2. **Entrenar modelo actual** con datos de entrenamiento
3. **Entrenar modelo propuesto** con mismos datos
4. **Evaluar ambos** en conjunto de validación
5. **Comparar métricas**:

```
=== BACKTESTING ===
Período train: {inicio} - {fin}
Período test: {inicio} - {fin}

                    Actual    Propuesto   Delta
Brier Score:        {v1}      {v2}        {d}
Log Loss:           {v1}      {v2}        {d}
Calibration Error:  {v1}      {v2}        {d}
CLV:                {v1}      {v2}        {d}
ROI:                {v1}      {v2}        {d}
Win Rate:           {v1}      {v2}        {d}
```

### Paso 6: Criterios de Aprobación

El cambio se aprueba SOLO si:

1. **Brier mejora** (disminuye) en test set
2. **Calibration error disminuye** o se mantiene
3. **CLV no se deteriora** significativamente
4. **No hay sobreajuste nuevo** (ratio train/test aceptable)
5. **Mejora es consistente** across folds temporales

**Rechazar si:**
- Brier empeora en test
- CLV disminuye > 0.01
- Nuevo sobreajuste detectado
- Mejora solo en train (no generaliza)

### Paso 7: Esperar Aprobación

**NUNCA crear versión sin aprobación explícita del usuario.**

Presentar:
1. Resumen de cambios propuestos
2. Resultados de backtesting
3. Comparativa con versión actual
4. Riesgos identificados
5. Recomendación (aprobar/rechazar)

El usuario responde:
- `aprobar` → Crear nueva versión
- `rechazar` → Descartar cambios
- `modificar` → Ajustar propuesta

### Paso 8: Crear Nueva Versión

Si se aprueba:

1. **Determinar número de versión**:
   - Cambio menor: v1.0 → v1.1
   - Cambio mayor: v1.0 → v2.0

2. **Crear archivo** `models/model-v{X}.{Y}.json`:
   - Copiar versión actual
   - Aplicar cambios aprobados
   - Actualizar metadata (versión, fecha, parent, status)
   - Actualizar métricas de validación

3. **Actualizar versiones anteriores**:
   - Versión anterior → status: `deprecated`
   - Nueva versión → status: `active`

4. **Actualizar changelog**:
   - Agregar entrada en `models/changelog.md`
   - Documentar cambios, métricas, justificación

5. **Reportar a usuario**:
   - Confirmar creación de nueva versión
   - Resumen de cambios implementados
   - Métricas de mejora

## Reglas Críticas

- **NUNCA modificar el modelo directamente.** Siempre proponer y esperar aprobación.
- **NUNCA saltar backtesting.** Todo cambio debe ser validado out-of-sample.
- **NUNCA sobrescribir versiones.** Crear nueva versión, no modificar existente.
- **NUNCA aprobar automáticamente.** Siempre esperar decisión del usuario.
- **Documentar todo.** Cada cambio debe tener justificación y métricas.
- **Priorizar sobre calibración.** La calibración es más importante que el ROI.
- **Un cambio a la vez.** No combinar múltiples cambios en una propuesta.
- **Series aisladas:** La identidad de la IA que generó el análisis es trazabilidad experimental; un refinement solo cambia el motor predictivo indicado, nunca esa identidad. Solicitar una serie concreta si el diagnóstico no la especifica.

Consultar `references/refinement-methodology.md` y `versioning-protocol.md`.
