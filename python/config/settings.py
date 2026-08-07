from pathlib import Path

# Root folder
ROOT_DIR = Path(__file__).resolve().parents[2]

# Data folders
DATA_DIR = ROOT_DIR / "data"

RAW_DATA = DATA_DIR / "raw"
CLEANED_DATA = DATA_DIR / "cleaned"
PROCESSED_DATA = DATA_DIR / "processed"

# Automatically create folders
RAW_DATA.mkdir(parents=True, exist_ok=True)
CLEANED_DATA.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

# Number of records

NUM_DEPARTMENTS = 20
NUM_DOCTORS = 250
NUM_PATIENTS = 5000
NUM_ADMISSIONS = 15000
NUM_BILLING = NUM_ADMISSIONS
NUM_LAB_RESULTS = 40000
