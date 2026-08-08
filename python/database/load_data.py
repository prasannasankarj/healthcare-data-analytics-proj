from pathlib import Path
import pandas as pd
from db_connection import engine

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "raw"

files = {
    "departments.csv": "departments",
    "doctors.csv": "doctors",
    "patients.csv": "patients",
    "admissions.csv": "admissions",
    "billing.csv": "billing",
    "lab_results.csv": "labresults"
}

# Define primary key columns for each table
primary_keys = {
    "departments": ["DepartmentID"],
    "doctors": ["DoctorID"],
    "patients": ["PatientID"],
    "admissions": ["AdmissionID"],
    "billing": ["BillID"],
    "labresults": ["LabID"]
}

# Define unique business keys for deduplication
unique_keys = {
    "departments": ["DepartmentName"],
    "doctors": ["DoctorName", "DepartmentID"],
    "patients": ["PatientName", "DateOfBirth"],
    "admissions": ["PatientID", "DoctorID", "AdmissionDate"],
    "billing": ["AdmissionID", "BillingDate"],
    "labresults": ["AdmissionID", "TestName", "TestDate"]
}

for csv_file, table in files.items():
    path = DATA / csv_file
    print(f"Loading {csv_file}")
    df = pd.read_csv(path)

    # Drop primary key columns if present (let MySQL auto-generate IDs)
    if table in primary_keys:
        for pk in primary_keys[table]:
            if pk in df.columns:
                df = df.drop(columns=[pk])

    # Fix column mismatch for doctors.csv (Experience → ExperienceYears)
    if table == "doctors" and "Experience" in df.columns:
        df = df.rename(columns={"Experience": "ExperienceYears"})

    # Deduplicate against existing records in DB
    if table in unique_keys:
        existing = pd.read_sql(f"SELECT {', '.join(unique_keys[table])} FROM {table}", con=engine)
        # Drop duplicates based on unique business keys
        df = df.merge(existing, on=unique_keys[table], how="left", indicator=True)
        df = df[df["_merge"] == "left_only"].drop(columns=["_merge"])

    if not df.empty:
        df.to_sql(
            table,
            con=engine,
            if_exists="append",
            index=False
        )
        print(f"{len(df)} new rows inserted into {table}")
    else:
        print(f"No new rows to insert into {table}")

print("\nData loading completed successfully.")
