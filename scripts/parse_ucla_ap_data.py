import json
import pandas as pd

# Step 1: Load the JSON data from file
with open("data/ucla_ap_data.json", "r") as f:
    data = json.load(f)

# Step 2: Extract metadata and AP test list
university_name = data["values"]["name"]
ap_tests = data["values"]["examTypes"]

# Step 3: Initialize clean rows list
rows = []

# Step 4: Loop through each AP test entry
for test in ap_tests:
    exam_name = test["examType"]
    credit_rules = test["value"]

    if credit_rules is None:
        continue

    for rule in credit_rules:
        # Extract and clean each field
        try:
            min_score = int(rule["apcpMinScoreRequired"])
        except (ValueError, TypeError):
            min_score = None

        try:
            credits_awarded = int(rule["apcpCreditsAwarded"])
        except (ValueError, TypeError):
            credits_awarded = None

        course_equivalent = rule.get("apcpCourseEquivalent", "")
        if course_equivalent:
            course_equivalent = str(course_equivalent).strip().replace("\t", " ").replace("\n", " ")

        credit_used_for = rule.get("apcpCreditUsedFor", "Unspecified")
        if credit_used_for in ["None/Not Specified", None]:
            credit_used_for = "Unspecified"

        row = {
            "university": university_name,
            "ap_exam": exam_name.strip(),
            "min_score": min_score,
            "credits_awarded": credits_awarded,
            "course_equivalent": course_equivalent,
            "credit_used_for": credit_used_for,
            "school_major": rule.get("apcpSchoolMajor", "All")
        }
        rows.append(row)

# Step 5: Convert to DataFrame and sort by exam + score
df = pd.DataFrame(rows)
df = df.sort_values(by=["ap_exam", "min_score"])

# Step 6: Save cleaned version
df.to_csv("data/ucla_ap_clean.csv", index=False)
print("✅ Saved improved data to data/ucla_ap_clean.csv")
print(df.head(10))
