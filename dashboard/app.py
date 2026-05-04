"""
dashboard/app.py — Premier League recruitment analytics dashboard.

Reads from SOCCER_RECRUITMENT.MARTS.* (the dbt mart layer) and serves a 3-page
Streamlit app: League Overview, Team Deep Dive, Head-to-Head.

Run:
    set -a && . ./.env && set +a
    streamlit run dashboard/app.py
"""
from __future__ import annotations

import os

import pandas as pd
import plotly.express as px
import snowflake.connector
import streamlit as st


# --------------------------------------------------------------------------
# Page config
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Premier League Recruitment Analytics",
    page_icon="⚽",
    layout="wide",
)


# --------------------------------------------------------------------------
# Connection layer
# --------------------------------------------------------------------------
def _credential(key: str) -> str:
    """Return a credential, preferring st.secrets, falling back to env vars.

    Supports both nested ([snowflake] section) and flat layouts in secrets.toml.
    """
    try:
        if "snowflake" in st.secrets:
            section = st.secrets["snowflake"]
            for variant in (key, key.lower(), key.upper()):
                if variant in section:
                    return section[variant]
        if key in st.secrets:
            return st.secrets[key]
    except (FileNotFoundError, KeyError, AttributeError):
        pass
    return os.environ[key]


@st.cache_resource
def get_connection() -> "snowflake.connector.SnowflakeConnection":
    return snowflake.connector.connect(
        account=_credential("SNOWFLAKE_ACCOUNT"),
        user=_credential("SNOWFLAKE_USER"),
        password=_credential("SNOWFLAKE_PASSWORD"),
        warehouse=_credential("SNOWFLAKE_WAREHOUSE"),
        role=_credential("SNOWFLAKE_ROLE"),
        database="SOCCER_RECRUITMENT",
        schema="MARTS",
    )


@st.cache_data(ttl=600)
def run_query(sql: str, params: dict | None = None) -> pd.DataFrame:
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql, params)
        return cur.fetch_pandas_all()
    finally:
        cur.close()


# --------------------------------------------------------------------------
# SQL constants
# --------------------------------------------------------------------------
KPI_SQL = """
SELECT
    COUNT(*)                                         AS total_matches,
    SUM(total_goals)                                 AS total_goals,
    AVG(total_goals)                                 AS avg_goals_per_match,
    100.0 * COUNT_IF(winner = 'HOME_TEAM') / COUNT(*) AS home_win_pct
FROM fct_match_results
"""

STANDINGS_SQL = """
WITH team_results AS (
    SELECT
        home_team_key            AS team_key,
        full_time_home_goals     AS goals_for,
        full_time_away_goals     AS goals_against,
        home_points              AS points,
        CASE winner
            WHEN 'HOME_TEAM' THEN 'W'
            WHEN 'AWAY_TEAM' THEN 'L'
            ELSE 'D'
        END                      AS team_outcome
    FROM fct_match_results
    UNION ALL
    SELECT
        away_team_key            AS team_key,
        full_time_away_goals     AS goals_for,
        full_time_home_goals     AS goals_against,
        away_points              AS points,
        CASE winner
            WHEN 'AWAY_TEAM' THEN 'W'
            WHEN 'HOME_TEAM' THEN 'L'
            ELSE 'D'
        END                      AS team_outcome
    FROM fct_match_results
)
SELECT
    t.team_name                              AS team,
    COUNT(*)                                 AS played,
    COUNT_IF(tr.team_outcome = 'W')          AS wins,
    COUNT_IF(tr.team_outcome = 'D')          AS draws,
    COUNT_IF(tr.team_outcome = 'L')          AS losses,
    SUM(tr.goals_for)                        AS goals_for,
    SUM(tr.goals_against)                    AS goals_against,
    SUM(tr.goals_for) - SUM(tr.goals_against) AS goal_difference,
    SUM(tr.points)                           AS points
FROM team_results tr
JOIN dim_team t ON t.team_key = tr.team_key
GROUP BY t.team_name
ORDER BY points DESC, goal_difference DESC, goals_for DESC
"""

MATCHDAY_GOALS_SQL = """
SELECT matchday, SUM(total_goals) AS goals
FROM fct_match_results
GROUP BY matchday
ORDER BY matchday
"""

TEAMS_SQL = "SELECT team_name FROM dim_team ORDER BY team_name"

TEAM_HOME_SQL = """
SELECT
    COUNT_IF(f.winner = 'HOME_TEAM') AS wins,
    COUNT_IF(f.winner = 'DRAW')      AS draws,
    COUNT_IF(f.winner = 'AWAY_TEAM') AS losses
FROM fct_match_results f
JOIN dim_team t ON t.team_key = f.home_team_key
WHERE t.team_name = %(team)s
"""

TEAM_AWAY_SQL = """
SELECT
    COUNT_IF(f.winner = 'AWAY_TEAM') AS wins,
    COUNT_IF(f.winner = 'DRAW')      AS draws,
    COUNT_IF(f.winner = 'HOME_TEAM') AS losses
FROM fct_match_results f
JOIN dim_team t ON t.team_key = f.away_team_key
WHERE t.team_name = %(team)s
"""

TEAM_MATCHDAY_GOALS_SQL = """
WITH per_team AS (
    SELECT matchday, full_time_home_goals AS gf, full_time_away_goals AS ga,
           home_team_key AS team_key
    FROM fct_match_results
    UNION ALL
    SELECT matchday, full_time_away_goals AS gf, full_time_home_goals AS ga,
           away_team_key AS team_key
    FROM fct_match_results
)
SELECT
    p.matchday,
    SUM(p.gf) AS goals_for,
    SUM(p.ga) AS goals_against
FROM per_team p
JOIN dim_team t ON t.team_key = p.team_key
WHERE t.team_name = %(team)s
GROUP BY p.matchday
ORDER BY p.matchday
"""

TEAM_RECENT_SQL = """
SELECT
    f.utc_date::DATE                                                                  AS date,
    CASE WHEN ht.team_name = %(team)s THEN 'H' ELSE 'A' END                           AS venue,
    CASE WHEN ht.team_name = %(team)s THEN at.team_name ELSE ht.team_name END         AS opponent,
    CASE WHEN ht.team_name = %(team)s THEN f.full_time_home_goals
         ELSE f.full_time_away_goals END                                              AS goals_for,
    CASE WHEN ht.team_name = %(team)s THEN f.full_time_away_goals
         ELSE f.full_time_home_goals END                                              AS goals_against,
    CASE
        WHEN (ht.team_name = %(team)s AND f.winner = 'HOME_TEAM') THEN 'W'
        WHEN (at.team_name = %(team)s AND f.winner = 'AWAY_TEAM') THEN 'W'
        WHEN f.winner = 'DRAW' THEN 'D'
        ELSE 'L'
    END                                                                                AS result
FROM fct_match_results f
JOIN dim_team ht ON ht.team_key = f.home_team_key
JOIN dim_team at ON at.team_key = f.away_team_key
WHERE ht.team_name = %(team)s OR at.team_name = %(team)s
ORDER BY f.utc_date DESC
LIMIT 10
"""

H2H_SQL = """
SELECT
    COUNT(*)                          AS matches_played,
    COUNT_IF(f.winner = 'HOME_TEAM')  AS home_wins,
    COUNT_IF(f.winner = 'AWAY_TEAM')  AS away_wins,
    COUNT_IF(f.winner = 'DRAW')       AS draws,
    SUM(f.total_goals)                AS total_goals
FROM fct_match_results f
JOIN dim_team ht ON ht.team_key = f.home_team_key
JOIN dim_team at ON at.team_key = f.away_team_key
WHERE ht.team_name IN (%(team_a)s, %(team_b)s)
  AND at.team_name IN (%(team_a)s, %(team_b)s)
"""


# --------------------------------------------------------------------------
# Page renderers
# --------------------------------------------------------------------------
def show_overview() -> None:
    st.title("League Overview")
    st.caption("Season-wide descriptive statistics for the 2024-25 Premier League.")

    kpis = run_query(KPI_SQL).iloc[0]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Matches", f"{int(kpis['TOTAL_MATCHES']):,}")
    c2.metric("Total Goals", f"{int(kpis['TOTAL_GOALS']):,}")
    c3.metric("Avg Goals/Match", f"{float(kpis['AVG_GOALS_PER_MATCH']):.2f}")
    c4.metric("Home Win %", f"{float(kpis['HOME_WIN_PCT']):.1f}%")

    st.subheader("Standings")
    standings = run_query(STANDINGS_SQL)
    st.dataframe(
        standings,
        use_container_width=True,
        hide_index=True,
        column_config={
            "TEAM": st.column_config.TextColumn("Team"),
            "PLAYED": st.column_config.NumberColumn("P", format="%d"),
            "WINS": st.column_config.NumberColumn("W", format="%d"),
            "DRAWS": st.column_config.NumberColumn("D", format="%d"),
            "LOSSES": st.column_config.NumberColumn("L", format="%d"),
            "GOALS_FOR": st.column_config.NumberColumn("GF", format="%d"),
            "GOALS_AGAINST": st.column_config.NumberColumn("GA", format="%d"),
            "GOAL_DIFFERENCE": st.column_config.NumberColumn("GD", format="%+d"),
            "POINTS": st.column_config.NumberColumn("Pts", format="%d"),
        },
    )

    st.subheader("Total Goals by Matchday")
    matchday = run_query(MATCHDAY_GOALS_SQL)
    fig = px.line(matchday, x="MATCHDAY", y="GOALS", markers=True)
    fig.update_layout(margin=dict(l=20, r=20, t=10, b=20),
                      xaxis_title="Matchday", yaxis_title="Total Goals")
    st.plotly_chart(fig, use_container_width=True)


def show_team(team_name: str) -> None:
    standings = run_query(STANDINGS_SQL).reset_index(drop=True)
    standings.insert(0, "position", standings.index + 1)
    team_row = standings[standings["TEAM"] == team_name].iloc[0]

    c1, c2, c3 = st.columns(3)
    c1.metric("League Position", f"#{int(team_row['position'])}")
    c2.metric("Points", int(team_row["POINTS"]))
    c3.metric("Goal Difference", f"{int(team_row['GOAL_DIFFERENCE']):+d}")

    home = run_query(TEAM_HOME_SQL, {"team": team_name}).iloc[0]
    away = run_query(TEAM_AWAY_SQL, {"team": team_name}).iloc[0]

    left, right = st.columns(2)
    with left:
        st.subheader("Home vs Away Record")
        record = pd.DataFrame({
            "Outcome": ["Wins", "Draws", "Losses"],
            "Home":    [int(home["WINS"]), int(home["DRAWS"]), int(home["LOSSES"])],
            "Away":    [int(away["WINS"]), int(away["DRAWS"]), int(away["LOSSES"])],
        }).melt(id_vars="Outcome", var_name="Venue", value_name="Count")
        fig = px.bar(record, x="Outcome", y="Count", color="Venue", barmode="group")
        fig.update_layout(margin=dict(l=20, r=20, t=10, b=20))
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Goals For/Against by Matchday")
        gd = run_query(TEAM_MATCHDAY_GOALS_SQL, {"team": team_name})
        long = gd.melt(id_vars="MATCHDAY", value_vars=["GOALS_FOR", "GOALS_AGAINST"],
                       var_name="Side", value_name="Goals")
        long["Side"] = long["Side"].map({"GOALS_FOR": "For", "GOALS_AGAINST": "Against"})
        fig = px.line(long, x="MATCHDAY", y="Goals", color="Side", markers=True)
        fig.update_layout(margin=dict(l=20, r=20, t=10, b=20),
                          xaxis_title="Matchday")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Most Recent 10 Matches")
    recent = run_query(TEAM_RECENT_SQL, {"team": team_name})
    st.dataframe(
        recent,
        use_container_width=True,
        hide_index=True,
        column_config={
            "DATE": st.column_config.DateColumn("Date"),
            "VENUE": st.column_config.TextColumn("H/A"),
            "OPPONENT": st.column_config.TextColumn("Opponent"),
            "GOALS_FOR": st.column_config.NumberColumn("GF", format="%d"),
            "GOALS_AGAINST": st.column_config.NumberColumn("GA", format="%d"),
            "RESULT": st.column_config.TextColumn("Result"),
        },
    )


def show_head_to_head(team_a: str, team_b: str) -> None:
    if team_a == team_b:
        st.warning("Pick two different teams.")
        return

    h2h = run_query(H2H_SQL, {"team_a": team_a, "team_b": team_b}).iloc[0]
    matches_played = int(h2h["MATCHES_PLAYED"])

    st.subheader(f"Head-to-Head: {team_a} vs {team_b}")
    if matches_played == 0:
        st.info(f"No matches between {team_a} and {team_b} in the loaded data.")
    else:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Home Wins", int(h2h["HOME_WINS"]))
        c2.metric("Away Wins", int(h2h["AWAY_WINS"]))
        c3.metric("Draws", int(h2h["DRAWS"]))
        c4.metric("Total Goals", int(h2h["TOTAL_GOALS"] or 0))

    st.subheader("Season Totals (both teams)")
    standings = run_query(STANDINGS_SQL)
    pair = standings[standings["TEAM"].isin([team_a, team_b])][
        ["TEAM", "POINTS", "GOALS_FOR", "GOALS_AGAINST", "WINS"]
    ]
    pair_long = pair.melt(id_vars="TEAM", var_name="Metric", value_name="Value")
    pair_long["Metric"] = pair_long["Metric"].map({
        "POINTS": "Points",
        "GOALS_FOR": "Goals For",
        "GOALS_AGAINST": "Goals Against",
        "WINS": "Wins",
    })
    fig = px.bar(pair_long, x="Metric", y="Value", color="TEAM", barmode="group")
    fig.update_layout(margin=dict(l=20, r=20, t=10, b=20),
                      xaxis_title=None, legend_title="Team")
    st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------------------------------
# Sidebar + router
# --------------------------------------------------------------------------
def main() -> None:
    st.sidebar.title("Premier League Analytics")
    page = st.sidebar.radio(
        "Page",
        ["League Overview", "Team Deep Dive", "Head-to-Head"],
    )

    if page == "League Overview":
        show_overview()

    elif page == "Team Deep Dive":
        st.title("Team Deep Dive")
        st.caption("Detailed performance metrics for one club.")
        teams = run_query(TEAMS_SQL)["TEAM_NAME"].tolist()
        team_name = st.selectbox("Select team", teams)
        show_team(team_name)

    elif page == "Head-to-Head":
        st.title("Head-to-Head")
        st.caption("Compare two clubs across head-to-head fixtures and full-season totals.")
        teams = run_query(TEAMS_SQL)["TEAM_NAME"].tolist()
        c1, c2 = st.columns(2)
        team_a = c1.selectbox("Team A", teams, index=0)
        team_b = c2.selectbox("Team B", teams, index=min(1, len(teams) - 1))
        show_head_to_head(team_a, team_b)


if __name__ == "__main__":
    main()
