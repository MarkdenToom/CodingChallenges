#! python3
# Opens first few pages of search results for google search.

"""This is what the program does:
Gets search keywords from the command line arguments
Retrieves the search results page
Opens a browser tab for each result

This means the code will need to do the following:
Read the command line arguments from sys.argv.
Fetch the search result page with the requests module.
Find the links to each search result.
Call the webbrowser.open() function to open the web browser.

How to use: type "searchpypi matplotlib packs" to search "matplotlib packs" on pypi.org."""

import requests
import sys
import webbrowser
import bs4

print('Searching...')  # display text while downloading the search result page
res = requests.get('https://google.com/search?q=''https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')  # retrieves top search result links
linkElems = soup.select('.package-snippet')  # opens a browser tab for each result

numOpen = min(5, len(linkElems))  # open a max of 5 pages or any amount of results if there's less than 5 results
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
