import streamlit as st
import plotly.express as px

from utils.queries import *

st.set_page_config(layout="wide")

st.title("📈 Content Trends")

# ----------------------------------
# Titles by Year
# ----------------------------------

titles = get_titles_by_year()

fig = px.line(
    titles,
    x="RELEASE_YEAR",
    y="TOTAL",
    markers=True,
    title="Titles Released by Year"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# Movies vs Shows by Year
# ----------------------------------

content = get_movies_vs_shows_by_year()

fig = px.bar(
    content,
    x="RELEASE_YEAR",
    y="TOTAL",
    color="TYPE",
    barmode="group",
    title="Movies vs TV Shows by Year"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# Runtime Distribution
# ----------------------------------

runtime = get_runtime_distribution()

fig = px.histogram(
    runtime,
    x="RUNTIME",
    nbins=30,
    title="Runtime Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# Average IMDb by Year
# ----------------------------------

rating = get_avg_imdb_by_year()

fig = px.line(
    rating,
    x="RELEASE_YEAR",
    y="AVG_IMDB",
    markers=True,
    title="Average IMDb Rating by Year"
)

st.plotly_chart(fig, use_container_width=True)