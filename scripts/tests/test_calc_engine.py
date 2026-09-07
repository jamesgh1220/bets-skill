import unittest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.poisson import generate_poisson_matrix, calculate_1x2_over_btts
from models.dixon_coles import apply_dixon_coles
from calc_engine import run_ensemble, load_model_config

class TestCalcEngine(unittest.TestCase):

    def setUp(self):
        self.config = load_model_config("models/model-v1.0.json")
        self.sample_match = {
            "home_team": "Equipo A",
            "away_team": "Equipo B",
            "xg_home_for": 1.6,
            "xg_home_against": 0.9,
            "xg_away_for": 1.1,
            "xg_away_against": 1.4,
            "elo_home": 1600,
            "elo_away": 1500,
            "odds": {
                "1": 1.95,
                "X": 3.40,
                "2": 4.10,
                "under_2_5": 2.05
            }
        }

    def test_poisson_sum(self):
        matrix = generate_poisson_matrix(1.5, 1.0)
        res = calculate_1x2_over_btts(matrix)
        total_1x2 = res["1"] + res["X"] + res["2"]
        self.assertAlmostEqual(total_1x2, 1.0, places=2)

    def test_ensemble_output(self):
        res = run_ensemble(self.sample_match, self.config)
        probs = res["probabilities"]
        total_prob = probs["1"] + probs["X"] + probs["2"]
        self.assertAlmostEqual(total_prob, 1.0, places=2)
        self.assertIn("1", res["evaluations"])
        self.assertIn("edge", res["evaluations"]["1"])

if __name__ == "__main__":
    unittest.main()
