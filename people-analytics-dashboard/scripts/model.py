import json
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score
import joblib

DER = Path("data/derived")
MODELS = Path("models")
MODELS.mkdir(exist_ok=True, parents=True)

df = pd.read_csv(DER / "processed.csv")
y = df["attrition"]
X = df.drop(columns=["attrition"])

cat_cols = ["department","location","source"]
num_cols = ["tenure_years","performance_rating","salary","manager_tenure","eNPS","pulse_score","time_to_fill_days","diversity_flag","low_perf_flag","short_tenure_flag"]

ct = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ("num", "passthrough", num_cols)
])

pipe = Pipeline([
    ("prep", ct),
    ("clf", LogisticRegression(max_iter=1000))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
pipe.fit(X_train, y_train)

proba = pipe.predict_proba(X_test)[:,1]
pred = (proba > 0.5).astype(int)
metrics = {
    "roc_auc": float(roc_auc_score(y_test, proba)),
    "accuracy": float(accuracy_score(y_test, pred)),
    "n_test": int(len(y_test))
}
with open(MODELS / "metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)
joblib.dump(pipe, MODELS / "model.pkl")

print("Saved model and metrics:", metrics)
