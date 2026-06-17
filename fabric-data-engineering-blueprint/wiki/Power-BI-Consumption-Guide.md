# Power BI Consumption Guide

> **Learning stage:** Enterprise readiness
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply power bi consumption guide to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [SQL Analytics Endpoint Guide](SQL-Analytics-Endpoint-Guide) | [Home](Home) | [Semantic Model Design](Semantic-Model-Design)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Guide Power BI developers on consuming Fabric Lakehouse data through Gold tables, SQL views, and semantic models.

## Who Should Read This

Power BI developers, BI architects, analysts, and data engineers preparing data for report consumption.

## How Power BI Consumes Fabric Lakehouse Data

Power BI can consume Fabric data through semantic models built over Lakehouse or SQL Analytics Endpoint objects. The best experience comes from using a clean Gold layer with facts, dimensions, relationships, and documented measures.

## Direct Lake Conceptual Explanation

Direct Lake lets Power BI analyze data in Fabric-backed Delta tables without importing a separate copy into the model. Conceptually, it reduces duplication and supports large analytical datasets. Teams should still design the model carefully, define measures, and validate security.

## Role of the Semantic Model

The semantic model is the business layer. It defines relationships, measures, hierarchies, field names, and the user-facing analytical experience. Do not treat it as just a connector.

## Recommended Consumption Pattern

1. Build Gold facts and dimensions.
2. Validate Gold table relationships and row counts.
3. Create SQL views only where they simplify consumption.
4. Build a semantic model with clear relationships.
5. Define measures centrally.
6. Build reports from semantic measures, not raw columns.

## Recommended Naming

Use business-friendly field names in the semantic model. For example, expose Total Transaction Amount instead of sum_absolute_transaction_amount. Hide technical columns that are not useful to report users.

## Measures

Common measures include:

- Total Transaction Amount
- Transaction Count
- Active Customer Count
- Average Transaction Amount
- Account Count
- Customer Segment Count

## Avoid Too Much Transformation in Power BI

Power BI should not be the main data cleansing engine for this project. Heavy cleaning, key validation, deduplication, and dimensional modeling belong in Fabric notebooks and Lakehouse tables. Power BI should focus on modeling, measures, relationships, and reports.

## Best Practices

- Use Gold tables or governed views as sources.
- Keep relationships simple and directional where possible.
- Use a Date table.
- Hide surrogate keys unless users need them.
- Define measures once and reuse them.
- Document metrics in the glossary.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Connecting Power BI directly to raw CSV files | Reports are fragile and ungoverned | Consume Gold tables or views. |
| Rebuilding transformations in Power Query | Logic is duplicated | Transform in Silver and Gold. |
| Creating measures differently in every report | Metric drift | Centralize measures in semantic model. |

## Official Reference

- [Power BI semantic models in Fabric](https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models)
- [Direct Lake overview](https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview)

## Related Repo Files

- [semantic-model/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/semantic-model)
- [sql/powerbi_consumption_views.sql](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/sql/powerbi_consumption_views.sql)
- [notebooks/06_powerbi_ready_views.ipynb](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/notebooks/06_powerbi_ready_views.ipynb)

## Related Wiki Pages

- [SQL Analytics Endpoint Guide](SQL-Analytics-Endpoint-Guide)
- [Semantic Model Design](Semantic-Model-Design)
- [Data Quality Framework](Data-Quality-Framework)
- [Real-World Architecture Patterns](Real-World-Architecture-Patterns)

## Summary Checklist

- [ ] I can describe the role of Gold tables in Power BI.
- [ ] I understand Direct Lake at a conceptual level.
- [ ] I know why semantic model measures should be centralized.
- [ ] I know not to push heavy cleansing into Power BI.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [SQL Analytics Endpoint Guide](SQL-Analytics-Endpoint-Guide) | [Home](Home) | [Semantic Model Design](Semantic-Model-Design) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
