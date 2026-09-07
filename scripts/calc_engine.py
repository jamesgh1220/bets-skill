import json
import argparse
import sys
import os

# Agregar directorio actual a sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.poisson import generate_poisson_matrix, calculate_1x2_over_btts
from models.dixon_coles import apply_dixon_coles
from models.ratings import elo_win_probability
from models.regression import regression_expected_goals

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
    poisson_res = calculate_1x2_over_btts(p_matrix)
    
    # 3. Dixon-Coles
    dc_matrix = apply_dixon_coles(p_matrix, lambda_h, lambda_a, rho=model_config["components"]["dixon_coles"]["parameters"]["rho"])
    dc_res = calculate_1x2_over_btts(dc_matrix)
    
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
    
    # Ensamble Over/Under 2.5
    p_under = (weights["poisson"] * poisson_res["under_2_5"] + weights["dixon_coles"] * dc_res["under_2_5"]) / (weights["poisson"] + weights["dixon_coles"])
    p_over = 1.0 - p_under
    
    # Ensamble BTTS
    p_btts_no = (weights["poisson"] * poisson_res["btts_no"] + weights["dixon_coles"] * dc_res["btts_no"]) / (weights["poisson"] + weights["dixon_coles"])
    p_btts_yes = 1.0 - p_btts_no
    
    ensemble_probs = {
        "1": round(p_1, 4),
        "X": round(p_X, 4),
        "2": round(p_2, 4),
        "over_2_5": round(p_over, 4),
        "under_2_5": round(p_under, 4),
        "btts_yes": round(p_btts_yes, 4),
        "btts_no": round(p_btts_no, 4),
        "expected_goals_home": round(lambda_h, 2),
        "expected_goals_away": round(lambda_a, 2)
    }
    
    # Evaluación de Valor (EV, Edge, Cuota Justa) frente a cuotas de entrada
    odds = match_data.get("odds", {})
    evaluations = {}
    
    for market_key, odds_val in odds.items():
        if market_key in ensemble_probs and odds_val > 1.0:
            prob = ensemble_probs[market_key]
            fair_odds = round(1.0 / prob, 2) if prob > 0 else 999.0
            implied_prob = round(1.0 / odds_val, 4)
            edge = round((prob * odds_val) - 1.0, 4)
            ev = round(edge * 100, 2)
            
            # Kelly Criterium Fraccional (0.25 Kelly)
            b = odds_val - 1.0
            q = 1.0 - prob
            kelly = (b * prob - q) / b if b > 0 else 0.0
            fractional_kelly = max(0.0, round(kelly * 0.25, 2))
            
            evaluations[market_key] = {
                "market": market_key,
                "odds": odds_val,
                "model_prob": prob,
                "implied_prob": implied_prob,
                "fair_odds": fair_odds,
                "edge": round(edge * 100, 2),
                "ev_percent": ev,
                "stake_recommended_units": fractional_kelly,
                "has_value": edge >= model_config["markets"].get("1x2", {}).get("min_edge", 0.03)
            }
            
    return {
        "match": f"{match_data.get('home_team')} vs {match_data.get('away_team')}",
        "probabilities": ensemble_probs,
        "evaluations": evaluations
    }

def main():
    parser = argparse.ArgumentParser(description="Motor Cuantitativo de Predicción de Fútbol")
    parser.add_argument("--input", required=True, help="Ruta al archivo JSON de datos del partido")
    parser.add_argument("--config", default="models/model-v1.0.json", help="Ruta al archivo JSON de configuración del modelo")
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
