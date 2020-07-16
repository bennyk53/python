# Name: Ben Koczwara
# Date: Sept.9,2013
# Purpose: To create a program that will find the sum of a group of numbers

print "Sum of Numbers"
print "--------------"
print
print "This program will calculate the sum of a group numbers"
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

      total = 0
      for x in range(lower,upper+1):
            if x != upper:
                  print x,"+",
            else:
                  print x,"=",

            total += x

      print total
      print

      a = False
      while not a:
            again = raw_input("Would you like to run the program again (y/n): ").lower()

            if again != "":
                  again = again[0]
                  a = True
                  print
