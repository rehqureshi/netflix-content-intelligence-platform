select distinct

    country

from {{ ref('int_country') }}

where country is not null