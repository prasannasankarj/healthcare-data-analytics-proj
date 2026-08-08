import sys
from pathlib import Path

# Add project Python directory to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
PYTHON_DIR = PROJECT_ROOT / "python"

sys.path.insert(0, str(PYTHON_DIR))

from cleaning import (
    clean_departments,
    clean_doctors,
    clean_patients,
    clean_admissions,
    clean_billing,
    clean_lab_results,
)


def main():

    print("=" * 70)
    print("Healthcare Data Cleaning Pipeline")
    print("=" * 70)

    clean_departments.clean()

    clean_doctors.clean()

    clean_patients.clean()

    clean_admissions.clean()

    clean_billing.clean()

    clean_lab_results.clean()

    print("\n" + "=" * 70)
    print("All datasets cleaned successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()