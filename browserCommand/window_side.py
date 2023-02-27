import time

from selenium import webdriver
browser=webdriver.Chrome()
browser.maximize_window()
browser.get("http://sqa.linespay.com/")
current_window=browser.get_window_size()
print("current_window:width={}px,height={}px".format(current_window['width'], current_window['height']))

browser.set_window_size(800, 600)
set_window=browser.get_window_size()
#print("set_window:width={}px,height={}px".format(set_window['width'], set_window['height']))
try:
   assert set_window['width'] == 800 and set_window['height'] == 600, "window size isn't correct"
   print("window size correct")
except AssertionError:
    print(str(AssertionError)+"There's an error")
time.sleep(5)
browser.close()
print("test complete")

