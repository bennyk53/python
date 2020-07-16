# Name: Ben Koczwara
# Date: Oct.15,2103
# Purpose: to create a program that solves a quadratic
import math

def solve(a,b,c):
      try:
            x1 = (-b + (math.sqrt((b**2)-4*a*c)))/(2*a)
            x2 = (-b - (math.sqrt((b**2)-4*a*c)))/(2*a)

            return x1,x2
      except:
            x1 = ""
            x2 = ""
            return x1,x2

print "Solving Quadratic Equations"
print "---------------------------"
print
print "This program will solve your quadratic problems"
print
again = "y"
while again == "y":
      go = False
      while not go:
            try:
                  a = float(raw_input("Enter the value for a: "))
                  b = float(raw_input("Enter the value for b: "))
                  c = float(raw_input("Enter the value for c: "))
                  go = True
            except:
                  print
                  print "You can only enter numbers"
                  print

      x1,x2 = solve(a,b,c)

      if x1 != "" and x2 != "":
            print "The two roots tht solve the equation are:"
            print "x1 =",x1
            print "x2 =",x2
            print

      elif x1 == x2 and x1 != "":
            print "This quadratic only has 1 zero the vertex"
            print "vertex =",x1
      else:
            print "This quadratic equation does not have any real roots"
            print

      run_again = False
      while not run_again:
            again = raw_input("Would you like to run the program again (y/n): ").lower()
            if again != "":
                  run_again = True
            else:
                  print "You must enter something"

      again = again[0]
      print      
