-- Power BI-ready consumption views.

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
    a.account_id,
    a.account_type,
    a.account_status,
    p.product_name,
    p.product_category,
    p.product_family,
    b.branch_name,
    b.region,
    f.transaction_channel,
    f.transaction_type,
    f.transaction_status,
    f.currency,
    f.transaction_amount,
    f.absolute_transaction_amount,
    f.is_posted
FROM dbo.fact_transaction f
JOIN dbo.dim_date d ON f.date_key = d.date_key
JOIN dbo.dim_customer c ON f.customer_key = c.customer_key
JOIN dbo.dim_account a ON f.account_key = a.account_key
JOIN dbo.dim_product p ON f.product_key = p.product_key
JOIN dbo.dim_branch b ON f.branch_key = b.branch_key;
GO

CREATE OR ALTER VIEW dbo.vw_powerbi_monthly_transaction_summary AS
SELECT d.year_month, p.product_category, b.region, COUNT(DISTINCT f.transaction_id) AS transaction_count, SUM(f.absolute_transaction_amount) AS total_transaction_amount, AVG(f.absolute_transaction_amount) AS average_transaction_amount
FROM dbo.fact_transaction f
JOIN dbo.dim_date d ON f.date_key = d.date_key
JOIN dbo.dim_product p ON f.product_key = p.product_key
JOIN dbo.dim_branch b ON f.branch_key = b.branch_key
WHERE f.is_posted = 1
GROUP BY d.year_month, p.product_category, b.region;
GO

CREATE OR ALTER VIEW dbo.vw_powerbi_customer_account_summary AS
SELECT c.customer_id, c.customer_full_name, c.customer_segment, c.customer_status, c.city, c.state, COUNT(DISTINCT a.account_id) AS account_count, SUM(a.current_balance) AS total_current_balance
FROM dbo.dim_customer c
LEFT JOIN dbo.dim_account a ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.customer_full_name, c.customer_segment, c.customer_status, c.city, c.state;
GO
