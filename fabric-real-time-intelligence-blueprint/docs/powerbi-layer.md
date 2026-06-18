# Power BI Layer

## Purpose

This page explains how Power BI fits into the real-time intelligence architecture.

## Role Of Power BI

Real-Time Dashboards are best for live operational monitoring. Power BI is best for governed business reporting, trend analysis, executive views, and semantic model reuse.

In this blueprint, Power BI should consume curated Lakehouse Gold tables or views rather than raw event streams.

## Recommended Report Pages

| Page | Purpose |
| --- | --- |
| Executive Operations Overview | High-level SLA, delay, vehicle, and warehouse health metrics |
| Real-Time Shipment Monitoring | Current shipment status and active delay indicators |
| Delay and SLA Analysis | Delay trends by route, region, carrier, and time |
| Vehicle Health | Engine temperature, fuel level, harsh braking, and telemetry gaps |
| Warehouse Conditions | Temperature, humidity, vibration, and door-open activity |
| Regional Performance | Regional shipment volume, delay rate, and SLA performance |

## Semantic Model Guidance

Recommended fact tables:

- `fact_shipment_status`
- `fact_vehicle_telemetry`
- `fact_warehouse_conditions`
- `fact_sla_events`

Recommended dimensions:

- `dim_date`
- `dim_time`
- `dim_vehicle`
- `dim_route`
- `dim_region`
- `dim_warehouse`
- `dim_shipment_status`

## Model Design Rules

- Use a star schema for reporting.
- Keep raw event IDs in detail tables, not every summary table.
- Create business-friendly measure names.
- Hide technical columns from report consumers.
- Document metric definitions.
- Avoid doing heavy transformations in Power BI if they belong in Lakehouse.

## Related Files

- [../powerbi/semantic-model-notes.md](../powerbi/semantic-model-notes.md)
- [../powerbi/measures.dax](../powerbi/measures.dax)
- [../powerbi/report-layout.md](../powerbi/report-layout.md)
