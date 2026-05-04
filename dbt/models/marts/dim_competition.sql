SELECT
    {{ dbt_utils.generate_surrogate_key(['competition_code', 'season_year']) }} AS competition_key,
    competition_code,
    competition_name,
    season_year,
    current_season_start_date AS season_start_date,
    current_season_end_date   AS season_end_date,
    area_name
FROM {{ ref('stg_competitions') }}
