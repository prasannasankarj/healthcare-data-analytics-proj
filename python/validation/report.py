from pathlib import Path
from python.validation.validation_utils import execute_scalar

output = []

checks = {
    "Patients": "SELECT COUNT(*) FROM Patients",
    "Doctors": "SELECT COUNT(*) FROM Doctors",
    "Admissions": "SELECT COUNT(*) FROM Admissions",
    "Billing": "SELECT COUNT(*) FROM Billing",
    "LabResults": "SELECT COUNT(*) FROM LabResults",
}

output.append("Healthcare Data Validation Report")
output.append("=" * 40)

for table, query in checks.items():
    count = execute_scalar(query)
    output.append(f"{table}: {count} rows")

report_dir = Path(__file__).resolve().parents[2] / "reports"
report_dir.mkdir(exist_ok=True)

report_path = report_dir / "validation_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write("\n".join(output))

print(f"Validation report generated: {report_path}")