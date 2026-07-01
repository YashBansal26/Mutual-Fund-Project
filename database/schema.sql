CREATE TABLE dim_fund (
    fund_key INTEGER PRIMARY KEY,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    fund_key INTEGER,
    date_key INTEGER,
    nav REAL,
    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key),
    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    fund_key INTEGER,
    date_key INTEGER,
    amount REAL,
    transaction_type TEXT,
    state TEXT,
    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key),
    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    fund_key INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL,
    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    fund_key INTEGER,
    date_key INTEGER,
    aum REAL,
    FOREIGN KEY (fund_key)
        REFERENCES dim_fund(fund_key),
    FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key)
);