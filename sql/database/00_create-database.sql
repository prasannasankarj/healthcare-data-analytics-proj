-- =====================================================
-- Project: Healthcare Data Analytics Pipeline
-- Database: healthcare_analytics
-- Author: Prasanna Sankar J
-- =====================================================

-- Delete the database if it already exists
DROP DATABASE IF EXISTS healthcare_analytics;

-- Create a new database
CREATE DATABASE healthcare_analytics
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Use the database
USE healthcare_analytics;

-- Verify database
SELECT DATABASE() AS CurrentDatabase;