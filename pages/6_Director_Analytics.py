import streamlit as st
import plotly.express as px
from utils.ui import show_header

from utils.queries import *

st.set_page_config(
    page_title="Director Analytics",
    layout="wide"
)

show_header("Director Analytics")

# ============================================
# Top Directors
# ============================================

top = get_top_directors()

fig = px.bar(
    top,
    x="TOTAL_TITLES",
    y="DIRECTOR_NAME",
    orientation="h",
    title="Top 20 Directors by Number of Titles",
    color_discrete_sequence=["#E50914"]
)

fig.update_layout(
    yaxis={'categoryorder':'total ascending'}
)

st.plotly_chart(fig, use_container_width=True)

# ============================================
# Highest Rated Directors
# ============================================

rated = get_highest_rated_directors()

fig = px.bar(
    rated,
    x="AVG_IMDB",
    y="DIRECTOR_NAME",
    orientation="h",
    title="Highest Rated Directors (Minimum 3 Titles)",
    color_discrete_sequence=["#E50914"]
)

fig.update_layout(
    yaxis={'categoryorder':'total ascending'}
)

st.plotly_chart(fig, use_container_width=True)

# ============================================
# Search Director
# ============================================

st.header("🔍 Search Director")

directors = get_director_list()

selected = st.selectbox(
    "Choose a Director",
    directors["DIRECTOR_NAME"]
)

filmography = get_director_filmography(selected)

st.subheader(f"Filmography of {selected}")

st.dataframe(
    filmography,
    use_container_width=True,
    hide_index=True
)