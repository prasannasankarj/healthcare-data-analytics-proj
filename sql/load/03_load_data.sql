USE healthcare_analytics;

SELECT COUNT(*) AS departments FROM departments;
SELECT COUNT(*) AS doctors FROM doctors;
SELECT COUNT(*) AS patients FROM patients;
SELECT COUNT(*) AS admissions FROM admissions;
SELECT COUNT(*) AS billing FROM billing;
SELECT COUNT(*) AS labresults FROM labresults;

-- Sample Records
SELECT * FROM departments LIMIT 10;
SELECT * FROM doctors LIMIT 10;
SELECT * FROM patients LIMIT 10;
SELECT * FROM admissions LIMIT 10;
SELECT * FROM billing LIMIT 10;
SELECT * FROM labresults LIMIT 10;
