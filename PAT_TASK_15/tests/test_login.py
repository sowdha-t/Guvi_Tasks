import time
import pytest
from PAT_TASK_15.pages.login_page import LoginPage
from PAT_TASK_15.utils.excel_utils import ExcelUtils

#Get data from the excel
data = ExcelUtils.read_test_data()

#test_case_ids = [data["row_index"] for test_id in data]

@pytest.mark.parametrize("row_index,test_id,username,password",data)
def test_login_functionality(driver,row_index,test_id,username,password):
    login_page = LoginPage(driver)
    if  "successful login" in test_id:
        login_page.enter_login_details(username,password)
        login_page.submit_login_page()
        login_page.wait_for_url_contains("dashboard")
        assert "dashboard" in driver.current_url
    elif "invalid login" in test_id:
        login_page.enter_login_details(username,password)
        login_page.submit_login_page()
        error_text = login_page.get_authentication_error_msg()
        assert "Invalid credentials" in error_text
    elif "Blank Password" in test_id:
        login_page.enter_login_details(username,"")
        login_page.submit_login_page()
        error_text = login_page.get_password_validation_error_msg()
        assert "Required" in error_text
    elif "Blank username" in test_id:
        login_page.enter_login_details("", password)
        login_page.submit_login_page()
        error_text = login_page.get_email_validation_error_msg()
        assert "Required" in error_text
    elif "Both blank" in test_id:
        login_page.enter_login_details("", "")
        login_page.submit_login_page()
        error_email_text = login_page.get_email_validation_error_msg()
        error_password_text = login_page.get_password_validation_error_msg()
        assert "Required" in error_email_text and error_password_text







