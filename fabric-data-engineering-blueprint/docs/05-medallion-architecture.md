# Medallion Architecture

## Concept

Medallion architecture organizes data into Bronze, Silver, and Gold layers. Bronze preserves raw data, Silver cleans and conforms it, and Gold serves business-ready consumption.

## Why It Matters

Layering makes pipelines easier to debug, improves trust, and gives teams clear checkpoints for quality and governance.

## How It Works in Microsoft Fabric

Fabric Lakehouse tables can represent each layer using Delta format. Notebooks can transform Bronze to Silver and Silver to Gold. SQL analytics endpoint can expose Gold tables and views.

## Real-World Use Case

The retail banking project stores raw CSV-derived tables in Bronze, cleaned customer/account/product/branch/transaction data in Silver, and star schema tables in Gold.

## Beginner Explanation

Bronze is what arrived. Silver is what we trust technically. Gold is what the business can use.

## Enterprise Best Practice

Apply data quality checks before promoting data to Gold. Document ownership and SLA expectations for each Gold table.

## Common Mistakes

- Skipping Bronze and losing auditability.
- Skipping Silver and putting all logic into BI.
- Publishing Gold before validating key relationships.
- Using Gold as a place for every possible intermediate table.

## Practical Recommendation

Use Bronze, Silver, and Gold even for small proof of concepts so learners build the right habit early.

## Medallion Diagram

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
