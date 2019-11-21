from selenium import webdriver
import time
import pytest

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/computer/PycharmProjects/PythonAutomationFrameWork1/drivers/chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test1 Completed....!!!")

def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    print(driver.title)
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    yield
    driver.close()
    driver.quit()
    print("Test2 Completed....!!!")

def test_logout():
    driver.find_element_by_id("welcome").click()
    time.sleep(2)
    driver.find_element_by_partial_link_text("Logout").click()
    driver.close()
    driver.quit()
    print("Test3 Completed....!!!")