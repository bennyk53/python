# Name: Ben Koczwara
# Date: Oct.15,2103
# Purpose: to create a program that returns the lowest prime factor of a number

def Factor(number):
      x = 2
      while x != number:
            if number%x == 0:
                  y = 2
                  while x != y :
                        if x%y == 0 and y != 2:
                              y += 1
                        else:
                              return y
            x += 1
            
            

print "Smallest Factor"
print "---------------"
print
print "This program finds the smallest prime factor of a number"
print
again = "y"
while again == "y":
      go = False
      while not go:
            try:
                  
                  number = int(raw_input("Enter the number you wish to find the smallest prime factor for: "))
                  print
                  go = True
            except:
                  print
                  print "You can only enter whole numbers"
                  print 

      factor = Factor(number)

      if factor == None:
            factor = number
      print "The smallest prime factor of",number,"is",factor
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
