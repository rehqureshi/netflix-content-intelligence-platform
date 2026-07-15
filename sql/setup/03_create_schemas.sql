-- =====================================================================
-- File: 03_create_schemas.sql
-- Purpose: Create the layered schemas (RAW -> STAGING -> ANALYTICS)
--          that structure the Netflix Content Intelligence Platform's
--          data pipeline following a standard medallion-style layout.
-- Prerequisite: Run 02_create_database.sql first (or issue
--               `USE DATABASE NETFLIX_DB;`) so these schemas are created
--               inside the correct database.
-- =====================================================================

-- Ensure we are operating inside the correct database context before
-- creating schemas, in case this script is run independently.
USE DATABASE NETFLIX_DB;

-- RAW: Landing zone for untransformed, ingested source data
-- (e.g. raw Netflix catalog exports, ratings, viewing logs).
-- Data here should be treated as immutable and as close to the
-- source format as possible.
CREATE SCHEMA IF NOT EXISTS RAW
    DATA_RETENTION_TIME_IN_DAYS = 1  -- Short retention; raw data can be re-ingested from source if needed
    COMMENT                     = 'Landing zone for raw, untransformed source data ingested from external systems';

-- STAGING: Intermediate schema for cleaned, conformed, and lightly
-- transformed data (type casting, deduplication, standardization)
-- before it is modeled for analytics consumption.
CREATE SCHEMA IF NOT EXISTS STAGING
    DATA_RETENTION_TIME_IN_DAYS = 1  -- Short retention; staging data is derived and reproducible from RAW
    COMMENT                     = 'Intermediate schema for cleaned and conformed data prior to analytics modeling';

-- ANALYTICS: Curated, business-ready schema exposing final fact/dimension
-- tables and views intended for BI tools, dashboards, and downstream
-- consumption.
CREATE SCHEMA IF NOT EXISTS ANALYTICS
    DATA_RETENTION_TIME_IN_DAYS = 1  -- Short retention acceptable for a dev project; raise for prod if rollback protection is needed
    COMMENT                     = 'Curated, business-ready schema for analytics-facing tables and views';

-- Verify all three schemas were created successfully within NETFLIX_DB.
SHOW SCHEMAS IN DATABASE NETFLIX_DB;