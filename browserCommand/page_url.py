import time

from selenium import webdriver
browser=webdriver.Chrome()
browser.maximize_window()
browser.get("http://sqa.linespay.com/")
url=browser.current_url
print(url)
try:
    assert "http://sqa.linespay.com/" in url
except AssertionError:
    print(str(AssertionError))
time.sleep(5)
browser.close()
print("test complete")

