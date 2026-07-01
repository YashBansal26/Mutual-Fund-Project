import pandas as pd

master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Fund Master columns:")
print(master.columns)

print("\nNAV History columns:")
print(nav.columns)