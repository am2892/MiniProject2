from FileReader import readCSV 
import math

#open dataset:
dataSet = readCSV('CSV_files/test.csv')

def mode(dataSet):

    #define length of dataSet
    n = len(dataSet)

    #set up array that displays frequency of each data point:
    getMode = {}

    for l in dataSet:
        getMode[l] = getMode.get(l,0) + 1

    #find highest frequency
    maxValue = max(list(getMode.values()))
    modeValue = [a for a, v in getMode.items() if v == maxValue]

    if len(modeValue) == n:
        getMode = "No mode within given dataset"
    else:
        getMode = "Mode is / are: " + ', '.join(map(str, modeValue))

    print getMode
