# Architecture

This folder contains architecture views for the Retail Banking Customer Analytics blueprint.

## Diagram Index

| File | Purpose |
| --- | --- |
| fabric-end-to-end-architecture.md | Full flow from source files to Power BI |
| medallion-architecture.md | Bronze, Silver, Gold layering |
| data-product-architecture.md | Domain-oriented data product design |
| lakehouse-to-powerbi-flow.md | Consumption path from Lakehouse to semantic model |
| cicd-flow.md | Dev, Test, Prod deployment path |
| governance-model.md | Access, ownership, classification, and publishing model |

## Icon Guidance

The folder <code>architecture/assets/icons/</code> contains selected Fabric SVG icons sourced from the public <code>@fabric-msft/svg-icons</code> package for architecture documentation use. Keep labels beside icons, do not reshape icons, and follow Microsoft icon terms.

Official icon reference: https://learn.microsoft.com/fabric/fundamentals/icons

## Architecture Principles

- Keep raw data auditable.
- Make transformations explainable.
- Validate before publishing.
- Serve business users from Gold tables and views.
- Separate engineering, consumption, and governance responsibilities.
- Keep deployment paths repeatable and documented.
