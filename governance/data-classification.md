# Data Classification

## Classification Levels

| Level | Description | Example |
| --- | --- | --- |
| Public | Safe to share externally | Public product category descriptions |
| Internal | Business data not intended for public use | Branch region summaries |
| Confidential | Sensitive business or customer data | Account balances, transaction detail |
| Restricted | Highly sensitive regulated data | Customer PII, account identifiers when linked to identity |

## Retail Banking Classification Examples

| Field | Classification | Reason |
| --- | --- | --- |
| customer_id | Confidential | Customer-linked identifier |
| email | Restricted | Direct PII |
| phone | Restricted | Direct PII |
| customer_segment | Confidential | Business segmentation |
| current_balance | Confidential | Financial value |
| transaction_amount | Confidential | Financial transaction detail |
| branch_region | Internal | Operational grouping |

## Classification Template

| Table | Column | Classification | Owner | Masking required | Notes |
| --- | --- | --- | --- | --- | --- |
| dim_customer | email | Restricted | Customer Data Owner | Yes | Exclude from broad views |
| dim_account | current_balance | Confidential | Account Data Owner | No, restrict access | Use aggregate reporting where possible |

## Recommendation

Classify fields before publishing Gold views or semantic models. It is easier to prevent exposure than to clean it up after reports are shared.
