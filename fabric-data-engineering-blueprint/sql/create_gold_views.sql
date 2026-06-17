/*
    Gold layer consumption views for Retail Banking Customer Analytics.

    Run this script in the Microsoft Fabric Lakehouse SQL Analytics Endpoint
    after the Gold Delta tables have been created by 03_gold_dimensional_model.ipynb.

    Design goal:
    - Keep base Gold tables clean and dimensional.
    - Expose governed, business-friendly SQL views for analysts and validation.
*/

CREATE OR ALTER VIEW dbo.vw_dim_customer AS
SELECT
    customer_key,
    customer_id,
    customer_full_name,
    first_name,
    last_name,
    email,
    phone,
    city,
    state,
    country,
    customer_segment,
    customer_status,
    is_active_customer,
    customer_age_years,
    customer_tenure_years,
    date_of_birth,
    created_date
FROM dbo.dim_customer;
GO

CREATE OR ALTER VIEW dbo.vw_dim_account AS
SELECT
    account_key,
    account_id,
    customer_id,
    product_id,
    branch_id,
    account_type,
    account_status,
    is_open_account,
    opened_date,
    closed_date,
    current_balance,
    account_age_years
FROM dbo.dim_account;
GO

CREATE OR ALTER VIEW dbo.vw_dim_product AS
SELECT
    product_key,
    product_id,
    product_name,
    product_category,
    product_family,
    fee_model,
    is_active,
    launch_date
FROM dbo.dim_product;
GO

CREATE OR ALTER VIEW dbo.vw_dim_branch AS
SELECT
    branch_key,
    branch_id,
    branch_name,
    city,
    state,
    region,
    opened_date,
    is_active
FROM dbo.dim_branch;
GO

CREATE OR ALTER VIEW dbo.vw_dim_date AS
SELECT
    date_key,
    date_value,
    year,
    quarter,
    month,
    month_name,
    year_month,
    day_of_month,
    day_name,
    week_of_year,
    is_weekend
FROM dbo.dim_date;
GO

CREATE OR ALTER VIEW dbo.vw_fact_transaction AS
SELECT
    transaction_id,
    date_key,
    customer_key,
    account_key,
    product_key,
    branch_key,
    account_id,
    customer_id,
    product_id,
    branch_id,
    transaction_timestamp,
    transaction_date,
    year_month,
    transaction_type,
    transaction_channel,
    transaction_status,
    currency,
    transaction_amount,
    absolute_transaction_amount,
    debit_credit_indicator,
    is_posted,
    transaction_count,
    product_matches_account,
    branch_matches_account,
    _gold_load_timestamp
FROM dbo.fact_transaction;
GO

CREATE OR ALTER VIEW dbo.vw_gold_transaction_star AS
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
    p.product_id,
    p.product_name,
    p.product_category,
    p.product_family,
    b.branch_id,
    b.branch_name,
    b.region,
    f.transaction_channel,
    f.transaction_type,
    f.transaction_status,
    f.currency,
    f.transaction_amount,
    f.absolute_transaction_amount,
    f.debit_credit_indicator,
    f.is_posted
FROM dbo.vw_fact_transaction f
INNER JOIN dbo.vw_dim_date d
    ON f.date_key = d.date_key
INNER JOIN dbo.vw_dim_customer c
    ON f.customer_key = c.customer_key
INNER JOIN dbo.vw_dim_account a
    ON f.account_key = a.account_key
INNER JOIN dbo.vw_dim_product p
    ON f.product_key = p.product_key
INNER JOIN dbo.vw_dim_branch b
    ON f.branch_key = b.branch_key;
GO
