from FileReader import readCSV

dataSet = readCSV('CSV_files/test.csv')

def variancePopulationProportion(dataSet):
        mean = sum(dataSet) / len(dataSet)
        populationProportion = 1 / len(dataSet)
        print('populationProportion: ', populationProportion)
        if populationProportion != 0:
            variance = sum((xi - mean) ** 2 for xi in dataSet) / populationProportion
        else:
            variance = 0            

        return variance

        print("Variance of Population Proportion is:", variance)

variancePopulationProportion(dataSet)