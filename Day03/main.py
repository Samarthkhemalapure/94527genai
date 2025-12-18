#import required packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#start the selenium browser sessoin
driver=webdriver.Chrome()

#load desired 
#time.sleep(2.5)

driver.get("https://google.com/")

print("Initialize page title:",driver.title)

#define Wait strategy -- set one time in the application
"driver.implicitly_wait(5)"

#access the controls on the page 
#time.sleep(5)
search_box=driver.find_element(By.NAME,"q")

#Interact with console
for ch in "dkte result":
    search_box.send_keys(ch)
    time.sleep(0.2)

"""search_box.send_keys("dkte result")"""
search_box.send_keys(Keys.RETURN)

#wait for result
print("Laer Page Title:",driver.title)

#stop the session
time.sleep(10)
driver.quit()