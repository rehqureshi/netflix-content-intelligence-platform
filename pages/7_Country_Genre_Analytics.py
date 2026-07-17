import streamlit as st
import plotly.express as px
from utils.ui import show_header

from utils.queries import *

st.set_page_config(
    page_title="Country & Genre Analytics",
    layout="wide"
)

show_header("Country & Genre Analytics")


NETFLIX_COLORS = [
    "#E50914",
    "#B20710",
    "#F40612",
    "#831010",
    "#5C0000",
    "#C11119",
    "#FF4C4C",
    "#8B0000",
    "#D72638",
    "#660000"
]

# ===================================================
# Top Countries
# ===================================================

countries = get_top_countries()

fig = px.bar(
    countries,
    x="TOTAL_TITLES",
    y="COUNTRY",
    orientation="h",
    title="Top 20 Production Countries",
    color_discrete_sequence=NETFLIX_COLORS
)

fig.update_layout(
    yaxis={"categoryorder":"total ascending"}
)

st.plotly_chart(fig, use_container_width=True)

# ===================================================
# Top Genres
# ===================================================

genres = get_top_genres()

fig = px.bar(
    genres,
    x="TOTAL_TITLES",
    y="GENRE",
    orientation="h",
    title="Top Genres",
    color_discrete_sequence=NETFLIX_COLORS
)

fig.update_layout(
    yaxis={"categoryorder":"total ascending"}
)

st.plotly_chart(fig, use_container_width=True)

# ===================================================
# Genre Distribution
# ===================================================

fig = px.pie(
    genres,
    values="TOTAL_TITLES",
    names="GENRE",
    title="Genre Distribution",
    color_discrete_sequence=NETFLIX_COLORS
)

st.plotly_chart(fig, use_container_width=True)

# ===================================================
# Average IMDb by Genre
# ===================================================

ratings = get_genre_ratings()

fig = px.bar(
    ratings,
    x="AVG_IMDB",
    y="GENRE",
    orientation="h",
    title="Average IMDb Rating by Genre",
    color_discrete_sequence=NETFLIX_COLORS
)

fig.update_layout(
    yaxis={"categoryorder":"total ascending"}
)

st.plotly_chart(fig, use_container_width=True)

# ===================================================
# Average IMDb by Country
# ===================================================

country = get_country_ratings()

fig = px.bar(
    country,
    x="AVG_IMDB",
    y="COUNTRY",
    orientation="h",
    title="Average IMDb Rating by Country",
    color_discrete_sequence=NETFLIX_COLORS
)

fig.update_layout(
    yaxis={"categoryorder":"total ascending"}
)

st.plotly_chart(fig, use_container_width=True)