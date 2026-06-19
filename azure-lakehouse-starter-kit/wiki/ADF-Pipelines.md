# ADF Pipelines

## Purpose

This page explains the Azure Data Factory assets included in the starter kit.

## Included Pipelines

| Pipeline | Purpose |
| --- | --- |
| `pl_ingest_to_raw` | Metadata-driven source-to-raw ingestion |
| `pl_bronze_to_silver` | Orchestrates Silver Databricks notebooks |
| `pl_silver_to_gold` | Orchestrates Gold model publishing |
| `pl_master_orchestration` | Coordinates the complete end-to-end flow |

## Recommended Pattern

Use ADF for:

- Scheduling
- Metadata-driven orchestration
- Copying data into the raw zone
- Dependency management
- Retry and monitoring

Use Databricks for:

- Complex transformations
- Delta writes
- Deduplication
- Data quality checks
- Dimensional model building

## Metadata-Driven Ingestion

The metadata table defines source names, source objects, target folders, file formats, and load strategy. This allows adding new datasets without redesigning the pipeline.

## Checklist

- [ ] Pipeline parameters are environment-safe.
- [ ] Secrets are stored in Key Vault.
- [ ] Source metadata is reviewed.
- [ ] Failed pipeline runs are visible to support teams.
- [ ] Databricks notebook parameters are passed explicitly.

## Related Pages

- [Architecture](Architecture)
- [CI CD](CI-CD)
- [Troubleshooting](Troubleshooting)

