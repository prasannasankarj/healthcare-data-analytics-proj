from sqlalchemy import text

from db_connection import engine

tables = [

    "Departments",

    "Doctors",

    "Patients",

    "Admissions",

    "Billing",

    "LabResults"

]

with engine.connect() as conn:

    for table in tables:

        result = conn.execute(

            text(f"SELECT COUNT(*) FROM {table}")

        )

        count = result.scalar()

        print(f"{table}: {count}")