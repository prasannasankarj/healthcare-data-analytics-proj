from python.validation.validation_utils import *

print("\nPatient Validation")

count = execute_scalar("""

SELECT COUNT(*)

FROM Patients

""")

print_result(

"Patient Table Not Empty",

count > 0,

f"Rows = {count}"

)

duplicate = execute_scalar("""

SELECT COUNT(*)

FROM

(

SELECT PatientID

FROM Patients

GROUP BY PatientID

HAVING COUNT(*)>1

) x

""")

print_result(

"No Duplicate Patient IDs",

duplicate == 0,

f"Duplicates = {duplicate}"

)

missing = execute_scalar("""

SELECT COUNT(*)

FROM Patients

WHERE PatientName IS NULL

""")

print_result(

"Patient Names Present",

missing == 0,

f"Missing = {missing}"

)