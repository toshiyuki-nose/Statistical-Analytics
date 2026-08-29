"""Generate the dataset used in Chapter 07: Random Variables."""
from pathlib import Path
import pandas as pd

def find_project_root() -> Path:
    current_dir = Path.cwd().resolve()
    for candidate in [current_dir, *current_dir.parents]:
        if (candidate / "data").is_dir():
            return candidate
    return Path(__file__).resolve().parents[2]

def generate_dataset() -> pd.DataFrame:
    rows = [
        (0, 0.35, "No delayed deliveries"),
        (1, 0.45, "One delayed delivery"),
        (2, 0.15, "Two delayed deliveries"),
        (3, 0.05, "Three delayed deliveries"),
    ]
    return pd.DataFrame(rows, columns=["delayed_deliveries", "probability", "description"])

def main() -> None:
    project_root = find_project_root()
    output_path = project_root / "data" / "07_random_variables.csv"
    df = generate_dataset()
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Created: {output_path}")
    print(f"Rows: {len(df)}")
    print(df)

if __name__ == "__main__":
    main()
