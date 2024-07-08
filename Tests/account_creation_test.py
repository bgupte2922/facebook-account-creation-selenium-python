import time

from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from Pages.account_creation_page import AccountCreationPage
import HtmlTestRunner


class AccountCreationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_invalid_account_creation(self):
        driver = self.driver

        baseUrl = "https://www.facebook.com/"
        driver.get(baseUrl)

        acp = AccountCreationPage(driver)
        time.sleep(2)
        acp.create_new_account_button_click()
        time.sleep(2)
        acp.firstName_textbox_sendKeys("Firstname")
        time.sleep(2)
        acp.lastName_textbox_sendKeys("Lastname")
        time.sleep(2)
        acp.email_textbox_sendKeys("firstname.lastname@email.com")
        time.sleep(2)
        acp.emailConfirmation_textbox_sendKeys("firstname.lastname@email.com")
        time.sleep(2)
        acp.password_textbox_sendKeys("test123")
        time.sleep(2)
        acp.birthday_month_dropdown_click()
        time.sleep(2)
        acp.birthday_day_dropdown_click()
        time.sleep(2)
        acp.birthday_year_dropdown_click()
        time.sleep(2)
        acp.gender_radiobutton_click()
        time.sleep(2)
        acp.emailConfirmation_textbox_sendKeys("lastname.firstname@email.com")
        time.sleep(2)
        acp.signUp_button_click()
        time.sleep(2)
        message = acp.invalid_email_message()
        print(message)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/Bhagyashree/workspace_python/FacebookAccountCreation/Reports'))

# To run on command prompt, run as administrator
# Navigate to:
# C:\Users\Bhagyashree\workspace_python\FacebookAccountCreation
# Command:
# python -m Tests.account_creation_test
