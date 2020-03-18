from FileReader import readCSV

dataSet = readCSV('CSV_files/test.csv')


def variancePopulationProportion(dataSet):
        mean = sum(dataSet) / len(dataSet)
        populationProportion = 1 / len(dataSet)
        variance = sum((xi - mean) ** 2 for xi in dataSet) / (len(dataSet) - 1)

        return variance

print("Variance of Population Proportion is:", variance)
