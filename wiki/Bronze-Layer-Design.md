# Bronze Layer Design

> **Learning stage:** Implementation handbook
> **Blueprint anchor:** Retail Banking Customer Analytics on Microsoft Fabric
> **Outcome:** Apply bronze layer design to the Retail Banking Customer Analytics blueprint.
> **Navigate:** [Medallion Architecture](Medallion-Architecture) | [Home](Home) | [Silver Layer Design](Silver-Layer-Design)
> **Quick links:** [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)

## Purpose

Define the Bronze layer design, metadata requirements, auditability expectations, and validation checklist.

## Who Should Read This

Data engineers building ingestion, learners running notebook 01, and architects defining raw layer standards.

## Purpose of Bronze

Bronze stores source data as it arrived, with enough metadata to understand when, where, and how it was ingested. It is the landing table layer, not the business reporting layer.

## What to Store

- Source columns with minimal change.
- Ingestion timestamp.
- Source file name.
- Source system or entity name.
- Batch ID.
- Load date.

## What Not to Change

Avoid heavy business transformations in Bronze. Do not rename business fields unnecessarily. Do not convert values into final reporting categories. Do not remove records just because they are imperfect. Those responsibilities belong in Silver.

## Ingestion Metadata

| Metadata field | Purpose |
| --- | --- |
| _ingestion_timestamp | When the record was processed. |
| _source_file_name | Which file produced the record. |
| _source_system | Where the data came from. |
| _source_entity | Which entity was loaded. |
| _batch_id | Which run loaded the record. |
| _bronze_load_date | Date partitioning and audit helper. |

## Recommended Naming

Use bronze_entity_name, such as bronze_customers or bronze_transactions. Keep names lower case and predictable.

## Practical Example

Notebook 01 reads transactions.csv from Files and writes bronze_transactions. It preserves CSV columns as strings and adds metadata. It also writes bronze_ingestion_audit so row counts and failures are visible.

## Best Practices

- Log source and target row counts.
- Keep ingestion repeatable.
- Capture batch IDs.
- Preserve raw fields for replay.
- Do not expose Bronze as the main BI layer.

## Common Mistakes

| Mistake | Problem | Better approach |
| --- | --- | --- |
| Applying business rules in Bronze | Raw lineage is lost | Keep rules in Silver. |
| No batch ID | Troubleshooting is harder | Add batch metadata. |
| Overwriting without audit | Past loads disappear from monitoring | Persist ingestion audit rows. |

## Related Repo Files

- [notebooks/01_bronze_ingestion.ipynb](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/notebooks/01_bronze_ingestion.ipynb)
- [pipelines/ingestion_pipeline_template.json](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/pipelines/ingestion_pipeline_template.json)
- [data-quality/dq_rules.yml](https://github.com/ravikiranpagidi/fabric-data-engineering-blueprint/blob/main/data-quality/dq_rules.yml)

## Related Wiki Pages

- [Medallion Architecture](Medallion-Architecture)
- [Silver Layer Design](Silver-Layer-Design)
- [Governance and Security](Governance-and-Security)

## Summary Checklist

- [ ] Bronze tables preserve source structure.
- [ ] Ingestion metadata is present.
- [ ] Source and target row counts are logged.
- [ ] Bronze is not exposed as the primary reporting layer.

---

## Page Navigation

| Previous | Home | Next |
| --- | --- | --- |
| [Medallion Architecture](Medallion-Architecture) | [Home](Home) | [Silver Layer Design](Silver-Layer-Design) |

Helpful references: [FAQ](FAQ) | [Glossary](Glossary) | [Contributor Guide](Contributor-Guide)
