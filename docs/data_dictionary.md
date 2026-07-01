# Data Dictionary

## nav_history

| Column | Type | Description | Source |
|---------|------|-------------|---------|
| amfi_code | INTEGER | Unique fund identifier | AMFI |
| date | DATE | NAV date | NAV History |
| nav | FLOAT | Net Asset Value | NAV History |

## investor_transactions

| Column | Type | Description | Source |
|---------|------|-------------|---------|
| transaction_id | INTEGER | Unique transaction id | Transactions |
| amount | FLOAT | Investment amount | Transactions |
| transaction_type | TEXT | SIP/Lumpsum/Redemption | Transactions |
| state | TEXT | Investor state | Transactions |