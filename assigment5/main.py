from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ----------------------------
# SETUP DRIVER
# ----------------------------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(browser, 20)

# ----------------------------
# OPEN WEBSITE
# ----------------------------
browser.get("https://www.sunbeaminfo.in/")
time.sleep(3)

# ----------------------------
# CLICK INTERNSHIPS LINK
# ----------------------------
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Internships"))).click()

# ✅ WAIT UNTIL INTERNSHIP PAGE LOADS
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
time.sleep(2)

# ----------------------------
# STEP-BY-STEP SCROLL (IMPORTANT)
# ----------------------------
for _ in range(6):
    browser.execute_script("window.scrollBy(0, 600);")
    time.sleep(1)

# ----------------------------
# WAIT & CLICK TOGGLE BUTTON
# ----------------------------
plus_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='#collapseSix']"))
)

browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", plus_button)
time.sleep(1)
plus_button.click()
time.sleep(3)

# ----------------------------
# SCRAPE INTERNSHIP DETAILS
# ----------------------------
internships = browser.find_elements(By.CLASS_NAME, "course-box")

print("\n📌 Sunbeam Internship & Batch Details:\n")

for internship in internships:
    title = internship.find_element(By.TAG_NAME, "h3").text
    duration = internship.find_element(By.CLASS_NAME, "duration").text
    batch = internship.find_element(By.CLASS_NAME, "batch").text

    print("--------------------------------------")
    print("Internship Title :", title)
    print("Duration         :", duration)
    print("Batch Details    :", batch)

# ----------------------------
# CLOSE BROWSER
# ----------------------------
browser.quit()