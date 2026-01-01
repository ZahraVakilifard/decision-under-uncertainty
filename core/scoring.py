from core.models import OptionEvaluation, Criterion
from core.normalization import normalize
from typing import List, Dict
from core.uncertainty import risk_adjusted_score

def calculate_scores(
    options: List[OptionEvaluation], criteria: List[Criterion]
) -> Dict[str, float]:
    """
    Calculate weighted scores for each option
    """
    scores = {opt.option.name: 0.0 for opt in options}

    for criterion in criteria:
        values = [opt.outcomes[criterion.name].expected for opt in options]
        normalized_values = normalize(values, maximize=criterion.maximize)

        for opt, norm_val in zip(options, normalized_values):
            scores[opt.option.name] += norm_val * criterion.weight

    return scores


def calculate_scores_with_risk(
    options: list[OptionEvaluation],
    criteria: list[Criterion],
    risk_weight: float = 0.5
) -> dict[str, float]:
    scores = {opt.option.name: 0.0 for opt in options}


    for criterion in criteria:
        values = [risk_adjusted_score(opt.outcomes[criterion.name], risk_weight) for opt in options]
        normalized_values = normalize(values, maximize=criterion.maximize)

        for opt, norm_val in zip(options, normalized_values):
            scores[opt.option.name] += norm_val * criterion.weight

    return scores