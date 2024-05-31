import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

URL = "https://www.linkedin.com/feed/?trk=IN-SEM_google-adwords_Jordan-brand-sign-up"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

login_email = driver.find_elements(By.ID, value="username")
login_email.send_keys("")