from core.models import OptionEvaluation, Criterion

def expected_value(outcome) -> float:
    """Compute expected value from Outcome"""
    return outcome.expected

def risk_adjusted_score(outcome, risk_weight: float = 0.5) -> float:
    """
    Adjust score based on uncertainty
    risk_weight = 0 -> ignore uncertainty
    risk_weight = 1 -> penalize full worst deviation
    """
    # simple risk = best - worst
    uncertainty = outcome.best - outcome.worst
    return outcome.expected - (risk_weight * uncertainty)
