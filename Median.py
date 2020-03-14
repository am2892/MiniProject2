# import our readCSV file so we can read the csv
from FileReader import readCSV

dataSet = readCSV('CSV_files/test.csv')

def median(dataSet):
    listLength = len(dataSet)
    sortedList = sorted(dataSet)
    index = (listLength - 1) // 2
    if (listLength % 2):
        return sortedList[index]
    else:
        return (sortedList[index] + sortedList[index + 1])/2.0

# if you want to test the output of this file specifically just uncomment the file below
# print('median: ', str(median(dataSet)))
