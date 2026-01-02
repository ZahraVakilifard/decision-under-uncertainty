from core.strategies import Strategy
from core.models import OptionEvaluation, Criterion
from core.normalization import normalize

def risk_aware_agent(
    options: list[OptionEvaluation],
    criteria: list[Criterion],
    strategy: Strategy,
    risk_weight: float = 0.5
) -> dict:
    """
    Compute scores + breakdown + explanation.
    """
    # 1 validation
    from core.validation import validate_options
    validate_options(options, criteria)

    # 2 scoring
    scores = strategy.evaluate(options, criteria, risk_weight=risk_weight)

    # 3 ranking
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # 4 breakdown per option for human explanation
    breakdown = {}
    for opt_eval in options:
        option_name = opt_eval.option.name
        bd = {}
        for crit in criteria:
            out = opt_eval.outcomes[crit.name]
            # risk-aware adjustment
            spread = out.best - out.worst
            if crit.maximize:
                raw_score = out.expected - risk_weight * spread
            else:
                raw_score = out.expected + risk_weight * spread
            bd[crit.name] = raw_score
        breakdown[option_name] = bd

    return {
        "scores": scores,
        "ranking": ranked,
        "breakdown": breakdown
    }
