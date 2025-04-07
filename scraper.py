from linkify import linkifyInput
from frontend import welcome

import pandas as pd
from bs4 import BeautifulSoup as Soup
import requests
from pandas import DataFrame
from time import sleep
import sys

# Might want to move this to its own file with any other
# functions I think up
# This one takes a row from the html table and extracts
# each date and its number of listeners
def parseRow3(row):
    timeSrch = row.find(attrs={'class':['js-date']})
    time = str(timeSrch.attrs['datetime'])

    listenersSrch = row.find(attrs={'class':['js-value']})
    listeners = int(listenersSrch.attrs['data-value'])

    return time, listeners

if (welcome() == False):
    sys.exit("Program exited")

# gets the lists returned by linkify.py
names, playcounts, links = linkifyInput()

frameStarter = {"name": names,
        "playcount": playcounts,}

frame = pd.DataFrame(frameStarter)

print(frame)

oneweek = []
onemonth = []
threemonths = []
sixmonths = []

idx = 1

for link in links:
    print("running link", idx, "of", len(links)) # progress meter
    ffc_response = requests.get(link) # gets raw code from a site and stores it in a variable
    adp_soup = Soup(ffc_response.text, "html.parser") # turns raw code into a Soup object
    tables = adp_soup.find_all('table') # finds tables in the site
    adp_table = tables[1] # as the site stands now, the second table is the one with the data we want
    rows = adp_table.find_all('tr') # stores all rows in the table
    list_of_parsed_rows = [parseRow3(row) for row in rows[1:]] # parses every row except the header
    df = DataFrame(list_of_parsed_rows) # turns parsed rows into a pandas dataframe

    lastWeek = df.loc[173:179]
    lastMonth = df.loc[150:179]
    last3Months = df.loc[90:179]

    oneweek.append(round(lastWeek[[1]].mean().iloc[0], 3))
    onemonth.append(round(lastMonth[[1]].mean().iloc[0], 3))
    threemonths.append(round(last3Months[[1]].mean().iloc[0], 3))
    sixmonths.append(round(df[[1]].mean().iloc[0], 3))

    sleep(1)
    idx += 1

frame["1w"] = oneweek
frame["1mo"] = onemonth
frame["3mo"] = threemonths
frame["6mo"] = sixmonths

# print(frame)
frame.to_csv('file1.csv')