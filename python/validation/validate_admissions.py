from python.validation.validation_utils import *

print("\nAdmission Validation")

count = execute_scalar("""

SELECT COUNT(*)

FROM Admissions

""")

print_result(

"Admissions Exist",

count > 0,

f"Rows = {count}"

)

invalid_dates = execute_scalar("""

SELECT COUNT(*)

FROM Admissions

WHERE DischargeDate < AdmissionDate

""")

print_result(

"Valid Admission Dates",

invalid_dates == 0,

f"Invalid = {invalid_dates}"

)