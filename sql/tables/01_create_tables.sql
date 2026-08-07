USE healthcare_analytics;

-- =====================================================
-- Departments
-- =====================================================

CREATE TABLE Departments
(
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    DepartmentName VARCHAR(100) NOT NULL UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- Doctors
-- =====================================================

CREATE TABLE Doctors
(
    DoctorID INT PRIMARY KEY AUTO_INCREMENT,

    DoctorName VARCHAR(150) NOT NULL,

    DepartmentID INT NOT NULL,

    ExperienceYears INT NOT NULL,

    Phone VARCHAR(20),

    Email VARCHAR(150),

    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_doctor_department
        FOREIGN KEY (DepartmentID)
        REFERENCES Departments(DepartmentID)
);

-- =====================================================
-- Patients
-- =====================================================

CREATE TABLE Patients
(
    PatientID INT PRIMARY KEY AUTO_INCREMENT,

    PatientName VARCHAR(150) NOT NULL,

    Gender ENUM
    (
        'Male',
        'Female'
    ) NOT NULL,

    DateOfBirth DATE NOT NULL,

    City VARCHAR(100),

    State VARCHAR(100),

    BloodGroup VARCHAR(5),

    InsuranceProvider VARCHAR(100),

    Phone VARCHAR(20),

    Email VARCHAR(150),

    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- Admissions
-- =====================================================

CREATE TABLE Admissions
(
    AdmissionID INT PRIMARY KEY AUTO_INCREMENT,

    PatientID INT NOT NULL,

    DoctorID INT NOT NULL,

    DepartmentID INT NOT NULL,

    AdmissionDate DATE NOT NULL,

    DischargeDate DATE,

    Diagnosis VARCHAR(200),

    RoomNumber VARCHAR(20),

    AdmissionType ENUM
    (
        'Emergency',
        'Inpatient',
        'Outpatient'
    ) DEFAULT 'Inpatient',

    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_admission_patient
        FOREIGN KEY (PatientID)
        REFERENCES Patients(PatientID),

    CONSTRAINT fk_admission_doctor
        FOREIGN KEY (DoctorID)
        REFERENCES Doctors(DoctorID),

    CONSTRAINT fk_admission_department
        FOREIGN KEY (DepartmentID)
        REFERENCES Departments(DepartmentID)
);

-- =====================================================
-- Billing
-- =====================================================

CREATE TABLE Billing
(
    BillID INT PRIMARY KEY AUTO_INCREMENT,

    AdmissionID INT NOT NULL,

    TotalAmount DECIMAL(12,2) NOT NULL,

    InsuranceAmount DECIMAL(12,2) DEFAULT 0,

    PatientAmount DECIMAL(12,2) DEFAULT 0,

    PaymentStatus ENUM
    (
        'Paid',
        'Pending',
        'Partially Paid'
    ) DEFAULT 'Pending',

    PaymentMethod ENUM
    (
        'Cash',
        'Card',
        'UPI',
        'Insurance'
    ) DEFAULT 'Cash',

    BillingDate DATE,

    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_billing_admission
        FOREIGN KEY (AdmissionID)
        REFERENCES Admissions(AdmissionID)
);

-- =====================================================
-- Lab Results
-- =====================================================

CREATE TABLE LabResults
(
    LabID INT PRIMARY KEY AUTO_INCREMENT,

    AdmissionID INT NOT NULL,

    TestName VARCHAR(150) NOT NULL,

    ResultStatus ENUM
    (
        'Normal',
        'Abnormal',
        'Borderline'
    ),

    TestValue VARCHAR(100),

    TestDate DATE,

    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_lab_admission
        FOREIGN KEY (AdmissionID)
        REFERENCES Admissions(AdmissionID)
);

-- =====================================================
-- Verify
-- =====================================================

SHOW TABLES;