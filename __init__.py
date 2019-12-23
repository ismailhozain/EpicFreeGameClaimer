from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
website_link = "https://www.epicgames.com/id/login"
username = ""
password = ""
driver = webdriver.Chrome()
driver.get(website_link)
time.sleep(5)
element = driver.find_element_by_name("email")
element.send_keys(username)
element = driver.find_element_by_name("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
#logged in now :)
website_link = "https://www.epicgames.com/store/en-US/free-games"
driver.get(website_link)
time.sleep(5)
link = driver.find_elements_by_tag_name("a")
link[28].click()
time.sleep(5)
button = driver.find_elements_by_tag_name("button")
button[8].click()
time.sleep(5)
element = driver.find_element_by_name("email")
element.send_keys(username)
element = driver.find_element_by_name("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
time.sleep(5)
button = driver.find_elements_by_tag_name("button")
button[8].click()
print("done boomer")
