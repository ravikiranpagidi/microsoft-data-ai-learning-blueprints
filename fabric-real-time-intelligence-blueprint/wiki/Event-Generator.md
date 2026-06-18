# Event Generator

## Purpose

Explain the Python generator used to create synthetic logistics events.

## Event Types

- Shipment events.
- Vehicle telemetry events.
- Warehouse sensor events.

## Why It Exists

Real-time demos need live-looking data. The generator lets you test KQL queries, dashboards, and alert logic without using production systems.

## Configuration

Use `src/event-generator/config.example.json` to control:

- Event mix.
- Regions.
- Origins and destinations.
- Warehouses.
- Routes.
- Default event count.
- Default event interval.

## Security Note

Secrets are not stored in the config file. Event Hubs and endpoint credentials must use environment variables.

Previous: [Demo Walkthrough](Demo-Walkthrough) | Next: [Eventstream Design](Eventstream-Design)
