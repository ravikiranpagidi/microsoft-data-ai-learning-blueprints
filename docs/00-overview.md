# Repository Overview

This repository is a complete Microsoft Fabric Data Engineering blueprint using Retail Banking Customer Analytics as the sample domain.

## Vision

Build a practical learning and implementation path that takes a learner from raw source files to a business-ready Power BI semantic model while explaining the architecture decisions behind each step.

## Exact Repository Structure

~~~text
fabric-data-engineering-blueprint/
|-- adr/
|   |-- 001-why-medallion-architecture.md
|   |-- 002-why-gold-star-schema.md
|   |-- 003-why-use-delta-tables.md
|   |-- 004-why-separate-engineering-and-consumption-layers.md
|   |-- 005-why-use-dev-test-prod-workspaces.md
|   |-- 006-why-apply-data-quality-before-gold-layer.md
|   +-- README.md
|-- architecture/
|   |-- assets/
|   |   |-- icons/
|   |   |   |-- copy_job_48_item.svg
|   |   |   |-- data_warehouse_48_item.svg
|   |   |   |-- dataflow_gen2_48_item.svg
|   |   |   |-- lakehouse_48_item.svg
|   |   |   |-- notebook_48_item.svg
|   |   |   |-- NOTICE.md
|   |   |   |-- one_lake_48_color.svg
|   |   |   |-- pipeline_48_item.svg
|   |   |   |-- power_bi_48_color.svg
|   |   |   |-- report_48_item.svg
|   |   |   |-- semantic_model_48_item.svg
|   |   |   +-- sql_database_48_item.svg
|   |   +-- README.md
|   |-- cicd-flow.md
|   |-- data-product-architecture.md
|   |-- fabric-end-to-end-architecture.md
|   |-- governance-model.md
|   |-- lakehouse-to-powerbi-flow.md
|   |-- medallion-architecture.md
|   +-- README.md
|-- cicd/
|   |-- deployment-pipeline-guide.md
|   |-- dev-test-prod-strategy.md
|   |-- environment-configuration.md
|   |-- git-integration-guide.md
|   |-- README.md
|   +-- release-checklist.md
|-- community/
|   |-- blog-series-plan.md
|   |-- contribution-tracker-template.md
|   |-- meetup-session-abstract.md
|   |-- README.md
|   +-- youtube-demo-series.md
|-- data-quality/
|   |-- dq_examples.md
|   |-- dq_framework.py
|   |-- dq_report_template.md
|   |-- dq_rules.yml
|   +-- README.md
|-- docs/
|   |-- 00-overview.md
|   |-- 01-what-is-microsoft-fabric.md
|   |-- 02-fabric-data-engineering-concepts.md
|   |-- 03-lakehouse-vs-warehouse.md
|   |-- 04-onelake-explained.md
|   |-- 05-medallion-architecture.md
|   |-- 06-data-pipeline-vs-notebook.md
|   |-- 07-sql-analytics-endpoint.md
|   |-- 08-power-bi-consumption.md
|   |-- 09-cicd-and-deployment.md
|   |-- 10-security-and-governance.md
|   |-- 11-best-practices.md
|   |-- 12-common-mistakes.md
|   |-- 13-cost-and-performance-considerations.md
|   |-- 14-fabric-for-azure-data-engineers.md
|   +-- 15-learning-resources.md
|-- governance/
|   |-- access-control-model.md
|   |-- data-classification.md
|   |-- data-ownership-model.md
|   |-- governance-checklist.md
|   |-- naming-standards.md
|   |-- pii-handling.md
|   +-- README.md
|-- interview-guide/
|   |-- architecture-discussion-points.md
|   |-- fabric-data-engineering-questions.md
|   |-- hands-on-practice-tasks.md
|   |-- README.md
|   +-- scenario-based-questions.md
|-- notebooks/
|   |-- 00_setup_lakehouse.ipynb
|   |-- 01_bronze_ingestion.ipynb
|   |-- 02_silver_transformation.ipynb
|   |-- 03_gold_dimensional_model.ipynb
|   |-- 04_data_quality_checks.ipynb
|   |-- 05_delta_optimization.ipynb
|   |-- 06_powerbi_ready_views.ipynb
|   +-- README.md
|-- pipelines/
|   |-- ingestion_pipeline_template.json
|   |-- orchestration_pattern.md
|   |-- pipeline_overview.md
|   |-- README.md
|   +-- transformation_pipeline_template.json
|-- roadmap/
|   |-- advanced-path.md
|   |-- beginner-path.md
|   |-- intermediate-path.md
|   +-- README.md
|-- sample-data/
|   |-- accounts.csv
|   |-- branches.csv
|   |-- customers.csv
|   |-- products.csv
|   |-- README.md
|   +-- transactions.csv
|-- semantic-model/
|   |-- business_glossary.md
|   |-- measures.md
|   |-- powerbi_model_guidelines.md
|   |-- README.md
|   +-- semantic_model_design.md
|-- sql/
|   |-- business_metrics.sql
|   |-- create_gold_views.sql
|   |-- powerbi_consumption_views.sql
|   |-- README.md
|   +-- validation_queries.sql
|-- .gitignore
|-- CHANGELOG.md
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
+-- README.md
~~~

## End-to-End Flow

~~~mermaid
flowchart LR
    source["Source CSV files"] --> pipeline["Fabric Data Pipeline<br/>Copy activity"]
    pipeline --> onelake["OneLake"]
    onelake --> files["Lakehouse Files<br/>retail_banking/source"]
    files --> bronze["Bronze Delta tables<br/>raw plus metadata"]
    bronze --> notebook["Fabric Notebook<br/>PySpark transformation"]
    notebook --> silver["Silver Delta tables<br/>clean and conformed"]
    silver --> dq["Data quality checks<br/>rules, reconciliation, freshness"]
    dq --> gold["Gold dimensional model<br/>facts and dimensions"]
    gold --> sql["SQL analytics endpoint<br/>views and metrics"]
    sql --> semantic["Power BI semantic model<br/>relationships and measures"]
    semantic --> dashboard["Business dashboards<br/>customer analytics"]

    classDef fabric fill:#742774,stroke:#4B155F,color:#ffffff;
    classDef storage fill:#0078D4,stroke:#004578,color:#ffffff;
    classDef quality fill:#107C10,stroke:#0B5A0B,color:#ffffff;
    classDef consume fill:#F2C811,stroke:#B38600,color:#111111;
    class pipeline,notebook,sql fabric;
    class onelake,files,bronze,silver,gold storage;
    class dq quality;
    class semantic,dashboard consume;
~~~

## Recommended Phased Implementation Plan

### Version 1: Beginner End-to-End Blueprint

- Learn the core Fabric services used by data engineers.
- Create a workspace and Lakehouse.
- Upload sample source files.
- Run notebooks to create Bronze, Silver, and Gold Delta tables.
- Query curated data through the SQL analytics endpoint.
- Connect Power BI to the Gold model.

### Version 2: Data Pipelines, CI/CD, and Governance

- Add Fabric Data Pipeline ingestion.
- Parameterize notebooks and environments.
- Add YAML-driven data quality checks.
- Configure Dev, Test, and Prod workspace promotion.
- Document role-based access, PII handling, and ownership.

### Version 3: Performance, Monitoring, and Advanced Patterns

- Add incremental loading and CDC patterns.
- Add monitoring, alerting, and data freshness dashboards.
- Optimize Delta tables and Spark jobs.
- Add domain data product patterns.
- Expand the Power BI semantic model design.

## How To Use This Repo

1. Read the concept docs in order.
2. Review the architecture diagrams.
3. Upload sample data into a Fabric Lakehouse.
4. Run notebooks in numeric order.
5. Run SQL scripts against the SQL analytics endpoint.
6. Build the semantic model and dashboard recommendations.
7. Review governance, CI/CD, ADRs, and interview guide.
