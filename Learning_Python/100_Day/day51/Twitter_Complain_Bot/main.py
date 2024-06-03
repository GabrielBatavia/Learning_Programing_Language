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

URL = "https://x.com/i/flow/login"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(5)

email_input = driver.find_element(By.CSS_SELECTOR, "input[name='text']")
email_input.send_keys(EMAIL)

time.sleep(5)
next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()

time.sleep(5)
password_input = driver.find_element(By.XPATH, "//input[@type='password']")
password_input.send_keys(PASSWORD)