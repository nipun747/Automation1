from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# 1 load browser
browser = webdriver.Chrome()
browser.maximize_window()
# 2 load the desired url
browser.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'dropdown'))))
default_selected_option=dropdown.first_selected_option
try:
    assert default_selected_option.is_selected,'Please select an option'
    print("default option is correct")
except AssertionError:
    print("default option not selected")
# Dropdown select options
# dropdown.select_by_value() -accept string values
# dropdown.select_by_index() -accept integar values
# dropdown.select_by_visible_text() -accept string values
dropdown.select_by_value("1")
time.sleep(5)
#6 get the selected option and check if it's correct
new_selected_option=dropdown.first_selected_option
try:
    assert new_selected_option.is_selected,"option 1"
    print("option 1 is selected correctly")
except AssertionError:
    print("couldn't select")


print("test case passed")