from selenium import webdriver
from PAT_TASK_16.pages.population_page import PopulationPage

def test_population_live():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        world_population_url = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"
        driver.get(world_population_url)
        page = PopulationPage(driver)
        current_value = page.get_population_element().text
        print(f"Current World Population: {current_value}")
        #record_property("Population",current_value)

        while True:
            # Wait until AJAX updates the counter
            new_value = page.wait_for_ajax_update(current_value)
            print(f"Updated World Population: {new_value}")
            #record_property("Population Update", new_value)
            current_value = new_value
    except KeyboardInterrupt:
        print("Stopped by user (Ctrl+C).")
        assert True
    finally:
        driver.quit()


