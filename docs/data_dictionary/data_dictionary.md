# Data Dictionary

## Departments

| Column | Description |
|----------|-------------|
| DepartmentID | Department Identifier |
| DepartmentName | Department Name |

---

## Doctors

| Column | Description |
|----------|-------------|
| DoctorID | Doctor Identifier |
| DoctorName | Doctor Name |
| DepartmentID | Foreign Key |
| ExperienceYears | Experience |

---

## Patients

| Column | Description |
|----------|-------------|
| PatientID | Patient Identifier |
| PatientName | Patient Name |
| Gender | Gender |
| DateOfBirth | DOB |
| City | City |
| InsuranceProvider | Insurance |

---

## Admissions

Stores patient admissions.

---

## Billing

Stores financial information.

---

## LabResults

Stores laboratory test information.