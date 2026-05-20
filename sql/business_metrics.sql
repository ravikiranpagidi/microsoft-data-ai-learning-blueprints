-- Business metrics for Retail Banking Customer Analytics.

SELECT COUNT(DISTINCT customer_key) AS active_customer_count
FROM dbo.vw_dim_customer
WHERE is_active_customer = 1;

SELECT p.product_category, p.product_name, COUNT(DISTINCT f.transaction_id) AS transaction_count, SUM(f.absolute_transaction_amount) AS total_transaction_amount
FROM dbo.vw_fact_transaction f
JOIN dbo.vw_dim_product p ON f.product_key = p.product_key
WHERE f.is_posted = 1
GROUP BY p.product_category, p.product_name
ORDER BY transaction_count DESC;

SELECT d.year_month, COUNT(DISTINCT f.transaction_id) AS transaction_count, SUM(f.absolute_transaction_amount) AS total_transaction_amount, AVG(f.absolute_transaction_amount) AS average_transaction_amount
FROM dbo.vw_fact_transaction f
JOIN dbo.dim_date d ON f.date_key = d.date_key
WHERE f.is_posted = 1
GROUP BY d.year_month
ORDER BY d.year_month;

SELECT b.region, b.branch_name, COUNT(DISTINCT f.transaction_id) AS transaction_count, SUM(f.absolute_transaction_amount) AS total_transaction_amount
FROM dbo.vw_fact_transaction f
JOIN dbo.vw_dim_branch b ON f.branch_key = b.branch_key
WHERE f.is_posted = 1
GROUP BY b.region, b.branch_name
ORDER BY total_transaction_amount DESC;

SELECT c.customer_segment, COUNT(DISTINCT c.customer_key) AS customer_count, COUNT(DISTINCT f.transaction_id) AS transaction_count, SUM(f.absolute_transaction_amount) AS total_transaction_amount
FROM dbo.vw_dim_customer c
LEFT JOIN dbo.vw_fact_transaction f ON c.customer_key = f.customer_key AND f.is_posted = 1
GROUP BY c.customer_segment
ORDER BY customer_count DESC;
