# https://www.last.fm/music/Catfish+and+the+Bottlemen/The+Ride
# https://www.last.fm/music/Tyler,+the+Creator
# https://www.last.fm/music/Chance+the+Rapper/_/Hot+Shower
# https://www.last.fm/music/Prince

starter = "https://www.last.fm/music/"

f = open('input.txt')

names = ["a","a","a","a","a"]
playcounts = [0,0,0,0,0] 
links = ["a","a","a","a","a"]

for i in range(5):
    names[i] = f.readline()
    playcounts[i] = int(f.readline())
# for line in f:
#     print(line, end='')

f.closed

print(names)
print(playcounts)

for i in range(5):
    tempstr = ""
    for char in names[i]:
        if (char == " "):
            tempstr += "+"
        else:
            tempstr += char
    names[i] = tempstr

for i in range(len(links)):
    links[i] = starter + names[i][:-1]

print(links)