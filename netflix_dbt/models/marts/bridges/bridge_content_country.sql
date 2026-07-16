{{ config(materialized='table') }}

SELECT
    t.ID AS CONTENT_ID,
    TRIM(f.VALUE::STRING, '"') AS COUNTRY
FROM {{ ref('stg_titles') }} t,
LATERAL FLATTEN(
    INPUT => PARSE_JSON(REPLACE(t.PRODUCTION_COUNTRIES, '''', '"'))
) f
WHERE t.PRODUCTION_COUNTRIES IS NOT NULL