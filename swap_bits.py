import sys

nb = int(input("Entrer un nombre tel que : 0 <= nb <= 255 \n"))
nb = nb % 256

print("before {0:08b}".format(nb))
sol = ((nb & 0b11110000) >> 4) | ((nb & 0b00001111) << 4)
print("after  {0:08b}".format(sol))

