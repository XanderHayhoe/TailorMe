from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import requests
from bs4 import BeautifulSoup
import pickle
load_dotenv()  # Loads variables from .env

driver_path = os.environ.get("CHROMEDRIVER_PATH")
print(driver_path)

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

cookies_file = "cookies.pkl"
jobs_url = "https://www.linkedin.com/jobs"

def login_and_save_cookies():
    driver.get("https://www.linkedin.com/login")
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_input = driver.find_element(By.ID, "password")
    email_input.send_keys(os.environ.get("LINKEDIN_EMAIL"))
    password_input.send_keys(os.environ.get("LINKEDIN_PASSWORD"))
    sign_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    sign_in_button.click()
    WebDriverWait(driver, 10).until(EC.url_contains("/feed"))  # Wait for login to complete
    with open(cookies_file, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

def load_cookies_and_navigate():
    driver.get("https://www.linkedin.com")  # Must visit domain before adding cookies
    with open(cookies_file, "rb") as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(jobs_url)
    wait = WebDriverWait(driver, 10)
    job_title_inputs = driver.find_elements(By.CSS_SELECTOR, "input[aria-label='Search by title, skill, or company']")
    for input_box in job_title_inputs:
        if input_box.is_displayed() and input_box.is_enabled():
            input_box.clear()
            input_box.send_keys("Software Engineer")
            break
    else:
        print("No interactable input found!")

    location_inputs = driver.find_elements(By.CSS_SELECTOR, "input[aria-label='City, state, or zip code']")
    for location_box in location_inputs:
        if location_box.is_displayed() and location_box.is_enabled():
            location_box.clear()
            location_box.send_keys("Toronto, Ontario, Canada")
            break
    else:
        print("No interactable location input found!")

if not os.path.exists(cookies_file):
    login_and_save_cookies()
    driver.get(jobs_url)
else:
    load_cookies_and_navigate()

print(driver.page_source)  # Print the HTML after login/cookie load

time.sleep(20)
driver.quit()


