from python.validation.validation_utils import *

print("\nLab Validation")

count = execute_scalar("""

SELECT COUNT(*)

FROM LabResults

""")

print_result(

"Lab Results Exist",

count > 0,

f"Rows = {count}"

)

missing_test = execute_scalar("""

SELECT COUNT(*)

FROM LabResults

WHERE TestName IS NULL

""")

print_result(

"Test Names Present",

missing_test == 0,

f"Missing = {missing_test}"

)