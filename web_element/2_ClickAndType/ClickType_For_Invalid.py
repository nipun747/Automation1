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
    password.send_keys("sm")
    #step 4: Click login button
    login=browser.find_element(By.ID,"login")
    login.click()

    #step 5:Expected result by text
    expected_result="* Login is incorrect!"
    #step 6:Current Result
    current_result=browser.find_element(By.CSS_SELECTOR,"form[method='post'] > .error").text
    #step 7: assertion
    try:
        assert expected_result==current_result
        print("Test Case for Invalid=Passed")
    except AssertionError:
        print(AssertionError,"Test case for Invalid=Failed")
login_page()