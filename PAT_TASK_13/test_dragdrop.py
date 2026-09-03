from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get('https://jqueryui.com/droppable/')
    #driver.maximize_window()
    iframe_element = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
    driver.switch_to.frame(iframe_element)
    yield driver
    driver.switch_to.default_content()
    driver.quit()

def test_drag_and_drop_positive(driver):
    # Locators
    drag_obj = driver.find_element(By.CSS_SELECTOR, "#draggable")
    drop_obj = driver.find_element(By.CSS_SELECTOR, "#droppable")
    drop_obj_text = drop_obj.find_element(By.XPATH, "//div[@id='droppable']//p").text
    print("Initial Drop Object Text:",drop_obj_text)
    action = ActionChains(driver)
    action.drag_and_drop(drag_obj, drop_obj).perform()
    after_drop_text = drop_obj.find_element(By.XPATH, "//div[@id='droppable']//p").text
    print("After dropping the Object:",after_drop_text)
    assert after_drop_text == "Dropped!"

def test_drag_and_drop_negative(driver):
    # Locators
    drag_obj = driver.find_element(By.CSS_SELECTOR, "#draggable")
    drop_obj = driver.find_element(By.CSS_SELECTOR, "#droppable")
    drop_obj_text = drop_obj.find_element(By.XPATH, "//div[@id='droppable']//p").text
    print("Initial Drop Object Text:", drop_obj_text)
    action = ActionChains(driver)
    action.drag_and_drop(drag_obj, drop_obj).perform()
    after_drop_text = drop_obj.find_element(By.XPATH, "//div[@id='droppable']//p").text
    print("After dropping the Object:", after_drop_text)
    assert after_drop_text != "Drop here"



