from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/chaeyunsim/Documents/developments/chromedriver"
TWITTER_EMAIL = "twitter_email"
TWITTER_PASSWORD = "twitter_password"
TWITTER_NICKNAME = 'twitter_name'


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
        print("Wait . . . .")
        time.sleep(50)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div['
                                                       '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                       '1]/div[1]/div/div[2]/span').text
        print('down:', self.down)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div['
                                                     '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                     '2]/div/div[2]/span').text
        print('up:', self.up)
        time.sleep(5)

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/i/flow/login")
        time.sleep(5)
        email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/div/div/div/div/div/div/div['
                                                   '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                   '2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(1)

        print(self.driver.window_handles)

        confirm_nickname = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                              '2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                              '2]/label/div/div[2]/div/input')
        confirm_nickname.send_keys(TWITTER_NICKNAME)
        confirm_nickname.send_keys(Keys.ENTER)

        time.sleep(1)

        print(self.driver.window_handles)

        password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/div/div/div/div/div/div/div['
                                                      '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                      '3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(3)

        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                         '2]/header/div/div/div/div[1]/div[3]/a')
        post_button.click()

        text = self.driver.find_element(by=By.CLASS_NAME, value="public-DraftEditor-content")
        TEXT_TO_POST = f"My internet speed is {self.down} down / {self.up} up! \n- written by automated twitter bot"
        text.send_keys(TEXT_TO_POST)
        twit_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div['
                                                         '2]/div[3]/div/div/div[2]/div[4]')
        twit_button.click()

        time.sleep(5)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
