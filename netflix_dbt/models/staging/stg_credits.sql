with source as (

    select *
    from {{ source('raw', 'credits') }}

),

renamed as (

    select

        person_id,
        id,
        name,
        character,
        role

    from source

)

select *
from renamed