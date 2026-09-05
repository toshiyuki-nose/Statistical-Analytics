"""Generate the synthetic population for Chapter 10."""
from pathlib import Path
import numpy as np
import pandas as pd

def find_project_root():
    cwd=Path.cwd().resolve()
    for p in [cwd,*cwd.parents]:
        if (p/"data").is_dir(): return p
    return Path(__file__).resolve().parents[2]

rng=np.random.default_rng(42)
N=1000
regions=rng.choice(["Region_A","Region_B","Region_C","Region_D"],N,p=[.28,.25,.27,.20])
effects={"Region_A":0,"Region_B":5,"Region_C":-4,"Region_D":8}
spending=np.clip([rng.normal(280+effects[r],55) for r in regions],100,500).round(1)
df=pd.DataFrame({"household_id":[f"Household_{i:04d}" for i in range(1,N+1)],"region":regions,"monthly_spending_usd":spending})
out=find_project_root()/"data"/"10_sampling.csv"
df.to_csv(out,index=False)
print(f"Created: {out}")
