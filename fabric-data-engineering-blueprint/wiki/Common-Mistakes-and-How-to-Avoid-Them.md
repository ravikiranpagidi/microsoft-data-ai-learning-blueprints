# Common Mistakes and How to Avoid Them

> **Learning stage:** Decision, career, and community
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply common mistakes and how to avoid them to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Performance and Optimization](Performance-and-Optimization) | [Home](Home) | [Architecture Decision Records Guide](Architecture-Decision-Records-Guide)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

List common Fabric Data Engineering mistakes, explain why they cause problems, and show the better approach.

## Who Should Read This

Beginners, practitioners, reviewers, and teams preparing a Fabric proof of concept or production release.

## How to Use This Page

Use this page as a design review checklist. If a project has many of these mistakes, pause and fix the foundation before adding more features.

| # | Mistake | Why It Is a Problem | Better Approach |
| ---: | --- | --- | --- |
| 1 | Treating Lakehouse as a file dump | Raw files pile up without structure, ownership, or consumption rules. | Use Files for landing and Delta Tables for governed layers. |
| 2 | Skipping the Silver layer | Dirty records and inconsistent types reach BI. | Clean, type, deduplicate, and validate in Silver. |
| 3 | Exposing Bronze to business users | Users see raw, inconsistent, or sensitive data. | Expose Gold tables, SQL views, or semantic models. |
| 4 | Not defining table grain | Metrics become ambiguous and hard to reconcile. | State grain, such as one row per transaction. |
| 5 | Not validating business keys | Joins fail or duplicate results appear. | Check required keys, uniqueness, and referential integrity. |
| 6 | Hardcoding paths | Dev/Test/Prod promotion requires risky code edits. | Use parameters and environment configuration. |
| 7 | Ignoring data quality | Bad data reaches dashboards and trust is lost. | Run DQ rules before broad consumption. |
| 8 | Creating too many notebooks | Logic becomes fragmented and hard to orchestrate. | Use modular notebooks with clear responsibilities. |
| 9 | Creating one huge notebook | Testing, review, and reruns are hard. | Split setup, Bronze, Silver, Gold, DQ, and consumption. |
| 10 | Not documenting metrics | Different reports define metrics differently. | Use semantic model docs and a business glossary. |
| 11 | Overusing Power BI transformations | Business logic is duplicated outside engineering controls. | Transform in Silver and Gold, model in Power BI. |
| 12 | Ignoring security | Sensitive fields may be overexposed. | Apply least privilege and PII handling. |
| 13 | Not planning CI/CD | Releases become manual and fragile. | Use Git, deployment strategy, and release checklist. |
| 14 | Not separating environments | Development changes can break production users. | Use Dev/Test/Prod workspaces. |
| 15 | Poor naming standards | Assets are hard to find and automate. | Adopt naming standards early. |
| 16 | Over-partitioning | Small tables become slower and more complex. | Partition only with evidence. |
| 17 | Not managing small files | Query performance degrades over time. | Monitor file counts and optimize Delta tables. |
| 18 | No ownership model | Issues have no accountable resolver. | Assign owner, steward, and technical maintainer. |
| 19 | No glossary | Business terms drift across teams. | Maintain metric and term definitions. |
| 20 | No release checklist | Validation steps are missed. | Require checklist before promotion. |
| 21 | No monitoring plan | Failures are discovered by users. | Track runs, row counts, DQ results, and refreshes. |
| 22 | Treating shortcuts like copies | Ownership and freshness are misunderstood. | Document shortcut source, owner, and SLA. |
| 23 | Using SQL views to hide bad modeling | Complexity moves downstream. | Fix the model and keep views purposeful. |
| 24 | Not reviewing semantic model fields | PII or technical fields leak into reports. | Hide or secure fields before release. |
| 25 | Building without ADRs | Key decisions are forgotten or repeated. | Document important tradeoffs with ADRs. |

## Practical Review Routine

1. Review layer responsibilities.
2. Review table grain and relationships.
3. Run validation queries.
4. Run data quality checks.
5. Review PII and access.
6. Review semantic model measures.
7. Review release checklist.
8. Document new decisions.

## Best Practices

- Treat mistakes as signals, not blame.
- Fix architecture issues before adding more dashboards.
- Add automated or repeatable checks when a mistake is found.
- Convert recurring mistakes into documentation and templates.

## Severity Guide

| Severity | Meaning | Example | Action |
| --- | --- | --- | --- |
| High | Can break trust, security, or production reliability | Exposing Bronze with PII to business users | Fix before release |
| Medium | Creates maintainability or quality risk | No metric glossary | Add to backlog and assign owner |
| Low | Causes friction but is not immediately dangerous | Inconsistent page wording | Clean up during documentation pass |

## Pre-Release Review Checklist

Use this checklist before calling a Fabric proof of concept production-ready:

- [ ] Bronze is not the business consumption layer.
- [ ] Silver applies type casting, deduplication, and referential validation.
- [ ] Gold table grain is documented.
- [ ] SQL views do not hide broken modeling.
- [ ] Data quality rules run and critical failures stop promotion.
- [ ] PII fields are classified and access-reviewed.
- [ ] Semantic model measures have business definitions.
- [ ] Dev/Test/Prod promotion path is clear.
- [ ] Release checklist and rollback notes exist.
- [ ] At least one ADR captures major architecture choices.

## How to Turn Mistakes into Contributions

If you find one of these mistakes in the repo or Wiki, open a focused issue or pull request. Good community improvements include adding a validation query, improving a checklist, clarifying a decision page, or adding a realistic example from the Retail Banking flow.

## Related Repo Files

- [docs/17-common-enterprise-mistakes.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/docs/17-common-enterprise-mistakes.md)
- [checklists/fabric-project-checklist.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/checklists/fabric-project-checklist.md)
- [data-quality/dq_rules.yml](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/data-quality/dq_rules.yml)
- [cicd/release-checklist.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/cicd/release-checklist.md)

## Related Wiki Pages

- [Medallion Architecture](Medallion-Architecture)
- [Data Quality Framework](Data-Quality-Framework)
- [Governance and Security](Governance-and-Security)
- [CI/CD and Deployment Strategy](CICD-and-Deployment-Strategy)
- [Performance and Optimization](Performance-and-Optimization)

## Summary Checklist

- [ ] I reviewed all 25 mistakes.
- [ ] I know which mistakes apply to my project.
- [ ] I have added fixes to the backlog or checklist.
- [ ] I know when to create an ADR.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Performance and Optimization](Performance-and-Optimization) | [Home](Home) | [Architecture Decision Records Guide](Architecture-Decision-Records-Guide) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
