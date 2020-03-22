# import our readCSV file so we can read the csv
from FileReader import readCSV
import math

dataSet = readCSV('CSV_files/test.csv')

def standardDeviation(dataSet):
    mean = sum(dataSet) / len(dataSet)
    std = math.sqrt(sum([(val - mean)**2 for val in dataSet])/(len(dataSet) - 1))

    return std

# if you want to test the output of this file specifically just uncomment the file below
# print('standard deviation: ', str(standardDeviation(dataSet)))
