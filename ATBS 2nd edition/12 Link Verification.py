#! python3
# Download every linked page on the page, flag invalid links and print them out.
# NOTE: I'm using Dutch language settings, therefore this may not work in non-Dutch browsers.

r"""This program does the following (using selenium):
Go to specified link
Find all hrefs
Print all invalid links"""

import validators
import requests
from bs4 import BeautifulSoup


def verify_links(webpage):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                             '70.0.3538.77 Safari/537.36'}  # user agent added to avoid "403: forbidden errors"
    res = requests.get(webpage, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # find all href
    list_of_href = []
    for href in soup.find_all('a'):
        list_of_href.append(href.get('href'))
    list_of_href = list(dict.fromkeys(list_of_href))  # remove duplicates

    # find all links from href
    for href in list_of_href:
        if validators.url(href):  # validators ensures I only get actual URL's.
            res = requests.get(href)
            if res.status_code == 404:
                print('404 error detected: ' + href)


verify_links('https://markdentoom.github.io/')
