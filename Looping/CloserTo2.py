# Name: Ben Koczwara
# Date: Sept.11,2013
# Purpose: to create a program that will determine if the number is prime or not

print "Closer to 2"
print "-----------"
print
print "This program uses a loop to demonstrate that the result of adding"
print "the numbers 1/1, 1/2, 1/4, 1/8, 1/16, ... and so on gets closer and"
print "closer to 2 without becoming 2."
print
again = True
while again:
      go = False
      while not go:
            
            fraction = int(raw_input("Enter the number of fractions you wish to see: "))
            print
            if fraction > 0:
                  go = True
            else:
                  print "The number must be greater than or equal to 1"
                  print

      count = 1
      x = 1
      z = float(0)
      while count <= fraction:
            print z,"+ 1/"+str(x),"=",(z+(1/float(x)))

            z = ((2-z)/2)+z
            x *= 2
            count += 1
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

      if again[0] == "n":
            again = False
            
