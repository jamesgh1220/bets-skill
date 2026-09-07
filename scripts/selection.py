"""Portfolio eligibility rules for football betting analysis."""

from __future__ import annotations

from typing import Any


PRIORITY_MIN_ODDS = 1.50
PRIORITY_MAX_ODDS = 2.20
PRIORITY_MIN_PROB = 0.55
PRIORITY_MIN_ROBUST_EV = 5.0
LONGSHOT_MIN_ODDS = 3.00
LONGSHOT_MIN_PROB = 0.30
LONGSHOT_MIN_ROBUST_EV = 10.0
LONGSHOT_STAKE_CAP = 0.25


def classify_candidate(candidate: dict[str, Any]) -> tuple[str, str]:
    """Classify a value candidate without allowing raw EV to dominate variance."""
    odds = candidate["odds"]
    probability = candidate["model_prob"]
    robust_ev = candidate["robust_ev_percent"]
    if (PRIORITY_MIN_ODDS <= odds <= PRIORITY_MAX_ODDS
            and probability >= PRIORITY_MIN_PROB and robust_ev >= PRIORITY_MIN_ROBUST_EV):
        return "prioritario", "Cumple cuota media, probabilidad y EV robusto mínimos."
    if (odds >= LONGSHOT_MIN_ODDS and probability >= LONGSHOT_MIN_PROB
            and robust_ev >= LONGSHOT_MIN_ROBUST_EV):
        return "excepcional", "Cuota alta admitida solo como excepción robusta."
    if odds >= LONGSHOT_MIN_ODDS:
        return "excluido", "Cuota alta sin los mínimos reforzados de probabilidad y EV robusto."
    return "excluido", "No cumple los mínimos de selección probabilidad-primero."


def select_portfolio(candidates: list[dict[str, Any]], max_picks: int = 6) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Return selected candidates and excluded candidates, allowing one longshot."""
    selected: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    prioritized: list[dict[str, Any]] = []
    exceptional: list[dict[str, Any]] = []
    for candidate in candidates:
        profile, reason = classify_candidate(candidate)
        candidate["selection_profile"] = profile
        candidate["selection_reason"] = reason
        if profile == "prioritario":
            prioritized.append(candidate)
        elif profile == "excepcional":
            exceptional.append(candidate)
        else:
            excluded.append(candidate)
    key = lambda item: (item["model_prob"], item["robust_ev_percent"], item["ev_percent"])
    selected.extend(sorted(prioritized, key=key, reverse=True)[:max_picks])
    if len(selected) < max_picks and exceptional:
        pick = max(exceptional, key=key)
        pick["stake_recommended_units"] = min(pick["stake_recommended_units"], LONGSHOT_STAKE_CAP)
        selected.append(pick)
        excluded.extend(item for item in exceptional if item is not pick)
    else:
        excluded.extend(exceptional)
    return selected, excluded
