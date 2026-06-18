# Eventhouse And KQL

## Purpose

Explain how Eventhouse and KQL support operational analytics.

## Tables

- `ShipmentEvents`
- `VehicleTelemetry`
- `WarehouseSensorEvents`

## Query Use Cases

- Latest shipment status.
- Delayed shipments.
- Average delay by region.
- Vehicle telemetry anomalies.
- Warehouse temperature breaches.
- SLA breach candidates.
- Event volume by minute.
- Top delayed routes.

## Best Practices

- Use time filters.
- Use `arg_max()` for latest state.
- Keep dashboard queries narrow.
- Keep alert queries explainable.

Previous: [Eventstream Design](Eventstream-Design) | Next: [Lakehouse Integration](Lakehouse-Integration)
