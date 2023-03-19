from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait():
    #step 1:launch the browser
    browser=webdriver.Chrome()
    browser.maximize_window()
    #step 2: go to the login page
    browser.get('http://sqa.linespay.com/')
    #step 3: Enter username and password

    username=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.NAME,"username")))

    display_state= username.is_displayed()
    try:
        assert display_state==True
        username.send_keys("mnc")
    except AssertionError:
        print("username not found")

    password=browser.find_element(By.NAME,"pwd")
    password_enabled_state=password.is_enabled()
    try:
        assert password_enabled_state==True
        password.send_keys("Prism")
    except AssertionError:
        print("password not enabled")
    #step 4: Click login button
    login=browser.find_element(By.ID,"login")
    try:
        assert login.is_enabled()
        login.click()
    except AssertionError:
        print("login button isn't available")



wait()