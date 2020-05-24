#! python3
# Download every linked page on the page, flag invalid links and print them out.
# NOTE: I'm using Dutch language settings, therefore this may not work in non-Dutch browsers.

r"""This program does the following (using selenium):
Go to specified link
Find all hrefs
Print all invalid links"""

from selenium import webdriver
import validators


def get_all_links(webpage):
    browser = webdriver.Chrome()
    browser.get(webpage)
    list_of_href = []  # create list for links
    for href in browser.find_elements_by_link_text(''):
        list_of_href.append(href.get_attribute('href'))  # find all href links
    list_of_href = list(dict.fromkeys(list_of_href))  # remove duplicates
    for href in list_of_href:
        if validators.url(href):
            print('Link found: ' + str(href))


# Site made for webscraping
get_all_links('http://shop.demoqa.com/')
