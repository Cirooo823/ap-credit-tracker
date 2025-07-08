from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Setup
options = Options()
options.add_argument("--window-size=1200,800")
# options.add_argument("--headless")  # Optional

driver = webdriver.Chrome(options=options)
driver.get("https://apstudents.collegeboard.org/getting-credit-placement/search-policies")

try:
    wait = WebDriverWait(driver, 15)

    # Step 1: Click "Find Your College"
    college_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Find Your College')]")))
    college_radio.click()
    print("✅ Clicked 'Find Your College'")

    # Step 2: Wait for input box to appear
    search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='College name']")))

    # Step 3: Click into the box using ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(search_input).click().perform()
    print("✅ Focused on the input box")

    # Step 4: Type the college name
    search_input.send_keys("University of California")
    print("✅ Typed into the search input")

    input("⏳ Press Enter to close browser...")

finally:
    driver.quit()
