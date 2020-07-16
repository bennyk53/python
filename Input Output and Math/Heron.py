# Ben Koczwara
# Purpose: to create a program that will use Heron's Formula to find the area
# Date: Sept.3,2013

import math 

print "Heron"
print "-----"
print
print "This program will calculate the area of the triangle using Heron's Formulas"
print

again = "y"
while again == "y":
    go = False
    while not go:
        try:
            
            a = float(raw_input("Enter the length of the first side: "))
            b = float(raw_input("Enter the length of the second side: "))
            c = float(raw_input("Enter the length of the third side: "))
            print
            go = True

        except:
            print "You must enter in a number"
            print

    s = (a+b+c)/2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print "The area of the triangle is",round(area,2),"units squared"
    print
    again = raw_input("Would you like to calculate another area? (y/n) ").lower()
    again = again[0]
    print
