"""Count-market probabilities for corners and cards.

These markets are deliberately isolated from the goals ensemble.  They are only
available when the four team-rate inputs are present, preventing fabricated
corners/cards estimates from entering a portfolio.
"""

import math


def expected_total(home_for: float, home_against: float, away_for: float, away_against: float) -> float:
    """Blend each team's for-rate with its opponent's against-rate."""
    return ((home_for + away_against) + (away_for + home_against)) / 2.0


def negative_binomial_pmf(k: int, mean: float, dispersion: float) -> float:
    """NB2 PMF, where variance is mean + mean² / dispersion."""
    if mean <= 0:
        return 1.0 if k == 0 else 0.0
    r = max(dispersion, 0.01)
    log_p = (
        math.lgamma(k + r) - math.lgamma(r) - math.lgamma(k + 1)
        + r * math.log(r / (r + mean))
        + k * math.log(mean / (r + mean))
    )
    return math.exp(log_p)


def probability_over(line: float, mean: float, dispersion: float, max_count: int = 80) -> float:
    """Probability of a count being over a half-point market line."""
    threshold = math.floor(line) + 1
    return min(1.0, max(0.0, sum(negative_binomial_pmf(k, mean, dispersion) for k in range(threshold, max_count + 1))))
