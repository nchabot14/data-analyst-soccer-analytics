WITH latest_raw AS (
    SELECT *
    FROM {{ source('raw', 'RAW_COMPETITIONS') }}
    QUALIFY ROW_NUMBER() OVER (PARTITION BY competition_code, season ORDER BY extracted_at DESC) = 1
)

SELECT
    payload:id::NUMBER                                      AS competition_id,
    payload:code::STRING                                    AS competition_code,
    payload:name::STRING                                    AS competition_name,
    payload:area.id::NUMBER                                 AS area_id,
    payload:area.name::STRING                               AS area_name,
    TRY_TO_DATE(payload:currentSeason.startDate::STRING)    AS current_season_start_date,
    TRY_TO_DATE(payload:currentSeason.endDate::STRING)      AS current_season_end_date,
    season::NUMBER                                          AS season_year,
    extracted_at
FROM latest_raw
