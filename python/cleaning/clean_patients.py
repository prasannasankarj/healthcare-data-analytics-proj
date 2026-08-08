from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "patients.csv"
CLEANED_FILE = BASE_DIR / "data" / "cleaned" / "patients.csv"

def clean():
    print("Cleaning patients...")

    df = pd.read_csv(RAW_FILE)

    # Drop completely empty rows
    df = df.dropna(how="all")

    # Drop exact duplicates
    df = df.drop_duplicates()

    # Clean text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Required fields (excluding PatientID, since DB auto-generates it)
    required_columns = ["PatientName", "Gender", "DateOfBirth"]
    df = df.dropna(subset=[col for col in required_columns if col in df.columns])

    # Date of birth validation
    if "DateOfBirth" in df.columns:
        df["DateOfBirth"] = pd.to_datetime(df["DateOfBirth"], errors="coerce")
        df = df.dropna(subset=["DateOfBirth"])

    # Deduplicate by PatientName + DateOfBirth
    if {"PatientName", "DateOfBirth"} <= set(df.columns):
        df = df.drop_duplicates(subset=["PatientName", "DateOfBirth"])

    CLEANED_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        CLEANED_FILE,
        index=False,
        date_format="%Y-%m-%d"
    )

    print(f"Patients cleaned: {len(df)} rows")
    print(f"Saved to: {CLEANED_FILE}")

if __name__ == "__main__":
    clean()
