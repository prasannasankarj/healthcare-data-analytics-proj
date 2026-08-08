USE healthcare_analytics;

-- =============================================
-- KPI Dashboard Queries
-- =============================================

SELECT
    (SELECT COUNT(*) FROM patients) AS TotalPatients,
    (SELECT COUNT(*) FROM doctors) AS TotalDoctors,
    (SELECT COUNT(*) FROM admissions) AS TotalAdmissions,
    (SELECT COUNT(*) FROM billing) AS TotalBills,
    (SELECT SUM(TotalAmount) FROM billing) AS Revenue,
    (SELECT AVG(TotalAmount) FROM billing) AS AverageBill,
    (SELECT COUNT(*) FROM billing WHERE PaymentStatus = 'Pending') AS PendingBills;
