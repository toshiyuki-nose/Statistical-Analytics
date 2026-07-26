"""
Generate the dataset used in Chapter 02: Frequency Distributions.

The generated dataset contains fictional countries and regions.
It is designed for learning frequency tables, relative frequencies,
cumulative frequencies, class intervals, and histograms.
"""

from pathlib import Path

import numpy as np
import pandas as pd


def find_project_root() -> Path:
    """Find the repository root containing the data directory."""
    current_dir = Path.cwd().resolve()

    for candidate in [current_dir, *current_dir.parents]:
        if (candidate / "data").is_dir():
            return candidate

    # When this script is run directly from scripts/generate_data/,
    # parents[2] points to the repository root.
    return Path(__file__).resolve().parents[2]


def generate_dataset(seed: int = 42) -> pd.DataFrame:
    """Generate a reproducible fictional country dataset."""
    rng = np.random.default_rng(seed)

    regions = ["Region_A", "Region_B", "Region_C", "Region_D"]
    region_means = {
        "Region_A": 7.0,
        "Region_B": 6.2,
        "Region_C": 5.5,
        "Region_D": 4.8,
    }

    rows = []
    country_number = 1

    for region in regions:
        scores = rng.normal(
            loc=region_means[region],
            scale=0.65,
            size=10,
        )
        scores = np.clip(scores, 3.0, 8.5)
        scores = np.round(scores, 1)

        for score in scores:
            rows.append(
                {
                    "country_id": f"Country_{country_number:02d}",
                    "region": region,
                    "happiness_score": float(score),
                }
            )
            country_number += 1

    return pd.DataFrame(rows)


def main() -> None:
    project_root = find_project_root()
    output_path = project_root / "data" / "02_frequency_distributions.csv"

    df = generate_dataset()
    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"Created: {output_path}")
    print(f"Rows: {len(df)}")
    print(df.head())


if __name__ == "__main__":
    main()
