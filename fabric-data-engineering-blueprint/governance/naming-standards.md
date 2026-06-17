# Naming Standards

## Workspace Names

| Environment | Pattern | Example |
| --- | --- | --- |
| Dev | fab-domain-dev | fab-retailbank-dev |
| Test | fab-domain-test | fab-retailbank-test |
| Prod | fab-domain-prod | fab-retailbank-prod |

## Fabric Item Names

| Item | Pattern | Example |
| --- | --- | --- |
| Lakehouse | lh_domain_env | lh_retailbank_dev |
| Notebook | nn_step_subject | nn_01_bronze_ingestion |
| Pipeline | pl_action_subject | pl_ingest_retail_banking_csv |
| Semantic model | sm_domain_subject | sm_retailbank_customer_analytics |
| Report | rpt_domain_subject | rpt_retailbank_customer_analytics |

## Table Names

| Layer | Pattern | Example |
| --- | --- | --- |
| Bronze | bronze_entity | bronze_transactions |
| Silver | silver_entity | silver_transactions |
| Gold Dimension | dim_entity | dim_customer |
| Gold Fact | fact_event | fact_transaction |

## SQL View Names

| Type | Pattern | Example |
| --- | --- | --- |
| Dimension view | vw_dim_entity | vw_dim_customer |
| Fact view | vw_fact_event | vw_fact_transaction |
| Power BI view | vw_powerbi_subject | vw_powerbi_monthly_transaction_summary |

## Recommendation

Names should make ownership, layer, purpose, and environment obvious without opening the item.
