# Name: Ben Koczwara
# Date: Sept.11,2013
# Purpose: to create a program that will determine if the number is prime or not

print "Prime Number Calculator"
print "-----------------------"
print
print "This program will tell you if a number is a prime number or not"
print
again = "y"
while again == "y":
      nxt = False
      while not nxt:
            try:
                  number = int(raw_input("Enter the number to determine if it is prime: "))
                  print
            except:
                  number = 0
            if number > 0:
                  nxt = True
            else:
                  print "You must enter a positive integer"
                  print

      x = 2
      values = []
      while x <= (number-1):
            if (float(number) / float(x)) == (number/x):
                  values.append(x)

            x+=1

      if len(values) > 0:
            print number,"is NOT a prime number. It is evenly divisible by",
            for items in values:
                  if values.index(items)== (len(values)-1):
                        print str(items)+"."
                  else:
                        print str(items)+",",

      elif number == 1:
            print number,"is NOT a prime number, it is a special case"
      else:
            print number,"is a prime number"

      print
                  
      run_again = False
      while not run_again:
            again = raw_input("Would you like to run the program again? (y/n): ")
            print
            if again != "":
                  run_again = True
            else:
                  print "You must enter something"
                  print
