# Eventstream Design

## Purpose

Explain how Eventstream receives, transforms, and routes real-time events.

## Eventstream Responsibilities

- Receive events from Event Hubs, custom apps, or supported sources.
- Apply lightweight transformations.
- Route streams to Eventhouse.
- Route selected streams to Lakehouse.
- Support Activator scenarios.

## Recommended Routes

| Event Type | Destination | Reason |
| --- | --- | --- |
| Shipment | Eventhouse | Delay and SLA monitoring |
| Vehicle | Eventhouse | Telemetry and anomaly monitoring |
| Warehouse | Eventhouse | Condition and temperature alerting |
| Selected clean events | Lakehouse | Historical analytics |

## Best Practices

- Keep transformations simple.
- Preserve raw fields.
- Route by event type.
- Validate timestamps.
- Monitor failed events.

Previous: [Event Generator](Event-Generator) | Next: [Eventhouse and KQL](Eventhouse-and-KQL)
