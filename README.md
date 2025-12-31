# Decision Under Uncertainty

A structured Python-based decision support system designed to model and evaluate multiple options under uncertainty.  
This project focuses on clear, modular design and sets the foundation for future AI-augmented decision-making.

---

## Project Goals

- Model real-world decision problems with explicit `Option`, `Criterion`, and `Outcome` structures.
- Ensure decisions are explainable and traceable through deterministic scoring.
- Build a clean, extensible codebase suitable for future integration of data science and AI techniques.

---

## Phase 1: Domain Modeling (Completed)

Phase 1 covers the **core domain modeling**:

- **Option**: Represents a choice in a decision scenario (e.g., Job A, Investment B).
- **Criterion**: A measurable factor used to evaluate options (e.g., cost, growth, risk).
- **Outcome**: The expected, best, and worst results for an option per criterion.

---

## Phase 2: Normalization & Scoring (Completed)

Phase 2 introduces deterministic decision evaluation.

- Normalization of heterogeneous metrics to a common 0–1 scale
- Support for both maximization and minimization criteria
- Weighted aggregation of scores across multiple options
- Fully testable and explainable scoring pipeline

This phase enables objective comparison of complex options under uncertainty.

---

### Example — Phase 2 Decision Scoring

This example demonstrates how the system evaluates multiple options using
normalized and weighted criteria under uncertainty.

The scenario compares two job offers based on three criteria:
- Salary (maximize)
- Growth potential (maximize)
- Risk level (minimize)

Each option defines best, expected, and worst outcomes per criterion.
Phase 2 focuses on scoring using the expected values.

### Options Definition

**Job A**
- Salary: best 120, expected 100, worst 80
- Growth: best 10, expected 7, worst 5
- Risk: best 5, expected 7, worst 10

**Job B**
- Salary: best 110, expected 95, worst 80
- Growth: best 12, expected 8, worst 4
- Risk: best 3, expected 5, worst 8

### Criteria Configuration

| Criterion | Weight | Objective |
|---------|--------|-----------|
| Salary  | 0.5    | Maximize  |
| Growth  | 0.3    | Maximize  |
| Risk    | 0.2    | Minimize  |

Weights sum to 1.0 and reflect relative importance.

### Scoring Process

1. Extract expected values for each criterion
2. Normalize values to a 0–1 scale
3. Apply criterion weights
4. Aggregate weighted scores per option

The scoring logic is fully deterministic and explainable.

### Expected Result

```text
{
  "Job A": ~0.65,
  "Job B": ~0.70
}
```
---

### Tech Stack

- Python 3.13+
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

**Phase 3**: Uncertainty strategies and meta-reasoning agent
(risk-averse vs risk-seeking decision styles, human-readable explanations)

**Phase 4**: Data-driven extensions
(simulations, predictive models, ML integration)

**Phase 5**: AI-assisted decision advisor
(LLM-backed, explainable, decision-aware)

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
