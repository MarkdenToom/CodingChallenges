#! python3
# Go to https://www.flickr.com/ and download all images for a specific search result
# NOTE: Imgur uploads videos and gifs too and randomly changes the picture page sometimes. It's a far harder challenge.
# NOTE: I'm using Dutch language settings, therefore this may not work in non-Dutch browsers.

r"""This program does the following (using selenium):
Go to https://www.flickr.com/
Search specific string
Find links to all search results
Create folder for downloads
Download all image results to folder"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import chdir
from pathlib import Path
from urllib.request import urlretrieve


def download_all(search_keyword):
    new_directory = Path.home() / r'Py3Projects\12-Webscraping\12 Image Site Downloader' / search_keyword
    Path.mkdir(new_directory, parents=True, exist_ok=True)
    chdir(new_directory)
    browser.get('https://www.flickr.com/')
    sleep(1)
    browser.find_element_by_id('search-field').send_keys(search_keyword + Keys.ENTER)
    sleep(1)
    results = browser.find_elements_by_class_name('overlay')

    # create list of links to the individual pictures
    list_of_img_links = []
    for img_elem in results:
        list_of_img_links.append(img_elem.get_attribute('href'))

    # download full resolution pictures
    for img_link in list_of_img_links:
        browser.get(img_link)
        sleep(1)
        src = browser.find_element_by_class_name('main-photo').get_attribute('src')
        img_name = search_keyword + ' ' + str(list_of_img_links.index(img_link) + 1) + src[-4:]
        urlretrieve(src, img_name)
        print(f'Picture {src} saved as {img_name}!')
        sleep(1)
    print(f'Downloaded a total of {str(len(list_of_img_links))} pictures!')


browser = webdriver.Chrome()
download_all('Lasagna')
browser.close()



