# Lakehouse Design

## Purpose

This page explains how streaming data should be organized in Lakehouse for historical analytics, Power BI, and AI-ready datasets.

## Why Lakehouse Is Needed

Eventhouse supports low-latency operational query. Lakehouse supports durable historical analytics, curated Delta tables, BI-ready outputs, and AI feature creation.

Use both:

- Eventhouse for now, alerting, live dashboards, and KQL exploration.
- Lakehouse for history, conformed entities, reporting, data products, and machine learning features.

## Medallion Table Design

### Bronze

| Table | Purpose |
| --- | --- |
| `raw_shipment_events` | Raw shipment status events with metadata |
| `raw_vehicle_telemetry` | Raw telemetry readings from vehicles |
| `raw_warehouse_sensor_events` | Raw warehouse environmental events |

### Silver

| Table | Purpose |
| --- | --- |
| `shipment_status_clean` | Cleaned shipment state and delay fields |
| `vehicle_telemetry_clean` | Cleaned location, speed, fuel, engine, and safety data |
| `warehouse_sensor_clean` | Cleaned sensor readings with breach flags |

### Gold

| Table | Purpose |
| --- | --- |
| `shipment_sla_summary` | Shipment and SLA metrics by date, route, and region |
| `route_delay_summary` | Route-level delay behavior |
| `vehicle_health_summary` | Vehicle health and anomaly indicators |
| `warehouse_condition_summary` | Warehouse condition trends and breach counts |

## OneLake Connection

OneLake provides the unified storage foundation across Fabric. In a full implementation, selected events can be made available to Lakehouse, Eventhouse, and downstream consumers without copying data unnecessarily when shortcuts or native integrations are appropriate.

## AI-Ready Outputs

Useful AI-ready tables:

- `delay_prediction_features`
- `vehicle_anomaly_features`
- `warehouse_condition_features`
- `route_risk_features`

Feature examples:

- Historical average route delay.
- Last known vehicle engine temperature.
- Current weather risk indicator.
- Temperature breach duration.
- Shipment priority.
- Day-of-week and time-of-day attributes.

## Practical Recommendation

Do not push every raw event directly into broad Power BI models. Curate operational history into clean and summary tables first.
