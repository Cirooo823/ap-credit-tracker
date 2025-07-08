# scripts/launch_browser.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# Headless is OFF to see the browser
# options.add_argument("--headless")  # DO NOT USE THIS
options.add_argument("--window-size=1200,800")

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")

input("Press Enter to close...")
driver.quit()
