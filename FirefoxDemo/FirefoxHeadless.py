from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

Option = webdriver.FirefoxOptions()
Option.add_argument("--headless")

path = "../Driver/geckodriver.exe"
driver = webdriver.Firefox(options=Option,executable_path=path)

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