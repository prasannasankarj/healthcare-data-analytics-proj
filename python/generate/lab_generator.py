import random
import pandas as pd
from faker import Faker

from config.settings import RAW_DATA, NUM_LAB_RESULTS
from utils.constants import LAB_TESTS
from utils.logger import logger

fake = Faker()

def generate():
    rows = []

    for lab in range(1, NUM_LAB_RESULTS + 1):
        rows.append({
            "AdmissionID": random.randint(1, 15000),
            "TestName": random.choice(LAB_TESTS),
            "ResultStatus": random.choice(["Normal", "Abnormal", "Borderline"]),  # matches schema
            "TestValue": str(random.randint(50, 200)),  # optional numeric/string value
            "TestDate": fake.date_between(start_date="-2y", end_date="today")
        })

    pd.DataFrame(rows).to_csv(
        RAW_DATA / "lab_results.csv",
        index=False
    )

    logger.info("Lab results generated")

if __name__ == "__main__":
    generate()
