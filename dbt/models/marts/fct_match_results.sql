SELECT
    {{ dbt_utils.generate_surrogate_key(['match_id']) }}                        AS match_key,
    match_id,
    utc_date::DATE                                                              AS match_date_key,
    {{ dbt_utils.generate_surrogate_key(['home_team_id']) }}                    AS home_team_key,
    {{ dbt_utils.generate_surrogate_key(['away_team_id']) }}                    AS away_team_key,
    {{ dbt_utils.generate_surrogate_key(['competition_code', 'season']) }}      AS competition_key,
    match_status,
    matchday,
    full_time_home_goals,
    full_time_away_goals,
    goal_difference,
    full_time_home_goals + full_time_away_goals                                 AS total_goals,
    winner,
    CASE
        WHEN winner = 'HOME_TEAM' THEN 3
        WHEN winner = 'DRAW'      THEN 1
        ELSE 0
    END                                                                          AS home_points,
    CASE
        WHEN winner = 'AWAY_TEAM' THEN 3
        WHEN winner = 'DRAW'      THEN 1
        ELSE 0
    END                                                                          AS away_points,
    utc_date
FROM {{ ref('stg_matches') }}
WHERE match_status = 'FINISHED'
