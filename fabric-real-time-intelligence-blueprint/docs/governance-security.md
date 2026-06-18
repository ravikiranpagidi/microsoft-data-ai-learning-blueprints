# Governance And Security

## Purpose

This page describes governance and security considerations for a Fabric Real-Time Intelligence implementation.

## Governance Goals

- Know who owns each event stream.
- Know which data is sensitive.
- Control who can query raw operational data.
- Keep alert rules explainable and auditable.
- Document lineage from source event to dashboard or report.
- Avoid secrets in code and public repositories.

## Role Model

| Role | Access Pattern |
| --- | --- |
| Fabric admin | Capacity, tenant settings, workspace controls |
| Platform owner | Workspace structure, naming, monitoring, deployment standards |
| Data engineer | Eventstream, Eventhouse, KQL database, Lakehouse ingestion |
| Operations analyst | Real-Time Dashboard, approved querysets, alert review |
| BI developer | Curated Lakehouse tables, semantic model, reports |
| Business user | Power BI reports and approved alert outputs |

## Sensitive Data

Potential sensitive fields:

- Driver identifier.
- Vehicle location.
- Customer region and delivery destination.
- Order and shipment identifiers.
- Operational incident details.

## Security Recommendations

- Use least privilege workspace roles.
- Separate development and production workspaces.
- Store connection strings in environment variables or managed secret stores.
- Do not commit Event Hubs connection strings.
- Apply sensitivity labels where location or customer-related data is exposed.
- Keep raw streams restricted to engineering and operations personas.
- Expose curated summaries to broader business audiences.

## Audit And Monitoring

Track:

- Event ingestion health.
- Dashboard usage.
- Alert rule changes.
- KQL database query activity.
- Capacity trends.
- Failed or noisy alerts.

## Production Readiness Checklist

- [ ] Event source owners documented.
- [ ] Workspace roles reviewed.
- [ ] Sensitive fields identified.
- [ ] Alert owners and escalation channels defined.
- [ ] Retention rules agreed.
- [ ] Capacity monitoring enabled.
- [ ] Data lineage documented.
- [ ] No secrets committed to source control.
