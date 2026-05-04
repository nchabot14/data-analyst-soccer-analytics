SELECT
    s.competition_code,
    s.season,
    block.value:type::STRING                AS standings_type,
    team_row.value:position::NUMBER         AS position,
    team_row.value:team.id::NUMBER          AS team_id,
    team_row.value:team.name::STRING        AS team_name,
    team_row.value:playedGames::NUMBER      AS played_games,
    team_row.value:won::NUMBER              AS won,
    team_row.value:draw::NUMBER             AS draw,
    team_row.value:lost::NUMBER             AS lost,
    team_row.value:points::NUMBER           AS points,
    team_row.value:goalsFor::NUMBER         AS goals_for,
    team_row.value:goalsAgainst::NUMBER     AS goals_against,
    team_row.value:goalDifference::NUMBER   AS goal_difference,
    s.extracted_at
FROM {{ source('raw', 'RAW_STANDINGS') }} s,
     LATERAL FLATTEN(input => s.payload:standings) AS block,
     LATERAL FLATTEN(input => block.value:table)   AS team_row
