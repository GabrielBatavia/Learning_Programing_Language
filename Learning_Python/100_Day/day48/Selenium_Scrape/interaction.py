from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Edge browser open after opening
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

URL = "https://id.wikipedia.org/wiki/Joko_Widodo"

driver = webdriver.Edge(options=edge_options)
driver.get(URL)

# Find the element containing the name
figure_name_element = driver.find_element(By.CLASS_NAME, "mw-page-title-main")
figure_name = figure_name_element.text

# Find all paragraph elements
paragraph_elements = driver.find_elements(By.TAG_NAME, "p")

# Write the figure name and paragraphs to a file
with open("./Selenium_Scrape/joko_widodo.txt", "w", encoding="utf-8") as file:
    file.write(figure_name + "\n\n")
    for paragraph in paragraph_elements:
        file.write(paragraph.text + "\n\n")

# End browser
driver.quit()
