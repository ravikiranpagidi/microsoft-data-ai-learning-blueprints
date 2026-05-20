# Fabric Decision Guide

This guide helps teams make practical Microsoft Fabric architecture decisions. It is written for design reviews, proof-of-concept planning, interviews, and early enterprise adoption.

## How To Use This Guide

Start with the question you are trying to answer, then document the decision in an Architecture Decision Record if it affects production architecture, security, cost, or long-term ownership.

## Lakehouse vs Warehouse

| Choose Lakehouse when | Choose Warehouse when |
| --- | --- |
| You need Spark, notebooks, files, and Delta tables. | The team is SQL-first and wants relational warehouse patterns. |
| You are building Bronze, Silver, and Gold layers. | You are building curated dimensional marts mainly with SQL. |
| Data science or engineering teams need file-level access. | BI and SQL analysts are the primary builders. |
| Raw, semi-structured, or mixed data is part of the flow. | The data is already structured and modeled. |

Practical recommendation: use Lakehouse for this blueprint because the project starts with CSV files, PySpark transformations, Delta tables, and medallion architecture. Add Warehouse later only when a SQL-first serving layer has a clear business or performance reason.

## Notebook vs Data Pipeline

| Use Notebook for | Use Data Pipeline for |
| --- | --- |
| PySpark transformation logic. | Orchestration and scheduling. |
| Data validation and row-count checks. | Copy activities and movement. |
| Reusable engineering code. | Calling notebooks with parameters. |
| Complex joins, cleansing, and dimensional modeling. | Dependency handling and operational monitoring. |

Practical recommendation: keep transformation logic in notebooks and use pipelines to control the run order, parameters, retries, alerts, and refresh dependencies.

## Dataflow Gen2 vs Notebook

| Choose Dataflow Gen2 when | Choose Notebook when |
| --- | --- |
| Business users or analysts prefer Power Query. | Engineering teams need code review and reusable PySpark. |
| Transformations are mostly low-code shaping steps. | Transformations require complex joins, windows, testing, or libraries. |
| The workload is ingestion and simple standardization. | The workload is medallion modeling or data quality automation. |
| You want a visual transformation experience. | You need parameterized, modular, source-controlled code. |

Practical recommendation: use Dataflow Gen2 for approachable low-code ingestion and shaping. Use notebooks for the core engineering pattern in this repo.

## Shortcut vs Copy

| Use Shortcut when | Use Copy when |
| --- | --- |
| You want to reference data without duplicating it. | You need an auditable landing copy. |
| Ownership remains with another domain or workspace. | You need isolation from upstream changes. |
| Latency and storage duplication should be minimized. | You need a stable snapshot for reconciliation. |
| The target path is governed and reliable. | The source has unpredictable availability or quality. |

Practical recommendation: shortcuts are excellent for shared reference data and cross-domain reuse. Copy source extracts into Bronze when auditability, replay, and troubleshooting matter.

## Gold Table vs SQL View

| Use Gold table when | Use SQL view when |
| --- | --- |
| The data asset is reusable and curated. | You need business-friendly projection or renaming. |
| It has ownership, quality rules, and a stable grain. | You need to hide columns or simplify consumption. |
| Power BI relationships depend on it. | You need consumption-specific filters or joins. |
| It should be tested and versioned as a data product. | You want a lightweight semantic access layer. |

Practical recommendation: publish reusable facts and dimensions as Gold tables. Use SQL views to make consumption safer and easier.

## Star Schema vs Wide Table

| Choose Star Schema when | Choose Wide Table when |
| --- | --- |
| You need shared metrics across reports. | You need a narrow export or one-off analysis. |
| Dimensions are reused across facts. | The data shape is simple and temporary. |
| Power BI model performance and clarity matter. | The consumer cannot handle relationships. |
| Governance and semantic model reuse matter. | The trade-off is documented and owned. |

Practical recommendation: use a star schema for governed Fabric analytics. Wide tables can be useful at the edge, but they should not become the enterprise semantic foundation by accident.

## Direct Lake vs Import Mode in Power BI

| Choose Direct Lake when | Choose Import mode when |
| --- | --- |
| The data is in Fabric Lakehouse or Warehouse tables. | The model is small and refresh windows are acceptable. |
| You want to avoid duplicating data into a Power BI import model. | You need transformations or sources that are easier to handle in Power Query. |
| Large fact tables or frequent source updates are expected. | You need maximum compatibility with mature Import-mode modeling patterns. |
| You want Fabric-native semantic model consumption. | The data source is outside Fabric or mixed in ways Direct Lake does not support. |

Important nuance: Microsoft Fabric supports Direct Lake on OneLake and Direct Lake on SQL. Direct Lake on OneLake is recommended when you want strong OneLake alignment and modeling flexibility. Direct Lake on SQL is useful when you depend on SQL analytics endpoint behavior, delegated identity, or DirectQuery fallback.

Practical recommendation: for Fabric-native Gold Delta tables, start with Direct Lake. Use Import mode when the model is small, mixed-source, heavily shaped in Power Query, or when Direct Lake limitations affect required functionality.

## Decision Record Template

Use this short template when a decision will affect the project for more than one sprint.

| Field | Answer |
| --- | --- |
| Decision |  |
| Context |  |
| Option chosen |  |
| Alternatives considered |  |
| Consequences |  |
| Owner |  |
| Review date |  |

## Official References

- Microsoft Fabric documentation: https://learn.microsoft.com/fabric/
- Fabric Data Engineering: https://learn.microsoft.com/fabric/data-engineering/
- OneLake shortcuts: https://learn.microsoft.com/fabric/onelake/onelake-shortcuts
- Power BI semantic models in Fabric: https://learn.microsoft.com/fabric/data-warehouse/semantic-models
- Direct Lake overview: https://learn.microsoft.com/fabric/get-started/direct-lake-overview
- Direct Lake semantic model development: https://learn.microsoft.com/fabric/fundamentals/direct-lake-edit-tables
- Dataflow Gen2 overview: https://learn.microsoft.com/fabric/data-factory/dataflows-gen2-overview
