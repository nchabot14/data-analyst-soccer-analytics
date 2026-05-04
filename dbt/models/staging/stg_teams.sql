SELECT
    payload:id::NUMBER              AS team_id,
    payload:name::STRING            AS team_name,
    payload:shortName::STRING       AS short_name,
    payload:tla::STRING             AS tla,
    payload:crest::STRING           AS crest_url,
    payload:founded::NUMBER         AS founded_year,
    payload:venue::STRING           AS venue,
    payload:clubColors::STRING      AS club_colors,
    payload:website::STRING         AS website,
    payload:area.name::STRING       AS area_name,
    competition_code,
    season,
    extracted_at
FROM {{ source('raw', 'RAW_TEAMS') }}
