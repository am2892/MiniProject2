# import our readCSV file so we can read the csv
from FileReader import readCSV
import math

# dataSet = readCSV('CSV_files/test.csv')

def zScore(dataSet):
    mean = sum(dataSet) / len(dataSet)
    std = math.sqrt(sum([(val - mean)**2 for val in dataSet])/(len(dataSet) - 1))

    for num in dataSet:
        # calculates the z-score of each number in the dataset
        zScore = (num - mean)/std
        print("z-score of", num, "=", zScore)

# if you want to test the output of this file specifically just uncomment the file below
# zScore(dataSet)