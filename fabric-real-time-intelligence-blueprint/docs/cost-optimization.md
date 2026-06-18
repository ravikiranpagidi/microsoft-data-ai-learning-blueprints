# Cost Optimization

## Purpose

This page gives practical cost and capacity guidance for the blueprint.

## Main Cost Drivers

| Area | Cost Driver |
| --- | --- |
| Event ingestion | Event volume, message size, source connectors |
| Eventhouse | Retention, query frequency, compute usage, concurrency |
| Dashboards | Refresh interval, number of tiles, number of users |
| Activator | Number of rules, rule complexity, event volume |
| Lakehouse | Storage, transformation jobs, retention, Power BI usage |
| Power BI | Model size, refresh mode, Direct Lake or Import behavior |

## Practical Controls

- Start demos with low event rates.
- Use realistic event volumes during load testing.
- Filter dashboard queries to short time windows.
- Use summary queries for dashboard tiles.
- Retain raw events only as long as needed.
- Use Lakehouse summary tables for historical Power BI reporting.
- Avoid running exploratory KQL queries against very broad time windows.
- Review capacity usage after demo runs.

## Demo Settings

Recommended for local demo:

| Setting | Value |
| --- | --- |
| Event count | 100 to 1,000 |
| Event interval | 0.1 to 1 second |
| Dashboard time window | Last 15 to 60 minutes |
| Raw retention | Short for demo |
| Power BI model | Curated Gold tables |

## Enterprise Considerations

- Estimate events per second before production.
- Understand retention and compliance requirements.
- Separate development load tests from production workspaces.
- Monitor Eventhouse and capacity metrics.
- Define alert noise thresholds.
- Document when to scale Fabric capacity.
