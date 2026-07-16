select distinct

    genre

from {{ ref('int_genre') }}

where genre is not null