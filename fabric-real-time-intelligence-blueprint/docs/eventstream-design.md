# Eventstream Design

## Purpose

This page explains how to design Eventstream ingestion and routing for the logistics monitoring scenario.

## Eventstream Responsibilities

Eventstream should:

- Receive operational events from source systems.
- Apply lightweight transformations when needed.
- Route events to Eventhouse for real-time querying.
- Route selected events to Lakehouse for historical analytics.
- Keep the ingestion flow visible and understandable for operations and data teams.

## Sources

| Source | Example Event |
| --- | --- |
| Vehicle telemetry | Latitude, longitude, speed, fuel level, engine temperature |
| Shipment system | Shipment status, current ETA, delay minutes, planned delivery time |
| Warehouse sensors | Temperature, humidity, vibration, door-open state |
| Customer mobile app | Delivery reschedule, delivery instructions, pickup confirmation |
| ERP or order system | Order priority, customer region, shipment value |
| Weather API | Region, weather condition, temperature, severe weather indicator |

## Recommended Eventstream Routes

| Route | Destination | Reason |
| --- | --- | --- |
| Shipment events | Eventhouse shipment table | Real-time delay monitoring |
| Vehicle telemetry | Eventhouse telemetry table | Live vehicle health and location monitoring |
| Warehouse sensors | Eventhouse sensor table | Temperature and condition alerting |
| Selected clean streams | Lakehouse Bronze tables | Historical analytics and replay |
| Alert candidate streams | Activator | Business action rules |

## Transformation Guidance

Use Eventstream transformations for simple shaping:

- Select relevant columns.
- Rename fields to standard names.
- Convert simple types where supported.
- Filter obviously invalid events.
- Route by event type.

Avoid complex business logic in Eventstream. Put deeper business rules in KQL, Lakehouse transformations, or downstream semantic models.

## Production Notes

- Define event contracts before building dashboards.
- Include `event_timestamp` and source system timestamp when possible.
- Preserve raw payloads for audit and replay.
- Use separate streams or routing logic for event types.
- Monitor ingestion latency and dropped events.
- Document who owns each event source.
