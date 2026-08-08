from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "lab_results.csv"
CLEANED_FILE = BASE_DIR / "data" / "cleaned" / "lab_results.csv"


def clean():
    print("Cleaning lab results...")

    df = pd.read_csv(RAW_FILE)

    df = df.dropna(how="all")

    df = df.drop_duplicates()

    # Clean text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # IDs
    if "LabResultID" in df.columns:

        df["LabResultID"] = pd.to_numeric(
            df["LabResultID"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["LabResultID"]
        )

        df["LabResultID"] = (
            df["LabResultID"].astype(int)
        )

    if "AdmissionID" in df.columns:

        df["AdmissionID"] = pd.to_numeric(
            df["AdmissionID"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["AdmissionID"]
        )

        df["AdmissionID"] = (
            df["AdmissionID"].astype(int)
        )

    # Lab date
    if "TestDate" in df.columns:

        df["TestDate"] = pd.to_datetime(
            df["TestDate"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["TestDate"]
        )

    # Remove duplicate lab IDs
    if "LabResultID" in df.columns:

        df = df.drop_duplicates(
            subset=["LabResultID"]
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

    print(f"Lab results cleaned: {len(df)} rows")
    print(f"Saved to: {CLEANED_FILE}")


if __name__ == "__main__":
    clean()
    