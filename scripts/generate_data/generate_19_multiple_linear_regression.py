"""Generate the synthetic dataset for Chapter 19 — Multiple Linear Regression."""

from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
N = 120

def find_project_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "data").is_dir():
            return candidate
    raise FileNotFoundError("Could not find the project root containing a data/ directory.")

def generate_data() -> pd.DataFrame:
    rng = np.random.default_rng(SEED)

    experience = rng.uniform(0.5, 15.0, N)
    training = np.clip(
        3.0 + 0.28 * experience + rng.normal(0, 2.5, N),
        0.5,
        14.0,
    )
    project_load = rng.integers(1, 8, N)
    noise = rng.normal(0, 6.5, N)

    performance = (
        48
        + 2.25 * training
        + 1.15 * experience
        - 1.35 * project_load
        + noise
    )
    performance = np.clip(performance, 35, 100)

    return pd.DataFrame({
        "employee_id": [f"E{i:03d}" for i in range(1, N + 1)],
        "training_hours": np.round(training, 1),
        "experience_years": np.round(experience, 1),
        "project_load": project_load,
        "performance_score": np.round(performance, 1),
    })

if __name__ == "__main__":
    root = find_project_root(Path.cwd())
    output_path = root / "data" / "19_multiple_linear_regression.csv"
    generate_data().to_csv(output_path, index=False)
    print(f"Created: {output_path}")
