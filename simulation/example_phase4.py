from core.models import Option, Outcome, OptionEvaluation, Criterion
from core.strategies import ExpectedValueStrategy, RiskAverseStrategy, RegretMinimizationStrategy

options = [
    OptionEvaluation(
        option=Option("Job A"),
        outcomes={"salary": Outcome(120,100,80), "growth": Outcome(10,7,5), "risk": Outcome(5,7,10)}
    ),
    OptionEvaluation(
        option=Option("Job B"),
        outcomes={"salary": Outcome(110,95,80), "growth": Outcome(12,8,4), "risk": Outcome(3,5,8)}
    ),
]

criteria = [
    Criterion("salary", 0.5, True),
    Criterion("growth", 0.3, True),
    Criterion("risk", 0.2, False)
]

strategies = [ExpectedValueStrategy(), RiskAverseStrategy(), RegretMinimizationStrategy()]

for strat in strategies:
    print(f"--- {strat.__class__.__name__} ---")
    scores = strat.evaluate(options, criteria, risk_weight=0.5)
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for name, score in ranked:
        print(f"{name}: {score:.3f}")
