from FileReader import readCSV
import math

dataSet = readCSV('CSV_files/test.csv')


def sampleMean(dataSet):
        shortendDataSet = dataSet[0:5]
        smean = sum(dataSet) / len(dataSet)

        return smean

        print("Sample mean is:", smean)
