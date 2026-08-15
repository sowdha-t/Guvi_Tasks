from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import TestLoginPage
import time

def test_positive_login_flow(driver,username="validuser@gmail.com", password="validpswd"):
    login_page = TestLoginPage(driver)

    #Visiting to Guvi Page
    login_page.get_guvi_page()

    #Click the login link
    login_page.click_login_link()
    #assert
    print(f"Current URL:{driver.current_url}")
    #login_page.wait_for_page_load()
    login_page.wait_for_url_contains("sign-in")
    assert "sign-in" in driver.current_url

    #validating the input field
    username_field = login_page.wait_for_visible(login_page.username)
    password_field = login_page.wait_for_visible(login_page.password)
    assert username_field.is_enabled()
    assert password_field.is_enabled()
    assert username_field.is_displayed()
    assert password_field.is_displayed()

    #Enter the details
    login_page.enter_login_details(username, password)
    login_page.submit_login_page()
    print(driver.current_url)

    # Step 1: Click the profile button
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Profile'])[1]"))
    )
    element.click()
    element.is_displayed()

    #home_page_profile_element = login_page.wait_for_visible(login_page.dashboard_image)
    #assert home_page_profile_element.is_displayed()


def test_negative_login_flow(driver,username = "WrongTeste@gmail.com", password = "Wrongpswd"):
    login_page = TestLoginPage(driver)

    # Visiting to Guvi Page
    login_page.get_guvi_page()

    # Click the login link
    login_page.click_login_link()

    # Enter the details
    login_page.enter_login_details(username, password)
    login_page.submit_login_page()
    error_text = login_page.wait_to_get_text_attribute(login_page.error_pswd_msg)
    print(error_text)
    assert "Incorrect" in error_text








