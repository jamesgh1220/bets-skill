# Versioning Protocol

## Convención de Versiones

Formato: `v{MAJOR}.{MINOR}`

### MAJOR (v1.0 → v2.0)

Cambios significativos que alteran el comportamiento del modelo:

- Cambio de modelo base (ej: de Poisson a Dixon-Coles)
- Remoción o adición de componente del ensemble
- Cambio en la arquitectura del modelo
- Cambio en la estrategia de features

### MINOR (v1.0 → v1.1)

Cambios que refinan sin alterar la arquitectura:

- Ajuste de pesos de componentes
- Ajuste de pesos de features
- Recalibración de mercados
- Ajuste de umbrales
- Remoción de features problemáticas

## Estados de Versión

| Estado | Significado |
|--------|-------------|
| `active` | Versión actualmente en uso para predicciones |
| `deprecated` | Versión anterior, ya no se usa pero se conserva |
| `experimental` | Versión en pruebas, no aprobada aún |

**Reglas de estados**:
- Solo puede haber UNA versión `active` a la vez
- Cuando se crea nueva versión `active`, la anterior pasa a `deprecated`
- `experimental` solo se usa durante backtesting

## Estructura del Archivo de Versión

Cada `models/model-v{X}.{Y}.json` contiene:

```json
{
  "version": "1.1",
  "created_at": "2026-08-25T12:00:00Z",
  "parent_version": "1.0",
  "status": "active",
  "description": "Descripción del cambio",
  "model_type": "ensemble",
  "components": { ... },
  "markets": { ... },
  "features": { ... },
  "weighting": { ... },
  "filters": { ... },
  "calibration": { ... },
  "uncertainty": { ... },
  "validation": {
    "backtest_period": "...",
    "out_of_sample_period": "...",
    "metrics": { ... }
  }
}
```

## Changelog

Registrar cada versión en `models/changelog.md`:

```markdown
## vX.Y — Fecha

- **Cambios:** Descripción
- **Motivo:** Por qué
- **Métricas antes:** Brier, Log Loss, etc.
- **Métricas después:** Brier, Log Loss, etc.
- **Aprobado por:** usuario
```

## Proceso de Creación de Versión

1. **Determinar número**:
   - Cambio mayor → incrementar MAJOR
   - Cambio menor → incrementar MINOR

2. **Crear archivo**:
   - Copiar versión `active` actual
   - Aplicar cambios aprobados
   - Actualizar metadata:
     - `version`: nuevo número
     - `created_at`: fecha actual
     - `parent_version`: versión anterior
     - `status`: "active"
     - `description`: descripción del cambio
   - Actualizar `validation.metrics` con métricas del backtesting

3. **Actualizar estados**:
   - Versión anterior: `status` → "deprecated"
   - Nueva versión: `status` → "active"

4. **Actualizar changelog**:
   - Agregar entrada en `models/changelog.md`
   - Incluir métricas comparativas

5. **Verificar integridad**:
   - Confirmar que solo hay una versión `active`
   - Confirmar que `parent_version` es correcto
   - Confirmar que métricas están registradas

## Rollback

Si una versión nueva causa problemas:

1. **Identificar problema**: Ejecutar `football-model-evaluation`
2. **Decidir rollback**: Si problema es grave, volver a versión anterior
3. **Cambiar estados**:
   - Versión problemática: `status` → "deprecated"
   - Versión anterior: `status` → "active"
4. **Documentar**: Agregar entrada en changelog explicando rollback
5. **Investigar**: Por qué falló y cómo evitarlo en el futuro

**NUNCA eliminar versiones anteriores.** Solo cambiar su estado.

## Comparación de Versiones

Para comparar dos versiones:

```
=== COMPARACIÓN DE VERSIONES ===
v1.0 (anterior) → v1.1 (actual)

Métricas:
Brier:         0.191 → 0.184 (-0.007) ✅
Log Loss:      0.421 → 0.408 (-0.013) ✅
Calibration:   0.032 → 0.018 (-0.014) ✅
CLV:           0.014 → 0.018 (+0.004) ✅
ROI:           3.2%  → 4.8%  (+1.6%)  ✅

Cambios realizados:
- weight_adjustment: Poisson 0.35 → 0.30
- weight_adjustment: DC 0.30 → 0.35
- calibration: Recalibración de tramos Over/Under 2.5

Conclusión: v1.1 mejora consistentemente sobre v1.0
```

## Reglas

1. **Nunca sobrescribir** versiones existentes
2. **Nunca eliminar** versiones anteriores
3. **Siempre documentar** cambios en changelog
4. **Siempre registrar** métricas de validación
5. **Siempre mantener** solo una versión `active`
6. **Siempre validar** antes de aprobar nueva versión
