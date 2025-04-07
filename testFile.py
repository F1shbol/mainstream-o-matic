# str1 = "Princes\n"
# slice1 = str1[:-1]
# print(slice1)

# from datetime import datetime

# current_timestamp = int(datetime.now().timestamp())
# print(current_timestamp)
# lastWeek = current_timestamp - 604800
# print(lastWeek)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict)
# print("brand" in thisdict)

# var1 = "year"
# if (var1 in thisdict):
#     thisdict[var1] += 1
# else:
#     thisdict[var1] = 1

# var1 = "yeat"
# if (var1 in thisdict):
#     thisdict[var1] += 1
# else:
#     thisdict[var1] = 1

# print(thisdict)

import os
import fnmatch
import csv

def dictCheck(artist, thisdict):
    if (artist in thisdict):
        thisdict[artist] += 1
    else:
        thisdict[artist] = 1

cur_dir = os.getcwd()
pwdLs = os.listdir(cur_dir)
srch = fnmatch.filter(pwdLs, "scrobbles*")
if (len(srch) == 1):
    inputCsv = srch[0]

with open(inputCsv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    thisdict = dict()
    # for row in reader:
    for row in reader:
        # print(row['artist'])
        dictCheck(row['artist'], thisdict)

print(thisdict)

for x, y in thisdict.items():
    print(x, y)

# import fnmatch
# lst = ['this','is','just','a','test']
# filtered = fnmatch.filter(lst, 'th?s')