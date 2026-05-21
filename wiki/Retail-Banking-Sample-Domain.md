# Retail Banking Sample Domain

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply retail banking sample domain to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [End-to-End Project Walkthrough](End-to-End-Project-Walkthrough) | [Home](Home) | [Sample Dataset Guide](Sample-Dataset-Guide)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain the Retail Banking Customer Analytics domain and why it is useful for learning Fabric Data Engineering.

## Who Should Read This

Beginners, students, interview candidates, and architects who want business context behind the sample data model.

## Why Retail Banking?

Retail banking is useful for learning because it has familiar entities, clear relationships, meaningful metrics, and realistic governance concerns. Customers own accounts. Accounts use products. Transactions happen through branches and channels. Dates drive trend analysis. Some fields are sensitive and require careful access.

## Core Entities

| Entity | Business meaning | Example questions |
| --- | --- | --- |
| Customer | Person or organization served by the bank | How many active customers do we have? |
| Account | Banking account held by a customer | Which accounts have high balances? |
| Product | Banking product tied to an account | Which products are most used? |
| Transaction | Financial activity on an account | What is monthly transaction volume? |
| Branch | Physical or advisory location | Which branches are most active? |
| Date | Calendar dimension | How do balances and transactions trend over time? |

## Business Use Cases

- Customer segmentation and engagement.
- Product usage and adoption analysis.
- Branch activity analysis.
- Monthly transaction trends.
- Rejected transaction monitoring.
- Balance and account portfolio analysis.

## Real Enterprise Mapping

In a real bank, these datasets might come from core banking systems, card processors, CRM platforms, branch systems, and product catalogs. This sample keeps the data small but preserves the shape of enterprise analytics: multiple source entities, relationships, quality checks, governance concerns, and a dimensional Gold model.

## Best Practices

- Start with business questions before building tables.
- Identify entities and relationships early.
- Define fact table grain before building metrics.
- Treat customer and contact attributes as sensitive.
- Use a glossary so business terms are consistent.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Starting with tooling instead of questions | The model may not answer business needs | Start with questions and entities. |
| Ignoring sensitive data | Compliance risk | Classify PII fields early. |
| Treating product and account as the same thing | Metrics become confusing | Model them separately. |

## Related Repo Files

- [sample-data/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/sample-data)
- [semantic-model/business_glossary.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/semantic-model/business_glossary.md)
- [architecture/data-product-architecture.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/architecture/data-product-architecture.md)

## Related Wiki Pages

- [End-to-End Project Walkthrough](End-to-End-Project-Walkthrough)
- [Sample Dataset Guide](Sample-Dataset-Guide)
- [Building Dimensions and Facts](Building-Dimensions-and-Facts)
- [Glossary](Glossary)

## Summary Checklist

- [ ] I can explain the six core entities.
- [ ] I understand why this domain teaches real analytics patterns.
- [ ] I can map each entity to business questions.
- [ ] I know which data may be sensitive.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [End-to-End Project Walkthrough](End-to-End-Project-Walkthrough) | [Home](Home) | [Sample Dataset Guide](Sample-Dataset-Guide) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
