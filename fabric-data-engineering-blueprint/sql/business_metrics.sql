/*
    Business metrics for Retail Banking Customer Analytics.

    These queries answer the primary business questions from the blueprint.
    Account balances and transaction amounts are aggregated separately before
    being combined so totals are not duplicated by one-to-many joins.
*/

-- 1. Active customer count
SELECT
    COUNT(DISTINCT customer_key) AS active_customer_count
FROM dbo.vw_dim_customer
WHERE is_active_customer = 1;

-- 2. Customer count by segment and status
SELECT
    customer_segment,
    customer_status,
    COUNT(DISTINCT customer_key) AS customer_count
FROM dbo.vw_dim_customer
GROUP BY customer_segment, customer_status
ORDER BY customer_count DESC;

-- 3. Product usage by account count and transaction count
WITH product_accounts AS (
    SELECT
        product_id,
        COUNT(DISTINCT account_key) AS account_count
    FROM dbo.vw_dim_account
    GROUP BY product_id
),
product_transactions AS (
    SELECT
        product_key,
        COUNT(DISTINCT transaction_id) AS transaction_count,
        SUM(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount,
        AVG(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE NULL END) AS average_posted_transaction_amount
    FROM dbo.vw_fact_transaction
    GROUP BY product_key
)
SELECT
    p.product_category,
    p.product_family,
    p.product_name,
    COALESCE(a.account_count, 0) AS account_count,
    COALESCE(t.transaction_count, 0) AS transaction_count,
    COALESCE(t.posted_transaction_amount, 0) AS posted_transaction_amount,
    t.average_posted_transaction_amount
FROM dbo.vw_dim_product p
LEFT JOIN product_accounts a
    ON p.product_id = a.product_id
LEFT JOIN product_transactions t
    ON p.product_key = t.product_key
ORDER BY transaction_count DESC, posted_transaction_amount DESC;

-- 4. Transaction volume by month
SELECT
    d.year_month,
    COUNT(DISTINCT f.transaction_id) AS transaction_count,
    SUM(CASE WHEN f.is_posted = 1 THEN f.absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount,
    SUM(CASE WHEN f.transaction_amount > 0 AND f.is_posted = 1 THEN f.transaction_amount ELSE 0 END) AS credit_amount,
    SUM(CASE WHEN f.transaction_amount < 0 AND f.is_posted = 1 THEN ABS(f.transaction_amount) ELSE 0 END) AS debit_amount,
    AVG(CASE WHEN f.is_posted = 1 THEN f.absolute_transaction_amount ELSE NULL END) AS average_transaction_amount
FROM dbo.vw_fact_transaction f
INNER JOIN dbo.vw_dim_date d
    ON f.date_key = d.date_key
GROUP BY d.year_month
ORDER BY d.year_month;

-- 5. Branches with high transaction activity
WITH branch_accounts AS (
    SELECT
        branch_id,
        COUNT(DISTINCT account_key) AS account_count
    FROM dbo.vw_dim_account
    GROUP BY branch_id
),
branch_transactions AS (
    SELECT
        branch_key,
        COUNT(DISTINCT transaction_id) AS transaction_count,
        SUM(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount,
        AVG(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE NULL END) AS average_transaction_amount
    FROM dbo.vw_fact_transaction
    GROUP BY branch_key
)
SELECT
    b.region,
    b.branch_name,
    COALESCE(a.account_count, 0) AS account_count,
    COALESCE(t.transaction_count, 0) AS transaction_count,
    COALESCE(t.posted_transaction_amount, 0) AS posted_transaction_amount,
    t.average_transaction_amount
FROM dbo.vw_dim_branch b
LEFT JOIN branch_accounts a
    ON b.branch_id = a.branch_id
LEFT JOIN branch_transactions t
    ON b.branch_key = t.branch_key
ORDER BY posted_transaction_amount DESC, transaction_count DESC;

-- 6. Top customer segments by balances and posted transaction value
WITH customer_accounts AS (
    SELECT
        customer_id,
        COUNT(DISTINCT account_key) AS account_count,
        SUM(current_balance) AS total_current_balance
    FROM dbo.vw_dim_account
    GROUP BY customer_id
),
customer_transactions AS (
    SELECT
        customer_key,
        COUNT(DISTINCT transaction_id) AS transaction_count,
        SUM(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount
    FROM dbo.vw_fact_transaction
    GROUP BY customer_key
),
customer_360 AS (
    SELECT
        c.customer_key,
        c.customer_segment,
        COALESCE(a.account_count, 0) AS account_count,
        COALESCE(a.total_current_balance, 0) AS total_current_balance,
        COALESCE(t.transaction_count, 0) AS transaction_count,
        COALESCE(t.posted_transaction_amount, 0) AS posted_transaction_amount
    FROM dbo.vw_dim_customer c
    LEFT JOIN customer_accounts a
        ON c.customer_id = a.customer_id
    LEFT JOIN customer_transactions t
        ON c.customer_key = t.customer_key
)
SELECT
    customer_segment,
    COUNT(DISTINCT customer_key) AS customer_count,
    SUM(account_count) AS account_count,
    SUM(total_current_balance) AS total_current_balance,
    SUM(transaction_count) AS transaction_count,
    SUM(posted_transaction_amount) AS posted_transaction_amount
FROM customer_360
GROUP BY customer_segment
ORDER BY posted_transaction_amount DESC, total_current_balance DESC;

-- 7. Monthly balance and transaction trend
WITH monthly_transactions AS (
    SELECT
        d.year_month,
        COUNT(DISTINCT f.customer_key) AS active_transacting_customer_count,
        COUNT(DISTINCT f.account_key) AS transacting_account_count,
        COUNT(DISTINCT f.transaction_id) AS transaction_count,
        SUM(CASE WHEN f.is_posted = 1 THEN f.absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount
    FROM dbo.vw_fact_transaction f
    INNER JOIN dbo.vw_dim_date d
        ON f.date_key = d.date_key
    GROUP BY d.year_month
),
total_balance AS (
    SELECT SUM(current_balance) AS current_balance_snapshot
    FROM dbo.vw_dim_account
)
SELECT
    m.year_month,
    m.active_transacting_customer_count,
    m.transacting_account_count,
    m.transaction_count,
    m.posted_transaction_amount,
    b.current_balance_snapshot
FROM monthly_transactions m
CROSS JOIN total_balance b
ORDER BY m.year_month;

-- 8. Customers needing deeper analysis
WITH customer_accounts AS (
    SELECT
        customer_id,
        COUNT(DISTINCT account_key) AS account_count,
        SUM(current_balance) AS total_current_balance
    FROM dbo.vw_dim_account
    GROUP BY customer_id
),
customer_transactions AS (
    SELECT
        customer_key,
        COUNT(DISTINCT transaction_id) AS transaction_count,
        SUM(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount,
        MAX(transaction_timestamp) AS last_transaction_timestamp
    FROM dbo.vw_fact_transaction
    GROUP BY customer_key
)
SELECT TOP 20
    c.customer_id,
    c.customer_full_name,
    c.customer_segment,
    c.customer_status,
    COALESCE(a.account_count, 0) AS account_count,
    COALESCE(a.total_current_balance, 0) AS total_current_balance,
    COALESCE(t.transaction_count, 0) AS transaction_count,
    COALESCE(t.posted_transaction_amount, 0) AS posted_transaction_amount,
    t.last_transaction_timestamp
FROM dbo.vw_dim_customer c
LEFT JOIN customer_accounts a
    ON c.customer_id = a.customer_id
LEFT JOIN customer_transactions t
    ON c.customer_key = t.customer_key
ORDER BY posted_transaction_amount DESC, total_current_balance DESC;

-- 9. Rejected transactions for operational follow-up
SELECT
    f.transaction_id,
    f.transaction_timestamp,
    c.customer_id,
    c.customer_full_name,
    a.account_id,
    p.product_name,
    b.branch_name,
    f.transaction_type,
    f.transaction_channel,
    f.transaction_amount,
    f.transaction_status
FROM dbo.vw_fact_transaction f
INNER JOIN dbo.vw_dim_customer c
    ON f.customer_key = c.customer_key
INNER JOIN dbo.vw_dim_account a
    ON f.account_key = a.account_key
INNER JOIN dbo.vw_dim_product p
    ON f.product_key = p.product_key
INNER JOIN dbo.vw_dim_branch b
    ON f.branch_key = b.branch_key
WHERE f.transaction_status <> 'Posted'
ORDER BY f.transaction_timestamp DESC;
