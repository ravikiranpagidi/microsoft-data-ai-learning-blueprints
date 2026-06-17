# Files vs Tables in Fabric Lakehouse

> **Learning stage:** Foundation
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply files vs tables in fabric lakehouse to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Lakehouse vs Warehouse](Lakehouse-vs-Warehouse) | [Home](Home) | [Data Pipelines vs Notebooks](Data-Pipelines-vs-Notebooks)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain the difference between Files and Tables in a Fabric Lakehouse and how raw files become governed Delta tables.

## Who Should Read This

Beginners, Power BI developers, and data engineers who need a precise mental model for Lakehouse storage.

## Beginner Explanation

A Fabric Lakehouse has two important areas: Files and Tables. Files are raw or unmanaged files. Tables are managed Delta tables that Fabric can query and expose more reliably to analytics tools.

## Files Are Raw or Unmanaged

Files are useful for source data, landing zones, exports, and file-based staging. A CSV file in Files is not automatically a governed analytics table. It needs validation, typing, and transformation before business use.

## Tables Are Managed Delta Tables

Tables are created when Spark writes data using Delta table patterns such as saveAsTable. Tables carry structure, metadata, and are better suited for SQL, Power BI, and downstream reuse.

## When to Use Files

- Landing raw CSV extracts.
- Keeping source files for audit or replay.
- Storing reference files before transformation.
- Holding generated reports or non-table artifacts.

## When to Use Tables

- Bronze raw Delta tables with ingestion metadata.
- Silver cleaned and standardized datasets.
- Gold business-ready facts and dimensions.
- Data quality result tables.
- BI and SQL consumption layers.

## How Data Moves in This Repo

| Step | Area | Example |
| --- | --- | --- |
| Source landing | Files | Files/retail_banking/source/customers.csv |
| Bronze | Tables | bronze_customers |
| Silver | Tables | silver_customers |
| Gold | Tables | dim_customer, fact_transaction |
| Consumption | SQL views | vw_powerbi_customer_360 |

## Best Practices

- Keep raw files immutable when possible.
- Add ingestion metadata when promoting files to Bronze tables.
- Do not ask business users to report from raw Files.
- Use clear folder names for source, config, checkpoints, and reports.
- Use Delta tables for data that needs governance and reuse.

## Common Mistakes

| Mistake | Why it hurts | Better approach |
| --- | --- | --- |
| Treating CSV files as final data | Schema and quality are uncontrolled | Create Delta tables. |
| Deleting source files too early | Replay and audit are lost | Retain source or Bronze history based on policy. |
| Mixing configs with source data | Operational confusion | Use separate config folders. |

## Related Repo Files

- [sample-data/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/sample-data)
- [notebooks/01_bronze_ingestion.ipynb](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/notebooks/01_bronze_ingestion.ipynb)
- [docs/04-onelake-explained.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/docs/04-onelake-explained.md)

## Related Wiki Pages

- [OneLake Explained](OneLake-Explained)
- [Lakehouse Concepts](Lakehouse-Concepts)
- [Bronze Layer Design](Bronze-Layer-Design)
- [Silver Layer Design](Silver-Layer-Design)

## Summary Checklist

- [ ] I can explain Files versus Tables.
- [ ] I know why Bronze tables are created from source files.
- [ ] I know why business users should consume Gold tables or views.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Lakehouse vs Warehouse](Lakehouse-vs-Warehouse) | [Home](Home) | [Data Pipelines vs Notebooks](Data-Pipelines-vs-Notebooks) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
