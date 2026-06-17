# Common Mistakes

## Concept

Common Fabric mistakes usually come from treating the platform as a collection of screens rather than an engineered analytics system.

## Why It Matters

Avoiding common mistakes saves rework and helps teams build trust with business users.

## How It Works in Microsoft Fabric

Fabric makes it easy to create items quickly, but teams still need architecture, governance, testing, and deployment practices.

## Real-World Use Case

In banking analytics, a quick report on raw transactions may look useful until duplicate accounts, missing branch keys, and inconsistent status values break trust.

## Beginner Explanation

Fast demos are helpful, but production solutions need repeatable structure.

## Enterprise Best Practice

Review common mistakes in every design review and pull request.

## Common Mistakes

- Using raw files as reporting sources.
- Ignoring medallion layers.
- Mixing PII and public metrics.
- Building a semantic model without relationships documented.
- Manually changing production items.
- Skipping data freshness checks.
- Not aligning with tenant governance policies.

## Practical Recommendation

Use the checklist in this file before declaring a Fabric proof of concept successful.

## Decision Guides

### Gold Table vs View

Use a Gold table when the data is reused, quality checked, and part of the curated model. Use a view when the shape is consumption-specific, lightweight, or a business-friendly projection.

### Star Schema vs Wide Table

Use a star schema for governed analytics, reusable dimensions, and clean Power BI models. Use a wide table only for narrow, performance-driven, or export-oriented use cases with clear ownership.
