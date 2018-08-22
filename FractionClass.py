
# greatest common denominator
def gcd(m,n):     
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n


class Fraction:
    
    # constructor
    def __init__(self, top, bottom):     
        self.num = top     # numerator
        self.den = bottom  # denominator
        
    # string  
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    # addition
    def __add__(self, otherFraction):
        newNum = self.num*otherFraction.den + self.den*otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum,newDen)
        return Fraction(newNum//common,newDen//common)
    
    # subtraction
    def __sub__(self, otherFraction):
        newNum = self.num*otherFraction.den - self.den*otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum,newDen)
        return Fraction(newNum//common,newDen//common)

    # multiplication
    def __mul__(self, otherFraction):
        newNum = self.num*otherFraction.den * self.den*otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum,newDen)
        return Fraction(newNum//common,newDen//common)

    # division
    def __truediv__(self, otherFraction):
        newNum = self.num*otherFraction.den / self.den*otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum,newDen)
        return Fraction(newNum//common,newDen//common)

    # equality
    def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum == secondnum

    # greater than
    def __gt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum > secondnum

    # greater than or even to
    def __ge__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum >= secondnum

    # less than
    def __lt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum < secondnum

    # less than or equal to
    def __gt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum >= secondnum
        
    # not equal to
    def __gt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum != secondnum


# output
x = Fraction(1,4)
y = Fraction(1,2)
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







