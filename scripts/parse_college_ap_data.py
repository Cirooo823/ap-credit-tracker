import json
import csv
from typing import List, Dict, Any


def parse_ap_json(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    university_name = data["values"].get("name", "")
    exams = data["values"].get("examTypes", [])
    rows = []

    for exam in exams:
        exam_name = exam.get("examType", "")
        values = exam.get("value", [])

        if not values:
            continue

        for entry in values:
            row = {
                "university": university_name,
                "ap_exam": exam_name,
                "min_score": entry.get("apcpMinScoreRequired", ""),
                "credits_awarded": entry.get("apcpCreditsAwarded", ""),
                "course_equivalent": entry.get("apcpCourseEquivalent", ""),
                "credit_used_for": entry.get("apcpCreditUsedFor", "Unspecified"),
                "school_major": entry.get("apcpSchoolMajor", "All")
            }
            rows.append(row)

    return rows


def save_to_csv(rows: List[Dict[str, Any]], filename: str):
    if not rows:
        print("No data to write.")
        return

    fieldnames = ["university", "ap_exam", "min_score", "credits_awarded",
                  "course_equivalent", "credit_used_for", "school_major"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Saved {len(rows)} rows to {filename}")


if __name__ == "__main__":
    with open("ucla.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = parse_ap_json(data)
    save_to_csv(rows, "ucla_parsed.csv")
