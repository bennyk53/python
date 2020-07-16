# Name: Ben Koczwara
# Date: Sept.13,2013
# Purpose: to create a program that will make a list of 1000 values and find the number entered

import random
print "Random Numbers"
print "--------------"
print
print "This program will create a list of 1000 integers from 1 to 100. When"
print "you enter a number between 1 and 100 it will tell you where it is in the list"
print
again = "y"
while again == "y":
    values = []
    for x in range(0,1000):
        num = random.randint(1,100)
        values.append(num)
        
    number = -3
    while number < 1 or number > 100:
        try:
            number = int(raw_input("Enter a number you would like to search for: "))
            print
        except:
            number = 101
        

    look = True
    location = [] 
    while look :
        try:
            found =  values.index(number)
            location.append(found)
            values.remove(number)
        except:
            look = False
            again = "F"

    if len(location) == 1:
        p = "position:"
    else:
        p = "positions:"
        
    if len(location) > 0:
        print "Number",number,"occurs",len(location),"times at",p
        for x in location:
            print x,
        print
        print
    else:
           print number,"did not occur in the list"
           print

    run_again = False
    while not run_again:
        again = raw_input("Would you like to run the program again? (y/n): ").lower()
        print
        if again != "":
                run_again = True
        else:
            print "You must enter something"
            print

    again = again[0]




    
