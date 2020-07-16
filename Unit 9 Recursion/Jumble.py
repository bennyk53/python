# Name: Ben Koczwara
# Date: Oct.29,2013
# Purpose: to find all the possible combinations of a string of characters

import math

def jumble(string,combo):
      if not(string):
            print combo,
      else:
            for x in range(len(string)):
                  jumble(string[:x]+string[x+1:],combo+string[x])

print "Jumble"
print "------"
print
print "This program will determine all the combinations of a string of characters"
print
again = "y"
while again == "y":
      combo = ''

      string = raw_input("Enter a string of characters: ")

      jumble(string,combo)
      print
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
