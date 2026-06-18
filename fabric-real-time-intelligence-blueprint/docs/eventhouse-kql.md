# Eventhouse And KQL

## Purpose

This page explains the role of Eventhouse, KQL Database, and KQL Querysets in the blueprint.

## Eventhouse Role

Eventhouse stores and analyzes real-time operational events. It is designed for time-based event data and supports fast KQL queries over streaming and historical event records.

In this blueprint, Eventhouse is used for:

- Latest shipment state.
- Current delay detection.
- Vehicle telemetry anomaly detection.
- Warehouse temperature breach monitoring.
- Real-time dashboard tiles.
- Activator alert conditions.

## KQL Database Tables

| Table | Purpose |
| --- | --- |
| `ShipmentEvents` | Shipment status and delay tracking |
| `VehicleTelemetry` | Location and health telemetry |
| `WarehouseSensorEvents` | Temperature and condition monitoring |

## Query Categories

| File | Purpose |
| --- | --- |
| [../kql/create_tables.kql](../kql/create_tables.kql) | Create Eventhouse tables |
| [../kql/ingestion_mapping.kql](../kql/ingestion_mapping.kql) | Define JSON mappings |
| [../kql/realtime_queries.kql](../kql/realtime_queries.kql) | Operational analysis |
| [../kql/dashboard_queries.kql](../kql/dashboard_queries.kql) | Dashboard tile queries |
| [../kql/alert_queries.kql](../kql/alert_queries.kql) | Activator candidate rules |

## KQL Best Practices

- Always filter by time for dashboard queries.
- Use `summarize` for aggregations and tile-friendly outputs.
- Use `arg_max()` to get latest state per shipment or vehicle.
- Use clear column names for business users.
- Keep alert queries narrow and easy to explain.
- Test query cost and latency before using high refresh rates.

## Example Pattern

```kusto
ShipmentEvents
| where event_timestamp > ago(30m)
| summarize arg_max(event_timestamp, *) by shipment_id
| where delay_minutes > 30
| project shipment_id, vehicle_id, customer_region, destination, delay_minutes, current_eta
```

## Operational Recommendation

Treat KQL query files as reusable assets. The same query logic can support troubleshooting, dashboards, alert rules, and demo scripts.
