# Lakehouse Integration

## Purpose

Explain how streaming events become historical analytics assets.

## Why Lakehouse

Eventhouse is for real-time query. Lakehouse is for durable history, Delta tables, Power BI reporting, and AI feature engineering.

## Table Layers

Bronze:

- `raw_shipment_events`
- `raw_vehicle_telemetry`
- `raw_warehouse_sensor_events`

Silver:

- `shipment_status_clean`
- `vehicle_telemetry_clean`
- `warehouse_sensor_clean`

Gold:

- `shipment_sla_summary`
- `route_delay_summary`
- `vehicle_health_summary`
- `warehouse_condition_summary`

## Recommendation

Use Gold tables for Power BI and AI-ready feature creation. Keep raw events restricted.

Previous: [Eventhouse and KQL](Eventhouse-and-KQL) | Next: [Power BI Layer](Power-BI-Layer)
