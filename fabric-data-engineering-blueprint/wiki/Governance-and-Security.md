# Governance and Security

> **Learning stage:** Enterprise readiness
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply governance and security to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Data Quality Framework](Data-Quality-Framework) | [Home](Home) | [Access Control Model](Access-Control-Model)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain governance and security principles for a Fabric Lakehouse project, including ownership, stewardship, access, PII, and auditability.

## Who Should Read This

Architects, platform owners, data engineers, stewards, and enterprise teams preparing a Fabric proof of concept.

## Why Governance Matters

Governance turns a working demo into a trustworthy data product. Without governance, teams may not know who owns data, who can access sensitive fields, which metrics are approved, or how changes are promoted.

## Core Governance Concepts

| Concept | Practical meaning |
| --- | --- |
| Data owner | Accountable business owner for a dataset or domain. |
| Data steward | Reviews definitions, quality, and business meaning. |
| Data engineer | Builds and maintains pipelines, notebooks, and tables. |
| Data consumer | Uses approved Gold datasets and semantic models. |
| Data product | Governed data asset with owner, quality expectations, and consumers. |

## Access Control

Access should follow least privilege. Engineers may need Bronze and Silver access. Analysts usually need Gold, SQL views, or semantic models. Sensitive fields should be restricted or masked where appropriate.

## PII Classification

In this banking domain, email, phone, name, and date of birth are sensitive. Classify these fields and document who can access them.

## Bronze/Silver/Gold Access Model

| Layer | Typical access | Reason |
| --- | --- | --- |
| Bronze | Data engineers only | Raw data may be sensitive or inconsistent. |
| Silver | Engineers and stewards | Cleaned data still may contain sensitive fields. |
| Gold | Analysts and BI users | Business-ready and governed. |
| Semantic model | Business users | Friendly, curated consumption surface. |

## Auditability

Good governance requires lineage and operational evidence. Keep batch IDs, ingestion timestamps, data quality results, release notes, and ADRs.

## Documentation

Governance is not only permissions. It includes glossary, naming standards, ownership model, release checklist, and known limitations.

## Best Practices

- Define data owners and stewards early.
- Classify sensitive columns.
- Give business users Gold or semantic access, not raw access.
- Use naming standards.
- Review access during releases.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Everyone has access to everything | Security and privacy risk | Use least privilege. |
| No owner assigned | Issues are never resolved | Assign owner and steward. |
| Governance added after go-live | Rework and risk | Design governance from day one. |

## Related Repo Files

- [governance/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/governance)
- [semantic-model/business_glossary.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/semantic-model/business_glossary.md)
- [data-quality/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/data-quality)
- [adr/](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/tree/main/fabric-data-engineering-blueprint/adr)

## Related Wiki Pages

- [Access Control Model](Access-Control-Model)
- [PII and Sensitive Data Handling](PII-and-Sensitive-Data-Handling)
- [Naming Standards](Naming-Standards)
- [CI/CD and Deployment Strategy](CICD-and-Deployment-Strategy)

## Summary Checklist

- [ ] Data owner and steward are defined.
- [ ] Sensitive fields are classified.
- [ ] Access differs by layer.
- [ ] Data quality and release evidence are retained.
- [ ] Business users consume governed assets.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Data Quality Framework](Data-Quality-Framework) | [Home](Home) | [Access Control Model](Access-Control-Model) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
