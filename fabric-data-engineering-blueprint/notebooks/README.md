# Notebooks

These notebooks are written in Fabric-compatible PySpark style. Import them into a Fabric workspace, attach them to your Lakehouse, and run them in numeric order.

## Execution Order

| Order | Notebook | Purpose |
| --- | --- | --- |
| 00 | 00_setup_lakehouse.ipynb | Parameters, paths, and helper functions |
| 01 | 01_bronze_ingestion.ipynb | Source CSV to Bronze Delta tables |
| 02 | 02_silver_transformation.ipynb | Data cleaning, typing, deduplication, validation |
| 03 | 03_gold_dimensional_model.ipynb | Star schema dimensions and fact table |
| 04 | 04_data_quality_checks.ipynb | Rule-based data quality checks |
| 05 | 05_delta_optimization.ipynb | Delta maintenance pattern |
| 06 | 06_powerbi_ready_views.ipynb | Power BI-ready shape validation |
| 07 | 07_incremental_load_pattern.ipynb | Watermark-based incremental load pattern |
| 08 | 08_operational_monitoring_examples.ipynb | Audit tables, run status, freshness, and quality monitoring examples |

## Fabric Assumptions

- A default Lakehouse is attached to the notebook.
- Sample files are uploaded to <code>Files/retail_banking/source/</code>.
- Tables are created in the attached Lakehouse using <code>saveAsTable</code>.
- SQL endpoint scripts in <code>sql/</code> are used for persistent consumption views.

## Practice Ideas

- Add a new row to transactions.csv and rerun notebook 07 to see how the watermark changes.
- Add a failing condition to a Gold table and rerun notebook 08 to see how quality status could be tracked.
- Convert the audit examples into a small operational dashboard for data engineers.
