# Setup Guide

## Purpose

This guide explains how to set up the blueprint for local event generation and Microsoft Fabric implementation practice.

## Prerequisites

- Microsoft Fabric workspace with capacity enabled.
- Permission to create Eventstream, Eventhouse, KQL Database, Lakehouse, Real-Time Dashboard, and Activator items.
- Python 3.10 or later.
- Optional Azure Event Hubs namespace if you want to route through Event Hubs.
- Basic familiarity with KQL and Power BI.

## Local Setup

```powershell
cd fabric-real-time-intelligence-blueprint/src/event-generator
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python generate_events.py --config config.example.json --count 100 --output ../../samples/generated-events.jsonl
```

## Fabric Setup

1. Create or open a Fabric workspace.
2. Create an Eventhouse.
3. Create a KQL database named `logistics_ops_kql`.
4. Run [../kql/create_tables.kql](../kql/create_tables.kql).
5. Run [../kql/ingestion_mapping.kql](../kql/ingestion_mapping.kql).
6. Create an Eventstream.
7. Add a source such as Event Hubs, custom endpoint, or sample stream.
8. Route shipment, telemetry, and warehouse events to the KQL database.
9. Create a Real-Time Dashboard from queries in [../kql/dashboard_queries.kql](../kql/dashboard_queries.kql).
10. Configure Activator rules using [data-activator-alerts.md](data-activator-alerts.md).
11. Create a Lakehouse for historical data and run the SQL files under [../lakehouse](../lakehouse).

## Optional Event Hubs Setup

If using Azure Event Hubs:

1. Create an Event Hubs namespace.
2. Create an event hub, for example `logistics-events`.
3. Store the connection string in `EVENTHUB_CONNECTION_STR`.
4. Store the event hub name in `EVENTHUB_NAME`.
5. Run:

```powershell
python send_to_eventhub.py --config config.example.json --count 100
```

## Expected Output

- JSONL sample events generated locally.
- KQL tables created in Eventhouse.
- Real-time queries return operational metrics.
- Dashboard tiles show delay, telemetry, warehouse, and volume metrics.
- Alert rules are documented and ready to configure.
- Lakehouse table designs are available for historical analysis.

## Beginner Troubleshooting

| Issue | Likely Cause | Fix |
| --- | --- | --- |
| No events generated | Python dependency issue | Reinstall dependencies from `requirements.txt` |
| Event Hubs send fails | Missing environment variable | Check `EVENTHUB_CONNECTION_STR` and `EVENTHUB_NAME` |
| KQL table creation fails | Wrong database context | Open the target KQL database before running scripts |
| Dashboard tile is blank | Time filter too narrow | Increase the dashboard time range |
| Alert does not fire | Rule condition not met | Test the KQL alert query directly first |
