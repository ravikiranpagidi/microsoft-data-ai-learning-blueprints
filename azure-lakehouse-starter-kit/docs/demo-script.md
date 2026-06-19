# Demo Script

## Purpose

Provide a 10 to 15 minute presentation flow for community, portfolio, recruiter, or enterprise stakeholder demos.

## Demo Flow

### 1. Business Scenario

"This starter kit models a retail customer analytics lakehouse. We have customer, product, order, payment, inventory, and web activity data. The goal is to turn raw operational data into trusted Gold tables for Customer 360, sales reporting, product performance, inventory visibility, and AI-ready datasets."

### 2. Architecture

Show the architecture diagram. Explain that ADF handles ingestion and orchestration, ADLS Gen2 stores the lake layers, Databricks handles transformations, Delta Lake provides reliable tables, and Power BI consumes the curated Gold layer.

### 3. Repo Structure

Show `adf`, `databricks`, `sql`, `data`, `schemas`, `cicd`, and `tests`.

### 4. Sample Raw Data

Open sample customer, product, order, payment, inventory, and web activity data.

### 5. ADF Pipeline Design

Walk through metadata-driven ingestion and the master orchestration pipeline.

### 6. Bronze Notebook

Explain reading raw files, adding audit columns, and writing Delta.

### 7. Silver Notebook

Explain type casting, standardization, dedupe, business rules, and quarantine.

### 8. Data Quality

Show DQ rule examples, DQ results, and failed record handling.

### 9. Gold Transformation

Show `dim_customer`, `dim_product`, `fact_sales`, `customer_360`, and `daily_sales_summary`.

### 10. CI/CD

Explain validation, deployment templates, secrets, and environment promotion.

### 11. Extension Path

Close with Power BI semantic modeling and AI-ready Customer 360 features.
