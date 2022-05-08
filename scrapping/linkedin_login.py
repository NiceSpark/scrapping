
import csv
from time import sleep
from selenium import webdriver
from utils import open_json, write_json

# defining new variable passing two parameters
writer = csv.writer(open("output.csv", 'w+'))
credentials = open_json("./credentials.json")

# writerow() method to the write to the file object
writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/usr/bin/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_id
username = driver.find_element_by_id("session_key")

# send_keys() to simulate key strokes
username.send_keys(credentials["thomas"]["login"])

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_id
password = driver.find_element_by_id("session_password")

# send_keys() to simulate key strokes
password.send_keys(credentials["thomas"]["password"])
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_class_name(
    "sign-in-form__submit-button")


# .click() to mimic button click
sign_in_button.click()
