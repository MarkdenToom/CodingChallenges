#! python3
# Prints the current weather for a location from the command line.

# TODO: fix error: requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: http://api.openweathermap.org/data/2.5/forecast/daily?q=San%20Francisco,%20US&cnt=3&APPID=e1827eaa0d01f0f335aab9f5013a35fe

"""the program does the following:
1. Reads the requested location from the command line
2. Downloads JSON weather data from OpenWeatherMap.org
3. Converts the string of JSON data to a Python data structure
4. Prints the weather for today and the next two days

So the code will need to do the following:
1. Join strings in sys.argv to get the location.
2. Call requests.get() to download the weather data.
3. Call json.loads() to convert the JSON data to a Python data structure.
4. Print the weather forecast."""

import json
import requests
import sys
from os import chdir

chdir(r'C:\Users\Beheerder\Py3Projects')

weathermapAPI = open('openweathermap.org api.txt').read()
APPID = weathermapAPI

"""
# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickweather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])
"""
location = 'San Francisco, US'  # used to avoid running from the command line for faster testing

# Download the JSON data from openweathermap.org's API
url = f'api.openweathermap.org/data/2.5/weather?id={location}&appid={APPID}'
# url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into Python variable.
weatherData = json.loads(response.text)

# Uncomment to see the raw JSON text:
# print(response.text)

w = weatherData['list']
print(f"""Current weather in {location}:
{w[0]['weather'][0]['main']}-{w[0]['weather'][0]['description']}

Tomorrow:
{w[1]['weather'][0]['main']}-{w[1]['weather'][0]['description']}

Day after tomorrow:
{w[2]['weather'][0]['main']}-{w[2]['weather'][0]['description']}""")
