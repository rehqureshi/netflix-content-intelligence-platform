select

    id,

    title,

    type,

    description,

    release_year,

    age_certification,

    runtime,

    seasons,

    imdb_id,

    imdb_score,

    imdb_votes,

    tmdb_popularity,

    tmdb_score

from {{ ref('stg_titles') }}