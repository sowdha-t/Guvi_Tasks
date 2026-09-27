from PAT_TASK_14.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
class DashboardPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.profile_click_icon = (By.ID, "profile-click-icon")
        self.modal_popup = (By.XPATH, "//div[@class='mobile-app-promotion-main-div']")
        self.modal_popup_close_button = (By.XPATH, "//button[@aria-label='Close popup']")
        self.logout_link = (By.XPATH, "//div[@class ='user-avatar-menu' and text()='Log out']")

    def verify_logout_functionality(self):
        try:
            #Check if the modal is visible
            modal = self.check_visibility_of_element(self.modal_popup)
            print("Modal appeared! Proceeding to interact with it.")
            self.wait_and_click(self.modal_popup_close_button)
            self.wait_and_click(self.profile_click_icon)
            self.wait_and_click(self.logout_link)
        except TimeoutException:
            self.wait_and_click(self.profile_click_icon)
            self.wait_and_click(self.logout_link)