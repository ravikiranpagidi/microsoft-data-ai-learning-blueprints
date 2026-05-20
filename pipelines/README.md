# Pipelines

This folder contains conceptual and template assets for Fabric Data Pipeline orchestration.

## Files

| File | Purpose |
| --- | --- |
| pipeline_overview.md | Explains the ingestion and transformation pipeline design |
| ingestion_pipeline_template.json | Template-style pipeline definition for copying source files |
| transformation_pipeline_template.json | Template-style pipeline definition for notebook orchestration |
| orchestration_pattern.md | Production orchestration guidance |

## Recommended Pattern

- Use a pipeline to copy or land files into Lakehouse Files.
- Pass parameters such as environment, batch ID, and source path into notebooks.
- Run Bronze ingestion before Silver transformation.
- Run data quality before Gold publication or consumption refresh.
- Log row counts and pipeline status for operations.
