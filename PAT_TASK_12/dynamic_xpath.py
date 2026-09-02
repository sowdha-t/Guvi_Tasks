from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.guvi.in/")
driver.maximize_window()


dynamic_xpath_element = {"Live Classes" :"(//div[@id='solutions']//p)[1]",
                          "Courses" :"(//div[@id='solutions']//p)[2]",
                          "Practice" : "(//div[@id='solutions']//p)[3]",
                          "Resources" : "(//div[@id='solutions']//p)[4]",
                          "Our Products" : "(//div[@id='solutions']//p)[5]",
                         "Login" : "(//button[@id='login-btn'])[1]",
                         "Sign Up" :"(//button[text()='Sign up'])[1]"
                          }

def dynamic_xpaths(driver,element_name, dynamic_xpath):
    element = driver.find_element(By.XPATH, dynamic_xpath)
    print(f"{element_name} Text :{element.text}")

    parent_element = driver.find_element(By.XPATH, f"{dynamic_xpath}/parent::div")
    print("Parent Element Text", parent_element.text)
    print("Parent element Tag name",parent_element.tag_name)
    print("Parent Element Class:", parent_element.get_attribute("class"))

    # Checking for any child element for the course_element
    child_elements = parent_element.find_elements(By.XPATH, "./child::*")
    print("No. of. child elements", len(child_elements))
    print("Child elements:", [child.tag_name for child in child_elements])

    # Following Sibling for the given Element
    try:
        siblings = driver.find_element(By.XPATH, f"{dynamic_xpath}/following-sibling::*")
        print("Siblings for the element found")
        print("Sibling Class Attribute Value:", siblings.get_attribute("class"))
        print(f"Sibling Tag name:{siblings.tag_name}")
    except NoSuchElementException:
        print(f"No sibling found for this element...{element_name}")

    #Finding the parent element of the given element which has the href attribute
    try:
        href_parent = driver.find_element(By.XPATH, f"{dynamic_xpath}/ancestor::*[@href][1]")
        print(f"Parent/Ancestor with href found!")
        print("Href Link Value:", href_parent.get_attribute("href"))
        print("Href Parent Tag Name:", href_parent.tag_name)
    except NoSuchElementException:
        print(f"No parent or ancestor element with an 'href' attribute exists for {element_name}.")

    # Ancestors
    ancestors = driver.find_elements(By.XPATH, f"{dynamic_xpath}/ancestor::div")
    print("Ancestor count:", len(ancestors))

    # Following siblings
    following = driver.find_elements(By.XPATH, f"{dynamic_xpath}/ancestor::div/following-sibling::div")
    print("Following siblings:", [f.text for f in following])

    # Preceding siblings
    preceding = driver.find_elements(By.XPATH, f"{dynamic_xpath}/ancestor::div/preceding-sibling::div")
    print("Preceding siblings:", [p.text for p in preceding])

#For each element given in the task, we are finding its parent, child, ancestors, following-siblings and preceding siblings
for element, xpath in dynamic_xpath_element.items():
    print(f"Element Name:{element} , Element XPATH :{xpath}")
    dynamic_xpaths(driver,element,xpath)
    print("-"*100)



driver.quit()



