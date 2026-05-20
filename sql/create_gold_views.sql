-- Gold consumption views for Retail Banking Customer Analytics.
-- Run in the Fabric Lakehouse SQL analytics endpoint.

CREATE OR ALTER VIEW dbo.vw_dim_customer AS
SELECT customer_key, customer_id, customer_full_name, customer_segment, customer_status, city, state, country, is_active_customer, created_date
FROM dbo.dim_customer;
GO

CREATE OR ALTER VIEW dbo.vw_dim_account AS
SELECT account_key, account_id, customer_id, product_id, branch_id, account_type, account_status, is_open_account, opened_date, closed_date, current_balance
FROM dbo.dim_account;
GO

CREATE OR ALTER VIEW dbo.vw_dim_product AS
SELECT product_key, product_id, product_name, product_category, product_family, fee_model, is_active, launch_date
FROM dbo.dim_product;
GO

CREATE OR ALTER VIEW dbo.vw_dim_branch AS
SELECT branch_key, branch_id, branch_name, city, state, region, is_active
FROM dbo.dim_branch;
GO

CREATE OR ALTER VIEW dbo.vw_dim_date AS
SELECT date_key, date_value, year, quarter, month, month_name, year_month, day_of_month, day_name, is_weekend
FROM dbo.dim_date;
GO

CREATE OR ALTER VIEW dbo.vw_fact_transaction AS
SELECT transaction_id, date_key, customer_key, account_key, product_key, branch_key, transaction_timestamp, transaction_date, transaction_type, transaction_channel, transaction_status, currency, transaction_amount, absolute_transaction_amount, is_posted
FROM dbo.fact_transaction;
GO
