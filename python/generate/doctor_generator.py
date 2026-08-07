import random

import pandas as pd
from faker import Faker

from config.settings import RAW_DATA, NUM_DOCTORS
from utils.logger import logger

fake = Faker()


def generate():

    rows = []

    for doctor in range(1, NUM_DOCTORS + 1):

        rows.append({
            "DoctorID": doctor,
            "DoctorName": "Dr. " + fake.name(),
            "DepartmentID": random.randint(1,20),
            "Experience": random.randint(1,35)
        })

    pd.DataFrame(rows).to_csv(
        RAW_DATA / "doctors.csv",
        index=False
    )

    logger.info("Doctors generated")