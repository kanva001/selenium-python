from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)  # Pass the 'service' object you created

driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("hosanna official" + Keys.ENTER)

time.sleep(10)

driver.quit()

print("This is python-selenium set up")
