from PAT_TASK_14.pages.base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    #Locators
    def __init__(self,driver):
        super().__init__(driver)
        self.email_field = (By.CSS_SELECTOR,"input[id=':r1:']")
        self.password_field = (By.CSS_SELECTOR, "input[type='password']")
        self.sign_in_button = (By.CSS_SELECTOR, "button[type='submit']")

        self.email_validation_error_msg = (By.CSS_SELECTOR, "p[id=':r1:-helper-text']")
        self.password_validation_error_msg = (By.CSS_SELECTOR, "p[id=':r2:-helper-text']")


    def enter_login_details(self,username,password):
        self.wait_and_type(self.email_field, username)
        self.wait_and_type(self.password_field,password)

    def enter_login_details_blank_validation(self,username,password):
        if username == '' and password == '' :
            self.wait_and_clear(self.email_field)
            self.wait_and_clear(self.password_field)
        elif password != '' and username == '' :
            self.wait_and_clear(self.email_field)
            self.wait_and_type(self.password_field,password)
        elif username != '' and password == '' :
            self.wait_and_type(self.email_field, username)
            self.wait_and_clear(self.password_field)

    def submit_login_page(self):
        self.wait_and_click(self.sign_in_button)

    def get_email_validation_error_msg(self):
        return self.get_text(self.email_validation_error_msg)

    def get_password_validation_error_msg(self):
        return self.get_text(self.password_validation_error_msg)











