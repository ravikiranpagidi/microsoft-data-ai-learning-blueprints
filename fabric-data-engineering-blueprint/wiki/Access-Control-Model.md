# Access Control Model

> **Learning stage:** Enterprise readiness
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply access control model to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Governance and Security](Governance-and-Security) | [Home](Home) | [PII and Sensitive Data Handling](PII-and-Sensitive-Data-Handling)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Provide a practical role-based access model for Fabric Lakehouse projects across Bronze, Silver, Gold, SQL, and Power BI.

## Who Should Read This

Workspace administrators, architects, security reviewers, data engineers, and data stewards.

## Roles

| Role | Responsibilities | Typical access |
| --- | --- | --- |
| Admin | Workspace, capacity, security, settings | Full workspace management |
| Data engineer | Build pipelines, notebooks, tables | Bronze, Silver, Gold write in dev |
| Data steward | Review definitions, quality, and issues | Silver read, Gold read, DQ results |
| Analyst | Explore governed data | Gold read, SQL views, semantic model |
| Viewer | Consume dashboards | Power BI reports and apps |
| Business user | Make decisions from reports | Curated semantic model and reports |

## Suggested Access by Layer

| Layer or asset | Admin | Data engineer | Steward | Analyst | Viewer |
| --- | --- | --- | --- | --- | --- |
| Workspace settings | Manage | Limited | No | No | No |
| Bronze tables | Manage | Read/write | Optional read | No | No |
| Silver tables | Manage | Read/write | Read | Limited | No |
| Gold tables | Manage | Read/write | Read | Read | No |
| SQL views | Manage | Create in dev | Review | Read | No |
| Semantic model | Manage | Support | Review | Build or read | Read |
| Reports | Manage | Support | Review | Build | View |

## Practical Guidance

Start broad in a learning workspace, but tighten access before production. Production should not give every user direct access to every Lakehouse table. Access should reflect the maturity of the data layer.

## Example Pattern

- Engineers maintain Bronze and Silver.
- Stewards review Silver quality and Gold definitions.
- Analysts query Gold views.
- Business users use Power BI reports.

## Best Practices

- Use least privilege.
- Separate development and production permissions.
- Review access before each release.
- Document exceptions.
- Avoid granting raw data access for convenience.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Analysts query Bronze directly | Raw data confusion and privacy risk | Provide Gold views. |
| Dev permissions copied to Prod | Excessive access | Define environment-specific roles. |
| No periodic access review | Access drift | Add release checklist review. |

## Related Repo Files

- [governance/access-control-model.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/governance/access-control-model.md)
- [governance/governance-checklist.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/governance/governance-checklist.md)
- [cicd/release-checklist.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/fabric-data-engineering-blueprint/cicd/release-checklist.md)

## Related Wiki Pages

- [Governance and Security](Governance-and-Security)
- [PII and Sensitive Data Handling](PII-and-Sensitive-Data-Handling)
- [Dev/Test/Prod Workspace Strategy](Dev-Test-Prod-Workspace-Strategy)
- [Performance and Optimization](Performance-and-Optimization)

## Summary Checklist

- [ ] Roles are defined.
- [ ] Layer-level access is documented.
- [ ] Production access is stricter than development access.
- [ ] Access is reviewed before release.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Governance and Security](Governance-and-Security) | [Home](Home) | [PII and Sensitive Data Handling](PII-and-Sensitive-Data-Handling) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
