# Power BI Consumption

## Concept

Power BI should consume curated Gold tables or business-friendly SQL views, not raw engineering tables.

## Why It Matters

A semantic model is where business metrics, relationships, security behavior, and user-friendly names come together.

## How It Works in Microsoft Fabric

Power BI can connect to Fabric Lakehouse tables, SQL analytics endpoint views, or semantic models in the Fabric workspace.

## Real-World Use Case

The banking dashboard uses Gold dimensions and fact_transaction to show active customers, product usage, branch activity, and transaction trends.

## Beginner Explanation

Power BI is the storytelling and metric layer. It should not be where raw data gets cleaned.

## Enterprise Best Practice

Use a star schema, clear measure definitions, relationship direction discipline, and shared certified semantic models for enterprise reporting.

## Common Mistakes

- Building reports directly on Bronze tables.
- Creating one wide table for every dashboard without governance.
- Duplicating metric logic across many reports.
- Using ambiguous measure names like Amount or Count.

## Practical Recommendation

Use the Gold star schema and the measure definitions in semantic-model/measures.md.
