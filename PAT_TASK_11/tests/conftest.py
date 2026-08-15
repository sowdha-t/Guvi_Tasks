import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument("--incognito")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "excludeSwitches" : ["enable-automation"],
        "useAutomationExtension" :False

    }
    options.add_experimental_option("prefs", prefs)

    # Anti-bot detection configs
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Network and stability fixes for ERR_CONNECTION_TIMED_OUT
    #options.add_argument("--no-sandbox")
    #options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("--no-proxy-server")  # Forces bypass of system proxy bottlenecks

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()
