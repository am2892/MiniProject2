from FileReader import readCSV
from scipy.stats import sem, t
from scipy import mean
confidence = 0.95

dataSet = readCSV('CSV_files/test.csv')

def confidenceInterval(dataSet):
        n = len(dataSet)
        m = mean(dataSet)
        std_err = sem(dataSet)
        h = std_err * t.ppf((1 + confidence) / 2, n - 1)

        start = m + h

return start

print ("Confidence Interval is:", start)
