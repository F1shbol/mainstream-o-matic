from os import path
import pandas as pd
from bs4 import BeautifulSoup as Soup
import requests
from pandas import DataFrame

print(pd.__version__)

print("Hello world!")

ffc_response = requests.get('https://csweb.wooster.edu/')

# 
adp_soup = Soup(ffc_response.text, "html.parser")

tables = adp_soup.find_all('table')

print("tables: ", len(tables))

adp_table = tables[1]
rows = adp_table.find_all('tr')
# print(rows[0])

first_data_row = rows[1]
first_data_row.find_all('td')
[str(x.string) for x in first_data_row.find_all('td')]

def parse_row(row):
    # Take in a tr tag and get the data out of it in the form of a list of
    # strings.
    return [str(x.string) for x in row.find_all('td')]

list_of_parsed_rows = [parse_row(row) for row in rows[1:]]
# print(list_of_parsed_rows)

df = DataFrame(list_of_parsed_rows)
print(df.head())