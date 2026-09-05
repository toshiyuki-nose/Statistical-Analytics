"""Generate Chapter 11: Confidence Intervals educational dataset."""
from pathlib import Path
import numpy as np
import pandas as pd

def find_project_root() -> Path:
    cwd = Path.cwd().resolve()
    for p in [cwd, *cwd.parents]:
        if (p / "data").is_dir():
            return p
    return Path(__file__).resolve().parents[2]

def generate_dataset(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    N = 2000
    departments = rng.choice(
        ["Department_A", "Department_B", "Department_C", "Department_D"],
        size=N,
        p=[0.30, 0.25, 0.25, 0.20],
    )
    effects = {
        "Department_A": 0,
        "Department_B": 3,
        "Department_C": -2,
        "Department_D": 5,
    }
    commute = np.array([
        rng.normal(42 + effects[d], 11)
        for d in departments
    ])
    commute = np.clip(commute, 10, 90).round(1)

    return pd.DataFrame({
        "employee_id": [f"Employee_{i:04d}" for i in range(1, N + 1)],
        "department": departments,
        "commute_time_minutes": commute,
    })

if __name__ == "__main__":
    out = find_project_root() / "data" / "11_confidence_intervals.csv"
    df = generate_dataset()
    df.to_csv(out, index=False)
    print(f"Created: {out}")
    print(df.head())
