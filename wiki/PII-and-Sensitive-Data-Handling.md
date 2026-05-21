# PII and Sensitive Data Handling

> **Learning stage:** Enterprise readiness
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply pii and sensitive data handling to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Access Control Model](Access-Control-Model) | [Home](Home) | [Naming Standards](Naming-Standards)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Explain how to identify, classify, restrict, and document PII and sensitive data in the Retail Banking sample.

## Who Should Read This

Data engineers, stewards, architects, security reviewers, and contributors adding new fields.

## What Is PII?

PII means personally identifiable information. It is data that can identify a person directly or indirectly. In banking, PII must be handled carefully because customer trust, regulatory expectations, and internal policies are involved.

## Example PII in This Domain

| Field | Sensitivity | Recommended handling |
| --- | --- | --- |
| first_name, last_name | PII | Restrict raw access, consider masking in broad views. |
| email | PII | Mask or restrict outside approved roles. |
| phone | PII | Mask or restrict. |
| date_of_birth | Sensitive PII | Avoid broad exposure; use age bands where possible. |
| customer_id | Business identifier | Treat as sensitive if linkable. |
| transaction data | Sensitive financial data | Restrict and audit access. |

## Masking Recommendations

- Replace email with partial value for broad audiences.
- Hide phone from general reporting.
- Use age ranges instead of date of birth.
- Keep customer IDs only where needed for operations.
- Use aggregated metrics for broad dashboards.

## Access Restrictions

PII should not be available to every analyst by default. Use role-based access, semantic model design, SQL views, and workspace permissions to control exposure.

## Data Minimization

Only expose fields needed for the use case. If a dashboard only needs customer segment and region, do not expose names, emails, or phone numbers.

## Audit Requirements

Track who owns sensitive data, who can access it, and why. Retain release checklists and access reviews.

## Do and Do Not

| Do | Do Not |
| --- | --- |
| Classify sensitive fields early | Assume sample data rules are enough for production |
| Mask or remove PII from broad views | Put PII in every Power BI dataset |
| Document approved uses | Share raw customer extracts casually |
| Use least privilege | Grant raw Lakehouse access to all users |

## Best Practices

- Define PII classification in governance docs.
- Use Gold views that exclude unnecessary sensitive columns.
- Review semantic model fields before release.
- Keep operational and analytical access separate.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Leaving email and phone visible everywhere | Privacy risk | Mask or hide by audience. |
| Treating demo data as production-safe design | Bad habits transfer | Practice proper classification. |
| No documented sensitive fields | Security review slows down | Maintain classification docs. |

## Related Repo Files

- [governance/pii-handling.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/governance/pii-handling.md)
- [governance/data-classification.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/governance/data-classification.md)
- [semantic-model/business_glossary.md](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/semantic-model/business_glossary.md)

## Related Wiki Pages

- [Governance and Security](Governance-and-Security)
- [Access Control Model](Access-Control-Model)
- [Naming Standards](Naming-Standards)

## Summary Checklist

- [ ] PII fields are identified.
- [ ] Sensitive fields are masked or restricted.
- [ ] Broad dashboards use minimized data.
- [ ] Access and usage are documented.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Access Control Model](Access-Control-Model) | [Home](Home) | [Naming Standards](Naming-Standards) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
