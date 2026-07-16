with titles as (

    select
        id,
        production_countries
    from {{ ref('stg_titles') }}

),

cleaned as (

    select

        id,

        trim(value::string) as country

    from titles,

    lateral flatten(

        input => split(

            replace(
                replace(
                    replace(production_countries,'[',''),
                ']',''),
            '''',''),

        ',')

    )

)

select

    id,
    country

from cleaned

where country <> ''