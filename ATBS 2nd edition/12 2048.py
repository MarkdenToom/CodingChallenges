#! python3
# Play the 2048 game by going up, right, down and left ad infinitum.
# NOTE: I'm using Dutch language settings, therefore this may not work in non-Dutch browsers.

r"""This program does the following (using selenium):
Go to https://gabrielecirulli.github.io/2048/
Press up, right, down and left ad infinitum"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
while browser.find_element_by_class_name("retry-button").is_displayed() is False:
    browser.find_element_by_tag_name('html').send_keys(Keys.UP + Keys.RIGHT + Keys.DOWN + Keys. LEFT)
sleep(5)
browser.close()
