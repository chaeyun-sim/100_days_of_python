import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/chaeyunsim/Documents/developments/chromedriver"
TWITTER_EMAIL = "dummy.simune@gmail.com"
TWITTER_PASSWORD = "codbsajtwoddl123"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.test_start_button = None
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net")
        test_start_button = self.driver.find_element(By.CLASS_NAME, "js-start-test.test-mode-multi")
        test_start_button.click()
        time.sleep(50)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div['
                                                           '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                           '1]/div[1]/div/div[2]/span').text
        print('down:', self.down)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div['
                                                         '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                         '2]/div/div[2]/span').text
        print('up:', self.up)

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com")
        login = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div['
                                                   '1]/div/div[3]/div[5]/a')
        login.click()
        < a
        href = "/login"
        role = "link"

        class ="css-4rbku5 css-18t94o4 css-1dbjc4n r-1niwhzg r-sdzlij r-1phboty r-rs99b7 r-1loqt21 r-a9p05 r-eu3ka r-5oul0u r-17w48nw r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-1ipicw7" data-testid="loginButton" style="border-color: rgb(207, 217, 222);" > < div dir="auto" class ="css-901oao r-1awozwy r-1cvl2hr r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0"
        # self.driver.switch_to.window(self.driver.window_handles[1])
        # email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
        #                                            '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
        #                                            '2]/div/input')
        # email.click()
        # email.send_keys(TWITTER_EMAIL)
        # email.send_keys(Keys.ENTER)
        # password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
        #                                               '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
        #                                               '3]/div/label/div/div[2]/div[1]/input')
        # password.click()
        # password.send_keys(TWITTER_PASSWORD)
        # password.send_keys(Keys.ENTER)
        #
        # time.sleep(200)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
