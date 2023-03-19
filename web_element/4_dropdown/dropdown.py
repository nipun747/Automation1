from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def dropdown_function():
        #1 load browser
        browser=webdriver.Chrome()
        browser.maximize_window()
        #2 load the desired url
        browser.get("http://sqa.linespay.com/")
        #3 login with username
        #username=browser.find_element(By.NAME,'username')
        username=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.NAME,'username')))

        display_state=username.is_displayed()
        try:
            assert display_state==True
            username.send_keys("mnc")
        except AssertionError:
            print("username not found")

        #4 login with password

        password=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.NAME,'pwd')))

        display_state_password=password.is_displayed()

        try:
            assert display_state_password==True
            password.send_keys("su")
        except AssertionError:
            print("password not found")

        #5 click the login button

        login=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID,'login')))

        login_enabe_state=login.is_enabled()

        try:
            assert login_enabe_state==True
            login.click()
        except AssertionError:
            print("login button not found")
        #5 select dropdown
        browser.get("http://sqa.linespay.com/procurement/product_requisition/add/")

        dropdown=(WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID,'ufd_CommercialDoc_request_level'))))

        dropdown.click()
        time.sleep(5)
        #Dropdown select options
        #dropdown.select_by_value() -accept string values
        #dropdown.select_by_index() -accept integar values
        #dropdown.select_by_visible_text() -accept string values
        dropdown.select_by_value("2")
        time.sleep(10)
        print("test case passed")
dropdown_function()

