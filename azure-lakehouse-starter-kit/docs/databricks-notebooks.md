# Databricks Notebooks

## Purpose

Describe the Databricks notebook structure for the starter kit.

## Notebook Groups

| Folder | Purpose |
| --- | --- |
| `00_setup` | Catalog, schema, storage, and environment setup placeholders |
| `01_bronze` | Ingest raw files into Bronze Delta tables |
| `02_silver` | Clean, type, deduplicate, and quarantine bad records |
| `03_gold` | Build dimensions, facts, Customer 360, and summaries |
| `04_data_quality` | Execute reusable quality checks |
| `05_utilities` | Shared logging, config, Delta, and DQ helpers |

## Notebook Design Rules

- Accept parameters.
- Log row counts.
- Add audit columns.
- Keep one notebook focused on one responsibility.
- Write to Delta.
- Quarantine invalid records.
- Use merge for dimensions and upserts where appropriate.
