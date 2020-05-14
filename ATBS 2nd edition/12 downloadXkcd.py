#! python3
# Download every single XKCD comic from https://xkcd.com/

# raise MemoryError('Running this program will result in over 2000 pictures being downloaded to your computer')

"""This is what the program does:
Loads the XKCD home page
Saves the comic image on that page
Follows the Previous Comic link
Repeats until it reaches the first comic

This means the code will need to do the following:
Download pages with the requests module.
Find the URL of the comic image for a page using Beautiful Soup.
Download and save the comic image to the hard drive with iter_content().
Find the URL of the Previous Comic link, and repeat."""

import requests
import os
import bs4
from pathlib import Path

os.chdir(Path.home()/r'Py3Projects\12-Webscraping')

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)  # create folder in cwd, it's ok if it already exists
while not url.endswith('#'):
    # Download the page.
    print('Downloading page ' + url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if not comicElem:  # skip if there's no image file
        print('Comic image not found.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image ' + comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')  # example: 'xkcd/satellite.png/'

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the previous button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
