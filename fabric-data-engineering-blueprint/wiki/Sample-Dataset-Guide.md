# Sample Dataset Guide

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply sample dataset guide to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Retail Banking Sample Domain](Retail-Banking-Sample-Domain) | [Home](Home) | [Medallion Architecture](Medallion-Architecture)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Document each sample dataset, its business meaning, key columns, relationships, quality expectations, and layer flow.

## Who Should Read This

Hands-on users preparing sample data, data modelers, and contributors adding new example files.

## Dataset Overview

The sample-data folder contains small CSV files that are intentionally easy to inspect. They are not meant to simulate production volume. They are meant to teach relationships, typing, validation, and modeling.

## customers.csv

| Area | Detail |
| --- | --- |
| Meaning | Customer master data. |
| Key column | customer_id |
| Example fields | first_name, last_name, email, city, state, customer_segment, customer_status |
| Relationships | One customer can have many accounts and many transactions through accounts. |
| Quality expectations | customer_id required and unique; status values should be Active or Inactive; email should have valid shape. |
| Flow | Files -> bronze_customers -> silver_customers -> dim_customer |

## accounts.csv

| Area | Detail |
| --- | --- |
| Meaning | Customer accounts and balances. |
| Key column | account_id |
| Example fields | customer_id, product_id, account_type, account_status, current_balance, branch_id |
| Relationships | Many accounts belong to customers, products, and branches. |
| Quality expectations | account_id required and unique; customer_id, product_id, and branch_id must exist. |
| Flow | Files -> bronze_accounts -> silver_accounts -> dim_account |

## products.csv

| Area | Detail |
| --- | --- |
| Meaning | Banking products such as checking, savings, credit card, investment. |
| Key column | product_id |
| Relationships | One product can be linked to many accounts and transactions. |
| Quality expectations | product_id required and unique; product category and family should be populated. |
| Flow | Files -> bronze_products -> silver_products -> dim_product |

## branches.csv

| Area | Detail |
| --- | --- |
| Meaning | Branch or advisory location master data. |
| Key column | branch_id |
| Relationships | Branches relate to accounts and transactions. |
| Quality expectations | branch_id required and unique; region should be standardized. |
| Flow | Files -> bronze_branches -> silver_branches -> dim_branch |

## transactions.csv

| Area | Detail |
| --- | --- |
| Meaning | Account-level transaction events. |
| Key column | transaction_id |
| Example fields | account_id, product_id, branch_id, transaction_timestamp, transaction_type, transaction_amount, status |
| Relationships | Transactions join to account, product, branch, customer, and date. |
| Quality expectations | transaction_id required and unique; account_id must exist; amount should be numeric; status should be accepted. |
| Flow | Files -> bronze_transactions -> silver_transactions -> fact_transaction |

## Data Quality Expectations

- Required IDs are not null or blank.
- Business keys are unique.
- Status values come from accepted lists.
- Referential relationships are valid.
- Numeric amounts are in reasonable ranges.
- Row counts reconcile from Silver to Gold for transactions.

## How Contributors Can Extend the Data

Add new rows carefully. Preserve IDs and relationship integrity. If you add a new entity, update notebooks, SQL scripts, DQ rules, semantic docs, and this Wiki page.

## Related Repo Files

- [sample-data/customers.csv](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/sample-data/customers.csv)
- [sample-data/accounts.csv](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/sample-data/accounts.csv)
- [sample-data/products.csv](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/sample-data/products.csv)
- [sample-data/branches.csv](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/sample-data/branches.csv)
- [sample-data/transactions.csv](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/sample-data/transactions.csv)
- [data-quality/dq_rules.yml](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/data-quality/dq_rules.yml)

## Related Wiki Pages

- [Retail Banking Sample Domain](Retail-Banking-Sample-Domain)
- [Silver Layer Design](Silver-Layer-Design)
- [Gold Layer Design](Gold-Layer-Design)
- [Building Dimensions and Facts](Building-Dimensions-and-Facts)
- [Governance and Security](Governance-and-Security)

## Summary Checklist

- [ ] I know the purpose of each CSV file.
- [ ] I understand the primary keys and relationships.
- [ ] I know how each file moves through Bronze, Silver, and Gold.
- [ ] I know what to update when adding sample data.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Retail Banking Sample Domain](Retail-Banking-Sample-Domain) | [Home](Home) | [Medallion Architecture](Medallion-Architecture) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
