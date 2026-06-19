# Troubleshooting

## Purpose

This page lists common implementation issues and practical fixes.

## Common Issues

| Problem | Likely Cause | Fix |
| --- | --- | --- |
| Notebook cannot read files | Wrong raw path or missing permissions | Check `raw_base_path` and Unity Catalog permissions |
| Catalog creation fails | User lacks catalog privileges | Ask platform admin to grant catalog permissions |
| DQ checks fail | Required key or reference data issue | Inspect failed rows and fix Silver transformation rules |
| Power BI cannot connect | Gold tables unavailable or permissions missing | Confirm Gold table exists and grant read access |
| Pipeline parameter not passed | ADF activity base parameters missing | Review pipeline JSON and notebook widgets |
| Local tests fail | Sample data or schema contract mismatch | Fix CSV headers or schema JSON |

## Debugging Steps

1. Confirm the failing layer.
2. Check row counts.
3. Inspect schema.
4. Check null and duplicate keys.
5. Confirm table permissions.
6. Review ADF and Databricks run logs.
7. Re-run only the failed layer when possible.

## Related Pages

- [Setup Guide](Setup-Guide)
- [ADF Pipelines](ADF-Pipelines)
- [Data Quality](Data-Quality)

