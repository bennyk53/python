# Name: Ben Koczwara
# Date: Sept.16,2013
# Purpose: to create a program that will count the number of vowels and consonants

print "Letter Counter"
print "--------------"
print
print "This program will count the number of vowels and consonants"
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

      counter = word.lower()
      v_counter = 0
      c_counter = 0

      for x in counter:
            if x.isalpha():
                  if x in ["a","e","i","o","u","y"]:
                        v_counter += 1
                  else:
                        c_counter += 1

      print "The phrase '"+str(word)+"' has",v_counter,"vowels and",c_counter,"consonants"
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


