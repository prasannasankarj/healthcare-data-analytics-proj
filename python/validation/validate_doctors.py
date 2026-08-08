from python.validation.validation_utils import *

print("\nDoctor Validation")

count = execute_scalar("""

SELECT COUNT(*)

FROM Doctors

""")

print_result(

"Doctor Table Not Empty",

count > 0,

f"Rows = {count}"

)

missing_department = execute_scalar("""

SELECT COUNT(*)

FROM Doctors

WHERE DepartmentID IS NULL

""")

print_result(

"No Missing Department",

missing_department == 0,

f"Missing = {missing_department}"

)