import pandas as pd

from config.settings import RAW_DATA
from utils.constants import DEPARTMENTS
from utils.logger import logger


def generate():

    df = pd.DataFrame({
        "DepartmentID": range(1, len(DEPARTMENTS)+1),
        "DepartmentName": DEPARTMENTS
    })

    df.to_csv(RAW_DATA / "departments.csv", index=False)

    logger.info("Departments generated")