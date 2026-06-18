# Demo Script

## Purpose

This script supports a 10 to 15 minute presentation for a Fabric community event, data engineering meetup, portfolio review, student workshop, or enterprise proof-of-concept discussion.

## Audience

- Microsoft Fabric community.
- Data engineering meetup.
- MVP portfolio review.
- Student workshop.
- Enterprise stakeholders.

## Demo Flow

### 1. Business Problem, 1 minute

"We are looking at a smart logistics scenario. Delivery vehicles, shipment systems, warehouse sensors, and customer applications are producing operational events all day. The operations team needs to see delays as they happen, identify SLA risks, detect warehouse temperature problems, and preserve history for reporting and future predictive use cases."

### 2. Architecture, 2 minutes

Show the architecture diagram.

"The flow starts with operational sources. Events land in Fabric Eventstream, optionally through Azure Event Hubs. Eventstream routes events to Eventhouse for low-latency KQL queries and live dashboards. Fabric Activator watches for business conditions and triggers actions. Lakehouse stores historical events and curated summaries. Power BI consumes the curated layer for business reporting. The same historical data can later become AI-ready feature tables."

### 3. Event Generator, 2 minutes

Run:

```powershell
python generate_events.py --config config.example.json --count 100 --output ../../samples/generated-events.jsonl
```

"The generator creates three event types: shipment status, vehicle telemetry, and warehouse sensor events. The code uses fictional data and environment variables for secrets. For a local demo, we write JSON lines. For a streaming demo, we can send to Azure Event Hubs or a Fabric Eventstream endpoint pattern."

### 4. Eventhouse And KQL, 3 minutes

Open the KQL scripts.

"The tables represent the operational streams. The KQL examples answer practical questions: latest shipment status, delayed shipments, average delay by region, vehicle anomalies, warehouse temperature breaches, event volume by minute, and SLA breach candidates."

Run or explain a latest-delayed-shipments query.

### 5. Real-Time Dashboard, 2 minutes

"These dashboard queries can become tiles. The dashboard is for operational awareness: what is happening now, which shipments need attention, and which locations or vehicles are showing risk."

Show suggested tiles:

- Delayed shipment count.
- Average delay by region.
- Vehicle health anomalies.
- Warehouse temperature breaches.
- Event volume by minute.

### 6. Activator Alert, 2 minutes

"A dashboard tells the team what is happening. Activator helps the team act. For example, if a shipment delay exceeds 30 minutes or a warehouse temperature exceeds the allowed range, the rule can notify an operations team."

Show the alert examples file and explain one condition.

### 7. Lakehouse And Power BI, 2 minutes

"Eventhouse is the operational query layer. Lakehouse is the historical analytics layer. We keep raw events in Bronze, clean them in Silver, and build Gold summaries for Power BI. Power BI is where leaders review SLA trends, route performance, vehicle health, and warehouse condition history."

### 8. AI-Ready Extension, 1 minute

"The same curated data can become features for delay prediction or anomaly detection. For example, route history, weather, vehicle health, and warehouse events can help estimate delay risk before the SLA is breached."

## Closing

"This blueprint is intentionally more than a hello-world stream. It shows the design shape of a real Fabric Real-Time Intelligence solution: ingestion, operational query, visualization, action, historical analytics, governance, and AI readiness."
