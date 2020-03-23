import math

from FileReader import readCSV
dataSet = readCSV('CSV_files/test.csv')

def populationStandardDeviation(dataSet):
    # CSVlues are supposed to be the values that are given
    u = 0
    #This is the Mean
    Top = 0
    # This is the top half of the equation
    Set = 0
    # This the bottom half of the equation
    Ans = 0
    # This is the Answer
    u = sum(dataSet)/len(dataSet)

    for i in dataSet:
        Top +=(i-u)**2

    Set = Top/len(dataSet)

    Ans = math.sqrt(Set)

    return Ans

print("Population standard deviation: ", psd(dataSet))

