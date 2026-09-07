import unittest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.poisson import generate_poisson_matrix, calculate_1x2_over_btts
from models.dixon_coles import apply_dixon_coles
from calc_engine import run_ensemble, load_model_config
from selection import select_portfolio

class TestCalcEngine(unittest.TestCase):

    def setUp(self):
        self.config = load_model_config("models/model-v1.2.json")
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

    def test_extended_markets_and_conservative_ev(self):
        self.sample_match["odds"].update({
            "over_1_5": 1.60,
            "under_3_5": 1.70,
            "1x": 1.40,
            "dnb_home": 1.55,
        })
        res = run_ensemble(self.sample_match, self.config)
        self.assertIn("over_1_5", res["probabilities"])
        self.assertIn("under_3_5", res["evaluations"])
        self.assertLess(res["evaluations"]["over_1_5"]["robust_ev_percent"], res["evaluations"]["over_1_5"]["ev_percent"])
        self.assertGreater(res["evaluations"]["dnb_home"]["push_prob"], 0)

    def test_count_markets_require_complete_rates(self):
        self.sample_match["odds"]["over_corners_9_5"] = 1.90
        without_rates = run_ensemble(self.sample_match, load_model_config("models/model-v1.2.json"))
        self.assertNotIn("over_corners_9_5", without_rates["evaluations"])
        self.sample_match.update({
            "corners_home_for": 5.5, "corners_home_against": 4.2,
            "corners_away_for": 4.8, "corners_away_against": 5.1,
        })
        with_rates = run_ensemble(self.sample_match, load_model_config("models/model-v1.2.json"))
        self.assertIn("over_corners_9_5", with_rates["evaluations"])

    def test_calibration_shifts_probabilities(self):
        v11 = load_model_config("models/model-v1.1.json")
        v12 = load_model_config("models/model-v1.2.json")
        raw = run_ensemble(self.sample_match, v11)["probabilities"]
        cal = run_ensemble(self.sample_match, v12)["probabilities"]
        self.assertNotAlmostEqual(cal["over_2_5"], raw["over_2_5"], places=2)
        self.assertGreater(cal["over_2_5"], raw["over_2_5"])
        self.assertAlmostEqual(cal["1"] + cal["X"] + cal["2"], 1.0, places=4)
        self.assertAlmostEqual(cal["over_2_5"] + cal["under_2_5"], 1.0, places=4)
        self.assertEqual(cal["btts_yes"], raw["btts_yes"])  # BTTS no se calibra (identity)

    def test_portfolio_allows_one_exceptional_longshot(self):
        candidates = [
            {"odds": 1.80, "model_prob": 0.60, "robust_ev_percent": 6.0, "ev_percent": 8.0, "stake_recommended_units": 0.30},
            {"odds": 4.00, "model_prob": 0.35, "robust_ev_percent": 12.0, "ev_percent": 18.0, "stake_recommended_units": 0.40},
            {"odds": 3.50, "model_prob": 0.31, "robust_ev_percent": 11.0, "ev_percent": 15.0, "stake_recommended_units": 0.35},
        ]
        selected, excluded = select_portfolio(candidates)
        self.assertEqual(len(selected), 2)
        self.assertEqual(sum(item["selection_profile"] == "excepcional" for item in selected), 1)
        self.assertEqual(selected[-1]["stake_recommended_units"], 0.25)
        self.assertEqual(len(excluded), 1)

if __name__ == "__main__":
    unittest.main()
