from os import path
import pandas as pd
from bs4 import BeautifulSoup as Soup
import requests
from pandas import DataFrame

print(pd.__version__)

ffc_response = requests.get('https://www.last.fm/music/Prince')
# ffc_response = requests.get('https://www.last.fm/music/The+Weeknd/Hurry+Up+Tomorrow')

adp_soup = Soup(ffc_response.text, "html.parser")

tables = adp_soup.find_all('table')

print("tables: ", len(tables))

adp_table = tables[1]
rows = adp_table.find_all('tr')
print(rows[0])

first_data_row = rows[1]
print(first_data_row.find_all('td'))

def parse_row(row):
    # Take in a tr tag and get the data out of it in the form of a list of
    # strings.
    return [str(x.string) for x in row.find_all(['td','time'])]


# Makes a list manually with one slot for date and one slot for 
# time, then returns that
def parseRow2(row):
    timeList = [str(x.attrs['datetime']) for x in row.find_all(attrs={'class':['js-date']})]
    listenerList = [str(x.attrs['data-value']) for x in row.find_all(attrs={'class':['js-value']})]

    result = [timeList[0], listenerList[0]]
    return result


list_of_parsed_rows = [parseRow2(row) for row in rows[1:]]
# print(list_of_parsed_rows)

df = DataFrame(list_of_parsed_rows)
print(df.head())