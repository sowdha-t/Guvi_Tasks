from selenium.webdriver.common.by import By
from base_page import BasePage


class TestLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.guvi.in/"
        self.login_button = (By.XPATH,"(//button[@id='login-btn' and text()='Login'])[1]")
        self.username = (By.ID, "email")
        self.password = (By.ID, "password")
        self.submit_button = (By.ID,"login-btn")
        self.error_email_msg = (By.XPATH,"//div[@id='emailgroup']//div[contains(@class,'invalid-feedback') and contains(normalize-space(),'Incorrect Email or Password')]")
        self.error_pswd_msg = (By.CSS_SELECTOR,"div[id='passwordGroup'] div[class='invalid-feedback']")
        self.error_invalid_user_pswd = (By.XPATH,"//div[@id='emailgroup']//div[contains(@class,'invalid-feedback') and contains(normalize-space(),'Incorrect Email or Password')]")
        self.general_error_msg = (By.XPATH, "//div[@class='invalid-feedback'][normalize-space()='']")
        self.profile_image = (By.XPATH,"//img[@alt='Profile'])[1]")

    def get_guvi_page(self):
        self.driver.get(self.url)

    def click_login_link(self):
        self.wait_and_click(self.login_button)

    def enter_login_details(self,user,pswd):
        self.wait_and_type(self.username,user)
        self.wait_and_type(self.password,pswd)


    def submit_login_page(self):
        self.wait_and_click(self.submit_button)







