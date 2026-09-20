"""Generate the synthetic dataset for Chapter 20 — Logistic Regression."""

from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
N = 160

def find_project_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "data").is_dir():
            return candidate
    raise FileNotFoundError("Could not find the project root containing a data/ directory.")

def generate_data() -> pd.DataFrame:
    rng = np.random.default_rng(SEED)

    training = rng.uniform(0.5, 14.0, N)
    experience = rng.uniform(0.5, 15.0, N)
    project_load = rng.integers(1, 8, N)

    logit = (
        -2.6
        + 0.23 * training
        + 0.10 * experience
        - 0.20 * project_load
    )
    probability = 1 / (1 + np.exp(-logit))
    promoted = rng.binomial(1, probability, N)

    return pd.DataFrame({
        "employee_id": [f"E{i:03d}" for i in range(1, N + 1)],
        "training_hours": np.round(training, 1),
        "experience_years": np.round(experience, 1),
        "project_load": project_load,
        "promoted": promoted,
    })

if __name__ == "__main__":
    root = find_project_root(Path.cwd())
    output_path = root / "data" / "20_logistic_regression.csv"
    generate_data().to_csv(output_path, index=False)
    print(f"Created: {output_path}")
