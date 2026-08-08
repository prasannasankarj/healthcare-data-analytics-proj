USE healthcare_analytics;

-- ============================================================
-- HEALTHCARE ANALYTICS QUERIES
-- ============================================================

-- 1. Total Patients
SELECT COUNT(*) AS TotalPatients
FROM patients;

-- 2. Total Doctors
SELECT COUNT(*) AS TotalDoctors
FROM doctors;

-- 3. Total Admissions
SELECT COUNT(*) AS TotalAdmissions
FROM admissions;

-- 4. Total Revenue
SELECT ROUND(SUM(TotalAmount),2) AS TotalRevenue
FROM billing;

-- 5. Male vs Female Patients
SELECT Gender, COUNT(*) AS TotalPatients
FROM patients
GROUP BY Gender;

-- 6. Patients by Insurance Provider
SELECT InsuranceProvider, COUNT(*) AS Patients
FROM patients
GROUP BY InsuranceProvider
ORDER BY Patients DESC;

-- 7. Top Cities by Patient Count
SELECT City, COUNT(*) AS PatientCount
FROM patients
GROUP BY City
ORDER BY PatientCount DESC;

-- 8. Doctors per Department
SELECT dept.DepartmentName, COUNT(*) AS Doctors
FROM doctors d
JOIN departments dept ON d.DepartmentID = dept.DepartmentID
GROUP BY dept.DepartmentName
ORDER BY Doctors DESC;

-- 9. Admissions by Department
SELECT dept.DepartmentName, COUNT(*) AS Admissions
FROM admissions a
JOIN departments dept ON a.DepartmentID = dept.DepartmentID
GROUP BY dept.DepartmentName
ORDER BY Admissions DESC;

-- 10. Revenue by Department
SELECT dept.DepartmentName, ROUND(SUM(b.TotalAmount),2) AS Revenue
FROM billing b
JOIN admissions a ON b.AdmissionID = a.AdmissionID
JOIN departments dept ON a.DepartmentID = dept.DepartmentID
GROUP BY dept.DepartmentName
ORDER BY Revenue DESC;

-- 11. Average Bill Amount
SELECT ROUND(AVG(TotalAmount),2) AS AverageBill
FROM billing;

-- 12. Highest Bill (Top 10)
SELECT * FROM billing
ORDER BY TotalAmount DESC
LIMIT 10;

-- 13. Pending Bills
SELECT * FROM billing
WHERE PaymentStatus='Pending';

-- 14. Revenue by Payment Status
SELECT PaymentStatus, ROUND(SUM(TotalAmount),2) AS Revenue
FROM billing
GROUP BY PaymentStatus;

-- 15. Average Hospital Stay
SELECT ROUND(AVG(DATEDIFF(a.DischargeDate, a.AdmissionDate)),2) AS AvgStay
FROM admissions a
WHERE a.DischargeDate IS NOT NULL;

-- 16. Longest Stay
SELECT AdmissionID, DATEDIFF(DischargeDate, AdmissionDate) AS DaysStayed
FROM admissions
WHERE DischargeDate IS NOT NULL
ORDER BY DaysStayed DESC
LIMIT 20;

-- 17. Most Common Diagnosis
SELECT Diagnosis, COUNT(*) AS Cases
FROM admissions
GROUP BY Diagnosis
ORDER BY Cases DESC;

-- 18. Top Doctors by Admissions
SELECT d.DoctorName, COUNT(*) AS PatientsHandled
FROM admissions a
JOIN doctors d ON a.DoctorID = d.DoctorID
GROUP BY d.DoctorName
ORDER BY PatientsHandled DESC
LIMIT 10;

-- 19. Lab Tests Performed
SELECT TestName, COUNT(*) AS Total
FROM labresults
GROUP BY TestName
ORDER BY Total DESC;

-- 20. Abnormal Lab Results
SELECT TestName, COUNT(*) AS Abnormal
FROM labresults
WHERE ResultStatus='Abnormal'
GROUP BY TestName
ORDER BY Abnormal DESC;

-- 21. Patient Admission History
SELECT p.PatientName, a.AdmissionDate, a.DischargeDate, a.Diagnosis
FROM admissions a
JOIN patients p ON a.PatientID = p.PatientID
ORDER BY p.PatientName;

-- 22. Monthly Admissions
SELECT YEAR(AdmissionDate) AS Year, MONTHNAME(AdmissionDate) AS Month, COUNT(*) AS Admissions
FROM admissions
GROUP BY Year, Month
ORDER BY Year, Month;

-- 23. Monthly Revenue
SELECT YEAR(CreatedAt) AS Year, MONTHNAME(CreatedAt) AS Month, ROUND(SUM(TotalAmount),2) AS Revenue
FROM billing
GROUP BY Year, Month
ORDER BY Year, Month;

-- 24. Top 10 Cities by Revenue
SELECT p.City, ROUND(SUM(b.TotalAmount),2) AS Revenue
FROM billing b
JOIN admissions a ON b.AdmissionID = a.AdmissionID
JOIN patients p ON a.PatientID = p.PatientID
GROUP BY p.City
ORDER BY Revenue DESC
LIMIT 10;

-- 25. Revenue by Insurance Provider
SELECT p.InsuranceProvider, ROUND(SUM(b.TotalAmount),2) AS Revenue
FROM billing b
JOIN admissions a ON b.AdmissionID = a.AdmissionID
JOIN patients p ON a.PatientID = p.PatientID
GROUP BY p.InsuranceProvider
ORDER BY Revenue DESC;

-- 26. Doctor Experience Analysis
SELECT DoctorName, ExperienceYears
FROM doctors
ORDER BY ExperienceYears DESC;

-- 27. Patients Age Distribution
SELECT CASE
    WHEN TIMESTAMPDIFF(YEAR, DateOfBirth, CURDATE()) < 18 THEN 'Child'
    WHEN TIMESTAMPDIFF(YEAR, DateOfBirth, CURDATE()) BETWEEN 18 AND 40 THEN 'Young Adult'
    WHEN TIMESTAMPDIFF(YEAR, DateOfBirth, CURDATE()) BETWEEN 41 AND 60 THEN 'Adult'
    ELSE 'Senior'
END AS AgeGroup, COUNT(*) AS TotalPatients
FROM patients
GROUP BY AgeGroup;

-- 28. Department Revenue Ranking
SELECT dept.DepartmentName, ROUND(SUM(b.TotalAmount),2) AS Revenue,
       RANK() OVER (ORDER BY SUM(b.TotalAmount) DESC) AS Ranking
FROM billing b
JOIN admissions a ON b.AdmissionID = a.AdmissionID
JOIN departments dept ON a.DepartmentID = dept.DepartmentID
GROUP BY dept.DepartmentName;

-- 29. Highest Revenue Patient
SELECT p.PatientName, ROUND(SUM(b.TotalAmount),2) AS Revenue
FROM billing b
JOIN admissions a ON b.AdmissionID = a.AdmissionID
JOIN patients p ON a.PatientID = p.PatientID
GROUP BY p.PatientName
ORDER BY Revenue DESC
LIMIT 20;

-- 30. Dashboard KPI Query
SELECT
    (SELECT COUNT(*) FROM patients) AS TotalPatients,
    (SELECT COUNT(*) FROM doctors) AS TotalDoctors,
    (SELECT COUNT(*) FROM admissions) AS TotalAdmissions,
    (SELECT COUNT(*) FROM billing) AS TotalBills,
    (SELECT ROUND(SUM(TotalAmount),2) FROM billing) AS Revenue;
