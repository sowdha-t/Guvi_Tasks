import pytest
from datetime import datetime
from selenium import webdriver
from PAT_TASK_15.utils.config_reader import ConfigReader
from PAT_TASK_15.utils.excel_utils import ExcelUtils

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    config_details = ConfigReader.get_config()
    url = config_details["base_url"]
    driver.get(url)
    yield driver
    driver.quit()

#Pytest hook implementation for writing the result back to the excel

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        if "row_index" in item.callspec.params:
            row_index = item.callspec.params["row_index"]

        status = "Pass" if report.passed else "Fail"

        #Getting Current Date and Time
        now = datetime.now()
        current_date = now.strftime("%d-%m-%y")
        current_time = now.strftime("%H:%M:%S")

        #Updating the data in excel file
        ExcelUtils.update_test_results(row_index,status,current_date,current_time)



