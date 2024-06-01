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

URL = "https://tinder.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(5)

accept_button = driver.find_element(By.XPATH, "//div[text()='I accept']")
accept_button.click()

time.sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

time.sleep(2)
    
# Locate the Google login button and click it
google_login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[1]/div/div/div/iframe')
google_login_button.click()
time.sleep(5)


email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys(EMAIL)