from linkify import linkifyInput
import pandas as pd
from bs4 import BeautifulSoup as Soup
import requests
from pandas import DataFrame
from time import sleep

# You'll want to update this function and putthe 3rd version in this file
from testPrince import parseRow2

# gets the lists returned by linkify.py
names, playcounts, links = linkifyInput()

# print(names)
# print(playcounts)
# print(links)

data = {"name": names,
        "playcount": playcounts,}

frame = pd.DataFrame(data)

print(frame)

oneweek = []
onemonth = []
threemonths = []
sixmonths = []

idx = 1

for link in links:
    print("running link", idx, "of", len(links))
    ffc_response = requests.get(link)
    adp_soup = Soup(ffc_response.text, "html.parser")
    tables = adp_soup.find_all('table')
    adp_table = tables[1]
    rows = adp_table.find_all('tr')
    list_of_parsed_rows = [parseRow2(row) for row in rows[1:]]
    df = DataFrame(list_of_parsed_rows)

    lastWeek = df.loc[173:179]
    lastMonth = df.loc[150:179]
    last3Months = df.loc[90:179]

    print("array before appending:", oneweek)
    oneweek.append(round(lastWeek[[1]].mean().iloc[0], 3))
    print("array after:", oneweek)
    onemonth.append(round(lastMonth[[1]].mean().iloc[0], 3))
    threemonths.append(round(last3Months[[1]].mean().iloc[0], 3))
    sixmonths.append(round(df[[1]].mean().iloc[0], 3))

    sleep(2)
    idx += 1

# frame2["debt"] = 16.5
frame["1w"] = oneweek
frame["1mo"] = onemonth
frame["3mo"] = threemonths
frame["6mo"] = sixmonths

# print(frame)
frame.to_csv('file1.csv')