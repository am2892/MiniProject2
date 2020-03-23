import math

class PCC:

# PCC = (n*Exy) - (Ex*Ey)/ sqrt((n*Ex2-Ex**2)* (n*Ey2-Ey**2))
    def pcc(CSValuesX,CSValuesY):

        Ex = sum(CSValuesX)
        # The sum of all the values for CSValuesX

        Ey = sum(CSValuesY)
        # The sum of all the values for CSValuesY

        Exy = 0
        # The sum of all the values for CSValuesX time CSValuesY

        Ex2 = 0
        # The sum of all the values for CSValuesX squared

        Ey2 = 0
        # The sum of all the values for CSValuesY squared

        n = len(CSValuesX)
        # the number of numbers in CSValues

        if n != len(CSValuesY):

            cake ='The two data sets that you have entered do not have the same number of numbers.'
            return cake
        else:
            for i in range(len(CSValuesX)):
                Exy += CSValuesX[i]* CSValuesY[i]

                Ex2 += CSValuesX[i] ** 2

                Ey2 += CSValuesY[i] ** 2

            # for loop for getting sums


            Top = 0

            Top = (n*Exy) - (Ex*Ey)

            Bottom = 0

            Bottom = math.sqrt((n*Ex2-Ex**2)* (n*Ey2-Ey**2))

            ans = Top/Bottom

            return ans


#if __name__=="__main__":
#    print(PCC.pcc([5,9,10,12,6,3,4],[1,12,5,3,6,5,7]))

