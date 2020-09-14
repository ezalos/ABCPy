class Fraction:
    def __init__(self, num=1, den=1):
        if den == 0:
            print("Error den cant be 0. Has been replaced by 1")
            den = 1
        self.num = num
        self.den = den
        if (den < 0 and num < 0) or den < 0:
            self.mult_by(-1)

    def mult_by(self, n):
        self.num *= n
        self.den *= n

    def __add__(self, other):
        if type(other) == type(Fraction()):
            if self.den != other.den:
                den = self.den
                self.mult_by(other.den)
                other.mult_by(den)
            num = self.num + other.num
            den = self.den
            return(Fraction(num, den))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) == type(Fraction()):
            other.num *= -1
            return self.__add__(other)

    def __rsub__(self, other):
        return other.__sub__(self)

    def __str__(self):
        return (str(self.num) + '/' + str(self.den))

