def tau(x: int, y: int, lambda_h: float, mu_a: float, rho: float) -> float:
    """Factor de corrección de Dixon-Coles para marcadores bajos."""
    if x == 0 and y == 0:
        return 1.0 - (lambda_h * mu_a * rho)
    elif x == 1 and y == 0:
        return 1.0 + (mu_a * rho)
    elif x == 0 and y == 1:
        return 1.0 + (lambda_h * rho)
    elif x == 1 and y == 1:
        return 1.0 - rho
    else:
        return 1.0

def apply_dixon_coles(matrix, lambda_home: float, lambda_away: float, rho: float = -0.13):
    """Aplica la corrección Dixon-Coles sobre la matriz de probabilidades de Poisson."""
    dc_matrix = {}
    total_p = 0.0
    for (h, a), p in matrix.items():
        t = tau(h, a, lambda_home, lambda_away, rho)
        p_adj = p * t
        dc_matrix[(h, a)] = p_adj
        total_p += p_adj

    # Normalizar matriz
    if total_p > 0:
        for k in dc_matrix:
            dc_matrix[k] /= total_p

    return dc_matrix
