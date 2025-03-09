# str1 = "Princes\n"
# slice1 = str1[:-1]
# print(slice1)
from linkify import linkifyInput
names, playcounts, links = linkifyInput()

for link in links:
    print(link)