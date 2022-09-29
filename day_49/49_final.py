from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import threading

driver_path = "/Users/chaeyunsim/Documents/developments/chromedriver"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url="https://www.linkedin.com/")

email = driver.find_element(By.ID, "session_key")
pw = driver.find_element(By.ID, "session_password")
email.send_keys("cysh3426@gmail.com")
pw.send_keys("3426asdf")
pw.send_keys(Keys.ENTER)

time.sleep(3)

# driver.find_element(By.CLASS_NAME, "follow.artdeco-button.artdeco-button--secondary.artdeco-button--2").click()

driver.find_element(By.CLASS_NAME, "feed-shared-feed-discovery-entity__text-container.flex-grow-1").click()

time.sleep(5)


driver.find_element(By.CLASS_NAME, "follow.org-company-follow-button.org-top-card-primary-actions__action"
                                   ".artdeco-button.artdeco-button--primary").click()

time.sleep(120)


