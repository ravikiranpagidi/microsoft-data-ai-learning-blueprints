# Gold Layer Design

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply gold layer design to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Silver Layer Design](Silver-Layer-Design) | [Home](Home) | [Dimensional Modeling in Fabric](Dimensional-Modeling-in-Fabric)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Define the Gold layer design for business-ready dimensional models, SQL views, Power BI consumption, and metric consistency.

## Who Should Read This

BI developers, data engineers, analysts, and architects building governed consumption layers.

## Purpose of Gold

Gold is the business-ready layer. It should be understandable to analysts, stable for BI, and aligned to business questions. Gold is where this repo builds dimensions and a transaction fact table.

## Business-Ready Tables

Gold tables should use business-friendly names, clear keys, documented grain, and stable relationships. They should avoid exposing raw ingestion columns that are not useful to consumers.

## Dimensional Model

This repo uses a star schema:

- dim_customer
- dim_account
- dim_product
- dim_branch
- dim_date
- fact_transaction

## Consumption Views

SQL views make Gold easier for SQL users and Power BI developers. They can expose transaction detail, customer 360, branch activity, product usage, and executive KPIs.

## Power BI Readiness

Gold should make Power BI simpler, not push all modeling work into reports. Relationships, facts, dimensions, date table, and measure definitions should be clear before reports are built.

## Metric Consistency

Define measures such as Total Transaction Amount, Transaction Count, Active Customer Count, Account Count, and Average Transaction Amount consistently. Avoid each report redefining the same measure differently.

## Access Pattern

Business users generally consume Gold tables, SQL views, or semantic models. Engineers and stewards may access Silver. Bronze access should be limited to engineering and troubleshooting roles.

## Best Practices

- Define fact grain before building metrics.
- Use dimensions for descriptive attributes.
- Keep business keys for traceability.
- Use surrogate keys for stable BI relationships.
- Validate row counts and missing keys.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Building one wide table for every need | Hard to govern and extend | Use star schema where BI is important. |
| Mixing metric definitions across reports | Users lose trust | Centralize measures. |
| Skipping validation | Broken relationships reach Power BI | Run validation and DQ checks. |

## Related Repo Files

- [notebooks/03_gold_dimensional_model.ipynb](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/notebooks/03_gold_dimensional_model.ipynb)
- [sql/create_gold_views.sql](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/sql/create_gold_views.sql)
- [semantic-model/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/semantic-model)
- [adr/002-why-gold-star-schema.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/adr/002-why-gold-star-schema.md)

## Related Wiki Pages

- [Dimensional Modeling in Fabric](Dimensional-Modeling-in-Fabric)
- [Building Dimensions and Facts](Building-Dimensions-and-Facts)
- [Power BI Consumption Guide](Power-BI-Consumption-Guide)
- [Semantic Model Design](Semantic-Model-Design)

## Summary Checklist

- [ ] Gold tables answer business questions.
- [ ] Fact grain is documented.
- [ ] Dimensions and facts are validated.
- [ ] Power BI consumes Gold or governed views.
- [ ] Metric definitions are consistent.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Silver Layer Design](Silver-Layer-Design) | [Home](Home) | [Dimensional Modeling in Fabric](Dimensional-Modeling-in-Fabric) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
