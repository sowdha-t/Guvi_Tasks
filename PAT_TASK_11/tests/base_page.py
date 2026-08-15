from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver,timeout=10):
        self.driver =driver
        self.timeout = timeout

    def wait_and_click(self,locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def wait_and_type(self,locator,text):
        WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_for_visible(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_to_get_text_attribute(self,locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text.strip()

    def wait_for_page_load(self):
        """Wait until the page is fully loaded (document.readyState == complete)"""
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def wait_for_url_contains(self, text):
        """Wait until the URL contains the given text"""
        WebDriverWait(self.driver, self.timeout).until(
            EC.url_contains(text)
        )
        return self.driver.current_url

