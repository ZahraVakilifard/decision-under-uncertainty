import pytest
from core.models import Option, Outcome, OptionEvaluation, Criterion
from core.scoring import calculate_scores_with_risk

def test_risk_adjusted_order():
    options = [
        OptionEvaluation(
            option=Option(name="A"),
            outcomes={"c": Outcome(best=10, expected=8, worst=4)}
        ),
        OptionEvaluation(
            option=Option(name="B"),
            outcomes={"c": Outcome(best=9, expected=7, worst=6)}
        ),
    ]
    criteria = [Criterion(name="c", weight=1.0)]
    scores = calculate_scores_with_risk(options, criteria, risk_weight=0.5)
    # A has higher expected but bigger spread, risk_weight=0.5
    assert scores["B"] > scores["A"]  # risk-adjusted
