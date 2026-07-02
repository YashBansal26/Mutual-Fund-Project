import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///database/bluestock_mf.db"
)

files = {
    "nav_history":
        "data/processed/nav_history_cleaned.csv",
    "transactions":
        "data/processed/investor_transactions_cleaned.csv",
    "performance":
        "data/processed/scheme_performance_cleaned.csv",
    "aum_history":
        "data/processed/aum_history.csv"
}

for table, file in files.items():
    df = pd.read_csv(file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        engine
    )

    print(table, count.iloc[0]["cnt"])