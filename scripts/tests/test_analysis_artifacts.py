import sys
import tempfile
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from publish_analysis_artifact import publish
from validate_analysis_artifact import slugify_model, validate_artifact


VALID_ARTIFACT = """# Análisis de Apuestas — 7 de septiembre de 2026

## Metadatos
- **Fecha de análisis:** 2026-09-07T10:00:00-05:00
- **Fecha(s) de partido:** 7 de septiembre de 2026
- **Information cutoff:** 2026-09-07T09:30:00-05:00
- **Modelo de IA:** GPT 5
- **Versión del motor predictivo:** model-v1.0
- **Ligas analizadas:** LaLiga
- **Rango de fechas solicitado:** 2026-09-07
- **Partidos en universo:** 1
- **Picks iniciales con value:** 1
- **Picks finales seleccionados:** 1

## Universo Analizado
Equipo A vs Equipo B.

## Ranking Global
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Equipo A vs Equipo B | 1X2 | Local | prioritario | 2.00 | 55% | 1.82 | 10% | 10% | 5% | 0.25u | Media |

## Picks Recomendados (Top 1)
| Rank | Partido | Mercado | Selección | Perfil | Cuota | Prob. | Justa | Edge | EV | EV robusto | Stake | Confianza |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Equipo A vs Equipo B | 1X2 | Local | prioritario | 2.00 | 55% | 1.82 | 10% | 10% | 5% | 0.25u | Media |

## Detalle de Picks
### Pick 1: Equipo A vs Equipo B
- **Mercado:** 1X2
- **Selección:** Local
- **Cuota:** 2.00
- **Probabilidad modelo:** 55%
- **Probabilidad conservadora:** 50%
- **Probabilidad implícita:** 50%
- **Cuota justa:** 1.82
- **Edge:** 10%
- **EV:** 10%
- **EV robusto:** 5%
- **Perfil de selección:** prioritario
- **Cuota mínima:** 1.90
- **Stake:** 0.25u
- **Confianza:** Media
- **Incertidumbre:** Media
- **Por qué:** El motor detecta value.
- **Riesgos:** Variación de cuota.
- **Fuentes:** Fuente oficial.

## NO BET / Excluidos
- Ninguno.

## Portfolio y Correlaciones
- **Exposición total:** 0.25u
- **Correlaciones detectadas:** Ninguna.
- **Ajuste de stake por correlación:** No aplica.

## Tracking
| Pick | Estado | Resultado | Profit/Loss |
|---|---|---|---|
| Equipo A vs Equipo B | PENDIENTE | — | — |
"""


class TestAnalysisArtifacts(unittest.TestCase):
    def test_valid_artifact_passes_contract(self):
        errors = validate_artifact(
            VALID_ARTIFACT,
            filename="analisis-2026-09-07--gpt-5--v01.md",
            expected_date="2026-09-07",
            expected_model="GPT 5",
        )
        self.assertEqual(errors, [])

    def test_invalid_contract_is_rejected(self):
        invalid = VALID_ARTIFACT.replace("## NO BET / Excluidos\n- Ninguno.\n\n", "")
        errors = validate_artifact(invalid)
        self.assertTrue(any("NO BET" in error for error in errors))

    def test_missing_pick_detail_is_rejected(self):
        invalid = VALID_ARTIFACT.replace("- **Fuentes:** Fuente oficial.\n", "")
        errors = validate_artifact(invalid)
        self.assertTrue(any("Fuentes" in error for error in errors))

    def test_publish_allocates_incrementing_revisions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "first.md"
            second = root / "second.md"
            first.write_text(VALID_ARTIFACT, encoding="utf-8")
            second.write_text(VALID_ARTIFACT, encoding="utf-8")
            destination_one = publish(first, root / "artifacts", "2026-09-07", "GPT 5")
            destination_two = publish(second, root / "artifacts", "2026-09-07", "GPT 5")
            self.assertEqual(destination_one.name, "analisis-2026-09-07--gpt-5--v01.md")
            self.assertEqual(destination_two.name, "analisis-2026-09-07--gpt-5--v02.md")
            self.assertFalse(first.exists())
            self.assertFalse(second.exists())

    def test_model_slug_is_safe(self):
        self.assertEqual(slugify_model("GPT 5 / Ánalisis"), "gpt-5-analisis")


if __name__ == "__main__":
    unittest.main()
