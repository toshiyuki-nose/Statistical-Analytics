"""Generate Chapter 12: Hypothesis Testing educational dataset."""
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
    N = 120

    response_times = np.clip(
        rng.normal(loc=31.8, scale=6.5, size=N),
        12,
        55,
    ).round(1)

    channels = rng.choice(
        ["Email", "Chat", "Phone"],
        size=N,
        p=[0.40, 0.35, 0.25],
    )

    return pd.DataFrame({
        "case_id": [f"Case_{i:03d}" for i in range(1, N + 1)],
        "channel": channels,
        "response_time_minutes": response_times,
    })

if __name__ == "__main__":
    out = find_project_root() / "data" / "12_hypothesis_testing.csv"
    df = generate_dataset()
    df.to_csv(out, index=False)
    print(f"Created: {out}")
    print(df.head())
