import math

def poisson_pmf(k: int, mu: float) -> float:
    """Calcula la probabilidad de K eventos dado el promedio mu."""
    if mu <= 0:
        return 1.0 if k == 0 else 0.0
    return (math.pow(mu, k) * math.exp(-mu)) / math.factorial(k)

def generate_poisson_matrix(lambda_home: float, lambda_away: float, max_goals: int = 8):
    """Genera matriz de probabilidades para marcadores de 0x0 a max_goals x max_goals."""
    matrix = {}
    for i in range(max_goals + 1):
        p_h = poisson_pmf(i, lambda_home)
        for j in range(max_goals + 1):
            p_a = poisson_pmf(j, lambda_away)
            matrix[(i, j)] = p_h * p_a
    return matrix

def calculate_1x2_over_btts(matrix):
    """Extrae probabilidades de 1X2, Over/Under 2.5 y BTTS de la matriz de marcadores."""
    p_home = 0.0
    p_draw = 0.0
    p_away = 0.0
    p_over_2_5 = 0.0
    p_btts_yes = 0.0

    for (h, a), p in matrix.items():
        if h > a:
            p_home += p
        elif h == a:
            p_draw += p
        else:
            p_away += p
        
        if h + a > 2.5:
            p_over_2_5 += p
            
        if h > 0 and a > 0:
            p_btts_yes += p

    return {
        "1": p_home,
        "X": p_draw,
        "2": p_away,
        "over_2_5": p_over_2_5,
        "under_2_5": 1.0 - p_over_2_5,
        "btts_yes": p_btts_yes,
        "btts_no": 1.0 - p_btts_yes
    }


def probability_total_over(matrix, line: float) -> float:
    """Return the probability that the total goals is strictly above a line."""
    return sum(probability for (home, away), probability in matrix.items() if home + away > line)


def calculate_extended_markets(matrix):
    """Derive standard goals and protected-result markets from a score matrix."""
    base = calculate_1x2_over_btts(matrix)
    result = dict(base)
    for line in (1.5, 2.5, 3.5):
        key = str(line).replace(".", "_")
        over = probability_total_over(matrix, line)
        result[f"over_{key}"] = over
        result[f"under_{key}"] = 1.0 - over
    result.update({
        "1x": base["1"] + base["X"],
        "x2": base["X"] + base["2"],
        "12": base["1"] + base["2"],
        # DNB markets contain a push on the draw; the engine treats that separately.
        "dnb_home": base["1"],
        "dnb_away": base["2"],
    })
    return result
