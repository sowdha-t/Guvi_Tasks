from selenium.webdriver.common.by import By
from PAT_TASK_15.pages.base_page import BasePage
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #locators
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

        self.email_validation_error_msg = (By.XPATH, "//input[@name='username']/../following-sibling::span")
        self.password_validation_error_msg = (By.XPATH, "//input[@name='password']/../following-sibling::span")

        self.authentication_error_msg = (By.CSS_SELECTOR, "p.oxd-alert-content-text")

    def enter_login_details(self,username,password):
        self.wait_and_type(self.username,username)
        self.wait_and_type(self.password,password)

    def submit_login_page(self):
        self.wait_and_click(self.login_button)

    def get_email_validation_error_msg(self):
        return self.get_text(self.email_validation_error_msg)

    def get_password_validation_error_msg(self):
        return self.get_text(self.password_validation_error_msg)

    def get_authentication_error_msg(self):
        return self.get_text(self.authentication_error_msg)
