# Fabric Decision Guide

> **Learning stage:** Decision, career, and community
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Make practical tool and architecture choices with clear tradeoffs.
> **Navigate:** [Architecture Decision Records Guide](Architecture-Decision-Records-Guide) | [Home](Home) | [Real-World Architecture Patterns](Real-World-Architecture-Patterns)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Provide practical decision matrices for common Microsoft Fabric architecture choices.

## Who Should Read This

Architects, data engineers, Power BI developers, and interview candidates who need clear tool-selection reasoning.

## How to Use This Guide

Use these matrices when designing or reviewing a Fabric project. The goal is not to declare one option always best. The goal is to choose intentionally.

## Lakehouse vs Warehouse

| Choice | Use when | Avoid when | Best persona | Example scenario |
| --- | --- | --- | --- | --- |
| Lakehouse | You need files, Spark, Delta, medallion layers | Team is SQL-only and wants warehouse-first modeling | Data engineer | CSV to Bronze/Silver/Gold with PySpark |
| Warehouse | You need SQL-first relational warehouse patterns | You need raw file processing and Spark-heavy logic | SQL developer | Curated sales mart built with T-SQL |

## Notebook vs Pipeline

| Choice | Use when | Avoid when | Best persona | Example scenario |
| --- | --- | --- | --- | --- |
| Notebook | Complex transformations, PySpark, DQ, modeling | Simple copy or orchestration only | Data engineer | Build Silver and Gold tables |
| Pipeline | Scheduling, copy, dependencies, retries | Complex transformation code | Integration engineer | Run Bronze -> Silver -> Gold notebooks nightly |

## Dataflow Gen2 vs Notebook

| Choice | Use when | Avoid when | Best persona | Example scenario |
| --- | --- | --- | --- | --- |
| Dataflow Gen2 | Low-code shaping and Power Query style prep | Complex Spark logic and engineering controls | Analyst, citizen developer | Clean a small reference dataset |
| Notebook | Code-heavy transformations and validation | Simple visual transformations are enough | Data engineer | Deduplicate transactions and build dimensions |

## Shortcut vs Copy

| Choice | Use when | Avoid when | Best persona | Example scenario |
| --- | --- | --- | --- | --- |
| Shortcut | You want to reference existing data without duplication | Source ownership, access, or SLA is unclear | Architect | Reuse enterprise customer master data |
| Copy | You need isolated snapshot, transformation, or retention | Copying creates unnecessary duplication | Data engineer | Land external CSV files for processing |

## Gold Table vs SQL View

| Choice | Use when | Avoid when | Best persona | Example scenario |
| --- | --- | --- | --- | --- |
| Gold table | Data is a durable business entity or fact | Logic is only presentation-specific | Data engineer | fact_transaction |
| SQL view | You need reusable consumption shape or aliasing | It hides bad modeling or huge complexity | SQL analyst, BI developer | vw_powerbi_customer_360 |

## Star Schema vs Wide Table

| Choice | Use when | Avoid when | Best persona | Example scenario |
| --- | --- | --- | --- | --- |
| Star schema | Governed BI, reusable dimensions, clear metrics | One-off export is the only need | BI modeler | Customer analytics semantic model |
| Wide table | Simple extract or narrow ad hoc use | Enterprise semantic model or many relationships | Analyst | Temporary analysis dataset |

## Direct Lake vs Import Mode

| Choice | Use when | Avoid when | Best persona | Example scenario |
| --- | --- | --- | --- | --- |
| Direct Lake | Data is in Fabric Delta tables and model design supports it | You need features or transformations better suited to import | BI architect | Large Gold table semantic model |
| Import | You need isolated model copy, transformations, or compatibility | Data volume and refresh cost become too high | BI developer | Small curated departmental report |

## Decision Flow

~~~mermaid
flowchart TD
    A[Start with business question] --> B{Raw files or Spark-heavy engineering?}
    B -->|Yes| C[Lakehouse]
    B -->|No| D{SQL-first warehouse pattern?}
    D -->|Yes| E[Warehouse]
    D -->|No| F[Evaluate consumer and governance needs]
    C --> G{Complex transformations?}
    G -->|Yes| H[Notebook]
    G -->|No| I[Dataflow Gen2 or Pipeline]
    H --> J[Gold star schema]
    J --> K[Power BI semantic model]
~~~

## Best Practices

- Document major choices with ADRs.
- Revisit decisions as requirements mature.
- Choose based on workload, not preference.
- Keep consumption needs visible during engineering design.

## Decision Questions to Ask First

Before choosing a Fabric item, ask these questions in order:

1. What business question or operational outcome must this solve?
2. Is the data raw, cleaned, or business-ready?
3. Who owns the data and who consumes it?
4. Does the logic need code review, low-code shaping, or orchestration?
5. Does the output need to be reused by Power BI, SQL users, AI, or another data product?
6. What are the security, PII, and lifecycle requirements?
7. How will this move from Dev to Test to Prod?

## Retail Banking Examples

| Decision | Example in this repo | Why it fits |
| --- | --- | --- |
| Lakehouse | Retail Banking CSV to Delta tables | The project starts with files and uses PySpark transformations. |
| Notebook | Silver cleaning and Gold modeling | The logic includes casting, deduplication, joins, and surrogate keys. |
| Pipeline | End-to-end orchestration | A pipeline can run ingestion, transformation, DQ, and refresh steps. |
| SQL view | Customer 360 and executive KPIs | Views make common consumption shapes reusable for SQL and Power BI users. |
| Star schema | dim_customer plus fact_transaction | BI users need clear dimensions, measures, and filter paths. |
| Direct Lake | Gold Delta model for Power BI | The curated model lives in Fabric Delta tables. |

## Red Flags

| Red flag | What it usually means |
| --- | --- |
| Every problem is solved with a notebook | Orchestration and operational monitoring may be missing. |
| Every problem is solved with a pipeline | Complex logic may be hidden in visual activities. |
| Power BI does most cleansing | Engineering and governance layers are too weak. |
| A wide table is used for every report | The semantic model may become hard to maintain. |
| Lakehouse and Warehouse both contain the same truth | Ownership and source-of-truth decisions are unclear. |

## Interview-Ready Framing

A strong answer usually sounds like this: I would choose the tool based on the workload. For this Retail Banking blueprint, I use Lakehouse and notebooks because the project starts with source files and needs PySpark transformations. I use pipelines for orchestration, SQL views for governed consumption, and a Power BI semantic model for business measures. If the team were SQL-first with curated relational data, I would consider Warehouse instead.

## Related Repo Files

- [docs/16-fabric-decision-guide.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/docs/16-fabric-decision-guide.md)
- [adr/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/adr)
- [architecture/real-world-architecture-patterns.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/architecture/real-world-architecture-patterns.md)

## Related Wiki Pages

- [Lakehouse vs Warehouse](Lakehouse-vs-Warehouse)
- [Data Pipelines vs Notebooks](Data-Pipelines-vs-Notebooks)
- [Dataflow Gen2 vs Notebook vs Pipeline](Dataflow-Gen2-vs-Notebook-vs-Pipeline)
- [Architecture Decision Records Guide](Architecture-Decision-Records-Guide)
- [Real-World Architecture Patterns](Real-World-Architecture-Patterns)

## Summary Checklist

- [ ] I can justify Lakehouse versus Warehouse.
- [ ] I can choose Notebook, Pipeline, or Dataflow Gen2.
- [ ] I understand Shortcut versus Copy tradeoffs.
- [ ] I can explain Direct Lake versus Import at a practical level.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Architecture Decision Records Guide](Architecture-Decision-Records-Guide) | [Home](Home) | [Real-World Architecture Patterns](Real-World-Architecture-Patterns) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
