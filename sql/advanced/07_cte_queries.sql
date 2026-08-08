USE healthcare_analytics;

-- =============================================
-- Common Table Expressions (CTEs)
-- =============================================

-- 1. Department Revenue
WITH DepartmentRevenue AS (
    SELECT d.DepartmentName, SUM(b.TotalAmount) AS Revenue
    FROM billing b
    JOIN admissions a ON b.AdmissionID = a.AdmissionID
    JOIN departments d ON a.DepartmentID = d.DepartmentID
    GROUP BY d.DepartmentName
)
SELECT * FROM DepartmentRevenue ORDER BY Revenue DESC;

-- 2. Top Revenue Department
WITH DepartmentRevenue AS (
    SELECT d.DepartmentName, SUM(b.TotalAmount) AS Revenue
    FROM billing b
    JOIN admissions a ON b.AdmissionID = a.AdmissionID
    JOIN departments d ON a.DepartmentID = d.DepartmentID
    GROUP BY d.DepartmentName
)
SELECT * FROM DepartmentRevenue
WHERE Revenue = (SELECT MAX(Revenue) FROM DepartmentRevenue);

-- 3. Average Bill Per Department
WITH Bills AS (
    SELECT d.DepartmentName, AVG(b.TotalAmount) AS AvgBill
    FROM billing b
    JOIN admissions a ON b.AdmissionID = a.AdmissionID
    JOIN departments d ON a.DepartmentID = d.DepartmentID
    GROUP BY d.DepartmentName
)
SELECT * FROM Bills ORDER BY AvgBill DESC;
