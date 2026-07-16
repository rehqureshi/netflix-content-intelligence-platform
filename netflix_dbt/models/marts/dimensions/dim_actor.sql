select distinct

    person_id,

    actor_name

from {{ ref('int_actor') }}