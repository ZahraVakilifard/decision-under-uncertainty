import pytest
from core.models import Outcome, Criterion, Option

def test_valid_outcome():
    o = Outcome(best=100, expected=70, worst=40)
    o.validate()

def test_invalid_outcome():
    o = Outcome(best=50, expected=70, worst=30)
    with pytest.raises(ValueError):
        o.validate()

def test_valid_criterion():
    c = Criterion(name="cost", weight=0.3, maximize=False)
    c.validate()

def test_invalid_criterion_weight():
    c = Criterion(name="risk", weight=1.5)
    with pytest.raises(ValueError):
        c.validate()
