from FileReader import readCSV
import math

dataSet = readCSV('CSV_files/test.csv')

def populationMean(dataSet):
        mean = sum(dataSet) / len(dataSet)

        return mean

print("Population mean is:", mean) 
