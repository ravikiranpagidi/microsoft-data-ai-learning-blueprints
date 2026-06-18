# Architecture

## Purpose

Explain the target architecture for a Microsoft Fabric Real-Time Intelligence solution.

## Core Pattern

The blueprint uses Eventstream for ingestion, Eventhouse for low-latency operational query, KQL Database for event tables, Real-Time Dashboard for live monitoring, Fabric Activator for alerting, Lakehouse for historical analytics, and Power BI for governed reporting.

## Architecture Layers

| Layer | Components | Role |
| --- | --- | --- |
| Sources | Vehicles, shipments, sensors, apps, ERP, weather | Generate events |
| Ingestion | Event Hubs, Eventstream, generator | Receive and route events |
| Real time | Eventhouse, KQL Database, Querysets | Query current operational state |
| Action | Activator, notifications | Trigger business response |
| History | OneLake, Lakehouse, Delta | Store events and summaries |
| Reporting | Real-Time Dashboard, Power BI | Monitor and analyze |
| Governance | Roles, labels, lineage, audit | Control and document usage |

## Best Practices

- Keep event schemas stable.
- Include event timestamps.
- Use KQL for operational questions.
- Use Lakehouse for historical and curated analytics.
- Keep alert rules explainable.
- Restrict raw operational data.

## Common Mistakes

- Sending every event directly to Power BI.
- Building alerts before validating KQL logic.
- Ignoring retention and capacity.
- Not documenting alert ownership.

Previous: [Home](Home) | Next: [Setup Guide](Setup-Guide)
