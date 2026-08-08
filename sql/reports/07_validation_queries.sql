USE healthcare_analytics;

-- =============================================
-- Data Quality Checks
-- =============================================

-- 1. Missing Patients
SELECT *
FROM patients
WHERE PatientName IS NULL;

-- 2. Duplicate Patients
SELECT PatientID, COUNT(*) AS DuplicateCount
FROM patients
GROUP BY PatientID
HAVING COUNT(*) > 1;

-- 3. Negative Billing
SELECT *
FROM billing
WHERE TotalAmount < 0;

-- 4. Invalid Admission Dates
SELECT *
FROM admissions
WHERE DischargeDate < AdmissionDate;

-- 5. Missing Doctors
SELECT *
FROM doctors
WHERE DepartmentID IS NULL;

-- 6. Missing Lab Results
SELECT *
FROM labresults
WHERE TestName IS NULL;
