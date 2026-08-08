from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "doctors.csv"
CLEANED_FILE = BASE_DIR / "data" / "cleaned" / "doctors.csv"


def clean():
    print("Cleaning doctors...")

    df = pd.read_csv(RAW_FILE)

    df = df.dropna(how="all")

    df = df.drop_duplicates()

    # Clean text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Remove records without required IDs
    df = df.dropna(
        subset=[
            "DoctorID",
            "DepartmentID"
        ]
    )

    # Convert IDs
    df["DoctorID"] = df["DoctorID"].astype(int)
    df["DepartmentID"] = df["DepartmentID"].astype(int)

    # Experience should not be negative
    if "ExperienceYears" in df.columns:
        df["ExperienceYears"] = pd.to_numeric(
            df["ExperienceYears"],
            errors="coerce"
        )

        df = df[df["ExperienceYears"] >= 0]

    # Remove duplicate doctor IDs
    df = df.drop_duplicates(subset=["DoctorID"])

    CLEANED_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(CLEANED_FILE, index=False)

    print(f"Doctors cleaned: {len(df)} rows")
    print(f"Saved to: {CLEANED_FILE}")


if __name__ == "__main__":
    clean()