# Medallion Architecture

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply medallion architecture to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Sample Dataset Guide](Sample-Dataset-Guide) | [Home](Home) | [Bronze Layer Design](Bronze-Layer-Design)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain medallion architecture in Fabric and how Bronze, Silver, and Gold layers support reliable analytics.

## Who Should Read This

Beginners, engineers transitioning from Databricks or Synapse, BI developers, and architects designing a Lakehouse project.

## Beginner Explanation

Medallion architecture organizes data into layers of increasing quality and business readiness. Bronze stores raw data, Silver stores cleaned and standardized data, and Gold stores business-ready data for analytics.

## Layer Definitions

| Layer | Meaning | Main users | Example table |
| --- | --- | --- | --- |
| Bronze | Raw or lightly enriched source data | Data engineers | bronze_transactions |
| Silver | Cleaned, typed, deduplicated, conformed data | Data engineers, stewards | silver_transactions |
| Gold | Business-ready facts, dimensions, and views | Analysts, BI developers | fact_transaction |

## Medallion Flow

~~~mermaid
flowchart LR
    Files[Lakehouse Files: CSV source] --> Bronze[Bronze Delta Tables: raw plus metadata]
    Bronze --> Silver[Silver Delta Tables: cleaned and validated]
    Silver --> Gold[Gold Star Schema: facts and dimensions]
    Gold --> SQL[SQL Analytics Endpoint Views]
    Gold --> PowerBI[Power BI Semantic Model]
~~~

## Why It Matters

Without layers, raw data, cleaned data, and business-ready data get mixed together. That makes quality difficult to explain and reporting difficult to trust. Medallion architecture gives teams a shared language for data maturity.

## How It Applies in Fabric

Fabric Lakehouse tables are a natural fit for medallion architecture. Notebooks can transform between layers. Pipelines can orchestrate the layer sequence. SQL Analytics Endpoint and Power BI can consume Gold outputs.

## Best Practices

- Keep Bronze replayable and auditable.
- Apply type casting and standardization in Silver.
- Apply dimensional modeling and business naming in Gold.
- Run data quality checks before broad Gold consumption.
- Document table grain and ownership.

## Common Mistakes

| Mistake | Why it matters | Better approach |
| --- | --- | --- |
| Skipping Silver | Dirty data reaches Gold | Clean and validate before modeling. |
| Doing business metrics in Bronze | Raw layer loses replay value | Keep metrics in Gold or semantic model. |
| Exposing Bronze to business users | Users see inconsistent raw data | Grant business access to Gold views. |

## Related Repo Files

- [docs/05-medallion-architecture.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/docs/05-medallion-architecture.md)
- [architecture/medallion-architecture.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/architecture/medallion-architecture.md)
- [adr/001-why-medallion-architecture.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/adr/001-why-medallion-architecture.md)
- [notebooks/](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/tree/main/fabric-data-engineering-blueprint/notebooks)

## Related Wiki Pages

- [Bronze Layer Design](Bronze-Layer-Design)
- [Silver Layer Design](Silver-Layer-Design)
- [Gold Layer Design](Gold-Layer-Design)
- [Dimensional Modeling in Fabric](Dimensional-Modeling-in-Fabric)

## Summary Checklist

- [ ] I can define Bronze, Silver, and Gold.
- [ ] I know why layers improve trust.
- [ ] I know how notebooks and pipelines support the medallion flow.
- [ ] I can identify common layer mistakes.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Sample Dataset Guide](Sample-Dataset-Guide) | [Home](Home) | [Bronze Layer Design](Bronze-Layer-Design) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
