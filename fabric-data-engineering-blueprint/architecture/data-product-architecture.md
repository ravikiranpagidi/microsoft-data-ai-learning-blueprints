# Data Product Architecture

A data product is a governed, reusable data asset with ownership, documentation, quality expectations, and clear consumers.

~~~mermaid
flowchart LR
    domain["Retail Banking domain"] --> owner["Data owner"]
    owner --> steward["Data steward"]
    steward --> product["Customer analytics data product"]
    product --> contract["Data contract<br/>keys, definitions, SLA"]
    product --> gold["Gold tables<br/>dimensions and facts"]
    product --> semantic["Certified semantic model"]
    product --> consumers["Analysts, executives, branch managers"]
~~~

## Data Product Contents

- Purpose and business questions.
- Owner and steward.
- Source systems and refresh expectations.
- Tables, keys, and metric definitions.
- Data quality rules.
- Access model.
- Lineage and release history.

## Decision Guides

### Gold Table vs View

Use Gold tables for reusable curated entities such as dimensions and facts. Use SQL views for business-friendly projections, metric convenience, and consumption-specific naming.

### Star Schema vs Wide Table

Use a star schema when multiple reports and semantic models need consistent dimensions and measures. Use a wide table only when a narrow consumption use case needs a single denormalized export and the trade-off is documented.
