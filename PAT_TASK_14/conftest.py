import pytest
from selenium import webdriver

from PAT_TASK_14.pages.login_page import LoginPage
from PAT_TASK_14.utils.config_reader import ConfigReader

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    config_details = ConfigReader.get_config()
    url = config_details["base_url"]
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_user(driver):
    # valid username and password
    username = 'valid_email@gmail.com'
    password = 'valid_password'
    login_page = LoginPage(driver)
    login_page.enter_login_details(username, password)
    login_page.submit_login_page()
    return driver


