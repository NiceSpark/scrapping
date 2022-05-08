import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
from utils import open_json, write_json, validate_field, validate_url


# defining new variable passing two parameters
writer = csv.writer(open("output.csv", 'w+'))
credentials = open_json("./credentials.json")

# writerow() method to the write to the file object
writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver
ser = Service('/usr/bin/chromedriver')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_id
username = driver.find_element(By.ID, "session_key")

# send_keys() to simulate key strokes
username.send_keys(credentials["thomas"]["login"])

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_id
password = driver.find_element(By.ID, "session_password")

# send_keys() to simulate key strokes
password.send_keys(credentials["thomas"]["password"])
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element(By.CLASS_NAME,
                                     "sign-in-form__submit-button")


# .click() to mimic button click
sign_in_button.click()
sleep(2)

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
linkedin_urls = driver.find_elements(By.CLASS_NAME, 'iUh30')
# variable linkedin_url is equal to the list comprehension
linkedin_urls = [url.text.replace(" \u203a ", "/in/")
                 for url in linkedin_urls if validate_url(url)]
write_json("linkedin_urls.json", linkedin_urls)
sleep(0.5)


# For loop to iterate over each URL in the list
for linkedin_url in linkedin_urls:
    name = linkedin_url[linkedin_url.find(
        "linkedin.com/in/")+len("linkedin.com/in/"):]
    # get the profile URL
    driver.get(linkedin_url)
    sleep(3)
    # Get entire page screenshot
    image = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(image))  # uses PIL library to open image in memory
    im.save(f'screenshots/{name}.png')  # saves new cropped image
    sleep(2)

# terminates the application
driver.quit()
