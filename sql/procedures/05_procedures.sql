USE healthcare_analytics;

DELIMITER $$

CREATE PROCEDURE GetPatientHistory
(
IN p_patient_id INT
)

BEGIN

SELECT

p.PatientName,

a.AdmissionDate,

a.DischargeDate,

a.Diagnosis,

d.DoctorName,

dept.DepartmentName

FROM Admissions a

JOIN Patients p
ON a.PatientID=p.PatientID

JOIN Doctors d
ON a.DoctorID=d.DoctorID

JOIN Departments dept
ON a.DepartmentID=dept.DepartmentID

WHERE p.PatientID=p_patient_id

ORDER BY a.AdmissionDate DESC;

END $$

DELIMITER ;

-- Example

CALL GetPatientHistory(10);