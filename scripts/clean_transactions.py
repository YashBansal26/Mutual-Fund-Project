import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction type
mapping = {
    "sip": "SIP",
    "systematic investment plan": "SIP",
    "lumpsum": "Lumpsum",
    "lump sum": "Lumpsum",
    "redemption": "Redemption",
    "redeem": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .str.lower()
    .str.strip()
    .replace(mapping)
)

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC validation
valid_kyc = ["Verified", "Pending", "Rejected"]

df = df[df["kyc_status"].isin(valid_kyc)]

df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)