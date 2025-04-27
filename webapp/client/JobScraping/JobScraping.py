from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
load_dotenv()  # Loads variables from .env

driver_path = os.environ.get("CHROMEDRIVER_PATH")
print(driver_path)

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/login")


wait = WebDriverWait(driver, 10)
email_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
password_input = driver.find_element(By.ID, "password")

linkedin_email = os.environ.get("LINKEDIN_EMAIL")
linkedin_password = os.environ.get("LINKEDIN_PASSWORD")

email_input.send_keys(linkedin_email)
password_input.send_keys(linkedin_password)

sign_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in_button.click()

time.sleep(20)
driver.quit()






# # Job Title
# job_title = "Software Engineer"

# # Location
# location = "San Francisco, CA"
