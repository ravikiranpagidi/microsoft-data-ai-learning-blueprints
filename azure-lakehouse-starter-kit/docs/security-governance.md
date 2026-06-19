# Security And Governance

## Purpose

Explain practical security and governance for an Azure Lakehouse.

## Recommended Controls

- Azure Key Vault for secrets.
- Managed identities for Azure resources.
- Service principals for CI/CD where needed.
- ADLS Gen2 RBAC and ACLs.
- Unity Catalog permissions for Databricks if available.
- Workspace separation for dev, test, and prod.
- PII identification and masking.
- Row-level and column-level security concepts.
- Microsoft Purview for catalog and lineage.
- Audit logging for pipelines, jobs, and data access.

## PII Examples

- Customer name.
- Email address.
- Phone number.
- Street address.
- Payment token or masked card reference.

## Access Model

| Persona | Access |
| --- | --- |
| Data engineer | Raw, Bronze, Silver, Databricks jobs |
| Analytics engineer | Silver and Gold |
| BI developer | Gold and approved views |
| Business user | Power BI reports |
| Platform admin | Workspace, identity, networking, secrets |

## Practical Recommendation

Use Unity Catalog for governed table access where available. Use ADLS ACLs and workspace controls carefully when Hive metastore is used.
