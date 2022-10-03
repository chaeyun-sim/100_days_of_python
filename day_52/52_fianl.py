from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "/Users/chaeyunsim/Documents/developments/chromedriver"
PROJECT_ACCOUNT = "blackpinkofficial"
USERNAME = "account_for__xx"
PASSWORD = '4908tlacos'


class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                       options=webdriver.ChromeOptions())

    def login(self):
        self.driver.get(url='https://www.instagram.com/accounts/login/')
        time.sleep(2)

        login_id = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_id.send_keys(USERNAME)
        login_pw = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_pw.send_keys(PASSWORD)
        login_pw.send_keys(Keys.ENTER)

        time.sleep(5)

    def find_followers(self):
        self.driver.get(url='https://www.instagram.com/hi_sseulgi/')
        time.sleep(15)

        lst = self.driver.find_element(By.XPATH, '//a[contains(@href, "/following")]')
        lst.click()

        time.sleep(5)

        # self.driver.getWindowHandle()
        pop_up_window = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_8W"]/div/div/div/div[2]/div/div/div['
                                                           '1]/div/div[2]/div/div/div/div/div[2]/div/div/div['
                                                           '3]/div/div')
        while True:
            pop_up_window.click()
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       pop_up_window)
            time.sleep(1)

    def follow(self):
        pass


instagram = InstaFollower()
instagram.login()
instagram.find_followers()
instagram.follow()
