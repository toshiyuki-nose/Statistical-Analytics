"""Generate the synthetic dataset for Chapter 17 — Correlation Analysis."""

from pathlib import Path
import csv
import random

SEED = 42
N = 80

def find_project_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "data").is_dir():
            return candidate
    raise FileNotFoundError("Could not find the project root containing a data/ directory.")

def generate_rows():
    random.seed(SEED)
    rows = []
    for i in range(1, N + 1):
        training = round(random.uniform(0.5, 12.0), 1)
        performance = round(max(40, min(100, 55 + 3.0 * training + random.gauss(0, 8))), 1)
        experience = round(random.uniform(0.2, 12.0), 1)
        commute = round(max(5, min(90, 38 + random.gauss(0, 14))), 1)
        rows.append([f"E{i:03d}", training, performance, experience, commute])
    return rows

if __name__ == "__main__":
    root = find_project_root(Path.cwd())
    output_path = root / "data" / "17_correlation_analysis.csv"

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "employee_id",
            "training_hours",
            "performance_score",
            "experience_years",
            "commute_minutes",
        ])
        writer.writerows(generate_rows())

    print(f"Created: {output_path}")
