"""Generate Chapter 15: ANOVA synthetic educational data."""
from pathlib import Path
import numpy as np
import pandas as pd

def find_project_root() -> Path:
    cwd = Path.cwd().resolve()
    for p in [cwd, *cwd.parents]:
        if (p / "data").is_dir():
            return p
    return Path(__file__).resolve().parents[2]

rng = np.random.default_rng(42)

groups = {
    "Method_A": (30, 72, 8),
    "Method_B": (32, 76, 8),
    "Method_C": (31, 82, 9),
}

rows = []
idx = 1

for group, (n, mu, sigma) in groups.items():
    scores = np.clip(rng.normal(mu, sigma, n), 40, 100).round(1)
    for score in scores:
        rows.append([
            f"Participant_{idx:03d}",
            group,
            score,
        ])
        idx += 1

df = pd.DataFrame(
    rows,
    columns=["participant_id", "training_method", "assessment_score"],
)

out = find_project_root() / "data" / "15_anova.csv"
df.to_csv(out, index=False)

print(f"Created: {out}")
print(df.groupby("training_method")["assessment_score"].agg(["count", "mean", "std"]))
