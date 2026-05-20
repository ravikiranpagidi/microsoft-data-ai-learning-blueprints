# Why Medallion Architecture

## Status

Accepted

## Context

The project starts with raw CSV files and needs to support learning, auditability, debugging, data quality, and business-ready consumption.

## Decision

Use Bronze, Silver, and Gold layers in the Lakehouse. Bronze preserves raw data, Silver cleans and conforms data, and Gold publishes a dimensional model.

## Consequences

The design is easier to explain and troubleshoot. It adds some extra tables and notebook steps, but the structure is worth it for maintainability.

## Alternatives Considered

A single raw-to-report table, direct Power BI over CSV files, or a warehouse-only design.

## Recommendation

Use medallion architecture for the blueprint and teach each layer as a distinct quality checkpoint.
