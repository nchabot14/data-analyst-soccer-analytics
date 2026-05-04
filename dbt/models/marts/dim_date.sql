WITH date_spine AS (
    {{ dbt_utils.date_spine(
        datepart="day",
        start_date="cast('2024-01-01' as date)",
        end_date="cast('2026-01-01' as date)"
    ) }}
)

SELECT
    date_day                                AS date_key,
    date_day                                AS full_date,
    DAYOFWEEKISO(date_day)                  AS day_of_week,
    CASE DAYOFWEEKISO(date_day)
        WHEN 1 THEN 'Monday'
        WHEN 2 THEN 'Tuesday'
        WHEN 3 THEN 'Wednesday'
        WHEN 4 THEN 'Thursday'
        WHEN 5 THEN 'Friday'
        WHEN 6 THEN 'Saturday'
        WHEN 7 THEN 'Sunday'
    END                                     AS day_name,
    DAY(date_day)                           AS day_of_month,
    MONTH(date_day)                         AS month_number,
    TRIM(TO_VARCHAR(date_day, 'MMMM'))      AS month_name,
    QUARTER(date_day)                       AS quarter,
    YEAR(date_day)                          AS year,
    DAYOFWEEKISO(date_day) IN (6, 7)        AS is_weekend
FROM date_spine
