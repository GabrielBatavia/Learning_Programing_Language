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

URL = "https://www.linkedin.com/feed/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWORD)

sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value="button[data-litms-control-urn='login-submit']")
sign_in_button.click()

