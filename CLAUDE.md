# CLAUDE.md

## Project Purpose
An end-to-end analytics engineering pipeline targeting MLS soccer data, built as a portfolio project for an analytics engineering course. The project demonstrates the skills required for the Houston Dynamo FC Data Analyst role: SQL, dbt transformations, automated pipelines, dimensional modeling, and dashboard delivery.

## Data Sources
- **API:** football-data.org REST API — match results, player stats, team standings
- **Web Scrape:** FBref.com — player season stats, per-90 metrics, scouting data

## Pipeline Architecture
1. Python ingestion scripts pull from API and scraper → raw data lands in warehouse
2. dbt staging models clean and type-cast raw tables
3. dbt intermediate models build per-90 metrics and rolling averages
4. dbt mart models produce recruitment targets and team KPI scorecards
5. Dashboard reads from mart layer
