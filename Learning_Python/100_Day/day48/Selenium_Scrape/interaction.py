from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep edge browser open after open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)


URL = "https://id.wikipedia.org/wiki/Joko_Widodo"


driver = webdriver.Edge(options=edge_options)
driver.get(URL)

# Find the element containing the name
figure_name_element = driver.find_element(By.CLASS_NAME, "mw-page-title-main")
figure_name = figure_name_element.text
print(figure_name)


# Find all paragraph elements
paragraph_elements = driver.find_elements(By.TAG_NAME, "p")
for paragraph in paragraph_elements:
    print(paragraph.text)

# End browser
driver.quit()
