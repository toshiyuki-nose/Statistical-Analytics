"""Generate Chapter 08: Discrete Probability Distributions dataset."""

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
        ("Bernoulli", "Delivery arrives on time", 1, 0.80),
        ("Binomial", "On-time deliveries among 10 deliveries", 10, 0.80),
        ("Binomial", "Successful inspections among 8 inspections", 8, 0.70),
        ("Binomial", "Customers who purchase among 12 visitors", 12, 0.25),
    ]
    return pd.DataFrame(
        rows,
        columns=[
            "distribution",
            "scenario",
            "n_trials",
            "success_probability",
        ],
    )


def main() -> None:
    project_root = find_project_root()
    output_path = project_root / "data" / "08_discrete_probability_distributions.csv"
    df = generate_dataset()
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Created: {output_path}")
    print(df)


if __name__ == "__main__":
    main()
