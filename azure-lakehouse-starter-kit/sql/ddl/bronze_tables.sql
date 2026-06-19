-- Bronze table DDL examples for Azure Databricks SQL.
-- In practice, Bronze tables are often created by PySpark writes with mergeSchema enabled.

CREATE SCHEMA IF NOT EXISTS retail_lakehouse_dev.bronze;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.bronze.brz_customers
(
    customer_id STRING,
    first_name STRING,
    last_name STRING,
    email STRING,
    phone STRING,
    loyalty_tier STRING,
    customer_segment STRING,
    signup_date STRING,
    status STRING,
    state STRING,
    country STRING,
    _ingestion_utc TIMESTAMP,
    _source_file_name STRING,
    _batch_id STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS retail_lakehouse_dev.bronze.brz_orders
(
    order_id STRING,
    customer_id STRING,
    order_date STRING,
    order_status STRING,
    channel STRING,
    store_id STRING,
    order_total STRING,
    currency STRING,
    _ingestion_utc TIMESTAMP,
    _source_file_name STRING,
    _batch_id STRING
)
USING DELTA;
