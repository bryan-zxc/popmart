# l20drv_customers_by_country

- **Row count**: 8
- **Primary key**: country
- **Analysis script**: [l20drv_customers_by_country.sql](../../analysis/l20drv_customers_by_country.sql)

## Key Notes

- Each row represents a unique country with its customer count
- Aggregated from l10wrk_customers table
- Countries ordered by customer count (descending)

## Columns

### country (VARCHAR) — Categorical
- 8 distinct values
- Unique (primary key)
- Nulls: 0
- Values: United States (6,828), United Kingdom (1,944), Canada (1,553), Germany (1,473), Australia (1,420), Netherlands (733), France (670), Italy (645)

### customer_count (BIGINT) — Numeric
- Customer count per country
- Range: 645 to 6,828
- Nulls: 0
