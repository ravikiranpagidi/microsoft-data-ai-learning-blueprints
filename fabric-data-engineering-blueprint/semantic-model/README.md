# Semantic Model

This folder explains how to design a Power BI semantic model on top of the Gold star schema.

## Files

| File | Purpose |
| --- | --- |
| semantic_model_design.md | Recommended model structure and relationships |
| measures.md | Example DAX measures and metric definitions |
| powerbi_model_guidelines.md | Modeling, naming, and report author guidance |
| business_glossary.md | Business-friendly definitions for data elements and metrics |

## Recommended Model Pattern

Use Gold tables as the model foundation:

- fact_transaction as the central fact table.
- dim_customer, dim_account, dim_product, dim_branch, and dim_date as dimensions.
- One-to-many relationships from dimensions to the fact table.
- Measures defined once and reused across reports.
