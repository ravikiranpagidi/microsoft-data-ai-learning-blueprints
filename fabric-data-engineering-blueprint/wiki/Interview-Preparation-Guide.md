# Interview Preparation Guide

> **Learning stage:** Decision, career, and community
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Practice natural, scenario-ready answers using the project as evidence.
> **Navigate:** [Real-World Architecture Patterns](Real-World-Architecture-Patterns) | [Home](Home) | [30-Day Learning Plan](30-Day-Learning-Plan)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Provide interview-ready Microsoft Fabric Data Engineering questions, answers, scenario prompts, and hands-on tasks.

## Who Should Read This

Students, job seekers, career switchers, mentors, and interviewers preparing Fabric Data Engineering discussions.

## How to Use This Guide

Practice answering out loud. Good interview answers are direct first, then practical. Avoid reciting definitions without explaining how you would apply them.

## Beginner Questions

### What is Microsoft Fabric?

Strong answer: Microsoft Fabric is a unified analytics platform that brings data engineering, data factory, data warehouse, real-time analytics, data science, and Power BI together around OneLake and shared workspaces. In a data engineering project, I would use it to ingest data, transform it with notebooks or dataflows, store it in Lakehouse tables, and expose curated data to Power BI.

Follow-up: How is Fabric different from using separate Azure services?

### What is OneLake?

Strong answer: OneLake is the logical data lake built into Fabric. It gives Fabric items a shared storage foundation and helps reduce unnecessary copies. In a Lakehouse, I use Files for raw source files and Tables for managed Delta tables.

Follow-up: When would you use a shortcut instead of copying data?

### What is a Lakehouse?

Strong answer: A Lakehouse combines data lake flexibility with table-based analytics. In Fabric, it supports Files, Tables, Spark notebooks, SQL Analytics Endpoint, and Power BI consumption.

Follow-up: How do Files and Tables differ?

## Intermediate Questions

### Why use medallion architecture?

Strong answer: Medallion architecture separates raw, cleaned, and business-ready data into Bronze, Silver, and Gold layers. This improves auditability, quality, reuse, and trust. I would keep Bronze raw, standardize and validate Silver, and build facts and dimensions in Gold.

Follow-up: What should not happen in Bronze?

### When should you use a notebook instead of a pipeline?

Strong answer: I use pipelines for orchestration and notebooks for transformation. If I need scheduling, dependencies, copy, and retries, I use a pipeline. If I need PySpark logic, deduplication, joins, data quality, or dimensional modeling, I use a notebook.

Follow-up: How would you pass parameters from a pipeline to a notebook?

### Why build a Gold star schema?

Strong answer: A Gold star schema gives Power BI and SQL users clear facts, dimensions, relationships, and measures. It reduces report-level transformation and makes metrics easier to govern.

Follow-up: What is the grain of fact_transaction in this repo?

## Scenario Questions

### Scenario: Business users are reporting directly from Bronze. What do you do?

Strong answer: I would stop treating Bronze as a consumption layer, explain that Bronze is raw and may contain sensitive or inconsistent data, then provide Gold tables or governed SQL views. I would also review access permissions and document the approved consumption path.

### Scenario: Silver has duplicate customer IDs. What do you do?

Strong answer: I would identify duplicate patterns, apply a deterministic deduplication rule, quarantine questionable records, add a duplicate_key rule to dq_rules.yml, and validate downstream dimensions after the fix.

### Scenario: A report has wrong transaction totals. Where do you investigate?

Strong answer: I would check fact grain, duplicate joins, posted versus rejected transaction filtering, measure definition, and whether a wide SQL view is duplicating balances or amounts. Then I would reconcile totals with SQL validation queries.

## Architecture Questions

- How would you design Dev/Test/Prod workspaces?
- How would you handle PII in a customer analytics model?
- When would you choose Warehouse instead of Lakehouse?
- How would you document a major architecture decision?
- How would you make the Lakehouse AI-ready?

## Hands-On Tasks

1. Upload the five sample CSV files and run notebooks 00 through 06.
2. Add a new data quality rule for transaction_channel.
3. Write a SQL query for top branches by posted transaction amount.
4. Explain the fact_transaction grain and relationships.
5. Create a mock Power BI measure list.
6. Write an ADR for choosing Direct Lake or Import mode.

## Best Practices for Interview Answers

- Start with a clear answer.
- Add a practical example.
- Mention tradeoffs.
- Include governance and quality where relevant.
- Avoid claiming one Fabric item is always the answer.

## Answer Formula

Use this structure for interview answers:

1. Direct answer: choose the concept or tool.
2. Reason: explain why it fits the workload.
3. Example: connect it to the Retail Banking blueprint.
4. Tradeoff: mention when you would choose differently.
5. Governance: include quality, access, or deployment if relevant.

## Scoring Rubric for Your Answers

| Level | What the answer sounds like |
| --- | --- |
| Beginner | Defines the term correctly. |
| Practitioner | Explains how it is used in the repo. |
| Job-ready | Adds tradeoffs, validation, governance, and production concerns. |
| Senior | Connects the decision to ownership, scale, cost, security, and maintainability. |

## Retail Banking Scenario Practice

| Scenario | What a strong answer should include |
| --- | --- |
| A branch manager wants transaction trends by month | Gold fact grain, dim_date, branch dimension, posted transaction filter, Power BI measure. |
| A data steward finds duplicate account IDs | Silver duplicate check, quarantine pattern, DQ rule, downstream validation. |
| A Power BI developer asks for direct access to Bronze | Explain raw data risk and provide Gold or governed SQL view. |
| A platform owner asks about Dev/Test/Prod | Separate workspaces, parameterization, release checklist, DQ before promotion. |
| A security reviewer asks about customer email | PII classification, least privilege, masking or hiding in semantic model. |

## Mock Interview Prompt

Walk me through the project in five minutes.

Strong structure:

- The business problem is Retail Banking Customer Analytics.
- Source CSVs land in Lakehouse Files.
- Bronze captures raw data with ingestion metadata.
- Silver cleans and validates business keys.
- Gold builds dimensions and fact_transaction.
- SQL views and Power BI semantic model expose trusted metrics.
- Governance, DQ, CI/CD, and ADRs make the project enterprise-ready.

## Related Repo Files

- [interview-guide/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/interview-guide)
- [roadmap/30-day-learning-plan.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/roadmap/30-day-learning-plan.md)
- [roadmap/90-day-fabric-data-engineer-growth-plan.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/roadmap/90-day-fabric-data-engineer-growth-plan.md)
- [README.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/README.md)

## Related Wiki Pages

- [Glossary](Glossary)
- [30-Day Learning Plan](30-Day-Learning-Plan)
- [90-Day Professional Growth Plan](90-Day-Professional-Growth-Plan)
- [Fabric Decision Guide](Fabric-Decision-Guide)

## Summary Checklist

- [ ] I can answer beginner Fabric questions clearly.
- [ ] I can explain scenario-based decisions.
- [ ] I can discuss governance and data quality in interviews.
- [ ] I have practiced at least three hands-on tasks.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Real-World Architecture Patterns](Real-World-Architecture-Patterns) | [Home](Home) | [30-Day Learning Plan](30-Day-Learning-Plan) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
