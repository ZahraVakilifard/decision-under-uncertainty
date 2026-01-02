from core.models import OptionEvaluation, Criterion

def validate_options(options: list[OptionEvaluation], criteria: list[Criterion]) -> None:
    """
    Check that each OptionEvaluation has outcomes for all criteria
    """
    criterion_names = {c.name for c in criteria}
    for opt_eval in options:
        missing = criterion_names - set(opt_eval.outcomes.keys())
        if missing:
            raise ValueError(f"Option {opt_eval.option.name} is missing outcomes for: {missing}")
