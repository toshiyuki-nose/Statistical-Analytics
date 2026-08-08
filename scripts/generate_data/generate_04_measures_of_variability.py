"""Generate Chapter 04: Measures of Variability dataset."""

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
        ("Country_01","Region_A",42000),("Country_02","Region_A",45000),("Country_03","Region_A",47000),("Country_04","Region_A",39000),
        ("Country_05","Region_A",41000),("Country_06","Region_B",28000),("Country_07","Region_B",30000),("Country_08","Region_B",31000),
        ("Country_09","Region_B",29000),("Country_10","Region_B",32000),("Country_11","Region_C",18000),("Country_12","Region_C",20000),
        ("Country_13","Region_C",19000),("Country_14","Region_C",21000),("Country_15","Region_C",22000),("Country_16","Region_D",12000),
        ("Country_17","Region_D",14000),("Country_18","Region_D",15000),("Country_19","Region_D",16000),("Country_20","Region_D",17000),
        ("Country_21","Region_A",43000),("Country_22","Region_A",44000),("Country_23","Region_B",33000),("Country_24","Region_B",34000),
        ("Country_25","Region_C",23000),("Country_26","Region_C",24000),("Country_27","Region_D",18000),("Country_28","Region_D",19000),
        ("Country_29","Region_A",46000),("Country_30","Region_A",47000),("Country_31","Region_B",35000),("Country_32","Region_B",36000),
        ("Country_33","Region_C",25000),("Country_34","Region_C",26000),("Country_35","Region_D",20000),("Country_36","Region_D",21000),
        ("Country_37","Region_A",48000),("Country_38","Region_B",37000),("Country_39","Region_C",27000),("Country_40","Region_A",250000),
    ]
    return pd.DataFrame(rows, columns=["country_id","region","gdp_per_capita_usd"])


def main() -> None:
    project_root = find_project_root()
    output_path = project_root / "data" / "04_measures_of_variability.csv"
    df = generate_dataset()
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Created: {output_path}")
    print(f"Rows: {len(df)}")
    print(df.head())


if __name__ == "__main__":
    main()
