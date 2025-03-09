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
def linkifyInput():
    starter = "https://www.last.fm/music/"
    names = []
    playcounts = []

    # Finds the number of two-line entries in the input file
    with open(r"input.txt", 'r') as fp:
        lines = len(fp.readlines())
        entries = lines//2
        # print("lines:",lines)
        # print("entries",entries)

    # puts the input sile's content into name and playcount lists
    with open(r"input.txt", 'r') as fp:
        for i in range(entries):
            names.append(fp.readline())
            names[i] = names[i][:-1] # remove trailing \n
            playcounts.append(int(fp.readline()))

    # print(names)
    # print(playcounts)

    links = []

    for i in range(entries):
        tempstr = ""
        for char in names[i]:
            if (char == " "):
                tempstr += "+"
            else:
                tempstr += char
        names[i] = tempstr

    for i in range(entries):
        links.append(starter + names[i])

    # print(links)
    return names, playcounts, links