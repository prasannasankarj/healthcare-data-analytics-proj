import random
import pandas as pd
from faker import Faker

from config.settings import RAW_DATA, NUM_PATIENTS
from utils.constants import CITIES, INSURANCE
from utils.logger import logger

fake = Faker()

def generate():
    rows = []

    for _ in range(NUM_PATIENTS):
        phone = fake.msisdn()[:15]  # numeric-only, safe length
        rows.append({
            "PatientName": fake.name(),
            "Gender": random.choice(["Male", "Female"]),
            "DateOfBirth": fake.date_of_birth(minimum_age=1, maximum_age=95),
            "City": random.choice(CITIES),
            "State": fake.state(),
            "BloodGroup": random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]),
            "InsuranceProvider": random.choice(INSURANCE),
            "Phone": phone,
            "Email": fake.email()
        })

    pd.DataFrame(rows).to_csv(
        RAW_DATA / "patients.csv",
        index=False
    )

    logger.info("Patients generated")

if __name__ == "__main__":
    generate()
