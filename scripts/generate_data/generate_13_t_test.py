"""Generate Chapter 13 t-test synthetic educational data."""
from pathlib import Path
import numpy as np, pandas as pd
def root():
    cwd=Path.cwd().resolve()
    for p in [cwd,*cwd.parents]:
        if (p/"data").is_dir(): return p
    return Path(__file__).resolve().parents[2]
rng=np.random.default_rng(42)
one=np.clip(rng.normal(32,5.8,40),15,50).round(1)
a=np.clip(rng.normal(72,8,35),40,100).round(1)
b=np.clip(rng.normal(77,8,38),40,100).round(1)
before=np.clip(rng.normal(65,9,30),35,95)
after=np.clip(before+rng.normal(5,4,30),35,100)
rows=[]
for i,v in enumerate(one,1): rows.append(["one_sample",f"OS_{i:03d}","Current_Process",np.nan,np.nan,v])
for i,v in enumerate(a,1): rows.append(["independent",f"IA_{i:03d}","Method_A",np.nan,np.nan,v])
for i,v in enumerate(b,1): rows.append(["independent",f"IB_{i:03d}","Method_B",np.nan,np.nan,v])
for i,(x,y) in enumerate(zip(before,after),1): rows.append(["paired",f"P_{i:03d}","Same_Participants",round(x,1),round(y,1),np.nan])
df=pd.DataFrame(rows,columns=["analysis_type","record_id","group","before_score","after_score","value"])
out=root()/"data"/"13_t_test.csv"; df.to_csv(out,index=False); print(f"Created: {out}")
