# Why Use Delta Tables

## Status

Accepted

## Context

The Lakehouse needs reliable table storage, schema handling, Spark compatibility, and SQL endpoint consumption.

## Decision

Write Bronze, Silver, and Gold outputs as Delta tables.

## Consequences

Delta supports reliable lakehouse engineering patterns and integrates well with Fabric. Teams must still manage optimization, retention, and schema evolution carefully.

## Alternatives Considered

CSV-only storage, Parquet-only unmanaged files, or direct warehouse tables for every layer.

## Recommendation

Use Delta tables for lakehouse layers and reserve raw CSV files for source landing only.
