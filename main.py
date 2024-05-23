from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# PATH = "C:\chromedriver.exe"
service = Service(executable_path="chromedriver.exe")
# service = Service(executable_path="PATH")
# driver = webdriver.Chrome(PATH)

driver = webdriver.Chrome(service=service)  # Pass the 'service' object you created

driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("hosanna official" + Keys.ENTER)
search = driver.find_elements_by_id

time.sleep(10)
print(driver.title)
driver.quit()
