from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "departments.csv"
CLEANED_FILE = BASE_DIR / "data" / "cleaned" / "departments.csv"


def clean():
    print("Cleaning departments...")

    df = pd.read_csv(RAW_FILE)

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove leading/trailing spaces from text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Validate DepartmentID
    df = df.dropna(subset=["DepartmentID"])

    # Convert DepartmentID to integer
    df["DepartmentID"] = df["DepartmentID"].astype(int)

    # Remove duplicate Department IDs
    df = df.drop_duplicates(subset=["DepartmentID"])

    CLEANED_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(CLEANED_FILE, index=False)

    print(f"Departments cleaned: {len(df)} rows")
    print(f"Saved to: {CLEANED_FILE}")


if __name__ == "__main__":
    clean()