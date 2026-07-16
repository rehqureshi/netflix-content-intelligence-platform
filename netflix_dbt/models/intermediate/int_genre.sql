with titles as (

    select
        id,
        genres
    from {{ ref('stg_titles') }}

),

cleaned as (

    select
        id,
        trim(value::string) as genre

    from titles,

    lateral flatten(
        input => split(
            replace(
                replace(
                    replace(genres,'[',''),
                ']',''),
            '''',''),
        ',')
    )

)

select
    id,
    genre
from cleaned
where genre <> ''