# File: python/validation/validate_all.py

import subprocess
import sys
from pathlib import Path

# Directory containing the validation scripts
VALIDATION_DIR = Path(__file__).resolve().parent

files = [
    "validate_departments.py",
    "validate_doctors.py",
    "validate_patients.py",
    "validate_admissions.py",
    "validate_billing.py",
    "validate_lab_results.py",
]

for file in files:
    print("=" * 70)
    subprocess.run(
        [sys.executable, "-m", f"python.validation.{file[:-3]}"],  # run as module
        check=True
    )

print("\nValidation Completed Successfully")
