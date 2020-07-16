# Ben Koczwara
# Purpose: to create a program that will use sine law
# Date: Sept.3,2013

import math
print "Sine Law"
print "--------"
print
print "This program will help you determine your missing values"
print
again = "y"

while again == "y":
    wrong = True
    go = False
    while not go:
        try:
            a = float(raw_input("Enter the length of side a: "))
            print
            go = True
        except:
            print "You must enter a number"
            print
    while wrong:
        try:
            A = float(raw_input("Enter the value of angle A in degrees: "))
            B = float(raw_input("Enter the value of angle B in degrees: "))
            print

            if A + B >= 180:
                print "Your angles are too large"
            else:
                wrong = False
        except:
            print "You must enter a number"
            print
            
    angleC = 180 - (A + B)

    A = math.radians(A)
    B = math.radians(B)
    C = math.radians(angleC)

    sinA = math.degrees(math.sin(A))
    sinB = math.degrees(math.sin(B))
    sinC = math.degrees(math.sin(C))

    b = (a*sinB)/sinA
    c = (b*sinC)/sinB

    print "Side b is",round(b,2),"units long, side c is",round(c,2),"units long."
    print "Angle C has a value of",angleC
    print
    again = raw_input("Would you like to calculate some more missing values? (y/n) ").lower()
    again = again[0]
    print
