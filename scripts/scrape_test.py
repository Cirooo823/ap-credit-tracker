from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup headless Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # runs without opening a window
driver = webdriver.Chrome(options=options)

# Load the CollegeBoard AP Credit Search page
driver.get("https://apstudents.collegeboard.org/getting-credit-placement/search-policies")

# Wait for the search input field to appear
wait = WebDriverWait(driver, 15)
search_input = wait.until(EC.presence_of_element_located((By.ID, "college-search")))

# Enter a university name and search
search_input.send_keys("UCLA")
search_input.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(5)

# Grab the credit info rows
rows = driver.find_elements(By.CLASS_NAME, "college-search-result")

# Print all row text
for row in rows:
    print(row.text)

driver.quit()
# This script uses Selenium to scrape AP credit information from the CollegeBoard website.