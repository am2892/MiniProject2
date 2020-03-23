import math

from FileReader import readCSV

dataSet = readCSV('CSV_files/test.csv')


def pcc(dataSet):

    dataSet.pop()
    dataSetX = dataSet[9:18]
    dataSetY = dataSet[0:9]

    Ex = sum(dataSetX)
    Ey = sum(dataSetY)
    Exy = 0
    Ex2 = 0
    Ey2 = 0
    n = len(dataSetX)

    if n != len(dataSetY):
        cake ='The two data sets that you have entered do not have the same number of numbers.'
        return cake
    else:
        for i in range(len(dataSetX)):
            Exy += dataSetX[i]* dataSetY[i]
            Ex2 += dataSetX[i] ** 2
            Ey2 += dataSetY[i] ** 2

        Top = 0
        Top = (n*Exy) - (Ex*Ey)
        Bottom = 0
        Bottom = math.sqrt((n*Ex2-Ex**2)* (n*Ey2-Ey**2))
        ans = Top/Bottom
        return ans

print(pcc(dataSet))


