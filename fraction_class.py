import math

class Fraction : 

    def __init__(self, top, bottom) :
        self.num = top
        self.denom = bottom


    def __str__(self) :
        return "Fraction = "+str(self.num)+"/"+str(self.denom)


    def __add__(self, fr2) :
        self.num = self.num*fr2.denom + self.denom*fr2.num
        self.denom = self.denom * fr2.denom
        common = Fraction.gcd(self.num, self.denom)
        
        return Fraction(round(self.num/common), round(self.denom/common))   


    def show(self) :
        print("Fraction = ",self.num,"/",self.denom)


    def gcd(m, n) :
        while m%n != 0 :
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn

        return n


fr1 = Fraction(1,4)
fr2 = Fraction(1,2)
print(fr1+fr2)
