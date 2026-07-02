import pandas as pd

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Parse date
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Extract year
df["year"] = df["date"].dt.year

# Map aum_crore to aum_cr
df["aum_cr"] = df["aum_crore"]

# Drop duplicates
df = df.drop_duplicates()

# Sort
df = df.sort_values(["fund_house", "date"])

df.to_csv(
    "data/processed/aum_history.csv",
    index=False
)

print("AUM data cleaned and saved to data/processed/aum_history.csv")
print(df.info())
