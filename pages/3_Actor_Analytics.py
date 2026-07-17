import streamlit as st
import plotly.express as px
from utils.ui import show_header

from utils.queries import *

st.set_page_config(
    page_title="Actor Analytics",
    layout="wide"
)

show_header("Actor Analytics")

# ============================================
# Top Actors
# ============================================

top = get_top_actors()

fig = px.bar(
    top,
    x="TOTAL_TITLES",
    y="ACTOR_NAME",
    orientation="h",
    title="Top 20 Actors by Number of Titles",
    color_discrete_sequence=["#E50914"]
)

fig.update_layout(yaxis={'categoryorder':'total ascending'})

st.plotly_chart(fig, use_container_width=True)

# ============================================
# Highest Rated Actors
# ============================================

rated = get_highest_rated_actors()

fig = px.bar(
    rated,
    x="AVG_IMDB",
    y="ACTOR_NAME",
    orientation="h",
    title="Highest Rated Actors (Minimum 3 Titles)",
    color_discrete_sequence=["#E50914"]
)

fig.update_layout(yaxis={'categoryorder':'total ascending'})

st.plotly_chart(fig, use_container_width=True)

# ============================================
# Search Actor
# ============================================

st.header("🔍 Search Actor")

actors = get_actor_list()

selected = st.selectbox(
    "Choose an Actor",
    actors["ACTOR_NAME"]
)

filmography = get_actor_filmography(selected)

st.subheader(f"Filmography of {selected}")

st.dataframe(
    filmography,
    use_container_width=True,
    hide_index=True
)