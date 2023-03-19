from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def login_page():
    #step 1:launch the browser
    browser=webdriver.Chrome()
    browser.maximize_window()
    #step 2: go to the login page
    browser.get('http://sqa.linespay.com/')
    #step 3: Enter username and password
    username=browser.find_element(By.NAME,"username")
    username.send_keys("mnc")
    password=browser.find_element(By.NAME,"pwd")
    password.send_keys("Prism")
    #step 4: Click login button
    login=browser.find_element(By.ID,"login")
    login.click()

    #step 5:Expected result
    expected_result="http://sqa.linespay.com/"
    #step 6:Current Result
    current_result=browser.current_url
    #step 7: assertion
    try:
        assert expected_result==current_result
        print("passed")
    except AssertionError:
        print(AssertionError)
login_page()