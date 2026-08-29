"""Generate Chapter 09 educational dataset."""
from pathlib import Path
import pandas as pd

def find_project_root():
    cwd=Path.cwd().resolve()
    for p in [cwd,*cwd.parents]:
        if (p/"data").is_dir(): return p
    return Path(__file__).resolve().parents[2]

values=[24.8,28.1,29.4,30.2,31.7,32.5,33.1,34.6,35.0,35.8,36.4,37.2,37.9,38.5,39.1,39.8,40.3,40.9,41.5,42.0,42.6,43.1,43.7,44.2,44.8,45.3,45.9,46.5,47.1,47.8,48.4,49.0,49.7,50.4,51.1,51.8,52.6,53.4,54.3,55.2,56.1,57.0,58.2,59.4,60.7,62.0,63.5,65.1,67.0,70.2]
df=pd.DataFrame({"delivery_id":[f"Delivery_{i:02d}" for i in range(1,51)],"delivery_time_minutes":values})
out=find_project_root()/"data"/"09_continuous_probability_distributions.csv"
df.to_csv(out,index=False)
print(f"Created: {out}")
