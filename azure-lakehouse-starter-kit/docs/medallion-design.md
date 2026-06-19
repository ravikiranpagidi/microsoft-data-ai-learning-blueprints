# Medallion Design

## Purpose

Explain how Raw, Bronze, Silver, and Gold layers are used in this starter kit.

## Layers

| Layer | Purpose | Example Tables |
| --- | --- | --- |
| Raw | Store original extracts as received | Files under `raw/customer/` |
| Bronze | Store raw data as Delta with audit columns | `bronze_customers`, `bronze_orders` |
| Silver | Clean, typed, deduplicated, validated data | `silver_customers`, `silver_orders` |
| Gold | Business-ready dimensional and analytical tables | `dim_customer`, `fact_sales`, `customer_360` |

## Table Grain

| Table | Grain |
| --- | --- |
| `dim_customer` | One row per customer |
| `dim_product` | One row per product |
| `fact_sales` | One row per order item |
| `fact_inventory` | One row per product, location, and inventory snapshot date |
| `customer_360` | One row per customer with summary metrics |
| `daily_sales_summary` | One row per date, region, and product category |

## Recommendations

- Keep Bronze close to source structure.
- Make Silver conform names, types, keys, and business rules.
- Build Gold around business questions.
- Avoid exposing Bronze directly to BI users.
- Add audit columns in every layer.
