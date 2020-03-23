import math


class PSD:
#Population Standard Deviation

# o=(sumof([x-u]^2/N)^{1/2})
# o = is the popution standard deviation
# x = is an individual value
# u = is the average of the population
# N = is the total number of the population

    def psd(CSValues):
        # CSVlues are supost to be the values that are given
        u = 0
        #This is the Mean

        Top = 0
        # This is the top half of the equation

        Set = 0
        # This the bottom half of the equation

        Ans = 0
        # This is the Answer

        u = sum(CSValues)/len(CSValues)
        #print(u)

        for i in CSValues:
            Top +=(i-u)**2

        #print(Top)
        Set = Top/len(CSValues)

        #print(Set)
        Ans = math.sqrt(Set)

        return Ans

#if __name__=="__main__":
#    print(PSD.psd([5,9,10,12,6,3,4]))

# Used https://www.calculator.net/standard-deviation-calculator.html?numberinputs=5%2C9%2C10%2C12%2C6%2C3%2C4&ctype=p&x=61&y=24
# to check is answer provided was correct

