import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.positive
def test_login_url(driver,login_page):
    # assert
    print(f"Current URL:{driver.current_url}")
    # login_page.wait_for_page_load()
    login_page.wait_for_url_contains("sign-in")
    assert "sign-in" in driver.current_url

@pytest.mark.positive
@pytest.mark.skip
def test_username_field_enabled(driver,login_page):
    username_field = login_page.wait_for_visible(login_page.username)
    assert username_field.is_enabled()

@pytest.mark.positive
@pytest.mark.skip
def test_username_field_displayed(driver,login_page):
    username_field = login_page.wait_for_visible(login_page.username)
    assert username_field.is_displayed()

@pytest.mark.skip
@pytest.mark.positive
def test_password_field_enabled(driver,login_page):
    password_field = login_page.wait_for_visible(login_page.password)
    assert password_field.is_enabled()

@pytest.mark.skip
@pytest.mark.positive
def test_password_field_displayed(driver,login_page):
    password_field = login_page.wait_for_visible(login_page.password)
    assert password_field.is_displayed()


@pytest.mark.positive
def test_positive_login_flow(driver,login_page,username="sowdha.perumal@gmail.com", password="krishna#1"):
    #Enter the details
    login_page.enter_login_details(username, password)
    login_page.submit_login_page()
    # Step 1: Click the profile button
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Profile'])[1]"))
    )
    element.click()
    element.is_displayed()

@pytest.mark.negative
def test_negative_login_flow(driver,login_page,username = "WrongTeste@gmail.com", password = "Wrongpswd"):
    # Enter the details
    login_page.enter_login_details(username, password)
    login_page.submit_login_page()
    error_text = login_page.wait_to_get_text_attribute(login_page.error_pswd_msg)
    print(error_text)
    assert "Incorrect" in error_text








