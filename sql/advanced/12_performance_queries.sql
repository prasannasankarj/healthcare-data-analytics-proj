USE healthcare_analytics;

-- =============================================
-- Performance Queries
-- =============================================

-- 1. Execution Plan
EXPLAIN
SELECT p.PatientName, d.DoctorName, b.TotalAmount
FROM billing b
JOIN admissions a ON b.AdmissionID = a.AdmissionID
JOIN patients p ON a.PatientID = p.PatientID
JOIN doctors d ON a.DoctorID = d.DoctorID;

-- 2. Indexes
SHOW INDEXES FROM patients;
SHOW INDEXES FROM admissions;
SHOW INDEXES FROM billing;
SHOW INDEXES FROM doctors;
SHOW INDEXES FROM departments;
