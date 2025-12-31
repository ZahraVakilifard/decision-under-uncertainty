from core.models import OptionEvaluation, Criterion
from core.normalization import normalize
from typing import List, Dict

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
