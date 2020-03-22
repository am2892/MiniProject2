from FileReader import readCSV
import csv
dataSet = readCSV('CSV_files/test.csv')

def varianceSampleProportion(dataSet):
    mean = sum(dataSet) / len(dataSet)
    varianceSampleProportion = sum((xi - mean) ** 2 for xi in dataSet) / (len(dataSet) - 1)

    return varianceSampleProportion

    print("Variance of Sample Proportion is:", varianceSampleProportion)
