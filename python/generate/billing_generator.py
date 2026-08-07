import random

import pandas as pd

from config.settings import RAW_DATA, NUM_BILLING
from utils.logger import logger


def generate():

    rows=[]

    for bill in range(1, NUM_BILLING + 1):

        total = random.randint(2000,250000)

        insurance = random.randint(0,total)

        rows.append({

            "BillID": bill,

            "AdmissionID": bill,

            "TotalAmount": total,

            "InsuranceAmount": insurance,

            "PatientAmount": total-insurance,

            "PaymentStatus": random.choice(
                ["Paid","Pending","Partially Paid"]
            )

        })

    pd.DataFrame(rows).to_csv(
        RAW_DATA / "billing.csv",
        index=False
    )

    logger.info("Billing generated")