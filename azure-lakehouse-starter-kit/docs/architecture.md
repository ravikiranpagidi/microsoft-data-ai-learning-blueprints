# Architecture

## Purpose

This page explains the end-to-end Azure Lakehouse Starter Kit architecture.

## Architecture Summary

The architecture uses Azure Data Factory for ingestion and orchestration, ADLS Gen2 for storage, Azure Databricks for processing, Delta Lake for reliable tables, and Power BI or Databricks SQL for consumption.

## Layers

| Layer | Components | Responsibility |
| --- | --- | --- |
| Data sources | Customer CSV, product CSV, orders database, payment API, inventory system, web logs | Provide operational source data |
| Ingestion | ADF, metadata table, parameterized pipelines, Copy activity | Land source data into raw storage |
| Storage | ADLS Gen2 raw, bronze, silver, gold containers | Store data by quality and use |
| Processing | Databricks notebooks, PySpark, Delta Lake, jobs | Transform and validate data |
| Data quality | Rule tables, checks, quarantine, scorecard | Prevent bad data from reaching Gold |
| Consumption | Gold Delta, Power BI, Databricks SQL, ML-ready datasets | Serve business and AI use cases |
| Governance | Key Vault, identities, Unity Catalog or Hive metastore, Purview, logs | Secure and document the platform |

## Recommended Flow

```text
Sources -> ADF -> Raw -> Bronze Delta -> Silver Delta -> Gold Delta -> Power BI and ML-ready datasets
```

ADF triggers Databricks notebooks after ingestion. Data quality checks validate Bronze to Silver and Silver to Gold. CI/CD deploys pipelines, notebooks, jobs, and configuration across dev, test, and prod.

## Design Principles

- Keep orchestration and transformation separate.
- Use metadata to avoid hardcoded pipelines.
- Use Delta Lake for managed table reliability.
- Validate data before Gold.
- Treat Gold as the contract for BI and downstream consumers.
- Keep secrets in Key Vault, not code.
