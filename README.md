# Microsoft Fabric Data Engineering Blueprint

[![Microsoft Fabric](https://img.shields.io/badge/Microsoft%20Fabric-Data%20Engineering-742774?style=for-the-badge)](https://learn.microsoft.com/fabric/)
[![Data Engineering](https://img.shields.io/badge/Data%20Engineering-End--to--End-0078D4?style=for-the-badge)](docs/02-fabric-data-engineering-concepts.md)
[![Lakehouse](https://img.shields.io/badge/Lakehouse-Medallion%20Architecture-0078D4?style=for-the-badge)](docs/05-medallion-architecture.md)
[![PySpark](https://img.shields.io/badge/PySpark-Notebooks-E25A1C?style=for-the-badge)](notebooks/README.md)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Tables-00A1F1?style=for-the-badge)](adr/003-why-use-delta-tables.md)
[![Power BI](https://img.shields.io/badge/Power%20BI-Semantic%20Model-F2C811?style=for-the-badge)](semantic-model/README.md)
[![Open Source](https://img.shields.io/badge/Open%20Source-Contributions%20Welcome-2EA44F?style=for-the-badge)](CONTRIBUTING.md)

Practical, beginner-friendly, and enterprise-grade Microsoft Fabric Data Engineering blueprint for lakehouse-based analytics solutions.

This repository uses a realistic **Retail Banking Customer Analytics** domain to show how source CSV data can move through a professional Fabric data engineering flow: source files, Data Pipelines, Lakehouse Files, Bronze Delta tables, Fabric Notebooks, Silver tables, Gold dimensional modeling, SQL analytics endpoint views, and Power BI semantic model guidance.

The repo is intentionally more than a tutorial. It is a reusable open-source learning and implementation blueprint that a beginner can follow, an Azure data engineer can map to familiar tools, and an enterprise team can adapt for a first Microsoft Fabric proof of concept.

## Repository Vision

This blueprint helps you understand both **how to build** and **why each design decision matters** in Microsoft Fabric Data Engineering.

It is designed for:

- Beginners who want a guided path into Microsoft Fabric Data Engineering.
- Azure Data Engineers moving from ADF, Synapse, or Databricks to Fabric.
- Power BI developers who want to understand lakehouse engineering and star schema design.
- Students and interview candidates preparing for real scenario discussions.
- Enterprise teams building their first Fabric proof of concept.
- Architects documenting governance, CI/CD, medallion, and semantic model patterns.

## What You Will Learn

- How Microsoft Fabric Data Engineering fits into end-to-end analytics.
- How OneLake, Lakehouse, Delta tables, notebooks, pipelines, and SQL analytics endpoint work together.
- How to design Bronze, Silver, and Gold layers using medallion architecture.
- How to create dimensions, facts, SQL views, and Power BI-ready metrics.
- How to apply data quality checks before publishing curated data.
- How to think about governance, access control, PII, CI/CD, and deployment pipelines.
- How to explain Fabric architecture in interviews, design reviews, and stakeholder sessions.

## If You Are New to Fabric

Think of this repository as a guided build of a real analytics project:

| Concept | Beginner explanation |
| --- | --- |
| Workspace | The team area where Fabric items live. |
| OneLake | The shared storage foundation behind Fabric data. |
| Lakehouse | The place where files and Delta tables are stored for engineering and analytics. |
| Data Pipeline | The orchestration layer that moves data and runs activities. |
| Notebook | The code layer where PySpark transformations, validation, and modeling happen. |
| Bronze | Raw data as it arrived, with ingestion metadata. |
| Silver | Cleaned, typed, deduplicated, and validated data. |
| Gold | Business-ready facts and dimensions for reporting. |
| SQL analytics endpoint | SQL access over Lakehouse tables and views. |
| Semantic model | The Power BI business layer with relationships and measures. |

The simplest mental model is: **pipelines run the process, notebooks transform the data, Lakehouse stores the layers, SQL views simplify access, and Power BI tells the story.**

## End-to-End Architecture Overview

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

## Microsoft Fabric Icon Guidance

GitHub Mermaid diagrams do not reliably render custom SVG product icons inside flowchart nodes. To keep the repository readable on GitHub and still support professional architecture material, this repo includes an official Fabric icon mapping in <code>architecture/assets/README.md</code>. Use those icons when turning the diagrams into slide decks, blog diagrams, or meetup visuals.

## Sample Business Scenario

A retail banking analytics team wants to answer practical business questions from operational CSV extracts.

Business questions covered:

- How many active customers do we have?
- Which products are most used?
- What is the transaction volume by month?
- Which branches have high transaction activity?
- What are the top customer segments?
- How do balances and transactions trend over time?
- Which customers, accounts, and products need deeper analysis?

## Data Model Summary

| Entity | Purpose | Gold layer target |
| --- | --- | --- |
| Customer | Customer profile, segment, status, geography | dim_customer |
| Account | Account ownership, account type, status, balance | dim_account |
| Product | Banking product hierarchy and category | dim_product |
| Transaction | Monetary activity by account, branch, date, channel | fact_transaction |
| Branch | Branch geography and operational region | dim_branch |
| Date | Calendar attributes for reporting | dim_date |

## Technology Coverage

| Area | Covered in this repo |
| --- | --- |
| Microsoft Fabric workspace design | docs, governance, CI/CD |
| OneLake and Lakehouse | docs, architecture, notebooks |
| Data Factory pipelines in Fabric | pipeline templates and orchestration pattern |
| Fabric notebooks and Spark | PySpark notebook examples |
| Delta tables | Bronze, Silver, and Gold examples |
| Medallion architecture | docs, ADRs, notebook flow |
| SQL analytics endpoint | SQL scripts and consumption views |
| Power BI consumption | semantic model guidance and measures |
| Data quality | YAML rules, PySpark framework, report template |
| Governance | access model, PII handling, classification, ownership |
| CI/CD | Git integration, deployment pipelines, release checklist |
| Interview preparation | concept, scenario, and hands-on guides |

## Fabric Decision Guide

Use [docs/16-fabric-decision-guide.md](docs/16-fabric-decision-guide.md) during design reviews and proof-of-concept planning.

| Decision | Short recommendation |
| --- | --- |
| Lakehouse vs Warehouse | Use Lakehouse for file, Spark, Delta, and medallion engineering. Use Warehouse for SQL-first relational serving patterns. |
| Notebook vs Data Pipeline | Use notebooks for transformation logic and pipelines for orchestration. |
| Dataflow Gen2 vs Notebook | Use Dataflow Gen2 for low-code shaping; notebooks for code-based engineering and complex rules. |
| Shortcut vs Copy | Use shortcuts for reuse without duplication; copy when auditability and replay matter. |
| Gold table vs SQL View | Use Gold tables for reusable curated assets; SQL views for business-friendly consumption. |
| Star schema vs Wide table | Use star schema for governed BI; wide tables only for narrow, documented use cases. |
| Direct Lake vs Import | Use Direct Lake for Fabric-native large models; Import for small, mixed-source, or Power Query-heavy models. |

## Real-World Architecture Patterns

See [architecture/real-world-architecture-patterns.md](architecture/real-world-architecture-patterns.md) for diagrams and implementation notes.

| Pattern | Use when |
| --- | --- |
| Small team pattern | A small team is building its first Fabric proof of concept. |
| Enterprise pattern | Dev/Test/Prod, governance, CI/CD, and production support are required. |
| Data product pattern | A domain team owns reusable data for other teams. |
| Self-service BI pattern | Analysts need governed flexibility without raw-data exposure. |
| AI-ready lakehouse pattern | Curated data will support ML, semantic search, copilots, or analytics agents. |

## Common Enterprise Mistakes

The detailed guide is in [docs/17-common-enterprise-mistakes.md](docs/17-common-enterprise-mistakes.md).

Common mistakes this blueprint helps correct:

- Treating Fabric as only a Power BI reporting feature.
- Giving too many users workspace admin access.
- Building reports directly on Bronze data.
- Skipping data quality until users find issues.
- Hardcoding environment values in notebooks and pipelines.
- Creating too many semantic models with conflicting measures.
- Confusing pipeline success with data success.
- Overusing wide tables instead of designing a star schema.
- Ignoring PII until late in the project.
- Promoting changes without a release checklist.

## Fabric Project Checklist

Use [checklists/fabric-project-checklist.md](checklists/fabric-project-checklist.md) before production release or architecture review.

It covers workspace setup, naming standards, Lakehouse setup, data ingestion, transformation, data quality, security, governance, Power BI consumption, CI/CD, and production readiness.

## Exact Repository Structure

~~~text
fabric-data-engineering-blueprint/
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   |   |-- bug_report.yml
|   |   |-- config.yml
|   |   |-- documentation_improvement.yml
|   |   |-- feature_request.yml
|   |   +-- new_example_request.yml
|   +-- pull_request_template.md
|-- adr/
|   |-- 001-why-medallion-architecture.md
|   |-- 002-why-gold-star-schema.md
|   |-- 003-why-use-delta-tables.md
|   |-- 004-why-separate-engineering-and-consumption-layers.md
|   |-- 005-why-use-dev-test-prod-workspaces.md
|   |-- 006-why-apply-data-quality-before-gold-layer.md
|   |-- 007-why-start-with-direct-lake-for-fabric-power-bi.md
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
|   |-- README.md
|   +-- real-world-architecture-patterns.md
|-- checklists/
|   |-- fabric-project-checklist.md
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
|   |-- 15-learning-resources.md
|   |-- 16-fabric-decision-guide.md
|   +-- 17-common-enterprise-mistakes.md
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
|   |-- 07_incremental_load_pattern.ipynb
|   |-- 08_operational_monitoring_examples.ipynb
|   +-- README.md
|-- pipelines/
|   |-- ingestion_pipeline_template.json
|   |-- orchestration_pattern.md
|   |-- pipeline_overview.md
|   |-- README.md
|   +-- transformation_pipeline_template.json
|-- roadmap/
|   |-- 30-day-learning-plan.md
|   |-- 90-day-fabric-data-engineer-growth-plan.md
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
|   |-- advanced_analytics_examples.sql
|   |-- business_metrics.sql
|   |-- create_gold_views.sql
|   |-- operational_monitoring_examples.sql
|   |-- powerbi_consumption_views.sql
|   |-- README.md
|   +-- validation_queries.sql
|-- .gitattributes
|-- .gitignore
|-- CHANGELOG.md
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
+-- README.md
~~~

## Recommended Phased Implementation Plan

### Version 1: Beginner End-to-End Blueprint

- Create a Fabric workspace and Lakehouse.
- Upload the sample CSV files into Lakehouse Files.
- Run notebooks from setup through Gold dimensional model.
- Query the Gold tables using SQL analytics endpoint views.
- Build a simple Power BI report using the recommended semantic model design.

### Version 2: Data Pipelines, CI/CD, and Governance

- Replace manual file uploads with Fabric Data Pipeline ingestion.
- Parameterize notebook execution by environment and batch ID.
- Add data quality checks into orchestration.
- Configure Dev, Test, and Prod workspaces.
- Add Git integration, deployment pipeline guidance, and release checklists.
- Apply role-based access, PII classification, ownership, and naming standards.

### Version 3: Performance, Monitoring, and Advanced Patterns

- Add Delta optimization and maintenance routines.
- Introduce monitoring dashboards for pipeline health and data freshness.
- Add incremental load and CDC examples.
- Expand into data product architecture and domain ownership.
- Add advanced Power BI semantic model and aggregation patterns.
- Add enterprise observability and cost management practices.

## Step-by-Step Learning Path

1. Read [docs/00-overview.md](docs/00-overview.md).
2. Learn the Fabric concepts in [docs/01-what-is-microsoft-fabric.md](docs/01-what-is-microsoft-fabric.md) through [docs/07-sql-analytics-endpoint.md](docs/07-sql-analytics-endpoint.md).
3. Review the diagrams in [architecture/](architecture/README.md).
4. Upload the files from [sample-data/](sample-data/README.md) into a Fabric Lakehouse.
5. Run notebooks in order from [notebooks/00_setup_lakehouse.ipynb](notebooks/00_setup_lakehouse.ipynb) through [notebooks/06_powerbi_ready_views.ipynb](notebooks/06_powerbi_ready_views.ipynb).
6. Execute SQL scripts in [sql/](sql/README.md) against the SQL analytics endpoint.
7. Design the Power BI semantic model using [semantic-model/](semantic-model/README.md).
8. Review production topics in [governance/](governance/README.md), [cicd/](cicd/README.md), and [adr/](adr/README.md).
9. Use [interview-guide/](interview-guide/README.md) and [roadmap/](roadmap/README.md) for learning reinforcement.

## Setup Instructions

Prerequisites:

- Microsoft Fabric tenant with Fabric capacity or trial capacity enabled.
- Fabric workspace where you can create Lakehouse, Notebook, Data Pipeline, and Power BI items.
- Basic understanding of SQL and Python.
- Power BI Desktop or Power BI web authoring access.

Recommended setup:

1. Create a Fabric workspace named <code>fab-retailbank-dev</code>.
2. Create a Lakehouse named <code>lh_retailbank_dev</code>.
3. Upload files from <code>sample-data/</code> to <code>Files/retail_banking/source/</code>.
4. Import or recreate each notebook from <code>notebooks/</code> in the Fabric workspace.
5. Attach the notebooks to the Lakehouse.
6. Run notebooks in numeric order.
7. Open the SQL analytics endpoint for the Lakehouse and run scripts from <code>sql/</code>.
8. Create a Power BI semantic model using the Gold tables or SQL views.

## How to Run the Notebooks

| Order | Notebook | Purpose |
| --- | --- | --- |
| 00 | 00_setup_lakehouse.ipynb | Define parameters, paths, and reusable helpers |
| 01 | 01_bronze_ingestion.ipynb | Read CSVs, add ingestion metadata, write Bronze Delta tables |
| 02 | 02_silver_transformation.ipynb | Clean, cast, standardize, deduplicate, and validate data |
| 03 | 03_gold_dimensional_model.ipynb | Build dimensions and fact table for reporting |
| 04 | 04_data_quality_checks.ipynb | Run data quality checks and produce a pass/fail report |
| 05 | 05_delta_optimization.ipynb | Apply table maintenance and optimization patterns |
| 06 | 06_powerbi_ready_views.ipynb | Prepare reporting-friendly views and examples |
| 07 | 07_incremental_load_pattern.ipynb | Learn a watermark-based incremental load pattern |
| 08 | 08_operational_monitoring_examples.ipynb | Create simple audit and monitoring examples |

## How to Use the SQL Scripts

Open the Lakehouse SQL analytics endpoint and run scripts in this order:

1. [sql/create_gold_views.sql](sql/create_gold_views.sql)
2. [sql/business_metrics.sql](sql/business_metrics.sql)
3. [sql/validation_queries.sql](sql/validation_queries.sql)
4. [sql/powerbi_consumption_views.sql](sql/powerbi_consumption_views.sql)
5. [sql/advanced_analytics_examples.sql](sql/advanced_analytics_examples.sql)
6. [sql/operational_monitoring_examples.sql](sql/operational_monitoring_examples.sql)

## How to Connect Power BI

1. Open the Fabric workspace.
2. Select the Lakehouse SQL analytics endpoint or semantic model experience.
3. Use Gold tables or views such as <code>vw_fact_transaction</code>, <code>vw_dim_customer</code>, and <code>vw_monthly_transaction_summary</code>.
4. Create relationships from facts to dimensions using surrogate keys.
5. Add measures from [semantic-model/measures.md](semantic-model/measures.md).
6. Build report pages for customer overview, product usage, branch activity, and transaction trends.

## Best Practices Covered

- Keep raw data auditable in Bronze.
- Apply cleaning and conformance in Silver.
- Publish only business-ready facts and dimensions to Gold.
- Run data quality before Gold publication.
- Use SQL views to simplify consumption.
- Use least privilege access by layer.
- Separate Dev, Test, and Prod workspaces.
- Version notebooks, SQL, pipeline templates, data quality rules, and documentation.
- Avoid putting secrets, production data, or environment-specific IDs in source control.

## Common Mistakes Avoided

- Skipping the Silver layer and building reports directly on raw files.
- Treating notebooks and pipelines as interchangeable instead of complementary.
- Building wide reporting tables before understanding fact and dimension design.
- Ignoring data quality until Power BI users find errors.
- Giving all users access to all layers of the Lakehouse.
- Hardcoding workspace IDs, Lakehouse IDs, and environment paths.
- Publishing a semantic model without metric definitions and ownership.

## Decision Guides Included

- Lakehouse vs Warehouse
- Notebook vs Pipeline
- Dataflow Gen2 vs Notebook
- Shortcut vs Copy
- Gold table vs View
- Star schema vs Wide table

Start with [docs/03-lakehouse-vs-warehouse.md](docs/03-lakehouse-vs-warehouse.md), [docs/06-data-pipeline-vs-notebook.md](docs/06-data-pipeline-vs-notebook.md), and [architecture/data-product-architecture.md](architecture/data-product-architecture.md).

## Roadmap

See [roadmap/](roadmap/README.md) for beginner, intermediate, and advanced learning paths.

Structured plans:

- [30-Day Learning Plan for Beginners](roadmap/30-day-learning-plan.md)
- [90-Day Fabric Data Engineer Growth Plan](roadmap/90-day-fabric-data-engineer-growth-plan.md)

Immediate future enhancements:

- Larger synthetic transaction generator.
- Power BI report template.
- Optional deployment automation with Fabric APIs.

## Contributing

Contributions are welcome when they improve clarity, correctness, practical usefulness, or enterprise readiness. Start with [CONTRIBUTING.md](CONTRIBUTING.md), use the GitHub issue templates, and review [community/contribution-tracker-template.md](community/contribution-tracker-template.md).

Useful contribution areas:

- Add new Fabric scenarios.
- Improve notebooks or SQL examples.
- Add Power BI report screenshots or templates.
- Add data quality rule examples.
- Add interview questions and hands-on labs.
- Improve governance and CI/CD guidance.
- Add decision guides, architecture patterns, or production monitoring examples.
- Improve beginner explanations with diagrams and practical analogies.

## Author and Community

Created as a practical Microsoft Fabric Data Engineering learning and implementation blueprint for the data community.

If this repository helps you learn or explain Microsoft Fabric, consider starring it, forking it, and sharing what you build. The best open-source learning projects grow through practical examples, corrections, and field-tested patterns.

## Official References

- [Microsoft Fabric documentation](https://learn.microsoft.com/fabric/)
- [Microsoft Fabric Data Engineering](https://learn.microsoft.com/fabric/data-engineering/)
- [OneLake documentation](https://learn.microsoft.com/fabric/onelake/)
- [Fabric Git integration](https://learn.microsoft.com/fabric/cicd/git-integration/intro-to-git-integration)
- [Fabric deployment pipelines](https://learn.microsoft.com/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines)
- [Dataflow Gen2 overview](https://learn.microsoft.com/fabric/data-factory/dataflows-gen2-overview)
- [Direct Lake overview](https://learn.microsoft.com/fabric/get-started/direct-lake-overview)
- [Direct Lake semantic model development](https://learn.microsoft.com/fabric/fundamentals/direct-lake-edit-tables)
- [Microsoft Fabric icons](https://learn.microsoft.com/fabric/fundamentals/icons)
