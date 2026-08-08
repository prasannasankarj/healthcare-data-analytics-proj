USE healthcare_analytics;

-- =============================================
-- Interview Questions
-- =============================================

-- Q1 Top 5 Departments by Revenue
SELECT d.DepartmentName, SUM(b.TotalAmount) AS Revenue
FROM billing b
JOIN admissions a ON b.AdmissionID = a.AdmissionID
JOIN departments d ON a.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName
ORDER BY Revenue DESC
LIMIT 5;

-- Q2 Doctor Handling Most Patients
SELECT d.DoctorName, COUNT(*) AS Patients
FROM admissions a
JOIN doctors d ON a.DoctorID = d.DoctorID
GROUP BY d.DoctorName
ORDER BY Patients DESC
LIMIT 1;

-- Q3 Revenue By Payment Method
SELECT PaymentMethod, SUM(TotalAmount) AS Revenue
FROM billing
GROUP BY PaymentMethod;

-- Q4 Average Stay Per Department
SELECT d.DepartmentName,
       AVG(DATEDIFF(DischargeDate, AdmissionDate)) AS AverageStay
FROM admissions a
JOIN departments d ON a.DepartmentID = d.DepartmentID
WHERE DischargeDate IS NOT NULL
GROUP BY d.DepartmentName;

-- Q5 Top Diagnosis
SELECT Diagnosis, COUNT(*) AS Cases
FROM admissions
GROUP BY Diagnosis
ORDER BY Cases DESC
LIMIT 10;
