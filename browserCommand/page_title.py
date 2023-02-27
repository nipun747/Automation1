from selenium import webdriver
import time
browser = webdriver.Chrome()
time.sleep(5)
browser.maximize_window()
browser.get('http://sqa.linespay.com/')
title=browser.title
print(title)
try:
    assert "by " in title
except AssertionError:
    print(str(AssertionError))
time.sleep(5)
browser.close()
print("test complete")