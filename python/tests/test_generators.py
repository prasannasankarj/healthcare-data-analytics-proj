from pathlib import Path

def test_patient_csv_exists():
    file = Path("data/raw/patients.csv")
    assert file.exists()

def test_doctor_csv_exists():
    file = Path("data/raw/doctors.csv")
    assert file.exists()

def test_billing_csv_exists():
    file = Path("data/raw/billing.csv")
    assert file.exists()

def test_lab_results_csv_exists():
    file = Path("data/raw/lab_results.csv")
    assert file.exists()
