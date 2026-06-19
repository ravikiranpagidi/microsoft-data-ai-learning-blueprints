CREATE OR REPLACE VIEW retail_lakehouse_dev.gold.vw_customer_360 AS
SELECT
    customer_id,
    customer_name,
    loyalty_tier,
    customer_segment,
    state,
    country,
    is_active,
    COALESCE(order_count, 0) AS order_count,
    COALESCE(units_sold, 0) AS units_sold,
    COALESCE(total_sales_amount, 0) AS total_sales_amount,
    COALESCE(avg_line_sales_amount, 0) AS avg_line_sales_amount,
    last_order_date,
    COALESCE(web_event_count, 0) AS web_event_count,
    COALESCE(web_session_count, 0) AS web_session_count,
    last_web_event_timestamp
FROM retail_lakehouse_dev.gold.customer_360;
