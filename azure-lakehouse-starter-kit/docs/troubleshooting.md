# Troubleshooting

## Common Issues

| Issue | Likely Cause | Fix |
| --- | --- | --- |
| ADF copy fails | Linked service or path issue | Validate linked service and dataset parameters |
| No files in raw | Metadata disabled or wrong source path | Check metadata table active flag and source path |
| Databricks notebook fails | Missing parameter or path | Validate widget values and config |
| Silver table has no rows | Bronze data quality failure | Review quarantine and DQ results |
| Duplicate records | Missing business key logic | Add dedupe using keys and event timestamp |
| Power BI numbers differ | Wrong grain or raw table used | Use Gold tables and documented measures |
| CI fails JSON validation | Invalid ADF artifact syntax | Run local JSON validation |

## Debug Order

1. Check source metadata.
2. Check raw file arrival.
3. Check Bronze row counts.
4. Check Silver validation results.
5. Check DQ results.
6. Check Gold table grain.
7. Check Power BI measure definitions.
