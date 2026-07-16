from utils.connection import get_connection
import pandas as pd


def run_query(query):
    conn = get_connection()
    return pd.read_sql(query, conn)


# ==========================
# Executive KPIs
# ==========================

def get_total_titles():
    return run_query("""
        SELECT COUNT(*) AS total_titles
        FROM ANALYTICS.FACT_CONTENT
    """)


def get_movies():
    return run_query("""
        SELECT COUNT(*) AS movies
        FROM ANALYTICS.FACT_CONTENT
        WHERE TYPE='MOVIE'
    """)


def get_shows():
    return run_query("""
        SELECT COUNT(*) AS shows
        FROM ANALYTICS.FACT_CONTENT
        WHERE TYPE='SHOW'
    """)


def get_avg_imdb():
    return run_query("""
        SELECT ROUND(AVG(IMDB_SCORE),2) AS imdb
        FROM ANALYTICS.FACT_CONTENT
    """)


def get_avg_tmdb():
    return run_query("""
        SELECT ROUND(AVG(TMDB_SCORE),2) AS tmdb
        FROM ANALYTICS.FACT_CONTENT
    """)


def get_country_count():
    return run_query("""
        SELECT COUNT(*) AS countries
        FROM ANALYTICS.DIM_COUNTRY
    """)


def get_genre_count():
    return run_query("""
        SELECT COUNT(*) AS genres
        FROM ANALYTICS.DIM_GENRE
    """)


def get_director_count():
    return run_query("""
        SELECT COUNT(*) AS directors
        FROM ANALYTICS.DIM_DIRECTOR
    """)


# ==========================
# Charts
# ==========================

def movies_vs_shows():
    return run_query("""
        SELECT
            TYPE,
            COUNT(*) AS TOTAL
        FROM ANALYTICS.FACT_CONTENT
        GROUP BY TYPE
    """)


def titles_by_year():
    return run_query("""
        SELECT
            RELEASE_YEAR,
            COUNT(*) AS TOTAL
        FROM ANALYTICS.FACT_CONTENT
        GROUP BY RELEASE_YEAR
        ORDER BY RELEASE_YEAR
    """)


# ==========================
# Content Trends
# ==========================

def get_titles_by_year():
    return run_query("""
        SELECT
            RELEASE_YEAR,
            COUNT(*) AS TOTAL
        FROM ANALYTICS.FACT_CONTENT
        GROUP BY RELEASE_YEAR
        ORDER BY RELEASE_YEAR
    """)


def get_movies_vs_shows_by_year():
    return run_query("""
        SELECT
            RELEASE_YEAR,
            TYPE,
            COUNT(*) AS TOTAL
        FROM ANALYTICS.FACT_CONTENT
        GROUP BY RELEASE_YEAR, TYPE
        ORDER BY RELEASE_YEAR
    """)


def get_runtime_distribution():
    return run_query("""
        SELECT
            RUNTIME
        FROM ANALYTICS.FACT_CONTENT
        WHERE RUNTIME IS NOT NULL
    """)


def get_avg_imdb_by_year():
    return run_query("""
        SELECT
            RELEASE_YEAR,
            ROUND(AVG(IMDB_SCORE),2) AS AVG_IMDB
        FROM ANALYTICS.FACT_CONTENT
        WHERE IMDB_SCORE IS NOT NULL
        GROUP BY RELEASE_YEAR
        ORDER BY RELEASE_YEAR
    """)

# ==========================
# Search Catalog
# ==========================


def get_catalog():
    return run_query("""
        SELECT
            TITLE,
            TYPE,
            RELEASE_YEAR,
            AGE_CERTIFICATION,
            RUNTIME,
            IMDB_SCORE,
            TMDB_SCORE
        FROM ANALYTICS.FACT_CONTENT
        ORDER BY TITLE
    """)

# ==========================
# Rating Distribution
# ==========================

def get_imdb_distribution():
    return run_query("""
        SELECT
            IMDB_SCORE
        FROM ANALYTICS.FACT_CONTENT
        WHERE IMDB_SCORE IS NOT NULL
    """)


def get_tmdb_distribution():
    return run_query("""
        SELECT
            TMDB_SCORE
        FROM ANALYTICS.FACT_CONTENT
        WHERE TMDB_SCORE IS NOT NULL
    """)


def get_age_certification_distribution():
    return run_query("""
        SELECT
            AGE_CERTIFICATION,
            COUNT(*) AS TOTAL
        FROM ANALYTICS.FACT_CONTENT
        WHERE AGE_CERTIFICATION IS NOT NULL
        GROUP BY AGE_CERTIFICATION
        ORDER BY TOTAL DESC
    """)


def get_top_rated_titles():
    return run_query("""
        SELECT
            TITLE,
            TYPE,
            RELEASE_YEAR,
            IMDB_SCORE,
            TMDB_SCORE
        FROM ANALYTICS.FACT_CONTENT
        WHERE IMDB_SCORE IS NOT NULL
        ORDER BY IMDB_SCORE DESC,
                 IMDB_VOTES DESC
        LIMIT 20
    """)