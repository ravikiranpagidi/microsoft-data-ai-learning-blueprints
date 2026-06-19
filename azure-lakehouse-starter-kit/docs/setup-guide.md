# Setup Guide

## Purpose

This guide describes how to use the starter kit for local validation and Azure implementation planning.

## Azure Prerequisites

- Azure subscription.
- Azure Data Factory.
- ADLS Gen2 storage account.
- Azure Databricks workspace.
- Azure Key Vault.
- Optional Unity Catalog.
- Optional Microsoft Purview.

## Local Validation

```powershell
cd azure-lakehouse-starter-kit
python scripts/validate_notebooks.py
python -m pytest tests
```

## Suggested Azure Setup

1. Create resource group.
2. Create ADLS Gen2 storage account.
3. Create containers: `raw`, `bronze`, `silver`, `gold`, `quarantine`.
4. Create Azure Databricks workspace.
5. Create Azure Data Factory.
6. Create Key Vault and store connection details.
7. Configure managed identities or service principals.
8. Import or deploy ADF artifacts from `adf/`.
9. Import Databricks notebooks from `databricks/notebooks/`.
10. Configure Databricks job from `databricks/jobs/lakehouse_workflow.json`.

## Environment Naming

| Environment | Example |
| --- | --- |
| Dev | `rg-adls-retail-dev` |
| Test | `rg-adls-retail-test` |
| Prod | `rg-adls-retail-prod` |

## Expected Outputs

- Raw files landed in ADLS.
- Bronze Delta tables created.
- Silver tables cleansed and validated.
- Gold tables available for reporting.
- Data quality results logged.
