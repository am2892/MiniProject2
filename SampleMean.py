from FileReader import readCSV
import math

dataSet = readCSV('CSV_files/test.csv')

read_csv(..., nrows=10)

def sampleMean(dataSet):
        smean = sum(dataSet) / len(dataSet)

        return smean

print("Sample mean is:", smean)
