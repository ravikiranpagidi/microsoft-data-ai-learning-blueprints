# Architecture

## Purpose

This page explains the end-to-end architecture for the Smart Logistics and Operations Monitoring blueprint.

## Architecture Summary

The solution uses Microsoft Fabric Real-Time Intelligence for live operational monitoring and Fabric Lakehouse for historical analytics. Eventstream handles ingestion and routing. Eventhouse and KQL Database support fast operational queries. Real-Time Dashboard supports live monitoring. Fabric Activator supports action when conditions are detected. Lakehouse and Power BI support historical reporting and curated analytics.

## Logical Architecture

| Layer | Components | Responsibility |
| --- | --- | --- |
| Sources | Vehicle telemetry, shipment events, warehouse sensors, customer app events, ERP or order system, weather API | Emit operational events |
| Ingestion | Custom generator, optional Azure Event Hubs, Fabric Eventstream | Capture, transform, and route events |
| Real-time analytics | Eventhouse, KQL Database, KQL Querysets | Store and query time-series operational data |
| Live visualization | Real-Time Dashboard | Monitor current conditions and operational metrics |
| Action | Fabric Activator | Detect conditions and trigger notifications or workflows |
| Historical analytics | OneLake, Lakehouse, Delta tables | Store historical events and curated aggregates |
| BI and AI | Power BI, feature tables, anomaly datasets | Analyze trends and prepare predictive use cases |

## Why Eventhouse

Eventhouse is used for high-volume event data that needs low-latency querying. It is well suited for time-series data, operational dashboards, ad hoc KQL analysis, and alert conditions.

## Why Lakehouse

Lakehouse is used for durable historical analytics. It supports Delta tables, curated medallion layers, Power BI consumption, and AI-ready feature tables. Long-term reporting should not depend only on raw streaming tables.

## Operational Pattern

1. Events are produced by logistics systems and sensors.
2. Eventstream receives the events.
3. Eventstream routes high-value streams to Eventhouse.
4. KQL Database stores and serves operational queries.
5. Real-Time Dashboard visualizes current metrics.
6. Activator evaluates alert conditions.
7. Selected streams land in Lakehouse for historical analytics.
8. Power BI reports consume curated Lakehouse outputs.

## Enterprise Design Notes

- Keep raw streams immutable where possible.
- Use consistent event IDs and timestamps.
- Separate dashboard queries from exploratory queries.
- Define retention based on query need and compliance rules.
- Do not expose raw operational data broadly.
- Document alert owners and escalation channels.
- Monitor capacity before scaling event volume.

## Related Files

- [../diagrams/architecture.excalidraw](../diagrams/architecture.excalidraw)
- [eventstream-design.md](eventstream-design.md)
- [eventhouse-kql.md](eventhouse-kql.md)
- [lakehouse-design.md](lakehouse-design.md)
