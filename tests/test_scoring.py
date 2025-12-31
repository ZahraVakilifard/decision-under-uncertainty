import pytest
from core.models import Option, Outcome, OptionEvaluation, Criterion
from core.scoring import calculate_scores

def test_calculate_scores_basic():
    options = [
        OptionEvaluation(
            option=Option(name="A"),
            outcomes={"c": Outcome(10, 8, 5)}
        ),
        OptionEvaluation(
            option=Option(name="B"),
            outcomes={"c": Outcome(8, 6, 4)}
        )
    ]
    criteria = [Criterion(name="c", weight=1.0)]
    scores = calculate_scores(options, criteria)
    assert scores["A"] > scores["B"]