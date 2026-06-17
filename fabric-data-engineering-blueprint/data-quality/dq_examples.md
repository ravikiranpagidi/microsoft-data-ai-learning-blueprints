# Data Quality Examples

## Example Rule

~~~yaml
- name: account_customer_integrity
  type: referential_integrity
  column: customer_id
  parent_table: silver_customers
  parent_column: customer_id
  severity: critical
~~~

## Example Output

| Table | Rule | Status | Failed Count | Meaning |
| --- | --- | --- | ---: | --- |
| silver_customers | customer_id_not_null | PASS | 0 | Every customer has a key |
| silver_accounts | account_customer_integrity | PASS | 0 | Every account maps to a customer |
| silver_transactions | transaction_account_integrity | FAIL | 3 | Three transactions reference missing accounts |

## Practical Guidance

- Fail the pipeline for critical rules.
- Route warning rules to a data steward review queue.
- Keep row count reconciliation near ingestion and before consumption refresh.
- Store historical quality results so trends can be monitored over time.
