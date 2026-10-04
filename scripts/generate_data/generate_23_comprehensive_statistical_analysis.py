from pathlib import Path
import csv
import math
import random

SEED = 42
N = 240

random.seed(SEED)

def clamp(x, lo, hi):
    return max(lo, min(hi, x))

def weighted_choice(items, weights):
    return random.choices(items, weights=weights, k=1)[0]

def generate_rows():
    rows = []

    tracks = ["Data", "Business", "Technology"]
    styles = ["Self-paced", "Group", "Mentored"]

    track_effect = {"Data": 1.5, "Business": -0.5, "Technology": 0.5}
    style_effect = {"Self-paced": -1.0, "Group": 0.5, "Mentored": 2.0}

    for i in range(1, N + 1):
        program_track = weighted_choice(tracks, [0.38, 0.30, 0.32])
        study_style = weighted_choice(styles, [0.38, 0.34, 0.28])

        prior_score = clamp(random.gauss(61, 12), 25, 92)

        # Right-skewed weekly study time, capped to a realistic educational range.
        study_hours = clamp(random.gammavariate(3.0, 2.2), 1.0, 18.0)

        style_attendance = {"Self-paced": -3.0, "Group": 1.0, "Mentored": 4.0}[study_style]
        attendance_rate = clamp(
            70 + 0.65 * study_hours + style_attendance + random.gauss(0, 9),
            40,
            100,
        )

        # Support usage is discrete and somewhat more common in mentored learning.
        support_lambda = {
            "Self-paced": 1.2,
            "Group": 1.8,
            "Mentored": 2.7,
        }[study_style]
        support_sessions = min(
            8,
            sum(1 for _ in range(12) if random.random() < support_lambda / 12),
        )

        final_score = (
            18
            + 0.46 * prior_score
            + 1.25 * study_hours
            + 0.22 * attendance_rate
            + 0.70 * support_sessions
            + track_effect[program_track]
            + style_effect[study_style]
            + random.gauss(0, 8.5)
        )
        final_score = round(clamp(final_score, 35, 100), 1)

        satisfaction_latent = (
            2.6
            + 0.045 * (final_score - 70)
            + 0.035 * (attendance_rate - 75)
            + {"Self-paced": -0.25, "Group": 0.05, "Mentored": 0.30}[study_style]
            + random.gauss(0, 0.75)
        )
        satisfaction_level = int(round(clamp(satisfaction_latent, 1, 5)))

        # Completion is probabilistic, not deterministic.
        logit = (
            -7.0
            + 0.055 * final_score
            + 0.035 * attendance_rate
            + 0.055 * study_hours
            + 0.10 * support_sessions
        )
        p_completed = 1 / (1 + math.exp(-logit))
        completed = int(random.random() < p_completed)

        rows.append({
            "participant_id": f"P{i:03d}",
            "program_track": program_track,
            "study_style": study_style,
            "prior_score": round(prior_score, 1),
            "study_hours_weekly": round(study_hours, 1),
            "attendance_rate": round(attendance_rate, 1),
            "support_sessions": support_sessions,
            "satisfaction_level": satisfaction_level,
            "final_score": final_score,
            "completed": completed,
        })
    return rows

def find_project_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "data").exists():
            return candidate
    # Fallback for direct execution before the repository folders exist.
    return Path(__file__).resolve().parents[2]

def main():
    root = find_project_root(Path.cwd())
    output = root / "data" / "23_comprehensive_statistical_analysis.csv"
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
