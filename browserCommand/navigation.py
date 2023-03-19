import time

from selenium import webdriver
browser=webdriver.Chrome()
#Step 1: get an url
browser.get("https://google.com")
time.sleep(1)
#step 2: Go to another url
browser.get("http://sqa.linespay.com/")
time.sleep(3)
#step 3: go back to the previous url
browser.back()
browser.title
print(browser.title)
time.sleep(3)
#step 4: go to the forward website
browser.forward()
time.sleep(1)
browser.title
print(browser.title)
browser.close()
