from python.validation.validation_utils import *

print("\nDepartment Validation")

count = execute_scalar("""

SELECT COUNT(*)

FROM Departments

""")

print_result(

"Department Table Not Empty",

count > 0,

f"Rows = {count}"

)

duplicate = execute_scalar("""

SELECT COUNT(*)

FROM

(

SELECT DepartmentName

FROM Departments

GROUP BY DepartmentName

HAVING COUNT(*)>1

) x

""")

print_result(

"No Duplicate Departments",

duplicate == 0,

f"Duplicates = {duplicate}"

)