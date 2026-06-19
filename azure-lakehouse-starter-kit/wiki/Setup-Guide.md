# Setup Guide

## Purpose

Use this guide to run the starter kit in a development environment.

## Prerequisites

- Azure subscription
- Azure Data Lake Storage Gen2 account
- Azure Data Factory instance
- Azure Databricks workspace
- Unity Catalog enabled Databricks workspace
- Power BI Desktop or Power BI service access
- Git client
- Python 3.11 for local validation

## Step-by-Step Setup

1. Clone the repository.
2. Open `azure-lakehouse-starter-kit`.
3. Create a development ADLS Gen2 storage account.
4. Create containers or equivalent governed locations for `raw`, `bronze`, `silver`, `gold`, and `logs`.
5. Create or identify an Azure Databricks workspace.
6. Configure Unity Catalog storage credentials and external locations.
7. Run `databricks/notebooks/00_setup/create_catalog_schema.py`.
8. Upload files from `data/sample` into the raw landing path.
9. Run Bronze notebooks.
10. Run Silver notebooks.
11. Run DQ notebooks.
12. Run Gold notebooks.
13. Execute SQL views in `sql/views`.

## Local Validation

```bash
python -m compileall azure-lakehouse-starter-kit/databricks/notebooks azure-lakehouse-starter-kit/scripts
python azure-lakehouse-starter-kit/scripts/validate_notebooks.py
python -m pytest azure-lakehouse-starter-kit/tests
```

## Expected Output

- Bronze Delta tables for raw source data
- Silver Delta tables with clean, typed data
- Gold tables for `dim_customer`, `dim_product`, `fact_sales`, and `customer_360`
- SQL views for daily sales and customer 360
- Data quality results in `dq.dq_results`

## Troubleshooting

| Issue | Fix |
| --- | --- |
| Catalog creation fails | Check Unity Catalog permissions |
| Raw files not found | Verify the configured `raw_base_path` widget |
| Power BI cannot see tables | Confirm Gold tables are registered and permissions are granted |
| DQ checks fail | Inspect `dq.dq_results` and fix Silver data quality issues |

## Checklist

- [ ] Repository cloned.
- [ ] Azure resources available.
- [ ] Databricks widgets configured.
- [ ] Sample data uploaded.
- [ ] Validation tests pass.

## Related Pages

- [Architecture](Architecture)
- [Databricks Notebooks](Databricks-Notebooks)
- [Troubleshooting](Troubleshooting)

