USE healthcare_analytics;

-- =============================================
-- Subqueries
-- =============================================

-- 1. Highest Bill
SELECT * 
FROM billing
WHERE TotalAmount = (SELECT MAX(TotalAmount) FROM billing);

-- 2. Patients Above Average Bill
SELECT PatientName
FROM patients
WHERE PatientID IN (
    SELECT a.PatientID
    FROM admissions a
    JOIN billing b ON a.AdmissionID = b.AdmissionID
    WHERE b.TotalAmount > (SELECT AVG(TotalAmount) FROM billing)
);

-- 3. Departments Above Average Revenue
SELECT * 
FROM (
    SELECT d.DepartmentName, SUM(b.TotalAmount) AS Revenue
    FROM billing b
    JOIN admissions a ON b.AdmissionID = a.AdmissionID
    JOIN departments d ON a.DepartmentID = d.DepartmentID
    GROUP BY d.DepartmentName
) x
WHERE Revenue > (
    SELECT AVG(Revenue) 
    FROM (
        SELECT SUM(TotalAmount) AS Revenue
        FROM billing b
        JOIN admissions a ON b.AdmissionID = a.AdmissionID
        GROUP BY DepartmentID
    ) t
);
