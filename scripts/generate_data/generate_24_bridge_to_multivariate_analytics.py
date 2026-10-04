from pathlib import Path
import csv
import random

SEED = 42
N = 90

random.seed(SEED)

def clamp(x, lo=0, hi=100):
    return max(lo, min(hi, x))

def find_project_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "data").exists():
            return candidate
    return Path(__file__).resolve().parents[2]

def generate_rows():
    rows = []

    # Three latent profiles are used only to create an educational dataset
    # with meaningful multivariate structure. They are not written as labels.
    profiles = [
        {"development": 72, "connectivity": 70, "labor": 68},
        {"development": 52, "connectivity": 48, "labor": 55},
        {"development": 34, "connectivity": 30, "labor": 43},
    ]

    for i in range(1, N + 1):
        profile = profiles[(i - 1) % 3]

        development = random.gauss(profile["development"], 7)
        connectivity = random.gauss(profile["connectivity"], 8)
        labor = random.gauss(profile["labor"], 7)

        income_index = clamp(
            0.62 * development + 0.20 * labor + random.gauss(12, 5)
        )
        education_index = clamp(
            0.72 * development + 0.12 * connectivity + random.gauss(10, 5)
        )
        health_index = clamp(
            0.67 * development + 0.10 * labor + random.gauss(15, 5)
        )
        employment_index = clamp(
            0.35 * development + 0.55 * labor + random.gauss(8, 5)
        )
        digital_access_index = clamp(
            0.25 * development + 0.70 * connectivity + random.gauss(5, 5)
        )

        rows.append({
            "region_id": f"R{i:03d}",
            "income_index": round(income_index, 1),
            "education_index": round(education_index, 1),
            "health_index": round(health_index, 1),
            "employment_index": round(employment_index, 1),
            "digital_access_index": round(digital_access_index, 1),
        })

    random.shuffle(rows)
    return rows

def main():
    root = find_project_root(Path.cwd())
    output = root / "data" / "24_bridge_to_multivariate_analytics.csv"
    output.parent.mkdir(parents=True, exist_ok=True)

    rows = generate_rows()
    fieldnames = list(rows[0].keys())

    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created: {output}")
    print(f"Rows: {len(rows)}")

if __name__ == "__main__":
    main()
