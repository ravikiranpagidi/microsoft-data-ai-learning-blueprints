/*
    Power BI consumption views for Retail Banking Customer Analytics.

    Recommended use:
    - Use the Gold star schema tables directly for governed semantic models.
    - Use these views for quick exploration, beginner demos, validation, and
      business-friendly reporting shapes.

    Modeling note:
    Summary views aggregate accounts and transactions separately before joining.
    This avoids accidental balance duplication when one customer, branch, or
    product has multiple accounts and multiple transactions.
*/

CREATE OR ALTER VIEW dbo.vw_powerbi_transaction_detail AS
SELECT
    f.transaction_id,
    d.date_value AS transaction_date,
    d.year,
    d.quarter,
    d.month,
    d.month_name,
    d.year_month,
    c.customer_id,
    c.customer_full_name,
    c.customer_segment,
    c.customer_status,
    c.city AS customer_city,
    c.state AS customer_state,
    a.account_id,
    a.account_type,
    a.account_status,
    a.current_balance,
    p.product_id,
    p.product_name,
    p.product_category,
    p.product_family,
    b.branch_id,
    b.branch_name,
    b.region,
    f.transaction_channel,
    f.transaction_type,
    f.transaction_status,
    f.currency,
    f.transaction_amount,
    f.absolute_transaction_amount,
    f.debit_credit_indicator,
    f.is_posted
FROM dbo.vw_fact_transaction f
INNER JOIN dbo.vw_dim_date d
    ON f.date_key = d.date_key
INNER JOIN dbo.vw_dim_customer c
    ON f.customer_key = c.customer_key
INNER JOIN dbo.vw_dim_account a
    ON f.account_key = a.account_key
INNER JOIN dbo.vw_dim_product p
    ON f.product_key = p.product_key
INNER JOIN dbo.vw_dim_branch b
    ON f.branch_key = b.branch_key;
GO

CREATE OR ALTER VIEW dbo.vw_powerbi_monthly_transaction_summary AS
SELECT
    d.year_month,
    d.year,
    d.month,
    p.product_category,
    p.product_family,
    b.region,
    COUNT(DISTINCT f.transaction_id) AS transaction_count,
    SUM(f.absolute_transaction_amount) AS total_transaction_amount,
    AVG(f.absolute_transaction_amount) AS average_transaction_amount,
    SUM(CASE WHEN f.transaction_amount > 0 THEN f.transaction_amount ELSE 0 END) AS total_credit_amount,
    SUM(CASE WHEN f.transaction_amount < 0 THEN ABS(f.transaction_amount) ELSE 0 END) AS total_debit_amount
FROM dbo.vw_fact_transaction f
INNER JOIN dbo.vw_dim_date d
    ON f.date_key = d.date_key
INNER JOIN dbo.vw_dim_product p
    ON f.product_key = p.product_key
INNER JOIN dbo.vw_dim_branch b
    ON f.branch_key = b.branch_key
WHERE f.is_posted = 1
GROUP BY
    d.year_month,
    d.year,
    d.month,
    p.product_category,
    p.product_family,
    b.region;
GO

CREATE OR ALTER VIEW dbo.vw_powerbi_customer_360 AS
WITH account_summary AS (
    SELECT
        customer_id,
        COUNT(DISTINCT account_id) AS account_count,
        SUM(current_balance) AS total_current_balance
    FROM dbo.vw_dim_account
    GROUP BY customer_id
),
transaction_summary AS (
    SELECT
        customer_key,
        COUNT(DISTINCT transaction_id) AS transaction_count,
        SUM(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount,
        MAX(transaction_timestamp) AS last_transaction_timestamp
    FROM dbo.vw_fact_transaction
    GROUP BY customer_key
)
SELECT
    c.customer_key,
    c.customer_id,
    c.customer_full_name,
    c.customer_segment,
    c.customer_status,
    c.city,
    c.state,
    c.customer_age_years,
    c.customer_tenure_years,
    COALESCE(a.account_count, 0) AS account_count,
    COALESCE(a.total_current_balance, 0) AS total_current_balance,
    COALESCE(t.transaction_count, 0) AS transaction_count,
    COALESCE(t.posted_transaction_amount, 0) AS posted_transaction_amount,
    t.last_transaction_timestamp
FROM dbo.vw_dim_customer c
LEFT JOIN account_summary a
    ON c.customer_id = a.customer_id
LEFT JOIN transaction_summary t
    ON c.customer_key = t.customer_key;
GO

CREATE OR ALTER VIEW dbo.vw_powerbi_branch_activity AS
WITH account_summary AS (
    SELECT
        branch_id,
        COUNT(DISTINCT account_id) AS account_count
    FROM dbo.vw_dim_account
    GROUP BY branch_id
),
transaction_summary AS (
    SELECT
        branch_key,
        COUNT(DISTINCT transaction_id) AS transaction_count,
        SUM(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount,
        AVG(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE NULL END) AS average_posted_transaction_amount
    FROM dbo.vw_fact_transaction
    GROUP BY branch_key
)
SELECT
    b.branch_key,
    b.branch_id,
    b.branch_name,
    b.region,
    b.city,
    b.state,
    COALESCE(a.account_count, 0) AS account_count,
    COALESCE(t.transaction_count, 0) AS transaction_count,
    COALESCE(t.posted_transaction_amount, 0) AS posted_transaction_amount,
    t.average_posted_transaction_amount
FROM dbo.vw_dim_branch b
LEFT JOIN account_summary a
    ON b.branch_id = a.branch_id
LEFT JOIN transaction_summary t
    ON b.branch_key = t.branch_key;
GO

CREATE OR ALTER VIEW dbo.vw_powerbi_product_usage AS
WITH account_summary AS (
    SELECT
        product_id,
        COUNT(DISTINCT account_id) AS account_count
    FROM dbo.vw_dim_account
    GROUP BY product_id
),
transaction_summary AS (
    SELECT
        product_key,
        COUNT(DISTINCT transaction_id) AS transaction_count,
        SUM(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount
    FROM dbo.vw_fact_transaction
    GROUP BY product_key
)
SELECT
    p.product_key,
    p.product_id,
    p.product_name,
    p.product_category,
    p.product_family,
    p.fee_model,
    COALESCE(a.account_count, 0) AS account_count,
    COALESCE(t.transaction_count, 0) AS transaction_count,
    COALESCE(t.posted_transaction_amount, 0) AS posted_transaction_amount
FROM dbo.vw_dim_product p
LEFT JOIN account_summary a
    ON p.product_id = a.product_id
LEFT JOIN transaction_summary t
    ON p.product_key = t.product_key;
GO

CREATE OR ALTER VIEW dbo.vw_powerbi_executive_kpis AS
WITH customer_summary AS (
    SELECT
        COUNT(DISTINCT CASE WHEN is_active_customer = 1 THEN customer_key END) AS active_customer_count
    FROM dbo.vw_dim_customer
),
account_summary AS (
    SELECT
        COUNT(DISTINCT account_key) AS account_count,
        SUM(current_balance) AS total_current_balance
    FROM dbo.vw_dim_account
),
transaction_summary AS (
    SELECT
        COUNT(DISTINCT transaction_id) AS transaction_count,
        SUM(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE 0 END) AS posted_transaction_amount,
        AVG(CASE WHEN is_posted = 1 THEN absolute_transaction_amount ELSE NULL END) AS average_posted_transaction_amount
    FROM dbo.vw_fact_transaction
)
SELECT
    c.active_customer_count,
    a.account_count,
    t.transaction_count,
    t.posted_transaction_amount,
    t.average_posted_transaction_amount,
    a.total_current_balance
FROM customer_summary c
CROSS JOIN account_summary a
CROSS JOIN transaction_summary t;
GO
