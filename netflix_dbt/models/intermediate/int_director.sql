select

    person_id,

    id,

    name as director_name

from {{ ref('stg_credits') }}

where upper(role)='DIRECTOR'