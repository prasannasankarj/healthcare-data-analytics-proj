from sqlalchemy import text
from db_connection import engine

# Use lowercase names to match actual MySQL tables
tables = [
    "departments",
    "doctors",
    "patients",
    "admissions",
    "billing",
    "labresults"
]

with engine.connect() as conn:
    for table in tables:
        result = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        )
        count = result.scalar()
        print(f"{table}: {count}")