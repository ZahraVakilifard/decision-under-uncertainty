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



### Example — Phase 2 Decision Scoring

```angular2html
from core.models import Option, OptionEvaluation, Outcome, Criterion
from core.strategies import ExpectedValueStrategy

# Options
options = [
    OptionEvaluation(
        Option("Job A"),
        {"salary": Outcome(120, 100, 80), "growth": Outcome(10, 7, 5), "risk": Outcome(5, 7, 10)}
    ),
    OptionEvaluation(
        Option("Job B"),
        {"salary": Outcome(110, 95, 80), "growth": Outcome(12, 8, 4), "risk": Outcome(3, 5, 8)}
    )
]

# Criteria
criteria = [
    Criterion("salary", 0.5, True),
    Criterion("growth", 0.3, True),
    Criterion("risk", 0.2, False)
]

# Scoring
scores = ExpectedValueStrategy().evaluate(options, criteria, risk_weight=0.5)
print(scores)

```
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

## Phase 3: Uncertainty & Risk Strategies (Completed)
Phase 3 introduces decision-making strategies under uncertainty:

- **Expected Value Strategy**: Simple, risk-adjusted expected score

- **Risk-Averse Strategy**: Penalizes options with high spread (less stable)

- **Regret Minimization Strategy**: Considers worst-case scenario to reduce potential regret

All strategies are **modular**, follow the same interface, and produce **human-readable**, **ranked outputs**.

### Phase 3 Example
```angular2html
from core.strategies import ExpectedValueStrategy, RiskAverseStrategy, RegretMinimizationStrategy
scores = ExpectedValueStrategy().evaluate(options, criteria, risk_weight=0.5)
```
- Outputs ranking of options

- Supports **all criteria**, including growth, salary, and risk

- Normalized and weighted scores allow **fair comparison**

---

## Phase 4: Decision Strategies & Data-Driven Extensions (Completed)
Phase 4 enhances decision-making by **applying multiple strategies and risk adjustments simultaneously**:

- Expected Value
- Risk-Averse
- Regret Minimization
- Supports risk_weight parameter to tune decision conservatism
- Fully incorporates all criteria with weights and maximize/minimize objectives
- Prepares the system for sensitivity analysis and AI-assisted decision recommendations

```angular2html
strategies = [ExpectedValueStrategy(), RiskAverseStrategy(), RegretMinimizationStrategy()]

for strat in strategies:
    scores = strat.evaluate(options, criteria, risk_weight=0.5)
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print(f"{strat.__class__.__name__}: {ranked}")
```
- Phase 4 outputs option rankings per strategy
- Allows comparison of short-term vs long-term, risk-prone vs risk-averse decisions

---

## Phase 5: Sensitivity Analysis
- Test effect of changing criterion weights and risk_weight.
- Analyze ranking stability under different assumptions.
- Prepare for visualization and AI-assisted decisions.

---

## Phase 6: AI Decision Agent

Integrates risk-aware scoring, growth, and spread.

Produces human-readable breakdown for each option:

- Expected value
- Spread-adjusted score
- Total weighted score

Ready for future LLM / AI assistance.

### Example

```python
from core.agent import risk_aware_agent
from core.strategies import RiskAverseStrategy

result = risk_aware_agent(
    options, 
    criteria, 
    strategy=RiskAverseStrategy(), 
    risk_weight=0.5
)

for opt, bd in result["breakdown"].items():
    print(f"Option: {opt}")
    for crit, score in bd.items():
        print(f"  {crit}: {score:.2f}")
    print(f"  Total Score: {result['scores'][opt]:.3f}")

print("Ranking:", [r[0] for r in result["ranking"]])
```

---

## Phase 7: Project Polishing & Visualization

- Add visualization for sensitivity analysis using matplotlib.
- Provide integration-ready examples in simulation/.
- Prepare GitHub-ready README, modular structure, and full tests.

```angular2html
import matplotlib.pyplot as plt
from core.sensitivity import sensitivity_analysis

results = sensitivity_analysis(options, criteria, strategy=RiskAverseStrategy())
for opt in ["Job A", "Job B"]:
    scores = [results[rw][opt] for rw in sorted(results.keys())]
    plt.plot(sorted(results.keys()), scores, marker='o', label=opt)
plt.xlabel("Risk Weight")
plt.ylabel("Score")
plt.title("Sensitivity Analysis")
plt.legend()
plt.show()

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
├── core/          # Domain models & core logic
│   ├── agent.py
│   ├── models.py
│   ├── normalization.py
│   ├── scoring.py
│   ├── sensitivity.py
│   ├── strategies.py
│   ├── uncertainty.py
│   └── validation.py
├── simulation/    # Example runs & experiments
│   ├── example_phase2.py
│   ├── example_phase3.py
│   ├── example_phase4.py
│   └── sensitivity_example.py
├── tests/         # Unit & integration tests
│   ├── test_agent.py
│   ├── test_models.py
│   ├── test_scoring.py
│   ├── test_sensitivity.py
│   ├── test_strategies.py
│   └── test_uncertainty.py
├── main.py        # Demo script
├── README.md

```

---

## Roadmap

| Phase | Status | Focus |
|-------|--------|-------|
| 1     | ✅ Completed | Domain Modeling (Option, Criterion, Outcome) |
| 2     | ✅ Completed | Normalization & Scoring |
| 3     | ✅ Completed | Uncertainty & Risk Strategies |
| 4     | ✅ Completed | Decision Strategies & Risk Adjustment |
| 5     | ✅ Completed | Sensitivity Analysis & Scenario Testing |
| 6     | ✅ Completed | AI Decision Agent & Explainable Ranking |
| 7     | ✅ Completed | Visualization & GitHub-Ready Polishing |

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/ZahraVakilifard/decision-under-uncertainty.git
cd decision-under-uncertainty
```

2. Set up Python environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

3. Run all tests
```bash
pytest
```
