from abc import ABC, abstractmethod
from typing import List, Dict
from core.models import OptionEvaluation, Criterion
from core.scoring import calculate_scores_with_risk
from core.normalization import normalize

# -------------------------
# Base Strategy (Abstract)
# -------------------------
class Strategy(ABC):
    @abstractmethod
    def evaluate(
        self,
        options: List[OptionEvaluation],
        criteria: List[Criterion],
        risk_weight: float = 0.5
    ) -> Dict[str, float]:
        """
        Evaluate options and return a dictionary mapping Option name -> score
        """
        pass

# -------------------------
# Expected Value Strategy
# -------------------------
class ExpectedValueStrategy(Strategy):
    def evaluate(
        self, options: List[OptionEvaluation], criteria: List[Criterion], risk_weight: float = 0.5
    ) -> Dict[str, float]:
        return calculate_scores_with_risk(options, criteria, risk_weight)

# -------------------------
# Risk-Averse Strategy
# -------------------------
class RiskAverseStrategy(Strategy):
    def evaluate(
        self, options: List[OptionEvaluation], criteria: List[Criterion], risk_weight: float = 0.5
    ) -> Dict[str, float]:
        scores = {opt.option.name: 0.0 for opt in options}
        for criterion in criteria:
            adjusted_values = [
                opt.outcomes[criterion.name].expected - risk_weight * (opt.outcomes[criterion.name].best - opt.outcomes[criterion.name].worst)
                for opt in options
            ]
            normalized_values = normalize(adjusted_values, maximize=criterion.maximize)
            for opt, norm_val in zip(options, normalized_values):
                scores[opt.option.name] += norm_val * criterion.weight
        return scores

# -------------------------
# Regret Minimization Strategy
# -------------------------
class RegretMinimizationStrategy(Strategy):
    def evaluate(
        self, options: List[OptionEvaluation], criteria: List[Criterion], risk_weight: float = 0.5
    ) -> Dict[str, float]:
        scores = {opt.option.name: 0.0 for opt in options}
        for criterion in criteria:
            best_worst = max([opt.outcomes[criterion.name].worst for opt in options])
            regrets = [max(0.0, best_worst - opt.outcomes[criterion.name].worst) for opt in options]
            normalized = normalize(regrets, maximize=False)
            for opt, norm_val in zip(options, normalized):
                scores[opt.option.name] += norm_val * criterion.weight
        return scores

# -------------------------
# Strategy Factory (Modular & Dynamic)
# -------------------------
class StrategyFactory:
    """
    Returns strategy instance based on a name string.
    """
    _mapping = {
        "expected_value": ExpectedValueStrategy,
        "risk_averse": RiskAverseStrategy,
        "regret_minimization": RegretMinimizationStrategy
    }

    @staticmethod
    def get_strategy(name: str) -> Strategy:
        if name not in StrategyFactory._mapping:
            raise ValueError(f"Strategy '{name}' not found.")
        return StrategyFactory._mapping[name]()
