import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Flag anomalies
for col in return_cols:
    anomalies = df[
        (df[col] > 100) |
        (df[col] < -100)
    ]
    print(f"{col}: {len(anomalies)} anomalies")

# Expense ratio validation
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)