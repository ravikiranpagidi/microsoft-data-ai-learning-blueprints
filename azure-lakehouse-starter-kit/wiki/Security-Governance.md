# Security Governance

## Purpose

This page explains the minimum governance model for a practical Azure Lakehouse proof of concept.

## Core Controls

| Control | Recommendation |
| --- | --- |
| Identity | Use Microsoft Entra ID groups |
| Secrets | Store secrets in Azure Key Vault |
| Storage access | Use Unity Catalog storage credentials and external locations |
| Data access | Grant access by schema and role |
| Sensitive data | Mask or restrict PII columns |
| Ownership | Assign data owner and data steward |

## Suggested Access By Layer

| Role | Raw | Bronze | Silver | Gold |
| --- | --- | --- | --- | --- |
| Platform admin | Admin | Admin | Admin | Admin |
| Data engineer | Read/write | Read/write | Read/write | Read/write |
| Data steward | No direct access | Read | Read | Read |
| Analyst | No access | No access | Limited read | Read |
| Business user | No access | No access | No access | Power BI only |

## Common Mistakes

- Sharing raw data broadly.
- Keeping secrets in notebooks.
- Treating dev and prod as the same workspace.
- Not documenting data ownership.
- Ignoring PII in sample designs.

## Related Pages

- [Architecture](Architecture)
- [CI CD](CI-CD)
- [Data Quality](Data-Quality)

