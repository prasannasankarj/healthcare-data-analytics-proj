import random
import pandas as pd
from faker import Faker

from config.settings import RAW_DATA, NUM_BILLING
from utils.logger import logger

fake = Faker()

def generate():
    rows = []

    for bill in range(1, NUM_BILLING + 1):
        total = random.randint(2000, 250000)
        insurance = random.randint(0, total)

        rows.append({
            # BillID is auto-increment in DB, so we don’t include it in CSV
            "AdmissionID": bill,
            "TotalAmount": total,
            "InsuranceAmount": insurance,
            "PatientAmount": total - insurance,
            "PaymentStatus": random.choice(["Paid", "Pending", "Partially Paid"]),
            "PaymentMethod": random.choice(["Cash", "Card", "UPI", "Insurance"]),
            "BillingDate": fake.date_between(start_date="-2y", end_date="today")
        })

    pd.DataFrame(rows).to_csv(
        RAW_DATA / "billing.csv",
        index=False
    )

    logger.info("Billing generated")

if __name__ == "__main__":
    generate()
