from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver_path = "/Users/chaeyunsim/Documents/developments/chromedriver"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url="https://www.amazon.com/dp/B00FLYWNYQ/ref=sr_1_1_sspa?keywords=instant+pot&qid=1664374931&qu"
               "=eyJxc2MiOiI0LjU0IiwicXNhIjoiNC4wOCIsInFzcCI6IjMuNjIifQ%3D%3D&sr=8-1-spons&psc=1&spLa"
               "=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNUJSUElYTVE4RDA4JmVuY3J5cHRlZElkPUEwNTQ5NTIwSFk2Vk1IR0NQTTlPJmVuY3J5cHRlZEFkSWQ9QTA2MzQ0MDEzSEUxWldRM0NIUjI5JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)

driver.quit()
