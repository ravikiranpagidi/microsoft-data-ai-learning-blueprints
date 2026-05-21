# End-to-End Project Walkthrough

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply end-to-end project walkthrough to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Dataflow Gen2 vs Notebook vs Pipeline](Dataflow-Gen2-vs-Notebook-vs-Pipeline) | [Home](Home) | [Retail Banking Sample Domain](Retail-Banking-Sample-Domain)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Walk through the complete Retail Banking Customer Analytics implementation from source files to Power BI-ready outputs.

## Who Should Read This

Learners who want to understand the full project before diving into individual layer design pages.

## Business Problem

The fictional retail bank wants trusted analytics for customers, accounts, products, branches, and transactions. Business users need to answer questions about active customers, product usage, transaction volume, high-activity branches, customer segments, balances, and accounts that need deeper analysis.

## Source Data

The project starts with five CSV files: customers, accounts, products, branches, and transactions. These files simulate extracts from operational banking systems.

## Ingestion

The ingestion pattern lands files in the Lakehouse Files area and creates Bronze Delta tables. Bronze preserves the source structure and adds metadata such as ingestion timestamp, source file name, source entity, and batch ID.

## Bronze

Bronze is the replayable raw layer. The goal is not to make the data perfect. The goal is to capture what arrived and make it auditable.

## Silver

Silver cleans and conforms data. It casts dates and numeric values, standardizes status fields, removes duplicates, validates business keys, and creates quarantine tables when records fail validation.

## Gold

Gold creates business-ready dimensions and facts. In this repo, Gold includes dim_customer, dim_account, dim_product, dim_branch, dim_date, and fact_transaction. This layer supports SQL views and Power BI semantic modeling.

## SQL Views

SQL scripts create business-friendly views for transaction detail, customer 360, product usage, branch activity, executive KPIs, and validation. These views help SQL users and Power BI developers work with understandable names.

## Power BI

Power BI should consume the Gold model or governed SQL views. The semantic model should define relationships, measures, hierarchies, and business-friendly naming.

## Governance and CI/CD

The project includes governance docs, naming standards, role-based access guidance, data quality rules, release checklists, and Dev/Test/Prod strategy. Treat these as required production thinking, not optional extras.

## Expected Final Outcome

At the end, users should have a complete beginner-friendly but enterprise-shaped data engineering project that can be demonstrated in a portfolio, interview, meetup, or proof of concept.

## Implementation Steps

1. Set up workspace and Lakehouse.
2. Upload sample CSV files.
3. Run notebooks 00 through 06.
4. Run SQL scripts in the SQL Analytics Endpoint.
5. Build or document a Power BI semantic model.
6. Review data quality, governance, and CI/CD readiness.

## Related Repo Files

- [notebooks/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/notebooks)
- [sql/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/sql)
- [sample-data/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/sample-data)
- [governance/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/governance)
- [cicd/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/cicd)

## Related Wiki Pages

- [Retail Banking Sample Domain](Retail-Banking-Sample-Domain)
- [Medallion Architecture](Medallion-Architecture)
- [Building Dimensions and Facts](Building-Dimensions-and-Facts)
- [Semantic Model Design](Semantic-Model-Design)

## Summary Checklist

- [ ] I can describe the project from source CSV to dashboard.
- [ ] I know which layer performs each responsibility.
- [ ] I know the expected Gold tables and SQL outputs.
- [ ] I understand that governance and CI/CD are part of the project, not afterthoughts.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Dataflow Gen2 vs Notebook vs Pipeline](Dataflow-Gen2-vs-Notebook-vs-Pipeline) | [Home](Home) | [Retail Banking Sample Domain](Retail-Banking-Sample-Domain) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
