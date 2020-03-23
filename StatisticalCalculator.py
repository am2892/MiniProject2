# coding: utf-8
# import function to read csv file
from FileReader import readCSV

# import math library
import math

#from scipy import sem, t
#  In order to calculate two of these functions, scipy must be imported

#  get numbers from dataset
dataSet = readCSV('CSV_files/test.csv')

#################################################################################
#################################################################################
#########################   LET USER TEST FUNCTIONS    ##########################
#################################################################################
#################################################################################
choice = ''

print('Select operation!')
print('1.Population Mean')
print('2.Median')
print('3.Mode')
print('5.Variance of Population Proportion')
print('6.Calculate Z-Score for each Number')
print('9.Confidence Interval')
print('10.Calculate Population Variance')
print('13.Sample Mean')
print('14.Standard Deviation')

choice = input('Enter choice:')

if choice == "1":
    from StatisticsModule import populationMean
    print('population mean: ', str(populationMean(dataSet)))
elif choice == "2":
    from StatisticsModule import median
    print('median: ', str(median(dataSet)))
elif choice =="3":
    from StatisticsModule import mode
    print('mode(s): ', str(mode(dataSet)))
elif choice == "5":
    from StatisticsModule import variancePopulationProportion
    print('variance of population proportion: ', str(variancePopulationProportion(dataSet)))    
elif choice == "6":
    from StatisticsModule import zScore
    print('z-score: ', str(zScore(dataSet)))
elif choice == "9":
    from StatisticsModule import confidenceInterval
    print('confidence interval: ', str(confidenceInterval(dataSet)))    
elif choice == "10":
    from StatisticsModule import variance
    print('variance: ', str(variance(dataSet)))
elif choice == "13":
    from StatisticsModule import sampleMean
    print('sample mean: ', str(sampleMean(dataSet)))    
elif choice == "14":
    from StatisticsModule import standardDeviation
    print('standard deviation: ', str(standardDeviation(dataSet)))    
else:
    print("(•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ ) something went wrong (•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ )")
