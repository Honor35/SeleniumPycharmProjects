from selenium import webdriver
import unittest
import time
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import HtmlTestRunner
from SampleProject_Two.TestPage.LoginPage_Test import Loginpage
from SampleProject_Two.TestPage.HomePage_Test import Homepage
from SampleProject_Two.Locators.Locator_Demo import locate

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\computer\\PycharmProjects\\SeleniumTutorialPractice\\Driver\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_validate(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")

        log = Loginpage(driver)
        log.uname("Admin")
        log.upass("admin123")
        log.logbutton()

        out = Homepage(driver)
        out.welcome_but()
        out.logout_but()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed......")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C://Users//computer//PycharmProjects//SeleniumTutorialPractice//SampleProject_Two//Report"))