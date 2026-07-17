import streamlit as st
from utils.ui import show_header

from utils.queries import (
    get_catalog_details,
    get_actors,
    get_directors,
    get_genres,
    get_countries
)

st.set_page_config(
    page_title="Search Catalog",
    page_icon="🎬",
    layout="wide"
)

show_header("Search Netflix Catalog")

catalog = get_catalog_details()

selected_title = st.selectbox(
    "Select a Title",
    catalog["TITLE"]
)

movie = catalog[catalog["TITLE"] == selected_title].iloc[0]

content_id = movie["ID"]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Type", movie["TYPE"])

with col2:
    st.metric("Release Year", int(movie["RELEASE_YEAR"]))

with col3:
    imdb = movie["IMDB_SCORE"] if movie["IMDB_SCORE"] is not None else "N/A"
    st.metric("IMDb", imdb)

with col4:
    tmdb = movie["TMDB_SCORE"] if movie["TMDB_SCORE"] is not None else "N/A"
    st.metric("TMDB", tmdb)

st.divider()

# ------------------------
# Director
# ------------------------

st.subheader("🎬 Director")

directors = get_directors(content_id)

if directors.empty:
    st.info("No director information available.")
else:
    st.write(", ".join(directors["DIRECTOR_NAME"]))

# ------------------------
# Actors
# ------------------------

st.subheader("🎭 Actors")

actors = get_actors(content_id)

if actors.empty:
    st.info("No actor information available.")
else:
    st.write(", ".join(actors["ACTOR_NAME"]))

# ------------------------
# Genres
# ------------------------

st.subheader("🎯 Genres")

genres = get_genres(content_id)

if genres.empty:
    st.info("No genres available.")
else:
    st.write(", ".join(genres["GENRE"]))

# ------------------------
# Countries
# ------------------------

st.subheader("🌍 Production Countries")

countries = get_countries(content_id)

if countries.empty:
    st.info("No country information available.")
else:
    st.write(", ".join(countries["COUNTRY"]))