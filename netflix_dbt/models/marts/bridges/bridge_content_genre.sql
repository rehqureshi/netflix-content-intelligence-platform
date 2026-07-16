{{ config(materialized='table') }}

SELECT
    t.ID AS CONTENT_ID,
    TRIM(f.VALUE::STRING, '"') AS GENRE
FROM {{ ref('stg_titles') }} t,
LATERAL FLATTEN(
    INPUT => PARSE_JSON(REPLACE(t.GENRES, '''', '"'))
) f
WHERE t.GENRES IS NOT NULL