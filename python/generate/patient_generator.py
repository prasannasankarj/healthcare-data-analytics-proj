import random

import pandas as pd
from faker import Faker

from config.settings import RAW_DATA, NUM_PATIENTS
from utils.constants import CITIES, INSURANCE
from utils.logger import logger

fake = Faker()


def generate():

    rows = []

    for patient in range(1, NUM_PATIENTS + 1):

        rows.append({

            "PatientID": patient,

            "PatientName": fake.name(),

            "Gender": random.choice(["Male","Female"]),

            "Age": random.randint(1,95),

            "City": random.choice(CITIES),

            "Insurance": random.choice(INSURANCE)

        })

    pd.DataFrame(rows).to_csv(
        RAW_DATA / "patients.csv",
        index=False
    )

    logger.info("Patients generated")