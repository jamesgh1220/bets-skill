# Changelog — Modelos

Registro de todas las versiones del modelo y sus cambios.

## Formato

```
## vX.Y — Fecha
- **Cambios:** Descripción de los cambios realizados
- **Motivo:** Por qué se hizo el cambio
- **Métricas antes:** Brier, Log Loss, calibration_error, ROI, CLV
- **Métricas después:** Brier, Log Loss, calibration_error, ROI, CLV
- **Aprobado por:** usuario
```

---

## v1.0 — 2026-08-25

- **Cambios:** Versión inicial del modelo ensemble (Poisson + Dixon-Coles + Ratings + Regression)
- **Motivo:** Punto de partida para el sistema de predicción
- **Métricas:** Pendientes de validación inicial
- **Aprobado por:** Sistema

---

## Historial

| Versión | Fecha | Cambio Principal | Brier | ROI | CLV |
|---------|-------|------------------|-------|-----|-----|
| v1.0 | 2026-08-25 | Versión inicial | — | — | — |
| v1.1 | 2026-09-07 | Mercados ampliados + selección probabilidad-primero | Pendiente | +2.21% (legacy, N=42) | Pendiente |
| v1.2 | 2026-09-07 | Recalibración Platt: 1X2 local/visitante + O/U 2.5 (ACTIVA) | 0.185 (OOS media 1X2) | Pendiente | Pendiente |
| v1.3 | 2026-09-17 | Recalibración Platt añadida a línea O/U 3.5 (ACTIVA) | test O/U 3.5: 0.231→0.211 | Pendiente | Pendiente |

## v1.2 — 2026-09-07 (ACTIVA → deprecada en v1.3)

## v1.1 — 2026-09-07 (experimental; no activo)

- **Cambios:** Líneas O/U 1.5, 2.5 y 3.5, BTTS, doble oportunidad, DNB y módulos independientes para corners/tarjetas; filtro de EV robusto y excepción limitada de cuota alta.
- **Motivo:** Reducir la exposición a underdogs de alta varianza sin sacrificar value comprobable.
- **Métricas antes/después:** Pendientes de backtest y validación out-of-sample por mercado y tramo de cuota. Se designa experimental para generar una serie de prueba nueva.
- **Aprobado por:** Usuario para desarrollo y prueba; activación pendiente de backtest obligatorio.

---

## v1.1 — 2026-09-07 (ACTIVA → deprecada en v1.2)

- **Cambios:** Activación oficial de v1.1 como modelo activo. Ajustes precautorios tras backtest: `over_under.min_edge` 0.03→0.04 y `btts.min_edge` 0.03→0.05 con `min_confidence` → `medium_high`.
- **Motivo:** Backtest sobre artefactos legacy (2026-08-27 a 2026-09-07, 42 picks resueltos) mostró sobreconfianza sistémica (EV medio ~18.7% vs ROI +2.21%), Under 2.5 sobreestimado (prob. modelo 54-58% vs 46.7% observado) y BTTS 0/2. El único mercado claramente rentable fue 1X2 visitante (+1.49u).
- **Métricas antes (v1.0 legacy):** ROI +2.21%, Win rate 40.48%, N=42, Stake 9.95u, Profit +0.22u, Max DD -1.83u, CLV sin datos.
- **Métricas después:** Pendientes de validación con la serie nueva (corner/tarjetas y mercados ampliados requieren serie propia).
- **Aprobado por:** Usuario (2026-09-07).

---

## v1.2 — 2026-09-07 (ACTIVA)

- **Cambios:** Recalibración de probabilidades con **Platt scaling** sobre `logit(prob)` para los mercados 1X2 (Local y Visitante) y Over/Under 2.5. Coeficientes persistidos en `calibration.params`. La calibración se aplica automáticamente en `calc_engine.run_ensemble` antes de evaluar value.
- **Motivo:** El backtest de v1.1 mostró sobreconfianza sistémica (EV model ~18.7% vs ROI +2.21%) y miscalibración en O/U 2.5 e 1X2. Se implementó por fin calibración real (antes inexistente: solo metadatos). Prioridad del proyecto: calibración > ROI.
- **Método evaluado:** Isotonic regression rechazada — infla LogLoss en muestra pequeña (clips a 0/1, e.g. 0.96 vs 0.67 en O/U 2.5). **Platt elegida**: robusta, monotónica, paramétrica (2 coefs por mercado).
- **Métricas antes (sin calibrar, test OOS n=46):**
  - Over 2.5: Brier 0.2425 · LogLoss 0.6775 · CalErr 0.0797
  - 1X2 Local: Brier 0.1955 · LogLoss 0.5781 · CalErr 0.1371
  - 1X2 Visitante: Brier 0.1536 · LogLoss 0.4745 · CalErr 0.1354
- **Métricas después (calibrado Platt, test OOS n=46):**
  - Over 2.5: Brier 0.2372 · LogLoss 0.6666 · CalErr 0.0473
  - 1X2 Local: Brier 0.1905 · LogLoss 0.5633 · CalErr 0.0926
  - 1X2 Visitante: Brier 0.1456 · LogLoss 0.4636 · CalErr 0.1697 (CalErr sube por ruido en tranches extremos; Brier/LogLoss mejoran)
  - Empate (X) y BTTS: NO se calibran (calibrarlos no mejora OOS; ver `not_enabled_rationale`).
- **Dataset:** `scratch/calibration_dataset.json` — 153 partidos con resultado (artefactos legacy 2026-08-27 a 2026-09-07 consolidados). Split temporal 70/30; CV repetida 10×5 para selección de método.
- **Aprobado por:** Usuario (2026-09-07).

---

## v1.3 — 2026-09-17 (ACTIVA)

- **Cambios:** Calibración Platt añadida al mercado Over/Under 3.5 (`calibration.enabled_markets` incluye ahora `over_3_5` con `params.over_3_5 = {a: 1.5542696742, b: 1.0510711272}`; `under_3_5` se deriva como complemento). Hook aditivo en `calc_engine.py` y `PlattCalibration.transform` para propagar `over_3_5`/`under_3_5` al output calibrado (identidad si no está habilitado → v1.2 sin cambios de comportamiento).
- **Motivo:** El diagnóstico (`football-model-evaluation`, 2026-09-17) detectó miscalibración severa en la línea 3.5: `under_3_5` sobreestimado (vivos CE −0.43, 1G/4P). Raíz en el corpus: el crudo del ensemble subestimaba over_3_5 (mean 0.284 vs rate 0.435 en test OOS) y por tanto inflaba under_3_5 (0.716 vs 0.565). Prioridad del proyecto: calibración > ROI.
- **Métricas antes (crudo, test OOS n=46, línea 3.5):** Brier 0.2311 · LogLoss 0.6423 · CalErr 0.1929
- **Métricas después (Platt, test OOS n=46):** Brier 0.2107 (−0.020) · LogLoss 0.6053 (−0.037) · CalErr 0.1242 (−0.069)
- **Folds temporales:** Brier 4/4, LogLoss 3/4, CalErr 3/4. Fold 3 degrada CE (+0.039) en ventana ya calibrada y rango de p baja no seleccionada.
- **Aprobado por:** Usuario (2026-09-17).
