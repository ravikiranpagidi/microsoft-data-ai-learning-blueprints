/*
    Validation queries for the Retail Banking Customer Analytics blueprint.

    Use these queries after running the notebooks to confirm that each layer is
    complete, reconciled, and ready for consumption.
*/

-- 1. Row counts by layer
SELECT 'bronze_customers' AS object_name, COUNT(*) AS row_count FROM dbo.bronze_customers
UNION ALL SELECT 'bronze_accounts', COUNT(*) FROM dbo.bronze_accounts
UNION ALL SELECT 'bronze_products', COUNT(*) FROM dbo.bronze_products
UNION ALL SELECT 'bronze_branches', COUNT(*) FROM dbo.bronze_branches
UNION ALL SELECT 'bronze_transactions', COUNT(*) FROM dbo.bronze_transactions
UNION ALL SELECT 'silver_customers', COUNT(*) FROM dbo.silver_customers
UNION ALL SELECT 'silver_accounts', COUNT(*) FROM dbo.silver_accounts
UNION ALL SELECT 'silver_products', COUNT(*) FROM dbo.silver_products
UNION ALL SELECT 'silver_branches', COUNT(*) FROM dbo.silver_branches
UNION ALL SELECT 'silver_transactions', COUNT(*) FROM dbo.silver_transactions
UNION ALL SELECT 'dim_customer', COUNT(*) FROM dbo.dim_customer
UNION ALL SELECT 'dim_account', COUNT(*) FROM dbo.dim_account
UNION ALL SELECT 'dim_product', COUNT(*) FROM dbo.dim_product
UNION ALL SELECT 'dim_branch', COUNT(*) FROM dbo.dim_branch
UNION ALL SELECT 'dim_date', COUNT(*) FROM dbo.dim_date
UNION ALL SELECT 'fact_transaction', COUNT(*) FROM dbo.fact_transaction;

-- 2. Bronze to Silver row count review
SELECT
    source_layer,
    target_layer,
    entity_name,
    source_row_count,
    target_row_count,
    source_row_count - target_row_count AS row_count_difference
FROM (
    SELECT 'bronze' AS source_layer, 'silver' AS target_layer, 'customers' AS entity_name,
           (SELECT COUNT(*) FROM dbo.bronze_customers) AS source_row_count,
           (SELECT COUNT(*) FROM dbo.silver_customers) AS target_row_count
    UNION ALL
    SELECT 'bronze', 'silver', 'accounts',
           (SELECT COUNT(*) FROM dbo.bronze_accounts),
           (SELECT COUNT(*) FROM dbo.silver_accounts)
    UNION ALL
    SELECT 'bronze', 'silver', 'products',
           (SELECT COUNT(*) FROM dbo.bronze_products),
           (SELECT COUNT(*) FROM dbo.silver_products)
    UNION ALL
    SELECT 'bronze', 'silver', 'branches',
           (SELECT COUNT(*) FROM dbo.bronze_branches),
           (SELECT COUNT(*) FROM dbo.silver_branches)
    UNION ALL
    SELECT 'bronze', 'silver', 'transactions',
           (SELECT COUNT(*) FROM dbo.bronze_transactions),
           (SELECT COUNT(*) FROM dbo.silver_transactions)
) r
ORDER BY entity_name;

-- 3. Silver to Gold transaction reconciliation
SELECT
    (SELECT COUNT(*) FROM dbo.silver_transactions) AS silver_transaction_count,
    (SELECT COUNT(*) FROM dbo.fact_transaction) AS gold_fact_transaction_count,
    (SELECT COUNT(*) FROM dbo.silver_transactions) - (SELECT COUNT(*) FROM dbo.fact_transaction) AS row_count_difference;

-- 4. Duplicate business key checks
SELECT 'silver_customers' AS table_name, customer_id AS business_key, COUNT(*) AS duplicate_count
FROM dbo.silver_customers
GROUP BY customer_id
HAVING COUNT(*) > 1
UNION ALL
SELECT 'silver_accounts', account_id, COUNT(*)
FROM dbo.silver_accounts
GROUP BY account_id
HAVING COUNT(*) > 1
UNION ALL
SELECT 'silver_products', product_id, COUNT(*)
FROM dbo.silver_products
GROUP BY product_id
HAVING COUNT(*) > 1
UNION ALL
SELECT 'silver_branches', branch_id, COUNT(*)
FROM dbo.silver_branches
GROUP BY branch_id
HAVING COUNT(*) > 1
UNION ALL
SELECT 'silver_transactions', transaction_id, COUNT(*)
FROM dbo.silver_transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- 5. Missing dimension keys in the fact table
SELECT
    SUM(CASE WHEN date_key IS NULL THEN 1 ELSE 0 END) AS missing_date_key,
    SUM(CASE WHEN customer_key IS NULL THEN 1 ELSE 0 END) AS missing_customer_key,
    SUM(CASE WHEN account_key IS NULL THEN 1 ELSE 0 END) AS missing_account_key,
    SUM(CASE WHEN product_key IS NULL THEN 1 ELSE 0 END) AS missing_product_key,
    SUM(CASE WHEN branch_key IS NULL THEN 1 ELSE 0 END) AS missing_branch_key
FROM dbo.fact_transaction;

-- 6. Referential integrity review in Silver
SELECT 'silver_accounts.customer_id' AS check_name, COUNT(*) AS missing_parent_count
FROM dbo.silver_accounts a
LEFT JOIN dbo.silver_customers c
    ON a.customer_id = c.customer_id
WHERE c.customer_id IS NULL
UNION ALL
SELECT 'silver_accounts.product_id', COUNT(*)
FROM dbo.silver_accounts a
LEFT JOIN dbo.silver_products p
    ON a.product_id = p.product_id
WHERE p.product_id IS NULL
UNION ALL
SELECT 'silver_accounts.branch_id', COUNT(*)
FROM dbo.silver_accounts a
LEFT JOIN dbo.silver_branches b
    ON a.branch_id = b.branch_id
WHERE b.branch_id IS NULL
UNION ALL
SELECT 'silver_transactions.account_id', COUNT(*)
FROM dbo.silver_transactions t
LEFT JOIN dbo.silver_accounts a
    ON t.account_id = a.account_id
WHERE a.account_id IS NULL;

-- 7. Status distribution checks
SELECT 'customer_status' AS attribute_name, customer_status AS attribute_value, COUNT(*) AS row_count
FROM dbo.silver_customers
GROUP BY customer_status
UNION ALL
SELECT 'account_status', account_status, COUNT(*)
FROM dbo.silver_accounts
GROUP BY account_status
UNION ALL
SELECT 'transaction_status', transaction_status, COUNT(*)
FROM dbo.silver_transactions
GROUP BY transaction_status;

-- 8. Transaction amount sanity check
SELECT
    MIN(transaction_amount) AS minimum_transaction_amount,
    MAX(transaction_amount) AS maximum_transaction_amount,
    AVG(transaction_amount) AS average_signed_transaction_amount,
    AVG(absolute_transaction_amount) AS average_absolute_transaction_amount,
    SUM(CASE WHEN transaction_amount < 0 THEN 1 ELSE 0 END) AS debit_transaction_count,
    SUM(CASE WHEN transaction_amount >= 0 THEN 1 ELSE 0 END) AS credit_transaction_count
FROM dbo.fact_transaction;

-- 9. Data quality result summary, if 04_data_quality_checks.ipynb has been run
SELECT
    severity,
    status,
    COUNT(*) AS rule_result_count,
    SUM(failed_count) AS failed_row_count
FROM dbo.dq_results
GROUP BY severity, status
ORDER BY severity, status;
