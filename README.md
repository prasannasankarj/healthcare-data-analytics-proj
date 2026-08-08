# 🏥 Healthcare Data Analytics Project

## Project Overview

This repository contains a complete healthcare analytics workflow that starts with synthetic data generation and ends with SQL-based reporting and Power BI visualization.

The project flow is:

1. Generate synthetic healthcare datasets in Python
2. Save them as CSV files under the data folder
3. Load the data into a MySQL database
4. Run SQL analysis and validation queries
5. Visualize the results in Power BI

---

## What This Project Does

This project simulates a hospital analytics pipeline for questions such as:

- How many patients were admitted?
- Which departments generate the highest revenue?
- Which doctors handle the most patients?
- What are the most common diagnoses?
- Which insurance providers drive the highest billing amounts?
- What is the average length of stay?

---

## Tech Stack

- Python
- Pandas
- Faker
- MySQL
- SQLAlchemy
- Docker Compose
- SQL
- Power BI

---

## Project Structure

- data/ - Raw, cleaned, and processed datasets
- python/ - Data generation, ETL, validation, and database scripts
- sql/ - SQL scripts for database creation, views, stored procedures, and reports
- powerbi/ - Power BI dashboard assets
- screenshots/ - Dashboard screenshots

---

## Prerequisites

Make sure the following are installed on your machine:

- Python 3.10+
- Docker Desktop
- Git
- VS Code
- Power BI Desktop (optional for visualization)

---

## Step-by-Step Execution Guide

Run all commands from the project root.

### 1) Clone the repository

```powershell
git clone https://github.com/prasannasankarj/healthcare-data-analytics-proj.git
cd healthcare-data-analytics-proj
```

### 2) Create and activate a virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 3) Install Python dependencies

```powershell
pip install -r requirements.txt
```

### 4) Start MySQL using Docker Compose

```powershell
docker compose up -d
```

Verify that the MySQL container is running:

```powershell
docker compose ps
```

### 5) Create the environment file

Create a file named .env in the project root with the following content:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=healthcare_analytics
DB_USER=healthcare_user
DB_PASSWORD=healthcare_pass
```

### 6) Generate synthetic healthcare data

```powershell
python python/main.py
```

This will create CSV files under the data/raw folder.

### Copy the createtables sql file inside docker
```
docker cp "C:\Users\prasa\OneDrive\Desktop\Data_Analyst_Proj\healthcare-data-analytics-proj\sql\tables\01_create_tables.sql" healthcare_mysql:/01_create_tables.sql
```
```
docker exec -it healthcare_mysql mysql -u healthcare_user -p healthcare_analytics

password - healthcare_pass
```
```
source /01_create_tables.sql;
```

### 7) Load the generated data into MySQL

```powershell
python python/database/load_data.py
```

This step loads the CSVs into the database tables.

### 8) Verify the data in the database

```powershell
python python/database/verify_data.py
```

This prints row counts for the main tables.

### 9) Explore the SQL analytics scripts

The SQL scripts are available in the sql folder:

- sql/tables/01_create_tables.sql
- sql/load/03_load_data.sql
- sql/reports/06_analysis_queries.sql
- sql/views/04_views.sql
- sql/procedures/05_procedures.sql
- sql/advanced/07_cte_queries.sql

You can open these files in MySQL Workbench or any SQL client and run them against the database.

### 10) Open the Power BI dashboard

- Open Power BI Desktop
- Connect to your MySQL database
- Use the tables generated in the database
- Build or refresh the dashboard using the data from the project

---

## Optional Commands

Stop the MySQL container:

```powershell
docker compose down
```

Remove the MySQL data volume (useful if you want a fresh start):

```powershell
docker compose down -v
```

---

## Notes

- The project uses synthetic healthcare data, so it is ideal for learning ETL, database loading, SQL analytics, and dashboard development.
- The database schema and analytics queries are organized under the sql folder for easier learning and reuse.

---

## Author

Prasanna Sankar J

GitHub: github.com/prasannasankarj

LinkedIn: www.linkedin.com/in/prasanna-sankar-j
