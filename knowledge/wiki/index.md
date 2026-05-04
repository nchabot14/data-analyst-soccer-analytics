# Knowledge Base — Index

This knowledge base is a curated, scraped corpus of public-web pages about Major League Soccer (MLS) and its analytical landscape. It exists to support the recruitment-analysis project (the dbt + Snowflake + Streamlit pipeline elsewhere in this repo) by giving an analyst a single place to look up league structure, current standings and stat leaders, prominent players, and the analytical communities that publish about MLS. Sources span three domains — `fbref.com` (statistical reference), `mlssoccer.com` (the league's official site), and `americansocceranalysis.com` (an independent analytics publication) — totaling 18 raw files. All wiki content below is synthesized strictly from those scraped sources; nothing has been added from outside knowledge.

## Wiki pages

- [overview.md](overview.md) — Synthesis of MLS structure, recruitment dynamics, current league landscape, and how analytical sites cover it
- [key_entities.md](key_entities.md) — Structured list of teams, players, analysts, and governing structures named across the sources
- [themes.md](themes.md) — Recurring topics (DP signings, academy/U22, stats-driven recruitment) cited back to source files

## Raw sources

The table below lists every file in `knowledge/raw/`, the source domain, what kind of content it contains, and the source URL pulled from each file's front matter.

| File | Domain | Content type | Source URL |
|---|---|---|---|
| `en_comps_22_Major-League-Soccer-Stats.md` | fbref.com | 2026 MLS overview — Eastern/Western Conference standings, top scorers/assisters/clean sheets, league structure | https://fbref.com/en/comps/22/Major-League-Soccer-Stats |
| `en_comps_22_stats_Major-League-Soccer-Stats.md` | fbref.com | 2026 MLS standard player and squad stats (the largest scraped file) | https://fbref.com/en/comps/22/stats/Major-League-Soccer-Stats |
| `en_comps_22_shooting_Major-League-Soccer-Stats.md` | fbref.com | 2026 MLS shooting stats (xG, shots on target, conversion) | https://fbref.com/en/comps/22/shooting/Major-League-Soccer-Stats |
| `en_comps_22_passing_Major-League-Soccer-Stats.md` | fbref.com | 2026 MLS passing stats (completion %, progressive passes, key passes) | https://fbref.com/en/comps/22/passing/Major-League-Soccer-Stats |
| `en_comps_22_defense_Major-League-Soccer-Stats.md` | fbref.com | 2026 MLS defensive action stats (tackles, interceptions, blocks) | https://fbref.com/en/comps/22/defense/Major-League-Soccer-Stats |
| `en_comps_22_possession_Major-League-Soccer-Stats.md` | fbref.com | 2026 MLS possession stats (touches by zone, dribbles, carries) | https://fbref.com/en/comps/22/possession/Major-League-Soccer-Stats |
| `en_comps_22_misc_Major-League-Soccer-Stats.md` | fbref.com | 2026 MLS miscellaneous stats (fouls, cards, aerials) | https://fbref.com/en/comps/22/misc/Major-League-Soccer-Stats |
| `en_players_d70ce98e_Lionel-Messi.md` | fbref.com | Lionel Messi full FBref profile — bio, honors, club + national team stats | https://fbref.com/en/players/d70ce98e/Lionel-Messi |
| `en_players_00e7e57b_Sergio-Busquets.md` | fbref.com | **Failed scrape** — FBref returned an HTTP 500 error page; no usable content | https://fbref.com/en/players/00e7e57b/Sergio-Busquets |
| `en_players_8b04d6c1_Jordi-Alba.md` | fbref.com | **Mislabeled** — the 8-char player ID `8b04d6c1` actually points to Pierre-Emile Højbjerg's profile (Marseille / Denmark), not Jordi Alba. The file contains Højbjerg's data despite the filename | https://fbref.com/en/players/8b04d6c1/Jordi-Alba |
| `about.md` | mlssoccer.com | MLS official "About" page — founding date, league address, navigation links | https://www.mlssoccer.com/about/ |
| `news.md` | mlssoccer.com | MLS official news landing — recent headlines, transfer-tracker entries | https://www.mlssoccer.com/news/ |
| `standings.md` | mlssoccer.com | MLS standings page — column structure (Rank, Club, PTS, PPG, GP, W, L, T, GF, GA, GD, Home, Away); table itself was JS-loaded and not captured | https://www.mlssoccer.com/standings/ |
| `competitions_mls-cup-playoffs.md` | mlssoccer.com | Audi 2025 MLS Cup Playoffs landing — Inter Miami's championship coverage, 2026 playoffs schedule announcement | https://www.mlssoccer.com/competitions/mls-cup-playoffs |
| `home.md` | americansocceranalysis.com | ASA homepage — top article preview ("Towards a manual for the most common restart" by Ben Bellman, on long throw-ins) and 2026 NWSL/MLS season-preview list | https://www.americansocceranalysis.com/home |
| `home_2024_8_27_state-of-the-mls-academy-system.md` | americansocceranalysis.com | **Same homepage content as `home.md`** — Firecrawl could not render the actual academy article body (Squarespace SPA limitation); only the URL slug retains the topic name | https://www.americansocceranalysis.com/home/2024/8/27/state-of-the-mls-academy-system |
| `home_2024_2_16_breaking-down-mls-roster-rules.md` | americansocceranalysis.com | **Same homepage content as `home.md`** — actual roster-rules article body not captured | https://www.americansocceranalysis.com/home/2024/2/16/breaking-down-mls-roster-rules |
| `home_2023_11_15_mls-expected-goals-leaders.md` | americansocceranalysis.com | **Same homepage content as `home.md`** — actual xG-leaders article body not captured | https://www.americansocceranalysis.com/home/2023/11/15/mls-expected-goals-leaders |

### Caveats on source completeness

- **Three files are effectively empty for content purposes**: `en_players_00e7e57b_Sergio-Busquets.md` (FBref 500 error), `en_players_8b04d6c1_Jordi-Alba.md` (wrong player — Højbjerg, not in MLS), and the four ASA `home*.md` files (all serve identical homepage content rather than the requested article bodies). The wiki pages below treat these as known gaps rather than ignoring them.
- **`mlssoccer.com/standings/` returned an empty table** because the standings widget is JavaScript-loaded and Firecrawl captured only the static HTML shell. We have the column schema but not the rows.
- **Current MLS standings data therefore comes exclusively from `en_comps_22_Major-League-Soccer-Stats.md`** (FBref's 2026 MLS overview), which scraped successfully and contains a full Eastern Conference table.
