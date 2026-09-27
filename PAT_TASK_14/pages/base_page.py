from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PAT_TASK_14.utils.config_reader import ConfigReader

class BasePage:
    def __init__(self, driver):
        config_details = ConfigReader.get_config()
        self.driver = driver
        self.timeout = config_details["time_out"]
        self.wait = WebDriverWait(driver, self.timeout)

    def wait_and_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_and_type(self,locator,text):
        element  = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_and_clear(self,locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()

    def wait_for_url_contains(self,text):
        self.wait.until(EC.url_contains(text))

    def get_text(self, locator):
        element =  self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def check_visibility_of_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

