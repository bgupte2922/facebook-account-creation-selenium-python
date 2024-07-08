from selenium.webdriver.common.by import By
from Locators.locators import Locators
from selenium.webdriver.support.select import Select


class AccountCreationPage():

    def __init__(self, driver):
        self.driver = driver

        self.create_new_account_button_xpath = Locators.create_new_account_button_xpath
        self.firstName_textbox_xpath = Locators.firstName_textbox_xpath
        self.lastName_textbox_xpath = Locators.lastName_textbox_xpath
        self.email_textbox_xpath = Locators.email_textbox_xpath
        self.emailConfirmation_textbox_xpath = Locators.emailConfirmation_textbox_xpath
        self.password_textbox_xpath = Locators.password_textbox_xpath
        self.birthday_month_dropdown_xpath = Locators.birthday_month_dropdown_xpath
        self.birthday_day_dropdown_xpath = Locators.birthday_day_dropdown_xpath
        self.birthday_year_dropdown_xpath = Locators.birthday_year_dropdown_xpath
        self.gender_radiobutton_xpath = Locators.gender_radiobutton_xpath
        self.signUp_button_name = Locators.signUp_button_name
        self.error_message_id = Locators.error_message_id

        # def birthday_dayList_dropdown_click(self, dayList, day):
        #     dayList = self.driver.find_elements(By.XPATH, self.birthday_dayList_dropdown_xpath).text
        #     for day in dayList:
        #         if day == "27":
        #             self.driver.find_element(By.XPATH, self.birthday_dayList_dropdown_xpath).click()
        #
        # def birthday_yearList_dropdown_click(self, yearList, year):
        #     yearList = self.driver.find_elements(By.XPATH, self.birthday_yearList_dropdown_xpath).text
        #     for year in yearList:
        #         if year == "1991":
        #             self.driver.find_element(By.XPATH, self.birthday_yearList_dropdown_xpath).click()
        #
        # def genderList_radiobutton_click(self, genderList, gender):
        #     genderList = self.driver.find_elements(By.XPATH, self.genderList_radiobutton_xpath).get_attribute("value")
        #     for gender in genderList:
        #         if gender == "2":
        #             self.driver.find_element(By.XPATH, self.genderList_radiobutton_xpath).click()

    def invalid_email_message(self, message):
        message = self.driver.find_element(By.ID, self.error_message_id).text
        return message

    def create_new_account_button_click(self):
        self.driver.find_element(By.XPATH, self.create_new_account_button_xpath).click()

    def firstName_textbox_sendKeys(self, firstName):
        self.driver.find_element(By.XPATH, self.firstName_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstName_textbox_xpath).send_keys(firstName)

    def lastName_textbox_sendKeys(self, lastName):
        self.driver.find_element(By.XPATH, self.lastName_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.lastName_textbox_xpath).send_keys(lastName)

    def email_textbox_sendKeys(self, email):
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(email)

    def emailConfirmation_textbox_sendKeys(self, emailConfirmation):
        self.driver.find_element(By.XPATH, self.emailConfirmation_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.emailConfirmation_textbox_xpath).send_keys(emailConfirmation)

    def password_textbox_sendKeys(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def birthday_month_dropdown_click(self):
        month = Select(self.driver.find_element(By.XPATH, self.birthday_month_dropdown_xpath))
        month.select_by_visible_text("Nov")

    def birthday_day_dropdown_click(self):
        day = Select(self.driver.find_element(By.XPATH, self.birthday_day_dropdown_xpath))
        day.select_by_visible_text("27")

    def birthday_year_dropdown_click(self):
        year = Select(self.driver.find_element(By.XPATH, self.birthday_year_dropdown_xpath))
        year.select_by_visible_text("1992")

    def gender_radiobutton_click(self):
        self.driver.find_element(By.XPATH, self.gender_radiobutton_xpath).click()

    def signUp_button_click(self):
        self.driver.find_element(By.NAME, self.signUp_button_name).click()

    def invalid_email_message(self):
        message = self.driver.find_element(By.ID, self.error_message_id).text
        return message

