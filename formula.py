import numpy as np

def getScore(avg):
    result = 12.4619 * np.log(avg) - 67.0731
    return result