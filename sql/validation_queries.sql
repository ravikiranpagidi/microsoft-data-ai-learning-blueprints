-- Validation queries for Gold tables and views.

SELECT 'dim_customer' AS table_name, COUNT(*) AS row_count FROM dbo.dim_customer
UNION ALL SELECT 'dim_account', COUNT(*) FROM dbo.dim_account
UNION ALL SELECT 'dim_product', COUNT(*) FROM dbo.dim_product
UNION ALL SELECT 'dim_branch', COUNT(*) FROM dbo.dim_branch
UNION ALL SELECT 'dim_date', COUNT(*) FROM dbo.dim_date
UNION ALL SELECT 'fact_transaction', COUNT(*) FROM dbo.fact_transaction;

SELECT
    SUM(CASE WHEN customer_key IS NULL THEN 1 ELSE 0 END) AS missing_customer_key,
    SUM(CASE WHEN account_key IS NULL THEN 1 ELSE 0 END) AS missing_account_key,
    SUM(CASE WHEN product_key IS NULL THEN 1 ELSE 0 END) AS missing_product_key,
    SUM(CASE WHEN branch_key IS NULL THEN 1 ELSE 0 END) AS missing_branch_key,
    SUM(CASE WHEN date_key IS NULL THEN 1 ELSE 0 END) AS missing_date_key
FROM dbo.fact_transaction;

SELECT transaction_id, COUNT(*) AS duplicate_count
FROM dbo.fact_transaction
GROUP BY transaction_id
HAVING COUNT(*) > 1;

SELECT transaction_status, COUNT(*) AS row_count
FROM dbo.fact_transaction
GROUP BY transaction_status
ORDER BY row_count DESC;

SELECT a.account_id, a.customer_id
FROM dbo.dim_account a
LEFT JOIN dbo.dim_customer c ON a.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
