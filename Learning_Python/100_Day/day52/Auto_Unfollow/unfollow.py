from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Unfollow:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def login(self, email, password):
        self.driver.get("https://www.instagram.com/")
    
        time.sleep(10)
        email_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(email)
        
        time.sleep(2)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        
        time.sleep(3)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()        
        
        time.sleep(10)
        profile_picture = self.driver.find_element(By.XPATH, "//img[@alt=\"batavia_sensei's profile picture\"]")
        profile_picture.click()
        
        time.sleep(5)
        click_following = self.driver.find_element(By.XPATH, "//a[@href='/batavia_sensei/following/?next=%2F']")
        click_following.click()
        
        time.sleep(100)
        for _ in range(100):
            click_unfollowing = self.driver.find_element(By.CLASS_NAME, '_ap3a')
            click_unfollowing.click()
        
        
        
        time.sleep(100)
        
        
        

