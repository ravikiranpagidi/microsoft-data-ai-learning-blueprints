# Setup Guide

## Purpose

Set up the local generator and prepare the Fabric items needed for the blueprint.

## Prerequisites

- Fabric workspace with capacity.
- Permission to create Eventstream, Eventhouse, KQL Database, Dashboard, Activator, and Lakehouse items.
- Python 3.10 or later.
- Optional Azure Event Hubs.

## Local Generator

```powershell
cd fabric-real-time-intelligence-blueprint/src/event-generator
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python generate_events.py --config config.example.json --count 100 --output ../../samples/generated-events.jsonl
```

## Fabric Setup

1. Create Eventhouse.
2. Create a KQL database.
3. Run `kql/create_tables.kql`.
4. Run `kql/ingestion_mapping.kql`.
5. Create Eventstream.
6. Route events to KQL database.
7. Build dashboard tiles from `kql/dashboard_queries.kql`.
8. Configure Activator conditions from `docs/data-activator-alerts.md`.
9. Create a Lakehouse and review `lakehouse` SQL scripts.

## Expected Result

- Sample events generated.
- KQL tables available.
- Real-time queries return results.
- Dashboard and alert logic can be demonstrated.

Previous: [Architecture](Architecture) | Next: [Demo Walkthrough](Demo-Walkthrough)
