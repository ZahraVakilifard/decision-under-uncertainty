from abc import ABC, abstractmethod
from typing import List, Dict
from core.models import OptionEvaluation, Criterion
from core.scoring import calculate_scores_with_risk
from core.normalization import normalize

# -------------------------
# Strategy Interface
# -------------------------
class Strategy(ABC):
    @abstractmethod
    def evaluate(
        self,
        options: List[OptionEvaluation],
        criteria: List[Criterion],
        risk_weight: float = 0.5
    ) -> Dict[str, float]:
        pass

# -------------------------
# Expected Value Strategy
# -------------------------
class ExpectedValueStrategy(Strategy):
    def evaluate(self, options: List[OptionEvaluation], criteria: List[Criterion], risk_weight: float = 0.5) -> Dict[str, float]:
        return calculate_scores_with_risk(options, criteria, risk_weight)

# -------------------------
# Risk-Averse Strategy (Revised)
# -------------------------
class RiskAverseStrategy(Strategy):
    def evaluate(self, options: List[OptionEvaluation], criteria: List[Criterion], risk_weight: float = 0.5) -> Dict[str, float]:
        scores = {opt.option.name: 0.0 for opt in options}

        for criterion in criteria:
            adjusted_values = []
            for opt in options:
                outcome = opt.outcomes[criterion.name]
                spread = outcome.best - outcome.worst
                if criterion.maximize:
                    adj = outcome.expected - risk_weight * spread
                else:
                    adj = outcome.expected + risk_weight * spread
                adjusted_values.append(adj)

            normalized_values = normalize(adjusted_values, maximize=criterion.maximize)
            for opt, norm_val in zip(options, normalized_values):
                scores[opt.option.name] += norm_val * criterion.weight

        return scores

# -------------------------
# Regret Minimization Strategy (Revised)
# -------------------------
class RegretMinimizationStrategy(Strategy):
    def evaluate(self, options: List[OptionEvaluation], criteria: List[Criterion], risk_weight: float = 0.5) -> Dict[str, float]:
        scores = {opt.option.name: 0.0 for opt in options}

        for criterion in criteria:
            if criterion.maximize:
                best_val = max([opt.outcomes[criterion.name].best for opt in options])
                regrets = [max(0.0, best_val - opt.outcomes[criterion.name].worst) for opt in options]
            else:
                best_val = min([opt.outcomes[criterion.name].worst for opt in options])
                regrets = [max(0.0, opt.outcomes[criterion.name].worst - best_val) for opt in options]

            normalized_values = normalize(regrets, maximize=False)
            for opt, norm_val in zip(options, normalized_values):
                scores[opt.option.name] += norm_val * criterion.weight

        return scores
