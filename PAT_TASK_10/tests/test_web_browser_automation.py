from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SauceDemoTest:
    def __init__(self, url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def save_page_source(self, filename="Webpage_task_10.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)

    def quit(self):
        self.driver.quit()




# ------------------ Pytest Test Cases ------------------

def test_saucedemo_positive_negative():
    test_data_url ="https://saucedemo.com/"
    testdata_username ="standard_user"
    test_data_password = "secret_sauce"
    browser = SauceDemoTest(test_data_url)

    #Test Title in login page
    assert browser.get_title() == "Swag Labs"  # Positive case
    assert browser.get_title() != "Wrong Title"  # Negative case
    print(f"Browser title: {browser.get_title()}")
    print(f"Browser current url: {browser.get_url()}")
    # Perform login
    browser.login(testdata_username, test_data_password)

    # Fetch details
    title = browser.get_title()
    url = browser.get_url()
    browser.save_page_source()
    print(f"Browser title: {browser.get_title()}, current url: {url}")

    #After successful login, Check for url and title
    assert "saucedemo.com" in url  # Positive case
    assert "google.com" not in url  # Negative case

    # Positive assertions
    assert title == "Swag Labs"
    assert "saucedemo.com" in url
    assert "inventory.html" in url

    # Negative assertions
    assert title != "Wrong Title"
    assert "google.com"  not in url
    assert "login.html" not in url

    # Close browser
    browser.quit()









    


