# Governance And Security

## Purpose

Explain governance and access practices for the real-time blueprint.

## Key Practices

- Use least privilege access.
- Restrict raw operational data.
- Protect driver and vehicle location details.
- Document stream owners.
- Apply sensitivity labels where needed.
- Keep connection strings out of code.
- Monitor capacity and alert changes.

## Access Pattern

| Persona | Access |
| --- | --- |
| Data engineer | Eventstream, Eventhouse, Lakehouse |
| Operations analyst | Dashboards and approved querysets |
| BI developer | Curated Lakehouse tables and semantic model |
| Business user | Power BI reports and alert outputs |
| Platform owner | Workspace, capacity, labels, monitoring |

Previous: [Data Activator](Data-Activator) | Next: [Cost Optimization](Cost-Optimization)
