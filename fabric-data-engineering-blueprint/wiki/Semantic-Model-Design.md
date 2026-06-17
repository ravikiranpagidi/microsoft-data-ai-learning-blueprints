# Semantic Model Design

> **Learning stage:** Enterprise readiness
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply semantic model design to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Power BI Consumption Guide](Power-BI-Consumption-Guide) | [Home](Home) | [Data Quality Framework](Data-Quality-Framework)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain how to design a business-friendly Power BI semantic model over the Retail Banking Gold layer.

## Who Should Read This

BI developers, semantic model designers, data engineers, and architects who want consistent reporting metrics.

## Business-Friendly Model

A semantic model should feel like the business domain, not like source system tables. Users should see Customer, Account, Product, Branch, Date, and Transaction concepts with clear measures and readable names.

## Facts and Dimensions

Use fact_transaction as the main fact table. Use dim_customer, dim_account, dim_product, dim_branch, and dim_date as dimensions. Relationships should flow from dimensions to fact where possible.

## Measures

Recommended measures:

| Measure | Definition idea |
| --- | --- |
| Total Transaction Amount | Sum of absolute transaction amount for posted transactions. |
| Transaction Count | Count of transaction IDs. |
| Active Customer Count | Distinct count of active customer keys. |
| Average Transaction Amount | Total transaction amount divided by transaction count. |
| Account Count | Distinct count of account keys. |
| Customer Segment Count | Distinct count of customer segments. |

## Hierarchies

Useful hierarchies include:

- Date: Year -> Quarter -> Month -> Date
- Geography: Region -> State -> City -> Branch
- Product: Product Family -> Product Category -> Product Name
- Customer: Segment -> Customer

## Date Table

Use dim_date as the official date table. Time intelligence becomes much easier when all date filtering goes through a dedicated date dimension.

## Naming Conventions

- Use spaces in display names for report users.
- Keep table names business-friendly.
- Hide technical keys and load columns.
- Prefix measures only if your team standard requires it.
- Use descriptions for measures and fields.

## Business Glossary

A glossary keeps definitions stable. If Active Customer means customer_status equals Active, write that definition down. If Total Transaction Amount uses absolute posted amounts, document it.

## Best Practices

- Keep relationships simple.
- Avoid bidirectional filters unless justified.
- Use explicit measures instead of implicit aggregations.
- Hide columns not meant for report users.
- Validate totals against SQL queries.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| No measure descriptions | Users misunderstand metrics | Add business definitions. |
| Too many visible technical columns | Model is noisy | Hide keys and load metadata. |
| Multiple date columns without a clear date table | Time analysis becomes inconsistent | Use dim_date relationships intentionally. |

## Related Repo Files

- [semantic-model/semantic_model_design.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/semantic-model/semantic_model_design.md)
- [semantic-model/measures.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/semantic-model/measures.md)
- [semantic-model/business_glossary.md](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/semantic-model/business_glossary.md)
- [sql/business_metrics.sql](https://github.com/ravikiranpagidi/microsoft-data-ai-learning-blueprints/blob/main/fabric-data-engineering-blueprint/sql/business_metrics.sql)

## Related Wiki Pages

- [Power BI Consumption Guide](Power-BI-Consumption-Guide)
- [Building Dimensions and Facts](Building-Dimensions-and-Facts)
- [Glossary](Glossary)

## Summary Checklist

- [ ] I know the fact and dimension tables in the semantic model.
- [ ] I can define the core measures.
- [ ] I can create useful hierarchies.
- [ ] I know why a glossary matters.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Power BI Consumption Guide](Power-BI-Consumption-Guide) | [Home](Home) | [Data Quality Framework](Data-Quality-Framework) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
