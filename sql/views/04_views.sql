USE healthcare_analytics;

-- =====================================================
-- Patient Admission View
-- =====================================================

CREATE OR REPLACE VIEW vw_patient_admissions AS

SELECT

a.AdmissionID,

p.PatientName,

p.Gender,

TIMESTAMPDIFF(YEAR,p.DateOfBirth,CURDATE()) AS Age,

p.City,

d.DoctorName,

dept.DepartmentName,

a.AdmissionDate,

a.DischargeDate,

a.Diagnosis

FROM Admissions a

JOIN Patients p
ON a.PatientID=p.PatientID

JOIN Doctors d
ON a.DoctorID=d.DoctorID

JOIN Departments dept
ON a.DepartmentID=dept.DepartmentID;

-- =====================================================
-- Billing View
-- =====================================================

CREATE OR REPLACE VIEW vw_billing_summary AS

SELECT

b.BillID,

p.PatientName,

dept.DepartmentName,

b.TotalAmount,

b.InsuranceAmount,

b.PatientAmount,

b.PaymentStatus

FROM Billing b

JOIN Admissions a
ON b.AdmissionID=a.AdmissionID

JOIN Patients p
ON a.PatientID=p.PatientID

JOIN Departments dept
ON a.DepartmentID=dept.DepartmentID;

SELECT * FROM vw_patient_admissions LIMIT 20;

SELECT * FROM vw_billing_summary LIMIT 20;