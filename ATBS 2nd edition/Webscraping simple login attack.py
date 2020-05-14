#! Python3
# Copied from YT video: https://www.youtube.com/watch?v=UtNYzv8gLbs
# I copied this to learn how to use information from other files and how to interact with websites using Py3

import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://craiglist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhas'

names = json.load(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(10))

    requests.post(url, allow_redirects=False, data={
        'auid2yjauysd2uasdasdasd': username,
        'kjauysd6sAJsDhyui2yasd': password
    })

    print(f'sending username {username} and password {password}')
