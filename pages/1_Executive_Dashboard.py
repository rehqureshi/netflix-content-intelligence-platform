from utils.ui import show_header
import streamlit as st
import plotly.express as px

from utils.queries import *

st.set_page_config(layout="wide")

show_header("Executive Dashboard")

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

# -----------------------------
# KPIs
# -----------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Total Titles",
        int(get_total_titles().iloc[0,0])
    )

with col2:
    st.metric(
        "Movies",
        int(get_movies().iloc[0,0])
    )

with col3:
    st.metric(
        "TV Shows",
        int(get_shows().iloc[0,0])
    )

with col4:
    st.metric(
        "Avg IMDb",
        get_avg_imdb().iloc[0,0]
    )


col5,col6,col7,col8 = st.columns(4)

with col5:
    st.metric(
        "Avg TMDB",
        get_avg_tmdb().iloc[0,0]
    )

with col6:
    st.metric(
        "Countries",
        int(get_country_count().iloc[0,0])
    )

with col7:
    st.metric(
        "Genres",
        int(get_genre_count().iloc[0,0])
    )

with col8:
    st.metric(
        "Directors",
        int(get_director_count().iloc[0,0])
    )


st.divider()

# -----------------------------
# Charts
# -----------------------------

left,right = st.columns(2)

with left:

    pie = movies_vs_shows()

    fig = px.pie(
        pie,
        values="TOTAL",
        names="TYPE",
        title="Movies vs TV Shows",
        color_discrete_sequence=NETFLIX_COLORS
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with right:

    trend = titles_by_year()

    fig = px.line(
        trend,
        x="RELEASE_YEAR",
        y="TOTAL",
        markers=True,
        title="Titles Released by Year",
        color_discrete_sequence=["#E50914"]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )