import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
DER = Path("data/derived")
DER.mkdir(parents=True, exist_ok=True)

hris = pd.read_csv(RAW / "hris.csv", parse_dates=["hire_date"])
eng = pd.read_csv(RAW / "engagement.csv")
rec = pd.read_csv(RAW / "recruiting.csv")
# terminations optional
try:
    term = pd.read_csv(RAW / "terminations.csv", parse_dates=["termination_date"])
except FileNotFoundError:
    term = None

df = hris.merge(eng, on="employee_id", how="left").merge(rec, on="employee_id", how="left")
if term is not None:
    df = df.merge(term[["employee_id","termination_date"]], on="employee_id", how="left")

# Simple feature engineering
df["low_perf_flag"] = (df["performance_rating"] <= 2).astype(int)
df["short_tenure_flag"] = (df["tenure_years"] < 1).astype(int)

df.to_csv(DER / "processed.csv", index=False)
print("Wrote", DER / "processed.csv")
