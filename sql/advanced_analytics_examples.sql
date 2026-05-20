-- Advanced analytics examples for Retail Banking Customer Analytics.
-- Run these after Gold tables and standard views are available.

-- 1. Top customers by transaction activity.
SELECT TOP (10)
    c.customer_id,
    c.customer_full_name,
    c.customer_segment,
    COUNT(DISTINCT f.transaction_id) AS transaction_count,
    SUM(f.absolute_transaction_amount) AS total_transaction_amount,
    AVG(f.absolute_transaction_amount) AS average_transaction_amount
FROM dbo.fact_transaction f
JOIN dbo.dim_customer c ON f.customer_key = c.customer_key
WHERE f.is_posted = 1
GROUP BY c.customer_id, c.customer_full_name, c.customer_segment
ORDER BY total_transaction_amount DESC;

-- 2. Product penetration by customer segment.
SELECT
    c.customer_segment,
    p.product_category,
    COUNT(DISTINCT c.customer_key) AS customers_using_product_category,
    COUNT(DISTINCT f.transaction_id) AS transaction_count,
    SUM(f.absolute_transaction_amount) AS total_transaction_amount
FROM dbo.fact_transaction f
JOIN dbo.dim_customer c ON f.customer_key = c.customer_key
JOIN dbo.dim_product p ON f.product_key = p.product_key
WHERE f.is_posted = 1
GROUP BY c.customer_segment, p.product_category
ORDER BY c.customer_segment, total_transaction_amount DESC;

-- 3. Branch activity ranking by month.
WITH branch_month AS (
    SELECT
        d.year_month,
        b.region,
        b.branch_name,
        COUNT(DISTINCT f.transaction_id) AS transaction_count,
        SUM(f.absolute_transaction_amount) AS total_transaction_amount
    FROM dbo.fact_transaction f
    JOIN dbo.dim_date d ON f.date_key = d.date_key
    JOIN dbo.dim_branch b ON f.branch_key = b.branch_key
    WHERE f.is_posted = 1
    GROUP BY d.year_month, b.region, b.branch_name
)
SELECT
    year_month,
    region,
    branch_name,
    transaction_count,
    total_transaction_amount,
    DENSE_RANK() OVER (PARTITION BY year_month ORDER BY total_transaction_amount DESC) AS branch_rank_in_month
FROM branch_month
ORDER BY year_month, branch_rank_in_month;

-- 4. Accounts that may need deeper analysis.
-- This is not fraud detection. It is a simple analytical triage query for unusual activity review.
SELECT
    a.account_id,
    a.account_type,
    c.customer_full_name,
    c.customer_segment,
    COUNT(DISTINCT f.transaction_id) AS transaction_count,
    SUM(f.absolute_transaction_amount) AS total_transaction_amount,
    MAX(f.absolute_transaction_amount) AS largest_transaction_amount
FROM dbo.fact_transaction f
JOIN dbo.dim_account a ON f.account_key = a.account_key
JOIN dbo.dim_customer c ON f.customer_key = c.customer_key
WHERE f.is_posted = 1
GROUP BY a.account_id, a.account_type, c.customer_full_name, c.customer_segment
HAVING COUNT(DISTINCT f.transaction_id) >= 2
   OR MAX(f.absolute_transaction_amount) >= 10000
ORDER BY largest_transaction_amount DESC;

-- 5. Month-over-month transaction trend.
WITH monthly AS (
    SELECT
        d.year_month,
        SUM(f.absolute_transaction_amount) AS total_transaction_amount
    FROM dbo.fact_transaction f
    JOIN dbo.dim_date d ON f.date_key = d.date_key
    WHERE f.is_posted = 1
    GROUP BY d.year_month
)
SELECT
    year_month,
    total_transaction_amount,
    LAG(total_transaction_amount) OVER (ORDER BY year_month) AS previous_month_transaction_amount,
    total_transaction_amount - LAG(total_transaction_amount) OVER (ORDER BY year_month) AS month_over_month_change
FROM monthly
ORDER BY year_month;
