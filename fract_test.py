from fractions import Fraction
import copy

def print_and_test(frac1, frac2):
    f1 = copy.deepcopy(frac1)
    f2 = copy.deepcopy(frac2)
    print("First: ", frac1, "\t", "Second: ", frac2)
    print("+\t= ", frac1 + frac2)
    print("-\t= ", f1 - f2)
    print("")

#Same
print_and_test(Fraction(1, 1), Fraction(1, 1))
print_and_test(Fraction(1, 2), Fraction(1, 2))

#To mult
print_and_test(Fraction(1, 3), Fraction(1, 2))

#Neg
print_and_test(Fraction(1, 2), Fraction(-1, -2))
print_and_test(Fraction(1, -2), Fraction(1, 2))

#Zero
print_and_test(Fraction(0, -2), Fraction(1, 2))
print_and_test(Fraction(0, 0), Fraction(1, 2))
