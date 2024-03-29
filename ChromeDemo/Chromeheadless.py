from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
option.add_argument("--headless")

driver = webdriver.Chrome(options=option,executable_path="../Driver/chromedriver.exe")
time.sleep(2)

driver.get("https://www.google.com")
print(driver.title)
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Automation step by step")
time.sleep(3)
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(3)
print(driver.title)

driver.close()
print("Test Completed")