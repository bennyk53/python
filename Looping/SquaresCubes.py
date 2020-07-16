# Name: Ben Koczwara
# Date: Sept.9,2013
# Purpose: To create a program that will find the square,square root and the cube of numbers
import math

print "MATH CLASS"
print "----------"
print
print "This program will find the squares, square roots and cubes of numbers in a range"
print
again = "y"
while again == "y":
      done = False
      while not done:
            try:
                  lower = int(raw_input("Enter the lower number (must be a whole number): "))
                  upper = int(raw_input("Enter the higher number (must be a whole number): "))
                  print

                  if upper >= lower:
                        done = True
                        
                  else:
                        print "The first number must be lower than the second" 
                        print
                  
            except:
                  print "Both numbers must be whole "
                  
      print "Number".rjust(7),"Square".rjust(7),"Square Root".rjust(12),"Cube".rjust(7)

      for x in range(lower,upper+1):
            print str(x).rjust(7),

            square = x **2
            print str(square).rjust(7),

            square_root = math.sqrt(x)
            print str(round(square_root,4)).rjust(12),

            cube = x**3
            print str(cube).rjust(7)
      
      print
      
      a = False
      while not a:
            again = raw_input("Would you like to run the program again (y/n): ").lower()

            if again != "":
                  again = again[0]
                  a = True
                  print


