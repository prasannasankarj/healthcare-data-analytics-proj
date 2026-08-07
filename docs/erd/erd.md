PATIENTS
--------
PatientID (PK)
Name
Gender
DOB
City
InsuranceID

        │
        │
        │
        ▼

ADMISSIONS
-----------
AdmissionID (PK)
PatientID (FK)
DoctorID (FK)
DepartmentID (FK)
AdmissionDate
DischargeDate
Diagnosis

        │
        │
        │
        ▼

DOCTORS
--------
DoctorID (PK)
DoctorName
DepartmentID (FK)
Specialization

        │
        │
        ▼

DEPARTMENTS
------------
DepartmentID (PK)
DepartmentName

        │
        ▼

BILLING
---------
BillID (PK)
AdmissionID (FK)
TotalAmount
InsuranceAmount
PatientAmount
PaymentStatus

        │
        ▼

LAB_RESULTS
-------------
LabID (PK)
AdmissionID (FK)
TestName
Result
ResultDate