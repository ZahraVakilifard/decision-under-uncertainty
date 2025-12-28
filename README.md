# Decision Under Uncertainty

A structured Python-based decision support system designed to model and evaluate multiple options under uncertainty.  
This project focuses on clear, modular design and sets the foundation for future AI-augmented decision-making.

---

## Project Goals

- Model real-world decision problems with explicit `Option`, `Criterion`, and `Outcome` structures.
- Ensure decisions are explainable and traceable through deterministic scoring.
- Build a clean, extensible codebase suitable for future integration of data science and AI techniques.

---

## Current Status — Phase 1

Phase 1 covers the **core domain modeling**:

- **Option**: Represents a choice in a decision scenario (e.g., Job A, Investment B).
- **Criterion**: A measurable factor used to evaluate options (e.g., cost, growth, risk).
- **Outcome**: The expected, best, and worst results for an option per criterion.

Implemented using:

- Python 3.11+
- `dataclasses` and type hints
- Modular structure for future extensibility

---

## Tech Stack

- Python 3.11+
- Standard library only (dataclasses, typing)
- PyCharm IDE for development

---

## Project Structure

```text
decision-under-uncertainty/
├── core/          # Domain models: Option, Criterion, Outcome
│   └── models.py
├── agent/         # Future AI/agent modules
│   └── agent.py
├── simulation/    # Example runs and experiments
│   └── run_simulation.py
├── tests/         # Unit and integration tests
│   └── test_models.py
├── .gitignore     # Ignore virtual environment, __pycache__, etc.
└── README.md      # This file
```


---

## Roadmap

1. **Phase 2**: Normalization, scoring, and deterministic decision evaluation
2. **Phase 3**: Agent layer for meta-reasoning and human-readable explanations
3. **Phase 4**: Optional data-driven extensions integrating predictive models

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/ZahraVakilifard/decision-under-uncertainty.git
```

2. Set up Python environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

3. Run tests to verify setup:
```bash
pytest
```