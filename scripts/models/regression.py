def regression_expected_goals(xg_home_for: float, xg_home_against: float, 
                              xg_away_for: float, xg_away_against: float,
                              league_avg_goals: float = 1.35, home_adv: float = 0.25) -> tuple:
    """Estimación de expectativas de gol (lambda) usando regresión de xG con ventaja de localía."""
    exp_goals_home = (xg_home_for + xg_away_against) / 2.0 + (home_adv / 2.0)
    exp_goals_away = (xg_away_for + xg_home_against) / 2.0 - (home_adv / 2.0)
    
    return max(0.2, exp_goals_home), max(0.2, exp_goals_away)
