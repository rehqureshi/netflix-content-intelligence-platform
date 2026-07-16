with source as (

    select *
    from {{ source('raw', 'titles') }}

),

renamed as (

    select

        id,
        title,
        type,
        description,
        cast(release_year as integer) as release_year,
        age_certification,
        cast(runtime as integer) as runtime,
        genres,
        production_countries,
        cast(seasons as integer) as seasons,
        imdb_id,
        cast(imdb_score as float) as imdb_score,
        cast(imdb_votes as integer) as imdb_votes,
        cast(tmdb_popularity as float) as tmdb_popularity,
        cast(tmdb_score as float) as tmdb_score

    from source

)

select *
from renamed where title is not null and id is not null