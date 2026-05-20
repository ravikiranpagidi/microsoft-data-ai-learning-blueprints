# Why Start With Direct Lake for Fabric Power BI

## Status

Accepted

## Context

The blueprint publishes Gold Delta tables in a Fabric Lakehouse and expects Power BI to consume governed curated data. Power BI can use Direct Lake or Import mode depending on model requirements, data size, source shape, and feature needs.

## Decision

Start with Direct Lake for Fabric-native Gold tables because it avoids unnecessary data duplication and aligns the semantic model with OneLake-backed data. Use Import mode when the model is small, mixed-source, heavily shaped in Power Query, or blocked by Direct Lake limitations.

## Consequences

Direct Lake keeps the architecture more Fabric-native and can reduce refresh duplication. Teams must still understand Direct Lake behavior, fallback conditions, permissions, and semantic model design. Import mode remains a valid option when compatibility or transformation requirements matter more than avoiding duplication.

## Alternatives Considered

Always use Import mode, always use Direct Lake, or use DirectQuery-only consumption.

## Recommendation

Document the mode decision for each semantic model. For this blueprint, Direct Lake is the recommended starting point for Gold Lakehouse tables, with Import mode as a pragmatic fallback when needed.
