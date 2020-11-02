#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# google_search.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.google.com')

# locate search form by_name
search_query = driver.find_element_by_name('q')

# send_keys() to simulate the search text key strokes
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')

# .send_keys() to simulate the return key
search_query.send_keys(Keys.RETURN)

# div = driver.find_element_by_class_name('yuRUbf')
# print(div.find_element_by_css_selector('a').get_attribute('href'))

# Get all URLs
elems = driver.find_elements_by_xpath("//a[@href]")
linkedin_urls = []
for elem in elems:
    # linkedin_urls = driver.find_elements_by_class_name('LC20lb')
    if not 'google' in elem.get_attribute("href"):
        #candidates = elem.get_attribute("href")
        linkedin_urls.append(elem.get_attribute("href"))

nomes = driver.find_elements_by_class_name('LC20lb')
print(driver.find_element_by_class_name('LC20lb').text)

# Gets the name of candidate
names_list = driver.find_elements_by_class_name('LC20lb')
names_list = [url.text for url in names_list]
# to print all elements within our list
names_list
linkedin_urls

# print the first value
linkedin_urls[0]
listaLinks[0]

# print the second value
linkedin_urls[1]
