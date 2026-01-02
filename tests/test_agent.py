from core.agent import risk_aware_agent
from core.strategies import RiskAverseStrategy
from core.models import Option, OptionEvaluation, Outcome, Criterion


def test_risk_aware_agent():
    options = [
        OptionEvaluation(
            option=Option(name="A"),
            outcomes={
                "salary": Outcome(best=10, expected=8, worst=5),
                "growth": Outcome(best=5, expected=4, worst=3),
            },
        ),
        OptionEvaluation(
            option=Option(name="B"),
            outcomes={
                "salary": Outcome(best=9, expected=7, worst=5),
                "growth": Outcome(best=6, expected=5, worst=4),
            },
        ),
    ]

    criteria = [
        Criterion(name="salary", weight=0.6, maximize=True),
        Criterion(name="growth", weight=0.4, maximize=True),
    ]

    result = risk_aware_agent(
        options,
        criteria,
        strategy=RiskAverseStrategy(),
        risk_weight=0.5,
    )

    assert "A" in result["scores"]
    assert "B" in result["scores"]
    assert len(result["ranking"]) == 2
