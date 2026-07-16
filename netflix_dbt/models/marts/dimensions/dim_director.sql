select distinct

    person_id,

    director_name

from {{ ref('int_director') }}