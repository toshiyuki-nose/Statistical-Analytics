"""Generate the synthetic dataset used in Chapter 01.

The dataset uses fictional country and region names. Its purpose is to
introduce observations, variables, data types, and measurement scales.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = PROJECT_ROOT / "data" / "01_data_and_variables.csv"


def build_dataset() -> pd.DataFrame:
    """Return the Chapter 01 synthetic country dataset."""
    records = [
        ("Country_01", "Region_A", "High", 18.4, 42500, 82.1, 79.2),
        ("Country_02", "Region_A", "Upper-Middle", 46.7, 18600, 77.4, 68.5),
        ("Country_03", "Region_B", "Lower-Middle", 92.3, 7200, 71.8, 54.1),
        ("Country_04", "Region_B", "Low", 31.5, 2800, 66.9, 39.7),
        ("Country_05", "Region_C", "High", 7.8, 58300, 84.0, 86.4),
        ("Country_06", "Region_C", "Upper-Middle", 64.2, 21400, 78.6, 72.8),
        ("Country_07", "Region_D", "Lower-Middle", 128.6, 9100, 73.2, 58.9),
        ("Country_08", "Region_D", "Low", 54.9, 3400, 68.5, 43.3),
        ("Country_09", "Region_E", "High", 12.1, 49700, 81.3, 82.7),
        ("Country_10", "Region_E", "Upper-Middle", 38.6, 17200, 76.1, 65.4),
        ("Country_11", "Region_F", "Lower-Middle", 76.4, 6400, 70.5, 49.8),
        ("Country_12", "Region_F", "Low", 22.7, 2100, 64.8, 35.6),
    ]

    columns = [
        "country_id",
        "region",
        "income_group",
        "population_million",
        "gdp_per_capita_usd",
        "life_expectancy",
        "urbanization_rate",
    ]
    return pd.DataFrame(records, columns=columns)


def main() -> None:
    """Create the data directory and write the CSV file."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataset = build_dataset()
    dataset.to_csv(OUTPUT_PATH, index=False)
    print(f"Created {OUTPUT_PATH}")
    print(f"Rows: {len(dataset)}, Columns: {len(dataset.columns)}")


if __name__ == "__main__":
    main()
