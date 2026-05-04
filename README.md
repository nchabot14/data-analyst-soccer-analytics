# data-analyst-soccer-analytics

## Pipeline Architecture

This project ingests MLS data through two parallel pipelines — a structured football-data.org REST API and Firecrawl-driven web scraping — that converge on a Snowflake star schema serving a Streamlit dashboard, plus a synthesized wiki for analyst queries. See [docs/pipeline.md](docs/pipeline.md) for the full layer-by-layer description.

```mermaid
flowchart TD
    %% --- Sources ---
    src1["football-data.org v4 API\nREST · JSON"]
    src2["fbref.com · mlssoccer.com\namericansocceranalysis.com\nHTML pages"]

    %% --- Orchestrator + extraction scripts ---
    gha["GitHub Actions\ncron: daily / weekly"]
    py1["Python: extract_football_data_api.py\nrequests + snowflake-connector-python"]
    py2["Python: extract_knowledge_sources.py\nfirecrawl-py SDK"]

    %% --- Raw layer ---
    raw1[("Snowflake RAW schema\n5 VARIANT tables")]
    raw2[("knowledge/raw/\n18 Markdown files")]

    %% --- Transformation (dbt) ---
    subgraph dbt_layer ["dbt on Snowflake"]
        stg[("STAGING schema\n5 views · 15 tests")]
        marts[("MARTS schema\n3 dims + 1 fact · star schema")]
    end

    %% --- Final consumers ---
    dash["Streamlit Cloud dashboard\n3 pages · cached SQL"]
    wiki["knowledge/wiki/\nClaude Code-generated · 4 files"]

    %% --- Flow ---
    src1 -->|HTTP fetch| py1
    src2 -->|Firecrawl scrape| py2
    gha -.->|schedules| py1
    gha -.->|schedules| py2
    py1 -->|PARSE_JSON · INSERT VARIANT| raw1
    py2 -->|writes .md + git commit| raw2
    raw1 -->|dbt run --select staging| stg
    stg -->|dbt run --select marts| marts
    marts -->|SELECT via snowflake-connector| dash
    raw2 -->|synthesized by Claude Code| wiki

    %% --- Styling ---
    classDef source fill:#dbeafe,stroke:#1d4ed8,stroke-width:2px
    classDef tool fill:#fef3c7,stroke:#b45309,stroke-width:2px
    classDef storage fill:#d1fae5,stroke:#047857,stroke-width:2px
    classDef consumer fill:#fce7f3,stroke:#be185d,stroke-width:2px

    class src1,src2 source
    class gha,py1,py2 tool
    class raw1,raw2,stg,marts storage
    class dash,wiki consumer
```