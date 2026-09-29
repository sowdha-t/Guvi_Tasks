from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PopulationPage:
    def __init__(self,driver):
        self.population_xpath = (By.XPATH, "//div[contains(@class,'counter-ticker')]")
        self.driver = driver
        self.timeout = 10

    def get_population_element(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.population_xpath)
        )

    def wait_for_ajax_update(self, old_text):
        """Wait until AJAX updates the text (population changes)"""
        WebDriverWait(self.driver, self.timeout).until_not(
            EC.text_to_be_present_in_element(self.population_xpath, old_text)
        )
        return self.get_population_element().text
