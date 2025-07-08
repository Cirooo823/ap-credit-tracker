import requests
import os
import time

# List of universities and their org IDs
universities = {
    "ucla": 992,
    # Add more universities here like:
    # "harvard": 693,
    # "berkeley": 991,
}

# Where to save files
os.makedirs("data/raw", exist_ok=True)

# Download function
def download_all_university_jsons():
    base_url = "https://hdcapcp.collegeplanning-prod.collegeboard.org"
    for name, org_id in universities.items():
        url = f"{base_url}/{org_id}/ap.json"
        print(f"Downloading {name.upper()} from {url}...")
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            filepath = f"data/raw/{name}.json"
            with open(filepath, "w") as f:
                import json
                json.dump(data, f, indent=2)
            print(f"✅ Saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to fetch data for {name}: {e}")
        except ValueError:
            print(f"❌ Failed to parse JSON for {name}")
        
        # Be polite to the server
        time.sleep(1)

if __name__ == "__main__":
    download_all_university_jsons()
