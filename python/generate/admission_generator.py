import random

import pandas as pd
from faker import Faker

from config.settings import RAW_DATA, NUM_ADMISSIONS
from utils.constants import DIAGNOSIS
from utils.logger import logger

fake = Faker()


def generate():

    rows=[]

    for admission in range(1, NUM_ADMISSIONS + 1):

        admission_date = fake.date_between("-2y","today")

        discharge = fake.date_between(
            admission_date,
            "+10d"
        )

        rows.append({

            "AdmissionID": admission,

            "PatientID": random.randint(1,5000),

            "DoctorID": random.randint(1,250),

            "DepartmentID": random.randint(1,20),

            "AdmissionDate": admission_date,

            "DischargeDate": discharge,

            "Diagnosis": random.choice(DIAGNOSIS)

        })

    pd.DataFrame(rows).to_csv(
        RAW_DATA / "admissions.csv",
        index=False
    )

    logger.info("Admissions generated")