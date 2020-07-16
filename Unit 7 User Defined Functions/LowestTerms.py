# Name: Ben Koczwara
# Date: Oct.16,2103
# Purpose: to create a program that will determine a fractions lowest possible form'
from fractions import Fraction

def GCD(n,d):
      if n > d:
            num = n/d
            n -= (num*d)
            fraction = Fraction(n,d)
      else:
            num = 0
            fraction = Fraction(n,d)
            
      return num,fraction

print "Lowest Terms"
print "------------"
print
print "This program will reduce a fraction to lowest terms"
print
again = "y"
while again == "y":
      go = False
      while not go:
            try:
                  n = int(raw_input("Enter the numerator of the fraction: "))
                  d = int(raw_input("Enter the denominator of the fraction: "))
                  print
                  go = True
            except:
                  print
                  print "You can only enter whole numbers"
                  print

      num,fraction = GCD(n,d)

      if fraction == 0:
            print "The fraction",str(n)+"/"+str(d),"reduces to",num

      else:
            if num != 0:
                  print "The fraction",str(n)+"/"+str(d),"reduces to",num,fraction
            else:
                  print "The fraction",str(n)+"/"+str(d),"reduces to",fraction
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
