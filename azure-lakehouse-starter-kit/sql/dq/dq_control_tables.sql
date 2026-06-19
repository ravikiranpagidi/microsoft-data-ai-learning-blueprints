CREATE SCHEMA IF NOT EXISTS retail_lakehouse_dev.dq;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.dq.dq_rules
(
    rule_id STRING,
    layer_name STRING,
    table_name STRING,
    rule_name STRING,
    rule_type STRING,
    column_name STRING,
    expected_value STRING,
    severity STRING,
    is_active BOOLEAN
)
USING DELTA;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.dq.dq_results
(
    run_id STRING,
    layer STRING,
    table_name STRING,
    rule_name STRING,
    rule_type STRING,
    status STRING,
    failed_count BIGINT,
    checked_utc TIMESTAMP,
    details STRING
)
USING DELTA;

INSERT INTO retail_lakehouse_dev.dq.dq_rules VALUES
('DQ001', 'silver', 'sil_customers', 'customer_id_not_null', 'not_null', 'customer_id', NULL, 'high', true),
('DQ002', 'silver', 'sil_orders', 'order_id_not_null', 'not_null', 'order_id', NULL, 'high', true),
('DQ003', 'silver', 'sil_order_items', 'order_item_id_unique', 'duplicate', 'order_item_id', NULL, 'high', true),
('DQ004', 'gold', 'fact_sales', 'sales_amount_non_negative', 'range', 'sales_amount', '>=0', 'high', true);
