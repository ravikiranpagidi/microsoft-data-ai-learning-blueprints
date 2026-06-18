# Troubleshooting

## Purpose

Help users diagnose common setup and demo issues.

## Common Issues

| Issue | Fix |
| --- | --- |
| Events are not generated | Reinstall Python requirements |
| Event Hubs send fails | Check environment variables |
| KQL query returns no rows | Increase the time window |
| Dashboard tile is blank | Validate table and time filters |
| Alert does not fire | Test the KQL condition directly |
| Power BI metrics disagree | Check table grain and metric definitions |

## Debug Order

1. Validate local event payload.
2. Validate Eventstream source.
3. Validate Eventhouse table schema.
4. Validate ingestion mapping.
5. Run KQL queries manually.
6. Validate dashboard and alert logic.
7. Validate Lakehouse and Power BI outputs.

Previous: [Cost Optimization](Cost-Optimization) | Next: [Roadmap](Roadmap)
