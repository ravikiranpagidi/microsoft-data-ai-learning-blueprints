# Fabric Activator Alert Examples

## Purpose

This page documents alert scenarios for the logistics monitoring blueprint.

Fabric Activator is used to detect conditions in operational data and trigger actions. In this blueprint, alert rules are designed for logistics operations teams.

## Alert Scenarios

| Alert | Business Meaning | Trigger Condition | Recommended Action | Notification Channel |
| --- | --- | --- | --- | --- |
| Shipment delay exceeds 30 minutes | A shipment is already late enough to need attention | Latest shipment delay is greater than 30 minutes | Contact dispatcher, update ETA, notify customer if needed | Teams channel or email |
| SLA breach risk is high | Shipment is likely to miss committed delivery window | Delay is greater than 20 minutes and ETA is after planned delivery | Escalate to operations lead | Teams channel |
| Vehicle engine temperature exceeds threshold | Vehicle may need maintenance intervention | Engine temperature is greater than 225 F | Ask driver to inspect vehicle and notify fleet team | Teams and maintenance queue |
| Warehouse temperature outside range | Temperature-sensitive goods may be at risk | Temperature is less than 35 F or greater than 45 F for refrigerated zone | Notify warehouse supervisor | Email and incident queue |
| No telemetry received for 10 minutes | Vehicle may have connectivity or device problem | No latest telemetry event for vehicle in 10 minutes | Contact driver or inspect device | Teams channel |
| Repeated delay on same route | Route may have systemic congestion or planning issue | Three or more delayed shipments on route in one hour | Review route plan and dispatch capacity | Operations review queue |

## Sample KQL Alert Conditions

### Shipment Delay Exceeds 30 Minutes

```kusto
ShipmentEvents
| where event_timestamp > ago(15m)
| summarize arg_max(event_timestamp, *) by shipment_id
| where delay_minutes > 30
```

### Vehicle Engine Temperature

```kusto
VehicleTelemetry
| where event_timestamp > ago(5m)
| summarize arg_max(event_timestamp, *) by vehicle_id
| where engine_temperature > 225
```

### Warehouse Temperature Breach

```kusto
WarehouseSensorEvents
| where event_timestamp > ago(10m)
| where temperature < 35 or temperature > 45
| summarize breach_count = count() by warehouse_id, zone_id, bin(event_timestamp, 5m)
| where breach_count >= 2
```

## Design Guidance

- Keep alert conditions explainable.
- Avoid noisy alerts by adding time windows and repeat thresholds.
- Define alert owner, action, and escalation path.
- Review alerts weekly during proof-of-concept phases.
- Use dashboard tiles to validate alert logic before enabling notifications.
