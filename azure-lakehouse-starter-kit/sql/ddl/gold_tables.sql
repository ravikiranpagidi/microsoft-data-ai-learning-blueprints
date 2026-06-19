-- Gold table DDL examples for the Retail Customer Analytics dimensional model.

CREATE SCHEMA IF NOT EXISTS retail_lakehouse_dev.gold;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.gold.dim_customer
(
    customer_key BIGINT NOT NULL,
    customer_id STRING NOT NULL,
    first_name STRING,
    last_name STRING,
    customer_name STRING,
    email STRING,
    phone_digits STRING,
    loyalty_tier STRING,
    customer_segment STRING,
    signup_date DATE,
    status STRING,
    is_active BOOLEAN,
    state STRING,
    country STRING,
    gold_processed_utc TIMESTAMP
)
USING DELTA;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.gold.dim_product
(
    product_key BIGINT NOT NULL,
    product_id STRING NOT NULL,
    product_name STRING,
    category STRING,
    sub_category STRING,
    brand STRING,
    unit_price DECIMAL(10,2),
    is_active BOOLEAN,
    effective_date DATE,
    gold_processed_utc TIMESTAMP
)
USING DELTA;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.gold.fact_sales
(
    sales_line_id STRING NOT NULL,
    order_id STRING NOT NULL,
    customer_key BIGINT,
    product_key BIGINT,
    customer_id STRING,
    product_id STRING,
    order_date DATE,
    channel STRING,
    store_id STRING,
    order_status STRING,
    payment_method STRING,
    payment_status STRING,
    is_completed BOOLEAN,
    is_captured BOOLEAN,
    quantity INT,
    unit_price DECIMAL(10,2),
    discount_amount DECIMAL(10,2),
    line_total DECIMAL(12,2),
    order_total DECIMAL(12,2),
    sales_amount DECIMAL(12,2),
    order_year_month STRING,
    gold_processed_utc TIMESTAMP
)
USING DELTA;
