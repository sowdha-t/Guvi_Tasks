import pytest
import time
from PAT_TASK_14.pages.login_page import LoginPage

@pytest.mark.positive
def test_successful_login(driver):
    #valid username and password
    username = 'valid_email@gmail.com'
    password = 'valid_password'
    login_page = LoginPage(driver)
    login_page.enter_login_details(username,password)
    login_page.submit_login_page()
    login_page.wait_for_url_contains("dashboard")
    print(driver.current_url)
    curr_url = driver.current_url
    assert "dashboard" in curr_url

@pytest.mark.positive
def test_unsuccessful_login(driver):
    #Authentication level validation
    username = 'valid_email@gmail.com'
    password = 'invalid_password#1'
    login_page = LoginPage(driver)
    login_page.enter_login_details(username,password)
    login_page.submit_login_page()
    error_msg = login_page.get_email_validation_error_msg()
    print(error_msg)
    assert "Invalid" in error_msg

@pytest.mark.negative
def test_username_field_validation(driver):
    #username field level alidation
    username = '1235add'
    password = 'abc#1'
    login_page = LoginPage(driver)
    login_page.enter_login_details(username, password)
    login_page.submit_login_page()
    error_msg = login_page.get_email_validation_error_msg()
    print(error_msg)
    assert "Incorrect email" in error_msg

@pytest.mark.negative
def test_password_field_validation(driver):
    #password field level validation
    username = 'valid_email@gmail.com'
    password = ''
    login_page = LoginPage(driver)
    login_page.enter_login_details(username, password)
    login_page.submit_login_page()
    error_msg = login_page.get_password_validation_error_msg()
    print(error_msg)
    assert "Password required!" in error_msg

@pytest.mark.negative
def test_blank_email_field_validation(driver):
    #Both fields are empty
    username = ''
    password = ''
    login_page = LoginPage(driver)
    login_page.enter_login_details_blank_validation(username, password)
    login_page.submit_login_page()
    error_msg = login_page.get_password_validation_error_msg()
    assert "Email and password required!" in error_msg

    #Blank Email Validation
    password = 'invalid_password'
    login_page.enter_login_details_blank_validation(username, password)
    login_page.submit_login_page()
    error_msg = login_page.get_email_validation_error_msg()
    assert "Email required!" in error_msg


def test_blank_password_field_validation(driver):
    #Blank Password Validation
    username = 'valid_email@gmail.com'
    password = ''
    login_page = LoginPage(driver)
    login_page.enter_login_details_blank_validation(username, password)
    login_page.submit_login_page()
    error_msg = login_page.get_password_validation_error_msg()
    assert "Password required!" in error_msg





