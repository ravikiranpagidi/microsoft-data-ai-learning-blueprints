# Architecture Decision Records Guide

> **Learning stage:** Decision, career, and community
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply architecture decision records guide to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Common Mistakes and How to Avoid Them](Common-Mistakes-and-How-to-Avoid-Them) | [Home](Home) | [Fabric Decision Guide](Fabric-Decision-Guide)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain Architecture Decision Records, why they matter, how this repo uses them, and when contributors should create one.

## Who Should Read This

Architects, maintainers, contributors, and engineers making decisions that affect project structure, governance, or consumption patterns.

## What Is an ADR?

An Architecture Decision Record is a short document that captures an important technical or architectural decision. It explains the context, the decision, the consequences, alternatives considered, and the recommendation.

## Why ADRs Matter

Projects forget why decisions were made. ADRs preserve reasoning so future contributors do not repeat the same debate or accidentally undo an important tradeoff.

## How This Repo Uses ADRs

This repo includes ADRs for medallion architecture, Gold star schema, Delta tables, engineering versus consumption layers, Dev/Test/Prod workspaces, and data quality before Gold. These are not academic documents. They explain practical decisions that shape the blueprint.

## ADR Format

Use this structure:

- Title
- Status
- Context
- Decision
- Consequences
- Alternatives considered
- Recommendation

## Example ADR

Title: Use Gold Star Schema for Power BI Consumption

Status: Accepted

Context: Business users need reliable customer, account, product, branch, date, and transaction analysis.

Decision: Build Gold dimensions and fact_transaction rather than exposing Silver tables directly.

Consequences: The model is easier for Power BI and SQL users, but requires extra modeling work.

Alternatives considered: Wide table, direct Silver access, report-level shaping.

Recommendation: Use star schema for governed BI scenarios.

## When to Create an ADR

Create an ADR when a decision affects architecture, governance, CI/CD, security, data model design, or contributor patterns. Do not create ADRs for tiny formatting edits.

## Best Practices

- Keep ADRs short and specific.
- Record alternatives honestly.
- Include consequences, not only benefits.
- Update status if a decision is superseded.
- Link ADRs from relevant docs and Wiki pages.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| ADRs written after everyone forgets context | Poor accuracy | Write ADRs when the decision is made. |
| ADRs only list the chosen option | Tradeoffs are hidden | Include alternatives. |
| ADRs never referenced | They become stale | Link them from docs and reviews. |

## Related Repo Files

- [adr/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/adr)
- [adr/README.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/adr/README.md)
- [adr/002-why-gold-star-schema.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/adr/002-why-gold-star-schema.md)
- [CONTRIBUTING.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/CONTRIBUTING.md)

## Related Wiki Pages

- [Common Mistakes and How to Avoid Them](Common-Mistakes-and-How-to-Avoid-Them)
- [Fabric Decision Guide](Fabric-Decision-Guide)
- [Contributor Guide](Contributor-Guide)

## Summary Checklist

- [ ] I understand the purpose of ADRs.
- [ ] I know the ADR format used by this repo.
- [ ] I know when a new contribution needs an ADR.
- [ ] I can explain decision consequences and alternatives.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Common Mistakes and How to Avoid Them](Common-Mistakes-and-How-to-Avoid-Them) | [Home](Home) | [Fabric Decision Guide](Fabric-Decision-Guide) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
