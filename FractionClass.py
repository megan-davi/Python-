# 1.17. Programming Exercises from Problem Solving with
#    Algorithms and Data Structures using Python
# Exercises 1 - 9

class Fraction:
    
    # constructor
    def __init__(self, top, bottom):
        
        # check to see if inputs are integers
        if isinstance(top, int):
            self.num = top
        else:
            raise ValueError("Numerator is not an integer.")
            
        if isinstance(bottom, int):
            self.den = bottom
        else:
            raise ValueError("Denominator is not an integer.")
        
        if isinstance(bottom, 0):
            self.den = bottom
        else:
            raise ValueError("The denominator cannot be zero.")

        common = gcd(self.num,self.den)   # apply gcd function
        self.num = self.num//common       # numerator
        self.den = self.den//common       # denominator
        
    # string  
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    # addition
    def __add__(self, otherFraction):
        newNum = self.num * otherFraction.den + self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        return Fraction(newNum, newDen)
    
    # subtraction
    def __sub__(self, otherFraction):
        newNum = self.num * otherFraction.den - self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        return Fraction(newNum,newDen)

    # multiplication
    def __mul__(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den
        return Fraction(newNum, newDen)

    # division
    def __truediv__(self, otherFraction):
        newNum = self.num * otherFraction.den
        newDen = self.den * otherFraction.num
        return Fraction(newNum,newDen)

    # equality
    def __eq__(self, otherFraction):
         firstNum = self.num * otherFraction.den
         secondNum = otherFraction.num * self.den
         return firstNum == secondNum

    # greater than
    def __gt__(self, otherFraction):
         firstNum = self.num * otherFraction.den
         secondNum = otherFraction.num * self.den
         return firstNum > secondNum

    # greater than or even to
    def __ge__(self, otherFraction):
         firstNum = self.num * otherFraction.den
         secondNum = otherFraction.num * self.den
         return firstNum >= secondNum

    # less than
    def __lt__(self, otherFraction):
         firstNum = self.num * otherFraction.den
         secondNum = otherFraction.num * self.den
         return firstNum < secondNum

    # less than or equal to
    def __le__(self, otherFraction):
         firstNum = self.num * otherFraction.den
         secondNum = otherFraction.num * self.den
         return firstNum <= secondNum
        
    # not equal to
    def __ne__(self, otherFraction):
         firstNum = self.num * otherFraction.den
         secondNum = otherFraction.num * self.den
         return firstNum != secondNum


# greatest common denominator
def gcd(m,n):     
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n



# output
x = Fraction(1,1)
y = Fraction(1,0)
print("The first fraction is",x)
print("The second fraction is", y)
print ("\n")
print("Added:", x + y)
print("Subtracted:", x - y)
print("Multiplied:", x * y)
print("Divided:", x / y)
print("\n")
print("First fraction is greater than second?", x > y)
print("First fraction is less than second?", x < y)
print("First fraction is greater than or equal to second?", x >= y)
print("First fraction is less than or equal to second?", x <= y)
print("First fraction is equal to second?", x == y)
print("First fraction is not equal to second?", x != y)









