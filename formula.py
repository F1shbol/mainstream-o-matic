import numpy as np
from pandas import DataFrame

# This one takes a row from the html table and extracts
# each date and its number of listeners
def parseRow3(row):
    timeSrch = row.find(attrs={'class':['js-date']})
    time = str(timeSrch.attrs['datetime'])

    listenersSrch = row.find(attrs={'class':['js-value']})
    listeners = int(listenersSrch.attrs['data-value'])

    return time, listeners

def multiplyCells(row):
    return float(row['playcount']) * float(row['1w'])

# Uses multiplyCells above to weight each artist's listener count by their
# playcount, then adds the resulting series to the dataframe as a new column
def addWeight(frame):
    result = frame.apply(multiplyCells, axis=1)
    frame['weighted'] = result
    return frame

# Uses the logarithmic regression of the Pro users' OWLAs and Mainstream scores
# to create an approximate Mainstream score
def getScore(avg):
    result = 12.4619 * np.log(avg) - 67.0731
    return result

# Uses binary search to find the artist whose OWLA is nearest the user's.
# It can't compare the two values it lands between yet, so it only goes down for now
def playSearch(A1, A2, n, Target):
    L = 0
    R = n-1
    while (L<=R):
        m = (L+R)//2
        if (A1[m] < Target):
            L = m + 1
        elif (A1[m] > Target):
            R = m - 1
        else:
            print("You're exactly as mainstream as ", A2[m-1], " (", A1[m-1], " listeners last week)", sep="")
            return
    print("You're about as mainstream as ", A2[m-1], " (", A1[m-1], " listeners last week)", sep="")
    return