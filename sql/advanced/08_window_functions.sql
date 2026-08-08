USE healthcare_analytics;

-- =============================================
-- Window Functions
-- =============================================

-- Revenue Ranking
SELECT d.DepartmentName, SUM(b.TotalAmount) AS Revenue,
       RANK() OVER (ORDER BY SUM(b.TotalAmount) DESC) AS DepartmentRank
FROM billing b
JOIN admissions a ON b.AdmissionID = a.AdmissionID
JOIN departments d ON a.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;

-- Dense Rank
SELECT DoctorName, ExperienceYears,
       DENSE_RANK() OVER (ORDER BY ExperienceYears DESC) AS ExperienceRank
FROM doctors;

-- Row Number
SELECT DoctorName, DepartmentID,
       ROW_NUMBER() OVER (PARTITION BY DepartmentID ORDER BY ExperienceYears DESC) AS DoctorOrder
FROM doctors;

-- Running Revenue
SELECT CreatedAt, SUM(TotalAmount) AS DailyRevenue,
       SUM(SUM(TotalAmount)) OVER (ORDER BY CreatedAt) AS RunningRevenue
FROM billing
GROUP BY CreatedAt;
