import math
class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        return num1 / num2
    def square(self, num1):
        return num1 ** 2
    def squareroot(self, num1):
        return math.sqrt(num1)
#    def mean(self, num1, num2):
#        return statistics.mean(num1, num2)
if __name__ == "__main__":
    c = Calculator()
    print (c.add(1,2))
    print (c.subtract(1,2))
    print (c.multiply(1,2))
    print (c.divide(1,2))
    print (c.square(1))
    print (c.squareroot(1))
#    print (c.mean(1,2))
