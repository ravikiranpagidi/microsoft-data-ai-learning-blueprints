# Fabric Data Engineering Overview

> **Learning stage:** Foundation
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply fabric data engineering overview to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Microsoft Fabric Fundamentals](Microsoft-Fabric-Fundamentals) | [Home](Home) | [OneLake Explained](OneLake-Explained)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain what Fabric Data Engineering means and how Lakehouse, notebooks, Spark, pipelines, Delta tables, SQL endpoint, and Power BI work together.

## Who Should Read This

Data engineers, Power BI developers, and learners who want to understand the implementation workflow before running notebooks.

## What Fabric Data Engineering Means

Fabric Data Engineering is the set of capabilities used to ingest, process, transform, validate, and prepare data for analytics inside Microsoft Fabric. In this blueprint, the Data Engineering experience centers on Lakehouse, notebooks, Spark, Delta tables, and orchestration.

## Core Components

| Component | Role in this repo |
| --- | --- |
| Lakehouse | Stores Files and Delta Tables in OneLake. |
| Notebook | Runs PySpark transformations for Bronze, Silver, and Gold. |
| Spark | Executes distributed data processing logic. |
| Data Pipeline | Orchestrates ingestion and notebook execution. |
| Delta Table | Provides reliable table storage with schema and transaction support. |
| SQL Analytics Endpoint | Lets SQL users query Lakehouse tables and create views. |
| Power BI | Consumes Gold tables or views through a semantic model. |

## Typical Workflow

1. Land source files in the Lakehouse Files area.
2. Use a pipeline to orchestrate ingestion.
3. Use a notebook to create Bronze Delta tables.
4. Use notebooks to clean and standardize Silver tables.
5. Use notebooks to build Gold facts and dimensions.
6. Use SQL views for governed consumption.
7. Use Power BI semantic models for business reporting.

## Practical Example

The transactions.csv file lands in Files. Notebook 01 writes bronze_transactions. Notebook 02 casts transaction timestamps, standardizes status values, validates account IDs, and writes silver_transactions. Notebook 03 joins transactions to dimensions and writes fact_transaction. SQL scripts expose business-friendly views for Power BI.

## Best Practices

- Keep orchestration in pipelines and complex transformation logic in notebooks.
- Keep Bronze raw enough to replay.
- Put business cleanup and conformance in Silver.
- Put reporting shape and metrics readiness in Gold.
- Use data quality checks before broad consumption.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Doing all work in one notebook | Hard to test and reuse | Separate setup, Bronze, Silver, Gold, DQ, and consumption. |
| Using pipelines for complex business logic | Visual flows become hard to maintain | Use notebooks for code-heavy transformations. |
| Exposing raw tables to Power BI | Business users see inconsistent data | Expose Gold tables and governed views. |

## Related Repo Files

- [notebooks/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/notebooks)
- [pipelines/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/pipelines)
- [sql/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/sql)
- [docs/02-fabric-data-engineering-concepts.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/docs/02-fabric-data-engineering-concepts.md)

## Related Wiki Pages

- [Microsoft Fabric Fundamentals](Microsoft-Fabric-Fundamentals)
- [Lakehouse Concepts](Lakehouse-Concepts)
- [Dataflow Gen2 vs Notebook vs Pipeline](Dataflow-Gen2-vs-Notebook-vs-Pipeline)
- [Bronze Layer Design](Bronze-Layer-Design)

## Summary Checklist

- [ ] I can describe the role of Lakehouse, notebooks, pipelines, and SQL endpoint.
- [ ] I understand the end-to-end data engineering workflow.
- [ ] I know why transformations are split into Bronze, Silver, and Gold.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Microsoft Fabric Fundamentals](Microsoft-Fabric-Fundamentals) | [Home](Home) | [OneLake Explained](OneLake-Explained) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
