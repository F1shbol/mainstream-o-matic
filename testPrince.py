from os import path
import pandas as pd
from bs4 import BeautifulSoup as Soup
import requests
from pandas import DataFrame

print(pd.__version__)

# ffc_response = requests.get('https://www.last.fm/music/Prince')
ffc_response = requests.get('https://www.last.fm/music/Doechii')

adp_soup = Soup(ffc_response.text, "html.parser")

tables = adp_soup.find_all('table')

print("tables: ", len(tables))

adp_table = tables[1]
rows = adp_table.find_all('tr')
print(rows[0])

first_data_row = rows[1]
# print(first_data_row.find_all('td'))

def parse_row(row):
    # Take in a tr tag and get the data out of it in the form of a list of
    # strings.
    return [str(x.string) for x in row.find_all(['td','time'])]


# Makes a list manually with one slot for date and one slot for 
# time, then returns that.
# Time and Listeners don't need to be their own lists, so you should
# replace the findall with find soon
def parseRow2(row):
    timeList = [str(x.attrs['datetime']) for x in row.find_all(attrs={'class':['js-date']})]
    listenerList = [int(x.attrs['data-value']) for x in row.find_all(attrs={'class':['js-value']})]

    result = [timeList[0], listenerList[0]]
    return result

def parseRow3(row):
    timeSrch = row.find(attrs={'class':['js-date']})
    time = str(timeSrch.attrs['datetime'])

    listenersSrch = row.find(attrs={'class':['js-value']})
    listeners = int(listenersSrch.attrs['data-value'])

    return time, listeners


list_of_parsed_rows = [parseRow3(row) for row in rows[1:]]
# print(list_of_parsed_rows)

df = DataFrame(list_of_parsed_rows)
# print(df.tail())
print(df.loc[173:179]) # prints last seven days of listeners

# Here you're filtering for the last 7, 30, and 90 days of listener data
# I'm assuming the data always goes back 180 days, so I'm going to leave it
# as treating 179 as the last index (loc doesn't support reverse-indexing
# for some reason)
lastWeek = df.loc[173:179]
lastMonth = df.loc[150:179]
last3Months = df.loc[90:179]
print("Last week's average listeners:", lastWeek[[1]].mean().iloc[0])
# print("iloc thing:", lastWeek[[1]].mean().iloc[0])
print("Last month's average listeners:", lastMonth[[1]].mean().iloc[0])
print("Last three months' average listeners:", last3Months[[1]].mean().iloc[0])
print("Last six months' average listeners:", df[[1]].mean().iloc[0]) # overall average listeners