import math

def elo_win_probability(rating_home: float, rating_away: float, home_adv: float = 100.0) -> dict:
    """Calcula la probabilidad esperada de victoria/empate basado en calificaciones Elo."""
    dr = (rating_home + home_adv) - rating_away
    e_home = 1.0 / (1.0 + math.pow(10, -dr / 400.0))
    e_away = 1.0 - e_home
    
    # Asignar un margen para empate según el diferencial
    p_draw = 0.26 * math.exp(-abs(dr) / 600.0)
    p_home = e_home * (1.0 - p_draw)
    p_away = e_away * (1.0 - p_draw)
    
    # Normalizar
    total = p_home + p_draw + p_away
    return {
        "1": p_home / total,
        "X": p_draw / total,
        "2": p_away / total
    }
