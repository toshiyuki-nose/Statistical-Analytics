"""Generate Chapter 14: Chi-Square Test synthetic educational data."""
from pathlib import Path
import numpy as np
import pandas as pd

def find_project_root() -> Path:
    cwd=Path.cwd().resolve()
    for p in [cwd,*cwd.parents]:
        if (p/"data").is_dir():
            return p
    return Path(__file__).resolve().parents[2]

rng=np.random.default_rng(42)
n=300
plans=rng.choice(["Basic","Standard","Premium"],n,p=[.38,.37,.25])
levels=["Low","Medium","High"]
probs={
    "Basic":[.40,.38,.22],
    "Standard":[.25,.45,.30],
    "Premium":[.15,.35,.50],
}
satisfaction=[rng.choice(levels,p=probs[p]) for p in plans]
channels=rng.choice(["Web","Store","Phone"],n,p=[.50,.30,.20])

df=pd.DataFrame({
    "customer_id":[f"Customer_{i:03d}" for i in range(1,n+1)],
    "plan":plans,
    "satisfaction":satisfaction,
    "signup_channel":channels,
})

out=find_project_root()/"data"/"14_chi_square_test.csv"
df.to_csv(out,index=False)
print(f"Created: {out}")
