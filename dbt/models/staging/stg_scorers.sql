WITH latest_raw AS (
    SELECT *
    FROM {{ source('raw', 'RAW_SCORERS') }}
    QUALIFY ROW_NUMBER() OVER (PARTITION BY competition_code, season ORDER BY extracted_at DESC) = 1
)

SELECT
    s.competition_code,
    s.season,
    scorer.value:player.id::NUMBER                          AS player_id,
    scorer.value:player.name::STRING                        AS player_name,
    scorer.value:player.nationality::STRING                 AS nationality,
    TRY_TO_DATE(scorer.value:player.dateOfBirth::STRING)    AS date_of_birth,
    scorer.value:team.id::NUMBER                            AS team_id,
    scorer.value:team.name::STRING                          AS team_name,
    scorer.value:team.tla::STRING                           AS team_tla,
    scorer.value:goals::NUMBER                              AS goals,
    scorer.value:assists::NUMBER                            AS assists,
    scorer.value:penalties::NUMBER                          AS penalties,
    scorer.value:playedMatches::NUMBER                      AS played_matches,
    s.extracted_at
FROM latest_raw s,
     LATERAL FLATTEN(input => s.payload:scorers) AS scorer
