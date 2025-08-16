import pandas as pd
from pathlib import Path

DER = Path("data/derived")
DER.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DER / "processed.csv")

# Attrition by department
attr_by_dept = df.groupby("department").agg(
    headcount=("employee_id","count"),
    attriters=("attrition","sum")
).reset_index()
attr_by_dept["attrition_rate"] = (attr_by_dept["attriters"] / attr_by_dept["headcount"]).round(3)
attr_by_dept.to_csv(DER / "attrition_by_department.csv", index=False)

# Recruiting funnel mock (offers assumed as 20% of headcount here for demo)
funnel = (df
    .groupby(["department","source"])
    .agg(people=("employee_id","count"))
    .reset_index())
funnel["applied"] = (funnel["people"] * 3).astype(int)
funnel["phone_screen"] = (funnel["applied"] * 0.6).astype(int)
funnel["onsite"] = (funnel["phone_screen"] * 0.5).astype(int)
funnel["offer"] = (funnel["onsite"] * 0.4).astype(int)
funnel["hired"] = (funnel["offer"] * 0.7).astype(int)
funnel.to_csv(DER / "recruiting_funnel.csv", index=False)

print("Wrote derived dashboard tables.")
