import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import open_json, write_json

# defining new variable passing two parameters
writer = csv.writer(open("output.csv", 'w+'))
credentials = open_json("./credentials.json")

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/usr/bin/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.google.com')

# click accept QS5gu sy4vM
accept_button = driver.find_element(By.ID, "L2AGLb")
accept_button.click()
sleep(0.5)

# locate search form by_name
search_query = driver.find_element(By.NAME, 'q')

# send_keys() to simulate the search text key strokes
search_query.send_keys(
    'site:linkedin.com/in/ AND "CEO" AND "Paris"')
# .send_keys() to simulate the return key
search_query.send_keys(Keys.RETURN)
sleep(0.5)

# locate URL by_class_name
linkedin_urls = driver.find_element(By.CLASS_NAME, 'iUh30')

# variable linkedin_url is equal to the list comprehension
linkedin_urls = [url.text for url in linkedin_urls]
