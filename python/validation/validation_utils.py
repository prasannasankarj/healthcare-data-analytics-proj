# File: python/validation/validation_utils.py

from sqlalchemy import text
# Use relative import since validation and database are sibling packages
from ..database.db_connection import engine


def execute_scalar(query: str):
    """Execute a query and return a single scalar value."""
    with engine.connect() as conn:
        return conn.execute(text(query)).scalar()


def execute_rows(query: str):
    """Execute a query and return all rows as a list of tuples."""
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()


def print_result(title: str, passed: bool, details: str = ""):
    """Print a formatted validation result with PASS/FAIL status."""
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {title}")
    if details:
        print(details)
