from core.agent import risk_aware_agent
from core.strategies import RiskAverseStrategy
from core.models import Option, OptionEvaluation, Outcome, Criterion

if __name__ == "__main__":
    # define criteria
    criteria = [
        Criterion(name="salary", weight=0.6, maximize=True),
        Criterion(name="growth", weight=0.4, maximize=True),
    ]

    # define options + outcomes
    options = [
        OptionEvaluation(
            option=Option(name="Job A"),
            outcomes={
                "salary": Outcome(best=100, expected=90, worst=70),
                "growth": Outcome(best=8, expected=6, worst=4),
            },
        ),
        OptionEvaluation(
            option=Option(name="Job B"),
            outcomes={
                "salary": Outcome(best=95, expected=85, worst=75),
                "growth": Outcome(best=9, expected=7, worst=5),
            },
        ),
    ]

    result = risk_aware_agent(
        options,
        criteria,
        strategy=RiskAverseStrategy(),
        risk_weight=0.5,
    )

    for opt, bd in result["breakdown"].items():
        print(f"Option: {opt}")
        for crit, score in bd.items():
            print(f"  {crit}: {score:.2f}")
        print(f"  Total Score: {result['scores'][opt]:.3f}")

    print("Ranking:", [r[0] for r in result["ranking"]])