# People Analytics Dashboard

A production-ready demo showing how to integrate **HRIS**, **recruiting**, and **performance** data, engineer features, and train an **attrition risk** model with **Python**, **SQL**, and export dashboard-ready CSVs for **Tableau/Power BI**.

## Problem
Leaders need a unified view of **headcount**, **attrition**, and **engagement** with the ability to slice by org, role, location, and tenure—and to proactively flag **high-risk** populations.

## Solution
- Consolidate HRIS + Recruiting + Engagement data
- Engineer features (tenure, performance, comp deltas, manager tenure, prior transfers)
- Train ML model (baseline **Logistic Regression**, optional **Random Forest**) to predict risk
- Export aggregated, **dashboard-ready** tables (dept/role/location splits, trends, funnels)

## Tech Stack
- **Python** (pandas, scikit-learn), **SQL** (PostgreSQL/BigQuery flavor), **Tableau / Power BI**
- Project layout: `data/`, `scripts/`, `sql/`, `dashboards/`, `notebooks/`

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r scripts/requirements.txt
python scripts/etl.py
python scripts/model.py
python scripts/dashboard_prep.py
```
Dashboard-ready CSVs are written to `data/derived/`.

## Outputs (example)
- `data/derived/attrition_by_department.csv`
- `data/derived/recruiting_funnel.csv`
- `models/model.pkl` and `models/metrics.json`

## Notes
- Sample data are **synthetic** and safe to share.
- Replace with real connectors/queries in `sql/` and `scripts/etl.py`.
