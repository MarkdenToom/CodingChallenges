# !python3
# Scrape web page for social media links

import requests
import validators
from bs4 import BeautifulSoup


def list_links(link):  # take all external links from a website and turn it into a list
    page = requests.get(link)  # download info from website
    page.raise_for_status()  # check if the download succeeded
    soup = BeautifulSoup(page.text, 'lxml')  # convert class to bs4
    list_of_results = []  # create empty list for results
    for link in soup.find_all('a'):  # find all <a>
        link = str(link.get('href'))  # prepare for filter by removing html fluff
        if validators.url(link):  # filter out non-links
            if 'facebook.com' in link or 'youtube.com' in link or 'instagram.com' in link or 'twitter.com' in link or \
                    'reddit.com' in link or 'pinterest.com' in link or 'linkedin.com' in link or 'github.com' in link:
                list_of_results.append(link)  # add results to the list
    list_of_results = list(dict.fromkeys(list_of_results))  # remove duplicates
    return list_of_results  # return found links


print(list_links('https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists'))
print(list_links('https://www.dreamgrow.com/top-15-most-popular-social-networking-sites/'))
print(list_links('http://automatetheboringstuff.com/2e/chapter12/'))
