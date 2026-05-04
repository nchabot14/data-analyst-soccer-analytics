# Soccer Analytics Dashboard

A Streamlit app that visualizes the dbt mart layer (`SOCCER_RECRUITMENT.MARTS.*` in Snowflake) for the 2024-25 Premier League season. Three pages: **League Overview** (KPIs, standings table, goals-by-matchday line chart), **Team Deep Dive** (per-team home/away splits, goals-by-matchday for/against series, recent-results table), and **Head-to-Head** (two-team H2H record plus side-by-side season-totals bars). Connection credentials are read from `st.secrets` first (for Streamlit Cloud) and fall back to environment variables (for local development with `.env`). The Snowflake connection is cached as a resource for the session, and every query result is cached for 10 minutes.

## Run locally

```bash
# from the repo root, with .env populated
set -a && . ./.env && set +a
.venv/bin/streamlit run dashboard/app.py
```

If `streamlit` or `plotly` aren't yet installed in the venv, run `.venv/bin/pip install -r requirements.txt` first.
