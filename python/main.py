
from generate import (
    department_generator,
    doctor_generator,
    patient_generator,
    admission_generator,
    billing_generator,
    lab_generator,
)

print("=" * 60)
print("Healthcare Data Generator")
print("=" * 60)

department_generator.generate()
doctor_generator.generate()
patient_generator.generate()
admission_generator.generate()
billing_generator.generate()
lab_generator.generate()

print("\nAll datasets generated successfully!")