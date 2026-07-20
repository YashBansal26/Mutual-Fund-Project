import pandas as pd
df=pd.read_csv(
"data/processed/scheme_performance_cleaned.csv"
)
risk=input(
"Risk (Low/Moderate/High): "
)
result=(
df[df["risk_grade"]==risk]
.sort_values(
"sharpe_ratio",
ascending=False
)
.head(3)
)
print(result[
[
"scheme_name",
"sharpe_ratio",
"return_3yr_pct",
"expense_ratio_pct"
]
])