# Semantic Model Notes

## Purpose

This file describes a practical Power BI semantic model for the logistics monitoring scenario.

## Recommended Tables

Facts:

- `shipment_sla_summary`
- `route_delay_summary`
- `vehicle_health_summary`
- `warehouse_condition_summary`

Dimensions:

- `dim_date`
- `dim_region`
- `dim_route`
- `dim_vehicle`
- `dim_warehouse`

## Relationship Guidance

- Relate `shipment_sla_summary[event_date]` to `dim_date[date]`.
- Relate route summaries to `dim_route[route_id]`.
- Relate vehicle summaries to `dim_vehicle[vehicle_id]`.
- Relate warehouse summaries to `dim_warehouse[warehouse_id]`.

## Metric Governance

Document these business definitions:

- Total Shipments.
- Delayed Shipments.
- Delay Rate.
- Average Delay Minutes.
- SLA Breach Count.
- Active Vehicles.
- Temperature Breach Count.
- On-Time Delivery Percentage.

## Recommendation

Use the real-time dashboard for live monitoring and Power BI for curated trend analysis, executive reporting, and reusable business metrics.
