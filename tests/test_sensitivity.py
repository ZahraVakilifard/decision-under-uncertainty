from core.models import Option, Outcome, OptionEvaluation, Criterion
from core.strategies import ExpectedValueStrategy
from core.sensitivity import sensitivity_analysis


def test_sensitivity_realistic():
    options = [
        OptionEvaluation(option=Option("A"), outcomes={"c": Outcome(10, 8, 5)}),
        OptionEvaluation(option=Option("B"), outcomes={"c": Outcome(8, 7, 6)})
    ]

    criteria = [Criterion("c", 1.0)]
    strategy = ExpectedValueStrategy()
    risk_weights = [0.0, 0.5, 1.0]

    results = sensitivity_analysis(options, criteria, strategy, risk_weights=risk_weights)

    # Dominance at zero risk
    scores_r0 = results[0.0]
    assert scores_r0["A"] > scores_r0["B"], "At zero risk, A should dominate B"

    # Risk reversal at high risk
    scores_r1 = results[1.0]
    assert scores_r1["B"] > scores_r1["A"], "At high risk, B should be preferred due to lower spread"

    # Optional: ranking consistency for all weights (relative, not absolute)
    for rw in risk_weights:
        scores = results[rw]
        ranked_options = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        assert ranked_options[0][0] in ["A", "B"], f"Unexpected top option at risk_weight={rw}"
