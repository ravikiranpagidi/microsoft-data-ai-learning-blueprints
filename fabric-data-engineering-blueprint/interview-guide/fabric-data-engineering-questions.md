# Fabric Data Engineering Questions

## 1. What is Microsoft Fabric?

Direct answer: Microsoft Fabric is a unified SaaS analytics platform that brings data integration, data engineering, warehousing, real-time analytics, data science, and Power BI together.

Practical explanation: Instead of stitching together many services manually, Fabric provides shared workspaces, OneLake storage, and integrated workloads.

Real-world example: A banking team can ingest CSV files, transform them with notebooks, publish Gold tables, and build Power BI reports in one Fabric workspace.

Follow-up question: How is Fabric different from using ADF, ADLS, Databricks, Synapse, and Power BI separately?

Strong interview-ready response: Fabric reduces integration overhead by bringing common analytics workloads into one SaaS platform with OneLake as the shared storage layer. You still need architecture, governance, and lifecycle management, but the platform simplifies collaboration between engineering and BI teams.

## 2. What is a Lakehouse in Fabric?

Direct answer: A Fabric Lakehouse stores files and Delta tables and supports Spark transformations plus SQL analytics endpoint consumption.

Practical explanation: It is useful when you need both file-based engineering and table-based analytics.

Real-world example: Source banking CSVs land in Lakehouse Files, then notebooks write Bronze, Silver, and Gold Delta tables.

Follow-up question: When would you choose Warehouse instead?

Strong interview-ready response: I choose Lakehouse when I need files, Spark, Delta, notebooks, and flexible medallion processing. I choose Warehouse when the solution is SQL-first and the team wants a relational warehouse development pattern.

## 3. What is OneLake?

Direct answer: OneLake is the shared data lake foundation for Microsoft Fabric.

Practical explanation: Fabric items use OneLake so data can be organized, reused, and governed consistently.

Real-world example: A Lakehouse stores Retail Banking source files and Delta tables in OneLake, and Power BI can consume the curated data.

Follow-up question: What is a shortcut?

Strong interview-ready response: OneLake provides a shared storage foundation. Shortcuts let teams reference data without copying it, but ownership, freshness, and permissions still need to be documented.

## 4. What is the SQL analytics endpoint?

Direct answer: The SQL analytics endpoint lets users query Lakehouse tables using SQL.

Practical explanation: Spark can create Delta tables, while SQL users and BI tools can query them through a familiar SQL layer.

Real-world example: Gold tables such as dim_customer and fact_transaction are exposed through SQL views for Power BI.

Follow-up question: Should reports query Bronze through the SQL endpoint?

Strong interview-ready response: Reports should use Gold tables or governed views. Bronze is for raw auditability and troubleshooting, not broad consumption.

## 5. Why use notebooks and pipelines together?

Direct answer: Pipelines orchestrate activities and movement. Notebooks implement code-based transformation logic.

Practical explanation: A pipeline controls what runs and in what order. A notebook controls how data is transformed.

Real-world example: A pipeline lands files and calls notebooks for Bronze ingestion, Silver transformation, Gold modeling, and data quality.

Follow-up question: What logic should not be placed in a pipeline?

Strong interview-ready response: I avoid embedding complex business transformation logic directly in pipeline activities. That logic is easier to test, version, and review in notebooks or libraries.
