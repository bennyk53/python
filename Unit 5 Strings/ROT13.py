# Name: Ben Koczwara
# Date: Sept.16,2013
# Purpose: to create a program that will encrypt a message

print "ROT13"
print "-----"
print
print "This program will encrypt a message"
print
again = "y"
while again == "y":
      go = False
      while not go:
            
            word = raw_input("Enter a word or phrase: ")
            print

            if word != "":
                  go = True
            else:
                  print "You must enter something"
                  print
      code = ""
      for x in word:
            if x.isalpha():
                  if x.isupper():
                        num = ord(x)
                        num += 13
                        if num > 90:
                              extra = num - 90
                              num = 64 + extra
                  elif x.islower():
                        num = ord(x)
                        num += 13
                        if num > 122:
                              extra = num - 122
                              num = 96 + extra

                  
                  letter = chr(num)
                  code += letter

            else:
                  code+= x

      print "The encrypted phrase is:",code
            
            
      run_again = False
      while not run_again:
            again = raw_input("Would you like to run the program again (y/n): ").lower()
            if again != "":
                  run_again = True
            else:
                  print "You must enter something"

      again = again[0]
      print
