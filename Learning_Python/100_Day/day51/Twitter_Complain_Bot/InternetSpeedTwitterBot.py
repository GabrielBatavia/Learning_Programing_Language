import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
X_EMAIL = os.getenv('EMAIL')
X_PASSWORD = os.getenv('PASSWORD')


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(10)
        accept_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_button.click()

        time.sleep(3)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text


    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")

        time.sleep(10)
        email_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        email_input.send_keys(X_EMAIL)

        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_button.click()
        
        time.sleep(5)
        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(X_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        time.sleep(20)
        tweet_compose = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div')
        tweet_compose.click()
        time.sleep(3)
        
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        print(tweet)
        tweet_compose.send_keys(Keys.ENTER)
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        tweet_button.click()

        time.sleep(2)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()