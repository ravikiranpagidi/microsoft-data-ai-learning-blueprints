# Naming Standards

> **Learning stage:** Enterprise readiness
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply naming standards to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [PII and Sensitive Data Handling](PII-and-Sensitive-Data-Handling) | [Home](Home) | [CI/CD and Deployment Strategy](CICD-and-Deployment-Strategy)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Provide practical naming standards for Fabric workspaces, Lakehouses, notebooks, pipelines, tables, columns, views, and environments.

## Who Should Read This

Contributors, engineers, architects, and teams preparing a reusable Fabric project structure.

## Why Naming Standards Matter

Clear names make projects easier to navigate, automate, secure, and support. Poor naming becomes expensive when a proof of concept grows into a team platform.

## Workspace Naming

Good: fabric-de-blueprint-dev, fabric-de-blueprint-test, fabric-de-blueprint-prod

Bad: testworkspace, ravisworkspace, finalfinalprod

## Lakehouse Naming

Good: lh_retail_banking_dev

Bad: lakehouse1, bankingdata, newlakehouse

## Notebook Naming

Use ordered, descriptive names:

- 00_setup_lakehouse
- 01_bronze_ingestion
- 02_silver_transformation
- 03_gold_dimensional_model

## Pipeline Naming

Use action and domain:

- pl_ingest_retail_banking_csv
- pl_orchestrate_retail_banking_medallion
- pl_refresh_powerbi_customer_analytics

## Table Naming

Use layer prefixes:

| Layer | Pattern | Example |
| --- | --- | --- |
| Bronze | bronze_entity | bronze_transactions |
| Silver | silver_entity | silver_transactions |
| Gold dimension | dim_entity | dim_customer |
| Gold fact | fact_process | fact_transaction |

## Column Naming

Use lower_snake_case for engineering tables. Avoid spaces in Lakehouse table columns. Power BI display names can be friendlier later.

## View Naming

Use purpose-driven prefixes:

- vw_dim_customer
- vw_fact_transaction
- vw_powerbi_customer_360
- vw_powerbi_executive_kpis

## Environment Naming

Use dev, test, and prod consistently. Do not mix environment names into business table names unless required. Prefer workspace or configuration-level environment separation.

## Best Practices

- Use names that reveal purpose and layer.
- Keep names stable once downstream users depend on them.
- Avoid personal names in shared assets.
- Document exceptions.
- Align file names and notebook names.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Vague names like final_table | No one knows ownership or purpose | Use layer and entity names. |
| Renaming assets often | Breaks downstream dependencies | Plan names before release. |
| Mixing naming styles | Hard to automate | Adopt one standard. |

## Related Repo Files

- [governance/naming-standards.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/governance/naming-standards.md)
- [notebooks/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/notebooks)
- [sql/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/sql)
- [cicd/environment-configuration.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/cicd/environment-configuration.md)

## Related Wiki Pages

- [Governance and Security](Governance-and-Security)
- [CI/CD and Deployment Strategy](CICD-and-Deployment-Strategy)
- [Performance and Optimization](Performance-and-Optimization)

## Summary Checklist

- [ ] Workspace names include project and environment.
- [ ] Tables use layer prefixes.
- [ ] Views use purpose-driven names.
- [ ] Notebook names are ordered and descriptive.
- [ ] Exceptions are documented.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [PII and Sensitive Data Handling](PII-and-Sensitive-Data-Handling) | [Home](Home) | [CI/CD and Deployment Strategy](CICD-and-Deployment-Strategy) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
