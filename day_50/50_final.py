from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

my_email = 'myemail'
my_password = 'my_password'

driver_path = "/Users/chaeyunsim/Documents/developments/chromedriver"
chrome_options = webdriver.ChromeOptions()
webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

webdriver.get(url="https://tinder.com")
time.sleep(6)

login = webdriver.find_element(By.XPATH, '//*[@id="q-1470728188"]/div/div[1]/div/main/div['
                                         '1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

facebook = webdriver.find_element(By.ID, 'Tinder')
facebook.click()

time.sleep(5)

webdriver.switch_to.window(webdriver.window_handles[1])

fb_id = webdriver.find_element(By.XPATH, '//*[@id="email"]')
fb_id.send_keys(my_email)
fb_pw = webdriver.find_element(By.XPATH, '//*[@id="pass"]')
fb_pw.send_keys(my_password)
fb_pw.send_keys(Keys.ENTER)

time.sleep(3)

# webdriver.switch_to.window(webdriver.window_handles[0])
# print(webdriver.title)

time.sleep(120)
