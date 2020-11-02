#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script.py

import parameters
import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# function to ensure all key data fields have a value
def validate_field(field):# if field is present pass if field:pass
    if field == 'none':
        field = 'No results'
        return field
    else:
        return field

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login')

username = driver.find_element_by_id('username')
username.send_keys(parameters.linkedin_username)

password = driver.find_element_by_id('password')
password.send_keys(parameters.linkedin_password)

# locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('btn__primary--large')
# locate submit button by_xpath
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
# .click() to mimic button click
log_in_button.click()
sleep(0.5)

driver.get('https://www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

# Get all URLs
elems = driver.find_elements_by_xpath("//a[@href]")
linkedin_urls = []
for elem in elems:
    if not 'google' in elem.get_attribute("href"):
        linkedin_urls.append(elem.get_attribute("href"))
linkedin_urls
sleep(0.5)

driver.get('https://www.linkedin.com/in/tadeubanzato')
driver.page_source
########### OK

header = ['Name', 'Job Title', 'Location', 'Link']
with open(parameters.file_name, 'a') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header) # write header
# For loop to iterate over each URL in the list
    for linkedin_url in linkedin_urls:

        # get the profile URL
        driver.get(linkedin_url)

        # add a 5 second pause loading each URL
        sleep(5)

        # assigning the source code for the webpage to variable sel
        sel = Selector(text=driver.page_source)

        name = sel.xpath('//*[starts-with(@class, "inline t-24 t-black t-normal break-words")]/text()').extract_first()
        if name:
          name = name.strip()
          # print(name)

        job_title = sel.xpath('//*[starts-with(@class, "mt1 t-18 t-black t-normal break-words")]/text()').extract_first()
        if job_title:
            job_title = job_title.strip()
            # print(jobtitle)

        location = sel.xpath('//*[starts-with(@class, "t-16 t-black t-normal inline-block")]/text()').extract_first()
        if location:
          location = location.strip()
          # print(location)

        linkedin_url = driver.current_url

        currentJob = sel.xpath('//h3/text()').extract_first()
        # validating if the fields exist on the profile
        name = validate_field(name)
        job_title = validate_field(job_title)
        location = validate_field(location)
        linkedin_url = validate_field(linkedin_url)

        rows = [name,job_title,location,linkedin_url]
        print('Writing to CSV:', rows)

        csv_writer.writerow([name,job_title,location,linkedin_url])
