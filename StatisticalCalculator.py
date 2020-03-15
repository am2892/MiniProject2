# import function to read csv file
from FileReader import readCSV

# import math library
import math

#  get numbers from dataset
dataSet = readCSV('CSV_files/test.csv')

#################################################################################
#################################################################################
#########################   LET USER TEST FUNCTIONS    ##########################
#################################################################################
#################################################################################
choice = ''

print('Select operation!')
print('1.Median')
print('2.Standard Deviation')
print('3.Calculate Z-Score for each Number')

choice = input('Enter choice:')

if choice == "1":
    from Median import median
    print('median: ', str(median(dataSet)))
elif choice == "2":
    from StandardDeviation import standardDeviation
    print('standard deviation: ', str(standardDeviation(dataSet)))
elif choice == "3":
    from zScore import zScore
    print('z-score: ', str(zScore(dataSet)))
else:
    print("(•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ ) something went wrong (•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ )")
