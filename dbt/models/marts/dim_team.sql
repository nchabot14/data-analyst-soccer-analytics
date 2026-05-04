SELECT
    {{ dbt_utils.generate_surrogate_key(['team_id']) }} AS team_key,
    team_id,
    team_name,
    short_name,
    tla,
    crest_url,
    founded_year,
    venue,
    club_colors,
    area_name
FROM {{ ref('stg_teams') }}
