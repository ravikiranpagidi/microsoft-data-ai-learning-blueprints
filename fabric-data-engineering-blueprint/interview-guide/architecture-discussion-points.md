# Architecture Discussion Points

## Explain the End-to-End Flow

A strong answer should mention source files, pipeline orchestration, Lakehouse Files, Bronze ingestion, Silver cleaning, Gold star schema, SQL endpoint views, semantic model measures, Power BI dashboards, governance, and CI/CD.

## Explain Layer Responsibilities

- Bronze: raw and auditable.
- Silver: clean, typed, deduplicated, and conformed.
- Gold: business-ready facts and dimensions.

## Explain Trade-Offs

| Decision | Trade-off |
| --- | --- |
| Lakehouse over Warehouse | More flexible engineering; SQL-first teams may prefer Warehouse |
| Star schema over wide table | Better governance and reuse; requires modeling discipline |
| Views over direct table exposure | Better business naming and security; more objects to manage |
| Dev/Test/Prod | Better release control; more operational overhead |

## Strong Architecture Summary

For a first Fabric data engineering proof of concept, I would build a Lakehouse-centered medallion architecture. Data Pipelines handle orchestration, notebooks perform Spark transformations, Delta tables store Bronze/Silver/Gold layers, data quality gates protect the Gold model, SQL endpoint views simplify consumption, and Power BI uses a governed star schema semantic model. I would separate Dev, Test, and Prod workspaces and apply least privilege by layer.
