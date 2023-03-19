from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get("http://sqa.linespay.com/")
browser.maximize_window()

username_field=browser.find_element(By.NAME,'username')
if username_field is not None:
    print("correct")
else:
    print("incorrect")
password_field=browser.find_element(By.NAME,'pwd')
if password_field is not None:
    print("correct")
else:
    print("incorrect")
browser.close()

