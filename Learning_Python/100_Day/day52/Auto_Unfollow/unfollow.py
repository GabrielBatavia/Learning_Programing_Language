from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

pop_up_window = '//button[@type="button" and contains(@class, "_abl-")]'

class Unfollow:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
        
    def scroll(self, popup_window):
            js_command = """
                        popup_window = document.querySelector('.isgrP');
                        popup_window.scrollTo(0, popup_window.scrollHeight);
                        var curr_page_len = popup_window.scrollHeight;
                        return curr_page_len;
                        """
            curr_page_len = self.driver.execute_script(js_command)
            scrolling = True
            time.sleep(1)
            while scrolling:
                prev_page_len = curr_page_len
                curr_page_len = self.driver.execute_script(js_command)
                if prev_page_len == curr_page_len:
                    scrolling = False
                time.sleep(1)

    def login(self, email, password):
        self.driver.get("https://www.instagram.com/")
    
        time.sleep(5)
        email_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(email)
        
        time.sleep(2)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        
        time.sleep(3)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()        
        
        time.sleep(5)
        profile_picture = self.driver.find_element(By.XPATH, "//img[@alt=\"batavia_sensei's profile picture\"]")
        profile_picture.click()
        
        time.sleep(5)
        click_following = self.driver.find_element(By.XPATH, "//a[@href='/batavia_sensei/following/?next=%2F']")
        click_following.click()
        
        time.sleep(10)
        for i in range(100):
            time.sleep(10)
            for _ in range(12):
                click_unfollowing = self.driver.find_element(By.XPATH, "//button[contains(., 'Following')]")
                click_unfollowing.click()
                time.sleep(2)
                confirm_button = self.driver.find_element(By.XPATH, "//button[contains(@class, '_a9-- _ap36 _a9-_')]")
                confirm_button.click()
                time.sleep(2)
            
            self.scroll(popup_window=pop_up_window)
        
        
        
        time.sleep(100)
        
        
        

