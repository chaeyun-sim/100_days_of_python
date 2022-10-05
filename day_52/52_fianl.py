from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "/Users/chaeyunsim/Documents/developments/chromedriver"
PROJECT_ACCOUNT = "hi_sseulgi"
USERNAME = "your account name"
PASSWORD = 'your password'


class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                       options=webdriver.ChromeOptions())
        self.follow_number = 18
        self.cnt = 0
        self.pop_up_window = None

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
        self.driver.get(url=f'https://www.instagram.com/{PROJECT_ACCOUNT}')

        time.sleep(15)

        lst = self.driver.find_element(By.XPATH, '//a[contains(@href, "/following")]')
        lst.click()

        time.sleep(5)

    def follow(self):
        self.pop_up_window = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        time.sleep(2)
        for num in range(1, self.follow_number):
            time.sleep(1)
            follow_button = self.driver.find_element(By.XPATH, f"//div[@class='_aano']/div/div/div[{num}]/div[3]/button/div")
            print(f"{num}: {follow_button.text}")

            if follow_button.text == "팔로우":
                try:
                    follow_button.click()
                    self.cnt += 1
                    if self.cnt % 5 == 0:
                        while True:
                            self.driver.execute_script(
                                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                self.pop_up_window)
                            time.sleep(3)
                            break
                except NoSuchElementException:
                    print("Follow End!")
                    quit()
            else:
                pass


instagram = InstaFollower()
instagram.login()
instagram.find_followers()
instagram.follow()
