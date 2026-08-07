USE healthcare_analytics;

-- =====================================================
-- 1 Total Patients
-- =====================================================

SELECT COUNT(*) AS TotalPatients
FROM Patients;

-- =====================================================
-- 2 Male vs Female
-- =====================================================

SELECT

Gender,

COUNT(*) AS Total

FROM Patients

GROUP BY Gender;

-- =====================================================
-- 3 Patients by City
-- =====================================================

SELECT

City,

COUNT(*) AS TotalPatients

FROM Patients

GROUP BY City

ORDER BY TotalPatients DESC;

-- =====================================================
-- 4 Admissions by Department
-- =====================================================

SELECT

dept.DepartmentName,

COUNT(*) AS Admissions

FROM Admissions a

JOIN Departments dept

ON a.DepartmentID=dept.DepartmentID

GROUP BY dept.DepartmentName

ORDER BY Admissions DESC;

-- =====================================================
-- 5 Average Billing
-- =====================================================

SELECT

ROUND(AVG(TotalAmount),2)

AS AverageBill

FROM Billing;

-- =====================================================
-- 6 Revenue by Department
-- =====================================================

SELECT

dept.DepartmentName,

SUM(b.TotalAmount) AS Revenue

FROM Billing b

JOIN Admissions a

ON b.AdmissionID=a.AdmissionID

JOIN Departments dept

ON a.DepartmentID=dept.DepartmentID

GROUP BY dept.DepartmentName

ORDER BY Revenue DESC;

-- =====================================================
-- 7 Top 10 Doctors
-- =====================================================

SELECT

d.DoctorName,

COUNT(*) AS PatientCount

FROM Admissions a

JOIN Doctors d

ON a.DoctorID=d.DoctorID

GROUP BY d.DoctorName

ORDER BY PatientCount DESC

LIMIT 10;

-- =====================================================
-- 8 Pending Bills
-- =====================================================

SELECT *

FROM Billing

WHERE PaymentStatus='Pending';

-- =====================================================
-- 9 Lab Tests
-- =====================================================

SELECT

TestName,

COUNT(*) AS Total

FROM LabResults

GROUP BY TestName

ORDER BY Total DESC;

-- =====================================================
-- 10 Average Length of Stay
-- =====================================================

SELECT

ROUND(

AVG(

DATEDIFF(

DischargeDate,

AdmissionDate)

),2)

AS AvgStay

FROM Admissions;