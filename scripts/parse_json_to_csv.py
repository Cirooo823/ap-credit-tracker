import json
import csv
import os

# Paths
input_path = "data/raw/ucla.json"
output_dir = "data/parsed"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "ucla.csv")

# Load JSON
with open(input_path, "r") as f:
    data = json.load(f)

org_name = data["values"]["name"]
exam_data = data["values"]["examTypes"]

# CSV header
headers = [
    "university",
    "ap_exam",
    "min_score",
    "credits_awarded",
    "course_equivalent",
    "credit_used_for",
    "school_major"
]

rows = []

for exam in exam_data:
    ap_exam = exam["examType"]
    values = exam.get("value")
    if not values:
        continue  # Skip empty entries

    for credit in values:
        row = [
            org_name,
            ap_exam,
            credit.get("apcpMinScoreRequired"),
            credit.get("apcpCreditsAwarded"),
            credit.get("apcpCourseEquivalent"),
            credit.get("apcpCreditUsedFor"),
            credit.get("apcpSchoolMajor")
        ]
        rows.append(row)

# Write CSV
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"✅ Saved CSV to {output_path}")
