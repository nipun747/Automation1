from selenium import webdriver
import time
browser = webdriver.Chrome()
time.sleep(5)
browser.maximize_window()
browser.get('http://sqa.linespay.com/')
time.sleep(500)
browser.close()
