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

def get_catalog_details():
    return run_query("""
        SELECT
            ID,
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

def get_actors(content_id):
    return run_query(f"""
        SELECT
            A.ACTOR_NAME
        FROM ANALYTICS.BRIDGE_CONTENT_ACTOR B
        JOIN ANALYTICS.DIM_ACTOR A
            ON B.PERSON_ID = A.PERSON_ID
        WHERE B.CONTENT_ID = '{content_id}'
        ORDER BY A.ACTOR_NAME
    """)

def get_directors(content_id):
    return run_query(f"""
        SELECT
            D.DIRECTOR_NAME
        FROM ANALYTICS.BRIDGE_CONTENT_DIRECTOR B
        JOIN ANALYTICS.DIM_DIRECTOR D
            ON B.PERSON_ID = D.PERSON_ID
        WHERE B.CONTENT_ID = '{content_id}'
        ORDER BY D.DIRECTOR_NAME
    """)

def get_genres(content_id):
    return run_query(f"""
        SELECT
            GENRE
        FROM ANALYTICS.BRIDGE_CONTENT_GENRE
        WHERE CONTENT_ID = '{content_id}'
        ORDER BY GENRE
    """)

def get_countries(content_id):
    return run_query(f"""
        SELECT
            COUNTRY
        FROM ANALYTICS.BRIDGE_CONTENT_COUNTRY
        WHERE CONTENT_ID = '{content_id}'
        ORDER BY COUNTRY
    """)

def get_top_actors():

    return run_query("""
        SELECT
            A.ACTOR_NAME,
            COUNT(*) AS TOTAL_TITLES
        FROM ANALYTICS.BRIDGE_CONTENT_ACTOR B
        JOIN ANALYTICS.DIM_ACTOR A
            ON B.PERSON_ID = A.PERSON_ID
        GROUP BY A.ACTOR_NAME
        ORDER BY TOTAL_TITLES DESC
        LIMIT 20
    """)
def get_highest_rated_actors():

    return run_query("""
        SELECT
            A.ACTOR_NAME,
            ROUND(AVG(F.IMDB_SCORE),2) AS AVG_IMDB,
            COUNT(*) AS TITLES
        FROM ANALYTICS.BRIDGE_CONTENT_ACTOR B

        JOIN ANALYTICS.DIM_ACTOR A
            ON B.PERSON_ID=A.PERSON_ID

        JOIN ANALYTICS.FACT_CONTENT F
            ON B.CONTENT_ID=F.ID

        WHERE F.IMDB_SCORE IS NOT NULL

        GROUP BY A.ACTOR_NAME

        HAVING COUNT(*) >= 3

        ORDER BY AVG_IMDB DESC

        LIMIT 20
    """)

def get_actor_list():

    return run_query("""
        SELECT
            ACTOR_NAME
        FROM ANALYTICS.DIM_ACTOR
        ORDER BY ACTOR_NAME
    """)
def get_actor_filmography(actor):

    return run_query(f"""
        SELECT
            F.TITLE,
            F.RELEASE_YEAR,
            F.TYPE,
            F.IMDB_SCORE
        FROM ANALYTICS.BRIDGE_CONTENT_ACTOR B

        JOIN ANALYTICS.DIM_ACTOR A
            ON B.PERSON_ID=A.PERSON_ID

        JOIN ANALYTICS.FACT_CONTENT F
            ON B.CONTENT_ID=F.ID

        WHERE A.ACTOR_NAME = '{actor}'

        ORDER BY F.RELEASE_YEAR DESC
    """)
def get_top_directors():

    return run_query("""
        SELECT
            D.DIRECTOR_NAME,
            COUNT(*) AS TOTAL_TITLES
        FROM ANALYTICS.BRIDGE_CONTENT_DIRECTOR B

        JOIN ANALYTICS.DIM_DIRECTOR D
            ON B.PERSON_ID = D.PERSON_ID

        GROUP BY D.DIRECTOR_NAME

        ORDER BY TOTAL_TITLES DESC

        LIMIT 20
    """)

def get_highest_rated_directors():

    return run_query("""
        SELECT
            D.DIRECTOR_NAME,
            ROUND(AVG(F.IMDB_SCORE),2) AS AVG_IMDB,
            COUNT(*) AS TITLES
        FROM ANALYTICS.BRIDGE_CONTENT_DIRECTOR B

        JOIN ANALYTICS.DIM_DIRECTOR D
            ON B.PERSON_ID = D.PERSON_ID

        JOIN ANALYTICS.FACT_CONTENT F
            ON B.CONTENT_ID = F.ID

        WHERE F.IMDB_SCORE IS NOT NULL

        GROUP BY D.DIRECTOR_NAME

        HAVING COUNT(*) >= 3

        ORDER BY AVG_IMDB DESC

        LIMIT 20
    """)

def get_director_list():

    return run_query("""
        SELECT
            DIRECTOR_NAME
        FROM ANALYTICS.DIM_DIRECTOR
        ORDER BY DIRECTOR_NAME
    """)

def get_director_filmography(director):

    return run_query(f"""
        SELECT
            F.TITLE,
            F.RELEASE_YEAR,
            F.TYPE,
            F.IMDB_SCORE
        FROM ANALYTICS.BRIDGE_CONTENT_DIRECTOR B

        JOIN ANALYTICS.DIM_DIRECTOR D
            ON B.PERSON_ID = D.PERSON_ID

        JOIN ANALYTICS.FACT_CONTENT F
            ON B.CONTENT_ID = F.ID

        WHERE D.DIRECTOR_NAME = '{director}'

        ORDER BY F.RELEASE_YEAR DESC
    """)

def get_country_ratings():

    return run_query("""
        SELECT
            C.COUNTRY,
            ROUND(AVG(F.IMDB_SCORE),2) AS AVG_IMDB
        FROM ANALYTICS.BRIDGE_CONTENT_COUNTRY C

        JOIN ANALYTICS.FACT_CONTENT F
            ON C.CONTENT_ID = F.ID

        WHERE F.IMDB_SCORE IS NOT NULL

        GROUP BY C.COUNTRY

        HAVING COUNT(*) >= 5

        ORDER BY AVG_IMDB DESC
    """)

def get_genre_ratings():

    return run_query("""
        SELECT
            G.GENRE,
            ROUND(AVG(F.IMDB_SCORE),2) AS AVG_IMDB
        FROM ANALYTICS.BRIDGE_CONTENT_GENRE G

        JOIN ANALYTICS.FACT_CONTENT F
            ON G.CONTENT_ID = F.ID

        WHERE F.IMDB_SCORE IS NOT NULL

        GROUP BY G.GENRE

        ORDER BY AVG_IMDB DESC
    """)

def get_top_genres():

    return run_query("""
        SELECT
            GENRE,
            COUNT(*) AS TOTAL_TITLES
        FROM ANALYTICS.BRIDGE_CONTENT_GENRE
        GROUP BY GENRE
        ORDER BY TOTAL_TITLES DESC
        LIMIT 20
    """)

def get_top_countries():

    return run_query("""
        SELECT
            COUNTRY,
            COUNT(*) AS TOTAL_TITLES
        FROM ANALYTICS.BRIDGE_CONTENT_COUNTRY
        GROUP BY COUNTRY
        ORDER BY TOTAL_TITLES DESC
        LIMIT 20
    """)