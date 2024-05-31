import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3936718501&f_AL=true&f_E=1&geoId=101165590&keywords=python&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(5)

# Sign in button
sign_in_button = driver.find_element(By.CSS_SELECTOR, "a.nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWORD)

sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value="button[data-litms-control-urn='login-submit']")
sign_in_button.click()

time.sleep(30)

job = driver.find_element(By.CSS_SELECTOR, "a[data-control-name='job_card']")
job.click()

save_job = driver.find_element(by=By.CSS_SELECTOR, value="button.jobs-save-button")
save_job.click()


