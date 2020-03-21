import math
from FileReader import readCSV
dataSet = readCSV('CSV_files/test.csv')
testData = [1,2,3]


def test_csv_reader():
    dataSet = readCSV('CSV_files/test.csv')
    assert len(dataSet) == 19 * 2

def test_csv_reader_fail():
    dataSet = readCSV('CSV_files/test.csv')
    assert len(dataSet) != 19

def test_calc_median():
    from Median import median
    assert median(testData) == 2

def test_calc_median_fail():
    from Median import median
    assert median(testData) != 1

def test_calc_variance():
    from Variance import variance
    assert variance(dataSet) == 79346

def test_calc_variance_fail():
    from Variance import variance
    assert variance(dataSet) != 2

def test_calc_std():
    from StandardDeviation import standardDeviation
    assert standardDeviation(dataSet) == standardDeviation(dataSet)

def test_calc_std_fail():
    from StandardDeviation import standardDeviation
    assert standardDeviation(dataSet) != 2
