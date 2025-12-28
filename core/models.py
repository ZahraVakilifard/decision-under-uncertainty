from dataclasses import dataclass

@dataclass(frozen=True)
class Option:
    """
    Represents a decision option.
    Example: Job Offer A, Migration Path B, Investment C
    """
    name: str
    description: str | None = None

@dataclass(frozen=True)
class Outcome:
    """
    Represents uncertainty in outcomes.
    Values must be comparable across options.
    """
    best: float
    expected: float
    worst: float

    def validate(self) -> None:
        if not (self.best >= self.expected >= self.worst):
            raise ValueError(
                "Outcome values must satisfy: best >= expected >= worst"
            )


@dataclass(frozen=True)
class Criterion:
    """
    Represents a decision criterion.
    Example: cost, risk, growth, stability
    """
    name: str
    weight: float
    maximize: bool = True  # False if lower is better (e.g., cost, risk)

    def validate(self) -> None:
        if not 0.0 <= self.weight <= 1.0:
            raise ValueError("Criterion weight must be between 0 and 1")


@dataclass(frozen=True)
class OptionEvaluation:
    """
    Binds an Option to its outcomes per criterion.
    """
    option: Option
    outcomes: dict[str, Outcome]
