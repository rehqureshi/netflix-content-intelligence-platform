{{ config(materialized='table') }}

SELECT DISTINCT
    ID AS CONTENT_ID,
    PERSON_ID
FROM {{ ref('stg_credits') }}
WHERE ROLE = 'DIRECTOR'