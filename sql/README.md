# SQL Scripts

Run these scripts in the Lakehouse SQL analytics endpoint after the Gold tables exist.

## Execution Order

1. create_gold_views.sql
2. business_metrics.sql
3. validation_queries.sql
4. powerbi_consumption_views.sql
5. advanced_analytics_examples.sql
6. operational_monitoring_examples.sql

## Notes

- The scripts use business-friendly naming for consumption.
- Adjust schema names if your SQL endpoint uses a different default schema.
- Keep sensitive PII out of broad consumption views unless approved by governance.
- Use advanced_analytics_examples.sql for practical ranking, trend, product usage, and deeper-analysis examples.
- Use operational_monitoring_examples.sql as a starting point for audit, freshness, and quality monitoring queries.
