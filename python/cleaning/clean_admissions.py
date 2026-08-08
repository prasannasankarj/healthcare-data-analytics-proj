from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "admissions.csv"
CLEANED_FILE = BASE_DIR / "data" / "cleaned" / "admissions.csv"


def clean():
    print("Cleaning admissions...")

    df = pd.read_csv(RAW_FILE)

    df = df.dropna(how="all")

    df = df.drop_duplicates()

    # Clean text fields
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Convert IDs
    id_columns = [
        "AdmissionID",
        "PatientID",
        "DoctorID",
        "DepartmentID"
    ]

    for column in id_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # Remove records without AdmissionID
    df = df.dropna(subset=["AdmissionID"])

    df["AdmissionID"] = df["AdmissionID"].astype(int)

    # Convert dates
    for column in [
        "AdmissionDate",
        "DischargeDate"
    ]:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    # Remove invalid admission dates
    if "AdmissionDate" in df.columns:
        df = df.dropna(subset=["AdmissionDate"])

    # Discharge date cannot be before admission date
    if "DischargeDate" in df.columns:
        df = df[
            (
                df["DischargeDate"].isna()
            )
            |
            (
                df["DischargeDate"]
                >= df["AdmissionDate"]
            )
        ]

    # Convert valid IDs to integers
    for column in [
        "PatientID",
        "DoctorID",
        "DepartmentID"
    ]:
        if column in df.columns:
            df = df.dropna(subset=[column])
            df[column] = df[column].astype(int)

    # Remove duplicate admissions
    df = df.drop_duplicates(
        subset=["AdmissionID"]
    )

    CLEANED_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        CLEANED_FILE,
        index=False,
        date_format="%Y-%m-%d"
    )

    print(f"Admissions cleaned: {len(df)} rows")
    print(f"Saved to: {CLEANED_FILE}")


if __name__ == "__main__":
    clean()