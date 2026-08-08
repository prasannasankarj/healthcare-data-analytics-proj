USE healthcare_analytics;

-- =============================================
-- Business Reports
-- =============================================

-- 1. Monthly Revenue
SELECT YEAR(CreatedAt) AS Year, MONTH(CreatedAt) AS Month,
       SUM(TotalAmount) AS Revenue
FROM billing
GROUP BY YEAR(CreatedAt), MONTH(CreatedAt)
ORDER BY Year, Month;

-- 2. Monthly Admissions
SELECT YEAR(AdmissionDate) AS Year, MONTH(AdmissionDate) AS Month,
       COUNT(*) AS Admissions
FROM admissions
GROUP BY YEAR(AdmissionDate), MONTH(AdmissionDate)
ORDER BY Year, Month;

-- 3. Top Insurance Providers
SELECT InsuranceProvider, COUNT(*) AS Patients, SUM(b.TotalAmount) AS Revenue
FROM billing b
JOIN admissions a ON b.AdmissionID = a.AdmissionID
JOIN patients p ON a.PatientID = p.PatientID
GROUP BY InsuranceProvider
ORDER BY Revenue DESC;
