# Why Use Dev Test Prod Workspaces

## Status

Accepted

## Context

Fabric items change over time, and production analytics need controlled release practices.

## Decision

Use separate Dev, Test, and Prod workspaces with Git integration and deployment pipeline guidance.

## Consequences

Changes become easier to review and promote. Teams need discipline around parameters and environment-specific configuration.

## Alternatives Considered

Single shared workspace or direct production edits.

## Recommendation

Use separate lifecycle workspaces before any enterprise proof of concept becomes operational.
