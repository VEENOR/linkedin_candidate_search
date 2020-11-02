#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# linkedin_login.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import parameters

# install webdrive when needed
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login')

# locate email form by element_by_id
username = driver.find_element_by_id('username')

# send_keys() to simulate key strokes
username.send_keys('login-email@youremail.com')

# locate password form by_class_name
password = driver.find_element_by_id('password')

# send_keys() to simulate key strokes
password.send_keys('<YOUR PASSWORD>')

# locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('btn__primary--large')

# locate submit button by_xpath
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()
