# OneLake Explained

## Concept

OneLake is the shared data lake foundation for Microsoft Fabric. It gives Fabric items a common storage layer and a consistent way to organize data.

## Why It Matters

A shared storage foundation reduces data duplication and helps teams discover and reuse data across Fabric workloads.

## How It Works in Microsoft Fabric

Lakehouses store Files and Tables in OneLake. Shortcuts can reference data in external locations or other Fabric items without physically copying it.

## Real-World Use Case

A bank can keep retail banking source files in a Lakehouse, expose curated Gold tables to Power BI, and use shortcuts for shared reference data such as branch regions.

## Beginner Explanation

OneLake is like the shared file system behind Fabric analytics. Lakehouse Files hold raw files; Lakehouse Tables expose Delta tables.

## Enterprise Best Practice

Use a clear folder and table layout. Separate raw, curated, and published assets. Control access through workspace roles, item permissions, and governance processes.

## Common Mistakes

- Treating OneLake like an unmanaged dumping ground.
- Copying data repeatedly when a shortcut would be better.
- Using shortcuts without documenting ownership and freshness.
- Mixing raw files and published tables without clear layers.

## Practical Recommendation

Use OneLake as the shared storage backbone, but still apply data architecture discipline.
