# Diagram Guide

## Purpose

This folder contains Excalidraw-friendly diagram descriptions and starter `.excalidraw` files.

## Diagram 1: End-To-End Microsoft Fabric Real-Time Intelligence Architecture

### Nodes

Data Sources:

- Vehicle telemetry.
- Shipment events.
- Warehouse sensors.
- Customer mobile app events.
- ERP or order system.
- External weather API.

Ingestion:

- Azure Event Hubs.
- Microsoft Fabric Eventstream.
- Custom event generator.

Real-Time Processing:

- Eventstream transformations.
- Eventhouse.
- KQL Database.
- KQL Querysets.

Storage:

- OneLake.
- Fabric Lakehouse.
- Delta tables.
- Historical event store.

Serving:

- Real-Time Dashboard.
- Power BI semantic model.
- Power BI reports.
- Fabric Activator.
- Alert notifications.

AI-ready layer:

- Feature tables.
- Delay prediction dataset.
- Anomaly detection dataset.
- Event summary tables.

Governance:

- Microsoft Purview.
- Fabric workspace roles.
- Sensitivity labels.
- Lineage.
- Monitoring and audit logs.

### Arrow Flow

Sources -> custom generator or Event Hubs -> Eventstream -> transformations -> Eventhouse -> KQL Database -> KQL Querysets -> Real-Time Dashboard and Activator -> alert notifications.

Eventstream and Eventhouse -> OneLake and Lakehouse -> Delta tables -> Power BI and AI-ready datasets.

Governance surrounds all layers.

### Layout Suggestion

Use a left-to-right layout with vertical lanes: Sources, Ingestion, Real-Time Processing, Storage, Serving, AI-ready layer. Put Governance as a bottom band or outer frame.

## Diagram 2: Real-Time Shipment Delay Detection Flow

### Nodes

- Shipment event generated.
- Eventstream receives event.
- Eventhouse stores event.
- KQL query calculates delay risk.
- Real-Time Dashboard shows status.
- Activator checks SLA threshold.
- Alert sent to operations team.
- Lakehouse stores historical pattern.
- Power BI shows daily SLA trend.

### Arrow Flow

Shipment event generated -> Eventstream receives event -> Eventhouse stores event -> KQL query calculates delay risk -> Real-Time Dashboard shows status -> Activator checks SLA threshold -> Alert sent to operations team.

Eventhouse stores event -> Lakehouse stores historical pattern -> Power BI shows daily SLA trend.

### Layout Suggestion

Use a central horizontal flow for real-time detection. Add a lower branch from Eventhouse to Lakehouse and Power BI for historical analysis.

## Diagram 3: Repo Demo Flow

### Nodes

- Generate sample events.
- Send events to Eventstream.
- Store in Eventhouse.
- Query with KQL.
- Visualize dashboard.
- Trigger alert.
- Persist to Lakehouse.
- Analyze in Power BI.
- Extend for ML or AI use case.

### Arrow Flow

Generate sample events -> Send events to Eventstream -> Store in Eventhouse -> Query with KQL -> Visualize dashboard -> Trigger alert -> Persist to Lakehouse -> Analyze in Power BI -> Extend for ML or AI use case.

### Layout Suggestion

Use numbered steps in a left-to-right flow. Keep this diagram simple enough for a 10 minute demo.
