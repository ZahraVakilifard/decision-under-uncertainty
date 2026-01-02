from core.agent import risk_aware_agent
from core.models import Option, OptionEvaluation, Outcome, Criterion
from core.strategies import RiskAverseStrategy
import matplotlib.pyplot as plt

# --- Options & Criteria ---
options = [
    OptionEvaluation(
        Option("Job A"),
        {"salary": Outcome(120,100,80), "growth": Outcome(10,7,5), "risk": Outcome(5,7,10)}
    ),
    OptionEvaluation(
        Option("Job B"),
        {"salary": Outcome(110,95,80), "growth": Outcome(12,8,4), "risk": Outcome(3,5,8)}
    )
]

criteria = [
    Criterion("salary", 0.5, True),
    Criterion("growth", 0.3, True),
    Criterion("risk", 0.2, False)
]

# --- Sensitivity Analysis ---
results = {}
for rw in [i/10 for i in range(0,11)]:
    res = risk_aware_agent(options, criteria, strategy=RiskAverseStrategy(), risk_weight=rw)
    results[rw] = res["scores"]

# --- Visualization ---
def plot_sensitivity(results, options):
    risk_weights = sorted(results.keys())
    for opt in options:
        scores = [results[rw][opt] for rw in risk_weights]
        plt.plot(risk_weights, scores, marker='o', label=opt)
    plt.xlabel("Risk Weight")
    plt.ylabel("Score")
    plt.title("Sensitivity Analysis of Options")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_sensitivity(results, ["Job A", "Job B"])
