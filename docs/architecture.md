# System Architecture

```
               +-----------------------+
               | Python Data Generator |
               +-----------+-----------+
                           |
                           |
                    CSV Files Generated
                           |
                           ▼
                 +--------------------+
                 | Python ETL Loader  |
                 +---------+----------+
                           |
                           |
                           ▼
                 +--------------------+
                 | MySQL Database     |
                 +---------+----------+
                           |
             SQL Queries / Views
                           |
                           ▼
                +---------------------+
                | Power BI Dashboard  |
                +---------------------+
```

## Components

### Python Generator

Creates realistic healthcare datasets.

### ETL Loader

Loads CSV files into MySQL.

### Database

Stores relational healthcare data.

### SQL Layer

Business reporting.

### Power BI

Visualization and dashboards.