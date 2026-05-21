# Dimensional Modeling in Fabric

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply dimensional modeling in fabric to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Gold Layer Design](Gold-Layer-Design) | [Home](Home) | [Building Dimensions and Facts](Building-Dimensions-and-Facts)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain dimensional modeling concepts in Fabric and why star schemas still matter for BI, SQL, and AI-ready analytics.

## Who Should Read This

Power BI developers, data engineers, architects, and interview candidates learning dimensional modeling in a Lakehouse context.

## Why Dimensional Modeling Still Matters

Fabric changes the platform experience, but it does not remove the need for good models. Business users still need clear facts, dimensions, relationships, and measures. A well-designed dimensional model makes reporting easier, faster to understand, and easier to govern.

## Star Schema

A star schema has a central fact table connected to surrounding dimension tables. Facts store measurable events. Dimensions store descriptive context.

## Facts

A fact table represents a business process at a defined grain. In this repo, fact_transaction has one row per transaction. Measures such as transaction amount and transaction count come from this table.

## Dimensions

Dimensions describe the who, what, where, and when of a fact. Customer, account, product, branch, and date dimensions provide slicers and grouping fields.

## Surrogate Keys

Surrogate keys are generated keys used for relationships in the model. They make joins stable and keep the model independent from natural business key changes.

## Natural Keys

Natural keys are source or business identifiers such as customer_id and account_id. Keep them for traceability and business conversations.

## Slowly Changing Dimensions Basics

A slowly changing dimension tracks how descriptive attributes change over time. This repo uses a simple current-state model for learning. In production, customer segment, branch region, or product attributes may require historical tracking.

## BI and AI Benefits

Dimensional models help Power BI because relationships and filter paths are clear. They also help AI and advanced analytics because entities and measures are explicit and documented.

## Best Practices

- Define fact grain first.
- Keep dimensions descriptive and facts measurable.
- Avoid many-to-many relationships unless intentionally designed.
- Include a Date dimension.
- Document measures and business terms.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Using transaction table as both fact and dimension | Confusing model | Separate facts and descriptive dimensions. |
| No Date dimension | Time analysis becomes inconsistent | Create dim_date. |
| No grain definition | Metrics are ambiguous | State one row per transaction. |

## Related Repo Files

- [semantic-model/semantic_model_design.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/semantic-model/semantic_model_design.md)
- [notebooks/03_gold_dimensional_model.ipynb](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/notebooks/03_gold_dimensional_model.ipynb)
- [adr/002-why-gold-star-schema.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/adr/002-why-gold-star-schema.md)

## Related Wiki Pages

- [Gold Layer Design](Gold-Layer-Design)
- [Building Dimensions and Facts](Building-Dimensions-and-Facts)
- [Semantic Model Design](Semantic-Model-Design)
- [30-Day Learning Plan](30-Day-Learning-Plan)

## Summary Checklist

- [ ] I can define facts, dimensions, grain, surrogate keys, and natural keys.
- [ ] I know why star schema matters in Fabric.
- [ ] I can explain current-state versus slowly changing dimensions at a basic level.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Gold Layer Design](Gold-Layer-Design) | [Home](Home) | [Building Dimensions and Facts](Building-Dimensions-and-Facts) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
