-- =====================================================================
-- File: 02_create_database.sql
-- Purpose: Provision the database that will house all schemas, tables,
--          and objects for the Netflix Content Intelligence Platform.
-- Prerequisite: Run 01_create_warehouse.sql first (or ensure a
--               warehouse is active) so subsequent DDL has compute
--               context, although CREATE DATABASE itself is metadata-only
--               and does not require an active warehouse.
-- =====================================================================

-- Create the database only if it doesn't already exist, keeping this
-- script idempotent and safe for repeated deployment runs.
CREATE DATABASE IF NOT EXISTS NETFLIX_DB
    DATA_RETENTION_TIME_IN_DAYS = 1  -- Minimal Time Travel retention for a dev project; keeps storage costs low (raise to 7-90 for prod compliance needs)
    COMMENT                     = 'Primary database for the Netflix Content Intelligence Platform project';

-- Confirm the database exists and inspect its properties.
SHOW DATABASES LIKE 'NETFLIX_DB';

-- Set this database as the active database for the current session so
-- the next script (schema creation) targets it by default.
USE DATABASE NETFLIX_DB;