# Glossary

> **Learning stage:** Decision, career, and community
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Use consistent Fabric, lakehouse, modeling, governance, and CI/CD terms.
> **Navigate:** [FAQ](FAQ) | [Home](Home) | End of Wiki
> **Quick links:** [FAQ](FAQ) | [Contributor Guide](Contributor-Guide)

## Purpose

Define common Microsoft Fabric, Lakehouse, data engineering, governance, and CI/CD terms used throughout the repo and Wiki.

## Who Should Read This

Beginners, interview candidates, contributors, and anyone who wants consistent terminology.

## How Terms Connect in This Blueprint

The Retail Banking sample starts with CSV files in Lakehouse Files. Notebooks create Bronze, Silver, and Gold Delta tables. Gold tables form a star schema with dimensions and fact_transaction. SQL Analytics Endpoint exposes views, while Power BI semantic models define measures and business-friendly consumption. Governance, data quality, CI/CD, and ADRs make the project credible beyond a demo.

## Terms by Category

### Fabric Platform

| Term | Definition |
| --- | --- |
| Microsoft Fabric | Unified analytics platform for data engineering, data integration, warehousing, real-time analytics, data science, and Power BI. |
| Workspace | Collaboration and security boundary that contains Fabric items such as Lakehouses, notebooks, pipelines, and reports. |
| Capacity | Compute resources assigned to run Fabric workloads. |
| OneLake | The logical data lake built into Fabric and shared across Fabric workloads. |
| Shortcut | A reference to data stored elsewhere that can reduce copying when ownership and access are clear. |

### Data Engineering Items

| Term | Definition |
| --- | --- |
| Lakehouse | Fabric item with Files and Tables areas for lake-based analytics. |
| Warehouse | SQL-first Fabric item for relational warehouse workloads. |
| Notebook | Interactive code artifact used for PySpark, SQL, documentation, and data engineering logic. |
| Spark | Distributed compute engine used for scalable data processing. |
| Data Pipeline | Orchestration artifact for copy, scheduling, dependencies, and activity execution. |
| Dataflow Gen2 | Low-code data preparation experience based on Power Query concepts. |

### Lakehouse Storage and Layers

| Term | Definition |
| --- | --- |
| Files | Raw or unmanaged file area in a Lakehouse, used in this repo for CSV source files. |
| Tables | Managed Delta table area in a Lakehouse, used for Bronze, Silver, Gold, and DQ outputs. |
| Delta Table | Reliable table format over data lake storage with transaction log and schema support. |
| Medallion Architecture | Layered architecture using Bronze, Silver, and Gold data layers. |
| Bronze Layer | Raw or lightly enriched layer that preserves source data and ingestion metadata. |
| Silver Layer | Cleaned, typed, deduplicated, and validated data layer. |
| Gold Layer | Business-ready layer for facts, dimensions, SQL views, and semantic consumption. |

### Modeling and BI

| Term | Definition |
| --- | --- |
| Fact Table | Table containing measurable business events at a defined grain. In this repo, fact_transaction has one row per transaction. |
| Dimension Table | Descriptive table used to filter, group, and explain facts, such as dim_customer or dim_product. |
| Surrogate Key | Generated key used for stable relationships in dimensional models. |
| Business Key | Natural source or business identifier, such as customer_id or account_id. |
| SQL Analytics Endpoint | SQL query surface for Lakehouse Delta tables. |
| Semantic Model | Power BI business model with relationships, measures, names, and metadata. |
| Direct Lake | Power BI mode for analyzing Fabric Delta data without importing a separate copy. |
| Measure | Reusable calculation in a semantic model, such as Total Transaction Amount. |

### Governance and Delivery

| Term | Definition |
| --- | --- |
| Data Quality | Practices and checks that ensure data is complete, valid, unique, fresh, and reliable. |
| Data Governance | Ownership, policies, access, definitions, and processes that make data trustworthy. |
| PII | Personally identifiable information such as names, emails, phone numbers, and date of birth. |
| RBAC | Role-based access control, where permissions are assigned by user role. |
| CI/CD | Continuous integration and delivery practices for controlled change and release. |
| Deployment Pipeline | Fabric capability for promoting content across environments. |
| Git Integration | Version-control integration for supported Fabric artifacts and collaboration workflows. |
| ADR | Architecture Decision Record documenting a meaningful design decision and its tradeoffs. |

## How to Extend the Glossary

When adding a new term, keep the definition short, practical, and connected to this repo. If a term affects business meaning, also update the business glossary in the semantic-model folder.

## Best Practices

- Use consistent terms across README, docs, Wiki, and semantic model.
- Define business metrics separately from technical platform terms.
- Link glossary terms from beginner pages when useful.
- Prefer project-specific examples over abstract definitions.

## Related Repo Files

- [semantic-model/business_glossary.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/semantic-model/business_glossary.md)
- [docs/15-learning-resources.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/docs/15-learning-resources.md)
- [README.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/README.md)

## Related Wiki Pages

- [Microsoft Fabric Fundamentals](Microsoft-Fabric-Fundamentals)
- [Power BI Consumption Guide](Power-BI-Consumption-Guide)
- [Interview Preparation Guide](Interview-Preparation-Guide)
- [FAQ](FAQ)

## Summary Checklist

- [ ] I can define the core Fabric terms.
- [ ] I understand medallion and dimensional modeling vocabulary.
- [ ] I know where to add business-specific glossary terms.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [FAQ](FAQ) | [Home](Home) | End of Wiki |

Helpful references: [FAQ](FAQ) | [Contributor Guide](Contributor-Guide)
