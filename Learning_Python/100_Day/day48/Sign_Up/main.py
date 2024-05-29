from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep edge browser open after open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

URL = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Edge(options=edge_options)
driver.get(URL)


firstName = driver.find_element(By.NAME, value="fName")
firstName.send_keys("Bagus")

lastName = driver.find_element(By.NAME, value="lName")
lastName.send_keys("Agus")

email = driver.find_element(By.NAME, value="email")
email.send_keys("agus@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, value=".btn.btn-lg.btn-primary.btn-block")
button.click()

# End browser
#driver.quit()