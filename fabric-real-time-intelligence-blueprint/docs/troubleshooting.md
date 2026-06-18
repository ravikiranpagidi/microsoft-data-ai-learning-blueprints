# Troubleshooting

## Purpose

This page lists common issues when running the blueprint.

## Local Event Generator

| Issue | Cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError` | Dependencies not installed | Run `pip install -r requirements.txt` |
| Output file missing | Wrong relative path | Use an explicit output path |
| Event Hubs send fails | Missing environment variables | Set `EVENTHUB_CONNECTION_STR` and `EVENTHUB_NAME` |
| Too many events generated | Count or interval too high | Lower `--count` or increase `--interval-seconds` |

## Eventstream

| Issue | Cause | Fix |
| --- | --- | --- |
| Events not visible | Source not connected | Verify source connection and event format |
| Destination not receiving events | Route not configured | Check Eventstream destination settings |
| Schema mismatch | Event field names differ | Compare payload with files under `schemas/` |

## Eventhouse And KQL

| Issue | Cause | Fix |
| --- | --- | --- |
| Table creation fails | Wrong database context | Open the target KQL database |
| Query returns no rows | Time filter too narrow | Extend `ago()` window |
| Delay query looks wrong | Event timestamps not UTC | Normalize timestamps before ingestion |
| Dashboard slow | Query scans too much data | Add time filters and summarize earlier |

## Activator

| Issue | Cause | Fix |
| --- | --- | --- |
| Alert not firing | Condition not met | Test the KQL logic first |
| Too many alerts | Rule too sensitive | Add thresholds, time windows, or repeat logic |
| Wrong owner receives alert | Channel not documented | Review alert ownership matrix |

## Power BI

| Issue | Cause | Fix |
| --- | --- | --- |
| Measures disagree with dashboard | Different data grain | Align Gold tables with dashboard metric definitions |
| Report model too complex | Raw events loaded directly | Use curated Lakehouse tables |
| Slow report page | Too much detail in visual | Add aggregates and date filters |

## Recommended Debug Order

1. Validate local event payload.
2. Validate Eventstream source.
3. Validate Eventhouse table schema.
4. Validate ingestion mapping.
5. Run KQL query with a broad time window.
6. Narrow query to dashboard or alert use case.
7. Validate downstream Lakehouse or Power BI output.
