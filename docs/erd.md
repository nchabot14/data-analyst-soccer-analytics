# Star Schema ERD

## Overview

The mart layer implements a classic Kimball star schema centered on `fct_match_results`, the only fact table. The grain of the fact is **one row per finished match** — every row represents a single completed fixture from football-data.org. Three dimensions hang off the fact: `dim_team` (joined twice, once via `home_team_key` and once via `away_team_key`), `dim_competition` (one row per competition+season), and `dim_date` (a 731-day spine where the date itself serves as the primary key). Surrogate keys are generated with `dbt_utils.generate_surrogate_key` (md5 hashes) so that joins are stable even if the underlying natural keys ever change types or formats; the natural keys are kept alongside for lineage. This shape is what makes BI questions like "home points vs. away points per team across the 2024-25 season" answerable with a single fact-to-dim join.

## Diagram

```mermaid
erDiagram
    fct_match_results {
        string match_key PK
        number match_id
        date match_date_key FK
        string home_team_key FK
        string away_team_key FK
        string competition_key FK
        string match_status
        number matchday
        number full_time_home_goals
        number full_time_away_goals
        number goal_difference
        number total_goals
        string winner
        number home_points
        number away_points
        timestamp utc_date
    }

    dim_team {
        string team_key PK
        number team_id
        string team_name
        string short_name
        string tla
        string crest_url
        number founded_year
        string venue
        string club_colors
        string area_name
    }

    dim_competition {
        string competition_key PK
        string competition_code
        string competition_name
        number season_year
        date season_start_date
        date season_end_date
        string area_name
    }

    dim_date {
        date date_key PK
        date full_date
        number day_of_week
        string day_name
        number day_of_month
        number month_number
        string month_name
        number quarter
        number year
        boolean is_weekend
    }

    dim_team           ||--o{ fct_match_results : "home_team_key"
    dim_team           ||--o{ fct_match_results : "away_team_key"
    dim_competition    ||--o{ fct_match_results : "competition_key"
    dim_date           ||--o{ fct_match_results : "match_date_key"
```
