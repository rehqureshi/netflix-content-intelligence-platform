select

    person_id,

    id,

    name as actor_name,

    character

from {{ ref('stg_credits') }}

where upper(role)='ACTOR'