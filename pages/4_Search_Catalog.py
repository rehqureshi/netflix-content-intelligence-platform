import streamlit as st

from utils.queries import get_catalog

st.set_page_config(
    page_title="Search Catalog",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Search & Explore Netflix Catalog")

# ----------------------------------
# Load Data
# ----------------------------------

df = get_catalog()

# ----------------------------------
# Sidebar Filters
# ----------------------------------

st.sidebar.header("Filters")

# Content Type

content_type = st.sidebar.multiselect(
    "Content Type",
    options=sorted(df["TYPE"].dropna().unique()),
    default=sorted(df["TYPE"].dropna().unique())
)

# Release Year

min_year = int(df["RELEASE_YEAR"].min())
max_year = int(df["RELEASE_YEAR"].max())

year_range = st.sidebar.slider(
    "Release Year",
    min_year,
    max_year,
    (min_year, max_year)
)

# IMDb Rating

rating = st.sidebar.slider(
    "Minimum IMDb Rating",
    0.0,
    10.0,
    0.0,
    0.1
)

# Runtime

min_runtime = int(df["RUNTIME"].fillna(0).min())
max_runtime = int(df["RUNTIME"].fillna(0).max())

runtime = st.sidebar.slider(
    "Maximum Runtime (Minutes)",
    min_runtime,
    max_runtime,
    max_runtime
)

# Search Box

search = st.text_input(
    "Search by Title"
)

# ----------------------------------
# Apply Filters
# ----------------------------------

filtered = df.copy()

filtered = filtered[
    filtered["TYPE"].isin(content_type)
]

filtered = filtered[
    (filtered["RELEASE_YEAR"] >= year_range[0]) &
    (filtered["RELEASE_YEAR"] <= year_range[1])
]

filtered = filtered[
    filtered["IMDB_SCORE"].fillna(0) >= rating
]

filtered = filtered[
    filtered["RUNTIME"].fillna(0) <= runtime
]

if search:

    filtered = filtered[
        filtered["TITLE"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ----------------------------------
# KPI Cards
# ----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Matching Titles",
        len(filtered)
    )

with col2:
    st.metric(
        "Movies",
        len(filtered[filtered["TYPE"] == "MOVIE"])
    )

with col3:
    st.metric(
        "TV Shows",
        len(filtered[filtered["TYPE"] == "SHOW"])
    )

st.divider()

# ----------------------------------
# Results
# ----------------------------------

st.subheader("Search Results")

st.dataframe(
    filtered.sort_values(
        by="IMDB_SCORE",
        ascending=False,
        na_position="last"
    ),
    use_container_width=True,
    hide_index=True
)

# ----------------------------------
# Download Button
# ----------------------------------

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="netflix_filtered_catalog.csv",
    mime="text/csv"
)