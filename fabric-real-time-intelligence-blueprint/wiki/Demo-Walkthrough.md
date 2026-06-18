# Demo Walkthrough

## Purpose

Provide a presenter-friendly flow for a 10 to 15 minute demo.

## Flow

1. Explain the logistics monitoring problem.
2. Show the architecture.
3. Run the event generator.
4. Show events arriving in the real-time layer.
5. Query Eventhouse with KQL.
6. Explain dashboard tiles.
7. Trigger or explain an alert condition.
8. Show Lakehouse historical design.
9. Explain Power BI report pages.
10. Close with AI-ready extensions.

## Demo Talk Track

"This is a smart logistics scenario. The operations team needs to see delayed shipments, vehicle issues, warehouse condition breaches, and SLA risks while they are happening. Fabric Real-Time Intelligence gives us the streaming, querying, dashboard, and alerting layer. Lakehouse and Power BI give us the historical and business reporting layer."

## Files To Open

- `diagrams/README.md`
- `src/event-generator/generate_events.py`
- `kql/realtime_queries.kql`
- `kql/dashboard_queries.kql`
- `docs/data-activator-alerts.md`
- `powerbi/report-layout.md`

Previous: [Setup Guide](Setup-Guide) | Next: [Event Generator](Event-Generator)
