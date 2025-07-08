import json
import os

data = {
  "orgId": 992,
  "values": {
    "name": "University of California: Los Angeles",
    "city": "Los Angeles",
    "state": "CA",
    "apCreditAwarded": "Yes",
    "apPlacementAwarded": "Yes",
    "apInstPolicyDescription": "UCLA awards credit for Advanced Placement (AP) exams with scores of 3 or higher. The specific credit received depends on the College/School where the student's major is located.",
    "apInstPolicyUrl": "https://admission.ucla.edu/admitted-students/ap-credit-the-college",
    "examTypes": [
      {
        "examType": "3-D Art and Design",
        "code": "33",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Physics C: Mechanics",
        "code": "27",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "PHYSICS General \u201cC\u201d",
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Music Non-Aural Subscore",
        "code": "24B",
        "value": None
      },
      {
        "examType": "Computer Science Principles",
        "code": "42",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Seminar",
        "code": "40",
        "value": None
      },
      {
        "examType": "French Language and Culture",
        "code": "14",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "FRNCH 6",
            "apcpMinScoreRequired": 5
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "FRNCH 5",
            "apcpMinScoreRequired": 4
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "FRNCH 4",
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Macroeconomics",
        "code": "22",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "None/Not Specified",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "ECON 2",
            "apcpMinScoreRequired": "5"
          }
        ]
      },
      {
        "examType": "Calculus BC: AB Subscore",
        "code": "4A",
        "value": [
          {
            "apcpSchoolMajor": "Engineering",
            "apcpCreditUsedFor": "None/Not Specified",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "Calculus",
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "MATH 31A",
            "apcpMinScoreRequired": 5
          }
        ]
      },
      {
        "examType": "English Literature and Composition",
        "code": "11",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "None/Not Specified",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": "8",
            "apcpCourseEquivalent": "ENGCOMP 3",
            "apcpMinScoreRequired": 4
          }
        ]
      },
      {
        "examType": "Spanish Literature and Culture",
        "code": "30",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "SPAN Literature",
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Chinese Language and Culture",
        "code": "6",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Art History",
        "code": "1",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Spanish Language and Culture",
        "code": "29",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "SPAN 5",
            "apcpMinScoreRequired": 5
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "SPAN 4",
            "apcpMinScoreRequired": 4
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "SPAN 3",
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "World History: Modern",
        "code": "37",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Physics C: Electricity and Magnetism",
        "code": "26",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "PHYSICS General \u201cC\u201d",
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Physics 1",
        "code": "38",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "PHYSICS General",
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Chemistry",
        "code": "5",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "General Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 4
          }
        ]
      },
      {
        "examType": "German Language and Culture",
        "code": "16",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "GERMAN 3",
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "GERMAN 5",
            "apcpMinScoreRequired": 5
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "GERMAN 4",
            "apcpMinScoreRequired": 4
          }
        ]
      },
      {
        "examType": "Statistics",
        "code": "31",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "None/Not Specified",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "STATS Unassigned",
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Calculus AB",
        "code": "3",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "MATH 31A",
            "apcpMinScoreRequired": 5
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Calculus BC",
        "code": "4",
        "value": [
          {
            "apcpSchoolMajor": "Engineering",
            "apcpCreditUsedFor": "None/Not Specified",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "Corresponding Major",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "MATH 31A/Calculus",
            "apcpMinScoreRequired": 4
          },
          {
            "apcpSchoolMajor": "Corresponding Major",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "MATH 31A/31B",
            "apcpMinScoreRequired": 5
          }
        ]
      },
      {
        "examType": "Comparative Government and Politics",
        "code": "7",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "African American Studies",
        "code": "43",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditsAwarded": "4",
            "apcpCourseEquivalent": "HIST\tUnited States",
            "apcpMinScoreRequired": "3"
          }
        ]
      },
      {
        "examType": "Pre-Calculus",
        "code": "44",
        "value": None
      },
      {
        "examType": "Computer Science A",
        "code": "8",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "None/Not Specified",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Human Geography",
        "code": "17",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Cybersecurity (Career Kickstart)",
        "code": "47",
        "value": None
      },
      {
        "examType": "Networking (Career Kickstart)",
        "code": "46",
        "value": None
      },
      {
        "examType": "Business with Personal Finance",
        "code": "45",
        "value": None
      },
      {
        "examType": "Psychology",
        "code": "28",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "None/Not Specified",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "PSYCH Unassigned",
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "PSYCH 10",
            "apcpMinScoreRequired": 4
          }
        ]
      },
      {
        "examType": "Physics 2",
        "code": "39",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "PHYSICS General",
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Music Aural Subscore",
        "code": "24A",
        "value": None
      },
      {
        "examType": "Drawing",
        "code": "34",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Japanese Language and Culture",
        "code": "19",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "2-D Art and Design",
        "code": "32",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "United States Government and Politics",
        "code": "35",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Latin",
        "code": "21",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "LATIN 1",
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "LATIN 3",
            "apcpMinScoreRequired": 4
          }
        ]
      },
      {
        "examType": "Music Theory",
        "code": "24",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Microeconomics",
        "code": "23",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "None/Not Specified",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": "ECON 1",
            "apcpMinScoreRequired": "5"
          }
        ]
      },
      {
        "examType": "Environmental Science",
        "code": "12",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 4,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "English Language and Composition",
        "code": "10",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "None/Not Specified",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "ENGCOMP 3",
            "apcpMinScoreRequired": 4
          }
        ]
      },
      {
        "examType": "United States History",
        "code": "36",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Italian Language and Culture",
        "code": "18",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "ITALIAN 4",
            "apcpMinScoreRequired": 4
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "ITALIAN 6",
            "apcpMinScoreRequired": 5
          },
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Corresponding Course",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": "ITALIAN 3",
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Biology",
        "code": "2",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      },
      {
        "examType": "Research",
        "code": "41",
        "value": None
      },
      {
        "examType": "European History",
        "code": "13",
        "value": [
          {
            "apcpSchoolMajor": "All",
            "apcpCreditUsedFor": "Dept Elective",
            "apcpPlacementOnly": None,
            "apcpCreditsAwarded": 8,
            "apcpCourseEquivalent": None,
            "apcpMinScoreRequired": 3
          }
        ]
      }
    ]
  }
}

os.makedirs("data/raw", exist_ok=True)

# Write JSON to file
with open("data/raw/ucla.json", "w") as f:
    json.dump(data, f, indent=2)

print("Saved to data/raw/ucla.json")