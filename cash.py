#Print out how many coins cashier should give customer for the rest.

import sys

x = (input("Change:"))

try:
    float(x)
    print("correct input")
except:
    print("Digits only")
    sys.exit
#
y = float(x)
q = (y - (y % 25)) / 25
print("Quarter quantity:",q)

a = y - (25*q)
n = (a - (a%10)) / 10
print("Dimes quantity:",n)

b = y - (25*q) - (10*n)
#print(b)

c = (b - (b%5)) / 5
print("Nickels quantity:",c)

e = y - (25*q) - (10*n) - (5*c)
p = (e - (e%1)) / 1
print("Pennies quantity:",p)

z = q + n + c + p
print("Total coins:",z)