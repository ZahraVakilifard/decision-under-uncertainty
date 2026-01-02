from typing import List, Dict
from core.models import OptionEvaluation, Criterion
from core.strategies import Strategy

def sensitivity_analysis(
    options: List[OptionEvaluation],
    criteria: List[Criterion],
    strategy: Strategy,
    risk_weights: List[float] = [0.0, 0.25, 0.5, 0.75, 1.0]
) -> Dict[float, Dict[str, float]]:
    """
    Perform sensitivity analysis over different risk weights.
    Returns a dict mapping risk_weight -> option scores
    """
    results = {}
    for rw in risk_weights:
        scores = strategy.evaluate(options, criteria, risk_weight=rw)
        results[rw] = scores
    return results