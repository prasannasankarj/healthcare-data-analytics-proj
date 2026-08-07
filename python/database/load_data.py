from pathlib import Path

import pandas as pd

from db_connection import engine

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data" / "raw"

files = {

    "departments.csv": "Departments",

    "doctors.csv": "Doctors",

    "patients.csv": "Patients",

    "admissions.csv": "Admissions",

    "billing.csv": "Billing",

    "lab_results.csv": "LabResults"

}

for csv_file, table in files.items():

    path = DATA / csv_file

    print(f"Loading {csv_file}")

    df = pd.read_csv(path)

    df.to_sql(

        table,

        con=engine,

        if_exists="append",

        index=False

    )

    print(f"{len(df)} rows inserted into {table}")

print("\nData loading completed successfully.")