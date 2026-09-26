"""Generate synthetic data for Chapter 21 — Nonparametric Statistics."""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
N = 80

def find_project_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "data").is_dir():
            return candidate
    raise FileNotFoundError("Could not find project root containing data/.")

def generate_data() -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    group = np.array(["A"] * 40 + ["B"] * 40)
    completion = np.concatenate([
        rng.gamma(3.0, 8.0, 40) + 20,
        rng.gamma(3.0, 7.0, 40) + 17,
    ])
    before = np.clip(np.rint(rng.normal(68, 9, N)), 40, 95).astype(int)
    improvement = rng.choice(
        range(8), N, p=[.08, .10, .14, .18, .18, .14, .10, .08]
    )
    after = np.clip(before + improvement + rng.integers(-2, 3, N), 40, 100).astype(int)
    satisfaction = rng.integers(1, 6, N)
    response = np.clip(
        75 - 9 * satisfaction + rng.gamma(2.2, 5.0, N), 5, None
    )
    return pd.DataFrame({
        "employee_id": [f"E{i:03d}" for i in range(1, N + 1)],
        "group": group,
        "completion_time_minutes": np.round(completion, 1),
        "score_before": before,
        "score_after": after,
        "satisfaction_level": satisfaction,
        "response_time_minutes": np.round(response, 1),
    })

if __name__ == "__main__":
    root = find_project_root(Path.cwd())
    path = root / "data" / "21_nonparametric_statistics.csv"
    generate_data().to_csv(path, index=False)
    print(f"Created: {path}")
