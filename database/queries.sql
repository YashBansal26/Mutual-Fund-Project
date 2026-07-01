-- 1
SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- 2
SELECT
strftime('%Y-%m', full_date),
AVG(nav)
FROM fact_nav
JOIN dim_date
ON fact_nav.date_key = dim_date.date_key
GROUP BY 1;

-- 3
SELECT
year,
SUM(amount)
FROM fact_transactions
JOIN dim_date
ON fact_transactions.date_key = dim_date.date_key
WHERE transaction_type='SIP'
GROUP BY year;

-- 4
SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 5
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- 6
SELECT
fund_key,
AVG(return_1y)
FROM fact_performance
GROUP BY fund_key;

-- 7
SELECT
transaction_type,
SUM(amount)
FROM fact_transactions
GROUP BY transaction_type;

-- 8
SELECT
year,
AVG(aum)
FROM fact_aum
JOIN dim_date
ON fact_aum.date_key = dim_date.date_key
GROUP BY year;

-- 9
SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 10;

-- 10
SELECT
fund_key,
COUNT(*)
FROM fact_transactions
GROUP BY fund_key
ORDER BY COUNT(*) DESC;