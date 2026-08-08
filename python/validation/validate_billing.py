from python.validation.validation_utils import *

print("\nBilling Validation")

negative = execute_scalar("""

SELECT COUNT(*)

FROM Billing

WHERE TotalAmount < 0

""")

print_result(

"No Negative Bills",

negative == 0,

f"Negative Bills = {negative}"

)

null_status = execute_scalar("""

SELECT COUNT(*)

FROM Billing

WHERE PaymentStatus IS NULL

""")

print_result(

"Payment Status Available",

null_status == 0,

f"Missing = {null_status}"

)