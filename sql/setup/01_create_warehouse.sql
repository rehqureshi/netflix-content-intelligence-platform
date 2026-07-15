-- =====================================================================
-- File: 01_create_warehouse.sql
-- Purpose: Provision the compute warehouse for the Netflix Content
--          Intelligence Platform project.
-- Notes:   Sized for a small development / portfolio project. Adjust
--          SIZE and AUTO_SUSPEND upward only if workloads grow.
-- =====================================================================

-- Create the warehouse only if it doesn't already exist, so this script
-- is safe to re-run without erroring out or disrupting an active warehouse.
CREATE WAREHOUSE IF NOT EXISTS NETFLIX_WH
    WAREHOUSE_SIZE       = 'XSMALL'   -- Smallest compute size; sufficient for dev/test workloads and keeps credit usage low
    AUTO_SUSPEND          = 60         -- Suspend after 60 seconds of inactivity to avoid burning credits when idle
    AUTO_RESUME           = TRUE       -- Automatically resume the warehouse when a new query is submitted
    INITIALLY_SUSPENDED   = TRUE       -- Start in a suspended state so no credits are consumed until first use
    MIN_CLUSTER_COUNT     = 1          -- Single cluster minimum; no need for multi-cluster scaling in a dev project
    MAX_CLUSTER_COUNT     = 1          -- Cap at one cluster to prevent unexpected auto-scaling costs
    SCALING_POLICY        = 'STANDARD' -- Default scaling policy (irrelevant at 1 cluster, but explicit for clarity/future-proofing)
    COMMENT               = 'Warehouse for Netflix Content Intelligence Platform - dev/test workloads';

-- Verify the warehouse was created with the expected properties.
SHOW WAREHOUSES LIKE 'NETFLIX_WH';

-- Set this warehouse as the active one for the current session so
-- subsequent scripts (database/schema creation) run against it.
USE WAREHOUSE NETFLIX_WH;