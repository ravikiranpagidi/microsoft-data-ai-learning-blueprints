CREATE OR REPLACE VIEW retail_lakehouse_dev.gold.vw_daily_sales AS
SELECT
    order_date,
    channel,
    store_id,
    COUNT(DISTINCT order_id) AS order_count,
    COUNT(*) AS sales_line_count,
    SUM(quantity) AS units_sold,
    SUM(sales_amount) AS total_sales_amount,
    AVG(sales_amount) AS average_line_sales_amount
FROM retail_lakehouse_dev.gold.fact_sales
WHERE is_completed = true
GROUP BY
    order_date,
    channel,
    store_id;
