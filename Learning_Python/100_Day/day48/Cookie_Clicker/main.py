from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://popcat.click/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(30)

cat = driver.find_element(By.CSS_SELECTOR, ".cat-img.p")

# Click the element 10 times
for _ in range(10000):
    cat.click()
