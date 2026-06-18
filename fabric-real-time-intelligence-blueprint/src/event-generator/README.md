# Event Generator

## Purpose

This folder contains a simple but production-inspired event generator for the Smart Logistics and Operations Monitoring scenario.

It can generate:

- Shipment events.
- Vehicle telemetry events.
- Warehouse sensor events.

It supports:

- Local JSON Lines output.
- Optional Azure Event Hubs publishing.
- Optional HTTP endpoint publishing pattern for Fabric Eventstream custom ingestion scenarios.
- Configurable event count and interval.
- Environment variables for secrets.

## Quick Start

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python generate_events.py --config config.example.json --count 100 --output ../../samples/generated-events.jsonl
```

## Event Hubs Publishing

Set these environment variables:

```powershell
$env:EVENTHUB_CONNECTION_STR = "<connection string>"
$env:EVENTHUB_NAME = "logistics-events"
python send_to_eventhub.py --config config.example.json --count 100
```

## HTTP Endpoint Publishing

Set these environment variables:

```powershell
$env:FABRIC_EVENTSTREAM_ENDPOINT = "https://example"
$env:FABRIC_EVENTSTREAM_TOKEN = "<token if required>"
python send_to_fabric_eventstream.py --config config.example.json --count 100
```

## Notes

The generator intentionally uses fictional values. Do not replace the sample data with real customer, driver, vehicle, or shipment data in a public repository.
