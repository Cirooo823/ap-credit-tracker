import requests
import json

# Step 1: Define the URL for UCLA (school ID = 992)
url = "https://hdcapcp.collegeplanning-prod.collegeboard.org/992/ap.json"

# Step 2: Send a GET request to the API
response = requests.get(url)

# Step 3: Check if the request succeeded (status code 200)
if response.status_code == 200:
    print("Data fetched successfully!")

    # Step 4: Convert the response to JSON (a Python dictionary)
    data = response.json()

    # Step 5: (Optional) Save it to a JSON file in the /data folder
    with open("data/ucla_ap_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Data saved to data/ucla_ap_data.json")
else:
    print("Failed to fetch data. Status code:", response.status_code)
