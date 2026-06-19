-- Silver table DDL examples.
-- Silver tables are cleaned, typed, deduplicated, and ready for Gold modeling.

CREATE SCHEMA IF NOT EXISTS retail_lakehouse_dev.silver;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.silver.sil_customers
(
    customer_id STRING NOT NULL,
    first_name STRING,
    last_name STRING,
    email STRING,
    phone_digits STRING,
    loyalty_tier STRING,
    customer_segment STRING,
    signup_date DATE,
    status STRING,
    is_active BOOLEAN,
    state STRING,
    country STRING,
    silver_processed_utc TIMESTAMP,
    silver_batch_id STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.silver.sil_orders
(
    order_id STRING NOT NULL,
    customer_id STRING NOT NULL,
    order_date DATE,
    order_status STRING,
    channel STRING,
    store_id STRING,
    order_total DECIMAL(12,2),
    currency STRING,
    is_completed BOOLEAN,
    silver_processed_utc TIMESTAMP,
    silver_batch_id STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.silver.sil_order_items
(
    order_item_id STRING NOT NULL,
    order_id STRING NOT NULL,
    product_id STRING NOT NULL,
    quantity INT,
    unit_price DECIMAL(10,2),
    discount_amount DECIMAL(10,2),
    line_total DECIMAL(12,2),
    calculated_line_total DECIMAL(12,2),
    silver_processed_utc TIMESTAMP,
    silver_batch_id STRING
)
USING DELTA;
