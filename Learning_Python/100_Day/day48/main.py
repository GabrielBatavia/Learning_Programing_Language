from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep edge browser open after open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)


URL = "https://www.amazon.com/Overlord-Light-Novel-Kugane-Maruyama/dp/B0B3DB4W1N/ref=sr_1_4?crid=1Y0SM1NE2ZEXY&dib=eyJ2IjoiMSJ9.pkG-udsbgqyFhKnBZnimxSsznRqynQrFmzdcobgDk5tPPYQsamEgICq9vLrI-hSyHO8so0fqPapD7Sb0Zq2r8liNRPjes1hlce58L_NUqj-cWb3FtMyUZvx3MNUEN2VDcyE5ckURRXF9kBMTKY-_ZOg85vwTrb4sr6X5rLX_pHqlBKD_ZYPtau750WIr2fCaolD0gmK0R1i5u8SGZRICUC1VW42LzbFp5zUejizRxjo.E49UQ9IbSoNaJv6v-PqmK_sSssmmdCPUQ2MhEV-9WUI&dib_tag=se&keywords=overlord&qid=1716724883&sprefix=overlord%2Caps%2C308&sr=8-4"


driver = webdriver.Edge(options=edge_options)
driver.get(URL)


#price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
#print(f"The price is ${price_dollar}.{price_cents}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))


# End browser
driver.quit()