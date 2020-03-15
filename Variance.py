# import our readCSV file so we can read the csv
from FileReader import readCSV
import math

# dataSet = readCSV('CSV_files/test.csv')
# print('dataSet: ', dataSet)

def variance(dataSet):
    # calculate mean
    mean = sum(dataSet) / len(dataSet)

    # calculate variance of list
    variance = sum((xi - mean) ** 2 for xi in dataSet) / len(dataSet)
    return variance
    # print('variance: ', variance)

# variance(dataSet)