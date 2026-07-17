import streamlit as st
import plotly.express as px
from utils.ui import show_header

from utils.queries import *

st.set_page_config(
    page_title="Rating Distribution",
    page_icon="⭐",
    layout="wide"
)

show_header("Rating Distribution")

# ----------------------------------
# IMDb Distribution
# ----------------------------------

imdb = get_imdb_distribution()

fig = px.histogram(
    imdb,
    x="IMDB_SCORE",
    nbins=20,
    title="IMDb Rating Distribution",
    color_discrete_sequence=["#E50914"]
)

fig.update_layout(height=450)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# TMDB Distribution
# ----------------------------------

tmdb = get_tmdb_distribution()

fig = px.histogram(
    tmdb,
    x="TMDB_SCORE",
    nbins=20,
    title="TMDB Rating Distribution",
    color_discrete_sequence=["#E50914"]
)

fig.update_layout(height=450)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# Age Certification
# ----------------------------------

age = get_age_certification_distribution()

fig = px.bar(
    age,
    x="AGE_CERTIFICATION",
    y="TOTAL",
    text="TOTAL",
    title="Content by Age Certification",
    color_discrete_sequence=["#E50914"]
)

fig.update_layout(height=500)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# Top Rated Titles
# ----------------------------------

st.subheader("🏆 Top 20 Highest Rated Titles")

top = get_top_rated_titles()

st.dataframe(
    top,
    use_container_width=True,
    hide_index=True
)