-- Customer counts aggregated by country
CREATE OR REPLACE TABLE l20drv_customers_by_country AS
SELECT
    country,
    COUNT(*) AS customer_count
FROM l10wrk_customers
GROUP BY country
ORDER BY customer_count DESC, country;
