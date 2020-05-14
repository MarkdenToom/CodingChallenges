#! python3
# Tabulates population and number of census tracts for each county.

"""This is what your program does:

Reads the data from the Excel spreadsheet
Counts the number of census tracts in each county
Counts the total population of each county
Prints the results
This means your code will need to do the following:

Open and read the cells of an Excel document with the openpyxl module.
Calculate all the tract and population data and store it in a data structure.
Write the data structure to a text file with the .py extension using the pprint module."""

from os import chdir
from pathlib import Path
import openpyxl
import pprint

chdir(Path.home()/r'Py3Projects\automate_online-materials')

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):  # start at the second row, continue to the end + skip the header.
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exists: countyData[state abbreviation{}]
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists:
    # countyData[state abbrev][county]['tracts']
    # countyData[state abbrev][county]['pop']
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tracts.
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
chdir(Path.home()/r'Py3Projects\13-Working with Excel Spreadsheets')
resultFile = open(Path('census2010.py'), 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')


"""If you change the cwd in the interactive shell to the location of the new file, you can use it as module: 

import census2010

print(census2010.allData['AK']['Anchorage'])  # {'pop': 291826, 'tracts': 55}
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchoragePop))  # The 2010 population of Anchorage was 291826"""
