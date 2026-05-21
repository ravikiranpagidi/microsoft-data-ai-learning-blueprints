# Getting Started

> **Learning stage:** Foundation
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Run the project safely in a Fabric workspace and know what output to expect.
> **Navigate:** [Home](Home) | [Home](Home) | [Microsoft Fabric Fundamentals](Microsoft-Fabric-Fundamentals)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Help a new user set up Microsoft Fabric, upload the sample data, run the notebooks, execute SQL scripts, and validate the expected outputs.

## Who Should Read This

Anyone who wants to run the project hands-on, especially beginners who have never created a Fabric Lakehouse before.

## Prerequisites

You need access to a Microsoft Fabric tenant and a workspace where you can create or use a Lakehouse, notebooks, pipelines, and Power BI items. You should also have GitHub access to this repository and basic familiarity with CSV files, SQL, and notebooks.

## Required Fabric Access

Ask your Fabric administrator for:

- Workspace access with permission to create Lakehouse, Notebook, Pipeline, and Power BI artifacts.
- Capacity access if your organization requires assigned capacity.
- Permission to upload files into the Lakehouse Files area.
- Permission to create and query Delta tables.

## Workspace Setup

1. Open Microsoft Fabric.
2. Create or select a workspace for learning.
3. Use a name that clearly identifies the environment, for example fabric-de-blueprint-dev.
4. Confirm the workspace has a Fabric capacity assigned if required by your tenant.
5. Keep this learning workspace separate from production workspaces.

## Lakehouse Setup

1. In the workspace, create a Lakehouse.
2. Use a clear name such as lh_retail_banking_dev.
3. Attach that Lakehouse to each notebook when running the project.
4. Use the Files area for raw CSV uploads.
5. Let the notebooks create the managed Delta tables in the Tables area.

## Uploading Sample Data

Upload these files from the sample-data folder into Files/retail_banking/source:

- customers.csv
- accounts.csv
- products.csv
- branches.csv
- transactions.csv

The expected Lakehouse path is Files/retail_banking/source. If you use a different path, update the path constants in the notebooks.

## Running Notebooks

Run the notebooks in this order:

| Order | Notebook | Purpose |
| ---: | --- | --- |
| 1 | 00_setup_lakehouse | Validate paths and helper functions. |
| 2 | 01_bronze_ingestion | Read CSV files and create Bronze tables. |
| 3 | 02_silver_transformation | Clean, type, deduplicate, and validate records. |
| 4 | 03_gold_dimensional_model | Build dimensions and fact table. |
| 5 | 04_data_quality_checks | Run rule-driven quality checks. |
| 6 | 05_delta_optimization | Inspect and optimize Delta tables. |
| 7 | 06_powerbi_ready_views | Validate Power BI-ready reporting shapes. |

## Running SQL Scripts

After Gold tables exist, open the Lakehouse SQL Analytics Endpoint and run:

1. create_gold_views.sql
2. validation_queries.sql
3. business_metrics.sql
4. powerbi_consumption_views.sql

## Expected Outputs

You should see Bronze tables, Silver tables, Gold dimensions, fact_transaction, data quality results, and Power BI-ready SQL views. The final model should answer customer, account, branch, product, and transaction questions.

## Troubleshooting Beginner Issues

| Issue | Likely cause | Fix |
| --- | --- | --- |
| File not found | CSV files uploaded to the wrong folder | Confirm Files/retail_banking/source path. |
| Table does not exist | Previous notebook did not run | Run notebooks in order. |
| Permission error | Workspace role is too limited | Ask admin for contributor-level access in learning workspace. |
| SQL view fails | Gold tables not created yet | Run notebook 03 first. |
| Power BI cannot see columns | Semantic model not refreshed | Refresh or recreate the semantic model after table changes. |

## Ten-Minute Sanity Check

Before running the full project, confirm these basics:

| Check | Expected result |
| --- | --- |
| Workspace exists | You can open the Fabric workspace without permission errors. |
| Lakehouse exists | A Lakehouse is attached to the notebooks. |
| Source files uploaded | Five CSV files are visible under Files/retail_banking/source. |
| Notebook 00 runs | Source readiness shows READY for each entity. |
| You know the run order | 00 -> 01 -> 02 -> 03 -> 04 -> 05 -> 06. |

## Expected Tables After Each Stage

| Stage | Tables or views you should see |
| --- | --- |
| Bronze ingestion | bronze_customers, bronze_accounts, bronze_products, bronze_branches, bronze_transactions, bronze_ingestion_audit |
| Silver transformation | silver_customers, silver_accounts, silver_products, silver_branches, silver_transactions, optional quarantine tables |
| Gold model | dim_customer, dim_account, dim_product, dim_branch, dim_date, fact_transaction |
| Data quality | dq_results |
| SQL consumption | vw_dim_customer, vw_fact_transaction, vw_powerbi_customer_360, vw_powerbi_executive_kpis, and related views |

## Beginner Recovery Tips

| Symptom | Quick recovery |
| --- | --- |
| Notebook cannot find a file | Re-check the Lakehouse Files path and file names. |
| Silver notebook fails on missing Bronze table | Run notebook 01 again and confirm Bronze table counts. |
| Gold notebook has missing keys | Review Silver referential checks and quarantine tables. |
| SQL view creation fails | Confirm Gold notebook completed and SQL endpoint metadata refreshed. |
| Power BI model looks confusing | Start from Gold star schema before using wide views. |

## Related Repo Files

- [sample-data/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/sample-data)
- [notebooks/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/notebooks)
- [sql/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/sql)
- [data-quality/dq_rules.yml](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/data-quality/dq_rules.yml)

## Related Wiki Pages

- [Home](Home)
- [Microsoft Fabric Fundamentals](Microsoft-Fabric-Fundamentals)
- [End-to-End Project Walkthrough](End-to-End-Project-Walkthrough)
- [Governance and Security](Governance-and-Security)

## Summary Checklist

- [ ] I have a Fabric workspace ready.
- [ ] I created or selected a Lakehouse.
- [ ] I uploaded all five CSV files to the expected source folder.
- [ ] I can run notebooks 00 through 06 in order.
- [ ] I can run SQL scripts after Gold tables exist.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Home](Home) | [Home](Home) | [Microsoft Fabric Fundamentals](Microsoft-Fabric-Fundamentals) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
