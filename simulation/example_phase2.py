from core.models import Option, Outcome, OptionEvaluation, Criterion
from core.scoring import calculate_scores

# options definition
options = [
    OptionEvaluation(
        option=Option(name="Job A"),
        outcomes={
            "salary": Outcome(best=120, expected=100, worst=80),
            "growth": Outcome(best=10, expected=7, worst=5),
            "risk": Outcome(best=5, expected=7, worst=10),
        },
    ),
    OptionEvaluation(
        option=Option(name="Job B"),
        outcomes={
            "salary": Outcome(best=110, expected=95, worst=80),
            "growth": Outcome(best=12, expected=8, worst=4),
            "risk": Outcome(best=3, expected=5, worst=8),
        },
    ),
]

# criteria definition
criteria = [
    Criterion(name="salary", weight=0.5, maximize=True),
    Criterion(name="growth", weight=0.3, maximize=True),
    Criterion(name="risk", weight=0.2, maximize=False),
]

scores = calculate_scores(options, criteria)
print(scores)
