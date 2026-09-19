"""Generate the synthetic dataset for Chapter 16 — Covariance."""

from pathlib import Path
import csv
import random

SEED = 42
N = 60

def find_project_root(start: Path) -> Path:
    """Find the repository root by locating its data directory."""
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "data").is_dir():
            return candidate
    raise FileNotFoundError("Could not find the project root containing a data/ directory.")

def generate_rows():
    random.seed(SEED)
    rows = []
    for i in range(1, N + 1):
        study_hours = round(random.uniform(1.5, 12.0), 1)
        exam_score = round(
            max(40, min(100, 48 + 3.4 * study_hours + random.gauss(0, 8))),
            1,
        )
        leisure_hours = round(
            max(0.5, min(8.0, 7.2 - 0.38 * study_hours + random.gauss(0, 1.1))),
            1,
        )
        rows.append([
            f"S{i:03d}",
            study_hours,
            exam_score,
            leisure_hours,
        ])
    return rows

if __name__ == "__main__":
    root = find_project_root(Path.cwd())
    output_path = root / "data" / "16_covariance.csv"

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "student_id",
            "study_hours_per_week",
            "exam_score",
            "leisure_hours_per_day",
        ])
        writer.writerows(generate_rows())

    print(f"Created: {output_path}")
