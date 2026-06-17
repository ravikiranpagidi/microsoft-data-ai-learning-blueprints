# FAQ

> **Learning stage:** Decision, career, and community
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Resolve common beginner and practitioner questions quickly.
> **Navigate:** [Contributor Guide](Contributor-Guide) | [Home](Home) | [Glossary](Glossary)
> **Quick links:** [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Answer common questions about Fabric, Lakehouse, Warehouse, OneLake, notebooks, pipelines, Power BI, data quality, governance, CI/CD, learning, and repo usage.

## Who Should Read This

All readers, especially beginners and contributors looking for quick answers.

## FAQ by Topic

Use this FAQ as a quick help desk. If an answer feels too short, follow the related Wiki link for the full guide.

### Fabric Basics

#### 1. What is Microsoft Fabric?

Microsoft Fabric is a unified analytics platform for data engineering, integration, warehousing, real-time analytics, data science, and Power BI. In this blueprint, it provides the workspace, Lakehouse, notebooks, SQL endpoint, and Power BI consumption path.

#### 2. Why should a data engineer learn Fabric?

Fabric brings engineering, orchestration, lakehouse storage, SQL access, and BI consumption into one integrated platform. A data engineer who understands these pieces can build practical analytics products faster and with clearer governance.

#### 3. How is Fabric different from traditional Azure data platforms?

Traditional Azure solutions often combine separate services such as ADLS, ADF, Synapse, Databricks, and Power BI. Fabric unifies many of those experiences around OneLake and workspace items, while still requiring good architecture and governance.

#### 4. Is Fabric only for Power BI users?

No. Power BI is important, but Fabric also includes Data Engineering, Data Factory, Warehouse, Real-Time Intelligence, Data Science, and related experiences.

#### 5. Do I need to know Azure before learning Fabric?

Azure knowledge helps, especially around data lakes and security, but beginners can learn Fabric directly by following the Lakehouse and notebook flow in this repo.

### OneLake and Lakehouse

#### 1. What is OneLake?

OneLake is the logical data lake built into Fabric. It helps Fabric workloads share data through a common storage foundation.

#### 2. What is a Lakehouse?

A Lakehouse is a Fabric item with Files and Tables areas. It supports raw file landing, Delta tables, Spark notebooks, SQL endpoint access, and Power BI consumption.

#### 3. What is the difference between Files and Tables?

Files are raw or unmanaged objects such as CSV files. Tables are managed Delta tables with metadata and better analytics support.

#### 4. Why does the repo upload CSV files into Files first?

That mirrors a common ingestion pattern: land source extracts first, then transform them into Bronze Delta tables with metadata.

#### 5. Should business users query Files directly?

Usually no. Business users should consume Gold tables, SQL views, or semantic models because those assets are cleaner and governed.

### Engineering Choices

#### 1. When should I use a notebook?

Use a notebook for PySpark transformations, data quality checks, deduplication, joins, dimensional modeling, and logic that benefits from code review.

#### 2. When should I use a pipeline?

Use a pipeline for orchestration: copy activities, scheduling, retries, dependencies, and running notebooks in sequence.

#### 3. When should I use Dataflow Gen2?

Use Dataflow Gen2 for low-code transformation and Power Query style shaping, especially when business analysts participate in data preparation.

#### 4. Lakehouse or Warehouse?

Use Lakehouse for file-based, Spark-heavy, medallion architecture projects. Use Warehouse for SQL-first relational warehouse workloads.

#### 5. Shortcut or copy?

Use shortcuts when you can reference governed data without duplication. Copy when you need an isolated snapshot, transformation boundary, or retention policy.

### Medallion and Modeling

#### 1. What is medallion architecture?

It is a layered design: Bronze for raw data, Silver for cleaned and conformed data, and Gold for business-ready analytics.

#### 2. What belongs in Bronze?

Raw source fields plus ingestion metadata such as batch ID, source file name, and ingestion timestamp.

#### 3. What belongs in Silver?

Cleaned, typed, deduplicated, standardized data with business key and referential validation.

#### 4. What belongs in Gold?

Business-ready facts, dimensions, consumption views, and metric-ready structures.

#### 5. What is the grain of fact_transaction?

One row per transaction event. This grain matters because transaction counts and amounts must be aggregated at the right level.

#### 6. Why use a star schema?

A star schema gives Power BI and SQL users clear facts, dimensions, relationships, and filter paths.

### SQL and Power BI

#### 1. What is SQL Analytics Endpoint?

It is the SQL query surface for Lakehouse Delta tables. Use it for querying, validation, and views over Lakehouse data.

#### 2. Can SQL Analytics Endpoint update Lakehouse tables?

For Lakehouse tables it is primarily a read-only query surface. Use supported write patterns such as Spark notebooks for table creation and updates.

#### 3. How should Power BI consume this project?

Power BI should consume the Gold star schema or governed SQL views through a semantic model with defined relationships and measures.

#### 4. What is Direct Lake?

Direct Lake is a Power BI mode designed to analyze Fabric Delta data without importing a separate copy, subject to model and feature considerations.

#### 5. Do I still need a semantic model?

Yes. The semantic model defines business names, relationships, measures, hierarchies, and report-ready meaning.

#### 6. Should I do transformations in Power BI?

Keep heavy cleansing and modeling in Fabric notebooks and Gold tables. Use Power BI for semantic modeling, measures, and reports.

### Data Quality and Governance

#### 1. Why use data quality rules?

They catch nulls, duplicates, invalid values, broken references, reconciliation issues, and freshness problems before reporting.

#### 2. Where are data quality rules stored?

Rules are stored in data-quality/dq_rules.yml and executed by data-quality/dq_framework.py and notebook 04.

#### 3. What should fail a pipeline?

Critical failures such as duplicate business keys, missing required IDs, broken referential integrity, or Silver-to-Gold reconciliation mismatches.

#### 4. What is PII in this project?

Names, email, phone, date of birth, customer identifiers, and financial transactions can be sensitive in a banking context.

#### 5. Who should access Bronze?

Usually data engineers and trusted troubleshooting roles, not broad business audiences.

#### 6. What is least privilege?

Users get only the access needed for their role, such as business users consuming semantic models rather than raw tables.

### CI/CD and Repo Usage

#### 1. What is Dev/Test/Prod in Fabric?

It is an environment strategy that separates building, validation, and production consumption across workspaces.

#### 2. What should be version controlled?

Notebooks, SQL scripts, DQ rules, documentation, ADRs, pipeline templates, and release checklists where supported.

#### 3. What should not be version controlled?

Secrets, tokens, production data extracts, credentials, and personal local configuration.

#### 4. Why are ADRs included?

ADRs explain why architecture choices were made, such as using medallion architecture or a Gold star schema.

#### 5. How do I become job-ready with this repo?

Run the project, extend it, explain decisions, practice scenarios, and turn your work into a portfolio story.

#### 6. How can I contribute?

Improve docs, add examples, extend notebooks, add SQL metrics, improve DQ rules, or add architecture and interview content.

## Best Practices for Using the FAQ

- Start here when a term, tool choice, or run step feels unclear.
- Use the Decision Guide when the question is about choosing between Fabric items.
- Use the Glossary when you need a short definition.
- Use the Interview Guide when you need a scenario-ready answer.
- Add a new FAQ entry when contributors ask the same question more than once.

## Related Repo Files

- [README.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/README.md)
- [docs/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/docs)
- [notebooks/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/notebooks)
- [community/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/community)

## Related Wiki Pages

- [Home](Home)
- [Fabric Decision Guide](Fabric-Decision-Guide)
- [Interview Preparation Guide](Interview-Preparation-Guide)
- [Glossary](Glossary)

## Summary Checklist

- [ ] I reviewed the common questions.
- [ ] I followed related pages for deeper topics.
- [ ] I know where to suggest new FAQ entries.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Contributor Guide](Contributor-Guide) | [Home](Home) | [Glossary](Glossary) |

Helpful references: [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
