# https://www.last.fm/music/Catfish+and+the+Bottlemen/The+Ride
# https://www.last.fm/music/Tyler,+the+Creator
# https://www.last.fm/music/Chance+the+Rapper/_/Hot+Shower
# https://www.last.fm/music/Prince
# Some link examples ^^

# This .py file takes in an imput file of form:
# artist1
# playcount
# ...
# and creates lists of the artists, the playcounts, and links to their
# last.fm pages
import os
import fnmatch
import csv

def linkifyInput():
    starter = "https://www.last.fm/music/"
    names = []
    playcounts = []

    # csv vs. txt
    # My plan is to ask the user which one they want, but for now
    # I'm hard-coding it
    filetype = 'csv'

    # Same deal. This option will ignore all artists with only one play
    fastMode = 'n'

    if (filetype == "txt"):
        # Finds the number of two-line entries in the input file
        with open(r"input.txt", 'r') as fp:
            lines = len(fp.readlines())
            entries = lines//2

        # puts the input file's content into name and playcount lists
        with open(r"input.txt", 'r') as fp:
            for i in range(entries):
                names.append(fp.readline())
                names[i] = names[i][:-1] # remove trailing \n
                playcounts.append(int(fp.readline()))

    elif (filetype == "csv"):
        # Maintains a count of how many plays are by each artist
        # If an artist is in the dictionary, increment its value by 1
        # If not, put it in the dictionary with a value of one
        def dictCheck(artist, thisdict):
            if (artist in thisdict):
                thisdict[artist] += 1
            else:
                thisdict[artist] = 1
        
        # Since the ghan exporter starts its .csv files with "scrobbles",
        # we search for that and if there's only one match we select it
        cur_dir = os.getcwd()
        pwdLs = os.listdir(cur_dir)
        srch = fnmatch.filter(pwdLs, "scrobbles*")
        if (len(srch) == 1):
            inputCsv = srch[0]

        # Reads the input .csv to a dict object, then iterates through it
        # creating a new dictionary where each artist is a key and their
        # playcount is the value
        with open(inputCsv, newline='', errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            thisdict = dict()
            for row in reader:
                dictCheck(row['artist'], thisdict)
        
        # Append the names and playcounts to their lists
        # For fast mode it checks if the artist has more than one play first
        if (fastMode == 'y'):
            for x, y in thisdict.items():
                if (int(y) > 1):
                    names.append(x)
                    playcounts.append(int(y))
        else:
            # entries = len(thisdict)
            for x, y in thisdict.items():
                names.append(x)
                playcounts.append(int(y))

    links = []

    namesCopy = names[:]

    # replaces spaces with plusses and fixes a few other trouble characters
    for i in range(len(names)):
        tempstr = ""
        for char in namesCopy[i]:
            if (char == " "):
                tempstr += "+"
            elif (char == "/"):
                tempstr += "%"
                tempstr += "2F"
            elif (char == "?"):
                tempstr += "%"
                tempstr += "3F"
            elif (char == "+"):
                tempstr += "%"
                tempstr += "252B"
            else:
                tempstr += char
        namesCopy[i] = tempstr
    
    for i in range(len(namesCopy)):
        links.append(starter + namesCopy[i])

    # print(links)
    return names, playcounts, links