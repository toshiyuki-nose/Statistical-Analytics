"""Generate synthetic data for Chapter 22 — Bootstrap."""

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
    raise FileNotFoundError("Could not find project root containing data/.")

def generate_data() -> pd.DataFrame:
    rng = np.random.default_rng(SEED)

    delivery = np.clip(
        rng.gamma(shape=4.0, scale=4.5, size=N) + 18,
        15,
        None,
    )
    distance = rng.uniform(1.5, 25.0, N)
    orders = rng.integers(1, 9, N)
    satisfaction = np.clip(
        np.rint(
            5.5
            - 0.055 * delivery
            + rng.normal(0, 0.65, N)
        ),
        1,
        5,
    ).astype(int)

    return pd.DataFrame({
        "delivery_id": [f"D{i:03d}" for i in range(1, N + 1)],
        "delivery_time_minutes": np.round(delivery, 1),
        "distance_km": np.round(distance, 1),
        "orders_in_batch": orders,
        "satisfaction_score": satisfaction,
    })

if __name__ == "__main__":
    root = find_project_root(Path.cwd())
    output = root / "data" / "22_bootstrap.csv"
    generate_data().to_csv(output, index=False)
    print(f"Created: {output}")
