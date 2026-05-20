# Semantic Model Design

## Purpose

The semantic model turns the Gold data model into a governed business layer for Power BI.

## Recommended Tables

| Table | Role | Relationship |
| --- | --- | --- |
| fact_transaction | Fact table | Many side of relationships |
| dim_customer | Customer dimension | One customer to many transactions |
| dim_account | Account dimension | One account to many transactions |
| dim_product | Product dimension | One product to many transactions |
| dim_branch | Branch dimension | One branch to many transactions |
| dim_date | Date dimension | One date to many transactions |

## Relationship Guidance

| From | To | Cardinality | Filter direction |
| --- | --- | --- | --- |
| dim_customer.customer_key | fact_transaction.customer_key | One-to-many | Single |
| dim_account.account_key | fact_transaction.account_key | One-to-many | Single |
| dim_product.product_key | fact_transaction.product_key | One-to-many | Single |
| dim_branch.branch_key | fact_transaction.branch_key | One-to-many | Single |
| dim_date.date_key | fact_transaction.date_key | One-to-many | Single |

## Why Star Schema

A star schema is easier for Power BI to optimize, easier for report authors to understand, and easier for data owners to govern. It separates descriptive attributes from measurable events.

## Report Pages

Recommended first dashboard pages:

1. Executive Overview: active customers, total transaction amount, transaction count, average transaction amount.
2. Customer Segments: customer counts, transaction trends, balances by segment.
3. Product Usage: product category and product name usage.
4. Branch Activity: transaction activity by branch and region.
5. Account and Transaction Deep Dive: account type, status, channel, transaction detail.

## Enterprise Recommendation

Create one certified semantic model for shared reporting. Avoid creating separate report-specific models unless a clear ownership or performance reason exists.
