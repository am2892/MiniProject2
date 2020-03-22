from FileReader import readCSV
from scipy.stats import sem, t

confidence = 0.95

dataSet = readCSV('CSV_files/test.csv')

def confidenceInterval(dataSet):
    n = len(dataSet)
    m = sum(dataSet) / n
    std_err = sem(dataSet)
    h = std_err * t.ppf((1 + confidence) / 2, n - 1)

    start = m + h
    end = m - h

    return start, end

    print ("Confidence Interval is:", start, end)
