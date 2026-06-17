# Environment Configuration

## Configuration Values

| Setting | Dev example | Test example | Prod example |
| --- | --- | --- | --- |
| Workspace | fab-retailbank-dev | fab-retailbank-test | fab-retailbank-prod |
| Lakehouse | lh_retailbank_dev | lh_retailbank_test | lh_retailbank_prod |
| Source folder | Files/retail_banking/source | Files/retail_banking/source | Files/retail_banking/source |
| Batch audit table | audit_pipeline_run_dev | audit_pipeline_run_test | audit_pipeline_run_prod |
| Semantic model | sm_retailbank_customer_analytics_dev | sm_retailbank_customer_analytics_test | sm_retailbank_customer_analytics |

## Parameterization Pattern

Pass these values from pipeline parameters into notebooks:

- environment
- batch_id
- source_base_path
- load_type
- run_optimization

## Recommendation

Do not hardcode production workspace or Lakehouse IDs inside notebooks. Keep notebooks portable and parameter-driven.
