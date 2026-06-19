# Databricks Notebooks

## Purpose

This page explains how the Databricks notebooks are organized and how to run them.

## Notebook Groups

| Folder | Purpose |
| --- | --- |
| `00_setup` | Catalog, schema, and storage access setup |
| `01_bronze` | Raw ingestion into Bronze Delta |
| `02_silver` | Cleaning, typing, standardization, and deduplication |
| `03_gold` | Dimensions, fact tables, and customer analytics outputs |
| `04_data_quality` | Schema, null, duplicate, and referential checks |
| `05_utilities` | Shared helper examples |

## Recommended Run Order

1. `00_setup/create_catalog_schema.py`
2. Bronze notebooks
3. Silver notebooks
4. DQ notebooks
5. Gold notebooks
6. SQL views

## Notebook Standards

- Use widgets for environment-specific values.
- Log row counts at every major step.
- Fail fast when required data is missing.
- Keep Bronze raw.
- Keep Silver clean and validated.
- Keep Gold business-friendly.

## Related Pages

- [Setup Guide](Setup-Guide)
- [Medallion Design](Medallion-Design)
- [Data Quality](Data-Quality)

