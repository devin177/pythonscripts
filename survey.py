from threading import Timer
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
load_dotenv()

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://cas.ucdavis.edu/cas/login?service=https%3a%2f%2fhem.ucdavis.edu%2findex-redirect.aspx')
# Select the id box
id_box = driver.find_element(By.NAME, 'username')
# Send id information
id_box.send_keys(os.getenv("username"))
# Find password box
pass_box = driver.find_element(By.NAME, 'password')
# Send password
pass_box.send_keys(os.getenv("password"))
# Find login button
login_button = driver.find_element(By.NAME, 'submit')
# Click login
login_button.click()
# Click the button that sends you a push notif
iframe = driver.find_element(By.ID, "duo_iframe")
driver.switch_to.frame(iframe)
push_button = driver.find_element(By.CSS_SELECTOR, '#auth_methods > fieldset > div.row-label.push-label > button')
push_button.click()

# Wait 5 seconds for user to authenticate
time.sleep(12)
# now on the HEM home page
survey_button = driver.find_element(By.CSS_SELECTOR, "#ctl03 > div.mt-3 > div > a")
survey_button.click()
continue_button = driver.find_element(By.CSS_SELECTOR, "#mainbody > div.container-fluid > div.header.ta-center.mb-3 > div > div.col-xs-6.ta-right > a")
continue_button.click()
q1 = driver.find_element(By.CSS_SELECTOR, "#mainbody > main > form > div:nth-child(60) > fieldset > div > div:nth-child(2) > div")
q2 = driver.find_element(By.CSS_SELECTOR, "#mainbody > main > form > div:nth-child(89) > fieldset > div > div:nth-child(2) > div")
q3 = driver.find_element(By.CSS_SELECTOR, "#mainbody > main > form > div:nth-child(118) > fieldset > div > div:nth-child(2) > div")
q4 = driver.find_element(By.CSS_SELECTOR, "#mainbody > main > form > div:nth-child(147) > fieldset > div > div:nth-child(2) > div")
q5 = driver.find_element(By.CSS_SELECTOR, "#mainbody > main > form > div:nth-child(176) > fieldset > div > div:nth-child(2) > div")
q6 = driver.find_element(By.CSS_SELECTOR, "#mainbody > main > form > div:nth-child(205) > fieldset > div")
q1.click()
q2.click()
q3.click()
q4.click()
q5.click()
q6.click()
final_submit = driver.find_element(By.CSS_SELECTOR, "#mainbody > footer > div > div.col-xs-6.ta-right > input")
final_submit.click()
