import pytest
from core.models import Option, Outcome, OptionEvaluation, Criterion
from core.strategies import ExpectedValueStrategy, RiskAverseStrategy, RegretMinimizationStrategy

# -------------------------
# Sample Options & Criteria
# -------------------------
options = [
    OptionEvaluation(
        option=Option("A"),
        outcomes={"salary": Outcome(120, 100, 80),
                  "growth": Outcome(10, 7, 5),
                  "risk": Outcome(5, 7, 10)}
    ),
    OptionEvaluation(
        option=Option("B"),
        outcomes={"salary": Outcome(110, 95, 80),
                  "growth": Outcome(12, 8, 4),
                  "risk": Outcome(3, 5, 8)}
    ),
]

criteria = [
    Criterion("salary", 0.5, True),
    Criterion("growth", 0.3, True),
    Criterion("risk", 0.2, False)
]

# -------------------------
# Test Expected Value Strategy
# -------------------------
def test_expected_value_strategy():
    strat = ExpectedValueStrategy()
    scores = strat.evaluate(options, criteria, risk_weight=0.5)
    assert "A" in scores and "B" in scores
    assert scores["B"] > scores["A"]

# -------------------------
# Test Risk-Averse Strategy
# -------------------------
def test_risk_averse_strategy():
    strat = RiskAverseStrategy()
    scores = strat.evaluate(options, criteria, risk_weight=0.5)
    assert "A" in scores and "B" in scores
    assert scores["B"] > 0 and scores["A"] > 0

# -------------------------
# Test Regret Minimization Strategy
# -------------------------
def test_regret_minimization_strategy():
    strat = RegretMinimizationStrategy()
    scores = strat.evaluate(options, criteria, risk_weight=0.5)
    assert "A" in scores and "B" in scores
    total_score_sum = scores["A"] + scores["B"]
    assert total_score_sum > 0
