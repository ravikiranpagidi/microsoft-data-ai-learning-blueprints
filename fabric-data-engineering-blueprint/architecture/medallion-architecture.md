# Medallion Architecture

The medallion architecture separates the Lakehouse into layers with clear quality expectations.

~~~mermaid
flowchart TB
    subgraph B["Bronze layer - raw and auditable"]
        b1["bronze_customers"]
        b2["bronze_accounts"]
        b3["bronze_transactions"]
        b4["bronze_products"]
        b5["bronze_branches"]
    end
    subgraph S["Silver layer - clean and conformed"]
        s1["silver_customers"]
        s2["silver_accounts"]
        s3["silver_transactions"]
        s4["silver_products"]
        s5["silver_branches"]
    end
    subgraph G["Gold layer - business-ready star schema"]
        d1["dim_customer"]
        d2["dim_account"]
        d3["dim_product"]
        d4["dim_branch"]
        d5["dim_date"]
        f1["fact_transaction"]
    end
    B --> S --> G
    d1 --> f1
    d2 --> f1
    d3 --> f1
    d4 --> f1
    d5 --> f1
~~~

## Layer Responsibilities

| Layer | Purpose | Example tables |
| --- | --- | --- |
| Bronze | Raw and auditable data with ingestion metadata | bronze_customers, bronze_transactions |
| Silver | Cleaned, typed, deduplicated, conformed data | silver_customers, silver_accounts |
| Gold | Business-ready dimensional model | dim_customer, fact_transaction |

## Why This Matters

- Bronze supports troubleshooting and auditability.
- Silver creates technical trust.
- Gold creates business trust.
- Quality checks can be applied before publication.
- Power BI models stay simpler and more reusable.

## Recommendation

Do not collapse the layers during the first proof of concept. Even small datasets benefit from clear lineage and explainability.
