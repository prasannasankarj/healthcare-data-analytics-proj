from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "billing.csv"
CLEANED_FILE = BASE_DIR / "data" / "cleaned" / "billing.csv"


def clean():
    print("Cleaning billing...")

    df = pd.read_csv(RAW_FILE)

    df = df.dropna(how="all")

    df = df.drop_duplicates()

    # Clean text fields
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Convert IDs
    if "BillID" in df.columns:
        df["BillID"] = pd.to_numeric(
            df["BillID"],
            errors="coerce"
        )

        df = df.dropna(subset=["BillID"])

        df["BillID"] = df["BillID"].astype(int)

    if "AdmissionID" in df.columns:
        df["AdmissionID"] = pd.to_numeric(
            df["AdmissionID"],
            errors="coerce"
        )

        df = df.dropna(subset=["AdmissionID"])

        df["AdmissionID"] = df["AdmissionID"].astype(int)

    # Convert monetary values
    monetary_columns = [
        "TotalAmount",
        "InsuranceAmount",
        "PatientAmount"
    ]

    for column in monetary_columns:
        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

            df = df.dropna(
                subset=[column]
            )

            # Remove negative amounts
            df = df[df[column] >= 0]

    # Billing date
    if "BillingDate" in df.columns:
        df["BillingDate"] = pd.to_datetime(
            df["BillingDate"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["BillingDate"]
        )

    # Remove duplicate bills
    if "BillID" in df.columns:
        df = df.drop_duplicates(
            subset=["BillID"]
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

    print(f"Billing records cleaned: {len(df)} rows")
    print(f"Saved to: {CLEANED_FILE}")


if __name__ == "__main__":
    clean()