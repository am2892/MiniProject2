from FileReader import readCSV
import math

dataSet = readCSV('CSV_files/test.csv')

def standardizedScore(dataSet):
    mean = sum(dataSet) / len(dataSet)
    std = math.sqrt(sum((val - mean) ** 2 for val in dataSet))/(len(dataSet))

    scores = []

    for num in dataSet:
        standardizedScore = (num - mean)/std
        scores.append(standardizedScore)
    return scores

    print("Standardized Scores of dataset:", standardizedScore(dataSet))
