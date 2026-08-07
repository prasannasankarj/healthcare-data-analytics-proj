USE healthcare_analytics;

SELECT COUNT(*) AS Departments FROM Departments;

SELECT COUNT(*) AS Doctors FROM Doctors;

SELECT COUNT(*) AS Patients FROM Patients;

SELECT COUNT(*) AS Admissions FROM Admissions;

SELECT COUNT(*) AS Billing FROM Billing;

SELECT COUNT(*) AS LabResults FROM LabResults;

-- Sample Records

SELECT * FROM Departments LIMIT 10;

SELECT * FROM Doctors LIMIT 10;

SELECT * FROM Patients LIMIT 10;

SELECT * FROM Admissions LIMIT 10;

SELECT * FROM Billing LIMIT 10;

SELECT * FROM LabResults LIMIT 10;