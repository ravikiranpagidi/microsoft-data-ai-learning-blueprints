# Security and Governance

## Concept

Governance defines who owns data, who can access it, how sensitive data is classified, and how changes are controlled.

## Why It Matters

Data engineering platforms become risky when every user can access every layer and no one owns definitions.

## How It Works in Microsoft Fabric

Fabric governance uses workspace roles, item permissions, sensitivity labels, endorsement, lineage, data access controls, and organizational policies.

## Real-World Use Case

PII such as customer email, phone, and address should be classified and restricted. Gold consumption views should expose only the fields needed for analytics.

## Beginner Explanation

Security is not only passwords. It is deciding who should see what data and why.

## Enterprise Best Practice

Apply least privilege, classify PII, define owners and stewards, and make Gold the default access layer for consumers.

## Common Mistakes

- Making everyone workspace admin.
- Publishing PII into broad consumption views.
- Not documenting metric ownership.
- Confusing development access with production access.

## Practical Recommendation

Use the governance checklist before publishing any Gold table or semantic model.
