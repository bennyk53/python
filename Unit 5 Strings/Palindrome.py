# Name: Ben Koczwara
# Date: Sept.16,2013
# Purpose: to create a program that will test if the word is a palindrome

print "Palindrome"
print "----------"
print
print "A palindrome is a word spelt the same forward as it is backwards"
print "This program will determine if the word is a palindrome"
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
            

      palindrome = word.lower()

      if palindrome.isalpha() == False:
            for letter in palindrome:
                  if letter.isalpha() == False:
                        palindrome = palindrome.replace(letter,"")

      if palindrome != "":

            if palindrome == palindrome[::-1]:
                  print word,"is a palindrome"

            else:
                  print word,"is not a palindrome"
      else:
            print word,"is not a palindrome"

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

      
