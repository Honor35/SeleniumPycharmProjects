from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from CommandLine.POMDemo.LoginPage import Loginpage
from CommandLine.POMDemo.HomePage import HomePage

class LoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome(executable_path="C:\\Users\\computer\\PycharmProjects\\SeleniumTutorialPractice\\Driver\\chromedriver.exe")
       cls.driver.implicitly_wait(10)

    def test_login(self):
       self.driver.get("https://opensource-demo.orangehrmlive.com")
       self.driver.maximize_window()

       login = Loginpage(self.driver)
       login.enter_username('Admin')
       time.sleep(2)
       login.enter_password('admin123')
       time.sleep(2)
       login.login_button()
       time.sleep(2)

       logout = HomePage(self.driver)
       logout.welcome_button_id
       time.sleep(2)
       logout.logout_button_text
       time.sleep(2)
       # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
       # time.sleep(2)
       # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
       # time.sleep(2)
       # self.driver.find_element_by_id("btnLogin").click()
       # time.sleep(3)
       # self.driver.find_element_by_id("welcome").click()
       # time.sleep(2)
       # self.driver.find_element_by_link_text("Logout").click()
       # time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed...")


if __name__ == "__main__":
    unittest.main()