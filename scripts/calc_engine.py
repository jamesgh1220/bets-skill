import json
import argparse
import sys
import os

# Agregar directorio actual a sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.poisson import generate_poisson_matrix, calculate_extended_markets
from models.dixon_coles import apply_dixon_coles
from models.ratings import elo_win_probability
from models.regression import regression_expected_goals
from models.count_markets import expected_total, probability_over
from models.calibration import PlattCalibration


def _count_market_probabilities(match_data: dict, model_config: dict) -> dict:
    """Calculate corners/cards only with complete verified team-rate inputs."""
    probabilities = {}
    for market, prefix in (("corners", "corners"), ("cards", "cards")):
        fields = [
            f"{prefix}_home_for", f"{prefix}_home_against",
            f"{prefix}_away_for", f"{prefix}_away_against",
        ]
        if not all(isinstance(match_data.get(field), (int, float)) for field in fields):
            continue
        mean = expected_total(*(float(match_data[field]) for field in fields))
        params = model_config.get("count_markets", {}).get(market, {})
        dispersion = float(params.get("dispersion", 8.0))
        for line in params.get("lines", []):
            line_key = str(line).replace(".", "_")
            over = probability_over(float(line), mean, dispersion)
            probabilities[f"over_{prefix}_{line_key}"] = over
            probabilities[f"under_{prefix}_{line_key}"] = 1.0 - over
    return probabilities


def _market_config_key(market_key: str) -> str:
    if market_key in {"1", "X", "2"}:
        return "1x2"
    if market_key.startswith(("over_", "under_")) and "corners" not in market_key and "cards" not in market_key:
        return "over_under"
    if market_key.startswith("btts"):
        return "btts"
    if market_key in {"1x", "x2", "12"}:
        return "double_chance"
    if market_key.startswith("dnb_"):
        return "dnb"
    if "corners" in market_key:
        return "corners"
    if "cards" in market_key:
        return "cards"
    return "1x2"


def _evaluate_market(market_key: str, odds: float, probabilities: dict, model_config: dict) -> dict:
    prob = probabilities[market_key]
    push_prob = probabilities.get("X", 0.0) if market_key.startswith("dnb_") else 0.0
    fair_odds = ((1.0 - push_prob) / prob) if prob > 0 else 999.0
    ev = (prob * odds) + push_prob - 1.0
    uncertainty = float(model_config.get("uncertainty", {}).get("base_uncertainty", 0.05))
    conservative_prob = max(0.0, prob - uncertainty)
    robust_ev = (conservative_prob * odds) + push_prob - 1.0
    b = odds - 1.0
    kelly = ev / b if b > 0 else 0.0
    config = model_config.get("markets", {}).get(_market_config_key(market_key), {})
    min_edge = float(config.get("min_edge", 0.03))
    return {
        "market": market_key,
        "odds": odds,
        "model_prob": round(prob, 4),
        "push_prob": round(push_prob, 4),
        "conservative_prob": round(conservative_prob, 4),
        "implied_prob": round(1.0 / odds, 4),
        "fair_odds": round(fair_odds, 2),
        "edge": round(ev * 100, 2),
        "ev_percent": round(ev * 100, 2),
        "robust_ev_percent": round(robust_ev * 100, 2),
        "stake_recommended_units": max(0.0, round(kelly * 0.25, 2)),
        "has_value": ev >= min_edge,
    }

def load_model_config(config_path: str):
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_ensemble(match_data: dict, model_config: dict):
    # Cargar parámetros del modelo active
    weights = {
        "poisson": model_config["components"]["poisson"]["weight"],
        "dixon_coles": model_config["components"]["dixon_coles"]["weight"],
        "ratings": model_config["components"]["ratings"]["weight"],
        "regression": model_config["components"]["regression"]["weight"]
    }
    
    # 1. Regresión xG para lambdas
    lambda_h, lambda_a = regression_expected_goals(
        match_data.get("xg_home_for", 1.4),
        match_data.get("xg_home_against", 1.1),
        match_data.get("xg_away_for", 1.2),
        match_data.get("xg_away_against", 1.3)
    )
    
    # 2. Poisson puro
    p_matrix = generate_poisson_matrix(lambda_h, lambda_a)
    poisson_res = calculate_extended_markets(p_matrix)
    
    # 3. Dixon-Coles
    dc_matrix = apply_dixon_coles(p_matrix, lambda_h, lambda_a, rho=model_config["components"]["dixon_coles"]["parameters"]["rho"])
    dc_res = calculate_extended_markets(dc_matrix)
    
    # 4. Elo Ratings
    elo_res = elo_win_probability(
        match_data.get("elo_home", 1500),
        match_data.get("elo_away", 1500),
        home_adv=model_config["components"]["ratings"]["parameters"]["home_advantage_elo"]
    )
    
    # Ensamble de probabilidades 1X2
    p_1 = (weights["poisson"] * poisson_res["1"] +
           weights["dixon_coles"] * dc_res["1"] +
           weights["ratings"] * elo_res["1"] +
           weights["regression"] * dc_res["1"])
           
    p_X = (weights["poisson"] * poisson_res["X"] +
           weights["dixon_coles"] * dc_res["X"] +
           weights["ratings"] * elo_res["X"] +
           weights["regression"] * dc_res["X"])
           
    p_2 = (weights["poisson"] * poisson_res["2"] +
           weights["dixon_coles"] * dc_res["2"] +
           weights["ratings"] * elo_res["2"] +
           weights["regression"] * dc_res["2"])
           
    total_1x2 = p_1 + p_X + p_2
    p_1, p_X, p_2 = p_1 / total_1x2, p_X / total_1x2, p_2 / total_1x2
    
    # Ensamble de líneas de goles y mercados protegidos que derivan de 1X2.
    goals_weight = weights["poisson"] + weights["dixon_coles"]
    goals_probs = {}
    for line in ("1_5", "2_5", "3_5"):
        under = (weights["poisson"] * poisson_res[f"under_{line}"] + weights["dixon_coles"] * dc_res[f"under_{line}"]) / goals_weight
        goals_probs[f"under_{line}"] = under
        goals_probs[f"over_{line}"] = 1.0 - under
    
    # Ensamble BTTS
    p_btts_no = (weights["poisson"] * poisson_res["btts_no"] + weights["dixon_coles"] * dc_res["btts_no"]) / (weights["poisson"] + weights["dixon_coles"])
    p_btts_yes = 1.0 - p_btts_no
    
    ensemble_probs = {
        "1": round(p_1, 4),
        "X": round(p_X, 4),
        "2": round(p_2, 4),
        **{key: round(value, 4) for key, value in goals_probs.items()},
        "btts_yes": round(p_btts_yes, 4),
        "btts_no": round(p_btts_no, 4),
        "1x": round(p_1 + p_X, 4),
        "x2": round(p_X + p_2, 4),
        "12": round(p_1 + p_2, 4),
        "dnb_home": round(p_1, 4),
        "dnb_away": round(p_2, 4),
        "expected_goals_home": round(lambda_h, 2),
        "expected_goals_away": round(lambda_a, 2)
    }
    
    ensemble_probs.update(_count_market_probabilities(match_data, model_config))

    # Calibración de probabilidades (Platt) según configuración del modelo.
    calibration_config = model_config.get("calibration", {})
    enabled_markets = set(calibration_config.get("enabled_markets", []))
    if calibration_config.get("enabled", False) and enabled_markets:
        calib = PlattCalibration(calibration_config.get("params", {}))
        calibrated = calib.transform(ensemble_probs, enabled_markets=enabled_markets)
        for key in ("1", "X", "2", "1x", "x2", "12", "dnb_home", "dnb_away",
                    "over_2_5", "under_2_5", "over_3_5", "under_3_5",
                    "btts_yes", "btts_no"):
            if key in calibrated:
                ensemble_probs[key] = round(calibrated[key], 4)

    # Evaluación determinista de valor y escenario conservador.
    odds = match_data.get("odds", {})
    evaluations = {}
    
    for market_key, odds_val in odds.items():
        if market_key in ensemble_probs and odds_val > 1.0:
            evaluations[market_key] = _evaluate_market(market_key, odds_val, ensemble_probs, model_config)
            
    return {
        "match": f"{match_data.get('home_team')} vs {match_data.get('away_team')}",
        "probabilities": ensemble_probs,
        "evaluations": evaluations
    }

def main():
    parser = argparse.ArgumentParser(description="Motor Cuantitativo de Predicción de Fútbol")
    parser.add_argument("--input", required=True, help="Ruta al archivo JSON de datos del partido")
    parser.add_argument("--config", default="models/model-v1.2.json", help="Ruta al archivo JSON de configuración del modelo")
    parser.add_argument("--output", help="Ruta de salida JSON (opcional)")
    
    args = parser.parse_args()
    
    with open(args.input, 'r', encoding='utf-8') as f:
        match_data = json.load(f)
        
    model_config = load_model_config(args.config)
    
    results = run_ensemble(match_data, model_config)
    
    output_json = json.dumps(results, indent=2, ensure_ascii=False)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_json)
        print(f"Resultados guardados en {args.output}")
    else:
        print(output_json)

if __name__ == "__main__":
    main()
