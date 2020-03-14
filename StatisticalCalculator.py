# import function to read csv file
from FileReader import readCSV

# import math library
import math

#  get numbers from dataset
dataSet = readCSV('CSV_files/test.csv')

# import functions from other files
from StandardDeviation import standardDeviation
from Median import median


#################################################################################
#################################################################################
#########################   LET USER TEST FUNCTIONS    ##########################
#################################################################################
#################################################################################
choice = ''

print('Select operation!')
print('1.Median')
print('2.Standard Deviation')

choice = input('Enter choice:')

if choice == "1":
    print('median: ', str(median(dataSet)))
elif choice == "2":
    print('standard deviation: ', str(standardDeviation(dataSet)))
else:
    print("(•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ ) something went wrong (•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ )")
