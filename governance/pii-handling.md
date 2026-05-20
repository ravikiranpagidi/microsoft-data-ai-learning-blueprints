# PII Handling

## PII Fields in the Sample Domain

- Customer name
- Email
- Phone
- Date of birth
- Customer-linked account identifiers

## Handling Recommendations

| Pattern | Use when | Example |
| --- | --- | --- |
| Exclude | Field is not needed for analytics | Do not expose email in public Gold views |
| Mask | Users need partial identity context | Show masked email such as a***@example.com |
| Hash | Need matching without direct identity | Hash customer_id in a sandbox export |
| Aggregate | Individual detail is not needed | Show segment-level transaction totals |
| Restrict | Detail is required by approved users | Limit transaction detail to approved analyst group |

## SQL View Recommendation

Do not expose email, phone, or full date of birth in broad Power BI consumption views. Keep these fields in restricted dimensions only when there is a documented use case.

## Notebook Recommendation

Avoid writing raw PII to debug logs. Use row counts, rule names, and masked samples when troubleshooting.

## Production Checklist

- PII fields classified.
- Access reviewed by data owner.
- Masking or exclusion applied to shared views.
- Semantic model fields hidden where not needed.
- Export permissions reviewed.
