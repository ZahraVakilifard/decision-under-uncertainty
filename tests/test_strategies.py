import pytest
from core.models import Option, Outcome, OptionEvaluation, Criterion
from core.strategies import StrategyFactory

# -------------------------
# Sample Options & Criteria
# -------------------------
options = [
    OptionEvaluation(
        option=Option("A"),
        outcomes={
            "salary": Outcome(120, 100, 80),
            "growth": Outcome(10, 7, 5),
            "risk": Outcome(5, 7, 10)
        }
    ),
    OptionEvaluation(
        option=Option("B"),
        outcomes={
            "salary": Outcome(110, 95, 80),
            "growth": Outcome(12, 8, 4),
            "risk": Outcome(3, 5, 8)
        }
    ),
]

criteria = [
    Criterion("salary", 0.5, True),
    Criterion("growth", 0.3, True),
    Criterion("risk", 0.2, False)
]

# -------------------------
# Test Strategies using Factory
# -------------------------

def test_expected_value_strategy():
    strat = StrategyFactory.get_strategy("expected_value")
    scores = strat.evaluate(options, criteria, risk_weight=0.5)
    assert "A" in scores and "B" in scores
    # floating-point safe comparison
    assert scores["A"] > scores["B"]

def test_risk_averse_strategy():
    strat = StrategyFactory.get_strategy("risk_averse")
    scores = strat.evaluate(options, criteria, risk_weight=0.5)
    assert "A" in scores and "B" in scores
    assert scores["B"] >= 0 and scores["A"] >= 0

def test_regret_minimization_strategy():
    strat = StrategyFactory.get_strategy("regret_minimization")
    scores = strat.evaluate(options, criteria, risk_weight=0.5)
    assert "A" in scores and "B" in scores
    total_score_sum = scores["A"] + scores["B"]
    assert total_score_sum > 0

# -------------------------
# Test all strategies in a loop (optional)
# -------------------------
@pytest.mark.parametrize("strategy_name", ["expected_value", "risk_averse", "regret_minimization"])
def test_all_strategies(strategy_name):
    strat = StrategyFactory.get_strategy(strategy_name)
    scores = strat.evaluate(options, criteria, risk_weight=0.5)
    assert all(opt.option.name in scores for opt in options)
    # ensure scores are numbers
    assert all(isinstance(score, (int, float)) for score in scores.values())
