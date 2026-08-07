USE healthcare_analytics;

-- =====================================================
-- Indexes for Better Query Performance
-- =====================================================

-- Patients
CREATE INDEX idx_patients_city
ON Patients(City);

CREATE INDEX idx_patients_insurance
ON Patients(InsuranceProvider);

-- Doctors
CREATE INDEX idx_doctor_department
ON Doctors(DepartmentID);

-- Admissions
CREATE INDEX idx_admission_patient
ON Admissions(PatientID);

CREATE INDEX idx_admission_doctor
ON Admissions(DoctorID);

CREATE INDEX idx_admission_department
ON Admissions(DepartmentID);

CREATE INDEX idx_admission_date
ON Admissions(AdmissionDate);

CREATE INDEX idx_admission_diagnosis
ON Admissions(Diagnosis);

-- Billing
CREATE INDEX idx_billing_status
ON Billing(PaymentStatus);

CREATE INDEX idx_billing_admission
ON Billing(AdmissionID);

-- Lab Results
CREATE INDEX idx_lab_admission
ON LabResults(AdmissionID);

CREATE INDEX idx_lab_test
ON LabResults(TestName);

CREATE INDEX idx_lab_result
ON LabResults(ResultStatus);

SHOW INDEX FROM Patients;
SHOW INDEX FROM Doctors;
SHOW INDEX FROM Admissions;
SHOW INDEX FROM Billing;
SHOW INDEX FROM LabResults;