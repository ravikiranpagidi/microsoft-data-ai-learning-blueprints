# SQL Analytics Endpoint

## Concept

The SQL analytics endpoint lets users query Lakehouse Delta tables using SQL without moving data into a separate SQL database.

## Why It Matters

It gives SQL and BI users a familiar access path to curated lakehouse data while engineering teams continue to use Delta and Spark.

## How It Works in Microsoft Fabric

When Lakehouse tables are created, they can be visible through the SQL analytics endpoint. Teams can create SQL views for business-friendly names, shaping, and metrics.

## Real-World Use Case

The retail banking Gold tables are queried through SQL views such as customer profile, account summary, monthly transaction summary, and branch activity.

## Beginner Explanation

Spark creates the tables. SQL analytics endpoint lets business and BI users read them with SQL.

## Enterprise Best Practice

Expose Gold tables and views through the SQL endpoint. Avoid encouraging report authors to query Bronze or unvalidated Silver tables.

## Common Mistakes

- Expecting the SQL endpoint to replace all warehouse features.
- Creating views over raw data with no quality checks.
- Using technical table names directly in reports.
- Putting sensitive PII in open consumption views.

## Practical Recommendation

Create business-friendly SQL views over Gold tables and use those views for Power BI consumption.
