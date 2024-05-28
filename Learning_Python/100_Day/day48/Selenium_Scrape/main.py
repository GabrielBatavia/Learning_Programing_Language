from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep edge browser open after open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)


URL = "https://www.python.org/"


driver = webdriver.Edge(options=edge_options)
driver.get(URL)

# Challenge : Print the event dates from python.org
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for time in event_times:
    print(time.text)
    
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for name in event_names:
    print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_times[n].text,
    }
print(events)

# End browser
driver.quit()
